# Handover Document
**Topic:** UK Arla Campaign — AI on CLP 承認プロセス調査・返信完了
**Date:** 2026-03-13
**Status:** 進行中（Luke返信待ち）

---

## 背景

Julia Sampaio（UK BIL Solutions Manager）から Luke & Shugo 宛に、Arla（乳製品ブランド、UK市場）のCLPキャンペーンでAIジングル生成を組み込みたいという相談メール（2026/3/11）。コンセプト「Morning Wins Worth Celebrating」。MARS「For You Who Did That Thing You Did」キャンペーンでのAI on CLP経験について7項目の質問。

ユーザーの指示: MARSは2024年実施なので思い出す必要あり。加えて、2025-2026年の承認プロセス更新（PetArmor/FAST/ASR Orange分類）を調査。

## 現在の状況

### Lukeへの返信メール送信済み（2026/3/13 13:09 AEDT）
- Outlookからメール送信完了。Lukeが内容を確認し、Julia に転送する流れ
- Subject: "RE: UK Arla Campaign — AI on CLP: Learning from your MARS experience"

### 返信ドラフト作成プロセス

#### 調査フェーズ（完了）
- Julia のメール全文取得・日本語訳・7つの質問サマライズ
- 承認プロセス調査: Before（2024 MARS Red）→ After（2026 Orange/FAST）
- UCD/PII分類調査: フリーフォーム=UCD=Critical=Red、Allow-listのみならOrange
- MARS FYWDTTYD Quip全ドキュメント読み込み
- PetArmor「Protect Playtime」AIアーキテクチャのコード解析
- WBR/QBR調査（WBR 3本で裏取り済み）

#### MARS FYWDTTYDコード解析（完了）
- **リポジトリ:** `APAC-BIL-Campaign-Mars-FYWDTTYD-ServiceCDK`（CDK）+ `APAC-BIL-Campaign-Stores-Mars-FYWDTTYD-2024`（フロントエンド）
- **ASR実データ:** Application `APAC-BIL-Campaign-Mars-FYWDTTYD-1710164373`、Owner: saitshug、ASR作成 3/11/2024、GenAI AppSec関与 ~7/19/2024、リリース 8/29/2024（ASRレビュー実期間 約6週間）
- **AWS Account:** `637423629615`（us-west-2）
- **ガードレール:** 6層（フロントエンド100文字制限 / WAF 6ルール / API Gateway / validateInputText 5段パイプライン / Bedrock Guardrails 4フィルタ / validateAnswer YES/NO/BLOCKED制約）
- **Bedrock Guardrails:** Content Filters全6カテゴリHIGH（PROMPT_ATTACK含む）、Denied Topics 28個、Word Filters 1,494語、PII Filters全カテゴリBLOCK
- **CloudWatchアラーム:** セキュリティ4（CloudTrailベース）+ API Gateway 2（エラー率>3%、p90レイテンシ>15s）+ DynamoDB AutoScaling 8
- **ダッシュボード:** ServiceHealthMonitoring（Bedrock/API GW/Lambda/WAF/Input Texts）
- **AI応答専用アラームは未設定。** 事後モニタリングはDynamoDB全ログ + 手動バッチレビュー

#### Q4補足: フリーフォーム vs プリセットの議論（ユーザー提供）
- プリセット制限はPlan Bとして検討された
- しかしクライアント要件を満たせず、クリエイティブとして弱い
- プリセットのみならLLM自体が不要（技術的にオーバーキル）
- プロトタイプを開発しフィージビリティ確認の上、フリーテキスト+多層ガードレールを選択

#### ドラフト作成フェーズ（完了）
- 回答ポイント対照表 → フルドラフト → 簡潔版 → ユーザー手動編集による最終版（reply-draft-base）の流れ
- 全Qに「ストレート回答 → 詳細」の構成を適用
- ASR実タイムライン（3/11作成 → 7/19 AppSec関与 → 8/29リリース）を反映
- 最終版をOutlookドラフト作成 → Lukeに送信

### 主要な技術知見

#### ASR Orange分類の条件
- **Orange:** GenAI使用だが Critical/Restricted データ非該当、UCD非該当、HR PII非該当
- **Red:** フリーフォーム入力(=UCD=Critical)、HR PII、business critical のいずれかに該当
- **唯一の回避策:** Allow-list（事前定義プロンプト）のみ → UCD非該当 → Orange → self-certify
- UIラベル/disclaimer/PIIフィルタリング/データ非保存 — いずれも分類は下げられない

#### MARS FYWDTTYD 技術スタック
- Claude 3 Sonnet on Bedrock / RAG(Knowledge Bases + OpenSearch) / temp=0.0
- 入力: フリーフォーム100文字 / 出力: YES/NO/BLOCKED のみ
- Andon Cord: Lambda環境変数 `USE_BEDROCK_API=false` で即時AI無効化

#### PetArmor AI（参考）
- Claude Sonnet 4.5 (Prod) / Vercel AI SDK / Tool Use パターン
- Orange self-certify取得（2026/1/20）— ただし実装上フリーフォーム入力あり（ギャップの可能性）

### 担当者
- **Julia Sampaio** — UK BIL Solutions Manager。Arlaキャンペーン担当
- **Luke Thistleton** (`lukthis`) — AU BIL SM。Julia のメールのcc、返信の最終送信者
- **Alec Kunkle** (`aleckunk`) — NA DT。PetArmor AI担当、FAST onboard実施者。最新プロセスに詳しい
- **fitzmaro** — BestFriendsAnimalSocietyAdoptionService Bindle owner
- **@monatang** — FAST Integration SOP を共有（2026/1/7）

## 成果物一覧

```
2026-03-11_uk-arla-ai-on-clp/
├── handover.md
├── artifacts/
│   ├── julia-reply-draft-en.md              — フルバージョン英語（リファレンス）
│   ├── julia-reply-draft-ja.md              — フルバージョン日本語（リファレンス）
│   ├── julia-reply-email-en.md              — 簡潔版英語
│   └── julia-reply-email-ja.md              — 簡潔版日本語
└── notes/
    ├── reply-draft-base-ja.md               — 最終版日本語（ユーザー手動編集）★送信版のベース
    ├── reply-draft-base-en.md               — 最終版英語（base-jaから翻訳）★Lukeに送信済み
    ├── julia-reply-draft-points-ja.md       — 回答ポイント対照表（全Q詳細）
    ├── research-summary-ja.md               — リサーチ結果の包括的サマリー
    ├── mars-fywdttyd-quip-summary.md        — MARS FYWDTTYD Quip読み込みサマリー
    ├── mars-fywdttyd-input-handling-code-analysis-ja.md — MARSコード解析（入力管理）
    ├── bestfriends-ai-analysis-ja.md        — PetArmor AI実装分析
    ├── bestfriends-data-handling-analysis.md — PetArmorデータ取り扱い/PII分析
    ├── fast-prompt-test-analysis.md          — FAST Prompt Test Analysis（英語）
    ├── fast-prompt-test-analysis-ja.md       — FASTコード調査（日本語）
    ├── petarmor-cdk-investigation-ja.md      — PetArmor CDK FAST/ASR調査
    └── ucd-pii-asr-investigation.md         — UCD/PIIポリシー調査
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|---|---|---|
| 1 | - | Julia への返信メール文面作成 | 完了（3/13送信） |
| 2 | - | Lukeに返信内容送信 | 完了（3/13 13:09 AEDT） |
| 3 | - | Lukeの確認・Julia への転送待ち | 待ち |
| 4 | - | Alec (aleckunk) に確認: 本番Phase 2はプリセットのみ or フリーフォームも含むか | 未着手（任意） |
| 5 | - | FAST SOP Quip 読み込み・UK適用可否確認 | 未着手（任意） |

## 重要な判断ログ

- 「Pet Amor」はユーザーの記憶違いで、正式名称は **PetArmor「Protect Playtime」** だった
- WBR原文の発見により、FAST/ASR Orange self-certify の情報は公式ソース（WBR 3本で裏取り済み）
- PetArmor Phase 2（AI）は 4/6/26 ローンチ予定のため、本番稼働の実績データはまだない
- **UCD/PII分類の重要発見:** フリーフォーム入力 = UCD = Critical = Red。Allow-list のみなら Orange 維持可能
- PetArmor のPII保護にギャップあり（CloudWatch Logsに全文記録、PII検出未実装、UI disclaimer なし）
- Julia のDTチームの「事前定義プロンプトが必要かも」は、ASR分類をOrangeに保つための戦略的選択として正当化できる
- MARS FYWDTTYD: フリーフォーム入力を許可したが出力をYES/NO/BLOCKEDに制約。それでもRed ASR（90h DT作業）
- MARS FYWDTTYD: クライアントGenAI承認が3ヶ月超かかった（Quipで確認: 4/8-19予定→7/14完了）。早期開始が必須
- MARS FYWDTTYD: Andon Cord（即時停止機構）はSOPとデモ録画まで求められた
- MARS ASR実タイムライン: ASR作成3/11 → AppSec関与7/19 → リリース8/29 = 約6週間（ギリギリ）。推奨2-3ヶ月
- 返信方針: テック面のみ、2026年更新は軽く触れAlec (aleckunk@) への連絡をサジェスト
- MARS Plan B議論: プリセットのみではクライアント要件不足+LLM不要になる → フリーテキスト+多層ガードレールを選択
- 承認上の技術要件「キャンペーン/モデルごとの個別承認」「全プロンプト/レスポンスのログ保存」はユーザーの記憶+コード実装から（明示的ポリシー文言の確認なし）
- CloudWatchアラーム: AI応答専用アラームは未設定。APIレベル（エラー率/レイテンシ）+ セキュリティ監視のみ。AI応答の事後監視はDynamoDB全ログ+手動レビュー
- ドラフト作成プロセス: フル版→簡潔版→ユーザー手動編集→最終版(reply-draft-base)の4段階。ユーザーが最終調整して送信可能レベルに

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
| MARS ASR Application | ASR App ID: d1f8d647-c905-48af-be66-d96231698216 |
| MARS AWS Account | 637423629615 (us-west-2) |

## 関連トピック

- `2026-02-26_cat-decoder-tech-case-study` — MARS Dine MindReader / Cat Decoder（同じくAI on CLPの事例）
