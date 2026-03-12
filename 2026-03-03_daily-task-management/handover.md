# Handover Document
**Topic:** Daily Task Management — WorkLog運用・Weekly Routine・WBRスケジュール・/daily Skill
**Date:** 2026-03-12
**Status:** 進行中

---

## 背景

`weekly-workflow-setup` トピックで確立したWorkLogテンプレート・Daily Log運用の仕組みを、継続的な運用管理として独立トピック化。3/9にWeekly WorkLog作成ワークフローを正式定義し、WBR隔週スケジュールの調査・Outlookリマインダー設定を完了。3/12に `/daily` Skill を作成。

## 現在の状況

### 3/12 完了タスク (12件、完了率67%)

- TEX OP1: チームにInput依頼シェア
- PES Tech Check: サマリードック完成 → Asana経由Matt共有
- Prep for 1:1 w/Chris + 14:15 1:1完了
- Halfpipe: Leon auto-dep返信 / StoreOverride確認 / Mirko ack / SM確認 / IVS確認(Chris/Mariko/Aayushi) / Mariko JP Live Streaming返信
- PV Live API: Mariko JP business opportunity返信 / Biz Justification更新+Mirko報告
- Coke: Billy確認(Discovery doc) / Matt&Lukeに共有

### 3/12 未完了 → 3/13 キャリーオーバー候補

- **TEX OP1**: 自分のInput作成(Survey解析) → Consolidate → Loop記入（3/16期限 🔴）
- **Halfpipe IVS**: Chris MENA inputサマライズ → Asanaコメント更新
- **Halfpipe SM**: JP/AU返信待ち
- **PV Live API**: Bindu intake requestアクセス待ち
- **Coke Rufus**: Billy返信 + Rufus team待ち（Alleyフォローアップ検討）
- **UK AI Question**: ドラフト作成

### /daily Skill（3/12作成・運用開始）

`~/.claude/skills/daily/SKILL.md` に定義。主要ルール:
- **全自動実行**: カレンダー・Notion・Slack・メール並列取得 → キャリーオーバー処理 → Notion書き込み → Daily Briefing表示 → 対話的確認
- **キャリーオーバー必須**: 昨日のエントリを必ず先に処理。省略・後回し禁止
- **タスクブレイクダウン必須**: ハイレベルな指示をそのまま書かず、親タスク+サブタスクに分解
- **構造継承ルール**: 昨日のタスク構造（階層・サブタスク・グルーピング）を活かしてマージ。フラット化禁止
- **Briefing表示**: 左ボーダーのみ、セクション別（カレンダー/Key Priority/キャリーオーバー/メール・Slack/返信待ち/要判断）
- `/daily yesterday` で振り返りモードも可

### Weekly Routine Tasks（確立済み）

| 曜日 | タスク |
|------|--------|
| 月 | カレンダー確認、AU WIP(12:00)、TEX Huddle(13:00)、Weekly Parc Check |
| 火 | Weekly Project Report → Mirko DM |
| 木 | Prep for 1:1 Chris、1:1 Chris(14:15) |
| 金 | Slack catchup、Asana review、Daily↔Weekly sync、WBR check |
| 隔週 | WBR Input(奇数週水)、WBR Read(奇数週木/偶数週火)、Mirko 1:1(月1) |

### WBR 隔週スケジュール（確立済み）

| WBR | 曜日 | Week |
|-----|------|------|
| TEX NA WBR | 水 | 奇数 (W11,W13...) |
| WW TEX WBR | 木 | 奇数 |
| TEX EU/APAC/MENA WBR | 木 | 奇数 |
| WW BIL WBR | 火 | 偶数 (W10,W12...) |

Outlookリマインダー4件作成済み（8-9am, Free, Loop links付き）

### 運用ルール（確立済み）
- Weekly TODOs = Single Source of Truth、Daily Log は派生
- Daily↔Weekly 整合性同期
- タスク数制限: 1日5件以下
- **Daily Log キャリーオーバー:** 未完了タスクを翌日にマージしたら前日から削除（重複回避）。構造継承必須
- **タスクブレイクダウン:** 親タスク + サブタスク階層。動詞で始める具体的アクション
- **WorkLog作成ワークフロー:** `notes/weekly-worklog-workflow.md` 参照
- **外部アクション承認ルール:** カレンダー招待・メール・Slack投稿は「Go」待ち（ai--mission-control のみ例外）

### WorkLog 運用
- **先週:** WorkLog26-Mar01 ID `31615ecd-1a0d-810d-991e-f3f40f169317` — クリーンアップ完了
- **今週:** WorkLog26-Mar08 ID `31e15ecd-1a0d-819a-83cf-e001c2a67194` — 3/12 Daily Log更新済み

### Asana / Notion DB 情報
- Asanaフィールド: Priority / Estimated / Category / Actual Time
- **(A) Work Log**: `collection://0eaa9ab4-2968-4c9f-90f1-2b0da3b2f769`
- **TEMPLATE-WorkLog26**: `31015ecd-1a0d-8104-8bdb-e24359b886a5`

### 来週の予定（FYI）

- **3/17 Annual Review — Mirko**（17:00 JST / 03:00 AEDT）: Forte Feedback提出を先に
- **3/16 TEX OP1 Preparation**（不参加、事前インプットのみ — 金曜までにLoop記入完了目標）

## 成果物一覧

```
2026-03-03_daily-task-management/
├── handover.md                        ← 本ファイル
├── history/
│   ├── 2026-03-03_handover.md         ← 初版
│   ├── 2026-03-03_2_handover.md       ← 第2版
│   ├── 2026-03-03_3_handover.md       ← 第3版
│   ├── 2026-03-05_handover.md         ← 第4版
│   ├── 2026-03-06_handover.md         ← 第5版
│   ├── 2026-03-07_handover.md         ← 第6版
│   ├── 2026-03-09_handover.md         ← 第7版
│   ├── 2026-03-10_handover.md         ← 第8版
│   └── 2026-03-12_handover.md         ← 第9版
├── artifacts/
│   ├── asana-weekly-summary.py        ← 週次集計スクリプト
│   └── run-weekly-summary.sh          ← シェルラッパー
└── notes/
    └── weekly-worklog-workflow.md      ← WorkLog作成ワークフロー
```

Skill:
- `~/.claude/skills/daily/SKILL.md` — /daily Skill定義

Notion上:
- WorkLog26-Mar01（クリーンアップ完了）
- WorkLog26-Mar08（3/12 Daily Log更新済み）

Memory:
- `memory/team-members.md` — チームメンバーalias・org構造・関係性

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | 今週 | **Forte Feedback** — CW, MC, GL, KW（8週持ち越し） | 未着手 |
| 2 | ✅ | **PES サマリードック** → Asana経由Matt共有 | 完了(3/12) |
| 3 | 今週 | **Croc Awards** — Luke回答待ち（Demo mode切替） | 待ち |
| 4 | 3/16 🔴 | **TEX OP1** — APAC インプット Loop 記入（金曜完成目標） | 進行中 |
| 5 | TBD | **AU OP1 BS Vol.2** — Topic 4 AI + Topic 5 | 未着手 |
| 6 | ✅ | **PV Live API Discovery** — Biz Justification更新+Mirko報告 | 完了(3/12) |
| 7 | 今週 | **Chris トークドラフト** フィードバック | 未着手 |
| 8 | 3/18 | **Halfpipe Deprecation** — IVS Chris MENA サマライズ残、SM返信待ち | 進行中 |
| 9 | 今週 | **Survey 全体サマライズ** | 未着手 |
| 10 | 今週 | Webflow+Livestreaming（Gift Reporting完了） | 一部完了 |
| 11 | ✅ | **Weekly Project Report** → Mirko DM | 完了(3/10) |
| 12 | - | Life Log 統合プラン決定 | 未着手 |
| 13 | 毎週 | 週次WorkLog作成・Weekly Routine実行 | 継続 |
| 14 | 今週 | **UK Arla Campaign** — ドラフト作成 | 進行中 |
| 15 | 3/17 | **Annual Review prep** — Forte Feedback先に完了させる | 未着手 |
| 16 | ✅ | **/daily Skill作成** — キャリーオーバー・ブレイクダウン・構造継承ルール含む | 完了(3/12) |
| 17 | 今週 | **Coke Rufus** — Billy返信 + Rufus team待ち + Alleyフォローアップ | 進行中 |

## 重要な判断ログ

- **weekly-workflow-setup から分離**（3/3）
- **Daily Log 作成フロー確立**（3/3）
- **Asana作業時間トラッキング導入**（3/7）
- **タスク数制限**（3/7）: 1日5件以下
- **WorkLog作成ワークフロー正式定義**（3/9）
- **WBR隔週スケジュール調査**（3/9）
- **Outlookリマインダー体系**（3/9）
- **外部アクション承認ルール**（3/9）
- **チームメンバーalias保存**（3/9）
- **キャリーオーバールール適用確認**（3/10）
- **CocaCola Pipeline ≠ World Cup**（3/11）
- **/daily Skill作成**（3/12）: 全自動実行+Briefing+対話。Notion書き込みまで自動化し、その後対話で精査
- **構造継承ルール追加**（3/12）: キャリーオーバー時に昨日のタスク構造を活かしてマージ。フラット化禁止
- **タスクブレイクダウン必須化**（3/12）: 親タスク+サブタスク階層。動詞で始める具体的アクション

## 関連トピック

- `2026-02-23_weekly-workflow-setup` — 設計・構築記録（完了・前身トピック）
- `2026-02-25_tex-survey-analysis` — Survey 分析（サマライズ待ち）
- `2026-02-26_tex-prime-video-sse-initiative` — SSE Initiative
- `2026-02-27_au-pes-tech-check` — AU PES Tech Check（サマリードック3/12完了）
- `2026-02-26_cat-decoder-tech-case-study` — Cat Decoder（Croc Awards）
- `2026-03-06_bil-op1-planning-fy27` — OP1 FY27（TEX OP1 3/16期限）
- `2026-03-07_halfpipe-ivs-deprecation` — Halfpipe IVS Deprecation
- `2026-03-08_halfpipe-deprecation` — Halfpipe全体状況（APAC POC、IVS進行中）
- `2026-03-09_tex-prime-video-live-sports-api-discovery` — PV Live Sports API（Biz Justification更新済み）
- `2026-03-09_tex-op1-fy27-goals` — TEX OP1 FY27 Goals（3/16期限）
