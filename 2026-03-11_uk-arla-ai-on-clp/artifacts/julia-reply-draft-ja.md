# Julia への返信ドラフト — 最終版

**Subject:** RE: UK Arla Campaign -- AI on CLP: MARSの経験からの学び

---

Hi Julia,

ご連絡ありがとうございます。Arla "Morning Wins Worth Celebrating" のコンセプト、とても面白いですね！AU での MARS "For You Who Did That Thing You Did" (FYWDTTYD) キャンペーンで得た知見を共有します。以下、技術的な観点から各質問に回答します。ビジネス・オペレーション面については Luke が補足できると思います。

---

## 1. AI承認プロセス

承認トラックは3つあり、並行して進みます：Amazon社内（Legal/PR）、ASR（セキュリティレビュー）、クライアント側の承認です。2026年以降、ユーザーのトレーニングデータを扱わない GenAI キャンペーンは ASR で "Orange" に分類され、self-certification が可能になりました。これは MARS 当時と比べて大幅に簡素化されたプロセスです。

私たちは**3つの承認トラック**を同時並行で進めました：

- **Amazon社内承認**（Legal/PR/Business）-- `approvals.amazon.com` 経由で提出。プリセールス段階で早期にローカルの Legal・PR と連携しました。
- **Amazon Security Review (ASR)** -- 当アプリケーションは **Red**（最高セキュリティティア）に分類され、GenAI AppSec チームから専任のセキュリティレビュアーが割り当てられました。標準の ASR タスクに加えて、**12件の GenAI 固有タスク**がありました：Review Training Data、Review AI Model、Prompt Data Sanitization、Andon Cord レビュー、FAST (Framework for AI Security Testing) オンボーディング、AI Response Logging、Guardrails バリデーション、Siloed Sessions バリデーション、Bug Bounty オンボーディング等。
- **クライアント外部承認** -- Mars Inc. のグローバル法務・セキュリティチームが GenAI の使用を個別に承認する必要がありました。これは UX/UI 承認とは別トラックで、最終的に最も時間がかかった項目です。

**ASR分類に関する重要なポイント：** Red に分類された理由は、顧客からの**フリーフォームテキスト入力**を受け付けたためです。Amazon のデータ分類ポリシーでは、フリーフォーム入力 = Undefined Customer Data (UCD) = Critical データ = Red ASR となります。これは設計段階の早期に理解しておくべき最も重要なポイントです（Q4で詳述）。

**2026年アップデート：** 2024年以降、ASR のランドスケープは大幅に改善されました。ユーザーデータやトレーニングデータを扱わないアプリケーションは **Orange** に分類でき、self-certification が可能です。これにより専任の InfoSec レビュアーが不要になります。Orange に該当するかどうかは、入力設計に大きく依存します -- Q4を参照してください。

---

## 2. 承認タイムライン

エンドツーエンドで3ヶ月以上かかりました。ボトルネックはクライアントの GenAI 承認（3ヶ月以上）であり、Amazon側のレビュー（Legal/PR 約3週間、ASR 4-6週間）ではありませんでした。2026年に Orange ASR の対象となる設計であれば、ASR 部分は数日に短縮できます。

具体的な参考値として：MARSプロジェクトではASRアプリケーションを2024年3月11日に作成し、GenAI AppSecチームが7月19日頃に関与開始（Slackチャネル作成で確認）、8月29日にリリースしました。ASRレビュー実期間は約6週間で、正直なところギリギリでした。ASRレビューに2-3ヶ月確保することをお勧めします。

| トラック | 期間 | 備考 |
|-------|----------|-------|
| 社内 Legal/PR | 約3週間 | ドキュメントが揃えば比較的スムーズ |
| ASR (Security Review) | 4-6週間 | セルフサービス 2-3週間、その後 InfoSec レビュー 2-3週間。DT工数：約90時間（標準45h + GenAI固有45h） |
| クライアント GenAI 承認 | **3ヶ月以上** | 想定以上に長期化。Mars のグローバルチームが詳細な AI ドキュメントを要求 |

ASR レビューは複数のステージを経ました：セルフサービスチェックリスト、DACE データ分類、GenAI-Sec チームとのコンサルテーション、セキュリティエンジニアの割り当て、そして実際のレビュー（アーキテクチャ、脅威モデル、コードレビュー、ペネトレーションテスト）。プロジェクト全体の DT スコーピングは405時間でした。

**アドバイス：** クライアントの GenAI 承認トラックはできるだけ早く開始してください。UX/UI 承認とは別トラックであり、容易にクリティカルパスになり得ます。経験に基づくと、ASR + クライアント承認ワークストリームに2-3ヶ月を確保することを推奨します。

**2026年アップデート：** 設計が Orange ASR の対象（プリデファインド入力のみ）であれば、FAST 自動テストで self-certify できます。ASR 部分は4-6週間から数日に短縮されます。ただし、クライアント承認のタイムラインは Arla の社内プロセス次第です。

---

## 3. 入力処理とGuardrails

リアルタイムの人的モデレーションは使用しませんでした。代わりに、フロントエンドバリデーションから Bedrock Guardrails、出力制約までの6層の自動ガードレールシステムを構築し、徹底的なローンチ前テスト（FAST + ペネトレーションテスト + ステークホルダー UAT）と、必要時の即時シャットダウン用 Andon Cord キルスイッチを組み合わせました。

6つの独立したレイヤーによる**多層防御アーキテクチャ**を実装しました。具体的な内容をコードベースから確認してお伝えします：

**Layer 1 -- フロントエンド：**
- 100文字の入力制限（UIでハード制御 + サーバーサイドバリデーション）
- 必須の T&C チェックボックスと明示的な PII 免責事項：*"You agree that you will not enter sensitive personal data of another individual"*
- 透明性に関する通知：*"Prompts and results may be reviewed through automated and manual methods for abuse prevention"*
- AI 目的の免責事項：*"AI powered for entertainment purposes"*

**Layer 2 -- ネットワーク：**
- AWS WAF（6ルール）：Common Rule Set、Known Bad Inputs、IP Reputation List、Anonymous IP List、Bot Control、IP ベースのレートリミット（5分あたり2,000リクエスト）
- WAF ログは KMS で暗号化、5年間保持

**Layer 3 -- API Gateway：**
- Lambda Authorizer（オリジンホワイトリスト + トークン検証）
- Request Validator（厳密なスキーマ、beta/prod では `additionalProperties: false`）
- スロットリング：30 req/s、バースト 20

**Layer 4 -- アプリケーションレベルの入力バリデーション：**
- 5段階のサニタイゼーションパイプライン：100文字切り詰め、小文字化、マルチバイト句読点の正規化、絵文字除去、URIエンコーディング、CRLF除去
- ユーザー入力は構造化された XML スタイルのプロンプトテンプレートにラップしてからモデルに送信（ユーザーテキストを指示から分離することでプロンプトインジェクションを防止）

**Layer 5 -- Amazon Bedrock Guardrails（すべて最大強度に設定）：**
- Content Filters：6カテゴリすべて HIGH（Hate、Sexual、Violence、Insults、Misconduct、Prompt Attack）
- Denied Topics：28トピック（5つのビルトイン + 23のカスタム。Alcohol、Brand safety、Celebrities、Competitors、Copyright、Politics、Religion、Security 等）
- Word Filters：1,494件のブロック対象ワード/フレーズ（複数言語対応。競合ブランド名、過激主義用語、冒涜語等 -- 管理用 Excel スプレッドシートから自動生成）
- PII Filters：**すべての PII カテゴリを BLOCK に設定**（General、IT、Finance、US/Canada/UK 固有）+ カスタム正規表現パターン

**Layer 6 -- 出力制御：**
- LLM レスポンスを厳密に **YES / NO / BLOCKED** のみに制約 -- 生の LLM テキストが顧客に表示されることは一切なし。予期しない出力は自動的に NO にデフォルト。
- すべてのリクエストとレスポンスを専用の DynamoDB テーブルに記録（KMS 暗号化、ポイントインタイムリカバリ有効）。記録内容：入力、プロンプト、回答、LLM 出力テキスト、引用、Guardrail アクション、タイムスタンプ

**Andon Cord（ASR必須）：**
- Lambda 環境変数による AI 機能の即時無効化（503を返す）。文書化された SOP とデモ録画がセキュリティレビュー時に明示的に要求されました。

**モデレーションアプローチに関する重要な注意：**
入出力のリアルタイム人的モデレーションは**実施していません**。代わりに、3つの柱に依拠しました：

1. **堅牢な自動ガードレール**（上記の6層アーキテクチャ） -- 人的介入なしでリアルタイムにコンテンツフィルタリングと安全性を確保
2. **徹底的なローンチ前テスト** -- FAST 自動プロンプトセキュリティテスト（beta 環境での Hydra ベース）、ASR の一環としての GenAI AppSec チームによるペネトレーションテスト、全ステークホルダー（クライアント、Legal、PR、DT）によるハンズオン UAT でガードレールの実効性を実際のプロンプトで検証
3. **インシデントレスポンス計画** -- エスカレーションパス、責任者、手順を文書化した正式な Incident Response Plan (ISR) を作成。必要時の AI 即時シャットダウン用 Andon Cord キルスイッチと組み合わせ

**ローンチ後のモニタリング：**
- **CloudWatch アラーム** -- 4つの CloudTrail ベースアラーム（コンソールサインイン失敗、認可失敗、CloudTrail 設定変更、IAM ポリシー変更）に SNS メール通知をチーム配布リストに設定。インフラ/セキュリティの異常に対する自動アラート。
- **CloudWatch Dashboard** -- チーム全体の可視性のため、WAF ログモニタリングダッシュボードを Wiki に埋め込み
- **DynamoDB 全ログ** -- すべてのリクエスト/レスポンスペアを `BedrockResponseTable` に保存（KMS 暗号化、PITR 有効）。全 AI インタラクションの事後分析が可能
- 収集した入出力の週次バッチレビュー
- BIL チームによる隔週の手動データレビュー

---

## 4. プリデファインド vs. フリーフォーム入力

はい、この議論はしました。プリデファインド入力だけではクライアントのクリエイティブ要件を満たせず、プリデファインドのみであれば LLM を使う必要性自体がなかったため、マルチレイヤーガードレール付きのフリーフォーム入力を選択しました。トレードオフは Red ASR 分類を受け入れることでした。2026年においては、プリデファインドのみ = Orange ASR = self-certification であり、戦略的に有力なパスです。

これは最大の設計トレードオフであり、セキュリティ分類と承認タイムラインに直接影響します。

入力をプリデファインドプロンプトに制限することを Plan B として検討しました。しかし、プリデファインドプロンプトでは**クライアントのクリエイティブ要件を部分的にしか満たせない**と結論づけました -- クリエイティブソリューションとしての体験が大幅に弱くなります。Mars キャンペーンでは顧客が自分自身の達成をフリーテキストで記述する必要があり、本質的にオープンエンドです。さらに、プリデファインドプロンプトのみで進めた場合、**LLM を使う実質的な必要性がなくなります** -- 単純なルックアップテーブルやルールベースシステムで対応できたでしょう。LLM を導入した理由は、フリーフォームの自然言語入力を解釈・分類する能力にありました。

**私たちのアプローチ（MARS）：** フリーフォームテキスト入力（最大100文字）を受け付けつつ、出力を厳密に3つのレスポンス（YES / NO / BLOCKED）に制約しました。生の LLM レスポンスが顧客に表示されることはありませんでした。考え方としては：フリー入力 -> AI 分類 -> プリデファインド出力。

**その結果：** フリーフォーム入力を受け付けたため、データは **Undefined Customer Data (UCD) = Critical** に分類され、**Red ASR 分類**がトリガーされました。これにより：専任セキュリティレビュアー、手動プロンプトテスト、約90時間の DT セキュリティ作業、4-6週間の ASR タイムライン、Q3で説明した完全なマルチレイヤーガードレールセットアップが必要になりました。重要な点として、免責事項や UI 警告はデータ分類を下げません -- UCD 分類をトリガーするのはフリーフォーム入力フィールドの存在そのものです。

**代替案（2026年推奨）：** 入力を**プリデファインドプロンプトのみ**（アローリストアプローチ）に制限すれば、データは UCD に分類されません。ASR 分類は **Orange** にとどまり、**self-certification** が可能になります -- 専任セキュリティレビュアー不要、FAST 自動テストで十分、タイムラインは劇的に短縮されます。なお、このルートを取る場合、ジングル生成の複雑さ次第では LLM すら不要かもしれません -- テンプレートベースのアプローチで足りる可能性があります。ただし、プリデファインドカテゴリ内でもクリエイティブなバリエーションが欲しい場合は、LLM が価値を発揮します。

**DT チームの直感は正しいです。** 「プリデファインドメッセージ/プロンプトを使用する必要があるかもしれない」という初期フィードバックは、技術的な安全性の観点だけでなく、セキュリティ分類と承認パスを根本的に変えるという点で、戦略的に健全な推奨です。

**私の推奨 -- 段階的アプローチ：**
- **V1：** プリデファインドプロンプトのみ -> Orange ASR -> self-certify -> 迅速なローンチ
- **V2（必要に応じて）：** フリーフォーム入力を追加 -> Red ASR -> フルセキュリティレビュー

これはまさに NA TEX チームが最近のキャンペーンで採用しているパターンです。

---

## 5. AIモデルとインフラストラクチャ

Anthropic Claude 3 Sonnet を Amazon Bedrock 上で使用し、RAG 構成（Knowledge Bases + OpenSearch Serverless）、temperature は完全に決定論的なレスポンスのため 0.0 に設定しました。すべて Amazon インフラ内でホスト -- 外部 AI API は Bedrock 要件で許可されていません。

| コンポーネント | 使用したもの |
|-----------|-------------|
| Foundation Model | **Anthropic Claude 3 Sonnet** on Amazon Bedrock |
| Embedding | Cohere Embed English v3（Knowledge Base インデキシング用） |
| RAG | Amazon Bedrock Knowledge Bases + Amazon OpenSearch Serverless |
| Guardrails | Amazon Bedrock Guardrails（ネイティブ、CDK管理） |
| Compute | AWS Lambda |
| API | API Gateway (REST) |
| Database | DynamoDB（プロンプト/レスポンスログ、KMS暗号化） |
| Storage | S3（Knowledge Base データソース + CloudTrail ログ） |
| Security | AWS WAF、CloudWatch（6ロググループ）、CloudTrail |
| Region | us-west-2 (Oregon) |
| IaC | CDK Pipeline、3環境（dev/beta/prod） |

主要な技術的判断：
- **Temperature: 0.0**（完全に決定論的、レスポンスにランダム性なし）
- **RAG over fine-tuning** -- 小規模データセットでのファインチューニングはハルシネーションリスクが高まると判断
- **Single-turn のみ** -- マルチターン会話なし、セッション永続化なし（"Siloed Sessions" ASR 要件を簡素化）
- **FAST インテグレーション**を beta 環境で実施（Hydra ベースの自動プロンプトセキュリティテスト）
- すべて Amazon インフラ内でホスト（Bedrock 要件 -- 外部 AI API は不可）

Arla のジングル生成については、モデル選択は異なる可能性が高いです（分類ではなくクリエイティブなテキスト生成にはより高性能なモデルが必要）。ただし、インフラパターンとセキュリティアーキテクチャは非常に類似したものになるでしょう。

---

## 6. ドキュメント

はい -- ご案内できる社内リソースがいくつかあります。加えて、MARS 固有の Quip ドキュメント（AI ツール概要、ASR キックオフ、インシデントレスポンス計画、Guardrails スプレッドシート）も必要であれば共有できます。

参考となる主要な社内リソース：

| リソース | リンク |
|----------|------|
| ASR Profiles & Classification Rules | https://w.amazon.com/bin/view/Infosec/Proactive_Security/Dev/SecurityReviewTooling/ASR/Profiles/ |
| FAST Framework (v2) | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/ |
| FAST Integration SOP (BIL TEX) | https://quip-amazon.com/FhvFAKBxf6Tu/SOP-FAST-Integration |
| Generative AI for Campaign（私が書いたガイド） | https://quip-amazon.com/aa1OAHdOJgua/Generative-AI-for-Campaign |
| BIL Approved AI Tools | https://w.amazon.com/bin/view/BIL-E/NA/BIL-AI-Tools |
| GenAI Security Standard (policy) | https://policy.a2z.com/docs/613805/publication |
| Andon Cord Guidance | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Guidance/Andon_Cords/ |

MARS 固有の Quip ドキュメント（AI ツール概要、ASR キックオフ、インシデントレスポンス計画、Guardrails スプレッドシート、モニタリングランブック）も必要であれば共有します -- お知らせください。

---

## 7. 学んだこと

最大の2つのポイント：クライアントの GenAI 承認は初日から開始すること（私たちは3ヶ月以上かかりクリティカルパスになりました）、そして入力設計にコミットする前にフリーフォーム入力 = Red ASR の連鎖を理解すること -- この1つの判断がセキュリティタイムライン全体を決定します。

1. **クライアントの GenAI 承認は想定以上に時間がかかる。** 私たちは3ヶ月以上かかりました（UX/UIは数週間）。初日からこのトラックを並行で開始し、詳細な AI 概要ドキュメントを早期にクライアントに準備してください。

2. **フリーフォーム入力 = Red ASR。これは絶対です。** 入力設計にコミットする前に UCD -> Critical -> Red の連鎖を理解してください。この1つの判断がセキュリティタイムライン全体と DT 作業量を決定します。免責事項は役に立ちません -- UCD 分類をトリガーするのは入力フィールドの存在そのものです。

3. **ASR は大きな工数を要する。** 4-6週間、DT 作業約90時間、12件の GenAI 固有タスク。DACE データ分類は前提条件なので早期に完了させるべきです。

4. **Andon Cord は必須。** AI 機能の即時キルスイッチが必要で、文書化された SOP と録画デモが求められます。ASR で交渉の余地なしでした。

5. **ワード/競合ブロッキングは不完全。** 1,494件のブロックワード（競合名50件以上含む）でも、スペルミスはすり抜けます。Guardrails アセット管理（denied topics、ワードリスト、PII パターン）は継続的なメンテナンスが必要です -- これを管理するため Excel スプレッドシートから Bedrock 設定への自動パイプラインを構築しました。

6. **FAST オンボーディングは困難を伴う可能性がある。** `ResponseMissingError` に遭遇し、プロジェクト途中で v1 から v2 への移行を乗り越える必要がありました。インテグレーション問題に時間を見込んでおいてください。

7. **すべてを個別にログする。** すべてのプロンプトとレスポンスは専用の暗号化データストアに保存する必要があります（CloudWatch だけでは不十分）。これは ASR 要件であり、ローンチ後のモニタリングにも不可欠です。

8. **制約を前提に設計する。** 最も強力な安全対策は出力を YES/NO/BLOCKED に制約したことでした -- 生の LLM テキストを表示しないことで、リスクのカテゴリ全体を排除しました。ジングル機能における「最小限の AI 出力」が何かを検討してください。

---

## 推奨される次のステップ

2024年の MARS キャンペーン以降、プロセスはかなり進化しています。Orange/FAST self-certification パスに関する最新のガイダンスについては、NA TEX チームの **Alec Kunkle (aleckunk@)** に連絡することを強くお勧めします。彼は最近の AI on CLP 実装をリードしており、現在のプロセスとツールについて説明してくれます。

私たちからは、以下のサポートが可能です：
- MARS の Quip ドキュメントパッケージの共有
- コールでのアーキテクチャの詳細説明
- DT チームが提案するアーキテクチャの、セキュリティ/ASR 観点からのレビュー

私たちは AEDT（シドニー）にいますので、こちらの朝 / そちらの午後遅めの時間帯がコールに適しています。

Best,
Shugo
