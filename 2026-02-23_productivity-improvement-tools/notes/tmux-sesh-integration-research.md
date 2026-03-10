# tmux + sesh Integration Research (2026-03-05)

## cmuxとtmuxの関係

- cmux (manaflow-ai) はtmuxとは**完全に独立した実装**
- Swift/AppKit製ネイティブmacOSアプリ、libghosttyでターミナルレンダリング
- tmuxのコード・プロトコル・サーバーは一切不使用
- ただしtmux CLIとの互換性を積極的に追求中（GitHub Issue #153）

## cmux + tmux 組み合わせパターン

| パターン | 概要 | 実現可能性 |
|---------|------|-----------|
| A: ネスト | cmux内でtmux起動 | 可能（採用） |
| B: tmuxバックエンド | cmuxがtmux control modeに接続 | 不可能（Discussion #681で提案のみ） |
| C: 用途別使い分け | ローカル=cmux、SSH=tmux | 可能 |
| D: ハイブリッド | 特定WSだけtmux | 可能（A+Cの折衷） |

## tmuxにあってcmuxにないもの

- **セッション永続化（detach/attach）** — 最大の差分。cmuxを閉じるとプロセスは死ぬ
- **リモートアクセス** — SSH先からattach可能
- **プラグインエコシステム** — tpm + resurrect, continuum等
- **高度な自動化** — pipe-pane, capture-pane, wait-for, set-hook

## 既存tmuxセットアップ

- tmux 3.6a (Homebrew)
- prefix: Ctrl+A
- TPM + tmux-sensible + tmux-resurrect + tmux-continuum (自動保存ON)
- vim風キーバインド (hjkl)
- TrueColor対応済み

## キーバインド競合

cmuxのショートカット（⇧⌘[/], ⌥⌘[/], ⌃⌘[/]）はCmd修飾キーベースで、tmuxのCtrl+A prefixとは**競合しない**。確認済み。

## 「cmux」CLIラッパーの調査結果

「tmuxセッションのfuzzy finder」としての「cmux」は**広く知られたツールは存在しない**。同名ツールは複数あるが全てニッチ（スター0〜327）。

## 代替ツール: sesh（採用）

- **sesh v2.24.2** — Go製tmuxセッションfuzzy switcher
- `brew install sesh` でインストール済み
- ~/.tmux.conf に `prefix + T` でfzf連携UIを追加済み
- fish shell対応、fzf連携、セッション自動作成

### sesh fzf UI 操作

| キー | 機能 |
|------|------|
| Ctrl+A | 全リスト表示 |
| Ctrl+T | tmuxセッションのみ |
| Ctrl+G | 設定済みセッション |
| Ctrl+X | zoxideディレクトリ |
| Ctrl+F | fd検索 |
| Ctrl+D | セッション削除 |

## 運用パターン（確立済み）

1. cmuxのワークスペースでtmux起動 → CC等を動かす
2. cmuxが落ちても `tmux attach` で完全復帰
3. CC内から `!tmux detach` でCCを終了せずにtmux detach可能
4. `Ctrl+A → T` でseshのfuzzyセッション切り替え

## 検証結果

- tmux detach/attach: 動作確認済み
- cmuxタブクローズ → 別タブからattach: 動作確認済み
- Ctrl+A prefix: cmuxにインターセプトされず正常動作
