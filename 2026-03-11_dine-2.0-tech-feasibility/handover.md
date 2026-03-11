# Handover Document
**Topic:** Mars Dine 2.0 "Ignored to Adored" — Tech Feasibility Validation
**Date:** 2026-03-11
**Status:** 進行中（クライアントフィードバック待ち）

---

## 背景

Mars Dine 2.0 "Ignored to Adored" 2026年キャンペーンのため、AU BIL クリエイティブチーム（Chris Wilson）が3つのクリエイティブアイデアを開発し、2026-03-11にクライアントに提案した。

経緯:
1. 2025年: Mars Dine "Cat Decoder" が成功し、"Ignored to Adored" ブランドプラットフォームを確立
2. 2026年計画: エージェンシー（Mars Inc. x Publicis）が「Amazon Dine Video / pspspsuedoscience」を提案 — PVコンテンツに猫向け音声を直接埋め込むコンセプト
3. エージェンシー案がAU BILに却下される
4. Cat Decoderの再実施を検討するも、最終的に新アイデア開発を決定
5. BILが3つの新コンセプトを開発 → "Ignored to Adored V3" として提案

本セッションでは、3アイデアのTech Feasibility Validationを実施し、Amazonプラットフォーム固有の技術制約とArc/Parcの過去事例を踏まえた評価を完了した。

## 現在の状況

### クライアント提案
- 2026-03-11にAU BILクリエイティブチームがクライアントに提案済み
- フィードバック待ちの状態

### Tech Feasibility結果サマリ

全3アイデアが **Yellow**（条件付き実現可能）。各アイデアに1つずつRedブロッカーあり、全てピボットで解消可能:

| Idea | Rating | Red Blocker | Pivot |
|------|--------|-------------|-------|
| 01: Cat Love Keyboard | Yellow | Amazon Music UGCパイプラインが存在しない | UGCとPlaylistを切り離し、プリキュレーション型に |
| 02: Adore Des Chats | Yellow | フィジカル製品の規制（APVMA 6-12ヶ月）+ 製造 | ブランド側が製造担当、限定シーディング |
| 03: Dinner and a Show | Yellow/Red | 超音波がスマホで物理的に不可能 | 8-18kHz帯の「猫向けリラクゼーションサウンドスケープ」にリフレーム |

**技術観点の推奨優先順位:** Idea 01 > Idea 03 > Idea 02

### Arc/Parc調査で発見された主要前例
- **Ad Council "When You Can't Say It, Play It"** — Idea 01の最も近い概念一致（Amazon Music + Alexa、260万シェア）
- **Coca-Cola Second Screen Sync** — Idea 01/03の技術基盤（Brand Store上のReactアプリ + WebSocket同期）
- **Fidelity Peek Portfolio SSE** — Idea 03の最も近いアナログ（PV視聴中のセカンドスクリーンコンパニオン）
- **Nespresso x The Weeknd Vinyl** — Idea 02の最も近い前例（限定フィジカルアイテム + sweepstakes）

### 超音波に関する技術的知見
- スマホスピーカー実用上限: 12-16kHz（スペック上20kHz）
- Echo（ツイーター搭載）: 18-20kHz
- TV内蔵: 12-15kHz
- 猫向けで現実的に狙える帯域: 8-18kHz（30代以上の人間には聞こえにくい）
- 65kHzは民生デバイスでは物理的に不可能

## 成果物一覧

```
2026-03-11_dine-2.0-tech-feasibility/
├── artifacts/
│   └── tech-feasibility-validation.md   ← 全文レポート（3アイデア詳細分析）
├── notes/
├── history/
│   └── 2026-03-11_handover.md           ← 初版アーカイブ
└── handover.md                          ← 本ファイル
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | TBD | クライアントフィードバック待ち — どのアイデアを進めるか決定 | 未着手（待ち） |
| 2 | フィードバック後即時 | ANZ Brand Store カスタム体験のデプロイ可否確認（BIL-E） | 未着手 |
| 3 | フィードバック後即時 | Idea 03進行時: jtransu（Second Screen Sync）、aleckunk（Fidelity PV SSE）に接触 | 未着手 |
| 4 | フィードバック後即時 | Idea 02進行時: APVMA規制アセスメント即着手（6-12ヶ月リードタイム） | 未着手 |
| 5 | 次回クライアント対面前 | Idea 03の超音波クレーム修正（ピッチ資料の技術的正確性を確保） | 未着手 |
| 6 | 全アイデア共通 | Amazon Promotions割引コードインフラのAUマーケット対応確認 | 未着手 |

## 重要な判断ログ

- **エージェンシー案のDNA継承**: Publicisの「pspspsuedoscience」（PV音声トラック埋め込み）は却下されたが、BIL Idea 03はその発想をセカンドスクリーン方式にピボット。技術的にはPV音声改変よりセカンドスクリーンの方がはるかに現実的で良い判断
- **超音波の物理的限界**: ブリーフの「20kHz+、65kHzまで」の主張はスマホスピーカーのハードウェア制約で不可能。8-18kHz帯へのリフレームを推奨
- **Amazon Music UGC不在**: ユーザー作曲→Amazon Musicプレイリスト投入の仕組みは存在しない。Vitaminwater/Cocktail Cabinet等の既存事例は全てプリキュレーション型。UGCとPlaylistの分離を推奨
- **技術優先順位の根拠**: Idea 01はデジタル完結でクロスチーム依存最小、Idea 03はインフラ前例が強いがPV連携の不確実性あり、Idea 02はクリエイティブインパクト最大だが物理製品がタイムライン全体を左右

## 関連トピック

- `2026-02-26_cat-decoder-tech-case-study` — 2025年Mars Dine Cat Decoderのテックケーススタディ（前年キャンペーンの技術詳細）
- `2026-02-23_sse-prototypes` — SSEプロトタイプ（Fidelity + SSE Viewer）。Idea 03のセカンドスクリーン基盤に関連
- `2026-03-05_prototype-ideation-research` — FY26プロトタイプIdeationリサーチ（オーディオフィンガープリンティング等）

## Asana Tasks

- https://app.asana.com/1/8442528107068/project/1213488615214853/task/1213610181703479 （PPTX読み込み・分析）
- https://app.asana.com/1/8442528107068/project/1213488615214853/task/1213609955342140 （Tech Feasibility × 3アイデア）
- https://app.asana.com/1/8442528107068/project/1213488615214853/task/1213609171347745 （ドキュメント作成）
