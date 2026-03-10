# Handover Document
**Topic:** TEX FY26 Discovery Planning Survey（APAC/MENA BIL Pod）の分析
**Date:** 2026-03-05
**Status:** 進行中（v3レポート完成、MENA未着手）

---

## 背景

TEX（Technology Experience）チームのFY26 Discovery Planningにあたり、APAC/MENA BIL Podのメンバー12名を対象に「APAC/MENA BIL Pod Priorities & Technology Opportunities - FY26」サーベイを実施した。FY26に向けた優先事項、課題、テクノロジー活用の機会を把握し、プロトタイプ候補の選定とロードマップ策定に活用することが目的である。

回答は8名/12名（回答率67%）から得られた。AU Pod 5名（lukthis, Rich, Mark, Chris, Matt）、JP Pod 3名（miyumat, shunakd, hayemiri）が回答。MENA Podからの回答は0件。マルチエージェントレビュー（Gemini/Kiro/Claude）統合のv2レポート完成後、Matt回答追加 + Quick chatインサイト統合のv3レポート（2026-03-05）を完成させた。

---

## 現在の状況

### サーベイ分析の完了

**v3レポート（2026-03-05）が完成。** v2（マルチエージェントレビュー統合版）に加え、Matt回答 + miyumat/marikoit/shunakd Quick chatインサイトを包括的に統合。回答率58%→67%に向上。新テーマ6件、新プロトタイプ候補2件を追加。

### 主要な発見事項

**5つの共通テーマ:**
1. **Prime Video統合の深化** — AU/JP両Pod共通の最優先領域。AUではFire TV非対応のため2nd Screenが唯一のPV統合Canvas
2. **AI活用への期待と温度差** — AUは「オペレーション寄り」、JPは「クリエイティブ寄り」と活用領域に差異
3. **Scoping/Proposalプロセスの非効率性** — アイデアから提案書への変換パイプラインにボトルネック
4. **マーケット固有のCanvas制約** — 各市場でCanvasの制約が異なり、グローバル標準の体験設計が困難
5. **Revenue Attribution & Measurement** — 効果測定の精度と効率化が提案の説得力と運用効率の両面で課題

**プロトタイプ候補（Tier構成）:**

| Tier | 候補 | 分類 | タイムライン |
|------|------|------|------------|
| **Tier 1** | PV Enhanced 2nd Screen Experience | Ad Innovation | Q1-Q2 |
| **Tier 1** | AI Scoping & Feasibility Assistant | Ops Efficiency | Q1-Q2 |
| **Tier 1** | Maltesers Indecision Duel WebSocket Framework | Ad Innovation | Q2（7月期限） |
| **Tier 2** | AI-Powered Title Matcher V2（AU主導） | Ops Efficiency | Q2-Q3 |
| **Tier 2** | AI Collaboration Idea 1-Pager Generator（JP主導） | Ops Efficiency | Q2-Q3 |
| **Tier 2** | Amazon Review-Powered Creative Experience | Ad Innovation | Q2-Q3 |
| **Tier 2** | Spider-Noir PV X-Ray Contextual Advertising | Ad Innovation | Q3-Q4+ |
| **Innovation** | Cross-Platform Personalization Engine | Ad Innovation | Q3-Q4+ |
| **Innovation** | AI Ideation Co-Pilot for CDs/ADs | Ops Efficiency | Q3-Q4+ |

### マルチエージェントレビューの統合結果

3者共通の最重要指摘:
- **MENA Pod回答不在が最大のリスク** — MENA不在でのTier決定は不完全
- **JP Podの回答がCreative寄りに偏り** — SM視点のオペレーション効率化ニーズが不足
- **Prime Video統合が最優先テーマとして妥当** — APAC共通のNorth Starとして設定可

Gemini独自の指摘: Ad Innovation vs Ops Efficiency のKPI分離、Amazon ReviewのTier格上げ、TPS早期着手
Kiro独自の指摘: Candidate 2の分割、AI Scoping のTier 1昇格、Handoff Document既存キャンペーンの活用、ツール成熟度の差異分析、技術実現可能性/リソース要件の詳細化

### 個人別分析の完成（2026-02-27追加）

7名の回答者それぞれの個人別分析を作成した。各人の役割、関心事、AIスタンス、課題認識、関連プロトタイプ候補、フォローアップポイントを整理。

**個人別フォローアップ優先度:**

| 優先度 | 回答者 | 役割 | 理由 |
|--------|--------|------|------|
| 最高 | hayemiri | SM (JP) | +1回答のみ。SM視点が完全に欠落 |
| 高 | lukthis | Sr. SM (AU) | Title Matcher V2/Scoping Assistantの要件定義に直結 |
| 高 | shunakd | CD (JP) | Amazon Review活用、AI-Team関係性の深掘り |
| 中 | miyumat | Sr. AD (JP) | PVS Tier 1、1-Pager Generator要件 |
| 中 | Chris | Pod Lead (AU) | Revenue Attribution、Brief Intake |
| 低 | Rich | Sr. Creative (AU) | 2nd Screen具体ビジョン |
| 低 | Mark | AD (AU) | Rich合同回答からの個別視点抽出 |

### フォローアップの進捗（2026-03-03更新）

**erensen（Eren Sen）:**
- 3/2 Zoomチャット実施（14分、非公式チェックイン）
- AU vs JP のAI活用の違い（AU: オペレーション寄り / JP: クリエイティブ寄り）について議論
- サーベイリンク送信済み、今週中（~3/6）の回答を合意
- 台湾旅行から帰国直後で、まだセトリング中

**marikoit（Mariko Ito）:**
- 3/4 Quick chat実施（15:00-15:31 AEDT, Zoom, 31分）✅
- サーベイ未回答だが、Quick chatでJP BILの2026年戦略フォーカスを詳細にヒアリング
- **JP BILの3大フォーカスエリア（Marikoの視点）:**
  1. **Flagship PVS（×1）** — タイトルベースで複数ブランドに提案。フルパネルキャンペーン設計でTier 1案件を最低1件成功させる目標。テクノロジーアイデアの宝箱＝すぐデプロイ可能なコンセプトのリポジトリが必要
  2. **Full Funnel Experience（×2）** — XCMとのスポンサーシップコラボ。例: XCMが買うOOHにLEGOも入れてもらう等。Beautyはリテールドリブンで Lower Funnel 寄りすぎる？という課題感
  3. **Push Boundary of Retail Experience** — Retail Experience / Custom LP。Webflow・3Pベンダー活用で効率処理
- **テクノロジーチームへの期待:** プリセールス関与＋実行サポート。PVキャンペーン向けアイデアリポジトリ構築でリードタイム短縮
- **チーム状況:** Discovery年間8プロトタイプ/人の目標あり。ビジネスインパクト評価基準が不明確。リーダーシップとの隔週MTGでリソース配分を継続議論中
- Miyukiチャットとの整合: PVS = Mariko/Shunリード（Miyuki情報と一致）、Core BIL効率化（Miyuki: リソース余裕あり）、Brand Sponsorship = XCMコラボ（Miyuki: アーリーステージ）

**miyumat（Miyuki Matsumoto）:**
- 3/4 Quick chat実施（13:00-13:15 AEDT, Zoom）✅
- Smith（AI）を紹介、PV↔Brand Store間のPersonalizationとして (1) BullsEye（即座に可能）(2) SSE Initiative を紹介
- **JP BILの3フォーカスとリソース状況:**
  1. **PVS（1/3）** — Mariko/Shun-sanで1-pagerを作成・提出中。ADまではまだ落ちてきていない（アーリーステージ）
  2. **Core BIL（1/3）** — 野心的なブリーフが来れば対応するが、基本は「粛々とこなす」方針。Webflow/3Pベンダー活用で対処中。**リソースが若干余っている状態** = 特に問題なし
  3. **Brand Sponsorship（1/3）** — XCMとのコラボ。ステークホルダーとのビジネス会話・Canvas選定などアーリーステージ。テック介入の段階ではない
- **現時点の結論:** フォーカス1/3がまだ本格化しておらず、リソースに若干余裕あり → Core BILのアップセル提案をやっても良いかも、という温度感

**Matt（Bryant, Matt）:**
- 3/3 Shugo & Matt Quick chat（13:00-13:30 AEDT, Kitchen）で対面チャット実施
- **サーベイ回答提出済み ✅**（3/5 PDF確認で回答を確認）
- 回答内容: LeadGen AU（Webflow版SOP）、AUTOバーティカル、Consumer Promotions（Game of Skill/Chance）、MIK拡大、PV API（Metadata/IMDb）
- v3レポートに統合済み

**shunakd（Shun Akeda）:**
- 3/3 Shugo/Shun Sync（14:00-14:30 AEDT, Zoom）でフォローアップ実施 ✅
- **主要な発見:**
  - AI体験を提案したいが実装時間がプロジェクトタイムラインに合わない → TEXのASR initiativeを共有予定
  - 新しい広告メニュー・技術（Interactive Video Ads等）の把握が不十分でBILとして提案に活かしきれない → AI活用エリア？
  - Amazon Reviewはユニークな資産、様々な形で活用できる状況が望ましい
  - 個人的にAI活用でクリエイティブ発想力・プロトタイピング速度を強化中（社内ツールカスタム）
  - 人によって使いやすいものが異なる → "Repository of Skills / MCPs" のアイデア、みんなが使えるツール＋個人最適化の両立が課題
- PVS, Sponsorship, Core BIL が優先領域

**jifuruya（Jin Furuya）:**
- 1月後半より体調不良で休職中（本人からSlack DMで報告）
- サーベイ/フォローアップは現実的に不可。無理せず休んでほしい旨を返信済み（3/2）
- **フォローアップ対象から除外**

**未回答者ステータス一覧（3/5時点）:**

| 名前 | Pod | ステータス |
|------|-----|-----------|
| erensen | JP | サーベイリンク送信済み、回答待ち（~3/6） |
| marikoit | JP | サーベイ未回答だがQuick chatで詳細ヒアリング済み（3/4） |
| ~~Matt~~ | ~~AU~~ | **回答済み ✅**（v3に統合） |
| jifuruya | JP | **休職中 — 除外** |
| aayuda | MENA | 未コンタクト（Slackメッセージ作成済み） |
| hmmushah | MENA | 未コンタクト（Slackメッセージ作成済み） |

### フォローアップメッセージの準備

Slack投稿用メッセージを作成済み:
- チャネル全体へのお礼メッセージ — タイトル: **[Update / Thank You] FY26 Pod Priorities & Tech Opportunities | 5mins Survey**
- AU回答者4名への個別サンクス+フォローアップ予告（英語）
- JP回答者2名（miyumat, hayemiri）へのクイックチャット依頼（日本語）
- JP未回答者（marikoit）へのチャット依頼（日本語） → **完了（DM送信済み）**
- MENA未回答者2名（aayuda, hmmushah）へのインプット依頼（英語）

---

## 成果物一覧

```
2026-02-25_tex-survey-analysis/
├── artifacts/
│   └── slack-messages.md        # Slackフォローアップメッセージ集（英日、全体/個別/未回答者向け）
├── notes/
│   ├── survey-analysis.md       # サーベイ分析レポート v3 日本語版（Matt回答 + Quick chat統合版）🆕
│   ├── survey-analysis-en.md    # サーベイ分析レポート v2 英語版（v3未反映）
│   ├── multi-agent-review.md    # マルチエージェントレビューサマリー 日本語版（Gemini/Kiro/Claude）
│   ├── multi-agent-review-en.md # マルチエージェントレビューサマリー 英語版（同上）
│   ├── individual-analysis.md   # 個人別分析（回答者7名の詳細プロファイル・フォローアップポイント）
│   ├── quick-chat-miyumat-20260304.md   # miyumat Quick chat記録（Zoom原文+日本語訳+メモ）🆕
│   ├── quick-chat-marikoit-20260304.md  # marikoit Quick chat記録（同上）🆕
│   └── quick-chat-shunakd-20260303.md   # shunakd Quick chat記録（ユーザーメモのみ、Zoomサマリーなし）🆕
├── history/
│   ├── 2026-02-25_handover.md   # 旧バージョンアーカイブ（圧縮版）
│   ├── 2026-03-02_handover.md   # 旧バージョンアーカイブ（圧縮版）
│   ├── 2026-03-03_handover.md   # 旧バージョンアーカイブ（圧縮版）
│   └── 2026-03-04_handover.md   # 旧バージョンアーカイブ（圧縮版）🆕
└── handover.md                  # 本ファイル
```

---

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | 2週間以内 | MENA Pod回答収集（aayuda, hmmushah）— Slackメッセージ作成済み | 未着手（メッセージ送信待ち） |
| 2 | 3/4 | marikoit Quick chat実施（15:00-15:15 AEDT, Zoom） | **完了 ✅**（3/4実施、31分） |
| 2a | ~3/6 | erensen サーベイ回答待ち — Zoomチャット実施済み（3/2, 14min）、サーベイリンク送信済み | 進行中（今週中の回答待ち） |
| 2b | — | Matt サーベイ入力 — 3/3対面チャットで合意 | **完了 ✅**（3/5 PDF確認、v3統合済み） |
| 3 | 3/4 | miyumat Quick chat実施（13:00-13:15 AEDT, Zoom） | **完了 ✅**（3/4実施） |
| 3a | 2週間以内 | hayemiri クイックチャット設定 | 未着手 |
| 3b | — | shunakd フォローアップチャット実施 | **完了 ✅**（3/3 Shugo/Shun Sync） |
| 4 | 1ヶ月以内 | 「Ad Innovation」vs「Ops Efficiency」のKPI定義策定 | 未着手 |
| 5 | 1ヶ月以内 | Prime Video APIアクセス権限確認 | 未着手 |
| 6 | Q1中 | TPS標準アーキテクチャの事前承認（Bedrock/SageMaker） | 未着手 |
| 7 | 即時 | Maltesers WebSocket Framework早期着手（7月ローンチ期限） | 未着手 |
| 8 | 1-2ヶ月 | Tier 1候補の技術PoC着手 | 未着手 |
| 9 | — | チャネルへのお礼Slackメッセージ投稿（タイトル確定済み: [Update / Thank You]） | 未着手（メッセージ作成済み） |
| 10 | — | 個人別分析を元にフォローアップチャットのアジェンダ作成 | 未着手（個人別分析は完了） |

---

## 重要な判断ログ

### 1. マルチエージェントレビューの採用
Claudeによる初版分析（v1）に対し、Gemini（Google）とKiro（Amazon Q）の2つのAIにレビューを依頼した。これにより、単一モデルのバイアスを補正し、以下の改善を実現した:
- プロトタイプ候補の分割（旧Candidate 2 → Title Matcher V2 + 1-Pager Generator）
- AI Scoping & Feasibility AssistantのTier 2→Tier 1昇格
- Handoff Document既存キャンペーン（Maltesers, Spider-Noir）のTier候補追加
- 技術的実現可能性・リソース要件の詳細化
- Ad Innovation vs Ops EfficiencyのKPI分離フレームワーク導入

### 2. 回答バイアスの明示的記録
- Rich & Markは合同インタビューで回答した2名の個人であり、AI活用への慎重スタンスはPod全体のコンセンサスではない可能性がある
- JP PodのSM視点はhayemiriの+1（miyumatへの賛同）のみで、独自の詳細回答がないため、オペレーション効率化ニーズは十分に把握できていない
- MENA回答0件のまま最終的なTier決定を行うべきではない

### 3. 推奨比率: Ad Innovation 60% / Ops Efficiency 40%
L10 Kingpin評価を最大化するにはAd Innovationが重要だが、Ops Efficiencyは即効性が高くPod全体の生産性向上に直結する。Q1-Q2はAd Innovation重点、Q3-Q4でOps Efficiency成果蓄積のフェーズ分けを推奨。

### 4. AU/JPのツール成熟度の違いが開発戦略に影響
AUは既存ツール（Title Matcher V1等）の改善型開発（3-6ヶ月）、JPはゼロベース構築（6-12ヶ月）と、同じカテゴリのツールでも開発計画・リソース配分を分けて考える必要がある。

### 5. Slackメッセージの言語選択
AU回答者・MENA未回答者には英語、JP回答者・JP未回答者には日本語でメッセージを作成。各人の言語環境に合わせたコミュニケーション設計とした。

### 6. Slackお礼メッセージのタイトル決定（2026-02-27）
General Thank-Youメッセージのタイトルを `[Update / Thank You] FY26 Pod Priorities & Tech Opportunities | 5mins Survey` に決定。Update（結果まとめ中の進捗共有）とThank You（回答への感謝）の両方のニュアンスを含む形式を選択。

### 7. 個人別分析の作成（2026-02-27）
全体分析に加え、回答者7名それぞれの個人別プロファイルを作成。各人の関心事・AIスタンス・課題認識・関連プロトタイプを整理し、フォローアップチャットのアジェンダ準備に活用可能な形にした。hayemiriが最優先フォローアップ対象（SM視点の欠落補完）。

### 8. jifuruya休職による対象除外（2026-03-02）
jifuruya（Jin Furuya）が1月後半から体調不良で休職中であることがSlack DMで判明。サーベイ/フォローアップ対象から除外。未回答者リストは実質4名（marikoit, erensen, aayuda, hmmushah）に。復帰後に改めてヒアリングの機会を検討。

### 9. erensen Zoomチャットでの知見（2026-03-02）
erensen（Eren Sen）とのZoomチャット（14分）で、AU vs JPのAI活用アプローチの違いについて議論。Zoom会議サマリーAIの話者分離精度に限界があることも確認（個人的な引越し話がErenの発言として誤認識された）。

### 10. Outlook MCP経由でのZoomリンク自動生成は不可（2026-03-03）
テスト検証の結果、Outlook MCPツール（aws-outlook-mcp）でカレンダー招待を作成しても、Zoomリンクは自動付与されないことを確認。Locationフィールドにテキストとして入るのみ。実際のZoomリンクはOutlookアドインから手動追加が必要。

### 11. Mattのサーベイ参加（2026-03-03）
3/3のShugo & Matt Quick chat（対面、Kitchen）でMatt（Bryant, Matt）がサーベイ入力に合意。AU Podからの追加回答として期待。

### 12. shunakdフォローアップでの知見（2026-03-03）
Shun Akeda（CD, JP）とのフォローアップで、3つの重要なインサイトを取得: (1) AI体験の実装時間がプロジェクトタイムラインに合わない問題 → TEX ASR initiativeとの接続点、(2) 新広告メニュー・技術のBIL内での情報共有不足（Interactive Video Ads等）、(3) AIツールの個人最適化 vs チーム標準化のジレンマ → "Repository of Skills / MCPs" コンセプト。Amazon Reviewのユニーク性を活用したいという要望はサーベイ回答と一貫。

### 13. miyumat Quick chatでの知見 — JP BILリソース状況（2026-03-04）
Miyuki（Sr. AD, JP）とのQuick chatで、JP BILの3フォーカス（PVS / Core BIL / Brand Sponsorship）のリソース配分と現状を把握。PVSはまだアーリーステージ（1-pager段階でADに落ちてきていない）、Core BILは粛々と消化でリソース余裕あり、Brand SponsorshipはXCMコラボのビジネス会話段階。テック観点では、余裕のあるCore BIL領域でのアップセル（BullsEye等）が現実的な着手点。Smith紹介、SSE Initiative共有済み。

### 14. marikoit Quick chatでの知見 — JP BIL 2026戦略フォーカス（2026-03-04）
Mariko（SM, JP）とのQuick chatで、JP BILの2026年3大フォーカスを具体的に把握: (1) Flagship PVS×1（タイトルベース複数ブランド提案、Tier 1成功目標）、(2) Full Funnel Experience×2（XCMスポンサーシップコラボ、LEGO等の事例）、(3) Retail Experience最適化（Webflow/3P活用）。テクノロジーチームには「すぐデプロイ可能なコンセプトのリポジトリ」を期待。Miyukiチャット（判断ログ#13）と整合性あり — PVSアーリーステージ、Core BILリソース余裕、Brand Sponsorship = XCMコラボの構図が両者から確認された。Beautyのリテールドリブン = Lower Funnel寄りすぎ？という新たな課題感も浮上。Slack DMの時間表記ミス（15:00 JSTと記載 → 実際は13:00 JST = 15:00 AEDT）があったが、ミーティング自体は問題なく実施。

### 15. survey-analysis v3 包括更新（2026-03-05）
Matt回答（AU, Sr. SM: LeadGen AU、AUTO vertical、Consumer Promotions、MIK拡大、PV API）+ miyumat/marikoit/shunakd Quick chatインサイトを統合し、survey-analysis.mdをv2→v3に更新。新Pain Point 6件（LeadGen AU、Consumer Promotions、Idea Repository不在、Beauty Lower Funnel、AIツール個人差、Discovery評価基準）、新Technology Opportunity 3件（PV Metadata API、Tech Concept Idea Repository、Repository of Skills/MCPs）、新プロトタイプ候補2件（#10 Idea Repository、#11 LeadGen + Consumer Promotions）を追加。回答率58%→67%。JP SM視点の欠落がmarikoitのQuick chatで大幅に補完された。

### 16. Slack DMの時間表記ミス（2026-03-04, 事後記録）
MarikointへのSlack DMで「15:00 JST」と記載したが、正しくは「13:00 JST（= 15:00 AEDT）」。2時間のズレ。ミーティング自体は問題なく実施されたが、Outlook MCP経由でのInvite作成時にタイムゾーン変換を怠ったことが原因。今後はAEDT→JST変換を必ず確認する。

---

## 関連トピック

- `2026-02-26_tex-prime-video-sse-initiative` — SSE APAC展開リサーチ（PV統合の文脈で密接に関連）
- `2026-02-23_sse-prototypes` — SSEプロトタイプ（Fidelity + SSE Viewer）のAUデモ環境構築
- `2026-03-03_consumer-promotion-research` — Consumer Promotion / Game of Chance / Game of Skill 調査（Mattの回答とリンク）
- `2026-03-04_au-bil-pv-growth-engagement` — AU BIL x PV Growth & Engagement（Seanミーティング、BullsEye/SSE関連）
