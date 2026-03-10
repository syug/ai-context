# cmux WS再構築計画 (2026-03-08)

## 経緯

cmux再起動 → PTY全破壊 → SIGHUP → CC全Kill。復旧後、cmuxに1WSしか残っていない。

## 恒久対策（実施済み）

tmuxソケットパスをcmux管理外に分離:
```
~/.tmux/server/tmux-503/default   <- tmuxソケット（NEW）
~/.tmux/sockets/cmux-notify-*     <- cmux named pipes（変更なし）
```

変更ファイル:
- `~/.config/fish/config.fish` — TMUX_TMPDIR
- `~/Library/LaunchAgents/com.saitshug.claude-slack-bridge.plist` — TMUX_TMPDIR
- `~/.config/fish/functions/cmux_tmux_attach.fish` — ゴースト検知フィルタ

## 再構築スクリプト

ファイル: `~/Development/claude-slack-bridge/rebuild-cmux.sh`

### 動作フロー
1. 既存WS1つを再利用（seed）
2. `cmux new-workspace` x 15 で残り作成（各1.5秒スリープ）
3. `cmux rename-workspace` で全16WSにアイコン付き名前設定
4. `cmux new-surface` で2タブWSに追加タブ作成
5. `cmux send` + `cmux send-key Enter` で各タブに `sesh connect {ws#}-{tab#}` 実行
6. WS1を選択

### WS定義（16WS, 24タブ）

| WS# | 名前 | タブ数 | セッション名 |
|-----|------|--------|-------------|
| 1 | 📊 確定申告 | 1 | 1-1 |
| 2 | 🏠 Apartment | 2 | 2-1, 2-2 |
| 3 | 🛒 Shopping | 1 | 3-1 |
| 4 | 🧾 経費精算 | 1 | 4-1 |
| 5 | 📧 Outlook | 1 | 5-1 |
| 6 | ⚡ Productivity | 2 | 6-1, 6-2 |
| 7 | 🤖 MeshClaw | 1 | 7-1 |
| 8 | 🎯 Mission Control | 2 | 8-1, 8-2 |
| 9 | 🎯 Org Goals | 2 | 9-1, 9-2 |
| 10 | 💡 Discovery | 2 | 10-1, 10-2 |
| 11 | 📺 Second Screen | 1 | 11-1 |
| 12 | 🎬 TEX | 2 | 12-1, 12-2 |
| 13 | 🦘 PES | 2 | 13-1, 13-2 |
| 14 | 🐱 Mars Dine | 2 | 14-1, 14-2 |
| 15 | 🎨 AU Creative | 1 | 15-1 |
| 16 | 🔧 BIL AI Tools | 1 | 16-1 |

### 使い方
```bash
./rebuild-cmux.sh --dry-run  # 確認
./rebuild-cmux.sh            # 実行
```

## 実行後の確認項目
- [ ] tmux list-sessions で24セッション表示
- [ ] $list (Slackブリッジ) で全WS表示
- [ ] 各WSでCCが起動していること
- [ ] cmux通知（Ctrl+U）が動作すること（通知リレー未実装のため期待しない）
