# Handover Document
**Topic:** Brand Store Preview URL変換スキルの作成
**Date:** 2026-02-24
**Status:** 完了

---

## 背景

Brand Store Preview URLは、パスワード（key）と有効期限（expirationTime）が埋め込まれた形式で共有される。VPN接続時にはこれらのパラメータが不要で、`isPreview` と `storeId` のみでアクセス可能。

手動でURLからパラメータを削除するのは面倒なので、Claude Codeスキルとして自動変換ツールを作成した。

## 現在の状況

### 作成したスキル

- **スキル名**: `/store-preview`
- **ファイル**: `/Users/saitshug/Development/repos/brazil-ws/Prototypes/.claude/commands/store-preview.md`
- **機能**: 入力URLから `isPreview` と `storeId` パラメータのみを残し、他を削除

### 対応するURL形式

1. `https://www.amazon.com/stores/page/{pageId}?isPreview=1&key=...&storeId=...&expirationTime=...`
2. `https://advertising.amazon.com.au/builder/openRetailPage?isPreview=true&pageId=...&storeId=...`
3. `https://www.amazon.com.au/stores/page/{pageId}?isPreview=1&key=...&storeId=...&isPasswordKey=1&expirationTime=...`

### 変換例

**入力:**
```
https://www.amazon.com.au/stores/page/90F570DA-A958-4EE9-94C5-F233AFD3EBC5?isPreview=1&key=AAA...&storeId=899F00B2-17F3-4B45-B70E-9BE16684BF9E&isPasswordKey=1&expirationTime=1773702664323
```

**出力:**
```
https://www.amazon.com.au/stores/page/90F570DA-A958-4EE9-94C5-F233AFD3EBC5?isPreview=1&storeId=899F00B2-17F3-4B45-B70E-9BE16684BF9E
```

## 成果物一覧

```
/Users/saitshug/Development/repos/brazil-ws/Prototypes/
└── .claude/
    └── commands/
        └── store-preview.md    # 作成したスキル定義
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | - | スキルファイル作成 | 完了 |
| 2 | - | スキル名を `/store-preview` に変更 | 完了 |
| 3 | - | 新セッションで動作確認 | 未実施（セッション再起動後に `/store-preview` が有効になる） |

## 重要な判断ログ

- **スキル配置場所**: プロジェクトローカル (`.claude/commands/`) に配置。グローバル (`~/.claude/commands/`) ではなくプロジェクト固有とした
- **パラメータ選定**: `isPreview` と `storeId` のみ残す。`pageId` はURLパスに含まれているため不要
- **スキル名変更**: `/preview-url` → `/store-preview`（より簡潔で覚えやすい名前に）
