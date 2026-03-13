# Julia への返信ドラフト — 回答ポイント対照表

## 方針
- テック面のみ
- 2026年最新情報（PetArmor事例等）は軽く触れ、Alecへの連絡をサジェスト
- MARS FYWDTTYD の経験をベースに回答

## 回答素案サマリー

| # | 質問 | 回答ポイント |
|---|---|---|
| 1 | **承認プロセス** | 3つの並行承認トラック（Amazon内部・ASR・クライアント外部）。2026年はGenAI=Orange分類でself-certify可能、大幅簡略化。ASR App名: `APAC-BIL-Campaign-Mars-FYWDTTYD-1710164373` |
| 2 | **タイムライン** | ASR作成(2024/3/11) → GenAI AppSecチーム関与(~7/19) → リリース(8/29)。ASRレビュー実期間は約6週間でギリギリだった。2-3ヶ月確保を推奨。2026年はOrangeならASRが数日に短縮 |
| 3 | **入力管理** | リアルタイム人手モデレーション不採用。6層の自動ガードレール＋事前テスト＋Andon Cordの3本柱で対応 |
| 4 | **自由入力 vs 定型** | MARSではフリーテキスト＋多層防御を選択（Plan Bのプリセット制限は却下）。2026年はプリセットのみならOrange=self-certifyで大幅に有利 |
| 5 | **AIモデル＆インフラ** | Claude 3 Sonnet on Bedrock、RAG構成、全てAmazonインフラ内。temp=0.0で完全決定論的 |
| 6 | **ドキュメント** | ASR Profiles Wiki、FAST Wiki/SOP、Generative AI for Campaign Quip等を共有可能。MARS固有のQuipも提供可 |
| 7 | **教訓** | 最大の教訓: クライアントGenAI承認を初日から並行開始すること。フリーフォーム=Red ASRの連鎖を設計初期に理解すべき |

---

## Q1. AI Approval Process

**原文:** What was the end-to-end process for getting the AI tool approved for use on CLP? Which teams/stakeholders were involved in the review (e.g., Legal, Trust & Safety, AdTech)?

**日本語訳:** CLPでのAIツール使用承認のエンドツーエンドのプロセスはどのようなものでしたか？レビューに関わったチーム/ステークホルダーは？

**ストレート回答:** 3つの並行承認トラックがある — Amazon内部（Legal/PR）、ASR（セキュリティレビュー）、クライアント外部承認。2026年からはGenAI=Orange分類でself-certify可能になり、大幅に簡略化されている。

**回答ポイント:**
- 3つの並行承認トラック:
  - **Amazon内部承認:** Legal + PR via `approvals.amazon.com`
  - **ASR (Amazon Security Review):** Red分類。標準タスク + GenAI固有12タスク（Training Data Review, AI Model Review, Prompt Data Sanitization, Andon Cord, FAST Testing 等）。GenAI AppSecチーム（AJ Lopez, Anshuman Bhatnagar）がレビュー。ASR Application: `APAC-BIL-Campaign-Mars-FYWDTTYD-1710164373` (App ID: `d1f8d647-c905-48af-be66-d96231698216`)、Bindle: `APAC-BIL-Campaign-Mars-FYWDTTYD`
  - **クライアント外部承認:** Mars のグローバル legal/security からGenAI使用承認
- **2026年更新:** プリセットのみの設計なら Orange → self-certify 可能（InfoSecレビュー不要）。詳細は Alec Kunkle (aleckunk@) に連絡を推奨

---

## Q2. Approval Timeline

**原文:** How long did the approval process take from initial proposal to green light? Were there multiple review stages?

**日本語訳:** 最初の提案からゴーサインが出るまで、承認プロセスにどのくらいかかりましたか？複数のレビュー段階がありましたか？

**ストレート回答:** 全体で最短でも3ヶ月超かかった。内部Legal/PRは約3週間、ASRは4-6週間だが、クライアントGenAI承認が3ヶ月超と最長ボトルネック。2026年はOrange分類ならASRが数日に短縮可能。

**MARS FYWDTTYD 実データ:**
- **ASR作成日:** 2024/3/11（self-service開始、リポジトリ作成と同時期）
- **GenAI AppSecチーム関与:** ~2024/7/19（Slackチャネル作成で確認）
- **リリース日:** 2024/8/29
- **ASRレビュー実期間:** 約6週間（7/19 → 8/29）— ギリギリだった
- **実感:** ASRレビューに2-3ヶ月確保を推奨

**回答ポイント:**
- Legal/PR 内部承認: **~3週間**
- ASR: **4-6週間**（self-service 2-3週 → InfoSecレビュー 2-3週）。DT作業見積 **90時間**（標準45h + GenAI固有45h）
- クライアント GenAI 承認: **3ヶ月超**（当初予定を大幅超過。UX/UIとは別トラック）
- **実績ベースのアドバイス:** ASRレビュー実期間は約6週間（7/19 → 8/29）でギリギリだった。ASR+クライアント承認に2-3ヶ月を確保すべき
- **2026年更新:** Orange分類なら ASR self-certify で大幅短縮。ただしクライアント承認は依然として長い可能性

---

## Q3. Input Handling

**原文:** How did you manage user-generated input? Did you use any guardrails, content filters, or moderation layers to ensure appropriate responses?

**日本語訳:** ユーザー生成入力はどのように管理しましたか？適切な応答を確保するためのガードレール、コンテンツフィルター、モデレーションレイヤーは使用しましたか？

**ストレート回答:** リアルタイムの人手モデレーションは不採用。代わりに6層の自動ガードレール（WAF、入力検証、Bedrock Guardrails、出力制約等）で防御し、FAST/Pentestによる事前テストとAndon Cord即時停止機構を組み合わせた。

**回答ポイント:**
- **多層防御アーキテクチャ（6層、コードレビューで確認済み）:**
  1. **フロントエンド:** 100文字制限（`CHARACTER_LIMIT = 100`）+ T&C同意チェックボックス（PII disclaimer含む）+ `trim()`
  2. **ネットワーク:** WAF 6ルール（AWSManagedRules 4種 + BotControl + IP Rate Limit 2000req/5min）、ログ5年保持・KMS暗号化
  3. **API Gateway:** Lambda Authorizer（Origin whitelist + Token）、Request Validator（`additionalProperties: false`）、Throttling 30req/s
  4. **バックエンド入力検証:** `validateInputText` 5段パイプライン（100文字切捨 → lowercase → マルチバイト句読点変換 → 絵文字除去[node-emoji] → URIエンコード → CRLF除去）
  5. **Bedrock Guardrails（4フィルタ）:**
     - Content Filters: 全6カテゴリ HIGH（SEXUAL, VIOLENCE, HATE, INSULTS, MISCONDUCT, PROMPT_ATTACK）
     - Denied Topics: 28個（ビルトイン5 + カスタム23。Alcohol, Competitors, Politics, Religion, Brand safety等）
     - Word Filters: 1,494語（多言語。競合ブランド名、極右用語、不適切表現等。Excelから自動生成）
     - PII Filters: 全カテゴリ BLOCK（General, IT, Finance, USA/Canada/UK Specific）+ カスタム正規表現
  6. **レスポンス正規化:** `validateAnswer()` で YES/NO/BLOCKED の3択に制約。それ以外は全てNOにフォールバック。本番では `answer` のみ返却、LLM生テキスト非公開
- **プロンプト設計:** `buildPrompt()` でユーザー入力を `<action>` タグでラップし、固定質問文と組み合わせ。プロンプトインジェクション耐性を確保
- **Andon Cord（即時停止機構、コードレビューで確認済み）:** Lambda環境変数 `USE_BEDROCK_API` を `false` にして即座にAI無効化（503返却）。SOP + デモ録画まで求められた
- **全リクエスト/レスポンスの個別ログ保存:** DynamoDB `BedrockResponseTable`（KMS暗号化、PITR有効、Auto Scaling 1-10）に全フィールド記録（id, input, prompt, answer, comment, outputText, citation, guardrailId, guardrailAction等）

### リアルタイムモデレーション不採用と代替策

- **リアルタイムモデレーション（人手による即時レビュー）は不採用。** 代わりに以下の3本柱 + 事後モニタリングで対応:

**柱1: 堅牢なガードレール（多層防御）**
- 上記6層アーキテクチャがこれに該当。特にBedrock Guardrails（4フィルタ）+ validateAnswer（3択制約）+ 100文字制限の組み合わせにより、不適切な入出力をリアルタイムに**自動ブロック**する設計
- 人手のモデレーションではなく、技術的な多層防御で代替

**柱2: 徹底的な事前テスト**
- **FAST（Framework for AI Security Testing）:** Beta環境でHydra Stackを使った自動プロンプトセキュリティテスト
- **Pentest:** ASRプロセスの一環としてGenAI AppSecチームによるペネトレーションテスト
- **関係者テスト:** クライアント（Mars）、Legal、PR、DT全員でのUAT。実際のプロンプトでガードレールの有効性を検証

**柱3: ISR（Incident Response Plan）+ Andon Cord**
- **ISR:** インシデント発生時の対応手順書を事前に作成。エスカレーションパス、担当者、連絡先を明確化
- **Andon Cord:** Lambda環境変数 `USE_BEDROCK_API` を `false` にして即座にAI機能を停止（503返却）。SOP + デモ録画をASRで提出

**事後モニタリング: CloudWatch アラーム + Dashboard（CDKコードレビューで確認）**
- `cloudtrail-cloudwatch-alarms.ts` に4つのCloudTrailベースアラームを実装:
  | アラーム名 | トリガー条件 | 閾値 |
  |-----------|------------|------|
  | ConsoleSigninFailures | コンソールログイン認証失敗 | 3回/5分 |
  | AWSResourcesAuthorizationFailure | UnauthorizedOperation / AccessDenied | 3回/5分 |
  | CloudTrailChanges | CloudTrail設定変更（Create/Update/Delete/Start/StopLogging） | 1回 |
  | IAMPolicyChanges | IAMポリシー変更（16種のイベント） | 1回 |
- 全アラーム → SNS → `au-brandinnovationlab-mars-fywdttyd@amazon.com` にメール通知
- KMS暗号化、CloudTrailログ5年保持
- **CloudWatch Dashboard:** WAFログをWiki埋め込み可能なダッシュボードで可視化（`@amzn/cloudwatch-dashboards-wiki-cdk-construct`）
- **補足:** これらはインフラ/セキュリティ監視のアラーム。AIレスポンス内容の事後モニタリングはDynamoDB `BedrockResponseTable` の全ログ + 手動バッチレビュー（週次 + 隔週BILチームレビュー）で実施

---

## Q4. Pre-defined vs. Free-form

**原文:** Was there ever a discussion about restricting inputs to pre-defined prompts vs. allowing free text? What were the key considerations that led to your approach?

**日本語訳:** 入力を事前定義プロンプトに制限するか、フリーテキストを許可するかについて議論はありましたか？最終的なアプローチに至った主な考慮事項は何でしたか？

**ストレート回答:** はい、議論した。MARSではフリーテキスト＋多層ガードレールを選択した（プリセットのみではクライアント要件を満たせず、LLM自体が不要になるため）。ただしフリーフォーム入力=Red ASRという代償を受け入れた。2026年はプリセットのみならOrange=self-certifyで承認が大幅に簡略化される。

**回答ポイント:**
- **MARS での議論経緯（実体験）:**
  - 事前定義プロンプトへの制限は **Plan B として検討された**（議論あり）
  - しかし、プリセット制限ではクライアント（Mars）の要件を**満たすのが遥かに難しい、あるいは部分的にしか満たせない**。クリエイティブソリューションとしても弱くなる
  - さらに重要な点として、**プリセットのみにするならLLMを使用する必要自体がなかった**（技術的にオーバーキル）。LLMの価値はフリーフォーム入力を解釈できることにある
  - よって**フリーテキスト入力を採用し、多層ガードレール（Q3参照）で守る方針を選択**した
- MARS: **ハイブリッド（コードレビューで確認済み）** — 入力はフリーフォーム（100文字以内）、出力は厳密に事前定義（YES/NO/BLOCKED のみ）。`validateAnswer()` がYES/NO/BLOCKED以外を全てNOにフォールバック。LLMの生テキストは一切顧客に見せない
- **重要な含意:** フリーフォーム入力 = Undefined Customer Data (UCD) = Critical = **Red ASR**。この連鎖は設計の初期段階で理解しておくべき
- **2026年の新しい選択肢:** Allow-list approach（事前定義プロンプトのみ）にすれば UCD に該当せず → **Orange ASR → self-certify**。承認期間・工数が大幅に削減
- **トレードオフの構図:** フリーテキスト=クリエイティブの幅+LLM活用の意義 vs プリセット=ASR簡略化+承認短縮（ただしクリエイティブが犠牲+LLM不要の可能性）。2026年の新ルール（UCD=Red）を踏まえると、Arlaのジングル生成でも同じトレードオフが当てはまる
- Julia の DT チームの「事前定義プロンプトが必要かも」は、技術的制約ではなく **ASR分類を Orange に保つための戦略的選択**として正当化できる
- PetArmor (2026 US) ではプリセット + フリーフォームの両方を実装しているが、本番UIでのスコープは要確認

---

## Q5. AI Model & Infrastructure

**原文:** At a high level, what AI model/service did you use, and was it hosted within Amazon's infrastructure? Were there specific technical requirements from the approval side?

**日本語訳:** 使用したAIモデル/サービスは何ですか？Amazonインフラ内でホストされていましたか？承認上の技術要件は？

**ストレート回答:** Anthropic Claude 3 Sonnet on Amazon Bedrockを使用。RAG構成（Knowledge Bases + OpenSearch Serverless）、temperature=0.0。全てAmazonインフラ内でホスト（Bedrock要件として外部AI APIは不可）。

**回答ポイント:**
- **FM（コードレビューで確認済み）:** Anthropic Claude 3 Sonnet (`anthropic.claude-3-sonnet-20240229-v1:0`) on Amazon Bedrock。`bedrockVariables.ts` で全環境共通
- **埋め込み:** Cohere Embed English v3（Knowledge Bases用）
- **RAG:** Amazon Bedrock Knowledge Bases + Amazon OpenSearch Serverless（S3上の条件リスト約314件から検索）。`RetrieveAndGenerate` API使用
- **インフラ（コードレビューで確認済み）:** Lambda, API Gateway（REST）, DynamoDB（KMS+PITR）, S3, CloudWatch（6 log groups）, WAF, CloudTrail — 全てAmazonインフラ内。CDK Pipeline, us-west-2。3環境（dev/beta/prod）
- **温度設定:** `temperature: 0.0`, `topP: 1`（完全に決定論的）
- Fine-tuning は不採用（「小データセットではハルシネーションリスク増大」）
- **FAST統合:** Beta環境でFAST Stack + Hydra Stack を展開。Prod環境はコアBedrockスタックのみ
- **承認上の技術要件:** Bedrock使用必須（外部APIは不可）、FAST onboarding、全プロンプト/レスポンスのログ保存、Andon Cord 実装

---

## Q6. Documentation

**原文:** Is there any internal documentation, wiki, or approval template you went through that you could point us to? It would help us get a head start on our own submission.

**日本語訳:** 参考にできる社内Wiki・承認テンプレート等の共有依頼

**ストレート回答:** あり。ASR Profiles Wiki、FAST Wiki/SOP、自分が書いたGenerative AI for Campaign Quip等を共有できる。MARS固有のQuip（AI Tool Overview、ASR Kickoff、ISR等）も提供可能。

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

**ストレート回答:** 最大の教訓は2つ: (1) クライアントGenAI承認を初日から並行開始すること（3ヶ月超かかった）、(2) フリーフォーム入力=Red ASRの連鎖を設計初期に理解し、入力設計を戦略的に決めること。

**回答ポイント:**
- **クライアント GenAI 承認は想定以上に長い**（3ヶ月超）。UX/UI承認とは別トラックで早めに開始すべき
- **ASR は 4-6週間**。GenAI固有タスク12件が追加。DACEデータ分類を早めに完了させることが前提
- **フリーフォーム入力 = Red ASR** の連鎖を理解した上で設計判断を
- **FAST v2 のオンボーディングで技術的問題あり得る**（ResponseMissingError, v1→v2移行）
- **Andon Cord（即時停止機構）は必須**。SOPとデモ録画まで求められる
- **ミススペル対策は不完全:** Word Filter 1,494語でも競合名のタイポ全パターンはブロックできない（コードレビューで確認: `filtered-words.txt` はExcelから自動生成だが、3語超のフレーズはBedrock制約で除外）
- **Guardrailsアセット管理にコスト:** Denied Topics 28個 + Word Filters 1,494語 + PII全カテゴリの設定・メンテナンスは相当な工数。Excel管理 → スクリプト自動生成の仕組みを構築した
- **2026年のアドバイス:** プリセットのみでV1ローンチ（Orange）→ フリーフォーム追加でV2（Red）という段階的アプローチを推奨。Alec Kunkle (aleckunk@) が最新プロセスに詳しい

---

## 補足: PetArmor（2026 US）について

Julia への返信では詳細に触れない（聞かれていない）。「最近の事例として、NA TEXチームが新しい簡略化パスでAI on CLPをローンチ準備中。詳細はAlec Kunkle (aleckunk@) に連絡を」程度の言及にとどめる。
