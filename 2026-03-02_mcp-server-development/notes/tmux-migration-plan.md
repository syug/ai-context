# tmux 全面移行計画

**作成日:** 2026-03-05
**ステータス:** 承認済み・実装前

---

## 1. 目的

cmux ペイン内の全ターミナルセッションを tmux session 化し、ブリッジの送信を `tmux send-keys` に切替える。

**動機:**
- cmux API の癖（workspace_id vs workspace、UUID vs ref、\r ハック）を排除
- 1コマンドで確実に送信（3 RPC → 1 exec）
- スリープ復帰時の cmux ソケット断続切れを回避
- `tmux capture-pane` で出力読み取り可能（将来の self-reporting に有用）
- sesh によるセッション定義の一元管理

## 2. アーキテクチャ

### Before（現在）

```
User → Slack → Bridge → cmux RPC (surface.list → send_text → send_text \r)
                         ↓
                    cmux surface (直接ターミナル)
```

### After（移行後）

```
User → Slack → Bridge → tmux send-keys -t {session} "text" Enter
                         ↓
                    cmux pane → tmux attach → tmux session → claude
```

cmux は GUI シェル（ワークスペース表示、キーボードショートカット）として残す。
データ転送（テキスト送信）は tmux 経由。

## 3. 命名規則

```
{ws#}-{tab#}
```

| 例 | 意味 |
|----|------|
| `6-1` | WS6 タブ1 |
| `6-2` | WS6 タブ2 |
| `14-1` | WS14 タブ1 |

### ブリッジのルーティング

```
$6 テスト     → tmux send-keys -t 6-1 "📱 [Slack:6:TS] テスト" Enter
$6:2 テスト   → tmux send-keys -t 6-2 "📱 [Slack:6:TS] テスト" Enter
$14 テスト    → tmux send-keys -t 14-1 "📱 [Slack:14:TS] テスト" Enter
$list         → cmux workspace.list（従来通り） + tmux session 数を表示
```

## 4. sesh 設定（sesh.toml）

```toml
# ~/.config/sesh/sesh.toml
# 全 cmux ワークスペース × タブの tmux session 定義
# sesh connect {name} で接続（なければ自動作成 + claude 起動）

[[session]]
name = "1-1"
path = "~"
startup_command = "claude"

[[session]]
name = "2-1"
path = "~"
startup_command = "claude"

# ... 全セッション
```

- `path` はプロジェクトごとに設定可能（claude の起動ディレクトリ）
- `startup_command = "claude"` でセッション作成時に自動起動
- cmux ペインから `sesh connect 6-1` で接続

## 5. 移行手順

### Phase 1: sesh.toml 作成

1. 全16WS のタブ構成を確認（cmux surface.list で各WSのsurface数を取得）
2. `~/.config/sesh/sesh.toml` に全セッション定義を書く
3. 各セッションの `path` を適切なプロジェクトディレクトリに設定

### Phase 2: tmux session 一括作成 + cmux ペイン接続

1. スクリプトで全 tmux session をバックグラウンド作成:
   ```bash
   for session in 1-1 2-1 3-1 ... ; do
     sesh connect "$session"  # なければ作成、あれば接続
   done
   ```
2. 各 cmux ペインで `sesh connect {name}` を実行（cmux RPC `surface.send_text` で自動化可能）
3. 既存の直接起動 CC セッションは tmux 内に移行（新規 claude 起動）

### Phase 3: ブリッジ切替

1. `bridge.ts` の `sendToSurface` / `sendToCmux` を `tmux send-keys` に置換
2. `listSurfaces` は cmux API を維持（$list:N 用）
3. ビルド → テスト → デプロイ

### Phase 4: 検証

1. `$list` — WS一覧表示（cmux API）
2. `$6 テスト` — tmux send-keys でタブ1に送信
3. `$6:2 テスト` — tmux send-keys でタブ2に送信
4. `$all テスト` — 全WSに送信
5. スレッド返信 — threadTs が維持されること
6. スリープ復帰後の動作

## 6. ブリッジコード変更箇所

### 削除するもの
- `resolveSurfaceUUIDs()` — UUID キャッシュ不要に
- `listSurfaces()` での UUID 取得 — セッション名で直接送信
- `surface.send_text` / `surface.send_key` の呼び出し
- `\r` ハック

### 追加するもの
```typescript
import { execSync } from "node:child_process";

function sendViaTmux(sessionName: string, text: string): boolean {
  try {
    // Escape single quotes in text for shell
    const escaped = text.replace(/'/g, "'\\''");
    execSync(`tmux send-keys -t '${sessionName}' '${escaped}' Enter`, {
      timeout: 5000,
    });
    return true;
  } catch (error) {
    console.error(`[bridge] tmux send-keys failed for ${sessionName}:`, error);
    return false;
  }
}
```

### 変更するもの
- `sendToCmux(ws, text)` → `sendViaTmux(`${ws.index}-1`, text)`
- `sendToSurface(...)` → `sendViaTmux(`${ws.index}-${surfIdx}`, text)`
- `$list` は cmux `workspace.list` を維持

## 7. リスクと対策

| リスク | 対策 |
|--------|------|
| tmux server がダウン | `tmux has-session` でチェック、ログに警告 |
| セッション名が存在しない | `sesh connect` で自動再作成（sesh.toml 定義あり） |
| cmux ペインと tmux の接続が切れる | cmux ペインで `sesh connect` を再実行 |
| 既存CCセッションのコンテキスト消失 | 移行前に全WSで `/handover save` |

## 8. 将来の拡張

- `tmux capture-pane -t {session} -p` でCC出力を読み取り → self-reporting protocol に活用
- `tmux pipe-pane` でリアルタイム出力監視 → `$status` dashboard の実装
- tmux hook (`after-split-window` 等) で新ペイン作成時に自動セッション登録
