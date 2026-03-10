# cmux再起動時の挙動調査 (2026-03-08)

## 事象

cmux再起動時、Claude Codeが「システムがヤバい」と言い残して全プロセスをKillして消えた。

## 根本原因

**cmux再起動 → PTY全破壊 → SIGHUPカスケード → CC含む全プロセスが終了**

### シグナル伝搬経路

```
cmux app終了
  -> Ghosttyターミナルレイヤー破壊（PTY master side クローズ）
    -> カーネルが PTY slave side に SIGHUP 送信
      -> fish (シェル) に SIGHUP
        -> sesh に SIGHUP
          -> tmux client (attach-session) に SIGHUP
            -> tmux server は独立プロセスなので生存するはず...
              -> しかしソケットファイルが消失 -> サーバー孤立
```

CCの「システムがヤバい」= PTY切断を検知した正常なgraceful shutdown。CC側の問題ではない。

## 追加の問題: tmuxソケット消失

- tmux server (PID 3328) は生存しているが、ソケットファイル (`~/.tmux/sockets/tmux-503/default`) が消失
- cmux再起動時に `~/.tmux/sockets/` 内のnamed pipes (cmux-notify-*) をリクリエイトする際、tmuxのUNIXドメインソケットも巻き添えで消された可能性
- 結果: `tmux list-sessions` -> "no server running" でサーバーが孤立状態

## 調査で確認したプロセス状態

### tmuxプロセス内訳（Activity Monitorで約10個に見えた原因）

| 種別 | 数 | 状態 |
|------|-----|------|
| tmux server | 1 (PID 3328) | 稼働中だがソケット消失で孤立 |
| tmux client (attach) | 6 | 10-1に5重attach + 12-1に1 |
| fish通知ウォッチャー | ~9 | 全てT (stopped/suspended) |

### ソケット状態

| パス | 状態 |
|------|------|
| `~/.tmux/sockets/tmux-503/default` | 消失 |
| `/tmp/tmux-503/` | 存在しない（ゴーストなし）|
| `~/.tmux/sockets/cmux-notify-*` | 26個（全て21:22リクリエイト）|

### cmux claude wrapper のhooks

`/Applications/cmux.app/Contents/Resources/bin/claude` が `--settings` で以下のhooksを注入:
- `SessionStart` -> `cmux claude-hook session-start`
- `Stop` -> `cmux claude-hook stop` (timeout 10s)
- `Notification` -> `cmux claude-hook notification`

cmux自体が再起動中のため、Stop hookの `cmux claude-hook stop` はソケット (`/tmp/cmux.sock`) が存在せず失敗した可能性が高い。

## 事実と推測の区別

### 事実
- tmuxソケットが消失している
- tmux serverプロセスは生存している (PID 3328, PPID=1)
- bridge logに "no server running on ~/.tmux/sockets/tmux-503/default" が大量に記録
- sesh/fish通知ウォッチャーが全てstopped状態で残存
- cmux claude wrapperにStop hookが定義されている
- named pipes (cmux-notify-*) は全て21:22タイムスタンプ（リクリエイト痕跡）

### 推測
- SIGHUPの正確な伝搬経路
- cmuxがソケットディレクトリを操作した具体的メカニズム
- CCの「ヤバい」メッセージの正確なトリガー条件

## 推奨アクション

### 即時対応
1. 孤立tmux server (PID 3328) をkill
2. stopped状態のsesh/fishプロセスを全kill
3. cmux上でワークスペースを再構築

### 恒久対策（要検討）
1. **tmuxソケットパスをcmux管理外に分離** — `~/.tmux/sockets/` にcmux named pipesとtmuxソケットが同居している問題。tmuxソケットを別ディレクトリ（例: `~/.tmux/server/`）に分離すれば、cmux再起動時の巻き添え消失を防げる
2. **tmux-resurrect/continuum** — セッション内容の自動保存・復元は既に設定済み。tmux serverが再起動しても `prefix + Ctrl-r` でセッション復元可能
3. **cmux再起動時のgraceful shutdown** — cmux側がPTY破壊前にシグナルを送る仕組みがあるか確認（manaflow-aiに確認）

## 関連
- handover: `2026-03-06_workspace-and-bridge-infrastructure`
- 前回のデュアルサーバー事故: `notes/tmux-session-recovery-2026-03-07.md`
