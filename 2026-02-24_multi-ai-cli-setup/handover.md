# Handover Document
**Topic:** マルチAI CLI環境のセットアップ
**Date:** 2026-02-25
**Status:** 進行中

---

## 背景

Claude Code環境に加えて、他のAI CLIツール（Gemini CLI、Kiro CLI、OpenAI Codex CLI）も使えるようにしたいという要望から開始。複数のAIを比較・連携させる開発環境を構築した。

## 現在の状況

### インストール済みAI CLIツール

| ツール | バージョン | 認証 | 使い方 |
|--------|-----------|------|--------|
| Claude Code | (ホスト環境) | 設定済み | メイン作業環境 |
| Gemini CLI | 0.29.7 | Google API Key | `gemini -p "質問"` |
| Kiro CLI | 1.26.2 | (toolbox経由) | `kiro-cli chat "質問"` |
| OpenAI Codex CLI | 0.104.0 | codex login (ChatGPT Free) | `codex` / `codex exec "質問"` |

### 各CLIの特徴

**Claude Code**
- メインの開発環境
- チーム機能（TeamCreate）で複数エージェント並行作業が可能
- ファイル編集、Bash実行、MCP連携など全機能

**Gemini CLI (`@google/gemini-cli`)**
- Google AI Studioで取得したAPI Keyで認証
- `-p` フラグで非対話モード
- 対話モードは `gemini` で起動

**Kiro CLI (AWS)**
- `.toolbox/bin/kiro-cli` にインストール済み
- `--no-interactive` フラグで非対話モード
- MCPサーバー連携機能あり

**OpenAI Codex CLI (`@openai/codex`)**
- `codex login` でChatGPTアカウント連携（ブラウザOAuth）
- 現在Free tierで利用中（期間限定トライアル）
- `codex exec "質問"` で非対話モード
- `codex review` でコードレビュー機能
- MCP連携機能あり

### マルチAI連携の可能性

1. **Claude Codeチーム開発**
   - TeamCreateで複数Claudeエージェント起動
   - 実装/テスト/ドキュメントを並行作業

2. **クロスAIレビュー**
   - 同じコードを4つのAIにレビューさせて意見集約
   - 実装案を各AIに出させて比較

3. **ハイブリッド構成**
   - Claudeチームがメイン開発
   - 重要判断でGemini/Kiro/Codexにセカンドオピニオン

## 成果物一覧

```
2026-02-24_multi-ai-cli-setup/
├── handover.md
├── artifacts/   （空）
└── notes/       （空）
```

設定作業のみのため成果物ファイルなし。

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | - | Gemini CLIインストール | 完了 |
| 2 | - | Gemini認証設定 | 完了 |
| 3 | - | Kiro CLI動作確認 | 完了 |
| 4 | - | OpenAI Codex CLIインストール・認証 | 完了 |
| 5 | - | ChatGPT Plusへのアップグレード検討 | 未着手（優先度低） |
| 6 | - | マルチAIチーム開発の実証実験 | 未着手 |

## 重要な判断ログ

- **Geminiパッケージ名:** `@google/gemini-cli` が正解。`@anthropic-ai/gemini-cli` は誤り
- **認証方式:** Geminiは `GEMINI_API_KEY` 環境変数、Kiroは既存のtoolbox認証を使用
- **非対話モード:** Geminiは `-p` フラグ、Kiroは `--no-interactive` フラグ、Codexは `exec` サブコマンドで非対話実行可能
- **チーム開発:** Claude Code内のTeamCreate機能で複数エージェント連携は既に可能。異なるAI間の自動連携は今後の実験課題
- **Codex CLI:** `@openai/codex` パッケージ (npm)。認証は `codex login` でブラウザOAuth。ChatGPT Free/Goプランで期間限定トライアル利用可能、Plus ($20/月) でフル利用可能。Claude Code (Max $40/月) の半額だが、Plusの利用上限は要確認

## 関連トピック

- [2026-02-24_gemini-cli-setup](../2026-02-24_gemini-cli-setup/) — Gemini CLIインストールの詳細記録
