# Weekly WorkLog 作成ワークフロー

## 手順

### Step 1: 先週の見直しと整理
- 先週のWorkLogを開く
- Weekly TODOs の完了チェック（済んだものを [x] に）
- Daily Log に記録漏れがないか確認
- **Notionページのコメント欄もチェックする** — 追加タスクや完了状況のメモがコメントに書かれていることがある
- Retrospective セクションを記入（Well done / Could be better / Issue / Action plan / Summary）

### Step 2: テンプレートからコピーして新規週を作成
- **TEMPLATE-WorkLog26** (Notion ID: `31015ecd-1a0d-8104-8bdb-e24359b886a5`) を複製する
- ページタイトルを `WorkLog26-MarDD` に変更（DDは月曜の日付）
- テンプレートの構造（セクション、トグル、フォーマット）は必ず維持する
- テンプレなしで白紙から作らない

### Step 3: 持ち越しタスクのマージ
- 先週の未完了タスクを新しい週にコピー
- 今週のカレンダー・Slack・メール・handoverアクションアイテムから新規タスクを追加
- **Weekly Routine Tasks（下記）を確認し、必要なものを Weekly TODOs に追加**
- This Week's Priority を設定（↑↑↑ / ↑↑ / ↑ / → の優先度ラベル）
- Key Meetings を更新
- **Priority ↔ Weekly TODOs ↔ Daily Log の整合性を確認**

## テンプレート構造（必須セクション）
- This Week's Priority
- Key Meetings
- Weekly TODOs
  - Work: Campaigns & Briefs
  - Work: Discovery & Prototype
  - Work: Team
  - Work: Individual
  - Work: Projects
  - Private
- Daily Log
- Backlogs
- What's up to Now（トグル）
- Retrospective（トグル）
  - Well done / Could be better / Issue / Action plan / Summary

## Weekly Routine Tasks

### 毎週月曜
- [ ] カレンダー週次確認 — 今週のMTG出欠決定
- [ ] AU BIL Team WIP (12:00)
- [ ] TEX APAC DT Weekly Huddle (13:00) — 主催
- [ ] Weekly Parc Check — 新着プロトタイプ確認、面白いものは AU WIP でシェア

### 毎週火曜
- [ ] Weekly Project Report → Mirko DM (Loop)

### 毎週木曜
- [ ] Prep for 1:1 w/Chris
- [ ] 1:1 w/Chris (14:15)

### 毎週金曜
- [ ] Slack 未読キャッチアップ
- [ ] Asana タスク棚卸し
- [ ] Daily<>Weekly 整合性同期
- [ ] WBR チェック — 今週開催された WBR ドキュメントを読む（下記スケジュール参照）

### 隔週（奇数週 = WBR Input 週）
- [ ] WBR Input（APAC/MENA）— 水曜までに Loop 記入
- [ ] WBR Read: TEX NA + WW TEX + EU/APAC/MENA — 木曜以降にチェック

### 隔週（偶数週 = BIL WBR 週）
- [ ] WBR Read: WW BIL — 火曜以降にチェック

### 月1回
- [ ] Prep for 1:1 w/Mirko

### 週次キャッチアップ（読み物）
- [ ] TEX EU Weekly Meeting 議事録チェック
- [ ] AU WIP 議事録チェック
- [ ] JP BIL Weekly 議事録チェック

---

## WBR 隔週スケジュール

全 WBR は隔週。奇数週と偶数週で交互に開催。

| WBR | 曜日 | ISO週 | 対象 |
|-----|------|-------|------|
| **TEX NA WBR** | 水曜 | 奇数 (W11,W13,W15...) | NA リージョン |
| **WW TEX WBR** | 木曜 | 奇数 (同上) | TEX 全体 |
| **TEX EU/APAC/MENA WBR** | 木曜 | 奇数 (同上) | EU/APAC/MENA |
| **WW BIL WBR** | 火曜 | 偶数 (W10,W12,W14...) | BIL 全体 |

**パターン:**
- **奇数週（W11, W13...）:** TEX NA (水) + WW TEX & EU/APAC/MENA (木) → WBR Input 週
- **偶数週（W10, W12...）:** WW BIL (火) → BIL WBR 週
- 結果: **毎週金曜に何らかの WBR をチェック可能**

**WBR Input 準備（奇数週のみ）:**
- Mirko の "Add APAC/MENA WBR Inputs" は奇数週水曜 18:00 AEDT
- ただし現在全てキャンセル状態 — 非同期で Loop に直接記入する運用

**WBR ドキュメント (OneDrive PDF):**
- `Team/1. TEX/QBR:MBR:WBR/WW BIL WBR.pdf`
- `Team/1. TEX/QBR:MBR:WBR/WW TEX WBR.pdf`
- `Team/1. TEX/QBR:MBR:WBR/TEX NA WBR.pdf`
- `Team/1. TEX/QBR:MBR:WBR/TEX EU_APAC_MENA WBR.pdf`

---

## 運用ルール
- Weekly TODOs = Single Source of Truth
- Daily Log は Weekly TODOs からの派生
- Backlogs = 今週やらないが忘れたくないもの
- 週末に Daily<>Weekly 整合性同期
- タスク数制限: 1日5件以下にコミット
- **Daily Log キャリーオーバールール**: 前日の未完了タスクを翌日にマージしたら、前日のリストからは削除する（重複を避け、最新の日にだけ残す）。完了済みタスクはそのまま前日に残す。一行一タスクを徹底し、インデントでグルーピングする。

## Notion 日付フォーマットルール
- **Daily Log の日付見出し**: `<mention-date start="YYYY-MM-DD"/>` を使う（プレーンテキストの `**YYYY-MM-DD**` は使わない）
- **Key Meetings / Daily Log の時刻付きエントリ**: `<mention-date start="YYYY-MM-DD" startTime="HH:MM" timeZone="Australia/Sydney"/>` を使う
- 例: `- [ ] <mention-date start="2026-03-12" startTime="14:15" timeZone="Australia/Sydney"/>: 1:1 w/Chris`
- `Mon 12:00` のような曜日+時刻のプレーンテキストは使わない

## Outlook カレンダーリマインダー

| タイトル | 曜日 | 時間 | 頻度 |
|---------|------|------|------|
| 📊 WBR Input: APAC/MENA — Odd Week | 水 | 8-9am | 隔週（奇数） |
| 📊 WBR Read: NA + TEX + EU/APAC — Odd Week | 木 | 8-9am | 隔週（奇数） |
| 📊 WBR Read: BIL — Even Week | 火 | 8-9am | 隔週（偶数） |
| 📋 Weekly Review: WBR + Slack + Asana | 金 | 8-9am | 毎週 |

全て Free 表示、Descriptionに WBR Schedule + Loop リンク付き。

## Notion DB 情報
- **(A) Work Log**: `collection://0eaa9ab4-2968-4c9f-90f1-2b0da3b2f769`
- **Weekly log**: `collection://732cf7bf-7247-488c-89cc-ec220f0cb465`
- **TEMPLATE-WorkLog26**: `31015ecd-1a0d-8104-8bdb-e24359b886a5`
