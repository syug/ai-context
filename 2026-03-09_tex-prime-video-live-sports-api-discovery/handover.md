# Handover Document
**Topic:** PV Live Sports API Discovery -- BGW統合・商用ライセンス・リーガル準備
**Date:** 2026-03-11
**Status:** 進行中

---

## 背景

Prime Video Live Sports API（SDP: Sports Data Platform）をBrand Gateway経由でBIL Podsが利用可能にするDiscoveryプロジェクト。元々は `tex-prime-video-sse-initiative` の一部として管理していたが、SSEとは独立したイニシアチブのため 3/9 にspin off。

元々2025/12にGillette案件でAPI調査を開始 → Gillette失注で中断 → Mirkoが「案件に関係なくDiscoveryを続けたい」 → Binduが「BIL-Eは1案件だけでは動かない。複数Pod横断の例が必要」 → 2026/01 Binduとフォローアップ → 3/3 Mirkoがグローバルでビジネスインパクト収集開始 → 3/7 Jonathan Yi（PV BD）よりライセンスがeditorial onlyと判明。

## 現在の状況

### ライセンス問題（最重要）

3/6にBinduがSDP Core SDM (Anand Kumaravel) にメールで確認 → AnandがJonathan Yi（Sr. BD Manager, WW BD | Prime Video）をループイン → Jonathan Yiの回答（3/7）:

- SDPデータライセンスは現在 **PV専用・editorial use** に標準化
- **商用（commercial）利用には未対応**
- 商用利用は one-size-fits-all ではなく、データプロバイダーがuse case / reach / data scopeの3軸で個別に課金を算出
- コールを提案

**2レイヤー問題:**

| レイヤー | 管轄 | 担当者 | 状態 |
|---------|------|--------|------|
| 技術アクセス | SDP Core | Anand Kumaravel (SDM) | 全広告主OK |
| 商用ライセンス | PV BD | Jonathan Yi (Sr. BD Mgr) | editorial only、commercial は個別交渉 |

**saitshug方針: Chicken-and-Egg回避**
- 技術実装（PoC）を先行し、商用ライセンスはキャンペーン単位で対応
- PoC/デモは editorial/internal use の範囲で進める
- 動くものがないとプロバイダーとのライセンス交渉も進まない

### Mirkoの要求（3/10 Slackメッセージ）

Mirkoが #tex-discovery-pv-live-sports-api-enablement で3点を要求:
1. ライセンス申請の**プロセス**を明確にする
2. **POCs**（担当窓口）を特定する
3. **ETA**（タイムライン）の把握が必須

→ Bindu sync のアジェンダに反映済み

### Bindu sync（本日 3/11）

- **日時:** 水 3/11 19:00-19:30 AEDT (8:00-8:30 GMT)
- **Outlook招待送信済み**
- **Slackメッセージ送信済み** (#tex-discovery-pv-live-sports-api-enablement, 3/9)
- **アジェンダメモ作成済み**: `artifacts/bindu-sync-agenda-20260311.md`
- 初回syncのみ同期、以降は基本Slack非同期

アジェンダ:
1. Jonathan Yiコール段取り (10min) — 誰が設定/TZ/質問リスト（プロセス・POCs・ETA）
2. BIL-E Intake Request (8min) — タイミング判断、ビジネスケース強度
3. 技術PoC方針 (5min) — Chicken-and-Egg回避、editorial use範囲

### ビジネスインパクト収集（Mirko主導）

| Pod | 見積もり | ステータス |
|-----|---------|-----------|
| EU Endemics | $3MM/yr（P&G Champions League $1MM, Adidas $2MM） | Mirko記載済み |
| AU | 400k USD（NBA中心、クリケットは2026年なし） | Chris Wilson回答済み |
| US | 金額なし、PoC実行中（NHL Shots on Net → フードデリバリー割引） | Fitz/Kevin回答済み |
| JP | 未回答（Mariko: ポジティブだが「Sales Struggle + ライセンシー問題で壁が高い」） | **期限超過** |
| MENA | ポテンシャルありだが数字なし | Chris Wilson言及のみ |

### Discovery Doc (Quip) 状態

- **URL:** https://quip-amazon.com/c4cBAcoeV61e/Discovery-Prime-video-Live-sports-API
- **3/11確認:** 3/9以降の新規Biz updateなし。Business justificationは上記テーブルと同一。Next Stepsテーブルはステータス未記入。
- **要更新:** Jonathan Yiのライセンス問題が未反映 → Bindu sync後に更新予定

### Strategy v2 ドキュメント作成済み

3層ゴール（Tech / Commercial Licensing / Legal & Ad Policy）、アプローチ(A)(B)、Next Stepsを定義。Bindu syncで議論予定。

## 成果物一覧

```
2026-03-09_tex-prime-video-live-sports-api-discovery/
├── handover.md
├── artifacts/
│   ├── pv-live-sports-api-strategy-v2.md
│   └── bindu-sync-agenda-20260311.md        ← NEW
├── notes/
│   ├── pv-live-sports-api-research.md
│   ├── sdp-licensing-issue-analysis.md
│   └── strategy-review-20260309.md
└── history/
    └── 2026-03-09_handover.md               ← ARCHIVED
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | **3/11 19:00** | **Bindu sync コール** -- アジェンダ準備完了 | 本日実施予定 |
| 2 | **3/11後** | **Jonathan Yiコール段取り** -- Bindu + Jonathan Yiで実施。Mirko要求3点（プロセス・POCs・ETA）を確認 | Bindu sync後 |
| 3 | **TBD** | **SDP Coreに問い合わせ** -- 技術的ブロッカー、データ/プロバイダーマッピング取得 | 未着手 |
| 4 | **TBD** | **BIL-E Intake Request 準備・提出** -- ビジネスケース + Bindu syncの方針 | Bindu sync後 |
| 5 | **TBD** | **Mirkoにライセンス問題エスカレーション** | Jonathan Yiコール後 |
| 6 | **TBD** | **マッピングテーブル作成** -- データ x プロバイダー x 商用利用条件 x リーガル/ポリシー | PV BD確認後 |
| 7 | **TBD** | **Discovery Doc (Quip) 更新** -- ライセンス問題反映 | Bindu sync後 |
| 8 | **EOW過ぎ** | Mirkoメール返信: APAC/MENAビジネスインパクト見積もり | Mariko JP見積もり待ち |
| 9 | **TBD** | BIL Legal / Ad Policy チェック | ユースケース定義後 |

## 重要な判断ログ

- **Chicken-and-Egg回避方針**: 技術実装（PoC）を先行し、商用ライセンスはキャンペーン単位で対応。PoC/デモはeditorial/internal useの範囲、実広告主利用時に初めてライセンス交渉
- **2レイヤー問題**: 技術アクセス（SDP Core）とライセンス（PV BD）は別管轄・別組織。Anandの「全広告主OK」は技術アクセスの話。Jonathan Yi（BD）がライセンス面でeditorial only制約を指摘
- **タイムゾーン制約と会議方針**: Binduとの初回syncのみ同期（AEDT 19-21時 = GMT 08-10時）、以降は基本非同期。Jonathan Yiとの直接コールは非現実的（Sydney-Arlington 15時間差）。Bindu+Jonathan Yiコール → saitshugはメールCC+非同期
- **Live Sports API経緯**: Gillette案件で開始→失注で中断→Mirkoがキャンペーン関係なく続行指示→BIL-Eは複数Pod横断の正当化が必要→Mirkoがグローバルでインパクト収集中（3/4メール）
- **RACI**: A=Mirko、R=Shugo+Bindu、C=Pod leads・BIL-E・SDP Core・PV BD、I=グローバルステークホルダー
- **BIL-E動機付け**: Harish(BIL-E)は1案件だけでは不満。複数Pod横断キャンペーン例が必要
- **正しいフロー**: Business justification 収集 → Bindu sync → BIL-E Intake Request → BIL-E が SDP オンボーディング + BGW インテグレーション実行
- **Mariko JP 壁**: Sales Struggle + ライセンシー問題（Layer 2 + Layer 3 にまたがる可能性）
- **3/9 spin off**: tex-prime-video-sse-initiative から独立トピックとして分離
- **Discovery Doc Quip URL**: `c4cBAcoeV61e` — 3/11時点でライセンス問題未反映、Bindu sync後に更新予定

## 関連トピック

- [tex-prime-video-sse-initiative](../2026-02-26_tex-prime-video-sse-initiative/) -- SSE Initiative（元トピック。Sean Dylkeミーティング、Curated Collection Pages等）
- [au-bil-pv-growth-engagement](../2026-03-04_au-bil-pv-growth-engagement/) -- AU BIL x PV Growth連携
- [api-landscape-research](../2026-03-06_api-landscape-research/) -- Public API Landscape リサーチ（SDP含む）
- [sse-prototypes](../2026-02-23_sse-prototypes/) -- SSEプロトタイプ
