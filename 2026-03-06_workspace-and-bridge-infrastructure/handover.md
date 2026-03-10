# Handover Document
**Topic:** ワークスペース基盤 + Slack↔CCブリッジ — tmux/sesh/cmux統合管理
**Date:** 2026-03-10
**Status:** 進行中（3/10 workspaces.json dotfiles移行完了・tmux自動アタッチ暴走修正完了・rebuild-cmux.sh手動実行に一本化）

---

## 背景

macOSのSpacesを**16個**使用し、**1 Space = 1プロジェクト**として運用してきた。根底にある欲求は「タスクを忘れたくない」「同時進行したい」。cmux導入（2026-03-02）で全ターミナルが1ウィンドウに統合された結果、16 Spaces に Chrome/Finder を分散する意味が薄れた。

並行して、Claude CodeのSlack経由リモート操作を実現するため、Slack↔cmuxブリッジを構築（3/3〜）。UUIDベースルーティング、マルチタブ対応、クロスポスト、スレッド返信を実装し双方向通信を確立。しかしcmux APIの癖（3 RPC、\rハック、UUIDオンザフライ解決、ソケット断続切れ）が深刻で、tmux全面移行を決定（3/5）。cmuxはGUI、tmuxはデータ転送と役割分離する方針。

3/6にブリッジをtmux send-keysに書き換え、LaunchAgentで自動起動化を完了。E2Eテスト通過。Spaces再構築はマルチAIブレスト（Gemini+Claude）で5提案→P1完了、P2/P3は今後。

---

## 現在の状況

### tmux + sesh ワークスペース管理

#### cmuxとtmuxの関係
- cmux (manaflow-ai) はtmuxとは**完全に独立した実装**（Swift/AppKit + libghostty）
- 同名のCLIラッパー「cmux」（tmux fuzzy finder）は別物で、広く使われているものはない

#### tmuxセットアップ
- tmux 3.6a (Homebrew), prefix: `Ctrl+A`（cmuxと**競合なし**確認済み）
- TPM + tmux-sensible + tmux-resurrect + tmux-continuum（自動保存ON、**自動復元OFF** — 3/10変更）
- vim風キーバインド（hjkl）、TrueColor対応済み

#### sesh（tmuxセッションfuzzy switcher）
- sesh v2.24.2（Go製、`brew install sesh`）
- `~/.tmux.conf` に `prefix + T` でfzf連携UIを追加済み

#### 運用パターン（3/10改訂）
- **cmuxペイン起動時の自動tmuxアタッチは無効化済み**（config.fish コメントアウト）
- cmux再起動後は `rebuild-cmux.sh` で手動アタッチ（唯一の正式手段）
- cmuxが落ちても `tmux attach` で完全復帰（検証済み: タブクローズ→別タブからattach成功）
- CC内から `!tmux detach` でCCを終了せずにdetach可能
- `Ctrl+A → T` でseshのfuzzyセッション切り替え

#### tmux 全面移行 Phase 進捗

| Phase | 内容 | ステータス |
|-------|------|-----------|
| 1 | sesh.toml 作成（24セッション定義） | 完了 |
| 2a | tmux session 一括作成（24個 + claude起動） | 完了 |
| 2b | cmux ペインを tmux に接続 | 完了（3/6確認: 26session中23個attached） |
| 3 | ブリッジを tmux send-keys に切替 | 完了（3/6） |
| 4 | LaunchAgent で自動起動 | 完了（3/6） |
| 5 | E2E テスト | 完了（3/6 Slack→tmux→CC送受信確認） |
| 6 | tmux-resurrect/continuum インストール | 完了（3/7） |
| 7 | ソケットパス永続化 (`TMUX_TMPDIR=~/.tmux/sockets`) | 完了（3/7） |
| 8 | ゴーストサーバー検知 | 完了（3/7） |

#### tmux セッション消失 & デュアルサーバー事故（3/7）
- **症状:** `$list` が1セッションしか返さない、ブリッジが不完全
- **根本原因:** macOS Sleep 時に `/tmp/tmux-503/default` ソケットがクリーンアップされた。旧サーバーはプロセスとして生存（既存接続維持）するが新ソケットは新サーバーが作成→デュアルサーバー
- **再発防止（3点セット）:**
  1. `TMUX_TMPDIR=~/.tmux/server` — ソケットを `/tmp` から永続パスに移動（3/8にcmux named pipesとの分離のため `sockets` → `server` に変更）
  2. ゴーストサーバー検知 — `/tmp` ソケットのサーバーのみ kill（`~/.tmux/server` は保護）
  3. tmux-resurrect/continuum — セッション内容の自動保存・復元
- **notify_pipe / ブリッジログも `/tmp` → `~/.tmux/sockets/` に移動**
- 詳細: `notes/tmux-session-recovery-2026-03-07.md`

#### tmux自動アタッチ暴走の根本原因と修正（3/10 NEW）
- **症状:** Mac再起動/cmux再起動のたびにtmuxが暴走（セッション二重化、claude多重起動、制御衝突）
- **根本原因（5段階の連鎖）:**
  1. cmux起動 → 24ペインのfish shellが同時に `cmux_tmux_attach` を実行（config.fish L85-89）
  2. 24個の `sesh connect` が並行 → tmuxセッション一斉作成 + claude起動
  3. tmux-continuum の `@continuum-restore 'on'` が前回の24セッションを復元 → sesh作成分と二重存在
  4. rebuild-cmux.sh も `sesh connect` を送信 → さらに三重起動
  5. bridge.js (LaunchAgent) が5秒ポーリングで復活セッションを即検出
- **修正（3/10適用）:**
  1. `config.fish` の自動アタッチをコメントアウト（24並行sesh connect停止）
  2. `.tmux.conf` の `@continuum-restore` を `off` に変更（二重復元停止）
  3. tmuxアタッチは `rebuild-cmux.sh` で手動制御に一本化
- 詳細: `notes/tmux-auto-attach-investigation-2026-03-10.md`

#### cmux再起動によるCC全Kill事象（3/8）
- **症状:** cmux再起動時、CCが「システムがヤバい」と言い残して全プロセスをKillして消えた
- **根本原因:** cmux再起動 → PTY全破壊 → SIGHUPカスケード → fish → sesh → tmux client → CC 全滅
- **追加問題:** tmuxソケット (`~/.tmux/sockets/tmux-503/default`) も消失。cmux再起動時にnamed pipes (cmux-notify-*) をリクリエイトする際、同ディレクトリのtmuxソケットも巻き添え消失
- **プロセス残骸:** 孤立tmux server (PID 3328, ソケットなし) + stopped sesh×6 + stopped fish通知ウォッチャー×9 + 多重attach×5
- CCの「ヤバい」= PTY切断検知による正常なgraceful shutdown。CC側の問題ではない
- 詳細: `notes/cmux-restart-behavior-2026-03-08.md`

### Slack↔CC 双方向通信（tmux版で動作確認済み）

**User → CC:**
- `$6 テスト` → tmux session `6-1` に送信
- `$6:2 テスト` → tmux session `6-2`
- `$list` → WS一覧（cmux名 + タブ数付き）
- `$list:6` → WS6 のセッション一覧
- `$all テスト` → 全WSのfirst tabに一斉送信

**CC → User:**
- Asana Workflow → Slack bot名義通知
- Slack Webhook 即時通知
- `📱 [Slack:N:TS]` → `🤖 [WSN]` スレッド返信クロスポスト

### ブリッジ技術（tmux send-keys）

```typescript
// テキスト送信と Enter を分離（-- フラグが Enter キー解釈を妨げるため）
execSync(`tmux send-keys -t '${sessionName}' -- '${escaped}'`);
execSync(`tmux send-keys -t '${sessionName}' Enter`);
```
- cmux RPC 約200行 → tmux send-keys 約60行に簡素化
- UUID解決不要、ソケット接続不要
- WS_NAMES マッピングで cmux と同じワークスペース名を `$list` に表示
- セパレータ `:` と `-` の両対応（`$6:2` / `$6-2` どちらでもOK）

### LaunchAgent 自動起動

- plist: `~/Library/LaunchAgents/com.saitshug.claude-slack-bridge.plist`
- `KeepAlive: true` + `RunAtLoad: true` + `ThrottleInterval: 10`
- PATH に `/opt/homebrew/bin` を含める必要あり（tmux コマンド用）
- ログ: `/tmp/claude-slack-bridge.log`, `/tmp/claude-slack-bridge.error.log`

### cmux（GUIとして残存）

#### 課題: cmux導入後のSpaces形骸化
- cmux が全16プロジェクトのターミナルを1ウィンドウで管理 → Spaces の主要ドライバーが消失
- Chrome 27ウィンドウが各Spaceに分散 → 切替が煩雑
- Finder も同様に分散 → 実質的にアプリ毎の切替は Space 切替より Cmd+Tab の方が速い

#### マルチAIブレスト結果（2026-03-05）

Gemini CLI + Claude 深層分析で5つの提案を生成。採用ロードマップ:

| Phase | 提案 | 内容 | 工数 | ステータス |
|-------|------|------|------|-----------|
| **P1** | cmux-First Bridge | tmuxセッション切替に連動してChromeウィンドウを前面化 | 半日 | **完了** |
| **P2（今週）** | Zero Spaces 仮想コンテキスト | JXAでウィンドウをオフスクリーン移動、Raycast Extension化 | 4-5日 | 未着手 |
| **P3（安定後）** | Spaces削減 or 全廃 | 16 → 2-4 Spaces、cmux + Raycast が全コンテキスト切替を担う | -- | 未着手 |

#### P1: cmux-First Bridge（2026-03-05 実装完了）

tmux `client-session-changed` フックを使い、セッション切替時に対応する Chrome ウィンドウを自動的に前面化する。

**ファイル:**
- ~~`~/.config/project-focus/contexts.json`~~ — 削除済み（3/10、レガシー。workspaces.jsonに統合済みで全消費者が参照停止）
- `~/.config/project-focus/bridge.sh` — ブリッジスクリプト（bash+python3+osascript）
- `~/.tmux.conf` — `client-session-changed` フック追加（`run-shell -b`）
- ログ: `~/.config/project-focus/bridge.log`（100KB自動ローテーション）

#### Spaces マッピング（16 Spaces — 現行）

| Space | Icon | Project | Status |
|-------|------|---------|--------|
| 1 | 📊 | 確定申告 | 常駐 |
| 2 | 🏠 | Apartment | 進行中 |
| 3 | 🛒 | Shopping | 常駐 |
| 4 | 🧾 | 経費精算 | 常駐 |
| 5 | 📧 | Outlook | 常駐 |
| 6 | ⚡ | Productivity | 進行中 |
| 7 | 🤖 | MeshClaw | 進行中 |
| 8 | 🎯 | Mission Control | 常駐 |
| 9 | 🎯 | Org Goals | 進行中 |
| 10 | 💡 | Discovery | 進行中 |
| 11 | 📺 | Second Screen | 進行中 |
| 12 | 🎬 | TEX | 進行中 |
| 13 | 🦘 | PES | 進行中 |
| 14 | 🐱 | Mars Dine | 進行中 |
| 15 | 🎨 | AU Creative | 進行中 |
| 16 | 🔧 | BIL AI Tools | 進行中 |

#### インフラ（既存・動作中）

| ツール | 用途 |
|--------|------|
| cmux 0.61.0 | ターミナル統合管理（16ワークスペース） |
| tmux 3.6a + TPM + resurrect + continuum | セッション永続化 |
| sesh v2.24.2 | tmuxセッションfuzzy切り替え |
| Raycast Spaces Manager Extension | Space切替・MenuBar表示（dev mode + LaunchAgent永続化） |
| Rectangle（無印） | ウィンドウスナップ（3/9 Pro→無印に切替。Pro Layouts機能がmacOS Spaces非対応+自動トリガー未動作のため） |
| Contexts | クロスSpaceウィンドウ検索 |
| Karabiner-Elements | キーボードショートカット |
| Thaw | メニューバー管理（Ice後継） |
| WhichSpace | メニューバーにSpace番号表示 |

#### ショートカット体系

| レベル | 修飾キー | キー | 備考 |
|---|---|---|---|
| macOS Space 1-10 | Ctrl+Option+Shift | 1-0 | Raycast Extension バックエンド |
| macOS Space 11-16 | Ctrl+Option | 1-6 | Raycast Extension バックエンド |
| cmux Workspace | ⇧⌘ | `[` `]` | 最頻用 |
| cmux Surface | ⌥⌘ | `[` `]` | タブ切替 |
| cmux Pane 左右 | ⌃⌘ | `[` `]` | ブラケット |
| cmux Pane 上下 | ⌃⌘ | `;` `'` | ホームロウ |

### cmux通知復旧（調査中 — 3/6〜7）

**問題:** tmux化後、cmuxのペインハイライト + Ctrl+U通知が来なくなった

**根本原因（ソースコード解析で判明）:**
- cmux通知はbell(`\a`)ではなく、Claude Code hooks経由
- cmux claude wrapper (`/Applications/cmux.app/Contents/Resources/bin/claude`) が `--settings` で hooks JSON を注入
- hooks: `SessionStart`, `Stop`, `Notification` → `cmux claude-hook notification` を実行
- tmux内ではwrapperを経由せず直接 `claude` を起動しているため、hooks未注入

**追加の制約:**
- `cmux claude-hook notification` はcmuxソケットに接続が必要
- ソケットは**プロセス祖先チェック**（PID parent chain walkで cmux PID を探索）
- tmux server は `launchd` の子 → tmux内プロセスは全てアクセス拒否（"Access denied — only processes started inside cmux can connect"）

**現在のアプローチ: named pipe リレー（検証中）**
```
cmux → login → fish → [relay: pipe読み取り → cmux claude-hook notification] (background)
                    → sesh connect (foreground, exec なし)
```
- `~/.config/fish/functions/cmux_tmux_attach.fish` にリレー起動を追加済み
- `exec sesh` → `sesh`（exec なし）に変更し、fishが生き続けてリレーの親として機能
- `disown` なし — プロセスツリーを維持してcmuxソケットアクセスを通す
- パイプ: `/tmp/cmux-notify-{session_name}`
- **未検証:** リレーが cmux 子孫として認識されるか確認が必要（新タブ開き直しでテスト）

### Slack投稿ポリシー
- `settings.json`: post_message, create_draft, reaction_tool 許可
- `CLAUDE.md`: #ai--mission-control のみ自動OK
- クロスポスト: `📱 [Slack:N:TS]` → `🤖 [WSN]` スレッド返信

---

## 成果物一覧

```
2026-03-06_workspace-and-bridge-infrastructure/
├── handover.md                              -- 本ファイル（統合版）
├── history/
│   ├── 2026-03-06_handover.md
│   ├── 2026-03-07_handover.md
│   └── 2026-03-09_handover.md
├── artifacts/
├── notes/
│   ├── tmux-session-recovery-2026-03-07.md  ← セッション消失原因・復旧手順
│   ├── cmux-restart-behavior-2026-03-08.md  ← cmux再起動時のCC全Kill事象調査
│   ├── cmux-rebuild-plan-2026-03-08.md     ← cmux WS再構築計画・WS定義テーブル
│   ├── workspaces-json-ssot-2026-03-09.md ← workspaces.json SSOT移行の全記録
│   └── tmux-auto-attach-investigation-2026-03-10.md ← 自動アタッチ暴走の調査・修正記録

# 旧 productivity-improvement-tools の成果物（参照用）:
../2026-02-23_productivity-improvement-tools/
  artifacts/
    spaces.md                              -- 16 Spacesマッピングテーブル
    enable-space-shortcuts.sh              -- ショートカット設定スクリプト
    karabiner-spaces-10-16.json            -- Karabiner-Elements用設定
  notes/
    spaces-management-research.md          -- 初期包括リサーチ
    cross-space-window-search-research.md  -- クロスSpace検索の詳細調査
    rectangle-pro-workspace-arrangements.md -- Rectangle Pro Layouts調査（アーカイブ: Pro→無印に切替済み 3/9）
    space-keyboard-shortcuts-research.md   -- キーボードショートカット調査
    cmux-settings-backup-2026-03-03.plist  -- cmux設定バックアップv1
    cmux-settings-backup-2026-03-03-v2.plist -- cmux設定バックアップv2（最終版）
    tmux-sesh-integration-research.md      -- tmux + sesh リサーチ（2026-03-05）
    spaces-restructure-brainstorm-2026-03-05.md -- Spaces再構築マルチAIブレスト

# 旧 slack-bridge-and-tmux-migration の成果物（参照用）:
../2026-03-06_slack-bridge-and-tmux-migration/
  notes/
    phase3-tmux-migration-plan.md          -- Phase 3 移行計画

# 元トピック(mcp-server-development)に残存するnotes:
../2026-03-02_mcp-server-development/notes/cmux-multi-pane-design.md
../2026-03-02_mcp-server-development/notes/tmux-migration-plan.md
../2026-03-02_mcp-server-development/notes/bridge-auto-start-investigation.md
../2026-03-02_mcp-server-development/notes/bridge-socket-interference-analysis.md

# Single Source of Truth:
~/Development/repos/ghq/github.com/syug/dotfiles/workspaces/workspaces.json  -- WS定義の一元管理（dotfiles repo、全消費者がここから読む）

# システムファイル:
~/raycast-extensions/spaces-manager/       -- Raycast TypeScript Extension（JSON読み書きに移行済み）
~/Library/LaunchAgents/
  com.spaces-manager.shortcuts.plist       -- ログイン時ショートカット自動設定
  com.spaces-manager.raycast-dev.plist     -- ray develop自動起動
  com.saitshug.claude-slack-bridge.plist   -- Slack↔CCブリッジ自動起動
~/.tmux.conf                               -- tmux設定（sesh + bridge.shフック追加済み）
~/.config/project-focus/
  bridge.sh                                -- P1ブリッジスクリプト（workspaces.json読み取り+番号優先マッチ）
  bridge.log                               -- 実行ログ（自動ローテーション）
~/.config/sesh/sesh.toml                   -- seshセッション定義（24セッション、TOML直読みのため移行対象外）
~/Development/claude-slack-bridge/
  src/bridge.ts                            -- tmux send-keys 版ブリッジ（workspaces.json読み取り）
  start.sh                                 -- while true ループ（LaunchAgent では不要）
  rebuild-cmux.sh                          -- cmux WS自動再構築スクリプト（jqでworkspaces.json読み取り）
~/.claude/CLAUDE.md                        -- Slack投稿ポリシー・クロスポスト規約
~/.claude/settings.json                    -- Slack MCP許可設定
~/.config/fish/config.fish                 -- fish設定
```

## アクションアイテム

**完了済み（まとめ）:** ショートカット修飾キー変更、enable-space-shortcuts.sh書換、LaunchAgent再起動耐性、switcher.ts更新、レガシーパス修正、Script Commands削除、menu-bar interval追加、ray develop LaunchAgent、cmuxショートカット再設計、cmux plistバックアップ、tmux+seshセットアップ、CC運用パターン確立、P1 cmux-First Bridge完了、tmux Phase 1-8全完了、LaunchAgent化完了

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | -- | Iceのアクセシビリティ権限を削除 | **要実施** |
| 2 | -- | Spaces Manager Extension本番化（dev mode脱却） | 未着手 |
| 3 | 3月中 | **P2: Zero Spaces 仮想コンテキスト** — JXA オフスクリーン移動 + Raycast Extension | 未着手 |
| 4 | -- | **P3: Spaces削減** — 16 → 2-4 Spaces or 全廃 | 未着手（P2安定後） |
| 5 | -- | Mac再起動後のブリッジ自動起動テスト | 未実施 |
| 14 | -- | ~~config.fish 自動アタッチ無効化~~ + ~~continuum-restore OFF~~ | **完了（3/10）** |
| 15 | -- | rebuild-cmux.sh をcmux上で手動実行（既存WS2つのため対話確認必要） | **要実施** |
| 10 | -- | **cmux通知リレー検証** — 新タブ開き直し→パイプ書き込み→ペインハイライト確認（※config.fish自動アタッチ無効化により、リレー起動方法の再検討が必要） | **次タスク** |
| 11 | -- | リレー成功後: Claude Code hooks に pipe 書き込みを追加 | 未着手（#10 依存） |
| 12 | -- | ~~tmuxソケットパスをcmux管理外に分離~~ — `~/.tmux/server/` に分離完了 | **完了（3/8）** |
| 13 | -- | ~~孤立tmux server + stoppedプロセスのクリーンアップ~~ + rebuild-cmux.sh で16WS再構築完了 | **完了（3/8）** |
| 6 | -- | Self-reporting protocol強化（CLAUDE.md） | P1 未着手 |
| 7 | -- | Error self-recovery protocol（CLAUDE.md） | P1 未着手 |
| 8 | -- | `$status` dashboardコマンド実装 | P2 未着手 |
| 9 | -- | 名前ベースルーティング（`$tex` 等エイリアス） | P2 未着手 |

## 重要な判断ログ

1. **Ice → Thaw移行（2026-02-26）:** macOS Tahoeで壊滅的。Thaw（コミュニティフォーク）に移行。
2. **Bunch廃止判断（2026-02-26）:** macOS Tahoeで起動時クラッシュ。※ただし2026-03-05時点で実は稼働中と判明。
3. **Space-Task-Tab統合の発見（2026-02-26）:** Space = Notion Task = Chrome Window が1:1対応。
4. **TypeScript Extension採用（2026-02-27）:** Claude Codeバックグラウンドエージェントが約3分で自律構築。
5. **トピック名変更（2026-03-02）:** `macos-spaces-management` → `productivity-improvement-tools`。
6. **cmuxワークスペース導入（2026-03-02）:** macOS Spacesとcmuxのハイブリッド運用。
7. **ショートカット修飾キー変更（2026-03-02）:** Ctrl+数字 → Ctrl+Option+Shift+数字（競合回避）。
8. **PlistBuddy vs defaults write の教訓（2026-03-02）:** `defaults export` → PlistBuddy → `defaults import` が正解。
9. **killall Dock の必要性（2026-03-02）:** `activateSettings -u` だけでは不十分。
10. **cmux自動ソート無効化・番号命名（2026-03-02）**
11. **Script Commands削除判断（2026-03-02）:** menu-bar の `interval: "1m"` で代替。
12. **MenuBarExtra API制限（2026-03-02）:** ドロップダウンをプログラムで開けない。
13. **Rectangle Pro Layouts 半諦め判断（2026-03-02）:** Apple APIの制限。→ **3/9にPro→無印Rectangleに切替。** Layouts機能がmacOS Spaces非対応（16 Spaces環境で実質無意味）+ 自動トリガー未動作。無印で十分。
14. **cmux vs Rectangle Pro コンフリクトなし確認（2026-03-02）** → Rectangle（無印）でも競合なし。
15. **cmuxショートカット体系のGhosttyライク再設計（2026-03-03）:** 全レベルを `[`/`]` で統一。
16. **cmux (manaflow-ai) はtmuxと独立（2026-03-05）:** Swift/AppKit製、tmux不使用。同名CLIラッパーは別物。
17. **tmux prefix Ctrl+Aはcmuxと競合しない（2026-03-05）:** cmuxはCmd修飾キーベース、tmuxはCtrlベースで完全分離。
18. **sesh採用（2026-03-05）:** 「cmux」CLIラッパーは存在しないため、sesh（Go製、~1,800スター）を採用。
19. **Spaces再構築方針決定（2026-03-05）:** cmux統合でSpacesの価値が低下。マルチAIブレスト（Gemini+Claude）で5提案生成。P1→P2→P3の段階的アプローチを採用。
20. **P1実装: tmux client-session-changed フック採用（2026-03-05）:** cmuxにはフック機構がないため、tmuxの`client-session-changed`フックを活用。セッション名から先頭数字・末尾`-N`を除去し、contexts.jsonとの双方向部分文字列マッチでプロジェクトを特定。python3でJSON解析（日本語プロジェクト名対応）、AppleScript `set index of window to 1` で前面化。`run-shell -b`でバックグラウンド実行しセッション切替をブロックしない設計。
21. **cmux API の正しい使い方（ソース解析 3/5）:** `workspace_id` でフィルタ、`surface_id` UUID で送信、`workspace.select` は使わない。
22. **tmux 全面移行の決定（3/5）:** cmux API の癖（3 RPC、\rハック、UUIDオンザフライ解決、ソケット断続切れ）を排除。`tmux send-keys` で確実送信。sesh でセッション定義一元管理。cmux は GUI、tmux はデータ転送 — 役割分離。
23. **send-keys の Enter 問題（3/6）:** `tmux send-keys -t session -- 'text' Enter` だと `--` フラグが `Enter` キーの解釈を妨げる。テキスト送信と Enter を2コマンドに分離。
24. **LaunchAgent の Mach Bootstrap 問題（3/3 → 3/6 解決）:** cmux ソケット依存時は LaunchAgent から接続不可（macOS セッション隔離）。tmux send-keys 移行後に問題解消。PATH に `/opt/homebrew/bin` を含める必要あり。
25. **Slackスレッド vs チャネル:** スレッド内 `$ws` は非対応（API制約）→ 仕様として受容。
26. **cmux通知はClaude Code hooks経由（3/6ソースコード解析）:** bell(`\a`)ではない。cmux claude wrapperが`--settings`でNotification hookを注入。tmux内では未注入のため通知が来ない。
27. **tmux ソケット永続化の決定（3/7）:** macOS Sleep 時に `/tmp` がクリーンアップされデュアルサーバー問題が発生。`TMUX_TMPDIR=~/.tmux/sockets` で永続化。LaunchAgent plist にも同変数追加。ゴースト検知はソケットパスで判別し `~/.tmux/sockets` のサーバーは保護。Plan Verify エージェントで6項目レビュー済み。
28. **tmux-resurrect/continuum 未インストール発覚（3/7）:** TPM のみインストール済みでプラグイン本体が未インストールだった。Sleep 後に tmux server が死亡し 24 セッション消失。`tpm/bin/install_plugins` で修正。セーブパスは `~/.local/share/tmux/resurrect/`（XDG準拠）。
29. **cmuxソケットのプロセス祖先チェック（3/6）:** 接続時にPID parent chainをwalkしてcmux PIDを探索。tmux serverはlaunchd子→全tmux内プロセスがアクセス拒否。`disown`もreparent→拒否。解決策: `exec`なし+`disown`なしでリレーのプロセスツリーを維持。
30. **cmux再起動時のCC全Kill原因特定（3/8）:** cmux再起動→PTY全破壊→SIGHUPカスケードでCC含む全プロセスが終了。CCの「システムがヤバい」はPTY切断検知による正常なgraceful shutdown。追加問題としてtmuxソケットも巻き添え消失（`~/.tmux/sockets/`にcmux named pipesとtmuxソケットが同居しているため）。
31. **tmuxソケットパス分離の実施（3/8）:** `TMUX_TMPDIR`を`~/.tmux/server/`に変更（fish config, LaunchAgent, cmux_tmux_attach.fish）。cmux named pipesは`~/.tmux/sockets/`に残留。これでcmux再起動時のtmuxソケット巻き添え消失を防止。
32. **cmux WS自動再構築スクリプト作成（3/8）:** `rebuild-cmux.sh`でcmux CLI経由で16WS+24タブを自動作成。`cmux new-workspace`→`rename-workspace`→`new-surface`→`send sesh connect`の4段階。dry-run対応。cmux plistにはWS構成が保存されないため、再構築時は毎回CLIで実行が必要。
33. **workspaces.json SSOT化（3/9）:** WS定義が5箇所（spaces.md, rebuild-cmux.sh, bridge.ts, contexts.json, sesh.toml）に分散していた問題を解消。`~/.config/workspaces/workspaces.json`をSingle Source of Truthとし、全消費者（rebuild-cmux.sh→jq、bridge.ts→JSON.parse、bridge.sh→python3、Raycast→readFileSync）を移行。名前不整合9件を統一。sesh.tomlはseshがTOML直読みのため対象外。→ **3/10にdotfilesリポジトリに移行**（判断#36参照）。
34. **bridge.sh番号優先マッチ導入（3/9）:** セッション名`13pes-1`のcore=`pes`がWS2 "Pest Control"に誤マッチする潜在バグを発見。セッション名先頭数字でWS番号を直接照合→不一致時のみパターン検索にフォールバックするロジックに修正。
35. **tmux自動アタッチ暴走の修正（3/10）:** config.fishの自動アタッチ（24ペイン同時sesh connect）+ tmux-continuumの自動復元が二重衝突して暴走。自動アタッチをコメントアウト、continuum-restore OFF、rebuild-cmux.shによる手動制御に一本化。調査で5段階の連鎖（fish→sesh→continuum→rebuild→bridge）を全て特定。
36. **workspaces.json dotfilesリポジトリ移行（3/10）:** 3/9のGDriveレビューで「git管理」が採用案だった。当初は`~/.config/workspaces/`をgit化する計画だったが、dotfiles管理の一環として`github.com/syug/dotfiles`（private, ghq管理下）に新リポジトリを作成し移行。パスを`~/Development/repos/ghq/github.com/syug/dotfiles/workspaces/workspaces.json`に変更。全4消費者（rebuild-cmux.sh L43, bridge.ts L41, bridge.sh L11, parser.ts L6）のパスを更新。contexts.json（レガシー、全消費者が参照停止済み）を削除。sesh.tomlはseshがTOML直読みのため手動同期を継続。SSOT移行は機能的に完了。

## 関連トピック

- [自作MCPサーバー開発](../2026-03-02_mcp-server-development/handover.md) — ブリッジの分割元トピック
- [Slack/Outlook MCP連携](../2026-02-27_slack-outlook-mcp-integration-research/handover.md)
- [Dev Environment](../2026-02-28_dev-environment-setup/handover.md) — cmux導入の背景
- [MeshClaw](../2026-02-25_meshclaw-onboarding/handover.md) — Space 7 の詳細
- [Weekly Workflow](../2026-02-23_weekly-workflow-setup/handover.md) — WorkLog運用の背景
- **統合元:** [productivity-improvement-tools](../2026-02-23_productivity-improvement-tools/handover.md)（リダイレクト済み）
- **統合元:** [slack-bridge-and-tmux-migration](../2026-03-06_slack-bridge-and-tmux-migration/handover.md)（リダイレクト済み）
