# Handover Document
**Topic:** PV Live Sports API Discovery -- BGW統合・商用ライセンス・リーガル準備
**Date:** 2026-03-11
**Status:** 進行中

---

## 背景

Prime Video Live Sports API（SDP: Sports Data Platform）をBrand Gateway経由でBIL Podsが利用可能にするDiscoveryプロジェクト。元々は `tex-prime-video-sse-initiative` の一部として管理していたが、SSEとは独立したイニシアチブのため 3/9 にspin off。

元々2025/12にGillette案件でAPI調査を開始 → Gillette失注で中断 → Mirkoが「案件に関係なくDiscoveryを続けたい」 → Binduが「BIL-Eは1案件だけでは動かない。複数Pod横断の例が必要」 → 2026/01 Binduとフォローアップ → 3/3 Mirkoがグローバルでビジネスインパクト収集開始 → 3/7 Jonathan Yi（PV BD）よりライセンスがeditorial onlyと判明。

## 2トラック並行戦略

3/11 Bindu sync で合意。技術アクセスとライセンスは別管轄のため並行で進める:

```
Track 1 (技術): Biz justification → BIL-E Intake → SDP Onboarding + BGW統合  [Bindu担当]
Track 2 (ライセンス): Jonathan Yi連携 → プロセス/POCs/ETA把握 → 商用ライセンス交渉  [Shugo担当]
```

両トラックが合流するのは実キャンペーン実行時。PoC は editorial/internal use で Track 1 のみで走れる（Chicken-and-Egg回避）。

## 現在の状況

### Bindu sync 完了（3/11 19:00-19:29 AEDT）

**主な決定事項:**
1. **Track 1: (B) BIL-E主導に決定** — SDP Core直接ではなく、BIL-E経由でオンボーディング。SDE専門知識が必要なため。
2. **Bindu が BIL-E Intake チケットを作成** + SDP Core チームとのオンボーディング調整
3. **Shugo が Jonathan との初回 sync をスケジュール** — ライセンス要件の確認
4. **Legal/Policy は Track 2 が明確になるまで保留**
5. **現在の Biz Justification で Intake 開始OK** — Harish の以前のフィードバックを踏まえて十分と判断

**オーナーシップ分担:**
- **Bindu**: 技術担当（BIL-E Intake、SDP Core オンボーディング調整）
- **Shugo**: ライセンス担当（Jonathan Yi 連携、Mirko エスカレーション）

### Track 1: 技術アクセス — BIL-E Intake & SDP Onboarding

**方針決定: (B) BIL-E主導**
- BIL-E (Harish) 経由で SDP Core オンボーディング + BGW インテグレーション
- SDE専門知識が必要なため、直接オンボーディングではなくBIL-E経由が適切
- Bindu が Intake チケット作成を担当

**Biz Justification — 十分と判断:**

| Pod | 見積もり | ステータス |
|-----|---------|-----------|
| EU Endemics | $3MM/yr（P&G Champions League $1MM, Adidas $2MM） | Mirko記載済み |
| AU | 400k USD（NBA中心、クリケットは2026年なし） | Chris Wilson回答済み |
| US | 金額なし、PoC実行中（NHL Shots on Net → フードデリバリー割引） | Fitz/Kevin回答済み |
| JP | 未回答（Mariko: ポジティブだが「Sales Struggle + ライセンシー問題で壁が高い」） | **期限超過** |
| MENA | ポテンシャルありだが数字なし | Chris Wilson言及のみ |

グローバルスケーラビリティ + 複数スポーツリーグ + US PoC実績で、Harish の以前の条件（複数Pod横断）をクリア。

### Track 2: 商用ライセンス — Jonathan Yi (PV BD) 連携

**Jonathan Yi プロフィール:**
- Sr. BD Manager, PV Devices-BD Tech & Product
- alias: yijonatj | L6, Arlington VA (EST/EDT)
- 上司: Nina Pablo (ninapabl, Sr. Mgr, L7, Seattle)

**メールスレッド経緯:**
1. 3/5: Bindu → Anand に口頭確認（「全広告主OK」）
2. 3/5: Mirko が書面エビデンスを要求
3. 3/6: Bindu → Anand にメール送信
4. 3/7: Anand → Jonathan Yi をループイン
5. 3/7: Jonathan Yi 回答: editorial only、commercial は個別交渉、コールを提案
6. **3/11: Shugo が Reply All でコール提案に応じるメール送信** — 日程調整中

**2レイヤー問題:**

| レイヤー | 管轄 | 担当者 | 状態 |
|---------|------|--------|------|
| 技術アクセス | SDP Core | Anand Kumaravel (SDM, Chicago) | 全広告主OK |
| 商用ライセンス | PV BD | Jonathan Yi (Sr. BD Mgr, Arlington VA) | editorial only、commercial は個別交渉 |

**Jonathan とのコール — 日程調整中:**
- Shugo + Jonathan の2人コール（Bindu は CC）
- TZ: Sydney↔Arlington = 15時間差。8am AEDT = 5pm EDT（前日）が最適
- 候補: Fri 3/13 8:00 AM AEDT (= Thu 3/12 5pm EDT) or Wed 3/18 8:00 AM AEDT (= Tue 3/17 5pm EDT)
- Jonathan の返信待ち

**コールで確認すべき事項（Mirko要求3点対応）:**
1. **プロセス**: 商用利用ライセンスの申請フロー、PV BD の仲介範囲、必要インプット
2. **POCs**: Jonathan が一元窓口か、プロバイダーごとに異なるか、Anand との役割分担
3. **ETA**: 典型的なタイムライン、横断 or 個別
4. **追加**: PoC = editorial use 扱いか、データxプロバイダーマッピングの有無、コスト負担者

**Mirkoの要求（3/10 Slackメッセージ）:**
1. ライセンス申請の**プロセス**を明確にする
2. **POCs**（担当窓口）を特定する
3. **ETA**（タイムライン）の把握が必須

### Discovery Doc (Quip) 状態

- **URL:** https://quip-amazon.com/c4cBAcoeV61e/Discovery-Prime-video-Live-sports-API
- **3/11確認:** 3/9以降の新規Biz updateなし。Next Stepsテーブルはステータス未記入。
- **要更新:** Jonathan Yiのライセンス問題が未反映
- **Mirkoコメント未対応:** 「We need a precise list of regions covered and sports/circuits」

### Strategy v2 ドキュメント

3層ゴール（Tech / Commercial Licensing / Legal & Ad Policy）、アプローチ(A)(B)、組織図、Jonathan Yiメール分析、Next Stepsを定義。

## 成果物一覧

```
2026-03-09_tex-prime-video-live-sports-api-discovery/
├── handover.md
├── artifacts/
│   ├── pv-live-sports-api-strategy-v2.md
│   └── bindu-sync-agenda-20260311.md
├── notes/
│   ├── pv-live-sports-api-research.md
│   ├── sdp-licensing-issue-analysis.md     ← UPDATED (CC問題解決済み)
│   └── strategy-review-20260309.md
└── history/
    └── 2026-03-09_handover.md
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | ~~3/11 19:00~~ | ~~Bindu sync コール~~ | **完了** ✅ |
| 2 | **返信待ち** | **Jonathan Yi コール日程調整** -- Reply All送信済み、返信待ち | メール送信済み |
| 3 | **Bindu担当** | **BIL-E Intake チケット作成** + SDP Core オンボーディング調整 | Bindu対応中 |
| 4 | **Jonathan コール後** | **Mirkoにライセンス問題エスカレーション** | Jonathan確認後 |
| 5 | **TBD** | **マッピングテーブル作成** -- データ x プロバイダー x 商用利用条件 x リーガル/ポリシー | PV BD確認後 |
| 6 | **TBD** | **Discovery Doc (Quip) 更新** -- ライセンス問題反映 + Mirkoコメント対応 | Jonathan コール後 |
| 7 | **EOW過ぎ** | Mirkoメール返信: APAC/MENAビジネスインパクト見積もり | Mariko JP見積もり待ち |
| 8 | **TBD** | BIL Legal / Ad Policy チェック | Track 2 明確化後（保留中） |

## 重要な判断ログ

- **Bindu sync 決定事項（3/11）**: (B) BIL-E主導でオンボーディング。現在のBiz Justificationで十分。Bindu=技術担当、Shugo=ライセンス担当。Legal/Policyは保留。
- **2トラック並行戦略（3/11）**: Track 1（技術）と Track 2（ライセンス）を並行。技術アクセスはライセンス解決を待たない。合流は実キャンペーン時。
- **Jonathan Yi コール方針（3/11）**: Shugo + Jonathan の2人コール。Bindu はCC。8am AEDT = 5pm EDT（前日）が最適スロット。
- **Chicken-and-Egg回避方針**: 技術実装（PoC）を先行し、商用ライセンスはキャンペーン単位で対応。PoC/デモはeditorial/internal useの範囲。
- **2レイヤー問題**: 技術アクセス（SDP Core）とライセンス（PV BD）は別管轄・別組織。Anandの「全広告主OK」は技術アクセスの話。Jonathan Yi（BD）がライセンス面でeditorial only制約を指摘。
- **メールスレッドCC**: saitshugはBindu↔Anand↔Jonathan Yiのスレッドに入っている（3/11確認済み）。3/11にReply Allでコール提案に応答済み。
- **データプロバイダーは前向き**: PV利用がスポーツデータ収益を伸ばすため、receptiveの見込み（Bindu sync）。
- **タイムゾーン制約**: Sydney↔Arlington = 15時間差。3-way (Shugo/Bindu/Jonathan) は10pm AEDTしかなくきつい。2人コール (Shugo/Jonathan) なら8am AEDT = 5pm EDT（前日）で快適。
- **Live Sports API経緯**: Gillette案件で開始→失注で中断→Mirkoが続行指示→BIL-Eは複数Pod横断必要→Mirkoがインパクト収集中
- **RACI**: A=Mirko、R=Shugo+Bindu、C=Pod leads・BIL-E・SDP Core・PV BD、I=グローバルステークホルダー
- **Mariko JP 壁**: Sales Struggle + ライセンシー問題（Layer 2 + Layer 3 にまたがる可能性）
- **Discovery Doc Quip**: `c4cBAcoeV61e` — 3/11時点でライセンス問題未反映、Mirkoコメント「regions/sports list」未対応

## 関連トピック

- [tex-prime-video-sse-initiative](../2026-02-26_tex-prime-video-sse-initiative/) -- SSE Initiative（元トピック。Sean Dylkeミーティング、Curated Collection Pages等）
- [au-bil-pv-growth-engagement](../2026-03-04_au-bil-pv-growth-engagement/) -- AU BIL x PV Growth連携
- [api-landscape-research](../2026-03-06_api-landscape-research/) -- Public API Landscape リサーチ（SDP含む）
- [sse-prototypes](../2026-02-23_sse-prototypes/) -- SSEプロトタイプ
