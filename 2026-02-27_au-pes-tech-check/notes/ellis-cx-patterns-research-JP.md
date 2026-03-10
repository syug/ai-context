# Ellis Blueprint CX Constructs — AU PES Tech Check 追加リサーチ

**Date:** 2026-03-04
**背景:** AU PES Tech Check V2 レビュー中の追加調査

---

## 概要

本ドキュメントは、Amazon の Ellis Blueprint CX Constructs の全体像、LWA と Amazon Pay の関係性、および AU Prime Early Screenings (PES) プロジェクトへの示唆をまとめたリサーチノートである。

> **重要な補足（2026-03-10）：** PES AU の文脈では、Event Cinemas が自前でチケット管理を行う前提なら、Ellis は必須ではない。最低限必要なのは LWA による Prime 認証（`prime:benefit_status`）のみ。Ellis は Amazon 側でオファーライフサイクル（在庫、利用上限、重複防止等）を管理したい場合のオプションである。以下の Ellis パターンを読む際は、この区別を念頭に置くこと。

## Ellis CX パターン比較

Ellis は 5 つの OOB (Out-of-the-Box) Blueprint CX Construct を提供している：

| # | パターン | 統合の深さ | 3P側のAPI統合 | 代表パートナー | ローンチ |
|---|---------|-----------|-------------|--------------|---------|
| 1 | Online Offers | 深い | LWA + Ellis API | Grubhub+, Calm, Deliveroo | 2021/7 |
| 2 | Partner Promotions | 最も軽い | 不要（プロモコード/URL配布） | LinkedIn, Uber | 2022/5 |
| 3 | Prime Offer Code | 軽い〜中程度 | Ellis API のみ (Transactional) または LWA + Ellis API (Account Linking) | **Odeon Cinemas (UK)**, Peet's Coffee | 2023/12 |
| 4 | Pre-Verification | 中程度 | LWA + Ellis API | UNiDAYS | 2022/5 |
| 5 | Embedded Store | 最も深い | Amazon Pay + Ellis API + 独自エンドポイント | **Grubhub** | 2024/5 |

## LWA と Amazon Pay — 依存関係なし

**LWA (Login with Amazon)** と **Amazon Pay** は完全に独立したサービスである。

- LWA = OAuth 2.0 ベースの認証サービス（Identity Services チーム管轄）
- Amazon Pay = 決済サービス
- Amazon Pay が LWA を認証基盤として利用していた（逆ではない）
- 2017年頃の「LwA Decoupling」プロジェクトでさらに分離が進められた

### パターン別 Amazon Pay 必要性

| パターン | 決済の場所 | Amazon Pay |
|---------|-----------|------------|
| Online Offers | 3Pサイト（3Pの決済） | 不要 |
| Partner Promotions | 3Pサイト（3Pの決済） | 不要 |
| Prime Offer Code | 物理店舗 or 3Pサイト | 不要 |
| Pre-Verification | Amazonサイト（Primeサブスク） | 不要 |
| **Embedded Store** | **Amazonアプリ内** | **必須** |

**Amazon Pay が必要なのは Embedded Store CX のみ。**

## Embedded Store CX（Grubhub）詳細

### 概要

Embedded Store CX は、3P の Web 体験を Amazon アプリ（mShop / Amazon.com）の中に丸ごと埋め込むパターン。技術的には iOS の Safari View Controller (SVC) と Android の Chrome Custom Tab (CCT) を使い、Amazon アプリ内に 3P の Web をオーバーレイ表示する。

### ユーザーフロー

1. Amazon アプリで「Dining/Restaurants」を選択
2. Ellis 共同ブランディングページで Prime 特典を説明
3. **Amazon Pay SSW（Sign-in & Setup Wallet）** 同意画面：
   - Prime ステータス共有の同意
   - Amazon アカウント情報共有の同意
   - Amazon Pay ウォレットのセットアップ（決済手段の設定）
   - SSO により Amazon アプリにログイン済みなら追加認証不要
4. Grubhub が Amazon Pay API でバイヤー情報を取得
5. Grubhub が Ellis Benefits Discovery API で Prime 資格を確認
6. Grubhub がアカウントを自動作成、オファーを有効化
7. 顧客がレストランを閲覧、メニューを選択
8. **Amazon Pay でチェックアウト** — Amazon ウォレットの既存決済手段を使用
9. 注文追跡も Amazon アプリ内で可能

### なぜ Amazon Pay が必須か

Embedded Store CX における Amazon Pay は単なる決済手段ではなく、**認証 + 同意 + ウォレット + 決済** を一本化する統合レイヤーである：

- **唯一のパターン**: 顧客が Amazon アプリから離れずに 3P 商品を「購入」する
- **SSW 統合**: 元々は LWA 同意 → Saved Wallet 同意の 2 ステップだったがドロップが発生、1 画面に統合
- **Saved Wallet**: 2 回目以降は Amazon の決済手段がデフォルトとして自動適用

## PES への示唆

### 重要な発見: Odeon Cinemas (UK) の先行事例

**Odeon Cinemas（UK の映画館チェーン）が 2023 年 12 月に Prime Offer Code (Transactional) でローンチ済み。** 映画館 + Prime 統合の直接的な先行事例。

### パターン別 PES 適合性

| パターン | PES 適合性 | 理由 |
|---------|-----------|------|
| **Prime Offer Code (Transactional)** | **最高** | Odeon（UK 映画館）が直接先例。毎回 Prime 資格確認。バーコード/コードで POS 対応。LWA 不要。4-6 週。 |
| LWA + PrimePass (Fandango model) | 高い | US PES で実績あり。ただし統合コストは Offer Code より高い。 |
| Embedded Store | 低い | 統合コスト極大。PES には過剰。AU では Amazon Pay 未対応のため使用不可。 |

### V2 レポートの推奨順位への影響

V2 レポートの現在の推奨:
- Priority 1: LWA + Prime Ellis (Fandango model)
- Priority 2: Ellis Prime Offer Code CX (ODEON model)

**Odeon Cinemas が映画館の直接先例**であり、統合コストも低く期間も短いことから、推奨順位の再検討が必要な可能性がある。

### V2 レポートの修正箇所

1. **Task 2 制約テーブル**（Impact 列）:
   - 現行: "Cannot directly replicate the US Fandango model"
   - 修正案: "Ellis Embedded Store CX (Grubhub model) は AU で使用不可。推奨アプローチ（LWA + PrimePass / Offer Code CX）には影響しない。"

2. **Key Risks セクション**:
   - 現行: "Amazon Pay is not available in AU, limiting certain integration patterns"
   - 修正案: "Amazon Pay is not available in AU, preventing use of the Ellis Embedded Store CX (Grubhub model). Does NOT affect the recommended approaches."

## ソース

- [Ellis Blueprint CX Constructs](https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/BlueprintCXConstructs/)
- [Ellis GES (Grubhub Embedded Store) 設計](https://w.amazon.com/bin/view/PrimeTeam/Ellis/Projects/GES/)
- [Amazon Pay Prime Ellis Program](https://w.amazon.com/bin/view/AmazonPay/PrimeEllisProgram/)
- [Ellis メイン Wiki](https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/)
- [LWA Products](https://w.amazon.com/bin/view/IdentityServices/Products/LWA/)
- kellypru DM (2026-03-03) — US PES は LWA + Prime Ellis を使用
