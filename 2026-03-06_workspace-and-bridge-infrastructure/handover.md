# Handover Document
**Topic:** ワークスペース基盤 + Slack↔CCブリッジ — tmux/sesh/cmux統合管理
**Date:** 2026-03-13
**Status:** 進行中（3/13 WS構成 16→13 に整理完了・sesh.toml同期済み）

---

## 背景

macOSのSpacesを**16個**使用し、**1 Space = 1プロジェクト**として運用してきた。根底にある欲求は「タスクを忘れたくない」「同時進行したい」。cmux導入（2026-03-02）で全ターミナルが1ウィンドウに統合された結果、16 Spaces に Chrome/Finder を分散する意味が薄れた。

並行して、Claude CodeのSlack経由リモート操作を実現するため、Slack↔cmuxブリッジを構築（3/3〜）。UUIDベースルーティング、マルチタブ対応、クロスポスト、スレッド返信を実装し双方向通信を確立。しかしcmux APIの癖（3 RPC、\rハック、UUIDオンザフライ解決、ソケット断続切れ）が深刻で、tmux全面移行を決定（3/5）。cmuxはGUI、tmuxはデータ転送と役割分離する方針。

3/6にブリッジをtmux send-keysに書き換え、LaunchAgentで自動起動化を完了。E2Eテスト通過。Spaces再構築はマルチAIブレスト（Gemini+Claude）で5提案→P1完了、P2/P3は今後。

3/13にWS構成を16→13に整理（3 WS削除、1マージ、2リネーム、並び替え）。

---

## 現在の状況

### ワークスペース構成（13 WS — 3/13更新）

| # | Icon | Name | Tabs | Status |
|---|------|------|------|--------|
| 1 | 💰 | ファイナンス | 1 | 常駐 |
| 2 | 🏠 | Apartment | 2 | 進行中 |
| 3 | ⚡ | Productivity | 2 | 進行中 |
| 4 | 📧 | Outlook | 1 | 常駐 |
| 5 | 🎯 | Mission Control | 2 | 常駐 |
| 6 | 🎯 | Org Goals | 2 | 進行中 |
| 7 | 💡 | Discovery | 2 | 進行中 |
| 8 | ⛓️‍💥 | Halfpipe Deprecation | 1 | 進行中 |
| 9 | ⚾️ | Live Sports API | 2 | 進行中 |
| 10 | 🦘 | PES | 2 | 進行中 |
| 11 | 🐈‍⬛ | Dine 2.0 | 1 | 進行中 |
| 12 | 🔧 | UK AI Campaign | 1 | 進行中 |
| 13 | 🐱 | Mars Dine | 2 | 進行中 |

**3/13 変更履歴:**
- Space 1: 確定申告 → **ファイナンス**（旧 Space 4 経費精算をマージ、chromePatterns統合）
- Space 3 (Shopping): **削除**
- Space 4 (経費精算): **削除**（Space 1にマージ）
- Space 6 (Productivity): **Outlookの前に移動**（旧6→新3）
- Space 7 (MeshClaw): **削除**
- Space 15 (AU Creative): **AU BIL にリネーム** → さらに **Dine 2.0** (🐈‍⬛) にリネーム
- Space 13 (BIL AI Tools): **UK AI Campaign** にリネーム
- Space 11 (Mars Dine): **最後尾に移動**（新13）

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
| 1 | sesh.toml 作成 | 完了 |
| 2a | tmux session 一括作成 | 完了 |
| 2b | cmux ペインを tmux に接続 | 完了（3/6） |
| 3 | ブリッジを tmux send-keys に切替 | 完了（3/6） |
| 4 | LaunchAgent で自動起動 | 完了（3/6） |
| 5 | E2E テスト | 完了（3/6） |
| 6 | tmux-resurrect/continuum インストール | 完了（3/7） |
| 7 | ソケットパス永続化 (`TMUX_TMPDIR=~/.tmux/sockets`) | 完了（3/7） |
| 8 | ゴーストサーバー検知 | 完了（3/7） |

#### tmux セッション消失 & デュアルサーバー事故（3/7）
- **根本原因:** macOS Sleep 時に `/tmp/tmux-503/default` ソケットがクリーンアップされた
- **再発防止:** `TMUX_TMPDIR=~/.tmux/server`、ゴーストサーバー検知、tmux-resurrect/continuum
- 詳細: `notes/tmux-session-recovery-2026-03-07.md`

#### tmux自動アタッチ暴走の根本原因と修正（3/10）
- **根本原因:** 24ペインのfishが同時に `cmux_tmux_attach` を実行 → 多重起動
- **修正:** config.fish自動アタッチ無効化、continuum-restore OFF、rebuild-cmux.sh手動制御に一本化
- 詳細: `notes/tmux-auto-attach-investigation-2026-03-10.md`

#### cmux再起動によるCC全Kill事象（3/8）
- **根本原因:** cmux再起動→PTY全破壊→SIGHUPカスケード→CC全滅
- CCの「ヤバい」= PTY切断検知による正常なgraceful shutdown
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

#### マルチAIブレスト結果（2026-03-05）

| Phase | 提案 | 内容 | 工数 | ステータス |
|-------|------|------|------|-----------|
| **P1** | cmux-First Bridge | tmuxセッション切替に連動してChromeウィンドウを前面化 | 半日 | **完了** |
| **P2（今週）** | Zero Spaces 仮想コンテキスト | JXAでウィンドウをオフスクリーン移動、Raycast Extension化 | 4-5日 | 未着手 |
| **P3（安定後）** | Spaces削減 or 全廃 | 16 → 2-4 Spaces、cmux + Raycast が全コンテキスト切替を担う | -- | 未着手 |

#### P1: cmux-First Bridge（2026-03-05 実装完了）

tmux `client-session-changed` フックを使い、セッション切替時に対応する Chrome ウィンドウを自動的に前面化する。

**ファイル:**
- `~/.config/project-focus/bridge.sh` — ブリッジスクリプト（bash+python3+osascript）
- `~/.tmux.conf` — `client-session-changed` フック追加（`run-shell -b`）
- ログ: `~/.config/project-focus/bridge.log`（100KB自動ローテーション）

#### ショートカット体系

| レベル | 修飾キー | キー | 備考 |
|---|---|---|---|
| macOS Space 1-10 | Ctrl+Option+Shift | 1-0 | Raycast Extension バックエンド |
| macOS Space 11-16 | Ctrl+Option | 1-6 | Raycast Extension バックエンド |
| cmux Workspace | ⇧⌘ | `[` `]` | 最頻用 |
| cmux Surface | ⌥⌘ | `[` `]` | タブ切替 |
| cmux Pane 左右 | ⌃⌘ | `[` `]` | ブラケット |
| cmux Pane 上下 | ⌃⌘ | `;` `'` | ホームロウ |

#### インフラ（既存・動作中）

| ツール | 用途 |
|--------|------|
| cmux 0.61.0 | ターミナル統合管理 |
| tmux 3.6a + TPM + resurrect + continuum | セッション永続化 |
| sesh v2.24.2 | tmuxセッションfuzzy切り替え |
| Raycast Spaces Manager Extension | Space切替・MenuBar表示（dev mode + LaunchAgent永続化） |
| Rectangle（無印） | ウィンドウスナップ |
| Contexts | クロスSpaceウィンドウ検索 |
| Karabiner-Elements | キーボードショートカット |
| Thaw | メニューバー管理（Ice後継） |
| WhichSpace | メニューバーにSpace番号表示 |

### Raycast Spaces Manager Extension（3/13確認）

- `~/raycast-extensions/spaces-manager/` — TypeScript Extension
- workspaces.json を動的読み取り → WS構成変更に自動追従
- 旧WS名のハードコード: **なし**
- パス: SSOT パスと一致 ✓
- `switcher.ts:18` に `spaceNumber > 16` の上限チェックあり（現13 WSなので問題なし。増やす時に修正）
- Space 11-16 のキーバインドは削除不要（将来の増設に備えて残存）

### cmux通知復旧（調査中 — 3/6〜7）

**問題:** tmux化後、cmuxのペインハイライト + Ctrl+U通知が来なくなった

**根本原因:** cmux通知はClaude Code hooks経由。tmux内では未注入。プロセス祖先チェックでtmux内プロセスはアクセス拒否。

**現在のアプローチ: named pipe リレー（検証中）**
- config.fish自動アタッチ無効化により、リレー起動方法の再検討が必要

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
│   ├── 2026-03-09_handover.md
│   └── 2026-03-10_handover.md
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
    spaces.md                              -- 16 Spacesマッピングテーブル（旧構成）
    enable-space-shortcuts.sh              -- ショートカット設定スクリプト
    karabiner-spaces-10-16.json            -- Karabiner-Elements用設定
  notes/
    spaces-management-research.md          -- 初期包括リサーチ
    cross-space-window-search-research.md  -- クロスSpace検索の詳細調査
    rectangle-pro-workspace-arrangements.md -- Rectangle Pro Layouts調査（アーカイブ）
    space-keyboard-shortcuts-research.md   -- キーボードショートカット調査
    cmux-settings-backup-2026-03-03.plist  -- cmux設定バックアップv1
    cmux-settings-backup-2026-03-03-v2.plist -- cmux設定バックアップv2（最終版）
    tmux-sesh-integration-research.md      -- tmux + sesh リサーチ
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
~/.config/sesh/sesh.toml                   -- seshセッション定義（13セッション定義、TOML直読みのため手動同期）
~/Development/claude-slack-bridge/
  src/bridge.ts                            -- tmux send-keys 版ブリッジ（workspaces.json読み取り）
  start.sh                                 -- while true ループ（LaunchAgent では不要）
  rebuild-cmux.sh                          -- cmux WS自動再構築スクリプト（jqでworkspaces.json読み取り）
~/.claude/CLAUDE.md                        -- Slack投稿ポリシー・クロスポスト規約
~/.claude/settings.json                    -- Slack MCP許可設定
~/.config/fish/config.fish                 -- fish設定
```

## アクションアイテム

**完了済み（まとめ）:** ショートカット修飾キー変更、enable-space-shortcuts.sh書換、LaunchAgent再起動耐性、switcher.ts更新、レガシーパス修正、Script Commands削除、menu-bar interval追加、ray develop LaunchAgent、cmuxショートカット再設計、cmux plistバックアップ、tmux+seshセットアップ、CC運用パターン確立、P1 cmux-First Bridge完了、tmux Phase 1-8全完了、LaunchAgent化完了、config.fish自動アタッチ無効化+continuum-restore OFF（3/10）、workspaces.json 16→13 WS整理+sesh.toml同期（3/13）

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | -- | Iceのアクセシビリティ権限を削除 | **要実施** |
| 2 | -- | Spaces Manager Extension本番化（dev mode脱却） | 未着手 |
| 3 | 3月中 | **P2: Zero Spaces 仮想コンテキスト** — JXA オフスクリーン移動 + Raycast Extension | 未着手 |
| 4 | -- | **P3: Spaces削減** — 13 → 2-4 Spaces or 全廃 | 未着手（P2安定後） |
| 5 | -- | Mac再起動後のブリッジ自動起動テスト | 未実施 |
| 15 | -- | rebuild-cmux.sh を13 WS構成で再実行 | **要実施** |
| 16 | -- | macOS Spacesを16→13に減らす（System Settings） | **要実施** |
| 10 | -- | **cmux通知リレー検証**（config.fish自動アタッチ無効化により再検討要） | **次タスク** |
| 11 | -- | リレー成功後: Claude Code hooks に pipe 書き込みを追加 | 未着手（#10 依存） |
| 6 | -- | Self-reporting protocol強化（CLAUDE.md） | P1 未着手 |
| 7 | -- | Error self-recovery protocol（CLAUDE.md） | P1 未着手 |
| 8 | -- | `$status` dashboardコマンド実装 | P2 未着手 |
| 9 | -- | 名前ベースルーティング（`$tex` 等エイリアス） | P2 未着手 |
| 17 | -- | `switcher.ts:18` の上限16を可変にする（WS数増加時） | 低優先 |

## 重要な判断ログ

1. **Ice → Thaw移行（2026-02-26）:** macOS Tahoeで壊滅的。Thaw（コミュニティフォーク）に移行。
2. **Bunch廃止判断（2026-02-26）:** macOS Tahoeで起動時クラッシュ。
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
13. **Rectangle Pro → 無印切替（3/9）:** Layouts機能がmacOS Spaces非対応 + 自動トリガー未動作。無印で十分。
14. **cmux vs Rectangle コンフリクトなし確認（2026-03-02）**
15. **cmuxショートカット体系のGhosttyライク再設計（2026-03-03）:** 全レベルを `[`/`]` で統一。
16. **cmux (manaflow-ai) はtmuxと独立（2026-03-05）:** Swift/AppKit製、tmux不使用。
17. **tmux prefix Ctrl+Aはcmuxと競合しない（2026-03-05）**
18. **sesh採用（2026-03-05）:** Go製、~1,800スター。
19. **Spaces再構築方針決定（2026-03-05）:** P1→P2→P3の段階的アプローチ。
20. **P1実装: tmux client-session-changed フック採用（2026-03-05）**
21. **cmux API の正しい使い方（ソース解析 3/5）**
22. **tmux 全面移行の決定（3/5）:** cmux API の癖を排除。役割分離。
23. **send-keys の Enter 問題（3/6）:** テキスト送信と Enter を2コマンドに分離。
24. **LaunchAgent の Mach Bootstrap 問題解決（3/6）:** tmux send-keys 移行後に問題解消。
25. **Slackスレッド vs チャネル:** スレッド内 `$ws` は非対応（API制約）。
26. **cmux通知はClaude Code hooks経由（3/6）:** tmux内では未注入。
27. **tmux ソケット永続化の決定（3/7）:** `TMUX_TMPDIR=~/.tmux/server`。
28. **tmux-resurrect/continuum 未インストール発覚（3/7）**
29. **cmuxソケットのプロセス祖先チェック（3/6）**
30. **cmux再起動時のCC全Kill原因特定（3/8）:** SIGHUPカスケード。
31. **tmuxソケットパス分離の実施（3/8）:** `~/.tmux/server/` に変更。
32. **cmux WS自動再構築スクリプト作成（3/8）:** `rebuild-cmux.sh`。
33. **workspaces.json SSOT化（3/9）:** 5箇所分散→1箇所に統合。dotfilesリポジトリに移行（3/10）。
34. **bridge.sh番号優先マッチ導入（3/9）:** セッション名先頭数字でWS番号を直接照合。
35. **tmux自動アタッチ暴走の修正（3/10）:** 5段階の連鎖を特定、手動制御に一本化。
36. **workspaces.json dotfilesリポジトリ移行（3/10）**
37. **WS構成 16→13 整理（3/13）:** Shopping・経費精算・MeshClaw削除。確定申告→ファイナンス（経費精算マージ）。Productivity→Outlook前に移動。AU Creative→Dine 2.0、BIL AI Tools→UK AI Campaign。Mars Dine→最後尾。キーバインドは将来の増設に備えて16分残存。
38. **Raycast Extension ハードコード確認（3/13）:** 旧WS名のハードコードなし。switcher.ts:18 に上限16あるが現13WSで問題なし。workspaces.jsonパスはSSOTと一致。

## 関連トピック

- [自作MCPサーバー開発](../2026-03-02_mcp-server-development/handover.md) — ブリッジの分割元トピック
- [Slack/Outlook MCP連携](../2026-02-27_slack-outlook-mcp-integration-research/handover.md)
- [Dev Environment](../2026-02-28_dev-environment-setup/handover.md) — cmux導入の背景
- [Weekly Workflow](../2026-02-23_weekly-workflow-setup/handover.md) — WorkLog運用の背景
- **統合元:** [productivity-improvement-tools](../2026-02-23_productivity-improvement-tools/handover.md)（リダイレクト済み）
- **統合元:** [slack-bridge-and-tmux-migration](../2026-03-06_slack-bridge-and-tmux-migration/handover.md)（リダイレクト済み）
