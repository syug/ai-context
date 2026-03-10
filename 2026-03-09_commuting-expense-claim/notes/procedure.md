# Commuting Expense Claim Procedure (Sydney Flexible Commuter)

## Overview

Amazon Sydney勤務の通勤交通費（Flexible Commuter）を毎月精算する手順。
Transport for NSWのコンタクトレス決済履歴を元に、平日分のみMyBenefitsで請求する。

## Step 1: Transport利用履歴のダウンロード

1. https://transportnsw.info/account/activity にアクセス
2. 対象月の期間を指定（例: Feb 01 - Feb 28）
3. PDF or CSV をダウンロード
4. 保存先: `~/Library/CloudStorage/GoogleDrive-syugo3hz@gmail.com/My Drive/A/Expense/Commuting/transport-YYYYMM.pdf`

### PDFの読み方
- "Contactless Payment - ending in 7175 - Adult" セクションごとに日別合計が表示される
- 同一日に複数トリップ（バス、電車、ライトレールなど）がある場合、セクション内に全て含まれる
- セクション右上の金額が**日別合計**（= 請求額）

## Step 2: MyBenefitsにログイン

1. https://mybenefits.corp.amazon.com/ にアクセス
2. Amazon社内認証でログイン

## Step 3: クレーム入力

1. https://ssl3.prod-darwin.com/RewardCentre/M/RC#/SpendingAccount/ClaimHistory にアクセス
2. 各平日について1件ずつクレームを作成:
   - **Type of Claim**: `{Month} {Year} Flexible Commuter`（例: `February 2026 Flexible Commuter`）
   - **Receipt Date**: 利用日（DD/MM/YYYY）
   - **Receipt Amount**: Transport PDFの日別合計
   - **Claim Amount**: Receipt Amountと同額

## Step 4: 照合チェック

クレーム入力後、以下を確認する:
1. **日付の一致**: クレーム日 = PDFの利用日（平日のみ）
2. **金額の一致**: クレーム額 = PDFの日別合計（1セント単位まで）
3. **除外確認**: 土日の利用が含まれていないこと
4. **欠損確認**: PDFにある平日の利用が全てクレームされていること

## Rules

- **平日のみ請求**: 土日の利用は個人利用として除外
- **利用がない平日は請求しない**: オフィスに行かなかった日
- **金額はPDF日別合計と完全一致**: 端数まで合わせる
- **レシート添付**: Transport PDFをレシートとして添付（1つのPDFで全日分カバー）

## 実績

| 月 | 請求日数 | 合計額 | 備考 |
|----|---------|--------|------|
| 2026-02 | 17日 | AUD 102.96 | 06/02を$6.60→$4.62に修正 |

## Tips

- Transport PDFは月末から48時間後に最終確定される（それ以前はトランザクションが反映されない可能性あり）
- PDFのFare列とAmount列が異なる場合がある（Discount適用時）。**Amount列**を使用する
- 乗り継ぎ割引（transfer discount）がある場合、個別トリップの合計と日別合計が異なることがある → 日別合計を使う
