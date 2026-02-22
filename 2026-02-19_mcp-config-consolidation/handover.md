# Handover Document
**Topic:** MCP設定の統合・複数ツール間の共有化
**Date:** 2026-02-19
**Status:** 完了

---

## 背景

Claude Code、Kiro、Smith、Aki の4つのAIツールを利用しているが、MCP サーバーの設定がツールごとにバラバラに管理されていた。Claude Code では一部の MCP サーバー（asana, notion, memory）がプロジェクト固有設定（`/Users/saitshug` 専用）に置かれており、グローバルに使えない状態だった。

これを整理し、`~/.mcp.json` を Single Source of Truth として全ツールに設定を配布する仕組みを構築した。

## 現在の状況

### 設定のグローバル化（完了）

Claude Code の `~/.claude.json` において、`projects["/Users/saitshug"].mcpServers` にあった3サーバー（asana, notion, memory）をトップレベルの `mcpServers` に移動した。`jq` でアトミックに更新（Claude Code が頻繁にファイルを書き換えるため Edit ツールでは競合した）。

### 共有設定ファイル（完了）

`~/.mcp.json` を全 MCP サーバーの正規設定として整備：

| サーバー | 種別 | 接続方式 |
|---------|------|---------|
| builder-mcp | 社内ツール | stdio |
| playwriter | ブラウザ操作 | stdio (npx) |
| asana | タスク管理 | SSE |
| notion | ドキュメント | SSE |
| memory | 記憶永続化 | stdio (npx) |

### 同期スクリプト（完了）

`~/.config/mcp/sync-mcp.sh` を作成。`~/.mcp.json` を読み取り、各ツール固有の形式に変換して配布する。

| ツール | 設定ファイル | 形式の特徴 |
|--------|------------|-----------|
| Aki | `~/.aki/mcp_settings.json` | Kiro と同じ `{mcpServers: {...}}` 形式 |
| Claude Code | `~/.claude.json` の `mcpServers` | `type` フィールド必須（`stdio` / `sse`） |
| Kiro | `~/.kiro/settings/mcp.json` | `~/.mcp.json` と同じ `{mcpServers: {...}}` 形式 |
| Smith | `~/Library/Application Support/Smith/mcp-servers.json` | 配列形式 `{servers: [{id, name, serverType, ...}]}`、`serverType: "builtin"` は保持 |

スクリプトの特徴：
- `--dry-run` フラグで事前確認可能
- Smith のビルトインサーバー（Webflow, Figma Desktop）は保持したまま custom サーバーのみ同期
- 各ツールのディレクトリが存在しない場合は SKIP

## 成果物一覧

```
~/.mcp.json                     — MCP設定の Single Source of Truth
~/.config/mcp/sync-mcp.sh       — 同期スクリプト
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | - | `~/.mcp.json` を編集したら `sync-mcp.sh` を実行する運用を定着させる | 継続 |

## 重要な判断ログ

- **`~/.claude.json` の編集に `jq` を使用した理由**: Claude Code のプロセスが `~/.claude.json` を頻繁に更新するため、Read → Edit の間にファイルが変わりレースコンディションが発生した。`jq` でアトミックに読み書きすることで解決。同期スクリプトでも同じ理由で `jq` を採用。
- **Smith のビルトインサーバー保持**: Smith は Webflow や Figma Desktop など `serverType: "builtin"` のサーバーを独自に管理している。これらは `~/.mcp.json` には含めず、同期時に保持する設計とした。
- **`autoApprove` フィールドの扱い**: `~/.mcp.json` の `autoApprove` はそのまま Kiro に渡される。Claude Code 向けには除外している（Claude Code は別の権限管理を持つため）。
- **Aki の設定形式**: `~/.aki/mcp_settings.json` は Kiro と同じ `{mcpServers: {...}}` 形式。当初フラット形式と誤認していたが修正済み。
