## Q1. AI Approval Process

**原文:** What was the end-to-end process for getting the AI tool approved for use on CLP? Which teams/stakeholders were involved in the review (e.g., Legal, Trust & Safety, AdTech)?

**日本語訳:** CLPでのAIツール使用承認のエンドツーエンドのプロセスはどのようなものでしたか？レビューに関わったチーム/ステークホルダーは？

大まかに、下記 3つの並行承認トラックがありました:
- Amazon社内承認（Legal/PR/Business）-- approvals.amazon.com 経由で提出。プリセールス段階で早期にローカルの Legal・PR と連携しました。
- Amazon Security Review (ASR) -- 当アプリケーションは Red に分類され、GenAI AppSec チームの専任のセキュリティレビュアーによるレビューが必須でした。標準の ASR タスクに加えて、12件の GenAI 固有タスクがありました。
- クライアント外部承認 -- Mars Inc. のグローバル法務・セキュリティチームが GenAI の使用を個別に承認する必要がありました。これは UX/UI 承認とは別トラックで、最終的に最も時間がかかった項目です。

補足: ASRについて。アプリケーションが Orange 以下に分類されれば、セルフサービスでレビューを完了することができ、タイムラインを大幅に短縮することができます（外部のレビュアーによるHuman reviewは必要ない）。2026年現在であれば、Critical/Restrictedを扱わない = pre-defined の message/prompt であれば GenAI を利用していても Orange 分類となる可能性があります。

---

## Q2. Approval Timeline

**原文:** How long did the approval process take from initial proposal to green light? Were there multiple review stages?

**日本語訳:** 最初の提案からゴーサインが出るまで、承認プロセスにどのくらいかかりましたか？複数のレビュー段階がありましたか？

全体で最短でも3ヶ月超かかりました。内部Legal/PRは約3週間、ASRは約6週間だが、クライアントGenAI承認が3ヶ月超と最長ボトルネックでした。

---

## Q3. Input Handling

**原文:** How did you manage user-generated input? Did you use any guardrails, content filters, or moderation layers to ensure appropriate responses?

**日本語訳:** ユーザー生成入力はどのように管理しましたか？適切な応答を確保するためのガードレール、コンテンツフィルター、モデレーションレイヤーは使用しましたか？

下記の5つのポイントで対応しました：
- ユーザインプットの多層自動ガードレール -- フロントエンドバリデーション、AWS WAF、API Gatewayコントロール、アプリケーションレベルのサニタイゼーション、Amazon Bedrock Guardrails（Prompt attacks, コンテンツフィルター、禁止トピック、ワードフィルター、PIIブロック）
- 出力制約 - レスポンスをYES/NO/BLOCKEDのみに制約することで、生のLLMテキストが顧客に表示されることは一切ないように設計
- 徹底的なローンチ前テスト -- FAST自動プロンプトセキュリティテスト、GenAI AppSecによるペネトレーションテスト、全ステークホルダーによるハンズオンUAT
- インシデントレスポンス -- 正式な対応計画 + Andon CordキルスイッチによるAI即時シャットダウン（ASR必須）
- 全リクエスト/レスポンスの個別ログ保存と事後モニタリング -- DynamoDB, CloudWatch へのログ保存とキャンペーンフライト中の定期チェック（週次 + 隔週BILチームレビュー）を行いました。(リソースの観点から、リアルタイムの人手モデレーションは採用しませんでした)

---

## Q4. Pre-defined vs. Free-form

**原文:** Was there ever a discussion about restricting inputs to pre-defined prompts vs. allowing free text? What were the key considerations that led to your approach?

**日本語訳:** 入力を事前定義プロンプトに制限するか、フリーテキストを許可するかについて議論はありましたか？最終的なアプローチに至った主な考慮事項は何でしたか？

はい、議論しました。事前定義プロンプトへの制限は Plan B として検討されましたが、プリセットのみではクライアント要件を満たすクリエイティブアイデアを実現できないため、プロトタイプを開発しフィージビリティ確認の上、フリーテキスト＋多層ガードレールを選択しました。
* プリセットのみの場合、LLM自体が不要になります。
我々のユースケースでは、入力制限の代わりに事前定義された厳密な出力制限 - 出力はYES/NO/BLOCKED のみ - を加えています。

---

## Q5. AI Model & Infrastructure

**原文:** At a high level, what AI model/service did you use, and was it hosted within Amazon's infrastructure? Were there specific technical requirements from the approval side?

**日本語訳:** 使用したAIモデル/サービスは何ですか？Amazonインフラ内でホストされていましたか？承認上の技術要件は？

Anthropic Claude 3 Sonnet on Amazon Bedrockを使用したRAG構成（Knowledge Bases + OpenSearch Serverless）、全てAmazonインフラ内のサーバレス構成です。

- **Model:** Anthropic Claude 3 Sonnet on Amazon Bedrock
- **埋め込み:** Cohere Embed English v3（Knowledge Bases用）
- **RAG:** Amazon Bedrock Knowledge Bases + Amazon OpenSearch Serverless
- **FAST統合:** Beta環境でFAST Stack + Hydra Stack を展開。Prod環境はコアBedrockスタックのみ
- **承認上の技術要件:** Legal面: Bedrock使用必須・キャンペーン/モデルごとの個別承認、セキュリティ面: ASR準拠（FAST onboarding、全プロンプト/レスポンスのログ保存、Andon Cord 実装、など）

---

## Q6. Documentation

**原文:** Is there any internal documentation, wiki, or approval template you went through that you could point us to? It would help us get a head start on our own submission.

**日本語訳:** 参考にできる社内Wiki・承認テンプレート等の共有依頼

下記にドキュメントを共有します:

- ASR: https://w.amazon.com/bin/view/Review_Automation/SecurityReviews/
- SDO Information Security Support Portal: https://support.security.amazon.dev/tags
- Mars関連のQuip (開発関連): https://quip-amazon.com/Tnk0OtquZA7d/AU-Mars-FYWDTTYD-

---

## Q7. Lessons Learned

**原文:** Anything you'd do differently or any pitfalls to watch out for in the approval process?

**日本語訳:** やり直すなら何を変えるか、承認プロセスの落とし穴は？

最大の教訓は2つ: (1) クライアントGenAI承認を初日から並行開始すること（3ヶ月超かかった）、(2) できるだけ早く GenAI AppSec チームに連絡し、ASRのプロセスを開始すること

---

## 補足: 最新プロセスについて

2024年以降、GenAI アプリケーション承認プロセスはかなり変化しています。すでに連絡済みかもしれませんが、TEX チームの Alec Kunkle (aleckunk@) に連絡し、Orange/FAST self-certification パスに関する最新の情報を得ることをお勧めします。
