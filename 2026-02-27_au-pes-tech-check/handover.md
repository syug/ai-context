# Handover Document
**Topic:** AU Prime Early Screenings Tech Check — Event Cinemas パートナーシップ技術評価
**Date:** 2026-03-12
**Status:** 進行中（Tech Check 完了・サマリードック Matt にシェア済み・Matt が Hannah Hill にリーチアウト予定）

---

## 背景

AU BIL チーム（Matt Bryant/mjlb, Chris Wilson/wilsnup）から DT（Shugo Saito）にアサインされた Tech Check チケット。Prime Early Screenings (PES) をオーストラリアで Event Cinemas と実施するための技術評価。Asana: ENT | AU | Prime Early Screenings | Australia Pilot（TEX Global Intake, T2, DT Resource）。

PES は US で Fandango と提携して運用されているプログラムで、Prime 会員に映画の先行上映チケットを提供する。Fandango が AU で運営していないため、Event Cinemas を代替パートナーとして検討中。

## 現在の状況

### Tech Check レポート — V5（3/11）

- V1（2/27）→ V2（3/4）→ V3（3/10 AM）→ V4（3/10 PM）→ **V5（3/11）**
- **V5 の主な変更:**
  - PBS Onboarding Wiki で「Third Party Integration should go through Prime Ellis」を発見
  - LWA Only（V4 の Priority 0）を削除 — 3P には Prime Ellis 経由が必須
  - LWA + Prime Ellis を Priority 0（Primary）に昇格
  - ODEON モデルを Priority 1 に
  - PBS Onboarding Wiki / Products Using LWA Wiki をソースに追加
  - PBS リージョンエンドポイント（NA/EU/FE/CN、AU は FE 経由の可能性大）
  - Action Item #3（推奨順位見直し）→ Complete

### Matt Sync 完了（3/11）

- Tech Check 結果を共有。スクリプト v2 を使用
- **結果:** Matt が Hannah Hill にリーチアウトする
- Hannah へのメッセージドラフト（EN）も準備済み（グループ DM: Shugo + Matt + Hannah）

### サマリードック作成・シェア（3/12）

- Summary EN/JP を Matt 共有用にリファイン
  - ODEON モデル（代替案）を削除（方法不明、US ケースと異なり、問い合わせ先不明）
  - Bullseye を削除（ノイズ）
  - Action Items セクション削除
  - バージョン表記削除（シェア用ドキュメントのため）
  - 推奨アプローチをテーブルから1行に簡素化: 「LWA（Login with Amazon）」
  - 要確認事項: US PES で踏んだステップの全体像 / Prime Ellis・LWA チームとのエンゲージ方法
  - Task 詳細セクション追加（Task 1/2/3 の要点）
  - 脚注スタイル（*）で補足情報を整理
- **Asana（TEX Global Intake チケット）にコメント + EN サマリー添付済み**
- **Slack ドラフト作成済み（Matt DM、未送信）**
- ファイルリネーム: `_EN` サフィックス削除、EN がデフォルト

### PBS Onboarding Wiki の発見（3/11）

- https://w.amazon.com/bin/view/PBS/Onboarding/
- 「Third Party Integration should go through Prime Ellis」と明記
- PrimePass (`prime:benefit_status`) のコード例あり
- PBS エンドポイント: NA (prime.amazon.com) / EU (prime.amazon.eu) / FE (prime.amazon.co.jp) / CN (prime.amazon.cn)
- AU 専用エンドポイントなし、FE 経由の可能性大

### 追加で発見した内部 Wiki

- Products Using LWA: https://w.amazon.com/bin/view/IdentityServices/3P_Authz/Products_Using_LWA/
  - PrimePass: "allows select third parties access to the customer's Amazon Prime benefit status"
  - Product Domain: `prime`, Scope: `prime:benefit_status`
- LWA Prime Upsell: https://w.amazon.com/bin/view/IdentityServices/LWA/Projects/LWA_Prime_UpSell/
  - `prime:benefit_status` スコープの存在を確認

### Hannah Hill プロフィール（PhoneTool）

- Sr. Solutions Manager, BIL-VAR
- Virtual Location - California → US Pacific Time (PT)
- Manager: lebrooke
- L6, Total tenure 4+ years

### Kelly Prudente (kellypru) との DM — 完了（3/3）

- Kelly 原文: "the integration worked my SM (@hannahnl) was pretty key in leading this, i would reach out to her to understand all of the steps taken, how to engage the prime ellis team + LWA team"
- Fandango/Atom は LWA + Prime Ellis で統合
- LWA scope `prime:benefit_status` で Prime 会員判定
- Hannah Hill がプロセスをリード

### Ads Security — gulsunit gut check

- SHA256 Critical 2件の判定妥当性のみ Slack DM で非同期確認
- 3/10 DM 送信済み、3/12 時点で返信なし

## 成果物一覧

```
ai-context/2026-02-27_au-pes-tech-check/
├── handover.md                              ← 本ファイル
├── history/
│   ├── 2026-02-27_handover.md
│   ├── 2026-03-02_handover.md
│   ├── 2026-03-03_handover.md
│   ├── 2026-03-10_handover.md
│   └── 2026-03-10_2_handover.md
├── artifacts/
│   ├── AU_PES_TechCheck_Report.md           ← Tech Check レポート V5（EN、デフォルト）
│   ├── AU_PES_TechCheck_Report_JP.md        ← Tech Check レポート V5（JP）
│   ├── AU_PES_TechCheck_Summary.md          ← サマリー（EN、Matt シェア用）
│   └── AU_PES_TechCheck_Summary_JP.md       ← サマリー（JP、レビュー用）
└── notes/
    ├── verification-report.md
    ├── ellis-cx-patterns-research-EN.md
    └── ellis-cx-patterns-research-JP.md

OneDrive: ENT | AU | Prime Early Screenings | Australia Pilot/
├── Amazon_Prime_Preview_Partner_API_Spec.pdf
├── Amazon_Prime_Preview_Partner_API_Spec.docx
├── Event Cinemas Ticket Partner Customer Journey.pdf
├── Wicked_CLP_Screenshot.png
└── Smith Research/
    ├── SUMMARY - ENT | AU | Prime Early Screenings | Australia Pilot.pdf
    ├── TASK1 - US Prime Early Screenings — ユーザーフロー & 技術詳細レビュー.pdf
    ├── Task2_AU_Prime_Auth_Feasibility.pdf
    ├── Task3_EventCinemas_GutCheck.pdf
    └── AU_PES_TechCheck_Final.pdf
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|----------|-----------|
| 1 | — | gulsunit SHA256 Critical 判定 gut check | 🔄 DM 返信待ち（3/10〜） |
| 2 | 3/11 | Matt Sync で Tech Check 結果共有 | ✅ 完了（3/11） |
| 3 | — | 推奨順位の見直し | ✅ 完了（V5）— PBS Wiki で確定 |
| 4 | — | サマリードック作成 → Matt にシェア | ✅ 完了（3/12） |
| 5 | — | Matt が Hannah Hill にリーチアウト | ⬜ Matt 対応中 |
| 6 | — | Hannah 経由: US PES のステップ全体像 + Prime Ellis/LWA チームとのエンゲージ方法 | ⬜ #5 待ち |
| 7 | — | Event Cinemas に LWA モデルを逆提案 | ⬜ #6 後 |
| 8 | — | Full Scope 提出検討 | ⬜ #7 後 |

## 重要な判断ログ

### Event Cinemas SHA256 提案 → 不採用
- Critical 1: 秘密鍵の外部共有（Amazon 鍵管理ポリシー抵触）
- Critical 2: MemberId の PII 露出（PrimePass は Directed ID で保護）
- Event Cinemas 自体は却下しない → LWA ベースの統合への切替を逆提案

### 推奨アプローチの変遷（V1 → V5）
- V1: LWA + PrimePass / Ellis Offer Code CX を別選択肢
- V2: Kelly 証言で「LWA + Prime Ellis」にリネーム
- V3: Ellis 能力 vs 事実の区別を明記
- V4: LWA Only を Priority 0 として追加
- **V5: PBS Wiki で「3P は Prime Ellis 経由」を発見 → LWA Only 削除、LWA + Prime Ellis を Primary に確定**

### サマリードックのリファイン方針（3/12）
- Matt 共有用にシンプル化: ODEON・Bullseye・Action Items・バージョン表記を削除
- 推奨は LWA の1行のみ。Prime Ellis の要否は Hannah に確認
- Task 詳細セクションで根拠を補足、脚注スタイルで内部情報を整理
- EN がデフォルト（`_EN` サフィックス削除）、JP はレビュー用

### Hannah Hill への連絡方針（3/11 Matt Sync で決定）
- Matt が Hannah にリーチアウトする
- Hannah への DM ドラフト（EN）も準備済み（Shugo + Matt のグループ DM）
- 確認事項: US PES で踏んだステップの全体像 / Prime Ellis・LWA チームとのエンゲージ方法

### PBS Wiki の発見と影響（3/11）
- PBS Onboarding Wiki: 「Third Party Integration should go through Prime Ellis」
- LWA Only は 3P にサポートされたパスではない
- LWA + Prime Ellis が公式ドキュメントと Kelly 証言の両方で裏付け

## 重要リンク

### ARC 過去事例
- Wicked PES: https://console.harmony.a2z.com/arc/#/campaigns/universal-pictures-wicked-o
- Superman PES: https://console.harmony.a2z.com/arc/#/campaigns/anyone-can-be-super-warner-b

### Asana
- TEX Global Intake: https://app.asana.com/1/8442528107068/project/1212641864720082/task/1213411601791772?focus=true
- BIL-E Intake Task: https://app.asana.com/1/8442528107068/task/1213466153419679

### 社内 Wiki
- PES Wiki: https://w.amazon.com/bin/view/PrimeEarlyScreenings/
- Ellis Wiki: https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/
- Ellis Blueprint CX Constructs: https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/BlueprintCXConstructs/
- PBS Onboarding Wiki: https://w.amazon.com/bin/view/PBS/Onboarding/
- Products Using LWA: https://w.amazon.com/bin/view/IdentityServices/3P_Authz/Products_Using_LWA/
- LWA 3P Authorization: https://w.amazon.com/bin/view/IdentityServices/3PAuthZ/

### 開発者リソース
- LWA Developer Docs: https://developer.amazon.com/docs/login-with-amazon/web-docs.html
- LWA Scopes Portal: https://console.harmony.a2z.com/lwa-tools-portal/scopes

## 関連トピック

- `2026-02-23_sse-prototypes` — BIL-TEX AU デモ環境（同じ AU BIL コンテキスト）
- `2026-02-26_cat-decoder-tech-case-study` — Mars Dine CDK コード解析（JWT HS256 比較に使用）
