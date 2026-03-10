# Handover: Command Mode Setup for Claude Code
**Topic:** Claude Codeのワークモード切り替えシステム構築
**Date:** 2026-02-23
**Status:** 完了（テスト未実施）

---

## 背景

Claude Codeで2つの動作モードを切り替えられる仕組みを構築した:

- **Directorモード（デフォルト）**: メインスレッドは監督役としてユーザーとの会話に専念。全ての実作業（コード変更、調査、探索、分析）はバックグラウンドsub-agentに委任。大規模タスクではagentが自らAgent Teams（TeamCreate）を組んで並行作業可能。
- **Hands-onモード**: 通常のClaude Code動作。メインスレッドが直接全作業を実行。

切り替えは単一コマンド: `/command-mode director` or `/command-mode hands-on`

## 命名の検討経緯

1. "dispatcher/solo" → "dispatcher" が直感的でないため却下
2. "team/solo" → Agent Teamsを使わないのに "team" はミスリーディング
3. 3段階（solo/async/teams）を検討 → asyncモードのagentがTeamsを自発的に起動できるため2段階で十分
4. メタファー案: 軍事、将棋、船、料理、映画、戦国
5. **最終決定: director/hands-on**（映画メタファー）
6. コマンド形式: `/solo` `/team` の2コマンドではなく、`/command-mode X` の1コマンドに統一

## 現在の状況

システムは設定完了。次のセッションからデフォルトで有効。

## 成果物一覧

### command-mode関連
| ファイル | 内容 |
|---|---|
| `~/.claude/CLAUDE.md` | "Work mode: Director (Default)" セクション追加 |
| `~/.claude/commands/command-mode.md` | `/command-mode` スラッシュコマンド |

### 同セッションで作成したAmazon開発ツールSkill（Kiro steering docsから変換）
| ファイル | 内容 |
|---|---|
| `~/.claude/commands/brazil.md` | Brazilビルドシステム |
| `~/.claude/commands/brazil-git.md` | Gitワークフロー・コミット規約 |
| `~/.claude/commands/crux.md` | コードレビュー（CRUX） |
| `~/.claude/commands/amazon-systems.md` | 内部開発システム一覧 |
| `~/.claude/commands/taskei.md` | Taskei タスク管理 |
| `~/.claude/commands/production-safety.md` | 本番環境安全ルール |

## アクションアイテム

| # | アクション | ステータス |
|---|---|---|
| 1 | 新セッションでdirectorモードの動作テスト | 未着手 |
| 2 | バックグラウンドagentのAgent Teams自動起動を確認 | 未着手 |
| 3 | ~~agentへの権限委譲（Write/Bash）の改善検討~~ | 対応済み（2026-02-24） |
| 4 | トークン効率の監視（delegation overheadの評価） | 未着手 |
| 5 | 次セッションでsub-agentがgit diff等を実行できるか検証 | 未着手 |

## 重要な判断ログ

- **Directorモードをデフォルトにした理由**: ユーザーが「作業中も会話できる状態を常に維持したい」と明確に要望。CLAUDE.mdに記載することで毎セッション自動適用。
- **2段階にした理由**: バックグラウンドagentがTask tool内でTeamCreateを呼べるため、明示的な "teams" モードは不要。agentの判断に委ねる。
- **agentの書き込み権限問題**: 今回のhandover保存でバックグラウンドagentにWrite/Bash権限が付与されなかった。directorモードの実運用ではagentの権限設定（`mode` パラメータ）を適切に設定する必要あり。

### 2026-02-24: Sub-agent Bash権限の解決

**問題**: `mode: "bypassPermissions"` を指定してもsub-agentのBash実行は `settings.json` の許可リストに依存する。マッチしないコマンドはプロンプトなしで拒否される。

**対応**: `~/.claude/settings.json` の `permissions.allow` にREAD系Bashパターンを追加。

追加したパターン:
- **ファイル読み取り**: `cat *`, `head *`, `tail *`, `tree *`, `grep *`, `for *`
- **git READ系**: `git status`, `git log *`, `git diff *`, `git show *`, `git blame *`, `git branch`, `git remote *`, `git stash list`
- **cd + git READ系**: `cd * && git status*`, `cd * && git log *`, `cd * && git diff *`, `cd * && git show *`, `cd * && git blame *`, `cd * && git branch*`, `cd * && git remote *`, `cd * && git stash list*`
- **Brazil**: `brazil ws *`

**意図的に除外（write系git）**: `git add`, `git commit`, `git push`, `git reset`, `git checkout`, `git rebase` 等。当初 `Bash(git *)` で全許可したが、write系が含まれるためREAD系のみに絞った。

**パターンマッチ仕様**: `Bash(cd * && git status*)` の `*` は `&&` を含む任意文字列にマッチ。multi-chainコマンド（`cd /path && git status && git log ...`）も対応可能。
