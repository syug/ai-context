# Handover Document
**Topic:** 自作MCPサーバー開発（Asana MCP / PARC-ARC MCP）
**Date:** 2026-03-07
**Status:** 進行中（安定稼働・承認確認待ち）

---

## 背景

Claude Code / Gemini CLI / Kiro CLIでAmazon社内ツール連携を追加するため、AISmithの既存コードを流用してMCPサーバーを自作した。Asana MCP（13ツール）と PARC/ARC MCP（8ツール）を開発・デプロイ済み。社内Slack/Outlook MCPも採用・設定完了。

## 現在の状況

### MCP サーバー（安定稼働中）

| サーバー | ツール数 | 展開先 | ステータス |
|---------|---------|--------|-----------|
| Asana MCP | 13 | CC, Gemini, Kiro | 安定稼働 |
| PARC/ARC MCP | 8 | CC, Gemini, Kiro | 安定稼働 |
| Slack MCP | 社内 | CC | 安定稼働 |
| Outlook MCP | 社内 | CC | 安定稼働 |

- 4サーバー全て安定稼働中
- Smith開発チームへのLambda直呼び承認確認は未完了（ユーザーが連絡中）

### 3/7 追加: asana_time_tracking ツール

Time Tracking Entries の CRUD ツールを追加（12→13ツール）:
- `create` — タスクに時間エントリ追加（task_gid, duration_minutes, entered_on?, description?）
- `list` — タスクの時間エントリ一覧（task_gid）
- `get` / `update` / `delete` — エントリ単体操作（entry_gid）

実装箇所:
- `src/client/asana-client.ts` — `getTimeTrackingEntriesApi()` 追加（5メソッド）
- `src/tools/index.ts` — `asana_time_tracking` ツール登録

## 成果物一覧

```
2026-03-02_mcp-server-development/
├── handover.md
├── history/ (12 versions)
├── artifacts/
│   └── ai-mission-control-design.md
├── notes/
│   ├── bridge-auto-start-investigation.md
│   ├── bridge-socket-interference-analysis.md
│   ├── cmux-multi-pane-design.md
│   └── tmux-migration-plan.md

~/Development/asana-mcp-server/
~/Development/parc-arc-mcp-server/
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1-23 | — | MCP開発・デプロイ・設定 | ✅ 完了 |
| 24 | — | asana_time_tracking ツール追加 | ✅ 完了（3/7） |
| 32 | — | Smith開発チームにLambda直呼び承認確認 | ⏳ ユーザーが連絡中 |
| 33 | — | テストタスク削除（Onboarding Project内） | P3 |

## 重要な判断ログ

### AISmith Lambda直呼びアプローチ
- AISmithのコードを解析し、Lambda関数を直接呼ぶMCPサーバーを自作
- 社内Slack/Outlook MCPは既存の社内MCPサーバー（ai-community-slack-mcp, aws-outlook-mcp）を採用

## 関連トピック

- [ワークスペース基盤 + ブリッジ](../2026-03-06_workspace-and-bridge-infrastructure/handover.md) — 旧分割先トピック（統合済み）
- [Slack/Outlook MCP連携](../2026-02-27_slack-outlook-mcp-integration-research/handover.md)
- [MCP設定統合](../2026-02-19_mcp-config-consolidation/handover.md)
- [AI開発インフラ見直し](../2026-03-06_ai-workflow-infrastructure-overhaul/handover.md) — トピック分割の経緯
