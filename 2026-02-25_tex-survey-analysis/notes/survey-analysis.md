# TEX FY26 Discovery Planning Survey 分析レポート v3

**作成日:** 2026-02-25
**改訂:** v3（Matt回答追加 + フォローアップQuick chat統合版）
**v3更新日:** 2026-03-05
**対象:** TEX Discovery Planning Survey（AU/MENA/JP BIL Pod）
**回答数:** 8名 / 12名（回答率 67%）
**レビュー反映:** Gemini (Google), Kiro (Amazon Q), Claude (Anthropic)
**v3追加データ:** Matt サーベイ回答 + miyumat/marikoit/shunakd Quick chat（3/3-3/4）

> **v3 更新履歴:**
> - Matt（AU, Sr. SM）のサーベイ回答を統合（回答率 58%→67%）
> - miyumat Quick chat（3/4）: JP BIL 3フォーカス構造、リソース余裕の実態を反映
> - marikoit Quick chat（3/4, サーベイ未回答）: JP SM視点の3大フォーカス、テクノロジーニーズを統合
> - shunakd Quick chat（3/3）: AI実装タイムライン、Skills/MCPs コンセプトを反映
> - 新テーマ追加: LeadGen AU、Consumer Promotions、AUTO vertical、Idea Repository
> - Pain Points テーブル更新（8名ベース + Quick chatデータ）
> - プロトタイプ候補に新規2件追加（Candidate 10, 11）

---

## 1. Executive Summary（全体サマリー）

FY26 TEX Discovery Planning Surveyの回答を分析した結果、以下の大きなトレンドが浮かび上がった。

**AU Pod（5名回答：lukthis, Rich, Mark, Chris, Matt）** は、スコーピングの非効率性、Prime Videoとの統合の深化、AU市場固有のCanvas制約、およびLeadGen/Consumer Promotionsの法的課題を主要課題として挙げている。v3でMatt（Sr. SM）が追加され、LeadGen AU問題の重要度が上昇し、AUTOバーティカルとConsumer Promotions（Game of Skill/Chance）が新テーマとして浮上した。重要な構造的背景として、**AUではFire TVが利用不可であるため、2nd Screen体験がPrime Video統合における唯一の実行可能なCanvasとなっている**。この制約がAU Podの戦略方向性を規定しており、2nd Screen Experienceへの集中は選好ではなく必然である。AIの活用については「選択的に使うべき」というスタンスが見られるが、**これはRich & Mark（Creative担当、合同インタビューで回答した2名）の見解であり、Pod全体のコンセンサスとは限らない点に留意が必要**。オペレーション自動化（scoping、pitch deck、intake管理）には強いニーズがある。

**JP Pod（3名回答 + Quick chat 3名：miyumat、shunakd、hayemiri + marikoit/shunakd/miyumat Quick chat）** は、PVS Tier 1獲得、フルファネルスポンサーシップ、リテール体験最適化の3フォーカス構造が確認された。v3ではQuick chatにより、JP BILの実態（PVSはアーリーステージ、Core BILはリソース余裕あり、Brand SponsorshipはXCMコラボのビジネス会話段階）が鮮明になった。marikoitはサーベイ未回答だがQuick chatで詳細なSM視点を提供し、v2で指摘されていた「SM視点の欠落」が大幅に補完された。テクノロジーチームには「すぐデプロイ可能なコンセプトのIdea Repository」が求められている。shunakdからは「Repository of Skills / MCPs」コンセプトが提案され、AIツールの個人最適化 vs チーム標準化の課題が具体化した。

**MENA Pod** は回答0件であり、地域固有のニーズは本調査からは把握できていない。MENA市場は文化的・宗教的制約（ラマダンに連動するキャンペーンサイクル、コンテンツ規制、アラビア語RTLレイアウト等）がAU/JPと大きく異なるため、**MENA回答不在のままでのTier決定は不完全**であることを明記する。

**全体として、Prime Video統合、AI活用（オペレーション自動化 + アイデーション補助）、クロスプラットフォーム体験の3つが、FY26のDiscovery Planningにおける最重要テーマである。**

---

## 2. Key Themes（共通テーマ）

回答全体を横断的に分析した結果、以下の5つの共通テーマが抽出された。

### Theme 1: Prime Video統合の深化
- **AU:** Prime Videoが最優先FY26 Priority。2nd screen experience改善、TV視聴中のfloating widget、Device-TV連携機能を求めている。**AU市場ではFire TVが利用不可であるため、2nd Screen体験がPV統合の唯一の手段**であり、この集中は戦略的必然である。
- **JP:** PVSでのTier 1案件獲得が最重要目標。PV・FTV・Amazon.co.jp間の情報ブリッジが課題。PVスポンサードコンテンツ閲覧時の関連Sponsored Products自動レコメンドを希望。**PVS Tier 1 acquisitionのプレッシャーが高く、競合（特にNetflix広告参入）への対抗も急務**。
- **Handoff Document連携:** 既存キャンペーン（Maltesers Indecision Duel、Spider-Noir PV X-Ray）がPV統合の実例として存在。これらの進行中プロジェクトとSurveyで挙がったPain Pointsは直結しており、プロトタイプ候補として活用可能。
- **共通:** Prime Videoは両Pod共通で最優先領域であり、単なる広告枠ではなく「体験統合」レベルでの進化が求められている。

### Theme 2: AI活用への期待と温度差
- **AU:** AIはscoping自動化、マッチメイキング、brief生成などオペレーション効率化に活用したい。クリエイティブ領域には慎重な意見があるが、**これはRich & Mark（合同インタビューで回答した2名）の見解であり、AU Pod全体の温度感を代表するものではない可能性がある**。lukthis（SM）とChris（Pod Lead）はAI活用に肯定的。
- **JP:** AIはアイデーション補助として積極的に活用したい。CDやADが見逃している可能性をAIで補完したい。1-pagerのcollaboration idea自動生成、プロトタイピング高速化への期待が高い。shunakdはAIとチームの最適な関係性について深く考察しており、「共通ツール」と「個人最適化されたワークフロー」の両立を課題視。
- **共通:** AI活用そのものは両Podとも肯定的だが、AUは「オペレーション寄り」、JPは「クリエイティブ寄り」と活用想定領域に差がある。

### Theme 3: Scoping/Proposal プロセスの非効率性
- **AU:** 初見アイデアのフィージビリティ確認に時間がかかる。誰に聞けばいいか分からない。Pitch deck手動作成の負荷。Brief intake時の情報集約が煩雑。
- **JP:** 新Ad Menu/テクノロジーの理解不足でBILがフル活用できない。AI体験の実装に時間がかかりプロジェクトタイムラインに合わない。
- **共通:** 「アイデアから提案書へ」のプロセスにボトルネックがあり、自動化・効率化の余地が大きい。

### Theme 4: マーケット固有のCanvas制約
- **AU:** Fire TV、Alexa、Rufus、LeadGen APIが利用不可。Brand Store UXがネイティブアプリ体験と比較して劣る。**これらの制約がAUの戦略方向性を規定しており、利用可能なCanvas（2nd Screen、Mobile Web）に集中せざるを得ない構造**。
- **JP:** Interactive Video Adsなど新メニューの導入はあるが、BILの理解・活用が追いついていない。
- **MENA（推定）:** アラビア語RTLレイアウト対応、コンテンツ規制（宗教・文化的配慮）、ラマダン連動キャンペーンサイクルなど、AU/JPとは異なる制約が存在する可能性が高い。
- **共通:** 各マーケットごとにCanvasの制約が異なり、グローバル標準の体験設計が難しい。

### Theme 5: Revenue Attribution & Measurement
- **AU:** SS（Sponsored Solutions）のrevenue attribution問題。手動トラッキング vs 自動ダッシュボードの乖離。DSPからの情報取得→Salesforceへのrodeo ID入力が煩雑。
- **JP:** CPG案件でsales結果と紐づけた際の新規クリエイティブ提案の説得力不足。
- **共通:** 効果測定・アトリビューションの精度と効率化が、提案の説得力と運用効率の両面で課題。

---

## 3. Pod別分析

### 3.1 AU Pod

| 項目 | 概要 |
|------|------|
| **回答者** | lukthis（Sr. Solutions Manager）、Rich（richbpri, Senior Creative）& Mark（livmarkj, Art Director）※合同インタビュー・2名、Chris/wilsnup（Pod Lead）、**Matt（Sr. Solutions Manager）🆕 v3** — 計5名 |
| **FY26 Priority** | Prime Video（全員一致）、Export（Chris）、**MIK/Brand Store拡大（Matt）🆕** |
| **最大の課題** | Scoping効率化、Prime Video 2nd screen体験、AU市場のCanvas制約、**LeadGen AU導入（Matt）🆕**、**Consumer Promotions法的課題（Matt）🆕** |
| **AIへのスタンス** | オペレーション自動化に積極的、クリエイティブ領域には一部慎重意見あり |
| **ツール成熟度** | **既存ツールの進化型**（Title Matcher V1→V2等、ベースが存在） |

**AU Pod固有の注目点:**
- **Title Matcher V2 / Project DeadMaus**: lukthisが言及しており、既存AI toolのスケーリングが課題（Chrisも同様に言及）。AU発の自作ツールをグローバル展開する可能性。**既にV1が稼働しているため、改善型開発として比較的短期間でのプロトタイプ化が可能。**
- **Organic Discovery体験**: Rich & Markが「Do something -> Free sample model」を提案。購買ファネルの上流にある"発見"体験のデザインに注力。
- **Revenue Attribution**: Chrisが最も具体的な課題を記述。SS revenue attribution→DSP情報取得→Salesforce入力のワークフロー自動化は、TEX Discovery対象としては運用寄りだが、インパクトは大きい。
- **Canvas制約と戦略方向性**: Fire TV非対応がAUの2nd Screen集中の根本要因。これは「選択」ではなく「唯一の選択肢」であり、2nd Screenプロトタイプの成功がAU PodのFY26 PV戦略全体を左右する。

**🆕 v3追加: Matt（Sr. Solutions Manager）の回答:**
- **LeadGen AU問題の具体化**: lukthisも言及していたLeadGen未対応について、「Webflow版LeadGenをどうAUにインポートするか（SOPとして）」という具体的な解決アプローチを提案。2名のSMが共通して挙げる課題であり、重要度が上昇。
- **AUTOバーティカル**: Data capture for driving leads（自動車業界）が新テーマとして浮上。v2にはなかった業種固有の課題。
- **Consumer Promotions法的課題**: Game of Skill vs Game of Chance の法的区分がAUでのプロモーション実施の障壁。完全に新しいテーマ。
- **MIK（Brand Store）事業拡大**: FY26優先事項としてBrand Store向けビジネス拡大を明示。Rich & MarkのBrand Store UX問題指摘とリンク。
- **PV API活用**: PV関連API（Metadata、IMDb等）でブランド×コンテンツ推薦を希望。Title Matcher V2やPVS候補の正当性を強化。

### 3.2 JP Pod

| 項目 | 概要 |
|------|------|
| **回答者** | miyumat（Sr. Art Director）、shunakd（Creative Director）、hayemiri（Solutions Manager、miyumatの回答に+1）— 計3名（実質的な詳細回答は2名） |
| **FY26 Priority** | Core BIL（厳選キーブランドへのイノベーティブ提案）、PVS（Tier 1獲得）、Sponsorship |
| **最大の課題** | クロスプラットフォーム情報連携、新Ad Menuの理解不足、AI実装の時間的制約 |
| **AIへのスタンス** | アイデーション補助に積極的、個人最適化 vs チーム共通ツールの両立を模索 |
| **ツール成熟度** | **ゼロからの構築型**（既存ツールベースなし、新規開発が前提） |
| **回答バイアス** | **SM視点はhayemiriの+1に限定（独自の詳細回答なし）。実質的にCreative視点中心（AD×1 + CD×1 + SM endorsement×1）** |

**JP Pod固有の注目点:**
- **PVS Tier 1 Acquisition圧力**: miyumatがPVSで言及。Tier 1案件の獲得が最重要KPIであり、競合プラットフォーム（Netflix広告参入等）に対する差別化提案が急務。**このプレッシャーは単なる「PV統合」の話ではなく、ビジネスインパクトとして最も高い課題の一つ。**
- **CPG案件の説得力**: miyumatがCore BILで言及。Sales結果に紐づく場合、「全く新しいクリエイティブ」の提案が困難。データに裏打ちされた提案フレームワークが必要。
- **360度コラボレーション**: PV/FTV/Amazon.co.jp横断の情報ブリッジが課題。これはTEX Discovery Criteriaの「Amazon Canvas」「Prime Video」に直結する重要テーマ。
- **Amazon Reviewの活用**: shunakdが「Amazonのユニークアセット」として言及。ReviewデータをCX設計に活かすプロトタイプは差別化要素になりうる。**Geminiレビューで「Google/Metaが真似できない領域」として高評価。**
- **AIとチームの関係性**: shunakdが個人的な課題として深掘り。内部ツールを個人ワークフローにカスタマイズしているが、人によって使いやすさが異なる点を指摘。「チーム共通ツール」と「個別最適化」の両立が必要。

**🆕 v3追加: Quick chatで得られたJP BILの実態（3/3-3/4）:**

**miyumat Quick chat（3/4）— JP BILリソース状況:**
- JP BILの3フォーカス: PVS（1/3）、Core BIL（1/3）、Brand Sponsorship（1/3）
- **PVS**: Mariko/Shunで1-pager作成・提出中。ADにはまだ落ちてきていない（アーリーステージ）
- **Core BIL**: 基本は「粛々とこなす」方針。Webflow/3P活用で処理。**リソースが若干余っている** = テック介入のチャンス（BullsEye等のアップセル）
- **Brand Sponsorship**: XCMとのコラボ。ステークホルダーとのビジネス会話段階。テック介入はまだ早い
- Smith AI紹介済み、BullsEye + SSE Initiative共有済み

**marikoit Quick chat（3/4, サーベイ未回答）— JP SM視点の補完:**
- JP BIL 2026年3大フォーカス: (1) Flagship PVS×1（タイトルベース複数ブランド提案、テクノロジーアイデアの宝箱 = Idea Repository必要）、(2) Full Funnel Experience×2（XCMスポンサーシップ、例: LEGO OOH。Beautyはリテールドリブンで Lower Funnel寄りすぎ？）、(3) Push Boundary of Retail Experience（Webflow/3P活用）
- **テクノロジーチームへの期待**: プリセールス関与 + 実行サポート。すぐデプロイ可能なテクコンセプトのリポジトリでリードタイム短縮
- Discovery年間8プロトタイプ/人目標あり、ビジネスインパクト評価基準が不明確
- リーダーシップとの隔週MTGでリソース配分を継続議論中

**shunakd Quick chat（3/3）— AI実装とチーム標準化:**
- AI体験の実装時間がプロジェクトタイムラインに合わない → TEX ASR initiativeとの接続点
- 新広告メニュー・技術（Interactive Video Ads等）のBIL内での情報共有不足
- 「Repository of Skills / MCPs」コンセプト: みんなが使えるツール＋個人最適化の両立
- Amazon Reviewのユニーク性を活用したい（サーベイ回答と一貫）
- 優先領域: PVS, Sponsorship, Core BIL

### 3.3 AU/JP ツール成熟度の違い

| 観点 | AU Pod | JP Pod |
|------|--------|--------|
| **既存ツール** | Title Matcher V1（稼働中）、社内自作ツール複数 | なし（新規構築が前提） |
| **開発アプローチ** | 既存ツールの改善・拡張（Iterative） | ゼロベース構築（Greenfield） |
| **プロトタイプ期間** | 短期（3-6ヶ月、ベースあり） | 中期（6-12ヶ月、要件定義から） |
| **リスク** | スコープ拡大（V1→V2で機能過多） | 要件の不確実性（SMの詳細な声が不足） |

この成熟度の違いは、同じ「AIツール」でも開発計画とリソース配分を分けて考える必要があることを意味する。

---

## 4. Ad Innovation vs Ops Efficiency KPI分離

Geminiレビューの指摘を受け、FY26のTEX Discovery成果物を2軸で分類する。**それぞれの成功定義（Measurement）を明確に分離**することで、評価の混乱を防ぐ。

### 4.1 Ad Innovation（クライアント向けイノベーティブ体験）

| 定義 | クライアントへ売るための新しい広告体験・プロトタイプ |
|------|---------------------------------------------------|
| **成功指標** | BILへのピッチ回数、クライアント採用率、Revenue Attribution（広告売上貢献） |
| **該当候補** | PV 2nd Screen Experience、Amazon Review-Powered Experience、Maltesers WebSocket、Spider-Noir X-Ray、Cross-Platform Personalization |
| **Kingpin整合** | L10 Kingpin評価に直結（CX改善、クライアント価値創出） |

### 4.2 Ops Efficiency（チーム内オペレーション変革）

| 定義 | BILチームの業務効率を向上させる内部ツール・自動化 |
|------|------------------------------------------------|
| **成功指標** | 作業時間削減率、Scoping完了までのリードタイム短縮、ツール採用率 |
| **該当候補** | AI Scoping & Feasibility Assistant、Title Matcher V2、1-Pager Generator、Brief Intake自動化、Pitch Deck自動生成 |
| **Kingpin整合** | L10 Kingpin評価への直接貢献は限定的（ただしTEX Goalsの「2 prototypes / DT / quarter」にはカウント可能） |

### 4.3 両軸の戦略的バランス

**推奨比率: Ad Innovation 60% / Ops Efficiency 40%**

- L10 Kingpin評価を最大化するにはAd Innovationが重要
- 一方でOps Efficiencyは即効性が高く、Pod全体の生産性向上に直結
- FY26 Q1-Q2はAd Innovation重点、Q3-Q4でOps Efficiencyの成果を蓄積するフェーズ分けが有効

---

## 5. Pain Points（頻度・インパクト順）

| Rank | Pain Point | 言及者 | 頻度 | インパクト | Pod | 分類 |
|------|-----------|--------|------|-----------|-----|------|
| 1 | **PVS Tier 1案件獲得プレッシャー**（競合対抗、差別化提案の緊急性） | miyumat(PVS), marikoit(Chat) | 2/8+Chat | **最高** | JP | Ad Innovation |
| 2 | **Prime Video統合の制約**（2nd screen、クロスプラットフォーム連携不足） | Rich & Mark, miyumat(PVS), shunakd, **Matt🆕** | 4/8 | 高 | AU, JP | Ad Innovation |
| 3 | **Scopingプロセスの非効率性**（フィージビリティ確認、PIC特定） | lukthis, Chris | 2/8 | 高 | AU | Ops Efficiency |
| 4 | **AI実装のタイムライン制約**（提案はできるが実装が間に合わない） | shunakd, shunakd(Chat) | 1/8+Chat | 高 | JP | Ops Efficiency |
| 5 | **AU市場のCanvas制約**（Fire TV/Alexa/Rufus/LeadGen未対応） | Rich & Mark, lukthis, **Matt🆕** | 3/8 | 中-高 | AU | 構造的制約 |
| 5b | **🆕 LeadGen AU導入**（Webflow版SOPが必要） | lukthis, **Matt🆕** | 2/8 | 中-高 | AU | 構造的制約 |
| 6 | **Revenue Attribution / 効果測定**（SS attribution、DSP連携） | Chris | 1/8 | 中-高 | AU | Ops Efficiency |
| 6b | **🆕 Consumer Promotions法的課題**（Game of Skill vs Game of Chance） | **Matt🆕** | 1/8 | 中-高 | AU | 構造的制約 |
| 7 | **新Ad Menuの理解不足**（Interactive Video Ads等のBIL活用） | shunakd, shunakd(Chat) | 1/8+Chat | 中 | JP | Ops Efficiency |
| 7b | **🆕 テクコンセプトのリードタイム**（Idea Repository不在で提案が遅い） | marikoit(Chat) | Chat | 中 | JP | Ops Efficiency |
| 8 | **Brand Store UXの限界**（ネイティブアプリ体験との乖離） | Rich & Mark, **Matt🆕**(MIK拡大) | 2/8 | 中 | AU | Ad Innovation |
| 9 | **CPGブランドへの新規クリエイティブ提案の説得力不足** | miyumat | 1/8 | 中 | JP | Ad Innovation |
| 9b | **🆕 Beauty = Lower Funnel寄りすぎ？** | marikoit(Chat) | Chat | 中 | JP | Ad Innovation |
| 10 | **Briefの自動intake / 情報集約** | Chris | 1/8 | 中 | AU | Ops Efficiency |
| 11 | **Free Sampling UXの非シームレス性** | Rich & Mark | 1/8 | 低-中 | AU | Ad Innovation |
| 12 | **🆕 AIツールの個人差 vs チーム標準化** | shunakd(Chat) | Chat | 中 | JP | Ops Efficiency |
| 13 | **🆕 Discovery評価基準の不明確さ**（8 prototypes/person/year の KPI） | marikoit(Chat) | Chat | 低-中 | JP | 構造的課題 |

> **v3変更点:** Matt回答追加で頻度を/8ベースに更新。Quick chatデータは「(Chat)」マーカーで識別。6件の新Pain Pointを追加（5b, 6b, 7b, 9b, 12, 13）。

---

## 6. Technology Opportunity Areas（TEX Discovery Criteria マッピング）

TEX Discovery Criteriaに基づき、各テクノロジー機会を4軸で評価する。

### Discovery Criteria:
- **Technology involvement（テクノロジー要素あり）**: 必須
- **TEX Goals alignment**: FY26目標 = 2 prototypes / DT / quarter
- **BIL Pod Priority alignment**: AU/JP各Podの優先事項との整合性
- **Amazon Canvas / Prime Video**: Canvas活用またはPrime Video関連

---

### 6.1 Prime Video関連

| Opportunity | 説明 | 提案者 | TEX Goals | BIL Priority | Canvas/PV | 総合評価 |
|-------------|------|--------|-----------|-------------|-----------|---------|
| **PV 2nd Screen Experience Enhancement** | QR/URL共有を超えた、デバイス間シームレス連携の実現 | Rich & Mark | ★★★ | ★★★ | ★★★ | **S** |
| **PV Floating Widget on TV** | コンテンツ視聴中にインタラクティブなウィジェットをTV上に表示 | Rich & Mark | ★★★ | ★★★ | ★★★ | **S** |
| **PV Title Matcher V2** | Client briefとPrime Videoタイトルの自動マッチング（lukthis既存ツールの進化版） | lukthis | ★★★ | ★★★ | ★★★ | **S** |
| **PVスポンサードコンテンツ → Sponsored Products自動レコメンド** | PVコンテンツ視聴後に関連商品をクロスプラットフォームでレコメンド | miyumat(PVS) | ★★★ | ★★★ | ★★★ | **S** |
| **PV/FTV/Amazon.co.jpクロスプラットフォーム情報ブリッジ** | 360度コラボレーションにおけるプラットフォーム間データ連携 | miyumat(PVS) | ★★☆ | ★★★ | ★★★ | **A** |
| **Spider-Noir PV X-Ray Contextual Advertising** | PVコンテンツ視聴中のX-Ray UIを活用したコンテキスチュアル広告体験 | Handoff Document | ★★★ | ★★☆ | ★★★ | **A** |

### 6.2 AI / Automation関連

| Opportunity | 説明 | 提案者 | TEX Goals | BIL Priority | Canvas/PV | 総合評価 |
|-------------|------|--------|-----------|-------------|-----------|---------|
| **AI Scoping & Feasibility Assistant** | フィージビリティ確認・PIC特定のAI支援 | lukthis, shunakd | ★★★ | ★★★ | ★☆☆ | **S** |
| **AI-Powered Title Matcher V2** | 既存V1の進化版、AU主導のScoping効率化ツール | lukthis | ★★★ | ★★★ | ★★★ | **A** |
| **AI Collaboration Idea 1-Pager Generator** | ブランド向けコラボアイデアの1-pager自動生成、JP主導 | miyumat(PVS) | ★★★ | ★★★ | ★★☆ | **A** |
| **AI Ideation補助ツール**（CD/ADの視点を補完） | CDやADが見落としている可能性のアイデアをAIで発掘 | miyumat(Core), shunakd | ★★★ | ★★★ | ★☆☆ | **A** |
| **Creative Brief Automation** | ブリーフ情報のAI自動生成・整理 | lukthis | ★★☆ | ★★☆ | ★☆☆ | **B** |
| **Automatic Pitch Deck Creation** | インプット情報からピッチデックを自動生成 | Chris | ★★☆ | ★★☆ | ★☆☆ | **B** |
| **Brief Intake自動化 + SF Data Pull** | Slackからのbrief受信→Salesforceデータ取得→Ready Willing Able分析の自動化 | Chris | ★★☆ | ★★☆ | ★☆☆ | **B** |

### 6.3 Shopping / UX関連

| Opportunity | 説明 | 提案者 | TEX Goals | BIL Priority | Canvas/PV | 総合評価 |
|-------------|------|--------|-----------|-------------|-----------|---------|
| **Amazon Review-Powered Creative Experience** | ReviewデータをCX設計やパーソナライゼーションに活用。**Google/Metaが模倣不可能なAmazon独自アセット。** | shunakd | ★★★ | ★★★ | ★★☆ | **S** |
| **パーソナライゼーション体験**（ショッピング体験の動的変化） | ユーザーごとに異なるショッピング体験を提供 | miyumat(Core) | ★★★ | ★★★ | ★★☆ | **A** |
| **Seamless Sampling-to-Purchase Workflow** | Add-to-cart→次回購入のフリーサンプル体験をシームレス化 | Rich & Mark | ★★☆ | ★★☆ | ★★☆ | **B** |

### 6.4 Campaign-Linked Prototypes（Handoff Document連携）

| Opportunity | 説明 | 提案者 | TEX Goals | BIL Priority | Canvas/PV | 総合評価 |
|-------------|------|--------|-----------|-------------|-----------|---------|
| **Maltesers Indecision Duel WebSocket Framework** | リアルタイムWebSocket対戦体験。**7月ローンチ期限あり。** | Handoff Document | ★★★ | ★★★ | ★★☆ | **S** |
| **Spider-Noir PV X-Ray** | PV X-Ray UIを活用したコンテキスチュアル広告（6.1にも記載） | Handoff Document | ★★★ | ★★☆ | ★★★ | **A** |

### 6.5 Measurement / Ops関連

| Opportunity | 説明 | 提案者 | TEX Goals | BIL Priority | Canvas/PV | 総合評価 |
|-------------|------|--------|-----------|-------------|-----------|---------|
| **SS Revenue Attribution自動化** | 手動トラッキングからDSP自動連携・Salesforce入力までの統合 | Chris | ★☆☆ | ★★☆ | ★☆☆ | **C** |
| **LeadGen API Access（AU）** | AU市場でのLeadGen利用可能化 | lukthis, **Matt🆕** | ★☆☆ | ★★★ | ★★☆ | **C→B**🆕 |
| **🆕 PV Metadata/IMDb API活用** | ブランド×コンテンツ推薦の自動化 | **Matt🆕** | ★★★ | ★★★ | ★★★ | **A** |

### 6.6 🆕 Quick chatで浮上した新テーマ（v3追加）

| Opportunity | 説明 | 提案者 | TEX Goals | BIL Priority | Canvas/PV | 総合評価 |
|-------------|------|--------|-----------|-------------|-----------|---------|
| **🆕 Tech Concept Idea Repository** | すぐデプロイ可能なテクコンセプトのライブラリ。PV提案のリードタイム短縮 | marikoit(Chat) | ★★★ | ★★★ | ★★☆ | **A** |
| **🆕 Repository of Skills / MCPs** | AIスキル・MCPのチーム共有リポジトリ。個人最適化 + チーム標準化の両立 | shunakd(Chat) | ★★★ | ★★☆ | ★☆☆ | **B** |
| **🆕 Consumer Promotions体験** | Game of Skill/Chance の法的枠組みに対応した体験設計 | Matt🆕 | ★★☆ | ★★☆ | ★★☆ | **B** |

> **評価基準:** S = 最優先プロトタイプ候補、A = 強い候補、B = 条件付き候補、C = TEX Discoveryの範囲外またはインフラ依存

---

## 7. Technology Feasibility Assessment（技術的実現可能性）

Kiroレビューの指摘を受け、各プロトタイプ候補の技術的実現可能性とタイムライン推定を追加する。

### 7.1 実現可能性ティア

| ティア | 期間 | 候補 | 技術的根拠 |
|--------|------|------|-----------|
| **高**（3-6ヶ月） | Q1-Q2 | AI Scoping & Feasibility Assistant | LLM + 社内ナレッジベース。既存技術スタックで構築可能 |
| **高**（3-6ヶ月） | Q1-Q2 | Title Matcher V2 | V1ベースの改善。LLM API統合の追加 |
| **高**（3-6ヶ月） | Q1-Q2 | PV 2nd Screen Experience | Web技術ベース。PV API依存だが前例あり |
| **中**（6-12ヶ月） | Q2-Q3 | Maltesers WebSocket Framework | WebSocket + リアルタイム通信。7月期限のため早期着手必須 |
| **中**（6-12ヶ月） | Q2-Q3 | 1-Pager Generator | LLM + テンプレートエンジン。JP固有の要件定義が必要 |
| **中**（6-12ヶ月） | Q2-Q3 | Amazon Review-Powered Experience | Review API + NLP。データアクセス権限の確認が必要 |
| **低**（12ヶ月+） | Q3-Q4+ | Cross-Platform Personalization | 複数サービス間データ連携。アーキテクチャ設計から必要 |
| **低**（12ヶ月+） | Q3-Q4+ | Spider-Noir PV X-Ray | PV X-Ray UIへのアクセス権限・API確認が前提 |

### 7.2 TPS（Third Party Security）早期着手の推奨

**Geminiレビューからの重要指摘:** AI系プロトタイプ（SageMaker/Bedrock使用）はセキュリティ審査（TPS）に時間がかかるため、**Q1の早い段階で標準アーキテクチャのTPS承認を取得しておくべき**。

推奨アクション:
- Bedrock / SageMaker使用の標準アーキテクチャテンプレートを作成
- Q1中にTPS審査を完了
- 以降のAIプロトタイプは承認済みアーキテクチャをベースに開発（審査スキップ可能）

---

## 8. Resource Requirements（リソース要件）

Kiroレビューの指摘を受け、各プロトタイプ候補のリソース要件を明示する。

| リソースレベル | 候補 | 必要リソース | 備考 |
|--------------|------|-------------|------|
| **Level 1**（DT 1名で可能） | AI Scoping & Feasibility Assistant | DT×1 | LLM API + 社内データのみ |
| **Level 1**（DT 1名で可能） | Title Matcher V2 | DT×1 | V1ベースの改善 |
| **Level 2**（DT + Eng 1-2名） | PV 2nd Screen Experience | DT×1 + Eng×1-2 | PV API統合にエンジニア必要 |
| **Level 2**（DT + Eng 1-2名） | 1-Pager Generator | DT×1 + Eng×1 | LLMチューニング + UI |
| **Level 2**（DT + Eng 1-2名） | Amazon Review-Powered Experience | DT×1 + Eng×1 | Review API + フロントエンド |
| **Level 3**（チーム体制） | Maltesers WebSocket Framework | DT×1 + Eng×2 + PM×1 | リアルタイム通信 + 7月期限 |
| **Level 3**（チーム体制） | Cross-Platform Personalization | DT×1 + Eng×2 + PM×1 | 複数サービス連携 |
| **Level 3**（チーム体制） | Spider-Noir PV X-Ray | DT×1 + Eng×2 + PM×1 | PV X-Ray UI統合 |

---

## 9. Recommended Prototype Candidates（プロトタイプ候補の推奨）

TEX FY26目標（2 prototypes / DT / quarter）に基づき、Discovery Criteriaとの整合性が高く、かつ複数回答者のニーズに合致するプロトタイプ候補を優先度順に推奨する。

### Tier 1: 最優先（S評価 / Q1-Q2）

#### Prototype Candidate 1: **Prime Video Enhanced 2nd Screen Experience**
- **概要:** PVコンテンツ視聴中に、モバイルデバイス上でインタラクティブなブランド体験を提供。QR/URL共有を超えた、デバイス自動検出・連携機能を含む。
- **関連回答者:** Rich & Mark（AU）、miyumat（JP/PVS）
- **Discovery Criteria適合:** Technology ★★★ / TEX Goals ★★★ / BIL Priority ★★★ / Canvas-PV ★★★
- **想定スコープ:** TV上のfloating widgetまたは2nd screen companion app prototype
- **戦略的背景:** AUではFire TV非対応のため、2nd Screenが唯一のPV統合Canvas。この制約がプロトタイプの戦略的重要度をさらに高めている。
- **分類:** Ad Innovation
- **リソース:** Level 2（DT + Eng 1-2名）
- **実現可能性:** 高（3-6ヶ月）

#### Prototype Candidate 2: **AI Scoping & Feasibility Assistant**
- **概要:** 新しいアイデアのフィージビリティを自動判定し、適切なPICをレコメンド。LLM + 社内ナレッジベースで構築。
- **関連回答者:** lukthis（AU）、shunakd（JP）
- **Discovery Criteria適合:** Technology ★★★ / TEX Goals ★★★ / BIL Priority ★★★ / Canvas-PV ★☆☆
- **想定スコープ:** 自然言語でのアイデア入力→フィージビリティ判定→PIC・過去事例レコメンド
- **v2変更:** Tier 2から昇格（Kiro推奨）。AU/JP両Podの共通Pain Pointであり、即効性が高い。
- **分類:** Ops Efficiency
- **リソース:** Level 1（DT 1名で可能）
- **実現可能性:** 高（3-6ヶ月）

#### Prototype Candidate 3: **Maltesers Indecision Duel WebSocket Framework**
- **概要:** リアルタイムWebSocket対戦体験のフレームワーク。Maltesersキャンペーン向けだが、汎用的なリアルタイムインタラクション基盤として再利用可能。
- **関連:** Handoff Document（既存キャンペーン）
- **Discovery Criteria適合:** Technology ★★★ / TEX Goals ★★★ / BIL Priority ★★★ / Canvas-PV ★★☆
- **想定スコープ:** WebSocketベースのリアルタイム対戦UI + スコアリングエンジン
- **v2変更:** 新規追加（Kiro推奨）。**7月ローンチ期限**があり、早期着手が必須。
- **分類:** Ad Innovation
- **リソース:** Level 3（DT + Eng 2名 + PM 1名）
- **実現可能性:** 中（6-12ヶ月だが期限制約あり）

### Tier 2: 強い候補（A評価 / Q2-Q3）

#### Prototype Candidate 4: **AI-Powered Title Matcher V2**（AU主導）
- **概要:** Client briefとPrime Videoタイトルの自動マッチング。lukthis既存のTitle Matcher V1を進化させたツール。
- **関連回答者:** lukthis（AU）、Chris（AU）
- **v2変更:** 旧Candidate 2から分割（Kiro推奨）。AUのScoping効率化に特化。
- **分類:** Ops Efficiency
- **リソース:** Level 1（DT 1名で可能）
- **実現可能性:** 高（3-6ヶ月）

#### Prototype Candidate 5: **AI Collaboration Idea 1-Pager Generator**（JP主導）
- **概要:** ブランド向けコラボレーションアイデアの1-pagerをLLMで自動生成。PVS Tier 1提案の高速化に寄与。
- **関連回答者:** miyumat（JP/PVS）
- **v2変更:** 旧Candidate 2から分割（Kiro推奨）。JPのクリエイティブ支援に特化。
- **分類:** Ops Efficiency
- **リソース:** Level 2（DT + Eng 1名）
- **実現可能性:** 中（6-12ヶ月）

#### Prototype Candidate 6: **Amazon Review-Powered Creative Experience**
- **概要:** Amazon Reviewデータを活用した、ブランド体験のパーソナライゼーション。Amazonの1st Party Dataをクリエイティブに昇華させる試み。
- **関連回答者:** shunakd（JP）
- **v2変更:** Tier評価を維持しつつ優先度を引き上げ（Gemini推奨）。**「Google/Metaが模倣不可能なAmazon独自領域」**として戦略的価値が高い。
- **分類:** Ad Innovation
- **リソース:** Level 2（DT + Eng 1名）
- **実現可能性:** 中（6-12ヶ月）

#### Prototype Candidate 7: **Spider-Noir PV X-Ray Contextual Advertising**
- **概要:** PVコンテンツ視聴中のX-Ray UIを活用し、コンテンツに関連する広告・商品をコンテキスチュアルに表示。
- **関連:** Handoff Document（Spider-Noirキャンペーン）
- **v2変更:** 新規追加（Kiro推奨）。PV X-Rayという既存UIを広告チャネルとして活用する革新的アプローチ。
- **分類:** Ad Innovation
- **リソース:** Level 3（DT + Eng 2名 + PM 1名）
- **実現可能性:** 低（12ヶ月+、PV X-Ray APIアクセス確認が前提）

### Innovation Project（別トラック / Q3-Q4+）

#### Prototype Candidate 8: **Cross-Platform Personalization Engine**
- **概要:** PV/FTV/Amazon.co.jp横断で、ユーザーの視聴・購買行動に基づいたパーソナライズ体験を提供。
- **関連回答者:** miyumat（JP/Core + PVS）
- **分類:** Ad Innovation
- **リソース:** Level 3

#### Prototype Candidate 9: **AI Ideation Co-Pilot for CDs/ADs**
- **概要:** CDやADのクリエイティブアイデーションを補助するAIツール。
- **関連回答者:** miyumat（JP/Core）、shunakd（JP）
- **注意:** AUのRich & Mark（合同インタビュー2名）は「クリエイティブ領域でのAI活用に慎重」なスタンスのため、JP主導での展開が適切。
- **分類:** Ops Efficiency
- **リソース:** Level 2

#### 🆕 Prototype Candidate 10: **Tech Concept Idea Repository / PV Campaign Library**（v3追加）
- **概要:** PVキャンペーン向けのすぐデプロイ可能なテクノロジーコンセプトのライブラリ。グローバル事例・PARC/Arcプロトタイプを統合し、提案開発のリードタイムを短縮。
- **関連:** marikoit（JP/SM, Quick chat）、miyumat（JP/AD, Quick chat — BullsEye/SSE共有済み）
- **v3追加根拠:** marikoitが「テクノロジーアイデアの宝箱」として明確に要望。JP SMの提案プロセス高速化に直結。
- **分類:** Ops Efficiency
- **リソース:** Level 1（DT 1名、既存PARC/Arcデータの整理が中心）
- **実現可能性:** 高（3ヶ月以内。データ整理 + UIが主体）

#### 🆕 Prototype Candidate 11: **LeadGen AU Webflow SOP + Consumer Promotions Framework**（v3追加）
- **概要:** AU市場でのLeadGen体験をWebflow版として実装するSOPと、Game of Skill/Chance法的枠組みに対応したConsumer Promotions体験フレームワーク。
- **関連:** Matt（AU/SM）、lukthis（AU/SM）
- **v3追加根拠:** AU SM 2名が共通して挙げるLeadGen課題。Consumer Promotionsはconsumer-promotion-researchトピック（別途調査済み）とリンク。
- **分類:** Ad Innovation
- **リソース:** Level 2（DT + Eng 1名、法務確認が必要）
- **実現可能性:** 中（6ヶ月。法的フレームワーク確認が前提）

---

## 10. Gaps & Missing Perspectives（ギャップと不足している視点）

### 10.1 MENA Pod（回答0件）
MENA Podからの回答が皆無であり、地域固有のニーズは把握できていない。

**MENA固有の考慮事項（推定）:**
- **文化的・宗教的制約:** ラマダンに連動するキャンペーンサイクル、コンテンツ規制（肌の露出、アルコール関連等）
- **言語・UI制約:** アラビア語RTLレイアウト、多言語対応の必要性
- **市場特性:** 急成長市場だが広告主の成熟度にばらつき。ブランドセーフティへの感度が高い
- **規制環境:** 各国（UAE、サウジアラビア等）で広告規制が異なる

### 10.2 回答者の偏り（v3で大幅改善）
- **AU:** Solutions Manager×2（lukthis + Matt🆕）、Creative×2、Pod Lead×1。v3でSM視点が強化され、バランスがさらに改善。
- **JP:** サーベイ回答は3名（miyumat, shunakd, hayemiri+1）のままだが、**v3でQuick chatにより3名（miyumat, marikoit, shunakd）から詳細なインプットを取得し、SM視点の欠落が大幅に補完された。**
  - marikoit（SM）のQuick chatで、JP BILの3大フォーカス、テクノロジーニーズ、リソース配分、Discovery評価基準の不明確さなどSM固有の視点が得られた
  - ~~JPのオペレーション効率化ニーズは十分に反映されていない~~ → v3で一定程度解消
  - hayemiri（SM）の独自回答は依然としてないが、marikoitのインプットでJP SM全体像が補強された
  - **残る懸念:** hayemiriの個別フォローアップは未実施。jifuruyaは休職中のため除外。

### 10.3 カバーされていないテーマ
1. **Fire TV / Alexa体験** — JP/MENAでの活用可能性は未探索
2. **Rufus統合** — Discovery体験の可能性は未議論
3. **Twitch連携** — 全回答者から言及なし
4. **Measurement Innovation** — 新しい測定手法の提案はなし

---

## 11. 即座に実行すべきアクション

| # | アクション | 根拠 | 期限 | 担当 |
|---|-----------|------|------|------|
| 1 | MENA Pod回答収集（aayuda, hmmushah） | 全レビュアー共通指摘 | 2週間以内 | Pod Lead |
| 2 | ~~JP SMインプット収集~~ → **v3で一部完了**（marikoit Quick chat済み、jifuruya休職除外）。残: hayemiri個別フォローアップ | v3で大幅改善 | — |
| 3 | TPS標準アーキテクチャの事前承認（Bedrock/SageMaker） | Gemini指摘 | Q1中 | TEX Tech Lead |
| 4 | Prime Video APIアクセス権限確認 | Gemini + Kiro指摘 | 1ヶ月以内 | TEX Tech Lead |
| 5 | 「Ad Innovation」vs「Ops Efficiency」KPI定義 | Gemini指摘 | 1ヶ月以内 | TEX Lead |
| 6 | Tier 1候補の技術PoC着手 | Kiro指摘 | 1-2ヶ月 | DT |
| 7 | Maltesers WebSocket早期着手（7月期限） | Kiro指摘 | 即時 | DT + Eng |

---

*本レポートはTEX FY26 Discovery Planning Surveyの回答データ（8名分: lukthis, Rich, Mark, Chris, Matt, miyumat, shunakd, hayemiri）、マルチエージェントレビュー（Gemini, Kiro, Claude）、およびフォローアップQuick chat（miyumat 3/4, marikoit 3/4, shunakd 3/3）に基づくv3分析である。marikoitはサーベイ未回答だがQuick chatで詳細なSM視点を提供（「Quick chatベース」と明記）。有効対象は12名。MENA Pod（aayuda, hmmushah）および未回答者（erensen）の追加データにより、優先度や推奨事項は変更される可能性がある。jifuruyaは休職中のため対象外。*
