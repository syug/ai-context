# Handover Document
**Topic:** macOS 開発環境セットアップ（新規ラップトップ + QuickLook .ts対応 + cmux/Claude Code修正）
**Date:** 2026-03-02
**Status:** 進行中（QuickLook は再起動待ち）

---

## 背景

新しい macOS 開発ラップトップのセットアップ手順と、個別の環境カスタマイズを一元管理する。既存の laptop-setup-guide（2025-12-30作成）をベースに、追加の環境設定（QuickLook .ts対応等）を統合する。

### 参照ドキュメント

- **Laptop Setup Guide**: `/Users/saitshug/Library/CloudStorage/GoogleDrive-syugo3hz@gmail.com/My Drive/Development-environment-settings/A/laptop-setup-guide.md`
  - 2025-12-30 に作成された包括的なセットアップガイド

## 現在の状況

### 1. ベース環境セットアップ（laptop-setup-guide に基づく、完了済み）

以下が文書化・セットアップ済み:

| カテゴリ | ツール | 状態 |
|---------|--------|------|
| パッケージマネージャ | Homebrew | 完了 |
| ターミナル | Ghostty（Catppuccin Mocha, JetBrainsMono Nerd Font） | 完了 |
| ターミナル関連 | cmux（tmux セッションマネージャ） | 完了 |
| シェル | Fish Shell（デフォルトシェルに設定済み） | 完了 |
| Fish プラグイン | fisher, bobthefish, z, fzf, fish-ghq | 完了 |
| フォント | FiraCode / JetBrainsMono / Hack Nerd Font | 完了 |
| Git ツール | tig, git-lfs, SourceTree | 完了 |
| ランタイム管理 | mise（Node.js, Python 等） | 完了 |
| ウィンドウ管理 | Rectangle（無印。Pro→切替 3/9）, Contexts, jordanbaird-ice, WhichSpace | 完了 |
| 開発ツール | Insomnia, Figma | 完了 |
| 生産性 | Notion, Google Drive, Obsidian, Asana | 完了 |
| Amazon 内部 | Toolbox, Axe, Kiro CLI, Midway (mwinit) | 完了 |
| AI アシスタント | Claude Code（Bedrock経由, aki プロファイル） | 完了 |
| QuickLook | qlmarkdown（Markdown用） | 完了 |
| スクリーンショット | 保存先を `~/Pictures/Screenshots` に変更 | 完了 |

### 2. QuickLook .ts ファイル対応（追加設定、進行中）

Finder で `.ts`（TypeScript）ファイルを QuickLook（スペースキー）でプレビューしたい。macOS 標準では `.ts` のシンタックスハイライト表示に対応していない。

#### インストール済みプラグイン

1. **Syntax Highlight** (`brew install --cask syntax-highlight`)
   - `/Applications/Syntax Highlight.app` にインストール済み
   - システム設定 > 機能拡張 > Quick Look で有効化済み
   - `qlmanage -m` にはジェネレータとして表示されず（App Extension 方式のため）
   - quicklookd + Finder 再起動では効かなかった
   - 注意: deprecated（2026-09-01 に無効化予定）

2. **qlstephen** (`brew install --cask qlstephen`)
   - `~/Library/QuickLook/QLStephen.qlgenerator` にインストール済み
   - プレーンテキストとして表示するタイプ（シンタックスハイライトなし）
   - QuickLook キャッシュリセット・quarantine 属性削除は未実施（ユーザーが中断）
   - 注意: deprecated（2026-09-22 に無効化予定）

#### ブロッカー

- 両方とも macOS 再起動後に効く可能性が高い
- ユーザーは「後で再起動する」と回答

### 3. cmux（tmux）内での Claude Code 起動修正（完了）

#### 問題

cmux（tmux）のペインから `claude` コマンドを実行すると以下のエラーで起動できない:

```
Error: Claude Code cannot be launched inside another Claude Code session.
Nested sessions share runtime resources and will crash all active sessions.
To bypass this check, unset the CLAUDECODE environment variable.
```

原因: 親の Claude Code セッションが設定する `CLAUDECODE` 環境変数が、tmux の子シェルに継承されるためネスト検出に引っかかる。

#### 修正内容

`~/.config/fish/config.fish` の `claude` 関数に `set -e CLAUDECODE` を追加:

```fish
function claude
    set -e CLAUDECODE           # ← 追加: tmuxペインからの起動を許可
    set -x CLAUDE_CODE_USE_BEDROCK 1
    set -x ANTHROPIC_MODEL 'global.anthropic.claude-opus-4-5-20251101-v1:0'
    set -x ANTHROPIC_SMALL_FAST_MODEL 'global.anthropic.claude-sonnet-4-5-20250929-v1:0'
    set -x AWS_PROFILE 'aki'
    command claude $argv
end
```

また、tmux セッション内では自動的に `CLAUDECODE` を解除するガードも追加済み（config.fish 末尾）:

```fish
if set -q TMUX
    set -e CLAUDECODE
end
```

### 4. 主要な設定ファイルパス

| ファイル | パス |
|---------|------|
| Fish config | `~/.config/fish/config.fish` |
| Ghostty config | `~/.config/ghostty/config` |
| Fish completions | `~/.config/fish/completions/` |
| Claude Code config | Fish config 内の `claude` 関数で設定 |
| Ada profile | `aki` プロファイル（account: 657246199914） |

### 5. Claude Code 設定詳細

```fish
function claude
    set -e CLAUDECODE
    set -x CLAUDE_CODE_USE_BEDROCK 1
    set -x ANTHROPIC_MODEL 'global.anthropic.claude-opus-4-5-20251101-v1:0'
    set -x ANTHROPIC_SMALL_FAST_MODEL 'global.anthropic.claude-sonnet-4-5-20250929-v1:0'
    set -x AWS_PROFILE 'aki'
    command claude $argv
end
```

### 6. Fish Shell 主要エイリアス/略語

| 略語 | コマンド |
|------|---------|
| `bb` | `brazil-build` |
| `t` | `tig` |
| `p` | `pnpm` |
| `pi` | `pnpm i` |
| `grh` | `git reset --hard` |
| `gs` | `git stash` |
| `gsm` | `git stash -m` |
| `gsp` | `git stash pop` |
| `gfi/gff/gfff` | git flow init/feature start/feature finish |

## 成果物一覧

| ファイル | 場所 | 説明 |
|---------|------|------|
| laptop-setup-guide.md | `Google Drive/Development-environment-settings/A/` | 包括的セットアップガイド（2025-12-30作成） |
| handover.md | 本ファイル | 開発環境セットアップの引き継ぎ文書 |

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | -- | macOS を再起動して QuickLook（Syntax Highlight / qlstephen）が効くか確認 | 未着手 |
| 2 | -- | 効かない場合 qlstephen の quarantine 除去: `xattr -cr ~/Library/QuickLook/QLStephen.qlgenerator && qlmanage -r` | 未着手 |
| 3 | -- | 両方効かない場合、代替手段を検討 | 未着手 |
| 4 | -- | laptop-setup-guide.md に QuickLook .ts 対応手順を追記検討 | 未着手 |
| 5 | -- | Claude Code のモデルバージョンを定期的に更新確認（現在 Opus 4.6 / Sonnet 4.6） | 継続 |
| 6 | -- | laptop-setup-guide.md に cmux + Claude Code のネスト回避設定を追記 | 未着手 |

## 重要な判断ログ

- **2025-12-30**: laptop-setup-guide.md を作成。Homebrew ベースで統一的にツールを管理する方針。
- **2026-02-28**: QuickLook .ts 対応として Syntax Highlight を第一候補として選択（シンタックスハイライト対応のため）
- **2026-02-28**: Syntax Highlight が即座に効かなかったので qlstephen をバックアップとして追加インストール
- **2026-02-28**: 両方 deprecated だが、2026年9月まではまだ使える
- **2026-02-28**: 本 handover を setup-guide の情報と統合し、開発環境全体の引き継ぎ文書に拡張
- **2026-03-02**: cmux（tmux セッションマネージャ）を Homebrew でインストール
- **2026-03-02**: cmux ペインから Claude Code が起動できない問題を修正。`claude` 関数内で `set -e CLAUDECODE` を追加する方式を採用（tmux チェックより確実）。config.fish 末尾の tmux ガードも併用。
