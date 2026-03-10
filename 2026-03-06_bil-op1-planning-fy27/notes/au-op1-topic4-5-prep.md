# AU BIL OP1 Brainstorming — Topic 4 & 5 準備ノート
**Date:** 2026-03-06（作成）
**Next Meeting:** TBD（3/6の続き）
**Carried Over From:** 3/6 OP1ブレスト（Topic 1-3完了、時間切れでTopic 4/5は次回へ）

---

## Topic 1-3 決定事項サマリ（前提として）

| Topic | 決定事項 | Topic 4/5への影響 |
|---|---|---|
| 1: PVS戦略 | **ブリーフファースト**へ転換、Tier 2注力 | AI Scoping Assistantの重要性UP（ブリーフ解析自動化） |
| 2: Creative Engine | **ブランド非依存パッケージング**でスケール化 | AIでテンプレート化を加速可能 |
| 3: BPS連携 | エージェンシー経由を回避、直接関係を優先 | セラー向けAIツールで直接提案力を強化 / BPS=BIL傘下なのでTwitch連携をRetailに活用 |

---

## Topic 4: AI & Automation

### Loopの問い（原文）
> MiKプリセールス不要化？Smith ideationで低Tierブリーフ自動化？Sales向けWebflowツール？

### Topic 1-3を踏まえたインプット更新

**ブリーフファースト（Topic 1決定）→ AI Scoping Assistantが最重要ツールに:**
- ブリーフファーストとは「ブランドのブリーフを起点にタイトルマッチングする」アプローチ
- 年間ブリーフ約100件（+20%増見込み）→ 人力スコーピングが最大ボトルネックになる
- AI Scoping Assistant = ブリーフ入力 → タイトルマッチ → フィージビリティ判定 → PIC特定
- lukthis が Title Matcher V1を自作済み → これを拡張する形が最も自然

**ブランド非依存パッケージング（Topic 2決定）→ AIテンプレート化:**
- Tier 2のパッケージをブランド非依存にするなら、構造化されたテンプレートが必要
- Smith + AI で「ブリーフ → パッケージ提案書ドラフト」を半自動化できる
- MiKは関係構築・ブリーフ解釈に専念、ドラフト生成はAI

**直接関係優先（Topic 3決定）→ セラー向けAIツール:**
- エージェンシー経由を減らし直接関係を増やすなら、セラー自身の提案力を底上げする必要
- AI Toolkitでセラーが自分でブリーフ解析・タイトルマッチング・初期提案を生成
- MiKキャパシティの制約を超えてスケール可能

### Luke/MiK反論への対応（CRITICAL）

**Loopに追記された反論（Luke + Robboの共同見解）:**
- MiKの価値は「曖昧なブリーフの解釈・オポチュニティ形成・関係構築」にある
- **Coke 007事例**: Slack 64通 + メール16通 + クライアント会話2回 → SpotifyとStanに勝利
- 3つの懸念: (1) アイデアの質がバラバラに (2) MiKがエグゼキューション専門に (3) Tier 1/2案件が減るリスク

**対応フレーミング: 「MiK complement, not replacement」**
- Coke 007はMiKの高付加価値作業の好例 → これをもっと増やすためにAIで低価値タスクを引き受ける
- 「MiKが64通のSlackを送れたのは、デック整形や初稿構造化に時間を取られなかったから」という文脈
- AIがやること: デック初稿、タイトルリスト生成、パッケージテンプレート適用
- MiKがやること: ブリーフ解釈、関係構築、競合差別化（=Coke 007のような勝ち方）

### Matt + Luke Smith実験ステータス
- 進行中。MiKの簡易案件をSmith ideationツールで品質比較中
- 結果が出ていれば、Topic 4の議論を具体化する最重要データ
- 結果が未出の場合は「実験結果待ちだが、方向性として complement model を決めたい」

### チームAI温度感マップ（TEX Survey分析より）

| 人 | 役割 | AI活用スタンス |
|---|---|---|
| lukthis | Sr. SM (AU) | Title Matcher V1自作。Scoping自動化に最も積極的 |
| Chris Wilson | Pod Lead (AU) | Brief intake / Pitch deck / Revenue attribution 自動化に関心 |
| Rich & Mark | Creative (AU) | **クリエイティブAIに慎重**、Ops自動化にはOK |
| Matt Bryant | (AU) | Smith実験中。実務・効率寄り |
| miyumat | Sr. AD (JP) | AI ideation・1-pager自動生成に期待 |
| shunakd | CD (JP) | 最も深い思考。"Repository of Skills/MCPs"構想 |

→ Rich & Markの慎重姿勢を尊重。「クリエイティブを自動化する」ではなく「クリエイティブに集中できる時間を増やす」と話す。

### 提案アイデア（Topic 1-3反映版）

**1. Smith Ideation = MiK "Complement" モデル**
- MiK置換ではなく、MiKの低価値タスクをAIで補完
- Phase 1: Matt+Luke実験で品質ベースライン確立（進行中）
- Phase 2: Smith出力をMiKの「下書き」として活用
- Phase 3: MiKは関係構築・ブリーフ解釈に集中（=Coke 007型の勝ち方を増やす）
- **Topic 3「直接関係優先」との整合**: MiKがエージェンシー対応から解放され、ブランド直接関係に時間を使える

**2. AI Scoping Assistant（Topic 1「ブリーフファースト」の必須インフラ）**
- ブリーフ入力 → タイトルマッチング → フィージビリティ判定 → PIC・過去事例レコメンド
- lukthis Title Matcher V1を拡張する形
- AU/JP両Pod共通のPain Point
- DT 1名で3-6ヶ月、Level 1リソース
- **Topic 1決定との直結**: ブリーフファースト戦略を実行するには、100+ブリーフ/年を人力でスコーピングするのは非現実的

**3. AI Toolkit戦略（shunakd構想ベース）**
- 共通ツール層: AI Scoping Assistant, Title Matcher V2, 1-Pager Generator
- 個人カスタマイズ層: Smith, MCPサーバー, 個人ワークフロー
- ガバナンス層: Pre-approved AI architecture（FAST/ASRの審査4-6週を短縮）
- **Topic 2決定との直結**: ブランド非依存パッケージ = テンプレート化 → AIで自動適用

### 英語スクリプト例（Topic 1-3コンテキスト反映版）

**Opener（Topic 1-3との接続）:**
> "Before we dive in — I think the decisions from last time actually make AI even more relevant. We said brief-first for PVS, brand-agnostic packaging for creative, and direct relationships over agency. All three of those create scale challenges that AI can help solve."

**MiK Complement（Luke反論への応答）:**
> "Luke, I read your notes on MiK's value and the Coke 007 case — and I completely agree. That's exactly the kind of work MiK should be doing more of. The question is: can AI handle the lower-value tasks — deck formatting, initial title lists, package templating — so MiK has more time for the 64-Slack-message, win-over-Spotify kind of work?"

**AI Scoping Assistant（最優先提案）:**
> "With brief-first as our strategy, we're going to need a way to process 100-plus briefs a year without burning out the team. Luke already built a Title Matcher V1 — what if we extend that into a full AI Scoping Assistant? Brief in, feasibility and title match out. One DT, one quarter."

**AI Toolkit（長期ビジョン）:**
> "Longer term, shunakd in JP has this idea of a three-layer AI toolkit — shared tools everyone uses, personal customisation on top, and a pre-approved architecture underneath so we don't get stuck in 6-week security reviews every time. I think that's the right framework."

**リスク認識を示す（信頼構築）:**
> "To be clear — I'm not saying 'throw AI at everything.' The FAST security review takes 4 to 6 weeks per project. If we're serious about this for 2027, we need to get a standard architecture pre-approved. That's the unsexy but critical first step."

### 個人的な推奨
- **リード with**: AI Scoping Assistant（Topic 1ブリーフファーストとの直結で反論しにくい）
- **フォロー with**: Smith as MiK complement（Lukeの反論を正面から認めてから提案）
- **ホールドバック**: AI Toolkit 3層構造（聞かれたら出す。先に出すと抽象的すぎて議論が散る）
- **Smith実験結果が出ていれば**: データを先に共有してから議論（数字が最も説得力ある）

---

## Topic 5: Retail Sponsorships

### Loopの問い（原文）
> Project ChariotでOBA復活？MiK活用でlow-pain/high-gain？

### NEW: US Holiday Sponsorship — $42.4MM Pan-Amazon パッケージの全体像

**これは単なるOBAではない。Amazon史上初のAds + Retail/XCM統合パッケージ。**

**概要:**
- L10 Ads & Retail Leadership が2025年2月にアライン
- コンセプト: "Every thing for every holiday."
- スポンサーシップが "force multiplier" として全事業部をリフト

**4ブランド:**

| ブランド | カテゴリ | Net Budget | 特記 |
|---|---|---|---|
| Google | Tech (Pixel) | $8M | Live Sports (TNF/NBA)、Pause Ads含む |
| Unilever | Beauty (Dove等) | $4M | XCM OOH連携の好例 |
| LEGO | Toys | $3M | XCM Holiday Mass Ad出演（2年連続） |
| Shark/Ninja | Home | 不明 | 小規模フットプリント |

合計: $15M+ (Ads)、$42.4MM (Retail込み total)

**Ads側タクティクス:**
- Custom Landing Page (BIL制作)
- Amazon Live（Bethenny Frankelホスト）
- OLV/STV :15, DSP Display, Fire TV Pano + Feature Rotator
- Push通知, H1（トップページヒーロー）

**Retail/XCM側タクティクス:**
- Brand Filter（Holiday Shopサブページ）
- Social Amplification（@Amazon公式）
- Holiday Editorial (NASM)
- XCM Mass Campaign OOH — Times Square, Bryant Park, Penn Station, LA
- Home for the Holidays 体験型イベント（NYC immersive house）

**XCM OOHモデル（Slide 45）:**
- Amazon配送ボックスを巨大3D OOHビルボードに
- ベース: Amazon箱 + 赤リボン + "Every thing for every holiday"
- ブランド版: 箱が開いてDove Sugar Cookie Sprinkleが飛び出す
- **XCMのマスキャンペーンにBILスポンサーブランドを統合するモデル**

**測定:**
- Brand Awareness, Message Association, Purchase Intent, Content Performance, Partnership Impact, Shopping Behavior
- Google: Dynata / Unilever: Nielsen ONE + NCS / LEGO: Lucid + AMC

### NEW: JP BILは既にこの方向に動いている

**2026 Ambitions に明記:**
> "Sponsorship: Unlock new brand budget from top spenders via 'New Sponsorship Models' with XCM integration"
> → Execute 2 sponsorships

**Workstream体制:**
- Sponsorship Lead: Miyuki / Emiri
- 3月初旬にXCM等パートナー議論開始、3月末にパッケージ定義ドキュメント
- **Marikoが3/3にXCMメンバーをMTGに巻き込み開始**（実際に動いている）

**JP実績:**
- Amazon Beauty Festival: マルチブランド、$1.2MM、Black Friday連動
- LEGO Holiday: JP & AU ジョイント（APAC横断パッケージの先例）

**Kazuki の分析（US vs JP の3つの差）:**
1. USは各Portfolio Company単位のスポンサーシップ
2. XCMとの幅広いコラボ（Push通知、OOH活用）
3. 幅広いCanvas（Live, OLV, Fire TV）
- 所感: "massive XCM buy-inが必要だが、別角度として探る価値あり"

### NEW: 組織コンテキスト — Cross-Org Alignmentが必要

```
Amazon Ads (Paul Kotas)          Amazon Stores (Doug Herrington)
  └── Claire Paull (Ads Mktg)     └── Christine Beauchamp (NA Stores)
      └── Kate McCagg (BIL)           └── Jo Shoesmith (XCM)
```

- **BIL = Ads側、XCM = Stores/Retail側** → 完全に別組織
- US Holiday Sponsorshipが "Pan-Amazon初" と言われる理由 = この組織壁を越えたから
- US では L10 Ads & Retail Leadership がアラインして実現
- **AUでこれをやるなら、同様のcross-org alignmentが必要**（AU Ads Lead + AU Retail Lead）

### NEW: OBA プログラム — AUはまだロードマップに載っていない

**グローバル展開ロードマップ（TEX FY26 Goals）:**
- MX集約済み (Q1'26)
- MENA/JP標準化: Q4'26
- EU パイロット: Q4'26
- **AU: 未記載** → OP1で手を挙げるチャンス

**JP OBA実績:**
- POC: Mariko Ito (marikoit)
- 四半期キャップなし（US/CAは4件/Q制限）
- 3パターン: PV Sponsorship連動 / Holiday Retail / Retail Partnership

**OBA注意点:**
- 2025年7月に刷新: Amazonブランドエクイティに直接貢献する使い方のみ
- POC: Christine Arnstad (@carnstad)

### NEW: BPS (Twitch) がBIL傘下に — Cross-Canvas機会

- BPSは2025年8月にBIL統合済み（Victor Lu → Kate McCagg）
- **Chris Ott** (CD, Melbourne, L6) = BPS AUNZ、Gemma Battenbough配下
- Twitch x Amazon Ads のクロスキャンバス = Retail Sponsorshipの新しいCanvasとして活用可能
- 例: Twitch Live Shopping + PV Sponsorship + OBA = フルファネルパッケージ

### Live Sports API（オリジナル Prep より）

- Sports Data Platform (SDP): 36スポーツ / 432リーグのリアルタイムデータ
- AU見込み: Chris見積もり $400K（NBA中心）
- Cricket WC 2027 = AUにとって最大のスポーツアンカー
- ユースケース: リアルタイム予測チャレンジ / チーム連動プロダクトバンドル / 試合情報LP

### 提案アイデア（新リサーチ反映版）

**1. AU Pan-Amazon Sponsorship パイロット（USモデルのAUスケール版）**
- US Holiday $42.4MMをAUスケールに縮小した "Pan-Amazon AU" パイロット
- アンカーイベント: Prime Day AU or BFCM AU（JPのPrime Day/BFCM連動と同期可能）
- Ads側: BIL Custom LP + Fire TV + Push + DSP
- Retail/XCM側: Holiday Shop Brand Filter + Social Amplification
- スケール: 1-2ブランド、$1-2M目標（US比5%程度）
- **前提条件**: AU Ads と AU Retail/XCM のcross-org alignment（US L10アラインメントに相当）

**2. APAC協調アプローチ with JP**
- JP LEGO Holiday = JP+AU ジョイント実績あり → APAC横断パッケージの先例
- Marikoが3/3にXCM連携を開始 → AUも合流するタイミング
- JP Sponsorship WS (Miyuki/Emiri) と AU Pod の連携フレームワーク構築
- APAC統一スポンサーシップパッケージ → グローバルブランド（LEGO, Unilever等）に提案

**3. OBA AU エントリー — グローバル展開ロードマップに乗る**
- 現在のロードマップ: MX → MENA/JP → EU → **AUなし**
- OP1で手を挙げてQ1-Q2 2027パイロットを確保
- JPのOBA運用ノウハウ（Mariko）を活用
- TEXのAI-powered OBA技術（モック自動生成、コンプラレビュー自動化）で差別化

**4. Live Sports x Retail（Cricket WC 2027）**
- Cricket WC 2027をアンカーに、スポーツ×リテールのスポンサーパッケージ
- SDP リアルタイムデータ → 試合中のダイナミック商品プロモーション
- 「ハーフタイムにスナックが注文できる」= CX向上 + リテール売上
- US Holiday の Google パッケージ ($8M) にはLive Sports (TNF/NBA) が含まれていた → 同じモデル

**5. Twitch BPS x Retail クロスキャンバス**
- Chris Ott (CD, Melbourne) + Gemma (BPS Lead AUNZ) がローカルリソース
- Twitch Live Shopping + BIL Sponsorship + OBA = フルファネル
- BPSがBIL傘下になった今だからこそ可能なクロスセル
- ゲーミング/エンタメブランド（LEGO, Nintendo等）に最適

### 英語スクリプト例（新リサーチ反映版）

**Opener（US事例で議論をフレーム）:**
> "I want to reframe how we think about retail sponsorships. When I looked at the US Holiday case, it's not just OBA — it's a $42 million Pan-Amazon package combining Ads and Retail. Google paid 8 million, Unilever 4 million, LEGO 3 million. It's the first time L10 Ads and Retail leadership aligned on a joint sponsorship model."

**AUスケール提案:**
> "Obviously we're not doing $42 million in AU. But the model is what matters — BIL creates the custom experience, XCM amplifies through their mass channels, and the brand gets full-funnel coverage. Could we pilot this with one or two brands for Prime Day or Black Friday, at maybe a $1-2 million scale?"

**JP連携（既に動いている）:**
> "What's interesting is JP is already moving on this. Their 2026 strategy explicitly says 'new sponsorship models with XCM integration.' Mariko has started pulling XCM members into meetings as of March 3rd. And we already have a precedent — the LEGO Holiday campaign was a JP-AU joint effort."

**組織課題を率直に:**
> "The challenge is org structure. BIL sits under Ads, XCM sits under Stores. In the US they solved this with L10 leadership alignment. We'd need something similar in AU — probably a conversation between Chris and whoever leads AU XCM or Retail."

**OBAエントリー:**
> "On OBA specifically — the global expansion roadmap currently goes Mexico, then MENA and JP, then EU. AU isn't on it yet. OP1 might be the right time to put our hand up and get on that roadmap for 2027."

**BPS活用:**
> "One more thing — now that BPS reports into BIL, we have Chris Ott in Melbourne doing Twitch creative. There's a cross-canvas play here: Twitch Live Shopping plus BIL sponsorship plus retail integration. That's a package no one else can offer."

### 個人的な推奨

**リード with**: US Holiday Pan-Amazon事例の紹介（$42.4MMの数字がインパクト大、議論のフレームを設定）
→ そこから「AUスケールで何ができるか？」に落とす

**推奨優先順位:**
1. **Pan-Amazon AU パイロット** — 最もインパクト大、ただしcross-org alignmentが前提
2. **APAC協調 with JP** — 既にJPが動いている、LEGO先例あり、実現性高
3. **OBA AU エントリー** — 低コスト・低リスクで始められる。ロードマップに乗るだけ
4. **Live Sports x Retail** — Cricket WC 2027は時間的余裕あり、2027 H2に向けて仕込み
5. **Twitch BPS x Retail** — 新しいコンセプト、まずはアイデアとして植える

---

## Cross-Topic Synergies（Topic 1-5の全体接続）

### Topic 4 (AI) x Topic 5 (Retail)
- AI Scoping Assistant は Retail Sponsorship のスコーピングにも使える
- ブランド非依存パッケージ（Topic 2） + AI テンプレート化 = Retail Sponsorship パッケージの量産
- Smith で Retail Sponsorship の提案書ドラフトを自動生成 → MiKが仕上げ

### Topic 1 (PVS) x Topic 5 (Retail)
- PV Curated Collections + Retail Sponsorship = クロスキャンバスパッケージ
- 例: Woolworthsが「Friday Night Movie Night」コレクション + スナックバンドル
- US HolidayのGoogleパッケージにはPV Pause Ads + Live Sportsが含まれていた

### Topic 2 (Creative) x Topic 4 (AI)
- Innovation Showcase 四半期イベント → AI-powered Retail体験がテーマになりうる
- Cat Decoder実績 = TEXがAIを本番出荷できる証明 → Retail AI体験の信頼性

### Topic 3 (BPS) x Topic 5 (Retail)
- BPS=BIL傘下 → Twitch x Retail のクロスキャンバスが組織的に可能に
- Chris Ott (Melbourne) = AUローカルでBPS Creativeを実行できるリソース

### クイックリファレンス数字

| 数字 | 文脈 |
|---|---|
| $42.4MM | US Holiday Pan-Amazon total |
| $15M+ | US Holiday Ads portion |
| $8M / $4M / $3M | Google / Unilever / LEGO 個別 |
| $1.2MM | JP Amazon Beauty Festival |
| $400K | AU NBA Retail Sponsorship見込み (Chris見積もり) |
| $400M | AU Amazon Ads全体 来年見込み |
| $6M / 66% | AU BIL FY26目標 / コミット率 |
| 100+/年 | AU年間ブリーフ数（+20%増見込み） |
| 9,500 / 73% | Cat Decoder動画数 / 売上増 |
| 4-6週 | FAST/ASRセキュリティ審査期間 |

---

## Meeting Tactics

### Topic 4: AI & Automation

**トーン:** 謙虚 + 実験重視。「まだわからないことが多い」スタンスで。

**要注意人物: Luke Thistleton**
- MiK反論をLoop文書に追記した本人（Robboと共同）
- Coke 007事例に強い思い入れがある
- **対応:** 反論を正面から認める → 「agree, and...」で complement model に持っていく
- **絶対に避けること:** MiK不要化・置換のニュアンス。「MiKの仕事を減らす」ではなく「MiKの時間を高付加価値に集中」

**Rich & Markへの配慮:**
- クリエイティブAIに慎重 → 「クリエイティブを自動化する」とは言わない
- 「クリエイティブに集中できる時間を増やす」「Opsの自動化で工数を解放」

**リードする内容:** AI Scoping Assistant（全員が pain を感じている共通課題）
**ホールドバックする内容:** AI Toolkit 3層構造（抽象度が高い。聞かれたら出す）

### Topic 5: Retail Sponsorships

**トーン:** ワクワク感 + データドリブン。US事例の数字でインパクトを出す。

**要注意人物: Chris Wilson**
- Pod Lead として Retail Sponsorship の実行責任者になる
- 「面白い、でもリソースは？」「cross-org alignment誰がやるの？」という実務質問が来る
- **対応:** 段階的アプローチを提示（まずOBAエントリー → 次にPrime Day パイロット → 将来Pan-Amazon）
- JP連携をリソース効率化の文脈で出す（「JPが既にやっている = ゼロから作らなくていい」）

**Chris Ott (BPS) への言及:**
- もしChris Ottが参加していたら、Twitch x Retail を振る
- 参加していなくても「BPSにChris Ottがメルボルンにいる」とリソースの存在を示す

**リードする内容:** US Holiday $42.4MM の全体像（フレーム設定）
**ホールドバックする内容:** 詳細な組織図・OBAロードマップ（聞かれたら出す。先に出すと「政治的に難しい」で止まる）

### 全体の流れ

**Topic 4 を先にやる場合:**
1. Topic 1-3との接続（30秒）
2. Smith実験アップデート（Matt/Lukeに振る）
3. MiK complement フレーミング（Lukeに agree してから）
4. AI Scoping Assistant 提案（共通 pain point）
5. FAST/ASRリスク認識（信頼構築）

**Topic 5 を先にやる場合:**
1. US Holiday事例の紹介（数字でインパクト）
2. JP の動き紹介（「既に動いている」urgency）
3. AU Pan-Amazon パイロット提案
4. OBAエントリーの提案（低リスクの第一歩）
5. BPS x Retail（新コンセプトとして植える）

**どちらが先でも:** Cross-Topic Synergies は最後のまとめで触れる程度でOK。