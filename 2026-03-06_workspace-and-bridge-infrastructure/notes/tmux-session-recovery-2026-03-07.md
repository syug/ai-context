# tmux セッション消失 & 復旧手順（2026-03-07）

## 発生した問題

- Mac Sleep 中に tmux ソケット (`/tmp/tmux-503/default`) が macOS にクリーンアップされた
- 旧 tmux server (PID 27353) はプロセスとして生存、既存接続も維持
- 新しい cmux ペインが開かれた際、sesh が新 tmux server (PID 17250) を起動
- **デュアルサーバー問題:** CLI/ブリッジは新サーバーのみ参照し、24セッション中 `6-2` のみ可視

## 根本原因

1. **tmux ソケットが `/tmp` にある:** macOS は Sleep/再起動時に `/tmp` をクリーンアップする
2. **tmux-resurrect/continuum が未インストール:** TPM 登録済みだがプラグイン本体なし → セーブなし → 復元不可
3. **ゴーストサーバー検知なし:** ソケット消失したサーバーを検知・停止する仕組みがなかった

## 修正内容

### 1. tmux ソケットパスを永続化
- `config.fish` に `TMUX_TMPDIR=~/.tmux/sockets` を設定
- `mkdir -p` でディレクトリ自動作成
- LaunchAgent plist にも `TMUX_TMPDIR` を追加

### 2. ゴーストサーバー検知
- `cmux_tmux_attach.fish` で `tmux list-sessions` が失敗した場合:
  - `pgrep -x tmux` で全 tmux プロセスを列挙
  - `~/.tmux/sockets` を使っていないサーバーのみ kill（安全な判定）

### 3. notify_pipe も永続パスに変更
- `/tmp/cmux-notify-*` → `~/.tmux/sockets/cmux-notify-*`

### 4. ブリッジログも永続パスに変更
- `/tmp/claude-slack-bridge.log` → `~/.tmux/sockets/claude-slack-bridge.log`

### 5. tmux プラグインインストール
- `~/.tmux/plugins/tpm/bin/install_plugins` で resurrect + continuum インストール
- セーブパス: `~/.local/share/tmux/resurrect/`

## セッション再作成手順

```bash
# 方法1: cmux 再起動（推奨）
# cmux を閉じて再度開く。全ペインが自動的に:
#   config.fish → TMUX_TMPDIR 設定 → cmux_tmux_attach → ゴースト検知 → sesh connect
# で新しい永続ソケット上の tmux セッションに接続する。

# 方法2: 手動（cmux 再起動なし）
for session in 1-1 2-1 2-2 3-1 4-1 5-1 6-1 6-2 7-1 8-1 8-2 9-1 9-2 10-1 10-2 11-1 12-1 12-2 13-1 13-2 14-1 14-2 15-1 16-1; do
  tmux has-session -t "$session" 2>/dev/null || sesh connect "$session"
done
```

## Plan Verify（マルチエージェントレビュー）結果

| 指摘 | 対応 |
|------|------|
| LaunchAgent に TMUX_TMPDIR 未設定 | ✅ plist に追加済み |
| pkill が雑 — 正常サーバーも殺す | ✅ ソケットパスで判別するように修正 |
| ~/.tmux/sockets の事前作成 | ✅ config.fish に mkdir -p 追加 |
| notify_pipe も /tmp で同じ問題 | ✅ ~/.tmux/sockets/ に移動 |
| cmux.sock も /tmp（スコープ外） | 認識のみ — cmux アプリ側の問題 |
| continuum のデュアルサーバー優先度問題 | ✅ ゴースト検知で旧サーバーを kill して防止 |
