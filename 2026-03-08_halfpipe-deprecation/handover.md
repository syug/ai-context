# Handover Document
**Topic:** Halfpipe Deprecation — APAC POC として全体状況把握 + 対応タスク整理
**Date:** 2026-03-08
**Status:** 進行中

---

## 背景

BIL-E チーム（Leon Pahole, Mirko Cappai）が Halfpipe を 2026年11月12日までに全廃する計画を発表。各コンポーネントオーナーに「Deprecate or Migrate」の判断を求めている。Shugo は APAC POC（Point of Contact）として指名されており、JP 関連の Halfpipe コンポーネントの判断・調整を担当する。

Slack チャンネル #halfpipe-migration-or-deprecation が 3/6 に作成され、Mirko から全リージョン POC 宛てに指示が出ている。

### 関連リソース

- Asana プロジェクト: [BIL Halfpipe Deprecation](https://app.asana.com/1/8442528107068/project/1213527661372673) (GID: 1213527661372673)
- Slack: #halfpipe-migration-or-deprecation (C0AJV89EPSR)
- Wiki: https://w.amazon.com/bin/view/Halfpipe/Deprecation/
- Interest list: halfpipe-deprecation-interest@amazon.com

## 現在の状況

### 期限

| 日付 | アクション |
|------|-----------|
| 3/13 (金) | チケット acknowledge（Slackアナウンスの "next Friday"） |
| 3/18 | 全チケット完了; データ再評価 |
| 3/30 | Migration Decision 提出期限 |
| 11/12/2026 | 最終期限 — Halfpipe 完全廃止 |

### Shugo に関連するアイテム（6件）

#### A. 直接アサイン（Mirko から）— 3件、全て Awaiting Acknowledgement

1. **Shopping Guide v2** — Asana タスク（詳細未取得）
2. **Tutorial example spacer** — Asana タスク（詳細未取得）
3. **JPHeroCarouselAnchor** — Asana タスク（詳細未取得）

#### B. メンション（Leon/Mirko から）— JP 利用確認依頼 3件

4. **Reviews** — Leon: "one JP page is using this. Can we deprecate the page to deprecate the Halfpipe?"（3/9 にリマインダーメール受信）
5. **AXA Social Share** — Leon: "this is used on one page with very little visits, could we deprecate the page?"
6. **ImageComparisonSlider** — Mirko: "Used in JP Shugo Saito and Idia (Leon Pahole)"

#### C. 参考（他者アサイン、JP 関連）

- **Multi-asin hero showcase** (GID: 1213536673583070) — Assigned to Leigh (graleigh), JP のみ 1 ページ (317,968 visits/30d, KATE store)
- **Live Video IVS** — 別トピック `halfpipe-ivs-deprecation` で対応中

### Migration Options

1. **Deprecate** — コンポーネント不要。既存ページを廃止 or コンポーネント除去
2. **Move to AWLS** — Amazon Stores Builder のウィジェット化。スケール・顧客向け再利用性が必要な場合
3. **Move to Webflow Native** — Webflow デザイナーで実現可能な場合（コード不要）
4. **Webflow Custom Code Component** — カスタムロジックが必要な場合。Q1 以降まで未対応

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
    investigation-2026-03-08.md   -- 調査結果の詳細ノート
  handover.md                     -- 本ファイル
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | 3/13 | 3件のアサインタスク（Shopping Guide v2, Tutorial example spacer, JPHeroCarouselAnchor）を acknowledge（コメントで応答） | 未着手 |
| 2 | 3/13 | 3件のメンション（Reviews, AXA Social Share, ImageComparisonSlider）に JP ページ deprecate 可否を回答 | 未着手 |
| 3 | 3/13 | SM Lead に JP ページが live で必要かどうか確認（不要なら take down、必要なら auto-deprecation onboard） | 未着手 |
| 4 | 3/18 | 各タスクの "Migration Decision" カラムを更新 | 未着手 |
| 5 | — | 各タスクの詳細（Page Count, Visits, Pods currently using）を取得して判断材料を揃える | 未着手 |

## 重要な判断ログ

- Leon からのメンション（Reviews, AXA Social Share）はいずれも「JP 1 ページ、訪問少ない、deprecate できるか？」という内容。SM Lead 確認次第で Deprecate が有力
- ImageComparisonSlider は JP + Idia（Leon 管轄）で使用中。こちらも確認が必要
- Live Video IVS は別トピック (`halfpipe-ivs-deprecation`) で既に対応進行中

## 関連トピック

- `2026-03-07_halfpipe-ivs-deprecation` — Live Video IVS コンポーネントの個別対応（Asana コメント投稿済み）
