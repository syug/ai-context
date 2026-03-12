# Handover Document
**Topic:** PV Live Sports API Discovery -- BGW統合・商用ライセンス・リーガル準備
**Date:** 2026-03-13
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

### Track 1: 技術アクセス — BIL-E Intake & SDP Onboarding

**方針決定（3/11 Bindu sync）: (B) BIL-E主導**
- BIL-E経由で SDP Core オンボーディング + BGW インテグレーション
- SDE専門知識が必要なため、直接ではなくBIL-E経由が適切
- **Bindu が BIL-E Intake チケット作成済み**（3/11）: https://app.asana.com/1/8442528107068/project/1210071907827451/task/1213614486810150

**Biz Justification — 全Pod回答完了:**

| Pod | 見積もり | ステータス |
|-----|---------|-----------|
| EU Endemics | $3MM/yr（P&G Champions League $1MM, Adidas $2MM） | Mirko記載済み |
| AU | 400k USD（NBA中心、クリケットは2026年なし） | Chris Wilson回答済み |
| US | 金額なし、PoC実行中（NHL Shots on Net → フードデリバリー割引） | Fitz/Kevin回答済み |
| **JP** | **$300K-$600K**（MLB唯一人気、Boxing暴力的で売り困難、NBA低関心） | **Mariko回答済み（3/11）** |
| MENA | ポテンシャルありだが数字なし（スポーツスポンサー愛着強い） | Chris Wilson回答済み |

**合計見積もり: $3.7M-$4M/yr**（JP不確実性あり）。Harish の条件（複数Pod横断）をクリア。

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
6. 3/11: Shugo が Reply All でコール提案に応じるメール送信

**2レイヤー問題:**

| レイヤー | 管轄 | 担当者 | 状態 |
|---------|------|--------|------|
| 技術アクセス | SDP Core | Anand Kumaravel (SDM, Chicago) | 全広告主OK |
| 商用ライセンス | PV BD | Jonathan Yi (Sr. BD Mgr, Arlington VA) | editorial only、commercial は個別交渉 |

**Jonathan コール設定済み（3/12）:**
- **日時:** Wed 3/18 8:30-9:00 AM AEDT (= Tue 3/17 5:30-6:00 PM EDT)
- **参加者:** Shugo + Jonathan（Bindu optional）
- **場所:** Amazon Chime
- **アジェンダ:** プロセス / POCs / ETA / PoC = editorial?

**コールで確認すべき事項（Mirko要求3点対応）:**
1. **プロセス**: 商用利用ライセンスの申請フロー、PV BD の仲介範囲、必要インプット
2. **POCs**: Jonathan が一元窓口か、プロバイダーごとに異なるか、Anand との役割分担
3. **ETA**: 典型的なタイムライン、横断 or 個別
4. **追加**: PoC = editorial use 扱いか、データxプロバイダーマッピングの有無、コスト負担者

### Discovery Doc (Quip) 状態

- **URL:** https://quip-amazon.com/c4cBAcoeV61e/Discovery-Prime-video-Live-sports-API
- **3/12更新:** JP見積もり（$300K-$600K）をAPAC/MENAセクションにマージ済み
- **要更新:** Jonathan Yiのライセンス問題がまだ未反映 → 3/18コール後に更新予定
- **Mirkoコメント未対応:** 「We need a precise list of regions covered and sports/circuits」
- **Mirkoへ Slack で JP 追加を報告済み**（3/12 #tex-discovery-pv-live-sports-api-enablement）

### Strategy v2 ドキュメント

3層ゴール（Tech / Commercial Licensing / Legal & Ad Policy）、アプローチ(A)(B)、組織図、Jonathan Yiメール分析、Next Stepsを定義。

### オーナーシップ分担（3/11 Bindu sync 決定）

- **Bindu**: 技術担当（BIL-E Intake、SDP Core オンボーディング調整）
- **Shugo**: ライセンス担当（Jonathan Yi 連携、Mirko エスカレーション）

## 成果物一覧

```
2026-03-09_tex-prime-video-live-sports-api-discovery/
├── handover.md
├── artifacts/
│   ├── pv-live-sports-api-strategy-v2.md
│   └── bindu-sync-agenda-20260311.md
├── notes/
│   ├── pv-live-sports-api-research.md
│   ├── sdp-licensing-issue-analysis.md
│   └── strategy-review-20260309.md
└── history/
    ├── 2026-03-09_handover.md
    └── 2026-03-11_handover.md
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | ~~3/11~~ | ~~Bindu sync コール~~ | **完了** ✅ |
| 2 | ~~3/11~~ | ~~BIL-E Intake チケット作成~~ | **Bindu作成済み** ✅ |
| 3 | ~~3/12~~ | ~~Mariko JP見積もり~~ | **回答済み $300K-$600K** ✅ |
| 4 | ~~3/12~~ | ~~Discovery Doc JP追加~~ | **Quip更新済み** ✅ |
| 5 | ~~3/12~~ | ~~Jonathan Yi コール設定~~ | **3/18 8:30 AEDT 招待送信済み** ✅ |
| 6 | **3/18** | **Jonathan Yi コール** — プロセス / POCs / ETA / PoC = editorial? | 招待送信済み |
| 7 | **3/18後** | **Mirkoにライセンス問題エスカレーション** | Jonathan確認後 |
| 8 | **TBD** | **マッピングテーブル作成** -- データ x プロバイダー x 商用利用条件 x リーガル/ポリシー | PV BD確認後 |
| 9 | **3/18後** | **Discovery Doc (Quip) 更新** -- ライセンス問題反映 + Mirkoコメント対応 | Jonathan コール後 |
| 10 | **TBD** | BIL Legal / Ad Policy チェック | Track 2 明確化後（保留中） |

## 重要な判断ログ

- **Bindu sync 決定事項（3/11）**: (B) BIL-E主導でオンボーディング。現在のBiz Justificationで十分。Bindu=技術担当、Shugo=ライセンス担当。Legal/Policyは保留。
- **2トラック並行戦略（3/11）**: Track 1（技術）と Track 2（ライセンス）を並行。技術アクセスはライセンス解決を待たない。合流は実キャンペーン時。
- **Jonathan Yi コール確定（3/12）**: Wed 3/18 8:30 AM AEDT = Tue 3/17 5:30 PM EDT。Shugo + Jonathan 2人コール。Bindu optional。Amazon Chime。
- **JP Biz Justification（3/11-12）**: Mariko回答 $300K-$600K。Boxing暴力的で売り困難、NBA日本で不人気、MLB唯一人気だが権利制限。"highly uncertain" だがBiz justification全Pod回答完了（合計$3.7M-$4M/yr）。
- **BIL-E Intake 作成済み（3/11）**: Binduが即日対応。Asanaチケット作成。
- **Chicken-and-Egg回避方針**: 技術実装（PoC）を先行し、商用ライセンスはキャンペーン単位で対応。PoC/デモはeditorial/internal useの範囲。
- **2レイヤー問題**: 技術アクセス（SDP Core）とライセンス（PV BD）は別管轄・別組織。Anandの「全広告主OK」は技術アクセスの話。Jonathan Yi（BD）がライセンス面でeditorial only制約を指摘。
- **メールスレッドCC**: saitshugはBindu↔Anand↔Jonathan Yiのスレッドに入っている。3/11にReply Allでコール提案に応答済み。
- **データプロバイダーは前向き**: PV利用がスポーツデータ収益を伸ばすため、receptiveの見込み（Bindu sync）。
- **タイムゾーン制約**: Sydney↔Arlington = 15時間差。3-way は非現実的。2人コールで8:30am AEDT = 5:30pm EDT（前日）が最適。
- **RACI**: A=Mirko、R=Shugo+Bindu、C=Pod leads・BIL-E・SDP Core・PV BD、I=グローバルステークホルダー
- **Mariko JP 壁の詳細**: Boxing = 暴力的でスポンサー売り困難、NBA = 日本で関心低い、MLB = 唯一人気だがスポンサーシップ権利が限定的
- **Discovery Doc Quip**: `c4cBAcoeV61e` — 3/12にJP追加済み。ライセンス問題は3/18コール後に反映予定。Mirkoコメント「regions/sports list」未対応。

## 関連トピック

- [tex-prime-video-sse-initiative](../2026-02-26_tex-prime-video-sse-initiative/) -- SSE Initiative（元トピック。Sean Dylkeミーティング、Curated Collection Pages等）
- [au-bil-pv-growth-engagement](../2026-03-04_au-bil-pv-growth-engagement/) -- AU BIL x PV Growth連携
- [api-landscape-research](../2026-03-06_api-landscape-research/) -- Public API Landscape リサーチ（SDP含む）
- [sse-prototypes](../2026-02-23_sse-prototypes/) -- SSEプロトタイプ
