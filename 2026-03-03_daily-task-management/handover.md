# Handover Document
**Topic:** Daily Task Management — WorkLog運用・Weekly Routine・WBRスケジュール・/daily Skill
**Date:** 2026-03-16
**Status:** 進行中

---

## 背景

`weekly-workflow-setup` トピックで確立したWorkLogテンプレート・Daily Log運用の仕組みを、継続的な運用管理として独立トピック化。3/12に `/daily` Skill を作成・運用開始。3/13に W11 Weekly Review + Retrospective を実施。

## 現在の状況

### W11 (3/9-3/13) Weekly Review サマリー

- **週合計: 31/39完了 = 79%**
- **Well done**: Halfpipe毎日進捗、PES 2日完結、PV Live API BizJust前進、/daily Skill作成、新規3トピック
- **Could be better**: WBR Input未完了、Forte Feedback 9週持ち越し、Survey未着手、OP1 Loop記入遅延
- **Action plan**: OP1今日中完成 → Forte月曜90min → WBR W13水曜AM → Survey来週

### 3/13 完了タスク

- OP1 part 2 Brainstorming (Chris)
- Halfpipe: Leon JPHeroCarousel/Carousel Ulike/auto-dep onboarding 3件回答 + Fabio Bento Story Tile確認
- Coke: Billy返信 + Matt&Luke共有
- UK AI Question: ドラフト完了（Luke対応中、Julia返信済み）
- Weekly Review + Retrospective作成 → Notion反映
- WBR Highlights/Lowlights Draft (W11) 作成 → Notion反映

### 🔴 次回セッション開始時リマインド（3/14 Slackチェックで検出・未対応）

1. **Mirko グループDM（Alex/Nathan）** `C0ALKLXV109` — DCS HND permission件でMirkoが追加質問。APAC leadership合意の有無、ビジネスインパクト（売上/キャンペーン数）、Kate org外ページビルダーのリスクについて。**全文取得 → 返信必要**
2. **Billy Kwok DM** `D0AKC4PDY3D` — Rufus Nileオンボーディング進捗報告。各チームとコール済み、L6 SDE/SDMとのデザインレビュー準備が次ステップだが時間がない。**ライト返信でOK**

### 3/13 未完了 → 3/16 キャリーオーバー

- **TEX OP1**: 自分のInput作成(Survey解析) → Consolidate → Loop記入（3/16期限 🔴🔴）
- **Halfpipe IVS**: JP/AU Demand Clarification + BIL-E Decision（pending）
- **Halfpipe SM**: JP/AU返信待ち（pending）
- **PV Live API**: Bindu intake requestアクセス待ち（pending）
- **Coke Rufus**: Rufus team待ち + Alleyフォローアップ
- **Weekly Review**: Slack catchup / Asana review / Daily↔Weekly sync / WBR check（一部未完了）

### /daily Skill（運用中）

`~/.claude/skills/daily/SKILL.md` — 主要ルール:
- 全自動実行: カレンダー・Notion・Slack・メール並列取得 → キャリーオーバー処理 → Notion書き込み → Daily Briefing → 対話
- **キャリーオーバー**: 未完了は昨日から削除して今日に移動（重複回避）。完了済みはそのまま残す
- **タスクブレイクダウン**: 親タスク+サブタスク階層。動詞で始める
- **構造継承**: 昨日のタスク構造を活かしてマージ。フラット化禁止

### /weekly Skill（運用中）

`~/.claude/skills/weekly/SKILL.md` — WBR・Meeting ノート読み込み+サマリ生成。
- 奇数週金曜に WBR Highlights作成 を追加（3/16）

### Weekly Routine Tasks（確立済み）

| 曜日 | タスク |
|------|--------|
| 月 | カレンダー確認、AU WIP(12:00)、TEX Huddle(13:00)、Weekly Parc Check |
| 火 | Weekly Project Report → Mirko DM |
| 木 | Prep for 1:1 Chris、1:1 Chris(14:15) |
| 金 | Slack catchup、Asana review、Daily↔Weekly sync、WBR check |
| 隔週 | WBR Input(奇数週水)、WBR Read(奇数週木/偶数週火)、WBR Highlights作成(奇数週金)、Mirko 1:1(月1) |

### WBR 隔週スケジュール（確立済み）

| WBR | 曜日 | Week |
|-----|------|------|
| TEX NA WBR | 水 | 奇数 (W11,W13...) |
| WW TEX WBR | 木 | 奇数 |
| TEX EU/APAC/MENA WBR | 木 | 奇数 |
| WW BIL WBR | 火 | 偶数 (W10,W12...) |

### 運用ルール（確立済み）
- Weekly TODOs = Single Source of Truth、Daily Log は派生
- Daily↔Weekly 整合性同期
- タスク数制限: 1日5件以下
- **Daily Log キャリーオーバー:** 未完了タスクを翌日にマージしたら前日から削除。完了済みはそのまま残す（圧縮・書き換えしない）
- **タスクブレイクダウン:** 親タスク + サブタスク階層。動詞で始める具体的アクション
- **構造継承:** キャリーオーバー時に昨日のタスク構造を活かしてマージ。フラット化禁止
- **WorkLog作成ワークフロー:** `notes/weekly-worklog-workflow.md` 参照
- **外部アクション承認ルール:** カレンダー招待・メール・Slack投稿は「Go」待ち

### WorkLog 運用
- **先週:** WorkLog26-Mar01 ID `31615ecd-1a0d-810d-991e-f3f40f169317` — クリーンアップ完了
- **今週:** WorkLog26-Mar08 ID `31e15ecd-1a0d-819a-83cf-e001c2a67194` — W11 Retrospective反映済み

### OP1 インプット依頼状況
- **依頼元:** Mirko → Shugo（メール 3/7）
- **依頼先:** Shugo → Kaiyi/Leigh/Bindu（グループDM `C0ALF2Q9QU9`、3/12）
- **期限:** 3/16ミーティング前に最終化
- **Kaiyi:** 返信済み（自分のgoals baseで書くよう助言）
- **Leigh/Bindu:** 未回答

### 来週の予定
- **3/16 TEX OP1 Preparation**（不参加、事前インプットのみ — 今日中にLoop記入完了目標）
- **3/17 Annual Review — Mirko**（17:00 JST / 03:00 AEDT）
- **3/18 Jonathan Yi (PV BD) call**（08:30 AEDT）
- **3/18 Halfpipe Deprecation Acknowledge期限**
- **6/3-4-5 東京オフサイト**（Mirko通知、トラベル手配開始）

### Asana / Notion DB 情報
- **(A) Work Log**: `collection://0eaa9ab4-2968-4c9f-90f1-2b0da3b2f769`
- **TEMPLATE-WorkLog26**: `31015ecd-1a0d-8104-8bdb-e24359b886a5`

## 成果物一覧

```
2026-03-03_daily-task-management/
├── handover.md                        ← 本ファイル
├── history/
│   ├── 2026-03-03_handover.md
│   ├── 2026-03-03_2_handover.md
│   ├── 2026-03-03_3_handover.md
│   ├── 2026-03-05_handover.md
│   ├── 2026-03-06_handover.md
│   ├── 2026-03-07_handover.md
│   ├── 2026-03-09_handover.md
│   ├── 2026-03-10_handover.md
│   ├── 2026-03-12_handover.md
│   ├── 2026-03-12_2_handover.md
│   └── 2026-03-12_3_handover.md
├── artifacts/
│   ├── asana-weekly-summary.py
│   └── run-weekly-summary.sh
└── notes/
    └── weekly-worklog-workflow.md
```

Skills:
- `~/.claude/skills/daily/SKILL.md` — /daily Skill
- `~/.claude/skills/weekly/SKILL.md` — /weekly Skill（WBR Highlights追加済み）

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | 来週月曜 | **Forte Feedback** — CW 1人目だけでも（9週持ち越し） | 未着手 |
| 2 | ✅ | **PES サマリードック** → Asana経由Matt共有 | 完了(3/12) |
| 3 | 今週 | **Croc Awards** — Luke回答待ち | 待ち |
| 4 | 3/16 🔴🔴 | **TEX OP1** — Input作成 → Consolidate → Loop記入 | 進行中 |
| 5 | TBD | **AU OP1 BS Vol.2** — Topic 4 AI + Topic 5 | 未着手 |
| 6 | ✅ | **PV Live API Discovery** — BizJust更新+Mirko報告 | 完了(3/12) |
| 7 | 来週 | **Chris トークドラフト** フィードバック | 未着手 |
| 8 | 3/18 | **Halfpipe Deprecation** — IVS pending、SM pending、Leon/Fabio対応済み | 進行中 |
| 9 | 来週 | **Survey 全体サマライズ** | 未着手 |
| 10 | 来週 | Webflow+Livestreaming | 一部完了 |
| 11 | ✅ | **Weekly Project Report** | 完了(3/10) |
| 12 | - | Life Log 統合プラン決定 | 未着手 |
| 13 | 毎週 | 週次WorkLog作成・Weekly Routine実行 | 継続 |
| 14 | ✅ | **UK Arla Campaign** — ドラフト完了、Luke対応中 | 完了(3/13) |
| 15 | 3/17 | **Annual Review prep** — Forte先に | 未着手 |
| 16 | ✅ | **/daily Skill** + **/weekly Skill** WBR Highlights追加 | 完了 |
| 17 | 来週 | **Coke Rufus** — Rufus team待ち + Alleyフォローアップ | pending |
| 18 | - | **東京オフサイト 6/3-5** トラベル手配 | 新規 |

## 重要な判断ログ

- **weekly-workflow-setup から分離**（3/3）
- **Daily Log 作成フロー確立**（3/3）
- **Asana作業時間トラッキング導入**（3/7）
- **タスク数制限**（3/7）: 1日5件以下
- **WorkLog作成ワークフロー正式定義**（3/9）
- **WBR隔週スケジュール調査**（3/9）
- **外部アクション承認ルール**（3/9）
- **キャリーオーバールール**（3/10→3/13改善）: 未完了は削除して移動、完了はそのまま残す
- **CocaCola Pipeline ≠ World Cup**（3/11）
- **/daily Skill作成**（3/12）: 全自動+Briefing+対話
- **構造継承ルール**（3/12）: フラット化禁止
- **タスクブレイクダウン必須化**（3/12）: 親+サブタスク階層
- **Kaiyi OP1対応**（3/12）: ゴール・ロール・レイオフに触れない方針
- **OP1インプット取りまとめ構造**（3/12）: Mirko→Shugo→Kaiyi/Leigh/Bindu
- **W11 Retrospective**（3/13）: 79%完了率、Forte/Survey慢性先送りが課題
- **WBR Highlights隔週ルーティン追加**（3/13）: 奇数週金曜に作成、/weekly Skillにも反映

## 関連トピック

- `2026-02-23_weekly-workflow-setup` — 設計・構築記録（完了・前身トピック）
- `2026-02-25_tex-survey-analysis` — Survey 分析（サマライズ待ち）
- `2026-02-27_au-pes-tech-check` — AU PES Tech Check（3/12サマリードック完了）
- `2026-03-02_tex-wbr-review-and-deep-dive` — /weekly Skill、WBR W11読み込み
- `2026-03-06_bil-op1-planning-fy27` — OP1 FY27（TEX OP1 3/16期限）
- `2026-03-06_rufus-tex-research` — Rufus Billy協業、Coke AU
- `2026-03-07_halfpipe-ivs-deprecation` — Halfpipe IVS（MENA必須、JP需要あり）
- `2026-03-08_halfpipe-deprecation` — Halfpipe全体（Leon/Fabio対応済み）
- `2026-03-09_tex-prime-video-live-sports-api-discovery` — PV Live API（Jonathan Yi 3/18）
- `2026-03-09_tex-op1-fy27-goals` — TEX OP1 FY27（ドラフトv1、チームInput収集中）
- `2026-03-11_uk-arla-ai-on-clp` — UK Arla AI（ドラフト完了）
- `2026-03-11_dine-2.0-tech-feasibility` — Dine 2.0（Tech Feasibility完了）
