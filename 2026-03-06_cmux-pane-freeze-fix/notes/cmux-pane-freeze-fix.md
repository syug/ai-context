# cmux Pane Freeze Fix

## Problem
cmux WS15 (🎨 AU Creative) のペインがフリーズ。入力・スクロールに反応しない。
tmux session `15-1` のclaude プロセス (PID 36152) 自体は正常に動作中 (STAT: S+)。

## Diagnosis
- tmux session/pane は alive (pane_dead=0)
- tmux client は `/dev/ttys027` に attached
- cmux surface:23 (type=terminal) が WS15 に割り当て
- プロセスは正常 → cmux UI (surface) 側の問題

## Tried & Failed
1. `cmux refresh-surfaces` → surfaceは1つリフレッシュされたが改善せず
2. `tmux send-keys -t 15-1:1.1 -R` + `tmux clear-history` + `tmux refresh-client` → スクロール位置は戻ったが入力不可のまま

## Solution: Surface Detach/Reattach
cmux の surface を作り直して同じ tmux session に再接続する。

### Steps
```bash
# 1. 現状確認
cmux list-pane-surfaces --workspace workspace:15
# → surface:23 Terminal [selected]

# 2. 新しい surface を同じ pane に作成（最後の surface は閉じられないため先に作る）
cmux new-surface --type terminal --pane pane:22 --workspace workspace:15
# → OK surface:56

# 3. フリーズした古い surface を閉じる
cmux close-surface --surface surface:23 --workspace workspace:15

# 4. 新しい surface から tmux session に再接続
cmux send --workspace workspace:15 --surface surface:56 'tmux attach-session -t 15-1'
cmux send-key --workspace workspace:15 --surface surface:56 Enter
```

### Key Points
- `close-surface` は最後の surface では失敗する → 先に `new-surface` で代替を作る
- 新しい surface はデフォルトで新しいシェルが起動する → `tmux attach-session` で元の session に接続
- workspace 自体は変更しないので WS名やインデックスは保持される
- claude プロセスは tmux session 内で動いているため、surface の入れ替えでは影響を受けない
