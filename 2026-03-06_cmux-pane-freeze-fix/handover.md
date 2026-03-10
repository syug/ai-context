# Handover Document
**Topic:** cmuxペインフリーズの修復手順
**Date:** 2026-03-06
**Status:** 完了

---

## 背景

cmux WS15（🎨 AU Creative）のターミナルペインがフリーズし、入力・スクロールに一切反応しなくなった。tmuxセッション `15-1` 内のclaudeプロセス（PID 36152）は正常動作中（STAT: S+）であり、cmux UI（surface）側の問題と判断。

## 現在の状況

### 診断結果
- tmux session/pane は alive（`pane_dead=0`）
- tmux client は `/dev/ttys027` に attached
- cmux `surface:23`（type=terminal）が WS15 のペイン `pane:22` に割り当て
- プロセスツリー: fish (PID 36116) → claude (PID 36152) — 正常動作中

### 試行した対処法（効果なし）
1. **`cmux refresh-surfaces`** — 1 surface リフレッシュされたが改善せず
2. **`tmux send-keys -R` + `tmux clear-history` + `tmux refresh-client`** — スクロール位置は正常化したが入力不可のまま

### 解決した対処法: Surface Detach/Reattach
cmux の surface を新規作成し、古いフリーズした surface を閉じてから、新 surface で同じ tmux session に再接続する。

```bash
# 1. 新しい surface を同じ pane に作成（最後の surface は閉じられないため先に作る）
cmux new-surface --type terminal --pane pane:22 --workspace workspace:15
# → OK surface:56

# 2. フリーズした古い surface を閉じる
cmux close-surface --surface surface:23 --workspace workspace:15

# 3. 新しい surface から tmux session に再接続
cmux send --workspace workspace:15 --surface surface:56 'tmux attach-session -t 15-1'
cmux send-key --workspace workspace:15 --surface surface:56 Enter
```

### 重要なポイント
- `cmux close-surface` は最後の surface では失敗する → 先に `new-surface` で代替を作る
- 新しい surface はデフォルトで新しいシェルが起動 → `tmux attach-session` で元の session に接続
- workspace 自体は変更しないので WS名やインデックスは保持される
- claude プロセスは tmux session 内で動いているため、surface の入れ替えでは影響を受けない

## 成果物一覧
```
2026-03-06_cmux-pane-freeze-fix/
├── handover.md
└── notes/
    └── cmux-pane-freeze-fix.md    # 詳細な修復手順ノート
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| — | — | — | 全て完了 |

## 重要な判断ログ
- プロセスkillは避け、cmux UI側の修復に注力した（ユーザー指示）
- `refresh-surfaces` → `tmux send-keys -R` → surface detach/reattach と段階的にエスカレーション
- surface detach/reattach パターンは今後のcmuxフリーズ対処のテンプレートとして使える
