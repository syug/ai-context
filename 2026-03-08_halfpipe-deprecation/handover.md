# Handover Document
**Topic:** Halfpipe Deprecation — APAC POC として全体状況把握 + 対応タスク整理
**Date:** 2026-03-13
**Status:** 進行中（SM回答一部受領、IVS MENA必須判明、残回答3/16期限待ち）

---

## 背景

BIL-E チーム（Leon Pahole, Mirko Cappai）が Halfpipe を 2026年11月12日までに全廃する計画を発表。各コンポーネントオーナーに「Deprecate or Migrate」の判断を求めている。Shugo は APAC POC（Point of Contact）として指名されており、JP/AU 関連の Halfpipe コンポーネントの判断・調整を担当する。

Slack チャンネル #halfpipe-migration-or-deprecation (C0AJV89EPSR) が 3/6 に作成され、Mirko から全リージョン POC 宛てに指示が出ている。

### 関連リソース

- Asana プロジェクト: [BIL Halfpipe Deprecation](https://app.asana.com/1/8442528107068/project/1213527661372673) (GID: 1213527661372673)
- Slack: #halfpipe-migration-or-deprecation (C0AJV89EPSR)
- Wiki: https://w.amazon.com/bin/view/Halfpipe/Deprecation/
  - For Component Owners: https://w.amazon.com/bin/view/Halfpipe/Deprecation/ForComponentOwners
  - For Pods: https://w.amazon.com/bin/view/Halfpipe/Deprecation/ForPods
- Auto-deprecation: https://w.amazon.com/bin/view/CAPT/EU/ACLM/ForPods/
- Interest list: halfpipe-deprecation-interest@amazon.com

## 現在の状況

### 期限

| 日付 | アクション | 状態 |
|------|-----------|------|
| 3/13 (金) | チケット acknowledge | **全件完了** |
| 3/16 (月) | SM Lead 回答期限（自分で設定） | 一部回答あり |
| 3/18 | 全チケット完了; データ再評価 | 未着手 |
| 3/30 | Migration Decision 提出期限 | 未着手 |
| 11/12/2026 | 最終期限 — Halfpipe 完全廃止 | — |

### Shugo に直接アサインされたタスク（7件） — 全件 Acknowledged

| # | コンポーネント | GID | リージョン | ページ数 | Visits/30d | Asana セクション |
|---|---|---|---|---|---|---|
| 1 | Shopping Guide v2 | 1213536653768796 | AU | 1 (sandbox) | 50 | Acknowledged |
| 2 | Tutorial example spacer | 1213536649177929 | AU | 4 (3 prod + 1 sandbox) | 399,317 | Acknowledged |
| 3 | JPHeroCarouselAnchor | 1213536673560261 | JP | 1 | 39 | Acknowledged |
| 4 | Reviews | 1213528422756695 | JP | 1 | 9,439 | Acknowledged |
| 5 | AXA Social Share | 1213536648132544 | JP | 1 | 6,070 | Acknowledged |
| 6 | Sale Header | 1213536649685898 | JP | 1 | 933 | Acknowledged |
| 7 | Live Video IVS | 1213539247162724 | — | 0 | 0 | Acknowledged（別トピック） |

### メンションのみ（アサイン外）

- **ImageComparisonSlider** (GID: 1213536654505634) — Assignee: Daniel Castano (CA/MX POC)。JP 1ページ（Copilot+ PC sandbox）+ Ulike。Asanaコメントで確認中と回答済み
- **CCLP-Multi-UGS-2024** — Leon DM で直接依頼。JP 1ページ（not live）→ **Deprecate OK 返信済み、Leon ✅ リアクション**
- **StoreOverride** (GID: 1213529675275236) — Assignee: Leon。FerryService 廃止後もコード自体は動作継続。Configurator UI の移行が必要（Leon/BIL-E 対応中）。AU グループDM で Matt Roberts に回答済み

### ページ詳細（JP — 本番4件 + テスト1件）

| # | ページタイトル | ストア | Visits/30d | コンポーネント | SM回答 |
|---|---|---|---|---|---|
| 1 | ベスコス受賞ファンデーション | KANEBO | 9,439 / 9 avg | Reviews | 未回答 |
| 2 | WEB限定108色 アイカラーセレクター | KATE | 6,070 / 4 avg | AXA Social Share | 未回答 |
| 3 | ホームページ | Coke Christmas | 933 / 3 avg | Sale Header | 未回答 |
| 4 | ホームページ | Ulike | 39 / 1 avg | JPHeroCarouselAnchor | **Take down OK**（Mariko 3/11） |
| 5 | Copilot+ PC | Copilot+ PC | 66,907 / 117 avg | ImageComparisonSlider | テスト（SM確認不要） |

### ページ詳細（AU — 本番3件 + テスト1件）

| # | ページタイトル | ストア | Visits/30d | コンポーネント | SM回答 |
|---|---|---|---|---|---|
| 1 | Schwarzkopf Brilliance | Schwarzkopf Brilliance | 398,781 / 186 avg | Tutorial example spacer | 未回答 |
| 2 | Find your tool | Bosch Home & Garden | 456 / 0 avg | Tutorial example spacer | 未回答 |
| 3 | Brilliance | Brilliance | 30 / 2 avg | Tutorial example spacer | 未回答 |
| 4 | Home page | Shark Beauty Test | 50 / 2 avg | Tutorial example spacer, Shopping Guide v2 | テスト（SM確認不要） |

### SM Lead 確認状況

| リージョン | 宛先 | チャネル | 送信日 | 状態 |
|---|---|---|---|---|
| JP | Mariko, hayemiri | #jp-custom-pm-dt (G01PKRPA285) | 3/11 | Ulike take down OK。残3件未回答（3/16期限） |
| AU | Luke + チーム | グループDM (C0ALP1Z510Q) | 3/11 | StoreOverride 質問に回答済み。ページ take down/keep は未回答（3/16期限） |
| JP (IVS) | Mariko, Chris, Aayushi | グループDM (C0AJSBTJFR9) | 3/10 | Mariko: JP Livestreaming 需要あり。フォローアップ送信済み（Amazon Live/Twitch で代替可能か確認中） |

### Migration Options

1. **Deprecate** — コンポーネント不要。既存ページを廃止 or コンポーネント除去
2. **Move to AWLS** — Amazon Stores Builder のウィジェット化
3. **Move to Webflow Native** — Webflow デザイナーで実現可能な場合（コード不要）
4. **Webflow Custom Code Component** — カスタムロジックが必要な場合。Q1 以降まで未対応

### Auto-deprecation

ページの廃止スケジュールを管理する仕組み。データは火曜・木曜にAsanaチケットに自動反映される。
- オンボード: #bil-aclm-interest (C09KUALBK0S) で依頼 → チームがサポート
- 詳細: https://w.amazon.com/bin/view/CAPT/EU/ACLM/ForPods/
- Leon が JPHeroCarouselAnchor で auto-deprecation オンボードを要求 → 「直接 take down でいいか？」と聞き返し中（3/12）

### Board ワークフロー

Awaiting Acknowledgement → Acknowledged → Decision Made → Migration in progress → Migration Complete → Deprecated

### DTs POC 一覧

| Region | POC |
|--------|-----|
| EU Endemics | fjcr |
| EU Non-Endemics | gpernice |
| APAC | saitshug |
| MENA | sbindu |
| US | aleckunk |
| CA/MX | pcastand |
| BIL-E | lpahole |
| IN | deveshvp |

## 成果物一覧

```
2026-03-08_halfpipe-deprecation/
  notes/
    investigation-2026-03-08.md   -- 初回調査結果
  history/
    2026-03-08_handover.md        -- v1 アーカイブ
    2026-03-11_handover.md        -- v2 アーカイブ
  handover.md                     -- 本ファイル
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | 3/13 | 全7件のアサインタスクを acknowledge | **完了**（3/11） |
| 2 | 3/11 | SM Lead に JP/AU ページの take down or keep 確認を送信 | **完了**（3/11） |
| 3 | 3/11 | 各タスクの詳細取得 | **完了**（3/11） |
| 4 | 3/11 | Leon DM 返信（CCLP-Multi-UGS-2024 → Deprecate OK） | **完了**（3/11、Leon ✅） |
| 5 | 3/12 | ImageComparisonSlider JP分 Asana コメント | **完了**（3/12、確認中と回答） |
| 6 | 3/12 | AU StoreOverride 質問に回答（Matt Roberts） | **完了**（3/12） |
| 7 | — | Leon 返信待ち — JPHeroCarouselAnchor auto-deprecation vs 直接 take down | 返信待ち |
| 8 | — | IVS: Mariko フォローアップ — Amazon Live/Twitch 代替可能か確認 | 返信待ち |
| 9 | — | IVS: Chris に AU の IVS 需要確認（グループDM ドラフト済み） | 送信待ち |
| 10 | 3/12 | IVS: Amazon Live 対応マーケット確認（US/JP/IN のみ、AU/MENA 非対応） | **完了** |
| 11 | 3/12 | IVS: Asana に MENA/JP/AU 状況コメント投稿 | **完了** |
| 12 | 3/16 | JP SM 残3件回答待ち（KANEBO, KATE, Coke Christmas） | 回答待ち |
| 13 | 3/16 | AU SM 回答待ち（4ページ take down/keep） | 回答待ち |
| 14 | 3/18 | 全回答に基づき Migration Decision 更新 | 未着手 |

## 重要な判断ログ

- **Sale Header 漏れ発見（3/11）:** Asana 全件検索で発見。Acknowledge 済み
- **CCLP-Multi-UGS-2024（3/11）:** Leon DM 追加依頼 → Deprecate OK 返信済み（Leon ✅）
- **Ulike take down OK（3/11）:** Mariko（JP SM Lead）が廃止承認。Asana にコメント済み
- **Auto-deprecation vs 直接 take down（3/12）:** Leon が auto-deprecation オンボードを要求。Wiki では take down 可能なら直接 take down でOKとも読める。Leon に確認中
- **StoreOverride（3/12）:** FerryService 廃止後もコード自体は動作継続（vanilla JS、依存なし）。Configurator UI の移行のみ必要。AU チームに回答済み
- **IVS Livestreaming 需要（3/11-12）:** Mariko が JP で 2026年 Livestreaming 需要ありと回答（PVS + フルファネルキャンペーン）。ただし JP には Amazon Live / Twitch の代替あり。IVS 固有のニーズがあるかフォローアップ中
- **ネクストステップの整理:** SM Lead への Ask は2段階: (1) ページの take down or keep、(2) コンポーネントの Deprecate or Migrate（AWLS / Webflow Native / Webflow Custom Code）はページ利用状況に応じて DT 側が判断
- **ImageComparisonSlider JP（3/12）:** ダッシュボード確認で Copilot+ PC（sandbox）+ Ulike の2ページ → Asana コメント修正済み
- **MENA IVS 実使用（3/12）:** Chris から MENA で IVS を実際に使用中と報告。Amazon Live は MENA 非対応（US/JP/IN のみ）→ Webflow migration が必要になる可能性高い
- **Amazon Live 対応マーケット（3/12）:** US, JP, IN のみ。AU/MENA 非対応。ソース: https://advertising.amazon.com/solutions/products/amazon-live

## 関連トピック

- `2026-03-07_halfpipe-ivs-deprecation` — Live Video IVS コンポーネントの個別対応。Mariko が JP Livestreaming 需要ありと回答、Amazon Live/Twitch 代替可能か確認中
