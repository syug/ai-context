# Julia への返信ドラフト — 回答ポイント対照表

## 方針
- テック面のみ
- 2026年最新情報（PetArmor事例等）は軽く触れ、Alecへの連絡をサジェスト
- MARS FYWDTTYD の経験をベースに回答

## 回答素案サマリー

| # | 質問 | 回答ポイント |
|---|---|---|
| 1 | **承認プロセス** | 3並行トラック: Amazon内部（Legal/PR via approvals.amazon.com）+ ASR（Red、GenAI AppSecチーム）+ クライアント外部承認。Alecに連絡すれば2026年の簡略化パス（Orange/FAST）も説明可能 |
| 2 | **タイムライン** | Legal/PR: ~3週間、ASR: 4-6週間（DT 90h）、クライアントGenAI承認: 3ヶ月超（想定外に長い）。**2026年更新: プリセットのみならOrange → self-certify で大幅短縮** |
| 3 | **入力管理** | 5層ガードレール。特にBedrock Guardrails（Content filters, Denied topics, 競合名ブロック, PII filters）+ Andon Cord必須 |
| 4 | **自由入力 vs 定型** | MARS: フリーフォーム入力だが出力をYES/NO/BLOCKEDに制約。それでもRed。**プリセットのみにすればOrange（allow-list approach）** — Julia DTチームの「事前定義が必要かも」は正しい判断 |
| 5 | **AIモデル＆インフラ** | Claude 3 Sonnet on Bedrock、RAG（Knowledge Bases + OpenSearch Serverless）、temp=0.0、Lambda/API GW/DynamoDB。全てAmazonインフラ内 |
| 6 | **ドキュメント** | FAST SOP、ASR Profiles Wiki、Generative AI for Campaign Quip（Shugo作成）、FAST Wiki。MARS固有のQuipも共有可能 |
| 7 | **教訓** | クライアントGenAI承認を早期開始、ASR 4-6週間覚悟、FAST v2で技術問題あり得る、Andon Cord必須、フリーフォーム=Red を理解した上で設計判断を |

---

## Q1. AI Approval Process

**原文:** What was the end-to-end process for getting the AI tool approved for use on CLP? Which teams/stakeholders were involved in the review (e.g., Legal, Trust & Safety, AdTech)?

**日本語訳:** CLPでのAIツール使用承認のエンドツーエンドのプロセスはどのようなものでしたか？レビューに関わったチーム/ステークホルダーは？

**回答ポイント:**
- 3つの並行承認トラック:
  - **Amazon内部承認:** Legal + PR via `approvals.amazon.com`
  - **ASR (Amazon Security Review):** Red分類。標準タスク + GenAI固有12タスク（Training Data Review, AI Model Review, Prompt Data Sanitization, Andon Cord, FAST Testing 等）。GenAI AppSecチーム（AJ Lopez, Anshuman Bhatnagar）がレビュー
  - **クライアント外部承認:** Mars のグローバル legal/security からGenAI使用承認
- **2026年更新:** プリセットのみの設計なら Orange → self-certify 可能（InfoSecレビュー不要）。詳細は Alec Kunkle (aleckunk@) に連絡を推奨

---

## Q2. Approval Timeline

**原文:** How long did the approval process take from initial proposal to green light? Were there multiple review stages?

**日本語訳:** 最初の提案からゴーサインが出るまで、承認プロセスにどのくらいかかりましたか？複数のレビュー段階がありましたか？

**回答ポイント:**
- Legal/PR 内部承認: **~3週間**
- ASR: **4-6週間**（self-service 2-3週 → InfoSecレビュー 2-3週）。DT作業見積 **90時間**（標準45h + GenAI固有45h）
- クライアント GenAI 承認: **3ヶ月超**（当初予定を大幅超過。UX/UIとは別トラック）
- **2026年更新:** Orange分類なら ASR self-certify で大幅短縮。ただしクライアント承認は依然として長い可能性

---

## Q3. Input Handling

**原文:** How did you manage user-generated input? Did you use any guardrails, content filters, or moderation layers to ensure appropriate responses?

**日本語訳:** ユーザー生成入力はどのように管理しましたか？適切な応答を確保するためのガードレール、コンテンツフィルター、モデレーションレイヤーは使用しましたか？

**回答ポイント:**
- **5層ガードレール:**
  1. 入力バリデーション: 200文字制限、絵文字除去
  2. **Bedrock Guardrails:** Content filters（Hate/Sexual/Violence等、High strength）、Denied topics（Politics/Competitors/Religion等）、Word filters（競合53社名）、PII filters
  3. レスポンス簡素化: LLM出力を YES/NO/BLOCKED の3択に変換。「FM の生テキストは一切顧客に表示されない」
  4. プロンプト内ガードレール: "refuse to perform task" 等の指示を埋め込み
  5. WAF: IPレート制限、リファラーチェック
- **Andon Cord（即時停止機構）:** 環境変数 `USE_BEDROCK_API` を `false` にして即座に AI 無効化。SOP + デモ録画まで求められた
- **全プロンプト/レスポンスの個別ログ保存**（通常セキュリティログとは分離）

---

## Q4. Pre-defined vs. Free-form

**原文:** Was there ever a discussion about restricting inputs to pre-defined prompts vs. allowing free text? What were the key considerations that led to your approach?

**日本語訳:** 入力を事前定義プロンプトに制限するか、フリーテキストを許可するかについて議論はありましたか？最終的なアプローチに至った主な考慮事項は何でしたか？

**回答ポイント:**
- MARS: **ハイブリッド** — 入力はフリーフォーム（200文字以内）、出力は厳密に事前定義（YES/NO/BLOCKED のみ）。LLMの生テキストは一切顧客に見せない
- **重要な含意:** フリーフォーム入力 = Undefined Customer Data (UCD) = Critical = **Red ASR**。この連鎖は設計の初期段階で理解しておくべき
- **2026年の新しい選択肢:** Allow-list approach（事前定義プロンプトのみ）にすれば UCD に該当せず → **Orange ASR → self-certify**。承認期間・工数が大幅に削減
- Julia の DT チームの「事前定義プロンプトが必要かも」は、技術的制約ではなく **ASR分類を Orange に保つための戦略的選択**として正当化できる
- PetArmor (2026 US) ではプリセット + フリーフォームの両方を実装しているが、本番UIでのスコープは要確認

---

## Q5. AI Model & Infrastructure

**原文:** At a high level, what AI model/service did you use, and was it hosted within Amazon's infrastructure? Were there specific technical requirements from the approval side?

**日本語訳:** 使用したAIモデル/サービスは何ですか？Amazonインフラ内でホストされていましたか？承認上の技術要件は？

**回答ポイント:**
- **FM:** Anthropic Claude 3 Sonnet on Amazon Bedrock
- **埋め込み:** Cohere Embed English v3
- **RAG:** Amazon Bedrock Knowledge Bases + Amazon OpenSearch Serverless（S3上の条件リスト約314件から検索）
- **インフラ:** Lambda, API Gateway, DynamoDB, S3, CloudWatch, WAF — 全て Amazon インフラ内（CDK Pipeline, us-west-2）
- **温度設定:** `temperature: 0.0`（完全に決定論的）
- Fine-tuning は不採用（「小データセットではハルシネーションリスク増大」）
- **承認上の技術要件:** Bedrock使用必須（外部APIは不可）、FAST onboarding、全プロンプト/レスポンスのログ保存、Andon Cord 実装

---

## Q6. Documentation

**原文:** Is there any internal documentation, wiki, or approval template you went through that you could point us to? It would help us get a head start on our own submission.

**日本語訳:** 参考にできる社内Wiki・承認テンプレート等の共有依頼

**回答ポイント:**
- **ASR Profiles（分類ルール）:** https://w.amazon.com/bin/view/Infosec/Proactive_Security/Dev/SecurityReviewTooling/ASR/Profiles/
- **FAST Wiki:** https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/
- **FAST Integration SOP（BIL TEX向け）:** https://quip-amazon.com/FhvFAKBxf6Tu/SOP-FAST-Integration
- **Generative AI for Campaign（Shugo作成）:** https://quip-amazon.com/aa1OAHdOJgua/Generative-AI-for-Campaign
- **BIL 承認済み AI ツールリスト:** https://w.amazon.com/bin/view/BIL-E/NA/BIL-AI-Tools
- **GenAI Security Standard:** https://policy.a2z.com/docs/613805/publication
- MARS固有のQuip（AI Tool Overview, ASR Kickoff, Incident Response Plan）も共有可能

---

## Q7. Lessons Learned

**原文:** Anything you'd do differently or any pitfalls to watch out for in the approval process?

**日本語訳:** やり直すなら何を変えるか、承認プロセスの落とし穴は？

**回答ポイント:**
- **クライアント GenAI 承認は想定以上に長い**（3ヶ月超）。UX/UI承認とは別トラックで早めに開始すべき
- **ASR は 4-6週間**。GenAI固有タスク12件が追加。DACEデータ分類を早めに完了させることが前提
- **フリーフォーム入力 = Red ASR** の連鎖を理解した上で設計判断を
- **FAST v2 のオンボーディングで技術的問題あり得る**（ResponseMissingError, v1→v2移行）
- **Andon Cord（即時停止機構）は必須**。SOPとデモ録画まで求められる
- **ミススペル対策は不完全:** 競合名のタイポ全パターンはブロックできない
- **2026年のアドバイス:** プリセットのみでV1ローンチ（Orange）→ フリーフォーム追加でV2（Red）という段階的アプローチを推奨。Alec Kunkle (aleckunk@) が最新プロセスに詳しい
