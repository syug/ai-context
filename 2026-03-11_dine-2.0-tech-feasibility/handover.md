# Handover Document
**Topic:** Mars Dine 2.0 "Ignored to Adored" — Tech Feasibility Validation
**Date:** 2026-03-11
**Status:** 進行中（クライアントフィードバック待ち）

---

## 背景

Mars Dine 2.0 "Ignored to Adored" 2026年キャンペーンのため、AU BIL クリエイティブチーム（Chris Wilson）が3つのクリエイティブアイデアを開発し、2026-03-11にクライアントに提案した。

経緯:
1. 2025年: Mars Dine "Cat Decoder" が成功、"Ignored to Adored" ブランドプラットフォーム確立
2. 2026年計画: エージェンシー（Mars Inc. x Publicis）が「Amazon Dine Video / pspspsuedoscience」を提案
3. AU BILがエージェンシー案を却下 — 主因は戦略的問題（Luke Thistletonのフィードバック: ブランドが「トリックのスポンサー」になり製品が付随的）、副因は技術的制約
4. Cat Decoderの再実施を検討するも、最終的に新アイデア開発を決定
5. BILが3つの新コンセプトを開発 → "Ignored to Adored V3" として提案

## 現在の状況

### クライアント提案
- 2026-03-11にAU BILクリエイティブチームがクライアントに提案済み、フィードバック待ち

### Tech Feasibility結果

全3アイデア **🟡 Yellow**（条件付き実現可能）。各1つ🔴 Redブロッカーあり、全てピボットで解消可能:

| Idea | Rating | Red Blocker | Pivot |
|------|--------|-------------|-------|
| 01: Cat Love Keyboard | 🟡 | Amazon Music UGCパイプライン不在 | UGCとPlaylistを分離、プリキュレーション型に |
| 02: Adore Des Chats | 🟡 | フィジカル製品の規制（APVMA 6-12ヶ月）+ 製造 | ブランド側製造、限定シーディング |
| 03: Dinner and a Show | 🟡/🔴 | 超音波がスマホで物理的に不可能 + PV同期の複雑性 | 超音波→8-18kHz帯リフレーム、動的調整を廃止すればPV同期不要に |

**推奨優先順位（技術観点）:** Idea 01 > Idea 03 > Idea 02

### セッションで追加発見された重要な知見

1. **エージェンシー却下の本当の理由**: 技術的制約だけでなく、戦略的問題が主因（LukeのSlack DM 2026-02-10で確認）
2. **先行事例と本アイデアの差異**: Ad Council/Vitaminwaterは既存カタログ活用であり、UGC投入の前例ではない。Coca-Cola Second ScreenはBIL↔BIL同期であり、PVコンテンツ同期とは根本的に異なる
3. **STS API（SSE Beta）**: Anna Ikejianiメール（2026-02-21）でBIL SSEが正式プロダクト化。STS APIがPV同期の公式ルート。Beta Q3/Q4 2026
4. **オーディオフィンガープリンティング不可**: 猫オーディオ再生中はスピーカー/マイク競合でフィンガープリンティングが機能しない
5. **「番組に合わせる」が技術リスクの根本原因**: このメカニクスだけがPV同期を必要としている。ジャンルプリセットまたは一定再生にすればPV同期不要で全体が🟢に
6. **猫の行動科学**: 動的変化するオーディオより一貫した穏やかなオーディオの方がリラックス効果が高い。動的調整の廃止は科学的にも正しい

## 成果物一覧

```
2026-03-11_dine-2.0-tech-feasibility/
├── artifacts/
│   ├── tech-feasibility-validation.md      ← EN版 全文レポート
│   └── tech-feasibility-validation-ja.md   ← JA版 全文レポート
├── notes/
├── history/
│   ├── 2026-03-11_handover.md              ← 初版アーカイブ
│   └── 2026-03-11_2_handover.md            ← 第2版アーカイブ
└── handover.md                             ← 本ファイル
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | TBD | クライアントフィードバック待ち — どのアイデアを進めるか決定 | 未着手（待ち） |
| 2 | フィードバック後即時 | ANZ Brand Store カスタム体験のデプロイ可否確認（BIL-E） | 未着手 |
| 3 | フィードバック後即時 | Idea 03進行時: Chris Wilsonに「番組に合わせる」の具体的意図を確認（ジャンルプリセット or リアルタイムシーン同期） | 未着手 |
| 4 | フィードバック後即時 | Idea 03進行時: jtransu（Second Screen Sync）、aleckunk（Fidelity PV SSE）に接触 | 未着手 |
| 5 | フィードバック後即時 | Idea 02進行時: APVMA規制アセスメント即着手（6-12ヶ月リードタイム） | 未着手 |
| 6 | 次回クライアント対面前 | Idea 03の超音波クレーム修正（ピッチ資料の技術的正確性を確保） | 未着手 |
| 7 | 全アイデア共通 | Amazon Promotions割引コードインフラのAUマーケット対応確認 | 未着手 |

## 重要な判断ログ

- **エージェンシー却下理由の修正**: 当初「技術的不可能性が理由と推測」としていたが、LukeのSlack DMで主因は戦略的問題（製品が付随的になる）と判明。ドキュメントを修正済み
- **先行事例の正確な差異記述**: 各先行事例に「本アイデアとの違い」を明記し、「前例あり＝実現可能」という誤解を防止
- **動的調整廃止の推奨**: ブリーフの「番組に合わせて動的調整」がPV同期複雑性の唯一の根本原因。猫の行動科学的にも一定音の方が効果的。廃止すればIdea 03全体が🟢に
- **オーディオフィンガープリンティング不可の判断**: 同じデバイスでの再生と聴取の同時実行は音響結合で不可能

## 関連トピック

- `2026-02-26_cat-decoder-tech-case-study` — 2025年Mars Dine Cat Decoderのテックケーススタディ（前年キャンペーンの技術詳細）
- `2026-02-23_sse-prototypes` — SSEプロトタイプ（Fidelity + SSE Viewer）。Idea 03のセカンドスクリーン基盤に関連
- `2026-03-05_prototype-ideation-research` — FY26プロトタイプIdeationリサーチ（オーディオフィンガープリンティング等）

## Asana Tasks

- https://app.asana.com/1/8442528107068/project/1213488615214853/task/1213610181703479 （PPTX読み込み・分析）
- https://app.asana.com/1/8442528107068/project/1213488615214853/task/1213609955342140 （Tech Feasibility × 3アイデア）
- https://app.asana.com/1/8442528107068/project/1213488615214853/task/1213609171347745 （ドキュメント作成）
