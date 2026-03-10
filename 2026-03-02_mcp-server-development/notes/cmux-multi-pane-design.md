# cmux Multi-Pane Support 設計書

**作成日:** 2026-03-03
**対象:** claude-slack-bridge (`~/Development/claude-slack-bridge/src/bridge.ts`)
**ステータス:** Draft

---

## 1. 背景

現在の Slack → cmux bridge は workspace 単位でテキストを送信する。
cmux の各 workspace は複数の surface（tmux の pane に相当）を持てるが、
bridge はこれを区別せず、常に workspace のデフォルト（focused）surface に送信している。

multi-pane 環境では、特定の surface（例: 左ペインの Claude Code、右ペインの shell）に
ピンポイントでコマンドを送りたいケースがある。

---

## 2. コマンド構文仕様

### 2.1 基本構文

```
$<workspace>[:<surface>] <instruction>
```

| 構文 | 動作 |
|------|------|
| `$6 テスト` | workspace 6 の focused surface にテキスト送信（現行動作） |
| `$6:2 テスト` | workspace 6 の surface index 2 にテキスト送信 |
| `$tex:1 ls -la` | workspace "tex" の surface index 1 にテキスト送信 |
| `$list` | workspace 一覧を表示（現行動作） |
| `$list:6` | workspace 6 の surface 一覧を表示（新規） |
| `$list:tex` | workspace "tex" の surface 一覧を表示（新規） |
| `$all テスト` | 全 workspace の focused surface に送信（現行動作） |
| `$all:all テスト` | 全 workspace の全 surface に送信（新規・オプション） |

### 2.2 構文パース規則

targetName の `:` を境界として分割する:

```
targetName = "6:2"
  → workspacePart = "6"
  → surfacePart  = "2"

targetName = "tex"
  → workspacePart = "tex"
  → surfacePart  = undefined (focused surface を使用)

targetName = "list:6"
  → special command: list surfaces of workspace 6
```

### 2.3 Surface Index 体系

- cmux が返す surface ref は `"surface:23"` のような内部ID
- ユーザー向けには **1-based index** を使用（surface.list の返却順序に基づく）
- cmux の `surface.list` が返す `index` フィールドがあればそれを使用、なければ配列順

---

## 3. 全コマンド例

### 3.1 Workspace 一覧（現行）

```
$list
```

Slack レスポンス:
```
🤖 Workspaces:
  1. 📊 確定申告 ($確定申告 or $1)
  6. 🔧 tex-sse ($tex-sse or $6)
  7. 🌐 slack-bridge ($slack-bridge or $7)
```

### 3.2 Surface 一覧（新規）

```
$list:6
```

Slack レスポンス:
```
🤖 Surfaces in workspace 6 (🔧 tex-sse):
  1. terminal ★ (focused)
  2. terminal
  3. browser
```

Surface が1つだけの場合:
```
🤖 Surfaces in workspace 7 (🌐 slack-bridge):
  1. terminal ★ (focused, only surface)
```

### 3.3 特定 Surface への送信（新規）

```
$6:2 テスト
```

Slack レスポンス（なし — 現行と同じく送信成功時は silent）

ログ出力:
```
[bridge] Sent to workspace:6/surface:23: テスト
```

### 3.4 デフォルト Surface への送信（現行互換）

```
$6 テスト
```

動作: surface パラメータなしで `surface.send_text` を呼ぶ（cmux がフォーカス中の surface に送る）

### 3.5 全 Workspace 送信（現行互換）

```
$all handover saveして
```

動作: 全 workspace の focused surface に送信（surface 指定なし）

---

## 4. Bridge コード変更

### 4.1 新規 Interface

```typescript
interface CmuxSurface {
  ref: string;       // "surface:23"
  title: string;     // surface title (if any)
  type: string;      // "terminal" | "browser" | etc.
  focused: boolean;  // whether this surface is focused
  index: number;     // 1-based user-facing index
}
```

### 4.2 新規関数: `listSurfaces`

```typescript
async function listSurfaces(workspaceRef: string): Promise<CmuxSurface[]> {
  const resp = await cmuxRpc("surface.list", { workspace: workspaceRef });
  if (!resp.ok || !resp.result) return [];

  const result = resp.result as {
    surfaces?: Array<{
      ref: string;
      title?: string;
      type?: string;
      focused?: boolean;
      index?: number;
    }>;
  };

  if (!result.surfaces) return [];

  return result.surfaces.map((s, i) => ({
    ref: s.ref,
    title: s.title || "",
    type: s.type || "unknown",
    focused: s.focused || false,
    index: s.index ?? (i + 1),  // 1-based fallback
  }));
}
```

### 4.3 新規関数: `findSurface`

```typescript
function findSurface(
  surfaceId: string,
  surfaces: CmuxSurface[]
): CmuxSurface | null {
  // 数字の場合は index で検索（1-based）
  const num = parseInt(surfaceId, 10);
  if (!isNaN(num)) {
    return surfaces.find((s) => s.index === num) || null;
  }
  // 文字列の場合は type で部分一致（将来拡張用）
  return surfaces.find((s) => s.type.includes(surfaceId)) || null;
}
```

### 4.4 `sendToCmux` の変更

```typescript
async function sendToCmux(
  workspaceRef: string,
  text: string,
  surfaceRef?: string   // ← 新規オプション引数
): Promise<void> {
  try {
    const params: Record<string, unknown> = {
      workspace: workspaceRef,
      text,
    };
    if (surfaceRef) {
      params.surface = surfaceRef;
    }
    await cmuxRpc("surface.send_text", params);

    const keyParams: Record<string, unknown> = {
      workspace: workspaceRef,
      key: "enter",
    };
    if (surfaceRef) {
      keyParams.surface = surfaceRef;
    }
    await cmuxRpc("surface.send_key", keyParams);

    const target = surfaceRef
      ? `${workspaceRef}/${surfaceRef}`
      : workspaceRef;
    console.log(`[bridge] Sent to ${target}: ${text.substring(0, 80)}`);
  } catch (error) {
    console.error(`[bridge] Failed to send to ${workspaceRef}:`, error);
  }
}
```

### 4.5 コマンドパーサーの変更

`poll` 関数内のパース処理を以下のように変更する:

```typescript
// Parse target: workspace:surface pattern
const colonIdx = targetName.indexOf(":");
let workspacePart: string;
let surfacePart: string | undefined;

if (colonIdx !== -1) {
  workspacePart = targetName.substring(0, colonIdx);
  surfacePart = targetName.substring(colonIdx + 1);
} else {
  workspacePart = targetName;
  surfacePart = undefined;
}

// --- $list と $list:N の分岐 ---
if (workspacePart === "list") {
  if (surfacePart) {
    // $list:N → surface 一覧を表示
    const target = findWorkspace(surfacePart, workspaces);
    if (!target) {
      await postToSlack(client,
        `🤖 Unknown workspace: "${surfacePart}". Try $list`
      );
      continue;
    }
    const surfaces = await listSurfaces(target.ref);
    if (surfaces.length === 0) {
      await postToSlack(client,
        `🤖 No surfaces found in workspace ${target.index} (${target.name})`
      );
      continue;
    }
    const list = surfaces
      .map((s) => {
        const focused = s.focused ? " ★ (focused)" : "";
        const only = surfaces.length === 1 ? ", only surface" : "";
        return `  ${s.index}. ${s.type}${focused}${only}`;
      })
      .join("\n");
    await postToSlack(client,
      `🤖 Surfaces in workspace ${target.index} (${target.name}):\n${list}`
    );
    continue;
  } else {
    // $list → 既存のworkspace一覧（変更なし）
    // ...existing code...
    continue;
  }
}

// --- $all の処理（変更なし） ---
if (workspacePart === "all" && instruction) {
  // ...existing code...
  continue;
}

// --- 通常の送信処理 ---
const target = findWorkspace(workspacePart, workspaces);
if (!target) {
  await postToSlack(client,
    `🤖 Unknown workspace: "${workspacePart}". Try $list`
  );
  continue;
}

if (!instruction) continue;

if (surfacePart) {
  // Surface 指定あり → 解決してから送信
  const surfaces = await listSurfaces(target.ref);
  const surface = findSurface(surfacePart, surfaces);
  if (!surface) {
    await postToSlack(client,
      `🤖 Surface "${surfacePart}" not found in workspace ${target.index} (${target.name}). ` +
      `Available: ${surfaces.map((s) => s.index).join(", ")}. Try $list:${target.index}`
    );
    continue;
  }
  await sendToCmux(target.ref, instruction, surface.ref);
} else {
  // Surface 指定なし → focused surface（現行動作）
  await sendToCmux(target.ref, instruction);
}
```

---

## 5. Slack メッセージフォーマット

### 5.1 Surface 一覧

```
🤖 Surfaces in workspace 6 (🔧 tex-sse):
  1. terminal ★ (focused)
  2. terminal
  3. browser
```

### 5.2 Surface Not Found エラー

```
🤖 Surface "5" not found in workspace 6 (🔧 tex-sse). Available: 1, 2, 3. Try $list:6
```

### 5.3 Workspace Not Found エラー（既存を維持）

```
🤖 Unknown workspace: "foo". Try $list
```

### 5.4 Surface なし（空の workspace）

```
🤖 No surfaces found in workspace 6 (🔧 tex-sse)
```

---

## 6. Edge Cases

### 6.1 Workspace に Surface が1つだけ

- `$6:1 テスト` → surface ref を指定して送信（正常動作）
- `$6 テスト` → surface 未指定で送信（cmux がデフォルトを使う、現行と同じ）
- 両方とも同じ結果になるが、明示的な指定も受け付ける

### 6.2 Surface Index が範囲外

```
$6:99 テスト
→ 🤖 Surface "99" not found in workspace 6 (🔧 tex-sse). Available: 1, 2, 3. Try $list:6
```

### 6.3 Workspace が存在しない場合の `$list:N`

```
$list:99
→ 🤖 Unknown workspace: "99". Try $list
```

### 6.4 `:` が instruction テキストに含まれる

パースは `targetName`（最初のスペースまで）内の `:` のみを解釈する。
instruction 部分の `:` は影響しない。

```
$6 echo "hello:world"
→ workspacePart = "6", surfacePart = undefined, instruction = 'echo "hello:world"'

$6:2 echo "hello:world"
→ workspacePart = "6", surfacePart = "2", instruction = 'echo "hello:world"'
```

### 6.5 `$all:all` 全 workspace 全 surface（将来拡張）

初期実装ではスコープ外とする。必要になった時点で追加可能:

```typescript
if (workspacePart === "all" && surfacePart === "all" && instruction) {
  for (const ws of workspaces) {
    const surfaces = await listSurfaces(ws.ref);
    for (const s of surfaces) {
      await sendToCmux(ws.ref, instruction, s.ref);
    }
  }
}
```

### 6.6 Surface ref のキャッシュ

`surface.list` は毎回 RPC 呼び出しが発生する。
workspace 一覧は毎ポーリングサイクルで更新しているが、surface 一覧は
**コマンド実行時のみ取得** する（オンデマンド）。

理由:
- Surface の構成変更は workspace 変更より低頻度
- 毎サイクル全 workspace の surface を取得するとRPC負荷が増大
- 送信時に最新の surface ref を取得する方が正確

### 6.7 `$list` の拡張表示（オプション）

将来的に `$list` の出力に surface 数を追加することも検討:

```
🤖 Workspaces:
  1. 📊 確定申告 ($確定申告 or $1) [3 surfaces]
  6. 🔧 tex-sse ($tex-sse or $6) [2 surfaces]
  7. 🌐 slack-bridge ($slack-bridge or $7) [1 surface]
```

初期実装では不要（RPC呼び出し増加のため）。

---

## 7. 実装計画

### Phase 1: 最小実装

1. `CmuxSurface` interface 追加
2. `listSurfaces()` 関数追加
3. `findSurface()` 関数追加
4. `sendToCmux()` に `surfaceRef` オプション引数追加
5. コマンドパーサーで `:` 分割ロジック追加
6. `$list:N` コマンドハンドラ追加
7. `$workspace:surface` 送信ロジック追加

### Phase 2: 品質向上（オプション）

- `$list` に surface 数を表示
- `$all:all` サポート
- Surface type 別のアイコン表示（terminal=`>_`, browser=`🌐`）

### 既存動作への影響

- `$list` → 変更なし
- `$N instruction` → 変更なし（surfacePart = undefined のパスを通る）
- `$name instruction` → 変更なし
- `$all instruction` → 変更なし

`:` を含まない既存コマンドは全て現行と同じパスを通るため、後方互換性は完全に維持される。

---

## 8. テスト方針

### 手動テスト項目

| # | コマンド | 期待結果 |
|---|---------|---------|
| 1 | `$list` | workspace 一覧（現行と同じ） |
| 2 | `$list:N` | workspace N の surface 一覧 |
| 3 | `$list:invalidname` | "Unknown workspace" エラー |
| 4 | `$N テスト` | focused surface に送信（現行と同じ） |
| 5 | `$N:1 テスト` | surface 1 に送信 |
| 6 | `$N:2 テスト` | surface 2 に送信 |
| 7 | `$N:99 テスト` | "Surface not found" エラー |
| 8 | `$name:1 テスト` | 名前指定 + surface 指定 |
| 9 | `$all テスト` | 全 workspace focused に送信 |
| 10 | `$6 echo "a:b"` | instruction 内の `:` が影響しないこと |
