# Phase 3: ブリッジ tmux send-keys 移行計画

**Date:** 2026-03-06
**Status:** 着手中

---

## 概要

bridge.ts の cmux ソケット RPC（約200行）を `tmux send-keys`（約50-60行）に置換する。

## データモデル

### 現行
```typescript
interface CmuxWorkspace { shortName: string; index: number; ref: string; }
interface CmuxSurface { surfaceUUID: string; name: string; index: number; }
```

### 新
```typescript
interface TmuxSession {
  sessionName: string; // "6-1", "12-2"
  wsNumber: string;    // "6", "12"
  tabNumber: string;   // "1", "2"
}
```

## 主要な関数の置換

| 現行関数 | 行 | 新関数 | 実装 |
|---------|-----|--------|------|
| `cmuxRpcOnce()` | L78-143 | 削除 | — |
| `cmuxRpc()` | L145-158 | 削除 | — |
| `listWorkspaces()` | L160-185 | `listTmuxSessions()` | `tmux list-sessions -F '#{session_name}'` → `N-M` パターン抽出 |
| `resolveSurfaceUUIDs()` | L187-212 | 削除 | UUID概念消滅 |
| `listSurfaces()` | L214-233 | 削除 | session = 1 pane |
| `sendToSurface()` | L235-255 | `sendToTmux()` | `tmux send-keys -t 'N-M' -- 'text' Enter` |
| `sendToCmux()` | L257-269 | 削除 | `sendToTmux()` に統合 |
| `findWorkspace()` | L271-281 | `findSessions()` | wsNumber でフィルタ |

## コマンド体系の変更

| コマンド | 現行 | 新 |
|---------|------|-----|
| `$6 text` | cmux WS6 first surface | tmux session `6-1` |
| `$6:2 text` | cmux WS6 surface index 2 | tmux session `6-2` |
| `$list` | `workspace.list` RPC | `tmux list-sessions` |
| `$list:6` | `surface.list` for WS6 | WS6 の tmux sessions |
| `$all text` | 全WS first surface | 全 tmux sessions |

## import の変更

- 削除: `import * as net from "node:net"`
- 追加: `import { execSync } from "node:child_process"`

## エラーハンドリング

- tmux 未起動: `tmux list-sessions` が exit code 1 → 空配列
- session 不存在: `send-keys` が exit code 1 → catch で stderr ログ
- タイムアウト: `execSync` に `timeout: 5000` を明示

## エスケープ

```typescript
const escaped = text.replace(/'/g, "'\\''");
execSync(`tmux send-keys -t '${sessionName}' -- '${escaped}' Enter`);
```

## 変更しない部分

- Slack MCP クライアント（`createSlackClient`, `getRecentMessages`, `postToSlack`）
- `$` プレフィックスのパース・分岐ロジック（ターゲット部分のみ変更）
- `processedMessages` 重複排除
- SIGINT ハンドラ
- start.sh のループ構造（ログメッセージのみ更新）
- package.json, tsconfig.json

## 注意点

- 名前ベース検索（`$tex`）は廃止。番号のみ（`$6`）。エイリアスは後日検討
- `\r` ハック不要 — `send-keys ... Enter` で1コマンド完結
