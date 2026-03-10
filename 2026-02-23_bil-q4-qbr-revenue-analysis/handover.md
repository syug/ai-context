# Handover Document
**Topic:** BIL Q4 2025 QBR レベニューデータ解析
**Date:** 2026-02-23（更新: 2026-02-24）
**Status:** 完了

---

## 背景
Amazon Ads Brand Innovation Lab (BIL) の Q4 2025 QBR ドキュメント（PDF）からレベニューデータを抽出・分析した。ドキュメント内のレベニューデータは画像として埋め込まれていたが、PDF読み取りで全データの抽出に成功。

## 現在の状況

### 抽出済みデータ
- WW BIL Revenue 全体サマリー（Q4 2025 / FY 2025）
- 地域別レベニュー（US, CA, MX+BR, EU5各国, JP, AU, MENA）
- P&L（BIL Direct, Core BIL, PV Sponsorship）
- Twitch Ads / BPS レベニュー
- Publisher別アタッチレート

### 分析結果: JP, AU, MENA 構成比
FY 2025 WW BIL Revenue 内の構成比を USD/JPY 併記で算出。

| 市場 | Revenue (USD) | Revenue (JPY @150) | 構成比 | YoY |
|---|---|---|---|---|
| JP | $9.87M | ¥1,481M（約14.8億円） | 1.55% | -16% |
| AU | $4.77M | ¥715M（約7.2億円） | 0.75% | +100% |
| MENA | $1.17M | ¥175M（約1.7億円） | 0.18% | N/A（新規） |
| 3市場合計 | $15.80M | ¥2,371M（約23.7億円） | 2.48% | — |
| WW Total | $638.0M | ¥95,700M（約957億円） | 100% | +78% |

### 分析結果: 全リージョン構成比

| Region | Revenue ($M) | 億円 (@150) | 構成比 | YoY |
|---|---|---|---|---|
| US | 487.4 | 731 | 76.4% | +86% |
| EU5 (UK+DE+IT+FR+ES) | 96.2 | 144 | 15.1% | +71% |
| CA | 27.0 | 40 | 4.2% | +87% |
| MX+BR | 11.6 | 17 | 1.8% | +9% |
| JP | 9.9 | 15 | 1.55% | -16% |
| AU | 4.8 | 7.2 | 0.75% | +100% |
| MENA | 1.2 | 1.8 | 0.18% | New |
| **Total** | **638.0** | **957** | **100%** | **+78%** |

### 主要指標
- BIL Total WW Revenue FY2025: $638.0M (+78% YoY)
- BIL Core: $372.8M (+14% YoY)
- PV Sponsorship: $265.2M (+795% YoY) — マージン97%
- Direct Operating Margin: Q4 87% / FY 83%
- Twitch Ads: $562.3M (-14% YoY) — 減収トレンド
- 2026年見通し: $774M (+21% YoY)

### グラフ生成
全リージョン構成比のビジュアライゼーション（円グラフ＋横棒グラフ）を生成。
- 円グラフ: 構成比表示
- 横棒グラフ: USD / 億円の併記 + YoY成長率
- Hiragino Sans（macOSシステムフォント）で日本語対応
- EU5以下のバーラベルはバー外に統一（レイアウト崩れ修正済み）

## 成果物一覧
```
2026-02-23_bil-q4-qbr-revenue-analysis/
├── handover.md（本ファイル）
├── artifacts/
│   └── fy2025_bil_revenue_by_region.png（地域別構成比グラフ — USD/億円併記、YoY付き）
└── notes/（なし）
```

※ 元データは OneDrive 上の QBR ドキュメントに依存:
- `OneDrive-amazon.com/Team/2. Brand Innovation Lab/MBR:QBR/WW-BIL-2025-Q4-QBR_02-04-2026 FINAL.pdf`

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|---|---|---|
| — | — | 特になし | — |

## 重要な判断ログ
- .docx ファイルはバイナリのため Read ツールで読めず、PDF版から全データを抽出した
- 為替レートは 1 USD = 150 JPY の概算値を使用
- PDFの画像埋め込みテーブルもすべて読み取り可能だった（Claude の PDF 読み取り機能で対応）
- ページ13のBIL Productivity by Market テーブルの数値を地域分析に使用（マスターメトリクスとわずかな差異あり: JP $9,292K vs $9,873K）
- グラフ生成時、matplotlibのデフォルトフォント(DejaVu Sans)では日本語文字が表示できず、macOSシステムフォント「Hiragino Sans」を指定して解決
- EU5のバー内ラベルが崩れる問題は、USのみバー内表記・それ以外は全てバー外表記に統一して解決
