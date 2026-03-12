# Handover Document
**Topic:** UK Arla Campaign — AI on CLP 承認プロセス調査・返信準備
**Date:** 2026-03-13
**Status:** 進行中

---

## 背景

Julia Sampaio（UK BIL Solutions Manager）から Luke & Shugo 宛に、Arla（乳製品ブランド、UK市場）のCLPキャンペーンでAIジングル生成を組み込みたいという相談メール（2026/3/11）。コンセプト「Morning Wins Worth Celebrating」。MARS「For You Who Did That Thing You Did」キャンペーンでのAI on CLP経験について7項目の質問。

ユーザーの指示: MARSは2024年実施なので思い出す必要あり。加えて、2025-2026年の承認プロセス更新（PetArmor/FAST/ASR Orange分類）を調査。

## 現在の状況

### メール確認・翻訳
- Julia のメール全文を取得・日本語訳を提供済み
- 7つの質問をサマライズ済み

### 承認プロセス調査（完了）

#### Before（2024 MARS時代）
- GenAI = ASR Red、InfoSec手動レビュー必須、SLA 30日以上
- Legal事前承認不可、EU Legalは四半期1件制約
- Greenies Pet Interpreter（2024/5）でLegal報告漏れの教訓
- 2024/6 TEX-Anthropicミーティングで課題共有

#### After（2026〜）
- **ASR分類変更:** ユーザーデータ/トレーニングを扱わないGenAIアプリ → Orange（self-certify可能）
- **FAST（Framework for AI Security Testing）:** 全GenAIエクスペリエンスに必須化。V2が現行。自動プロンプトテスト
- **PetArmor事例:** BIL TEXがASR完了+FASTオンボード（01/20/26）。Phase 2で AI pet recommendations（4/6/26〜）

#### UCD/PII分類の重要な発見
- **フリーフォーム入力 = Undefined Customer Data (UCD) = Critical = Red**（ポリシー確認済み）
- UIラベル/disclaimerでは分類を下げられない（"Disclaimers or warnings do not lower the data classification"）
- **Allow-list（事前定義プロンプト）のみにすればUCD回避 → Orange維持可能**
- PetArmorがOrange判定を得た理由: おそらく本番UIではプリセットのみで出す想定（フリーフォームはPlayground限定）

### MARS FYWDTTYD Quip 読み込み（完了）
- `https://quip-amazon.com/Tnk0OtquZA7d/AU-Mars-FYWDTTYD-` 配下の全ドキュメントを読み込み
- Julia の7質問全てに対する回答素材を抽出済み
- 主要発見:
  - **3並行承認トラック:** Amazon内部(Legal/PR) + ASR(Red, GenAI 12タスク) + クライアント外部
  - **タイムライン:** Legal ~3週間 / ASR 4-6週間(DT 90h) / クライアント承認 3ヶ月超
  - **5層ガードレール:** 入力バリデーション / Bedrock Guardrails / レスポンス簡素化(YES/NO/BLOCKED) / プロンプト内指示 / WAF
  - **出力設計:** FM生テキストは一切顧客に表示されない（YES/NO/BLOCKED の3択のみ）
  - **Andon Cord必須:** 環境変数で即時AI無効化、SOP+デモ録画が求められた
  - **技術スタック:** Claude 3 Sonnet / Bedrock / RAG(Knowledge Bases + OpenSearch) / temp=0.0

### Julia への返信ドラフト準備（進行中）
- 質問×回答ポイント対照表を作成済み（`notes/julia-reply-draft-points-ja.md`）
- 方針: テック面のみ、2026年更新は軽く触れAlecへの連絡をサジェスト
- 文面はまだ未作成

### PetArmor「Protect Playtime」タイムライン
| 日付 | イベント |
|---|---|
| 01/13/26 | Best Friends Adoption APIオンボード（WW BIL WBR p.5） |
| 01/20/26 | ASR完了 + FASTオンボード、Orange self-certify（WW BIL WBR p.4） |
| 01/28-29/26 | TEX NA WBR p.6 / WW TEX WBR p.13 に記載（Alec名義） |
| 02/02/26 | Phase 1 ローンチ（Slack #launch-party, eddiecam） |
| 04/06/26 | Phase 2 AI機能追加予定 |

### PetArmor AI アーキテクチャ（コード解析完了）

#### リポジトリ構成
| リポ | 内容 | Bindle |
|---|---|---|
| BIL-TEX-PetArmor-ProtectPlaytime-BrandStore | Phase 1 フロントエンド（AI なし） | BIL-NA-Endemic-Campaigns |
| BIL-TEX-PetArmor-ProtectPlaytime-CDK | Phase 1 S3+CloudFront | 同上 |
| BestFriendsAnimalSocietyAdoptionServiceCDK | AI バックエンド CDK | **専用 Bindle** |
| BestFriendsAnimalSocietyAdoptionServicePlayground | AI デモ UI（Harmony） | 同上 |
| BestFriendsAnimalSocietyAdoptionServiceTests | FAST テスト | 同上 |
| Version Set | `BIL-TEX-PetArmor-ProtectPlaytime/development` | |

#### Bindle
- **名前:** `BestFriendsAnimalSocietyAdoptionService`
- **Owner:** fitzmaro
- **Team:** Brand Innovation Lab NA - Campaign Development
- **CTI:** Advertising > Brand Lab > WW TEX

#### AWS Accounts
- Non-prod: `130413243566`
- Prod: `898310714909`

#### AI スタック
- **Model:** Claude Sonnet 4.5 (Prod) / Haiku 4.5 (Non-prod) on Bedrock
- **SDK:** Vercel AI SDK (`ai` + `@ai-sdk/amazon-bedrock`)
- **Tool Use:** `toolChoice: 'required'`, `maxSteps: 5`, `queryAnimals` ツールのみ
- **ガードレール 11層:** Tool-only / ステップ制限 / 入力長制限 / AI分類(4カテゴリ) / fail-closed / Zod enum / 結果5件上限 / フォールバック / 非同期 / カスタムエラー / 監査ログ
- **PII フィルタリング:** 未実装（AI分類に PII カテゴリなし）
- **Bedrock Guardrails:** 未使用（全てカスタム実装）

#### FAST 統合
- Gamma ステージで `FASTIntegration Tests` 実行
- Hydra (Fargate) 上で FAST Python client が RecommendProcessorLambda を直接 invoke
- 閾値: output_validity 0.6 / pii 0.6 / deflection 0.6
- AAA relationships: GenAISecurityPromptsService + GenAISecurityScoringService + CloudAuthServer

#### Design Inspector
- `BestFriendsAnimalSocietyAdoptionServiceBackend` — 2フロー定義
- EventBridge Sync Flow: 外部API → DynamoDB 定期同期
- Lambda Query Data Flow: User → BGW → QueryAnimals / GetPromptPresets / RecommendPets / Filters

#### Harmony
- Beta: `https://bestfriendsanimalsocietyadoptionserviceplayground.beta.harmony.a2z.com/`
- Prod: `https://console.harmony.a2z.com/bestfriendsanimalsocietyadoptionserviceplayground/`
- BuilderHub Create: `https://create.hub.amazon.dev/cloned-applications/BestFriendsAnimalSocietyAdoptionService`

#### データ取り扱いリスク
| Issue | Severity |
|---|---|
| CloudWatch Logs にプロンプト全文記録（14日保持） | HIGH |
| PII フィルタリング未実装（入力側） | HIGH |
| UI に PII disclaimer なし | HIGH |
| RecommendJobs TTL有効化が外部依存 | MEDIUM |

### WBR/QBR 調査（完了）
- **WW TEX WBR p.13（01/29週）** — FAST/ASR/Orange の主要情報源
- **WW BIL WBR p.4-5（01/13, 01/20週）** — 同内容 + Best Friends API詳細
- **TEX NA WBR p.6（01/28週）** — 同内容
- **Q4 QBR p.8** — PetArmor Pet Finder が Paused で記載
- **2025 Quip WBR** — FAST/Orange 該当なし。GenAI ASR 30日SLAの旧ルール記載あり
- **ARC/PARC** — PetArmor 未登録

### Bindle ルール（Alec, #bil-ww-tex-dt）
- リージョン別 Holding Bindle に統合（例: `BIL-NA-Endemic-Campaigns`）
- **例外:** バックエンド + InfoSec レビュー必要 → 専用 Bindle
- プロトタイプ → `BIL-TEX-PrototypesDiscoveryTesting`
- 全リスト: https://quip-amazon.com/jn9bAOS0qo9t/BIL-TEX-Updated-Team-And-Bindle-List

### 担当者
- **Alec Kunkle**（`aleckunk`）— DT, TEX US。PetArmor AI担当、FAST onboard実施者
- **fitzmaro** — BestFriendsAnimalSocietyAdoptionService Bindle owner
- **yuvikoul** — Design Inspector 最終更新者
- **@monatang** — FAST Integration SOP を `#bil-ww-tex-dt` で共有（2026/1/7）

## 成果物一覧

```
2026-03-11_uk-arla-ai-on-clp/
├── handover.md
├── artifacts/
└── notes/
    ├── research-summary-ja.md              — リサーチ結果の包括的サマリー（日本語）
    ├── julia-reply-draft-points-ja.md      — Julia返信ドラフト回答ポイント対照表
    ├── mars-fywdttyd-quip-summary.md       — MARS FYWDTTYD Quip読み込みサマリー
    ├── bestfriends-ai-analysis-ja.md       — AI実装分析（日本語）
    ├── bestfriends-data-handling-analysis.md — データ取り扱い/PII分析
    ├── fast-prompt-test-analysis.md         — FAST Prompt Test Analysis（英語）
    ├── fast-prompt-test-analysis-ja.md      — FASTコード調査（日本語）
    ├── petarmor-cdk-investigation-ja.md     — CDK FAST/ASR調査（日本語）
    └── ucd-pii-asr-investigation.md        — UCD/PIIポリシー調査
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|---|---|---|
| 1 | - | Julia への返信メール文面作成 | 未着手 |
| 2 | - | Lukeと返信内容すり合わせ | 未着手 |
| 3 | - | Alec (aleckunk) に確認: 本番Phase 2はプリセットのみ or フリーフォームも含むか | 未着手 |
| 4 | - | FAST SOP Quip 読み込み・UK適用可否確認（任意） | 未着手 |

## 重要な判断ログ

- 「Pet Amor」はユーザーの記憶違いで、正式名称は **PetArmor「Protect Playtime」** だった
- WBR原文の発見により、FAST/ASR Orange self-certify の情報は公式ソース（WBR 3本で裏取り済み）
- PetArmor Phase 2（AI）は 4/6/26 ローンチ予定のため、本番稼働の実績データはまだない
- **UCD/PII分類の重要発見:** フリーフォーム入力 = UCD = Critical = Red。Allow-list のみなら Orange 維持可能
- PetArmor のPII保護にギャップあり（CloudWatch Logsに全文記録、PII検出未実装、UI disclaimer なし）
- Arla のジングル生成でも Tool Use パターンは適用可能（generateJingle ツールに構造化パラメータ）
- Julia のDTチームの「事前定義プロンプトが必要かも」は、ASR分類をOrangeに保つための戦略的選択として正当化できる
- MARS FYWDTTYD: フリーフォーム入力を許可したが出力をYES/NO/BLOCKEDに制約。それでもRed ASR（90h DT作業）
- MARS FYWDTTYD: クライアントGenAI承認が3ヶ月超かかった（想定外）。早期開始が必須
- MARS FYWDTTYD: Andon Cord（即時停止機構）はSOPとデモ録画まで求められた
- 返信方針: テック面のみ、2026年更新は軽く触れAlec (aleckunk@) への連絡をサジェスト

## 主要リソース一覧

| リソース | URL |
|---|---|
| ASR Profiles（分類ルール） | https://w.amazon.com/bin/view/Infosec/Proactive_Security/Dev/SecurityReviewTooling/ASR/Profiles/ |
| FAST Wiki | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/ |
| FAST Integration SOP | https://quip-amazon.com/FhvFAKBxf6Tu/SOP-FAST-Integration |
| Generative AI for Campaign（Shugo作成） | https://quip-amazon.com/aa1OAHdOJgua/Generative-AI-for-Campaign |
| MARS FYWDTTYD Quip フォルダ | https://quip-amazon.com/Tnk0OtquZA7d/AU-Mars-FYWDTTYD- |
| BIL 承認済み AI ツールリスト | https://w.amazon.com/bin/view/BIL-E/NA/BIL-AI-Tools |
| GenAI ASR プロファイル要否判定 | https://w.amazon.com/bin/view/InfoSec/Application_Security/AppSTAR/Appsec_AI/When_is_a_GenAI_ASR_Profile_required_/ |
| BIL-TEX Bindle リスト | https://quip-amazon.com/jn9bAOS0qo9t/BIL-TEX-Updated-Team-And-Bindle-List |
| PetArmor AI Bindle | https://bindles.amazon.com/software_app/BestFriendsAnimalSocietyAdoptionService |
| Design Inspector | https://design-inspector.a2z.com/#IBestFriendsAnimalSocietyAdoptionServiceBackend |
| Harmony Playground (Beta) | https://bestfriendsanimalsocietyadoptionserviceplayground.beta.harmony.a2z.com/ |
| BuilderHub Create | https://create.hub.amazon.dev/cloned-applications/BestFriendsAnimalSocietyAdoptionService |

## 関連トピック

- `2026-02-26_cat-decoder-tech-case-study` — MARS Dine MindReader / Cat Decoder（同じくAI on CLPの事例）
