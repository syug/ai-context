# Handover Document
**Topic:** PetArmor AI on CLP Deep Dive — BIL TEX AIリファレンスアーキテクチャ研究
**Date:** 2026-03-13
**Status:** 進行中

---

## 背景

uk-arla-ai-on-clp トピックでのArla返信準備中に、PetArmor「Protect Playtime」（NA TEX、Alec Kunkle担当）のAI実装を調査した。その結果、BIL TEX における AI on CLP のリファレンスアーキテクチャとして非常に価値の高い知見が得られたため、独立トピックとしてスピンアウトし、さらに深掘りする。

## 元トピックからの移管情報

### PetArmor「Protect Playtime」概要
- **Phase 1:** クイズ + ブランドストア（AI なし）— 2/2/2026 ローンチ
- **Phase 2:** AI pet recommendations — 4/6/2026 ローンチ予定
- **ASR:** Orange self-certify 取得（01/20/26 WW BIL WBR で確認）
- **FAST:** オンボード完了（同日）

### リポジトリ構成
| リポ | 内容 | Bindle |
|---|---|---|
| BIL-TEX-PetArmor-ProtectPlaytime-BrandStore | Phase 1 フロントエンド（AI なし） | BIL-NA-Endemic-Campaigns |
| BIL-TEX-PetArmor-ProtectPlaytime-CDK | Phase 1 S3+CloudFront | 同上 |
| BestFriendsAnimalSocietyAdoptionServiceCDK | AI バックエンド CDK | 専用 Bindle |
| BestFriendsAnimalSocietyAdoptionServicePlayground | AI デモ UI（Harmony） | 同上 |
| BestFriendsAnimalSocietyAdoptionServiceTests | FAST テスト | 同上 |

### Bindle
- **名前:** `BestFriendsAnimalSocietyAdoptionService`
- **Owner:** fitzmaro
- **Team:** Brand Innovation Lab NA - Campaign Development
- **CTI:** Advertising > Brand Lab > WW TEX

### AWS Accounts
- Non-prod: `130413243566`
- Prod: `898310714909`

### AI スタック
- **Model:** Claude Sonnet 4.5 (Prod) / Haiku 4.5 (Non-prod) on Bedrock
- **SDK:** Vercel AI SDK (`ai` + `@ai-sdk/amazon-bedrock`)
- **Tool Use:** `toolChoice: 'required'`, `maxSteps: 5`, `queryAnimals` ツールのみ
- **ガードレール 11層:** Tool-only / ステップ制限 / 入力長制限 / AI分類(4カテゴリ) / fail-closed / Zod enum / 結果5件上限 / フォールバック / 非同期 / カスタムエラー / 監査ログ
- **PII フィルタリング:** 未実装（AI分類に PII カテゴリなし）
- **Bedrock Guardrails:** 未使用（全てカスタム実装）

### FAST 統合
- Gamma ステージで `FASTIntegration Tests` 実行
- Hydra (Fargate) 上で FAST Python client が RecommendProcessorLambda を直接 invoke
- 閾値: output_validity 0.6 / pii 0.6 / deflection 0.6
- AAA relationships: GenAISecurityPromptsService + GenAISecurityScoringService + CloudAuthServer

### データ取り扱いリスク
| Issue | Severity |
|---|---|
| CloudWatch Logs にプロンプト全文記録（14日保持） | HIGH |
| PII フィルタリング未実装（入力側） | HIGH |
| UI に PII disclaimer なし | HIGH |
| RecommendJobs TTL有効化が外部依存 | MEDIUM |

### ASR Orange 分類の謎
- WBR記録: Orange self-certify でリリース
- 実装コード: フリーフォーム入力が存在する（`/recommend` エンドポイントで `{ prompt: "..." }`）
- ポリシー上はフリーフォーム = UCD = Critical = Red
- **ギャップ:** ASR認証時点でのスコープが不明。allow-listのみで認証 → 後からフリーフォーム追加の可能性

## リサーチ結果サマリー

| # | 領域 | 判明事項 | 確度 | ソース | 未解明/要深掘り |
|---|------|---------|------|--------|----------------|
| 1 | **ASR分類** | Orange self-certify で認証完了（01/20/26） | 高 | WBR 3本で裏取り | フリーフォーム入力があるのにOrange取得できた理由が不明 |
| 2 | **ASR Orange条件** | GenAI使用 + Critical/Restricted非該当 + UCD非該当 → Orange。フリーフォーム=UCD=Critical=Red | 高 | ASR Profiles Wiki + ポリシー文書 | PetArmorがこの条件をどう満たしたか |
| 3 | **AIモデル** | Claude Sonnet 4.5 (Prod) / Haiku 4.5 (Non-prod) on Bedrock | 高 | コードレビュー (`bedrockVariables`) | — |
| 4 | **出力制約** | `toolChoice: 'required'` でツール実行のみ。テキスト生成禁止 | 高 | コードレビュー | MARS(YES/NO/BLOCKED) との設計トレードオフ比較 |
| 5 | **ガードレール** | カスタム11層。Bedrock Guardrails未使用 | 高 | コードレビュー | なぜBedrock Guardrails不採用？MARSは使用していた |
| 6 | **入力方式** | フリーフォーム（`/recommend`）+ プリセット（AI事前生成8-12個） | 高 | コードレビュー | ASR認証時のスコープ（プリセットのみで申請？） |
| 7 | **FAST統合** | Hydra (Fargate) + FAST Python client。閾値 0.6/0.6/0.6 | 高 | コードレビュー (CDK) | 閾値の意味、テスト内容、SOP詳細 |
| 8 | **PII対策** | 未実装（AI分類にPIIカテゴリなし） | 高 | コードレビュー | MARSは全カテゴリBLOCK。差異の根拠は？ |
| 9 | **データ保存** | CloudWatch Logsにプロンプト全文（14日）。専用DBなし | 高 | コードレビュー | MARS(DynamoDB KMS暗号化)との差、許容される理由 |
| 10 | **SDK** | Vercel AI SDK (`ai` + `@ai-sdk/amazon-bedrock`) | 高 | コードレビュー | BIL TEXでの採用前例、Bedrock SDK直接との比較 |
| 11 | **Phase構成** | Phase 1(AIなし 2/2) → Phase 2(AI追加 4/6) | 高 | WBR + コード | Phase別ASR？Phase 2はRed再認証が必要？ |
| 12 | **Bindle構成** | フロントエンド=リージョンHolding / AI=専用Bindle | 高 | コード + Slack | InfoSecレビュー必要 → 専用Bindleのルール |

### MARS FYWDTTYD vs PetArmor 比較（初版）

| 観点 | MARS FYWDTTYD (2024 AU) | PetArmor (2026 US) |
|------|------------------------|-------------------|
| **ASR分類** | Red | Orange |
| **入力** | フリーフォーム（100文字） | フリーフォーム + プリセット |
| **出力** | YES/NO/BLOCKED（テキスト制約） | ツール実行結果のみ（Tool Use制約） |
| **モデル** | Claude 3 Sonnet | Claude Sonnet 4.5 |
| **SDK** | Bedrock REST API 直接 | Vercel AI SDK |
| **RAG** | Knowledge Bases + OpenSearch | なし（DynamoDB直接クエリ） |
| **Bedrock Guardrails** | 使用（4フィルタ、28 Denied Topics、1,494 Words、PII全BLOCK） | 未使用（カスタム実装） |
| **ガードレール層数** | 6層 | 11層（カスタム） |
| **PII対策** | Bedrock全カテゴリBLOCK + カスタム正規表現 | 未実装 |
| **ログ保存** | DynamoDB専用テーブル（KMS暗号化、PITR） | CloudWatch Logs（14日） |
| **FAST** | 未使用（2024年時点では未導入） | 統合済み（Hydra Stack） |
| **Andon Cord** | 環境変数で即時停止（SOP+デモ録画） | 未確認 |
| **ASR期間** | 約6週間（ギリギリ） | 不明（self-certifyで短縮？） |
| **クライアント承認** | 3ヶ月超 | 不明 |
| **温度** | 0.0（決定論的） | 未確認 |
| **非同期処理** | なし（同期） | あり（ジョブ+ポーリング） |

## 深掘り方針

### 1. ASR Orange取得の実経緯解明
- Alec (aleckunk) に確認: フリーフォーム入力があるのにOrangeを取得できた理由
- ASR Application ID を特定し、認証時のスコープを確認
- Phase 1（AIなし）とPhase 2（AI追加）で別々のASRなのか

### 2. Tool Use パターンの詳細解析
- `toolChoice: 'required'` による出力制約の仕組み
- queryAnimals ツールの設計（入力パラメータ、バリデーション）
- MARS（YES/NO/BLOCKED）との比較: Tool Use vs テキスト制約の設計トレードオフ

### 3. FAST 統合の完全理解
- Hydra Stack の構成とテスト実行フロー
- 閾値の意味と妥当性（output_validity 0.6 / pii 0.6 / deflection 0.6）
- FAST SOP Quip（`FhvFAKBxf6Tu`）の読み込み
- BIL TEX 向けの FAST 導入ガイドとしてドキュメント化

### 4. リファレンスアーキテクチャの体系化
- PetArmor + MARS FYWDTTYD の比較表
- AI on CLP を始めるチーム向けのアーキテクチャガイド
- Orange パス vs Red パスの意思決定フローチャート
- Bedrock Guardrails vs カスタム実装のトレードオフ

### 5. PII/データ取り扱いリスクの評価
- CloudWatch Logs のプロンプト全文記録は許容されるのか
- PII フィルタリング未実装で Orange 通過できた理由
- MARS（全カテゴリBLOCK）vs PetArmor（未実装）の差異の根拠

## 成果物一覧

```
2026-03-13_petarmor-ai-on-clp-deep-dive/
├── handover.md
├── artifacts/
└── notes/
```

元トピックの関連ノート（参照用）:
- `2026-03-11_uk-arla-ai-on-clp/notes/bestfriends-ai-analysis-ja.md`
- `2026-03-11_uk-arla-ai-on-clp/notes/bestfriends-data-handling-analysis.md`
- `2026-03-11_uk-arla-ai-on-clp/notes/petarmor-cdk-investigation-ja.md`
- `2026-03-11_uk-arla-ai-on-clp/notes/ucd-pii-asr-investigation.md`
- `2026-03-11_uk-arla-ai-on-clp/notes/fast-prompt-test-analysis.md`
- `2026-03-11_uk-arla-ai-on-clp/notes/fast-prompt-test-analysis-ja.md`

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|---|---|---|
| 1 | - | Alec (aleckunk) に確認: Orange取得の経緯、フリーフォーム入力のスコープ | 未着手 |
| 2 | - | FAST SOP Quip 読み込み・詳細理解 | 未着手 |
| 3 | - | Tool Use パターンの詳細コード解析 | 未着手 |
| 4 | - | MARS vs PetArmor 比較表作成 | 未着手 |
| 5 | - | AI on CLP リファレンスアーキテクチャガイド作成 | 未着手 |

## 重要な判断ログ

- uk-arla-ai-on-clp からのスピンアウト（3/13）。PetArmor調査結果の価値が高く独立トピックとして深掘りする判断
- cat-decoder-tech-case-study とのマージは見送り（アーキテクチャが全く異なる: GPU/LivePortrait vs Bedrock/RAG/Guardrails）

## 担当者
- **Alec Kunkle** (`aleckunk`) — NA DT L6。PetArmor AI担当、FAST onboard実施者
- **fitzmaro** — BestFriendsAnimalSocietyAdoptionService Bindle owner、NA DT Head
- **yuvikoul** — Design Inspector 最終更新者
- **@monatang** — FAST Integration SOP を `#bil-ww-tex-dt` で共有（2026/1/7）

## 主要リソース一覧

| リソース | URL |
|---|---|
| PetArmor AI Bindle | https://bindles.amazon.com/software_app/BestFriendsAnimalSocietyAdoptionService |
| Design Inspector | https://design-inspector.a2z.com/#IBestFriendsAnimalSocietyAdoptionServiceBackend |
| Harmony Playground (Beta) | https://bestfriendsanimalsocietyadoptionserviceplayground.beta.harmony.a2z.com/ |
| Harmony Playground (Prod) | https://console.harmony.a2z.com/bestfriendsanimalsocietyadoptionserviceplayground/ |
| BuilderHub Create | https://create.hub.amazon.dev/cloned-applications/BestFriendsAnimalSocietyAdoptionService |
| FAST Wiki | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/ |
| FAST Integration SOP | https://quip-amazon.com/FhvFAKBxf6Tu/SOP-FAST-Integration |
| ASR Profiles | https://w.amazon.com/bin/view/Infosec/Proactive_Security/Dev/SecurityReviewTooling/ASR/Profiles/ |
| UCD/PII ポリシー | https://w.amazon.com/bin/view/InfoSec/Application_Security/AppSTAR/Appsec_AI/When_is_a_GenAI_ASR_Profile_required_/ |

## 関連トピック

- `2026-03-11_uk-arla-ai-on-clp` — 元トピック。PetArmor調査はArla返信の一環として実施
- `2026-02-26_cat-decoder-tech-case-study` — MARS Dine MindReader / Cat Decoder（別のAI on CLP事例、GPU/LivePortrait系）
