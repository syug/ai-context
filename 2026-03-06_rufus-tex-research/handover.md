# Handover Document
**Topic:** Rufus x BIL TEX — APIオンボーディング協業・Coke AU Brief・AU展開確認
**Date:** 2026-03-13
**Status:** 進行中

---

## 背景

Amazon AI Shopping Assistant「Rufus」について、BIL TEXの観点から包括的なリサーチを3/6に実施・完了。その後、Billy Kwok (billyhkk) からの返信とMatt Roberts (robsmat, MIK) からのCoke AU briefに関するRufus統合の問い合わせにより、リサーチから実行フェーズに移行。

## 現在の状況

### Rufus API オンボーディング（Billy Kwok）
- Billy (3/12) 返信: PARCプロトタイプはハック的に構築。正式には**3つのNileシステム**（NileCXOrchestrator, NileCachingService, NileModelService）へのオンボーディングが必要
- 進捗は「super slowly」— 関係者の多さ、キャパシティ制約、優先度の問題
- **Billyは協業を歓迎** — "happy to share the work if you're interested in working together"
- Discovery doc共有済み: https://quip-amazon.com/BeNqA5zo9z9j
- Shugo → Billy返信済み (3/13): Coke AU briefの実需を伝え、協業意思表明、sync提案

### Coke AU Brief（Matt Roberts / MIK）
- Matt Roberts (robsmat, MIK Production Director) が Group DM (robsmat + lukthis + saitshug) でRufus × Brand Store統合について質問 (3/12 9:33am)
- Luke Thistleton: Cokeは「any integration with Rufus」を求めている。**"They just want to be the first to pull it off"**
- Shugo → Matt返信済み (3/13): TL;DRでステータス共有（正式にはまだできない、APIオンボーディング進行中だが遅い、AU利用可否も未確認）

### AU Rufus 利用可否（SIMチケット）
- SIMチケット作成済み (3/10): `Rufus AU (amazon.com.au) — Availability Status & Rollout Timeline Inquiry` → Rufus Discovery チーム宛
- **3日経過、返信なし**
- 未回答の論点: AU展開ロードマップ、Rufus未ローンチ地域でのAPI利用可否

### 前回リサーチの要点（3/6完了分）
- 10マーケット稼働中（US, UK, DE, FR, IT, ES, IN, JP, CA, PT）
- JP稼働中、**AU未ローンチ**（ロードマップに記載なし）
- Discovery 2件 + PARCプロトタイプ 1件 — 全てBilly Kwok主導のボトムアップ活動
- ARC Campaign 0件。OP1/正式ゴールには未組込

## 成果物一覧

```
2026-03-06_rufus-tex-research/
  notes/
    rufus-research.md    — 包括的リサーチレポート（ロケール、Discovery詳細、ソース一覧）
  history/
    2026-03-06_handover.md — 旧バージョン（リサーチ完了時点）
  handover.md            — 本ファイル
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|----------|
| 1 | — | Billy Kwokとのsync設定（返信待ち） | 進行中 |
| 2 | — | SIMチケット Rufus Discovery チームからの回答待ち（3日経過） | 待ち |
| 3 | — | AU Rufus未ローンチ地域でのAPI利用可否を確認（SIM回答後 or Billy sync時） | 未着手 |
| 4 | — | Coke briefへのRufus統合フィージビリティ最終回答（上記3件の結果次第） | 未着手 |

## 重要な判断ログ

- **リサーチ→実行フェーズへの移行 (3/13):** Billy返信 + Coke briefの実需により、調査完了から協業・実装検討フェーズに移行
- **Coke briefの戦略的意味:** クライアントが「Rufus統合の最初の事例になりたい」と明言。Billy側の優先度を上げる材料になりうる
- **2つの未確認リスク:** (1) AU未ローンチ地域でRufus APIが利用可能か (2) オンボーディングのタイムライン（Coke briefの期限に間に合うか）
- **前回リサーチの判断ログ（3/6）:** 調査手法は4エージェント並列、AU展開は「計画が見当たらない」状態、Billy Kwokのボトムアップ活動が唯一の推進力

## 関連トピック

- [tex-wbr-review-and-deep-dive](../2026-03-02_tex-wbr-review-and-deep-dive/) — WBRレビューでRufus関連タスクがEU Endemicsに記載
- [bil-op1-planning-fy27](../2026-03-06_bil-op1-planning-fy27/) — OP1にRufus未組込の背景
- [tex-survey-analysis](../2026-02-25_tex-survey-analysis/) — FY26 Discovery Planningサーベイ（Rufusは候補に挙がらず）
- [prototype-ideation-research](../2026-03-05_prototype-ideation-research/) — FY26プロトタイプ候補リサーチ
- [dine-2.0-tech-feasibility](../2026-03-11_dine-2.0-tech-feasibility/) — Mars Dine 2.0（同じくAU BIL案件）
