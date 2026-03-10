# tmux自動アタッチ暴走 調査結果（2026-03-10）

## 問題

Mac再起動/cmux再起動のたびにtmuxが暴走する。

## 発見した自動起動チェーン

### Phase 1: launchd (OS起動直後)

| # | トリガー | ファイル | 動作 |
|---|----------|----------|------|
| A | `RunAtLoad` + `KeepAlive` | `com.saitshug.claude-slack-bridge.plist` | bridge.js 起動、5秒ごとに `tmux list-sessions` ポーリング。tmux不在でも crash→relaunch 無限ループ |

### Phase 2: cmux起動 → fish shell → tmux自動アタッチ

| # | トリガー | ファイル | 動作 |
|---|----------|----------|------|
| B | cmuxペイン内でfish起動 | `config.fish` L85-89 | `CMUX_WORKSPACE_ID` + `CMUX_SURFACE_ID` 検出 → `cmux_tmux_attach` 自動実行 |
| C | `cmux_tmux_attach` 関数 | `cmux_tmux_attach.fish` L17-53 | cmux.sock RPC → WS番号+タブ番号解決 → セッション名生成 |
| D | ゴーストキル | 同上 L61-69 | `/tmp` ソケットの古いtmuxを掃除（24並行で競合条件あり） |
| E | `sesh connect` | 同上 L90 | セッション未存在なら**自動作成** + startup_command実行 |

### Phase 3: sesh による tmux セッション自動作成

| # | トリガー | ファイル | 動作 |
|---|----------|----------|------|
| F | `sesh connect {name}` | `sesh.toml` | 全24セッションで `startup_command = "claude"` → **claude 24個一斉起動** |

### Phase 4: tmux-continuum 自動復元

| # | トリガー | ファイル | 動作 |
|---|----------|----------|------|
| G | tmuxサーバ起動時 | `.tmux.conf` L112 | `@continuum-restore 'on'` → 前回保存状態を全復元 |
| H | continuum_restore.sh | tmux-continuum プラグイン | sesh新規作成 + resurrect復元が**二重に存在** |

### Phase 5: rebuild-cmux.sh (手動)

| # | トリガー | ファイル | 動作 |
|---|----------|----------|------|
| I | 手動実行 | `rebuild-cmux.sh` L218-238 | 全ペインに `sesh connect` を送信 → config.fishの自動アタッチと**二重起動** |

## 暴走メカニズム

### Mac再起動時
1. launchd → bridge.js → tmux list-sessions ポーリング開始
2. cmux起動 → 24ペインのfish が同時に `cmux_tmux_attach` 実行
3. 24個の `sesh connect` が並行 → tmuxセッション一斉作成 + claude起動
4. tmux-continuum が前回の24セッション復元 → sesh作成分と衝突
5. 結果: セッション二重化、claude多重起動

### cmux再起動時
1. cmux閉じ → fish/tmuxクライアント切断（tmuxサーバは生存）
2. cmux再起動 → 新ペインのfish → `cmux_tmux_attach` 発火
3. 既にclaude動作中のセッションに新クライアントがアタッチ → 制御衝突

## 適用した対処

1. **config.fish の自動アタッチを無効化** — `cmux_tmux_attach` 呼び出しをコメントアウト
2. **tmux-continuum の自動復元を無効化** — `@continuum-restore 'off'`
3. tmuxアタッチは `rebuild-cmux.sh` で手動制御に一本化

## 無関係なファイル

- `com.spaces-manager.shortcuts.plist` — キーボードショートカットのみ
- `com.spaces-manager.raycast-dev.plist` — Raycast dev server
- `bridge.sh` (project-focus) — Chrome前面化のみ
- `workspaces.json` — データ定義のみ
