# Handover Document
**Topic:** Store URL変換スキルの作成
**Date:** 2026-03-09
**Status:** 完了

---

## 背景

Amazon Store のプレビューURLには `key`, `expirationTime` 等の長いパラメータが付与されており、共有や記録に不便。短縮形式への変換ルールを確立し、再利用可能なClaude Codeスキルとして実装した。

## 現在の状況

### 変換ルール確定

試行錯誤の結果、以下の最小形式に確定:

```
https://www.amazon.{TLD}/stores/page/{PAGE_ID}?isPreview=1&storeId={STORE_ID}
```

- `PAGE_ID`: `page/` の後のUUID（元URLそのまま）
- `STORE_ID`: `storeId` パラメータの値（元URLそのまま）
- 除去対象: `key`, `expirationTime`, `deviceType`, `isPasswordKey`

### 試した中間形式（不採用）

1. `page/{STORE_ID}?isPreview=1&storeId={STORE_ID}` — PAGE_IDをSTORE_IDで置換 → 不正確
2. `?deviceType=Desktop&isPreview=1&isPasswordKey=0&storeId={STORE_ID}&key=` — パラメータ過多

### 成果物

- **スキル**: `~/.claude/skills/store-url-convert/SKILL.md` — `/store-url-convert <URL>` で呼び出し可能
- **メモリ**: `MEMORY.md` に変換ルールを追記済み

## 成果物一覧

```
~/.claude/skills/store-url-convert/
└── SKILL.md          — スキル定義（変換ルール・手順）

~/.claude/projects/-Users-saitshug/memory/
└── MEMORY.md         — Store URL Convert セクション追記
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | — | スキル作成 (`/store-url-convert`) | 完了 |
| 2 | — | メモリに変換ルール記録 | 完了 |

## 重要な判断ログ

- `PAGE_ID` と `STORE_ID` は異なる値になりうるため、両方とも元URLの値を保持する方針にした（STORE_IDで統一する案は不採用）
- 最小パラメータセットは `isPreview=1` と `storeId` の2つのみ。`deviceType`, `isPasswordKey`, `key`（空値）は不要と確認済み
