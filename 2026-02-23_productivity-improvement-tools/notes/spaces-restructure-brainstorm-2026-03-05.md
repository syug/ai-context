# Spaces管理再構築ブレスト（2026-03-05）

## 背景

cmux導入後、全ターミナルが1ウィンドウに統合され、16 macOS Spaces に Chrome/Finder を分散する意味が薄れた。Spaces切替アニメーションも遅く、cognitive overhead が高い。

## ライブ環境調査結果（Claude分析）

- Chrome **27ウィンドウ**が開いている（タイトルでプロジェクト識別可能）
- **Bunch が実は稼働中**（廃止判断したはずが11 `.bunch` ファイル健在）
- AppleScript/JXA で Chrome ウィンドウの列挙・位置制御・index操作が**動作確認済み**
- Chrome Tab Groups は AppleScript から**アクセス不可**
- Rectangle Pro URL scheme `rectangle-pro://execute-layout?name=...` が利用可能

## 提案一覧（Gemini + Claude 統合）

### A. cmux-First Bridge（半日・Phase 1）

cmuxワークスペース切替に連動して Chrome 窓を前面化。

```
cmuxワークスペース切替 → バックグラウンドスクリプトが検知
→ 該当プロジェクトの Chrome ウィンドウを `set index to 1` で前面化
```

- **Pros:** 30分で作れる、非破壊的、失敗しても何も壊れない
- **Cons:** 他のウィンドウを隠さない（前面に出すだけ）

### B. Single-Space Context Swapper（2-3日）

Spaces を 2-3 に削減（Comms / Work / Personal）。Raycast Extension が：
1. 全アプリを隠す
2. プロジェクトの Chrome Profile/ウィンドウを表示
3. cmux 切替
4. Rectangle Pro レイアウト適用

- **Pros:** 既存ツール活用、キーボード一発で全切替
- **Cons:** アプリ単位の show/hide → Chrome 27窓の中から3つだけ出す、ができない

### C. Zero Spaces — 仮想コンテキスト（4-5日・Phase 2）

Spaces を完全廃止。全ウィンドウを1デスクトップに置き、JXA で「オフスクリーン移動」で擬似コンテキスト切替。

```javascript
// 関連ウィンドウ → 保存位置に復元
w.position = savedPositions[w.name()];
// 無関係ウィンドウ → 画面外に追放
w.position = [-10000, 0];
```

**唯一「Chrome 27窓のうち3つだけ表示」が可能な方式。**

- **Pros:** ウィンドウ単位の粒度制御、Spacesアニメなし、可逆的
- **Cons:** 実装が最も重い、Mission Control に全窓表示される

### D. Chrome Profiles 分離（低工数）

プロジェクトごとに Chrome Profile を作成。Contexts アプリでプロファイル名検索。

- **Pros:** Cookie/認証が完全分離
- **Cons:** Profile 間のタブ移動不可、管理煩雑

### E. Bunch Revival（1-2日）

4カテゴリ Spaces に削減 + Bunch の `@@`（全隠し）+ 個別表示でフォーカスモード。

- **Pros:** 既存 `.bunch` ファイル11個が即活用可
- **Cons:** Tahoe での不安定性リスク

## 採用ロードマップ

```
Phase 1（今日）: A. cmux-First Bridge
  → 即効性あり、リスクゼロ

Phase 2（今週）: C. Zero Spaces の Raycast コマンド版
  → Chrome ウィンドウのオフスクリーン制御から着手
  → contexts.json にプロジェクト定義（URL/タイトルパターン）

Phase 3（安定後）: Spaces を 16 → 2-4 に削減 or 全廃
  → cmux + Raycast が全コンテキスト切替を担う
```

## 参加AI

- **Gemini CLI** — プロダクティビティシステム設計の観点（提案 B, D を主導）
- **Claude（深層分析）** — 現環境のライブ調査 + 技術的実現可能性（提案 A, C, E を主導）
- **Kiro CLI** — CLIインタフェースの問題で参加できず（stdin `-` フラグ問題）

---

## P1 実装結果（2026-03-05）

**Phase 1: cmux-First Bridge → 完了**

tmux `client-session-changed` フックで実装。当初の「cmuxワークスペース切替検知」からピボットし、tmuxのネイティブフック機構を活用。

### 作成ファイル

| ファイル | 内容 |
|---------|------|
| `~/.config/project-focus/contexts.json` | 16プロジェクト→Chromeタイトルパターン |
| `~/.config/project-focus/bridge.sh` | bash+python3+osascript ブリッジ |
| `~/.tmux.conf` (追記) | `client-session-changed` フック |

### 技術的決定

- **フック:** `client-session-changed`（`session-changed`ではない — tmux 3.6aで確認）
- **バックグラウンド実行:** `run-shell -b` でセッション切替をブロックしない
- **JSON解析:** python3 を使用（日本語プロジェクト名のUnicode対応）
- **マッチング:** セッション名から先頭数字・末尾`-N`除去 → 大文字小文字無視の双方向部分文字列マッチ
- **Chrome操作:** `set index of window to 1` で前面化（最軽量・非破壊）
- **ログ:** `~/.config/project-focus/bridge.log`（100KB自動ローテーション）
