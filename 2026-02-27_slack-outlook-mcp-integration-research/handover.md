# Handover Document
**Topic:** Slack/Outlook MCP連携 — リサーチから実装完了まで
**Date:** 2026-02-27
**Status:** 完了

---

## 背景

Claude CodeからAISmith（社内AIデスクトップアプリ）と同等のSlack・Outlook連携機能を使いたいというリクエスト。Gemini CLI・Kiro CLIでも同じ機能を共有したい。AISmithのコードを解析し、複数の実現アプローチを調査・比較した上で、社内MCPサーバーを採用し、3CLI全ての設定を完了した。

## 現在の状況

### リサーチフェーズ（完了）

6つのリサーチエージェントを並行起動し調査完了：

1. **AISmith Slack実装分析** — 9ツール、Midway+SAML SSO→xoxcトークン。ローカルコード（`/Users/saitshug/Development/repos/brazil-ws/AISmith`）を直接解析。
2. **AISmith Outlook実装分析** — 5ツール（EmailRead/Write, CalendarRead/Write, CalendarAnalyze）。8ステップOAuth+SAML+PKCEフロー、OWA JSON API使用。
3. **SantosMCPServers macOS互換性** — macOSで動作可能、Midway cookie認証、npm build可能。
4. **OSS Slack/Outlook MCPサーバー** — ubie-oss/slack-mcp（107 stars）、Softeria/ms-365-mcp（485 stars, 90+ツール）。Amazon企業認証でブロック。
5. **社内Outlook MCPサーバー** — `aws-outlook-mcp`（21ツール、Graph API、Midway認証）が最有力。
6. **Kiro CLI / Gemini CLI のMCP対応** — 両方stdioトランスポート対応、同じMCPサーバーを共有可能。

### マルチエージェントレビュー（完了）

4手法を3CLI視点（Claude Code / Gemini CLI / Kiro CLI）でレビュー：

| 手法 | 判定 | 理由 |
|------|------|------|
| A: 社内MCPサーバー | 基盤 | Midway認証済み、開発ゼロ |
| B: OSS MCPサーバー | **不採用** | Amazon企業Slack/M365の認証ブロック |
| C: AISmithフォーク | **不採用** | 8-13日の開発+メンテ負担、OWA APIよりGraph APIが安定 |
| D: ハイブリッド | **採用** | A手法の最適組み合わせ |

### インストール・設定フェーズ（完了）

| 項目 | 状態 | 詳細 |
|------|------|------|
| `ai-community-slack-mcp` | インストール済 | `~/.aim/mcp-servers/ai-community-slack-mcp`（AICommunitySlackMCP-1.0.35.0） |
| `aws-outlook-mcp` | インストール済 | `~/.toolbox/bin/aws-outlook-mcp`（v0.2.7） |
| Claude Code設定 | 完了 | `~/.claude.json` mcpServers に追加済（7サーバー） |
| `.mcp.json` 共有設定 | 完了 | 7サーバー構成 |
| Kiro CLI設定 | 完了 | `~/.kiro/settings/mcp.json`（7サーバー） |
| Gemini CLI設定 | 完了 | `~/.gemini/settings.json`（slack + outlook） |
| Midway認証 | 有効 | `~/.midway/cookie` 確認済 |

### 設定内容

**Slack MCP (`ai-community-slack-mcp`)**:
- コマンド: `/Users/saitshug/.aim/mcp-servers/ai-community-slack-mcp`
- env.PATH に `~/.toolbox/bin`, `~/.aim/mcp-servers`, node bin を明示（CLI環境でPATHが継承されない問題の対策）
- 実体は `aim mcp start-server ai-community-slack-mcp` を呼ぶラッパースクリプト

**Outlook MCP (`aws-outlook-mcp`)**:
- コマンド: `/Users/saitshug/.toolbox/bin/aws-outlook-mcp`
- M365 Graph APIベース、Midway認証

## 成果物一覧

```
2026-02-27_slack-outlook-mcp-integration-research/
├── handover.md         ← 本ファイル
├── artifacts/          （設定は各CLIの設定ファイルに直接適用済み）
└── notes/
```

設定変更を適用したファイル:
- `~/.claude.json` — ai-community-slack-mcp, aws-outlook-mcp 追加
- `~/.mcp.json` — 同上
- `~/.kiro/settings/mcp.json` — aws-outlook-mcp 追加（slackは既存）
- `~/.gemini/settings.json` — mcpServers セクション新規追加

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | — | Claude Code再起動して新MCPサーバーの読み込み確認 | 完了 |
| 2 | — | Slack動作テスト（チャンネル検索、メッセージ読み取り） | 完了 |
| 3 | — | Outlook動作テスト（カレンダー表示、メール読み取り） | 完了 |
| 4 | — | Gemini CLIでの動作テスト | 完了 |
| 5 | — | Kiro CLIでの動作テスト | 完了 |
| 6 | — | 使用後にツールギャップがあれば、upstream貢献またはフォーク検討 | 継続監視 |

## 重要な判断ログ

### なぜD手法（ハイブリッド）を採用したか
- **認証が全て**: Amazon企業環境ではMidway認証が唯一の実用的な認証経路。OSSサーバーはBot Token/Azure AD登録が必要で現実的でない
- **開発ゼロ vs 8-13日**: 既存の社内MCPサーバーで同等機能が即時利用可能
- **Graph API > OWA JSON API**: aws-outlook-mcpはMicrosoft公式のGraph APIを使用。AISmithのOWA JSON APIは非公式で壊れやすい

### Slackサーバーの選定: ai-community-slack-mcp > SantosMCPServers
- SantosMCPServersの旧Slack MCPは認証問題が報告されている
- ai-community-slack-mcpはその修正版、`aim mcp install`で簡単導入
- Kiro設定に既に登録済みだった（2/25導入）

### Outlookサーバーの導入手順
- `toolbox install aws-outlook-mcp` は初回レジストリ未登録で失敗
- `toolbox registry add s3://buildertoolbox-awsoutlook-mcp-us-west-2/tools.json` でレジストリ追加後に成功
- v0.2.7 がインストールされた

### .claude.json の更新方法
- Claude Code自身がskillUsage等を頻繁に更新するため、Edit toolでの更新が競合する
- `jq` による原子的な更新で解決

### PATH問題の対策
- MCPサーバーはCLIのシェル環境を継承しないことがある
- env.PATHに `~/.toolbox/bin`, `~/.aim/mcp-servers`, node binを明示的に設定

## 関連トピック

- [MCP設定の統合](../2026-02-19_mcp-config-consolidation/handover.md) — MCPサーバー設定の統合・共有化
- [MCP OAuth Token Expiry](../2026-02-20_mcp-oauth-token-expiry/handover.md) — MCPのOAuth問題調査
- [Gemini CLI Setup](../2026-02-24_gemini-cli-setup/handover.md) — Gemini CLI導入
- [Multi-AI CLI Setup](../2026-02-24_multi-ai-cli-setup/handover.md) — マルチAI CLI環境構築
- [MeshClaw Onboarding](../2026-02-25_meshclaw-onboarding/handover.md) — 社内AIエージェント導入
