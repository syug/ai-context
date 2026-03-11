# Handover Document
**Topic:** Halfpipe Deprecation — APAC POC として全体状況把握 + 対応タスク整理
**Date:** 2026-03-11
**Status:** 進行中（全タスク Acknowledged、SM Lead 確認送信済み、回答待ち）

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
| 3/16 (月) | SM Lead 回答期限（自分で設定） | 回答待ち |
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

- **ImageComparisonSlider** (GID: 1213536654505634) — Assignee: Daniel Castano (CA/MX POC)。JP 2ページ（sandbox）。JP分のみ回答すればOK
- **CCLP-Multi-UGS-2024** — Leon DM で直接依頼。JP 1ページ（not live）→ Deprecate OK。返信ドラフト済み（未送信）

### ページ詳細（JP — 本番4件 + テスト1件）

| # | ページタイトル | ストア | Visits/30d | コンポーネント | 状態 |
|---|---|---|---|---|---|
| 1 | ベスコス受賞ファンデーション | KANEBO | 9,439 / 9 avg | Reviews | 本番 |
| 2 | WEB限定108色 アイカラーセレクター | KATE | 6,070 / 4 avg | AXA Social Share | 本番 |
| 3 | ホームページ | Coke Christmas | 933 / 3 avg | Sale Header | 本番 |
| 4 | ホームページ | Ulike | 39 / 1 avg | JPHeroCarouselAnchor | 本番 |
| 5 | Copilot+ PC | Copilot+ PC | 66,907 / 117 avg | ImageComparisonSlider | テスト |

### ページ詳細（AU — 本番3件 + テスト1件）

| # | ページタイトル | ストア | Visits/30d | コンポーネント | 状態 |
|---|---|---|---|---|---|
| 1 | Schwarzkopf Brilliance | Schwarzkopf Brilliance | 398,781 / 186 avg | Tutorial example spacer | 本番（evergreen） |
| 2 | Find your tool | Bosch Home & Garden | 456 / 0 avg | Tutorial example spacer | 本番（evergreen） |
| 3 | Brilliance | Brilliance | 30 / 2 avg | Tutorial example spacer | 本番（evergreen） |
| 4 | Home page | Shark Beauty Test | 50 / 2 avg | Tutorial example spacer, Shopping Guide v2 | テスト |

### SM Lead 確認状況

| リージョン | 宛先 | チャネル | 送信日 | 状態 |
|---|---|---|---|---|
| JP | Kaiyi, hayemiri | #jp-custom-pm-dt (G01PKRPA285) | 3/11 | **送信済み** — 回答待ち（3/16期限） |
| AU | Luke + チーム | グループDM (C0ALP1Z510Q) | 3/11 | **送信済み** — 回答待ち（3/16期限） |

### Migration Options

1. **Deprecate** — コンポーネント不要。既存ページを廃止 or コンポーネント除去
2. **Move to AWLS** — Amazon Stores Builder のウィジェット化
3. **Move to Webflow Native** — Webflow デザイナーで実現可能な場合（コード不要）
4. **Webflow Custom Code Component** — カスタムロジックが必要な場合。Q1 以降まで未対応

### Auto-deprecation

ページの廃止スケジュールを管理する仕組み。データは火曜・木曜にAsanaチケットに自動反映される。
- オンボード: #bil-aclm-interest で依頼 → チームがサポート
- 詳細: https://w.amazon.com/bin/view/CAPT/EU/ACLM/ForPods/

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
    2026-03-08_handover.md        -- 旧バージョンアーカイブ
  handover.md                     -- 本ファイル
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | 3/13 | 全7件のアサインタスクを acknowledge | **完了**（3/11） |
| 2 | 3/11 | SM Lead に JP/AU ページの take down or keep 確認を送信 | **完了**（3/11 JP #jp-custom-pm-dt + AU グループDM） |
| 3 | 3/11 | 各タスクの詳細（Page Count, Visits, ページタイトル）を取得 | **完了**（3/11） |
| 4 | 3/16 | SM Lead からの回答を受け取る（JP: Kaiyi/hayemiri、AU: Luke） | 回答待ち |
| 5 | 3/18 | 回答に基づき各タスクの Migration Decision を更新 | 未着手 |
| 6 | — | Leon DM 返信（CCLP-Multi-UGS-2024 → Deprecate OK）— ドラフト済み、未送信 | 未完了 |
| 7 | — | ImageComparisonSlider の JP 分について Asana コメントで回答（sandbox 2ページ → Deprecate） | 未着手 |

## 重要な判断ログ

- **Sale Header 漏れ発見（3/11）:** handover のリストに含まれていなかった Sale Header (Coke Christmas, JP 1ページ) を Asana 全件検索で発見。Acknowledge 済み
- **CCLP-Multi-UGS-2024（3/11）:** Leon が DM で追加依頼。Asana プロジェクトのリスト外。JP 1ページ（not live）→ Deprecate OK で返信ドラフト作成
- **ネクストステップの整理:** SM Lead への Ask は2段階: (1) ページの take down or keep、(2) コンポーネントの Deprecate or Migrate（AWLS / Webflow Native / Webflow Custom Code）はページ利用状況に応じて DT 側が判断
- **Auto-deprecation:** Keep の場合は auto-deprecation にオンボードして廃止予定日を設定。#bil-aclm-interest でサポート依頼可能
- Leon からのメンション（Reviews, AXA Social Share）はいずれも「JP 1 ページ、訪問少ない、deprecate できるか？」という内容。SM Lead 確認次第で Deprecate が有力
- AU の Tutorial example spacer は Schwarzkopf Brilliance が 398K visits/30d でかなりアクティブ。SM 判断が重要
- Live Video IVS は別トピック (`halfpipe-ivs-deprecation`) で既に対応進行中（使用ページ 0、Deprecate が有力）

## 関連トピック

- `2026-03-07_halfpipe-ivs-deprecation` — Live Video IVS コンポーネントの個別対応（Asana コメント投稿済み）
