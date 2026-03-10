# TEX FY26 Discovery Planning Survey - 個人別分析

**作成日:** 2026-02-27
**ベースデータ:** survey-analysis.md (v2), multi-agent-review.md, slack-messages.md
**対象:** 回答者7名（AU Pod 4名、JP Pod 3名）

---

## AU Pod

---

## lukthis（Luke） — Sr. Solutions Manager

### 1. 役割/ポジション
- **Sr. Solutions Manager（AU Pod）**
- BILのクライアント対応・Scoping・提案プロセスの中心人物
- 自らTitle Matcher V1を構築・運用している技術志向のSM

### 2. 主要な関心事・優先事項
- **Prime Video**がFY26最優先（Pod全員一致）
- **Scopingプロセスの効率化** — フィージビリティ確認に時間がかかる、誰に聞けばいいか分からないという課題を強く認識
- **Title Matcher V2 / Project DeadMaus** — 既存V1の進化版。Client briefとPrime Videoタイトルの自動マッチングをスケールさせたい
- **Creative Brief自動生成** — ブリーフ情報のAI自動整理への期待
- **LeadGen API** — AU市場での利用不可を課題視

### 3. AI活用に対するスタンス
- **積極的。** AI活用にはポジティブで、scoping自動化、マッチメイキング、brief生成などオペレーション効率化に活用したい意向が明確
- 既にTitle Matcher V1というAIツールを自ら構築・運用しており、実践的なAI活用者
- クリエイティブ領域のAI活用についても慎重派ではない（慎重なのはRich & Mark）

### 4. 課題認識
- **Scopingのボトルネック**: 新しいアイデアのフィージビリティ確認に時間がかかりすぎる。PIC（担当者）の特定も困難
- **AU市場のCanvas制約**: Fire TV、Alexa、Rufus、LeadGen APIが利用不可。利用可能なCanvasに集中せざるを得ない構造的制約
- **Title Matcher V1のスケーリング**: 個人ツールからチーム/グローバルツールへの展開が課題

### 5. プロトタイプ候補との関連性
| Tier | 候補 | 関連度 |
|------|------|--------|
| Tier 1 | **AI Scoping & Feasibility Assistant** | 直接のPain Point提起者。最も恩恵を受ける |
| Tier 2 | **AI-Powered Title Matcher V2** | 自身のV1ツールの進化版。主導者候補 |
| Tier 1 | **PV 2nd Screen Experience** | PM視点でPV統合を推進 |
| - | LeadGen API Access (AU) | 要望あるがTEX Discovery範囲外（C評価） |

### 6. フォローアップのポイント
- **Title Matcher V1の現状詳細**: V1のアーキテクチャ、利用頻度、改善要望の具体像。V2への要件定義に必須
- **Scopingワークフローの具体的ボトルネック**: どのステップで最も時間がかかるか。AI Scoping Assistantの設計に直結
- **Project DeadMausの詳細**: V2以外に構想しているツールがあるか
- **LeadGen APIの業務インパクト**: 利用不可による機会損失の具体的な規模感

---

## Rich（richbpri） — Senior Creative

### 1. 役割/ポジション
- **Senior Creative（AU Pod）**
- Markと合同インタビューで回答（2名として記録されているが、回答は1セット）
- クリエイティブコンセプトの設計・提案を担当

### 2. 主要な関心事・優先事項
- **Prime Video 2nd Screen体験の改善** — QR/URL共有を超えた、デバイス間シームレス連携。TV視聴中のfloating widget、Device-TV連携機能
- **Organic Discovery体験** — 「Do something -> Free sample model」。購買ファネル上流の"発見"体験デザイン
- **Brand Store UXの改善** — ネイティブアプリ体験との乖離を課題視
- **Free Sampling UX** — Add-to-cart→次回購入のフリーサンプル体験のシームレス化

### 3. AI活用に対するスタンス
- **クリエイティブ領域でのAI活用には慎重。** ただし、これはRichとMark 2名の合同見解であり、AU Pod全体のコンセンサスではない点に注意
- AIを「選択的に使うべき」というスタンス
- オペレーション自動化（非クリエイティブ領域）でのAI活用自体は否定していない

### 4. 課題認識
- **PV 2nd Screen体験の限界**: 現状のQR/URLベースの連携が不十分。よりシームレスなデバイス連携が必要
- **AU Canvas制約**: Fire TV非対応のため2nd Screenに集中せざるを得ない。これは選択ではなく構造的必然
- **Brand Store UXの限界**: ネイティブアプリ体験と比較してBrand Storeが見劣りする
- **Free Sampling体験の非シームレス性**: サンプリングから購入への導線が断絶している

### 5. プロトタイプ候補との関連性
| Tier | 候補 | 関連度 |
|------|------|--------|
| Tier 1 | **PV Enhanced 2nd Screen Experience** | 直接の提案者。最も深く関与 |
| Tier 1 | PV Floating Widget on TV | 直接の提案者 |
| B評価 | Seamless Sampling-to-Purchase Workflow | 提案者だが優先度は中程度 |

### 6. フォローアップのポイント
- **2nd Screen体験の具体的ビジョン**: QR/URL以外にどんな連携手法を想定しているか。デバイス自動検出の技術的イメージ
- **AI慎重姿勢の理由の深掘り**: クリエイティブ領域でAIが不適切と考える具体的シナリオ。どこまでなら許容可能か
- **Organic Discovery体験の顧客旅程**: "Do something -> Free sample" の具体的なユーザーフロー
- **Brand Store UXの具体的な不満点**: どの要素がネイティブアプリと乖離しているか

---

## Mark（livmarkj） — Art Director

### 1. 役割/ポジション
- **Art Director（AU Pod）**
- Richと合同インタビューで回答（回答内容はRichと共同のため個別分離が困難）
- ビジュアルデザイン・アートディレクションを担当

### 2. 主要な関心事・優先事項
- Richとの合同回答のため、個別の優先事項の分離は困難
- 共同で挙げた主要テーマ:
  - **PV 2nd Screen体験改善**
  - **Organic Discovery体験**（Do something -> Free sample model）
  - **Brand Store UX改善**
  - **Free Sampling UXのシームレス化**

### 3. AI活用に対するスタンス
- Richと同様、**クリエイティブ領域でのAI活用には慎重**
- Art Directorとして、ビジュアル/デザイン領域でのAI生成に対する懸念がある可能性（詳細は合同回答のため分離不可）

### 4. 課題認識
- Richと共通（上記参照）
- Art Directorとしての視点で、Brand Store UXのビジュアル品質やネイティブアプリとの体験格差により敏感である可能性

### 5. プロトタイプ候補との関連性
- Richと同一（上記参照）

### 6. フォローアップのポイント
- **Richとの合同回答の中でのMark固有の視点の抽出**: 個別チャットでArt Director固有の課題（ビジュアル品質、デザインプロセス、ツール要望）を深掘りすべき
- **AI活用の慎重姿勢の個人的見解**: Rich/Mark合同見解とされているが、Mark個人としてのスタンスを確認
- **AU市場でのビジュアル制作の課題**: グローバルアセットのローカライゼーション、AU固有のデザイン要件など

---

## Chris（wilsnup） — Pod Lead

### 1. 役割/ポジション
- **Pod Lead（AU Pod）**
- AU BIL Pod全体の戦略・運営責任者
- チーム横断の課題（Revenue Attribution、Brief intake、ツールスケーリング）に言及

### 2. 主要な関心事・優先事項
- **Prime Video**（Pod全員一致）+ **Export**をFY26 Priorityとして追加で挙げている
- **Revenue Attribution / 効果測定** — SS revenue attributionの自動化。DSP情報取得→Salesforceへのrodeo ID入力の煩雑さを最も具体的に記述
- **Brief Intake自動化** — Slackからのbrief受信→Salesforceデータ取得→Ready Willing Able分析の自動化
- **Pitch Deck自動生成** — インプット情報からの自動生成
- **Title Matcher V2のスケーリング** — lukthisのツールのグローバル展開にも言及

### 3. AI活用に対するスタンス
- **肯定的。** AI活用に積極的で、特にオペレーション自動化（Brief intake、Pitch deck、Revenue attribution）への期待が高い
- lukthisと同様、実用的・オペレーション寄りの活用を志向
- Rich & Markの慎重姿勢とは対照的

### 4. 課題認識
- **Revenue Attribution問題**: SS（Sponsored Solutions）のrevenue attributionが手動トラッキングと自動ダッシュボードで乖離。DSPからのデータ取得→Salesforceへの入力ワークフローが煩雑。最も具体的な課題記述
- **Brief Intake / 情報集約の非効率**: 複数ソースからの情報収集が手動で、整理に時間がかかる
- **Pitch Deck手動作成の負荷**: 繰り返しの手作業が生産性を圧迫
- **ツールスケーリングの課題**: AU発の自作ツール（Title Matcher等）をグローバルに展開する方法

### 5. プロトタイプ候補との関連性
| Tier | 候補 | 関連度 |
|------|------|--------|
| Tier 2 | **Title Matcher V2** | スケーリング課題の当事者 |
| B評価 | **Automatic Pitch Deck Creation** | 直接の提案者 |
| B評価 | **Brief Intake自動化 + SF Data Pull** | 直接の提案者 |
| C評価 | SS Revenue Attribution自動化 | 直接の提案者だがTEX Discovery範囲外の可能性 |

### 6. フォローアップのポイント
- **Revenue Attributionワークフローの詳細マッピング**: DSP→Salesforce入力の具体的ステップ。自動化可能な箇所の特定
- **Brief Intakeの現状フロー**: Slackでのbrief受信から提案開始までの具体的プロセス。ボトルネックの特定
- **Export Priorityの詳細**: Exportが具体的に何を指すか（クロスボーダー案件？AU→他市場展開？）
- **Pod Leadとしての全体優先順位**: 個別ツール要望の多さに対して、Pod全体としてどこに最もリソースを割きたいか
- **Title Matcherグローバル展開の構想**: AU発ツールを他Pod（JP、MENA）に展開する際の課題認識

---

## JP Pod

---

## miyumat（Miyuki） — Sr. Art Director

### 1. 役割/ポジション
- **Sr. Art Director（JP Pod）**
- JP Podのクリエイティブサイドの中核メンバー
- PVS（Prime Video Sponsorship）とCore BILの両方に言及しており、幅広い案件に関与
- hayemiri（SM）が miyumatの回答に+1しており、SMからの信頼も厚い

### 2. 主要な関心事・優先事項
- **PVS Tier 1案件獲得** — JP Podにとって最重要KPI。競合プラットフォーム（特にNetflix広告参入）への対抗が急務
- **Core BIL: 厳選キーブランドへのイノベーティブ提案** — 特にCPG案件で「全く新しいクリエイティブ」の提案が求められるが、Sales結果との紐づけで困難
- **クロスプラットフォーム連携（360度コラボレーション）** — PV/FTV/Amazon.co.jp間の情報ブリッジ
- **PVスポンサードコンテンツ → Sponsored Products自動レコメンド** — PV視聴後のクロスプラットフォーム商品レコメンド
- **パーソナライゼーション体験** — ユーザーごとに異なるショッピング体験の提供

### 3. AI活用に対するスタンス
- **積極的。** アイデーション補助としてAIを活用したい意向が明確
- 1-pagerのcollaboration idea自動生成への期待が高い
- CDやADが見落としている可能性をAIで補完したいという具体的な活用ビジョン
- hayemiri（SM）も+1しており、実務的な活用にも前向き

### 4. 課題認識
- **PVS Tier 1案件獲得プレッシャー**: ビジネスインパクトとして最高レベルの課題。単なるPV統合ではなく、競合対抗・差別化の文脈
- **CPGブランドへの説得力不足**: Sales結果と紐づく場合、データに裏打ちされた提案フレームワークが必要
- **クロスプラットフォーム情報分断**: PV/FTV/Amazon.co.jp間で情報が連携されていない
- **パーソナライゼーションの実現困難**: アイデアはあるが実装手段が不足

### 5. プロトタイプ候補との関連性
| Tier | 候補 | 関連度 |
|------|------|--------|
| Tier 1 | **PV Enhanced 2nd Screen Experience** | PVS文脈で強く関連 |
| S評価 | **PVスポンサードコンテンツ → SP自動レコメンド** | 直接の提案者 |
| Tier 2 | **AI Collaboration Idea 1-Pager Generator** | PVS Tier 1提案の高速化に直結 |
| A評価 | **パーソナライゼーション体験** | 直接の提案者 |
| Innovation | **Cross-Platform Personalization Engine** | 360度コラボレーションの長期ビジョン |

### 6. フォローアップのポイント
- **PVS Tier 1提案の現状プロセス**: 提案作成にかかる時間、ボトルネック、競合（Netflix等）との具体的な差別化ポイント
- **CPG提案の説得力問題の具体例**: どのブランドで、どのようなデータが不足しているか
- **1-Pager Generatorへの具体的要件**: 入力情報は何か、出力フォーマットの期待値、どの段階で使うか
- **hayemiriとの役割分担**: SM視点でのオペレーション課題がmiyumatの+1に含まれているか、別途確認が必要

---

## shunakd（Shun） — Creative Director

### 1. 役割/ポジション
- **Creative Director（JP Pod）**
- JP Podのクリエイティブ戦略の指揮者
- AIとチームの関係性について最も深く考察しており、テクノロジー戦略への洞察力が高い
- 新しいAd Menu（Interactive Video Ads等）の理解・活用にも課題意識

### 2. 主要な関心事・優先事項
- **Amazon Reviewの活用** — Amazonのユニークアセットとして認識。ReviewデータをCX設計に活かすプロトタイプ構想。Geminiレビューで「Google/Metaが真似できない領域」と高評価
- **AIとチームの最適な関係性** — 共通ツール vs 個人最適化ワークフローの両立を深く考察
- **AIアイデーション補助** — CDとして見落としている可能性をAIで補完したい
- **新Ad Menu/テクノロジーの理解** — Interactive Video Ads等の新メニューをBILがフル活用できていない課題
- **AI実装のタイムライン** — 提案はできるが実装が間に合わないジレンマ

### 3. AI活用に対するスタンス
- **最も積極的かつ思慮深い。** AI活用に前向きなだけでなく、チーム内でのAI導入の実践的課題を深く考えている
- 内部ツールを個人ワークフローにカスタマイズして使っているが、人によって使いやすさが異なることを指摘
- 「チーム共通ツール」と「個別最適化」のバランスが重要と認識
- CDとしてAIがクリエイティブアイデーションを補完する役割を期待（AU Rich & Markの慎重姿勢とは対照的）

### 4. 課題認識
- **AI実装のタイムライン制約**: アイデアや提案はできるが、実装に時間がかかりプロジェクトタイムラインに合わない
- **新Ad Menuの理解不足**: Interactive Video Ads等の新メニューがBILに十分理解されておらず、活用が進んでいない
- **AIツールの個人差**: 同じツールでも人によって使いやすさ・効果が異なり、チーム標準化が困難
- **Scopingの非効率性**: lukthis（AU）と同様、フィージビリティ確認の課題を認識

### 5. プロトタイプ候補との関連性
| Tier | 候補 | 関連度 |
|------|------|--------|
| S評価 | **Amazon Review-Powered Creative Experience** | 直接の提案者。最も深く関与 |
| Tier 1 | **AI Scoping & Feasibility Assistant** | 共同Pain Point提起者（lukthisと） |
| A評価 | **AI Ideation補助ツール** | CDとしてのコア課題に直結 |
| Innovation | **AI Ideation Co-Pilot for CDs/ADs** | 長期ビジョンとして関連 |

### 6. フォローアップのポイント
- **Amazon Review活用の具体的ビジョン**: Reviewデータのどのような要素（テキスト、評価、画像）を、CXのどの段階で活用するイメージか
- **AIツールの個人カスタマイズの実態**: 現在どのようなツールをどう使っているか。チーム展開の障壁は何か
- **Interactive Video Adsの理解ギャップ**: BILメンバーが具体的にどの段階で躓いているか。教育・ドキュメント不足？技術的障壁？
- **AI実装タイムライン問題の具体例**: 過去に提案→実装断念となった案件の詳細
- **CDとしてのAIアイデーション活用イメージ**: どのようなインプットで、どのようなアウトプットを期待するか

---

## hayemiri（Emiri） — Solutions Manager

### 1. 役割/ポジション
- **Solutions Manager（JP Pod）**
- miyumat（Sr. Art Director）の回答に+1（賛同）する形で回答。独自の詳細回答はなし
- SM視点でのオペレーション課題は本調査では十分に把握できていない

### 2. 主要な関心事・優先事項
- miyumatの回答を全面支持しているため、以下が推定される:
  - **PVS Tier 1案件獲得**
  - **クロスプラットフォーム連携**
  - **パーソナライゼーション体験**
  - **AI活用によるアイデーション支援**
- ただし、**SM固有の優先事項（予算管理、納期管理、クライアント折衝プロセス、intake管理等）は不明**

### 3. AI活用に対するスタンス
- miyumatの回答に+1しているため、**基本的に前向き**と推定
- しかし、SM視点でのAI活用ニーズ（提案プロセス効率化、クライアントコミュニケーション支援、スケジュール管理等）は未回答

### 4. 課題認識
- **独自の課題認識は不明。** miyumatの課題認識に賛同しているが、SM固有の課題（以下は推定）は未表出:
  - クライアント折衝における情報整理の負荷
  - 予算・納期管理のツール不足
  - Brief intake→提案開始までのリードタイム
  - 社内調整（Creative/Tech間のコーディネーション）の負荷

### 5. プロトタイプ候補との関連性
- miyumatと同一の候補に関連すると推定
- ただし、**SM視点で最も恩恵を受ける可能性があるのは以下**:
  - AI Scoping & Feasibility Assistant（Scopingの効率化）
  - Brief Intake自動化（AU Chrisと同様の課題がある可能性）
  - 1-Pager Generator（提案プロセスの高速化）

### 6. フォローアップのポイント
- **最優先で個別ヒアリングが必要な人物。** +1回答のみのため、SM固有の視点が完全に欠落している
- **具体的な深掘りテーマ:**
  - JP SMとしての日常業務のペインポイント（AU lukthisやChrisと比較して）
  - クライアント折衝プロセスの課題
  - 予算・納期管理のツール/プロセスの現状
  - Brief intake→提案開始のワークフロー
  - miyumatの回答の中で特に強く共感したポイント、逆に補足したいポイント
- **Slackメッセージ**: miyumatとhayemiriへの合同チャット依頼が既に作成済み。15-20分のクイックチャットで深掘りする計画

---

## 補足: 回答者間の関係性マップ

```
AU Pod                          JP Pod
┌─────────────────┐            ┌─────────────────┐
│ Chris (Pod Lead) │            │                 │
│  - 全体統括       │            │ shunakd (CD)    │
│  - Ops効率化重視  │            │  - AI戦略思考    │
│  - Export追加     │            │  - Review活用    │
├─────────────────┤            ├─────────────────┤
│ lukthis (Sr.SM)  │            │ miyumat (Sr.AD) │
│  - Scoping課題   │◄──共通──►│  - PVS Tier 1   │
│  - Title Matcher │  Pain     │  - 360度連携     │
│  - AI積極的      │  Point    │  - AI積極的      │
├─────────────────┤            ├─────────────────┤
│ Rich & Mark      │            │ hayemiri (SM)   │
│  (合同回答)       │            │  - miyumatに+1  │
│  - 2nd Screen    │            │  - 独自回答なし  │
│  - AI慎重派      │            │  ⚠ 要フォロー    │
└─────────────────┘            └─────────────────┘

共通テーマ:
  ★ Prime Video統合 → 全員
  ★ AI活用 → 全員（程度差あり）
  ★ Scoping効率化 → lukthis, Chris, shunakd
```

---

## 分析まとめ: 個人別フォローアップ優先度

| 優先度 | 回答者 | 理由 |
|--------|--------|------|
| **最高** | **hayemiri** | +1回答のみ。SM視点が完全に欠落。JP Opsニーズの把握に必須 |
| **高** | **lukthis** | Title Matcher V2/Scoping Assistantの要件定義に直結。キーパーソン |
| **高** | **shunakd** | Amazon Review活用、AI-Team関係性の深掘り。Innovation Projectの方向性に影響 |
| **中** | **miyumat** | PVS Tier 1の詳細、1-Pager Generatorの要件。hayemiriとの合同チャットが効率的 |
| **中** | **Chris** | Revenue Attribution、Brief Intake、Pod全体の優先順位確認 |
| **低** | **Rich** | 2nd Screen体験の具体ビジョン、AI慎重姿勢の詳細 |
| **低** | **Mark** | Rich合同回答からの個別視点抽出。独立チャットが理想的 |

---

*本分析はTEX FY26 Discovery Planning Survey回答データおよびマルチエージェントレビュー（Gemini, Kiro, Claude）のフィードバックに基づく。Rich & Markは合同インタビューで回答した2名の個人であり、回答の個別分離には限界がある。hayemiriのSM視点は+1回答に限定されており、追加ヒアリングが強く推奨される。*
