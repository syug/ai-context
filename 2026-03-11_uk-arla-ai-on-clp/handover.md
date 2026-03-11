# Handover Document
**Topic:** UK Arla Campaign — AI on CLP 承認プロセス調査・返信準備
**Date:** 2026-03-11
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

### PetArmor「Protect Playtime」タイムライン
| 日付 | イベント |
|---|---|
| 01/13/26 | Best Friends Adoption APIオンボード（WW BIL WBR p.5） |
| 01/20/26 | ASR完了 + FASTオンボード、Orange self-certify（WW BIL WBR p.4） |
| 01/28-29/26 | TEX NA WBR p.6 / WW TEX WBR p.13 に記載（Alec名義） |
| 02/02/26 | Phase 1 ローンチ（Slack #launch-party, eddiecam） |
| 04/06/26 | Phase 2 AI機能追加予定 |

### WBR/QBR 調査（完了）
- **WW TEX WBR p.13（01/29週）** — FAST/ASR/Orange の主要情報源
- **WW BIL WBR p.4-5（01/13, 01/20週）** — 同内容 + Best Friends API詳細
- **TEX NA WBR p.6（01/28週）** — 同内容
- **Q4 QBR p.8** — PetArmor Pet Finder が Paused で記載
- **2025 Quip WBR** — FAST/Orange 該当なし。GenAI ASR 30日SLAの旧ルール記載あり
- **ARC/PARC** — PetArmor 未登録

### 担当者
- **Alec Kunkle**（`aleckunk`）— DT, TEX US。PetArmor AI担当、FAST onboard実施者
- **@monatang** — FAST Integration SOP を `#bil-ww-tex-dt` で共有（2026/1/7）

## 成果物一覧

```
2026-03-11_uk-arla-ai-on-clp/
├── handover.md
├── artifacts/
└── notes/
    └── research-summary.md    — リサーチ結果の包括的サマリー
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|---|---|---|
| 1 | - | Julia への返信ドラフト作成（MARS経験 + 最新FAST/Orange情報） | 未着手 |
| 2 | - | Lukeと返信内容すり合わせ | 未着手 |
| 3 | - | Alec (aleckunk) に PetArmor Phase 2 AI実装の詳細確認（任意） | 未着手 |
| 4 | - | FAST SOP Quip 読み込み・UK適用可否確認（任意） | 未着手 |

## 重要な判断ログ

- 「Pet Amor」はユーザーの記憶違いで、正式名称は **PetArmor「Protect Playtime」** だった
- WBR原文の発見により、FAST/ASR Orange self-certify の情報は公式ソース（WBR 3本で裏取り済み）として Julia に共有可能
- PetArmor Phase 2（AI）は 4/6/26 ローンチ予定のため、まだ本番稼働の実績データはない
- Arla のユースケース（AIジングル生成）は PetArmor（AI pet recommendations）と異なるが、承認プロセス（ASR/FAST）は共通

## 関連トピック

- `2026-02-26_cat-decoder-tech-case-study` — MARS Dine MindReader / Cat Decoder（同じくAI on CLPの事例）
