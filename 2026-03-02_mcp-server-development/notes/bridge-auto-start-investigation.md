# Slack↔CC ブリッジ自動起動 調査メモ

**Date:** 2026-03-06
**Status:** 調査完了 → 移行計画策定中

---

## 経緯

### Phase 1: LaunchAgent で常駐化を試行（2026-03-03）

- `~/Library/LaunchAgents/com.saitshug.claude-slack-bridge.plist` を作成
- **結果:** ConnectionRefused で失敗
- **原因:** macOS Mach Bootstrap セッション隔離 — LaunchAgent プロセスは cmux とは別のセッション空間で動くため、`/private/tmp/cmux.sock` に接続不可

### Phase 2: 方針転換 — cmux ワークスペース内実行（2026-03-03）

- LaunchAgent を断念・plist 削除
- cmux ワークスペース内で `start.sh` を手動実行する方式に変更
- `start.sh`: `while true` ループで異常終了時に5秒後自動再起動
- ログ: `/tmp/claude-slack-bridge.log`, `/tmp/claude-slack-bridge.error.log`

### Phase 3: tmux 全面移行の影響（2026-03-05〜）

- ブリッジを cmux ソケット → `tmux send-keys` に切替予定（handover アクション #30）
- tmux はユーザーセッション内で動くため、LaunchAgent からも `tmux send-keys` は実行可能
- → **tmux 移行完了後に LaunchAgent 化が可能になる**

---

## 現在の状態（2026-03-06 確認）

- ブリッジは **停止中**（最終稼働: 2026-03-04）
- LaunchAgent: なし（plist 削除済み）
- cmux hook: 未設定（`cmux set-hook --list` → "No hooks configured"）
- fish config: ブリッジ関連の記述なし

## ブリッジのアーキテクチャ

```
Slack #ai--mission-control
  ↕ (Slack MCP / ポーリング)
claude-slack-bridge (node dist/bridge.js)
  ↕ (現在: cmux Unix ソケット RPC → 移行後: tmux send-keys)
Claude Code セッション (WS1〜16)
```

## 自動起動の選択肢と制約

| 方式 | 現在（cmux ソケット依存） | tmux 移行後 |
|------|--------------------------|-------------|
| LaunchAgent | ❌ Mach Bootstrap 隔離 | ✅ tmux send-keys なら問題なし |
| cmux ペイン内 start.sh | ✅ 現行方式（手動起動） | 不要になる |
| fish config | ⚠️ 重複防止が面倒 | ⚠️ 同上 |
| cmux set-hook | 未検証（フック機構あり） | 不要になる |

## 結論

1. **短期:** cmux ペイン内で `start.sh` を手動起動（現行踏襲）
2. **中期:** tmux Phase 3（ブリッジを tmux send-keys に切替）完了後、LaunchAgent で完全自動化
3. LaunchAgent の Mach Bootstrap 問題は tmux 移行で根本解決される

## 関連ファイル

- `~/Development/claude-slack-bridge/start.sh` — 起動スクリプト
- `~/Development/claude-slack-bridge/src/bridge.ts` — ブリッジ本体
- `~/.config/sesh/sesh.toml` — tmux セッション定義
- `~/.config/fish/config.fish` — cmux→tmux 自動アタッチ設定
