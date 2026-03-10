# Handover Document
**Topic:** Gemini CLIのインストールと設定
**Date:** 2026-02-24
**Status:** 完了

---

## 背景

ユーザーがClaude Code環境でGemini（GoogleのAI）も使えるようにしたいと要望。Skill経由やMCPツールにGemini連携がないことを確認後、gemini-cliのインストールを実施した。

## 現在の状況

### インストール完了

- **パッケージ:** `@google/gemini-cli`
- **バージョン:** 0.29.7
- **インストール先:** `/Users/saitshug/.local/share/mise/installs/node/22.21.1/bin/gemini`
- **認証:** Google API Key設定済み（動作確認済み）

### 使い方

```bash
# 非対話モード（1回の質問）
gemini -p "質問内容"

# 対話モード
gemini
```

## 成果物一覧

```
2026-02-24_gemini-cli-setup/
├── handover.md
├── artifacts/   （空）
└── notes/       （空）
```

今回は設定作業のみのため成果物ファイルなし。

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | - | gemini-cliインストール | 完了 |
| 2 | - | 認証設定（API Key） | 完了 |
| 3 | - | 動作確認 | 完了 |

未完了アイテムなし。

## 重要な判断ログ

- **パッケージ名:** 当初 `@anthropic-ai/gemini-cli` という誤った情報があったが、正しくは `@google/gemini-cli`
- **認証方式:** `GEMINI_API_KEY` 環境変数を使用。他にVertex AIやGCA認証も選択可能だがAPI Keyが最もシンプル
- **使い分け:** Claude Code（メイン）とGemini CLI（セカンドオピニオン・比較検証用）の併用が可能な環境になった
