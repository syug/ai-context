# UK Arla Campaign — AI on CLP リサーチまとめ

## 1. 背景

Julia Sampaio（UK BIL Solutions Manager）から Luke & Shugo 宛に、**Arla「Morning Wins Worth Celebrating」キャンペーン**（UK市場、CLP上でAIジングル生成）について、MARS キャンペーンでの AI on CLP 経験を教えてほしいというリクエスト（2026/3/11）。

### Julia の質問（7項目）
1. AI承認プロセスの全体像と関与チーム
2. 承認のタイムライン（所要期間・段階数）
3. ユーザー入力のガードレール・フィルター・モデレーション
4. 自由入力 vs 事前定義プロンプトの判断基準
5. 使用AIモデル・インフラ（Amazon内ホストか）
6. 参考になる社内ドキュメント・承認テンプレート
7. 教訓・落とし穴

---

## 2. 2024 MARS キャンペーン時代の状況（Before）

| 項目 | 内容 |
|---|---|
| ASR分類 | GenAI = **Red**（当時はGenAI使用で自動的にRedになるケースが多かった） |
| レビュー | InfoSec チームによる**手動レビュー必須**、SLA **30日以上** |
| Legal | 事前承認モデルは不可。全AI生成物にLegal承認が必要 |
| EU制約 | Legalが四半期に**1キャンペーンしかサポートできない** |
| 教訓 | Greenies Pet Interpreter（2024/5）で Legal への GenAI 使用報告漏れが発生 → SM が早期報告するプロセスを確立 |
| Anthropic連携 | 2024/6に TEX が Anthropic と直接ミーティング。Legal承認の課題と構造化出力の必要性を共有 |

**ソース:** NA WBR 05/01/24, 06/12/24, 02/21/24

---

## 3. 2026 最新状況（After）

### 3.1 ASR GenAI 分類ルール（現行）

| 分類 | 条件 | レビュー方法 |
|---|---|---|
| **Red** | GenAI + (HR PII / Restricted/Critical データ **OR** business critical に接続) | セキュリティレビュワー必須 + **手動プロンプトテスト必須** |
| **Orange** | GenAI を使用（ただし Red 条件に該当しない） | **自己認証（self-certify）可能** + FAST 自動テストでOK |

**ポイント:** ユーザーデータの収集・保存やモデルトレーニングを行わず、ビジネスクリティカルでもない AI アプリ → **Orange** → InfoSec 手動レビュー不要。

**ソース:** ASR Profiles Wiki (https://w.amazon.com/bin/view/Infosec/Proactive_Security/Dev/SecurityReviewTooling/ASR/Profiles/)

### 3.2 FAST（Framework for AI Security Testing）

| 項目 | 内容 |
|---|---|
| 概要 | GenAI アプリの自動プロンプトセキュリティテストフレームワーク（V2が現行） |
| テスト対象 | PII漏洩、リモートコード実行、プロンプトインジェクション等 |
| 統合方法 | CI/CD パイプラインに Hydra テスト経由で統合 |
| Orange アプリ | FAST 自動テストで要件クリア可能 |
| Red アプリ | 手動プロンプトテストが**必須**（FASTだけでは不可） |
| 必須化 | 2025年以降、全GenAIエクスペリエンスに FAST 統合が必須 |

**ソース:** FAST Wiki (https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/), FAST SOP Quip (https://quip-amazon.com/FhvFAKBxf6Tu/SOP-FAST-Integration)

### 3.3 GenAI ASR タスク一覧（Orange の場合）

Baseline タスク + 以下の GenAI 固有タスク:
- Review Training Data / Monitoring
- Review Model
- Data Leak Check
- Prompt Data Sanitization
- Review Responses Untrusted Data
- Review Transitive Auth
- Prompt Response Logging
- Validate Guardrails
- Validate Siloed Sessions

---

## 4. PetArmor「Protect Playtime」— 最新の AI on CLP 事例

### 4.1 キャンペーン概要

| 項目 | 内容 |
|---|---|
| クライアント | PetArmor（PetIQ社）|
| マーケット | US Grocery |
| 予算 | $2M |
| 媒体 | Custom Brand Store, Display, Pause Ads |
| Phase 1 | 2/2/26 - 4/5/26（クイズ + ブランドストア、AI なし） |
| Phase 2 | 4/6/26〜（**AI-powered adoption tools** = AI ペット推薦） |
| 担当DT | **Alec Kunkle**（`aleckunk`）, Design Technologist, TEX US |

### 4.2 AI 開発タイムライン

| 日付 | ソース | 内容 |
|---|---|---|
| 01/13/26 | WW BIL WBR p.5 | **Best Friends Adoption API** オンボード完了。譲渡可能ペットリストを表示。次ステップ: Legal/InfoSec と AI 自然言語検索追加 |
| 01/20/26 | WW BIL WBR p.4 | **ASR 完了 + FAST オンボード完了**。Orange self-certify でリリース可能に |
| 01/28/26 | TEX NA WBR p.6 | 同内容記載 |
| 01/29/26 | WW TEX WBR p.13 | 同内容記載（Alec 名義） |
| 02/02/26 | Slack #launch-party | Phase 1 ローンチ |
| Q4 QBR | QBR p.8 | 「PetArmor Pet Finder」が Integrations パイプラインに Paused で記載 |

### 4.3 WBR 原文（WW TEX WBR p.13, 01/29 週）

> **[Alec] BIL TEX Onboarded to FAST for AI Pet Recommendations**
>
> In preparation for the Pet Armor campaign, BIL TEX successfully completed the Amazon Security Review (ASR) and onboarded to the Framework for AI Security Testing (FAST) to serve AI-recommended pets for adoption based on a user's prompt.
>
> Note: All applications that do not handle user data or training can now be self-certified as "orange." Reducing the need to work with the InfoSec team to manually review all AI applications.

---

## 5. 他の GenAI BIL キャンペーン事例

| キャンペーン | マーケット | 時期 | AI内容 |
|---|---|---|---|
| Greenies Pet Interpreter | US | 2024/5 | Claude v3 でペットレビューをリフレーズ |
| T-fal "Cooking in a New Light" | CA | 2025/11 | Bedrock + Knowledge Base Agent で AI レシピ生成。BIL Canada 初の GenAI キャンペーン |
| Hellmann's "Mayo For A Melody" | US | 2026/2 | Super Bowl LX、GenAI カラオケ体験、$1.1M |

---

## 6. 主要リソース一覧

| リソース | URL |
|---|---|
| ASR Profiles（分類ルール） | https://w.amazon.com/bin/view/Infosec/Proactive_Security/Dev/SecurityReviewTooling/ASR/Profiles/ |
| FAST Wiki | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/ |
| FAST Integration SOP | https://quip-amazon.com/FhvFAKBxf6Tu/SOP-FAST-Integration |
| Generative AI for Campaign（Shugo作成） | https://quip-amazon.com/aa1OAHdOJgua/Generative-AI-for-Campaign |
| BIL 承認済み AI ツールリスト | https://w.amazon.com/bin/view/BIL-E/NA/BIL-AI-Tools |
| GenAI ASR プロファイル要否判定 | https://w.amazon.com/bin/view/InfoSec/Application_Security/AppSTAR/Appsec_AI/When_is_a_GenAI_ASR_Profile_required_/ |
| 手動プロンプトテストガイダンス | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Guidance/Prompt_Testing/ |
| Generative AI Security Standard | https://policy.a2z.com/docs/613805/publication |
| Misclassified GenAI App（Shepherd） | https://w.amazon.com/bin/view/InfoSec/Application_Security/AppSTAR/Appsec_AI/Misclassified_GenAI/ |
| ASR ツール | https://asr.security.amazon.dev/ |

---

## 7. Julia への回答キーメッセージ

> 2024 MARS キャンペーン以降、承認プロセスは大幅に改善された。BIL TEX が FAST フレームワークにオンボードし、PetArmor キャンペーン（2026 US）で text-to-text AI を組み込んだ実績がある。ユーザーデータやモデルトレーニングに関わらない AI アプリは ASR で **Orange 分類**となり、**自己認証で承認が完了**できるようになった。MARS 時代（Red → レビュワー必須 → 30日+ SLA）からの大きな改善。
