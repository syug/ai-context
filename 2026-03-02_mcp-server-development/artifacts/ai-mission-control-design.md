# AI Mission Control - Comprehensive Design Document

**Version:** 2.0
**Date:** 2026-03-03
**Status:** Living Document

---

## 1. ゴール

**Enable productive asynchronous work with Claude Code from anywhere -- desk, couch, or mobile.**

cmux で最大 16 並列セッションを同時運用し、Slack 経由の双方向通信で iPhone から全セッションを制御する。

### Director Mode の原則

ユーザーは **"Director"**（指示を出し、通知を受け取る人）であり、**"Operator"**（ターミナルを直接操作する人）ではない。

| Role | Director (採用) | Operator (不採用) |
|------|----------------|------------------|
| 入力手段 | Slack からの高レベル指示 | ターミナル直接操作 |
| 出力手段 | Slack Push 通知（自己申告） | SSH でターミナル監視 |
| 観測可能性 | Self-reporting | ターミナル画面共有 |
| デバイス | iPhone Slack App で十分 | SSH クライアント必須 |
| 同時管理 | 16 セッション容易 | 1-2 セッションが限界 |

**コアコンセプト:** 観測可能性は SSH ではなく self-reporting で担保する。

---

## 2. アーキテクチャ

```
+============================================================+
|                    USER (iPhone Slack App)                   |
+============================================================+
  |                    |                           |
  | SEND               | RECEIVE                   | MANAGE
  | $workspace cmd     | Push notifications        | Asana Board
  v                    |                           v
+------------------+   |               +---------------------+
| #ai--mission-    |   |               | Asana Board (Kanban)|
| control (Slack)  |   |               | Backlog→InProgress  |
+--------+---------+   |               | →Review→Test→Done   |
         |             |               +---------------------+
         | poll (5s)   |
         v             |
+------------------+   |
| claude-slack-    |   |
| bridge (Node.js) |   |
+--------+---------+   |
         | JSON-RPC    |
         v             |
+------------------+   |
| cmux socket      |   |
+--------+---------+   |
    +----+----+----+   |
    v    v    v    v   |
  +--+ +--+ +--+ +--+ |
  |W1| |W2| |..| |16|-+--------+
  +--+ +--+ +--+ +--+          |
    MCP: Asana(12)              |
    PARC/ARC(8), Slack...      |
         |                      |
    +----+----+                 |
    v         v                 v
  Asana     curl POST      Asana Workflows
  comment   Webhook          (bot名義)
  (記録)    (即時~2s)       (遅延~10-40s)
              |                 |
              v                 v
         #ai--mission-control → iPhone Push
```

### データフロー

```
[Inbound]  User → Slack $cmd → Bridge → cmux socket → CC session
[Outbound] CC → Asana task → Workflow → Slack (10-40s)
           CC → curl Webhook → Slack (即時 ~2s)
           CC → Asana comment (記録のみ)
```

---

## 3. コンポーネント

| # | Component | Location | Status |
|---|-----------|----------|--------|
| 1 | Asana MCP (12 tools) | `~/Development/asana-mcp-server/` | ✅ |
| 2 | PARC/ARC MCP (8 tools) | `~/Development/parc-arc-mcp-server/` | ✅ |
| 3 | Slack→cmux Bridge | `~/Development/claude-slack-bridge/` | ✅ |
| 4 | Asana Workflows (2) | Asana GUI config | ✅ |
| 5 | Slack Webhook | curl POST | ✅ |
| 6 | Bridge auto-start | `~/.config/fish/config.fish` | ✅ |
| 7 | CLAUDE.md rules | `~/.claude/CLAUDE.md` | ✅ |
| 8 | cmux (16 WS) | `/private/tmp/cmux.sock` | ✅ |

---

## 4. 通信フロー

### Inbound: User → CC

`$tex SSE調査して` → Bridge poll (5s) → workspace解決 → `surface.send_text` + `surface.send_key` → CC receives input

### Outbound: CC → User

| Route | Trigger | Method | Push | Latency |
|-------|---------|--------|------|---------|
| Record+Push | タスク開始/完了 | Asana→Workflow→Slack | ✅ bot名義 | ~10-40s |
| Immediate | 進捗/質問/エラー | curl Webhook | ✅ Webhook名義 | ~2s |
| Record only | 経過記録 | Asana comment | ❌ | N/A |

### 並行発火パターン

進捗/質問/エラー時: `asana_comment_write` (記録) + `curl Webhook` (即時通知) を同時実行

---

## 5. 自己報告プロトコル

| Event | Asana | Webhook | Section Move |
|-------|-------|---------|-------------|
| 作業開始 | task create | — | Backlog→In Progress |
| 進捗 | comment | curl (並行) | — |
| 質問・ブロック | comment | curl (並行) | — |
| エラー | comment | curl (並行) | — |
| 作業完了 | task complete | — | →Done |

### Webhookメッセージフォーマット

- `✅ [project] 完了内容`
- `❓ [project] 質問内容`
- `❌ [project] エラー内容`
- `📊 [project] 進捗内容`

### Asanaタスク命名

`🤖 [プロジェクト名] タスク概要`

### エラー自己回復（計画中）

Error → Retry (max 2) → Success: continue + report / Failure: Webhook + STOP

### `$status` コマンド（計画中）

全WSの現在タスク状況をSlackに一覧表示

---

## 6. cmux マルチペイン対応（設計中）

### 階層: cmux → Window → Workspace → Pane → Surface

| Command | 動作 | Status |
|---------|------|--------|
| `$workspace command` | focused surface に送信 | ✅ |
| `$workspace:N command` | 特定 surface N に送信 | Planned |
| `$list` | workspace 一覧 | ✅ |
| `$list:N` | workspace N の surface 一覧 | Planned |

詳細: `notes/cmux-multi-pane-design.md`

---

## 7. 設計判断ログ

| ID | Decision | Reason |
|----|----------|--------|
| D1 | AISmith Auth Reuse | PATブロック、OAuth個人不可 → Midway SSO cookie唯一のパス |
| D2 | Asana + Webhook Hybrid | Workflow comment trigger不可 → Webhook必須。post_message=自分名義=Push通知なし |
| D3 | Socket Direct > CLI | cmux CLI=インタラクティブ設計、SIGPIPE → Socket JSON-RPC |
| D4 | cmux WS > LaunchAgent | Mach Bootstrapセッション分離 → LaunchAgentからcmux到達不能 |
| D5 | SSH不要 | Director Mode不一致、16並列非現実的、Self-reportingで代替 |
| D6 | Bridge双方向化不要 | Webhookで CC→User を十分カバー、複雑度増大でROI低 |
| D7 | OSS MCP不可 | Corporate認証互換性なし |
| D8 | AISmith Fork見送り | 工数8-13日 vs MCP SDK + Auth参考で0日 |

---

## 8. 棄却済みアプローチ

| Approach | Why Rejected |
|----------|-------------|
| OSS MCP Servers | Amazon Corporate認証ブロック |
| AISmith Full Fork | 工数8-13日 vs 0日 |
| PAT | 管理者ブロック |
| Slack post_message notifications | 自分名義=Push通知なし |
| LaunchAgent | Mach Bootstrapセッション分離 |
| SSH + Termius | Director Mode不一致 |
| OpenClaw | CorpSec BAN (2026-02-04) |
| Bridge双方向化 | Webhookで代替 |
| /rc Remote Control | Max plan必須、Bedrock非互換 |
| claude.ai/code | ローカルMCPアクセス不可 |
| cmux CLI (execSync) | SIGPIPE → Socket直接で解決 |

---

## 9. 残タスク

| Priority | Task | Type |
|----------|------|------|
| P0 | Self-reporting protocol強化 | CLAUDE.md |
| P0 | Error self-recovery protocol | CLAUDE.md |
| P1 | `$status` dashboard command | Code |
| P1 | Multi-pane support in bridge | Code |
| P2 | Lambda approval confirmation | Waiting |
| P3 | Asana test task cleanup | Minor |

---

## Appendix: Key IDs

| Resource | ID |
|----------|----|
| Asana Project | `1213488615214853` |
| Asana Assignee | `1212641864720047` |
| Slack Channel | `C0AJ12G6A04` |
| Webhook URL | `https://hooks.slack.com/triggers/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` |
| Section: Backlog | `1213488615214856` |
| Section: In Progress | `1213488615214857` |
| Section: Done | `1213488615214854` |

*Last updated: 2026-03-03 - Version 2.0*
