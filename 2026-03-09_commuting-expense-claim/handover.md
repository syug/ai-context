# Handover Document
**Topic:** Sydney通勤交通費 Flexible Commuter 月次精算
**Date:** 2026-03-09
**Status:** 進行中（毎月継続）

---

## 背景

Amazon Sydneyオフィスへの通勤交通費をFlexible Commuter福利厚生で毎月精算する。Transport for NSWのコンタクトレス決済履歴（PDF）を元に、平日分のみMyBenefitsで請求する。

## 現在の状況

### 2026年2月分 — 精算完了

- 請求日数: 17日（平日のみ）
- 合計: AUD 102.96
- 提出日: 2026-03-08
- ステータス: Requested（承認待ち）
- 修正: 06/02を$6.60→$4.62に修正（バス+ライトレール=$4.62が正しかった）

### 精算手順

1. Transport NSW (https://transportnsw.info/account/activity) からPDFダウンロード
2. MyBenefits (https://mybenefits.corp.amazon.com/) にログイン
3. RewardCentre (https://ssl3.prod-darwin.com/RewardCentre/M/RC#/SpendingAccount/ClaimHistory) で平日分を1日ずつ入力
4. Claude Codeで日付・金額の照合チェック

詳細手順: `notes/procedure.md`

### 月別実績

| 月 | 日数 | 合計 | 備考 |
|----|------|------|------|
| 2026-02 | 17 | AUD 102.96 | 初回。06/02金額修正あり |

## 成果物一覧

```
2026-03-09_commuting-expense-claim/
├── notes/
│   └── procedure.md          # 精算手順書（詳細）
└── handover.md
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|----------|
| 1 | 毎月初め | 前月分のTransport PDFダウンロード+クレーム入力+照合 | 継続 |
| 2 | — | 2026-02分の承認確認 | 未完了 |

## 重要な判断ログ

- **平日のみ請求**: 土日の利用は個人利用。Flexible Commuterは通勤目的のみ
- **日別合計で請求**: トリップ個別ではなく、PDFの日別合計（Contactless Paymentセクション右上の金額）を使用
- **Amount列を使用**: Fare列ではなくAmount列（割引適用後）が正しい請求額
- **06/02の教訓**: 金額を手入力する際の転記ミスに注意。必ずPDFと照合チェックすること

## 関連トピック

- Memory: `~/.claude/projects/-Users-saitshug/memory/commuting-expense.md`
