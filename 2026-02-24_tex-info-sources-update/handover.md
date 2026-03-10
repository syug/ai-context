# Handover Document
**Topic:** TEX 情報源マスターテーブル チェック・更新（v5.1 → OP1 v2 追加 + 2027 OP1 調査）
**Date:** 2026-03-03
**Status:** 進行中

---

## 背景
TEXチームの情報源マスターテーブル（TEX-Info-Sources.html / .md）の定期チェックと更新。v4→v5（2026-02-24）、v5→v5.1（2026-03-02）に続き、本セッション（2026-03-03）ではFY26 OP1 v2 docxの追加と、2027 OP1の存在調査を実施。

## 現在の状況

### 2027 OP1 調査結果
- Slack・Wiki・メールいずれにも **TEX 2027 OP1 はまだ存在しない**（2026-03-03時点）
- FY26 OP1の実績から推測: **3月末〜4月にキックオフ見込み**
  - FY26: 3月末 Mirko がWorking Groupキックオフ → 4/10 インプット期限 → 4月末 amjias が最終版共有
- ウォッチすべきチャンネル: `#bil-ww-tex`、`#eu-apac-op1-working-group`
- キーパーソン: mirkocap（ドラフティング主導）、amjias（TEX global lead）

### FY26 OP1 参考リソース
| リソース | 場所 |
|---------|------|
| FY26 OP1 Quip | https://quip-amazon.com/obz5A5UhfbsX |
| FY26 OP1 docx (v2) | OneDrive `Goals/TEX-FY26-OP1-0423250-v2.docx` |
| FY26 OP1 PDF (初版) | OneDrive `Goals/TEX-FY26-OP1-041325.pdf` |
| FY25 OP1 PDF | Slackから取得可能（`2025+BIL+TEX+OP1.pdf`） |

### TEX-Info-Sources 更新内容（本セッション）
1. **md + html の日付を 2026-03-03 に更新**、変更ログに「OP1 v2 docx追加」を追記
2. **Goals/OP セクションに OP1 v2 docx サブ行を追加**（`↳ OP1 v2 (.docx)` — パス: `Goals/TEX-FY26-OP1-0423250-v2.docx`）
3. 既存の PDF行・Quip行はそのまま保持

### ファイル構成
- **Source of Truth:** `TEX-Info-Sources.md`（Markdown）
- **HTML:** カスタムスタイル付き手作りHTML（今回 md / html 両方を更新）
- **PDF:** Chrome headless で生成（今回は未再生成）
- **パス:** `/Users/saitshug/Library/CloudStorage/OneDrive-amazon.com/Team/1. TEX/`

## 成果物一覧
```
2026-02-24_tex-info-sources-update/
├── handover.md（本ファイル — OP1 v2 追加 + 2027 OP1 調査を反映）
├── history/
│   ├── 2026-02-24_handover.md（v4→v5 更新時のアーカイブ）
│   └── 2026-03-02_handover.md（v5→v5.1 更新時のアーカイブ）
├── artifacts/（なし — 成果物は OneDrive 上に直接更新）
└── notes/（なし）
```

外部ファイル（OneDrive上）:
- `TEX-Info-Sources.html`（OP1 v2 追加済み — 2026-03-03更新）
- `TEX-Info-Sources.md`（OP1 v2 追加済み — 2026-03-03更新）
- `TEX-Info-Sources.pdf`（未再生成 — v5のまま）
- `Goals/TEX-FY26-OP1-0423250-v2.docx`（新規追加 — Slackからダウンロード）

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | - | QBR FINAL エントリ追加 | ✅ 完了（v5） |
| 2 | - | OneDrive フォルダパス更新 | ✅ 完了（v5） |
| 3 | - | ミーティングノートパス修正 | ✅ 完了（v5） |
| 4 | - | HTML/PDF v5反映 | ✅ 完了（v5） |
| 5 | - | Private SlackチャンネルID追加 | ✅ 完了（v5.1） |
| 6 | - | #apac-bil-dt-oncall Public移動 | ✅ 完了（v5.1） |
| 7 | - | OP1 v2 docx をmd/htmlに追加 | ✅ 完了（2026-03-03） |
| 8 | 3月末 | 2027 OP1 キックオフをウォッチ（#bil-ww-tex / #eu-apac-op1-working-group） | 未着手 |
| 9 | - | FY25 Goals PDFフォールバックをテーブルに追記 | 未着手（任意） |
| 10 | - | PDFをv5.1+に同期（再生成） | 未着手（任意） |

## 重要な判断ログ

- **MD が Source of Truth**: HTML/PDF は派生物（前回から継続）
- **v5.1 はHTML直接編集のみ**: Slack チャンネルID追加はHTMLテーブルの修正のみで完結
- **今回は md + html 両方更新**: OP1 v2 docx 追加は両ファイルに反映
- **2027 OP1 はまだ存在しない**: 3月末〜4月にキックオフされる見込み。FY26のタイムラインから推測
- **FY26 OP1 v2 docx をSlackから手動ダウンロード**: Slack MCPではバイナリファイルの直接ダウンロード不可のため、パーマリンクをブラウザで開いてダウンロード

## 関連トピック

- `2026-02-23_weekly-workflow-setup` — 元々このトピックが含まれていた
- `2026-02-23_bil-q4-qbr-revenue-analysis` — QBR データ分析
- `2026-03-02_tex-wbr-review-and-deep-dive` — WBR PDFレビュー・深掘り調査
- `2026-03-03_daily-task-management` — 日次タスク管理（本セッションの親コンテクスト）
