# Handover Document
**Topic:** AU Prime Early Screenings Tech Check — Event Cinemas パートナーシップ技術評価
**Date:** 2026-03-10
**Status:** 進行中（Tech Check 完了・レポート V3 最終化済み・Matt Sync 3/11 予定・Hannah Hill 連絡は Matt に委任提案予定）

---

## 背景

AU BIL チーム（Matt Bryant/mjlb, Chris Wilson/wilsnup）から DT（Shugo Saito）にアサインされた Tech Check チケット。Prime Early Screenings (PES) をオーストラリアで Event Cinemas と実施するための技術評価。Asana: ENT | AU | Prime Early Screenings | Australia Pilot（TEX Global Intake, T2, DT Resource）。

PES は US で Fandango と提携して運用されているプログラムで、Prime 会員に映画の先行上映チケットを提供する。Fandango が AU で運営していないため、Event Cinemas を代替パートナーとして検討中。

プロジェクトは非常に初期段階で、IO 未署名のプロアクティブな探索。Event Cinemas から Amazon との API 連携に関する技術プロポーザルを受け取った段階。

## 現在の状況

### Tech Check レポート — V3 最終化完了（3/10）

- V1（2/27）: 初版 EN/JP
- V2（3/4）: Kelly バリデーション + 構造改善
- **V3（3/10）: 本セッションでの最終化。主な変更:**
  - V1/V2 ファイル統合（バージョニング廃止、1ファイルに）
  - Amazon Pay 記述修正（LWA と独立、推奨アプローチに不要）
  - Ellis 能力 vs US PES 実際の利用範囲の区別を注記で明示
  - アクションアイテムをスコープ内/外の2テーブルに分割
  - Hannah Hill をエントリーポイントとして再構成（サブアイテム 6a-6d）
  - Prime Ellis チーム + LWA チーム両方へのエンゲージが必要と明記（Kelly 証言）
  - Bullseye API を「AU 対応済み」に更新
  - gulsunit を DM gut check に切替（フルレビュー不要）
  - Matt Sync 用 Summary 版 EN/JP を新規作成
- Ellis CX リサーチノート「6つ」→「5つ」訂正済み

### ARC 過去事例（US PES キャンペーン）— 3/10 発見

2件の Lighthouse キャンペーンを ARC で確認:

1. **Wicked "Oz Casts a Spell on Amazon"** (2024/10-12, Universal Pictures)
   - ARC: `https://console.harmony.a2z.com/arc/#/campaigns/universal-pictures-wicked-o`
   - $10M media spend, C0, Lighthouse
   - **Hannah Hill (hannahnl) が Senior SM としてチームに参加** — Kelly 証言の裏付け
   - **Kelly (kellypru) も DT として参加**
   - PES フロー: OzOnAmazon.com (Brand Store) → Fandango 経由チケット購入
   - 結果: 128K チケット販売（目標 100K の +28%）、$2.5M box office
   - 「first-time partnership and API integration with Fandango」と明記
   - ロケール: US, CA, AU, UK, IT, ES, DE, FR

2. **Superman "Anyone Can Be Super"** (2025/6, Warner Bros.)
   - ARC: `https://console.harmony.a2z.com/arc/#/campaigns/anyone-can-be-super-warner-b`
   - $5M media spend, C1, Lighthouse
   - PES フロー: amazon.com/superman (Brand Store) → Fandango 経由チケット購入
   - 初の Fandango Round-Up 統合（端数寄付）
   - 結果: 初日 144K チケット販売（$2.9M box office）、74% booking rate

**US PES ユーザーフロー（ARC から再構成）:**
1. 認知: H1 / Fire TV / Alexa / Amazon Live / TNF / Twitch 等で告知
2. ランディング: Brand Store（中央ハブ）— チケット、トレイラー、グッズ集約
3. チケット CTA: Brand Store 上の PES リンクをクリック
4. 3P 遷移: Fandango サイトに遷移 → LWA 認証（`prime:benefit_status`）
5. チケット発券: Fandango 上で座席選択・購入（Fandango 決済）

> **注:** LWA 認証の正確なタイミング（遷移時 or Fandango サイト内）は ARC に記載なし。Hannah Hill に要確認。

### Kelly Prudente (kellypru) との DM — 完了（3/3）

- **初回 DM（2/27）**: PES について質問 + フォローアップ（3/3）
- **Kelly 回答（3/3）**: Fandango/Atom は **LWA + Prime Ellis** で統合。**Prime Ellis チームと LWA チームの両方**と密接に連携
- LWA scope `prime:benefit_status` で Prime 会員判定
- **Hannah Hill (hannahnl)** がリーダー — 「彼女に連絡して全ステップを理解すべき」
- US Telent の amazon.com チケット販売企画は保留中

### LWA / Ellis / Amazon Pay の関係性整理

- **LWA（Identity Services）**: OAuth 2.0 認証 + `prime:benefit_status` で Prime 判定。AU 対応済み
- **Prime Ellis**: オフ Amazon パートナーシップ管理 — オファーライフサイクル、Verify/Redeem API。AU 対応は未確認
- **Amazon Pay**: 決済サービス。LWA とは独立。AU 未対応だが推奨アプローチには不要（Embedded Store CX のみ影響）
- **Ellis の能力 vs US PES の実態**: レポートの Ellis 機能記述は Wiki ドキュメント（Tier 2）ベース。US PES が実際にどこまで Ellis を使い、どこまで Fandango が自前実装かは未確認 — Hannah Hill に要確認

### Ads Security — gulsunit gut check

- フルセキュリティレビュー不要に方針変更（推奨が Prime Ellis 経由に確定したため）
- SHA256 Critical 2件の判定妥当性のみ Slack DM で非同期確認に切替
- 3/10 DM 送信済み、返信待ち

### Matt Sync 準備（3/11 予定）

- Summary 版レポート EN/JP 作成済み
- **Hannah Hill への連絡は Matt（SM）から行うことを提案予定** — SM-to-SM が自然、ビジネス判断を含むため
- 日英スクリプト準備済み（下記参照）

## Matt Sync 用スクリプト

### 日本語版

> Tech Check としては結論出てて、Event Cinemas の SHA256 提案は不採用、代わりに LWA + Prime Ellis か ODEON model を推奨。US 側で Kelly (DT) に裏取りも済んでる。
>
> で、次のステップなんだけど、Kelly から Hannah Hill っていう US TelEnt の SM を紹介されてて、Wicked と Superman の PES を直接リードした人。Ellis チームや LWA チームとのエンゲージ方法は全部彼女が知ってる。
>
> ここから先は SM 同士で話した方がスムーズだと思うんだよね — Hannah も SM だし、AU でやるかどうかのビジネス判断も含むから。Matt から Hannah に連絡取ってもらえると一番早いかなと。Kelly の名前出せば話は通ると思う。
>
> 俺の方では Tech Check レポートと、Hannah に聞くべき技術的な確認事項リストをまとめてあるから、連絡する時にそのまま共有してもらえればいいようにしてある。必要なら同席もするよ。

### English version

> Tech Check is done. Event Cinemas' SHA256 approach won't work — two Critical security issues. But we have good alternatives: LWA + Prime Ellis, or the ODEON model. I checked with Kelly on the US side and she confirmed this is how Fandango did it.
>
> Next step — Kelly pointed me to Hannah Hill, SM on US TelEnt. She ran the Fandango PES stuff for Wicked and Superman. She knows how to get the Prime Ellis team and LWA team involved.
>
> I think it makes sense for you to reach out to her since she's an SM too, and the next steps are more about how we want to move forward with AU than technical details. If you mention Kelly's name, she'll know what it's about.
>
> I've got the report and a list of questions ready — you can just share those with her. I can also join the call if you want.

## 成果物一覧

```
ai-context/2026-02-27_au-pes-tech-check/
├── handover.md                                  ← 本ファイル
├── history/
│   ├── 2026-02-27_handover.md                   ← 旧バージョン（圧縮アーカイブ）
│   ├── 2026-03-02_handover.md
│   ├── 2026-03-03_handover.md
│   └── 2026-03-10_handover.md                   ← 旧バージョン（圧縮アーカイブ）
├── artifacts/
│   ├── AU_PES_TechCheck_Report_EN.md            ← Tech Check レポート V3（英語版）
│   ├── AU_PES_TechCheck_Report_JP.md            ← Tech Check レポート V3（日本語版）
│   ├── AU_PES_TechCheck_Summary_EN.md           ← Matt Sync 用 Summary（英語版）
│   └── AU_PES_TechCheck_Summary_JP.md           ← Matt Sync 用 Summary（日本語版）
└── notes/
    ├── verification-report.md                   ← Slack/Quip/Wiki 検証レポート
    ├── ellis-cx-patterns-research-EN.md         ← Ellis CX リサーチ（英語版）
    └── ellis-cx-patterns-research-JP.md         ← Ellis CX リサーチ（日本語版）

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

### 依頼スコープ内（Tech Check として必要）

| # | アクション | ステータス |
|---|----------|-----------|
| 1 | gulsunit SHA256 Critical 判定 gut check | 🔄 DM 返信待ち（3/10） |
| 2 | mjlb への Tech Check 結果共有（3/11 Sync） | ⬜ 未着手 |
| 3 | 推奨順位の見直し（Fandango model vs ODEON model） | ⬜ 未着手 |
| 4 | Bullseye API AU 対応 | ✅ AU 対応済みと判断。Full Scope で要検証 |
| 5 | kellypru に US PES 詳細確認 | ✅ 完了（3/3） |
| 6 | レポート V1/V2 統合 + Amazon Pay 修正 + Ellis 5パターン訂正 | ✅ 完了（3/10） |
| 7 | Ellis 能力 vs 事実の区別明記（V3 注記） | ✅ 完了（3/10） |
| 8 | アクションアイテムのスコープ内/外分割 | ✅ 完了（3/10） |
| 9 | Summary 版 EN/JP 作成 | ✅ 完了（3/10） |

### 依頼スコープ外（次フェーズ / Full Scope）

| # | アクション | ステータス / 備考 |
|---|----------|-------------------|
| 10 | Hannah Hill (hannahnl) に連絡 — **Matt（SM）から連絡を提案予定** | ⬜ 3/11 Sync で Matt に委任提案 |
| 10a | Hannah 経由: US PES エンゲージメントプロセス + learnings（Prime Ellis チーム + LWA チーム両方） | ⬜ |
| 10b | Hannah 経由: US PES の Ellis 機能実際の利用範囲（Verify/Redeem, 在庫管理, 重複防止） | ⬜ |
| 10c | Hannah 経由: Ellis AU 対応 → Ellis チーム（Joshua Huang）に繋いでもらう | ⬜ |
| 10d | Hannah 経由: PrimePass (`prime:benefit_status`) AU 対応 → Identity Services に繋いでもらう | ⬜ |
| 11 | Event Cinemas に Ellis/LWA モデルを逆提案 | ⬜ #10c & #10d 確認後 |
| 12 | Full Scope 提出検討 | ⬜ 上記確認後 |
| 13 | Quip AU BIL Team WIP の PES セクション確認 | ⬜ |

## 重要な判断ログ

### Event Cinemas SHA256 提案 → 不採用
- Critical 1: 秘密鍵の外部共有（Amazon 鍵管理ポリシー抵触）
- Critical 2: MemberId の PII 露出（PrimePass は Directed ID で保護）
- Event Cinemas 自体は却下しない → LWA/Ellis モデルへの切替を逆提案

### 推奨アプローチの変遷（V1 → V2 → V3）
- V1: LWA + PrimePass（第一）、Ellis Offer Code CX（第二）を別選択肢として提示
- V2: Kelly 証言で PrimePass が Prime Ellis の一部と判明。第一推奨を「LWA + Prime Ellis」にリネーム
- V3: Ellis 機能記述が「能力ベース」（Wiki）vs「事実ベース」（Kelly 証言）の区別を明記。US PES が Ellis をどこまで使っているかは未確認

### LWA / Ellis / Amazon Pay の関係性（3/5-3/10 確定）
- LWA = 認証（「誰？Prime？」）、Ellis = オファー管理（「何のオファーを、どう届けるか」）
- Amazon Pay は LWA と完全に独立。推奨アプローチに不要（Embedded Store CX のみ影響）
- Fandango/PES は Ellis Blueprint CX Wiki に未掲載 → カスタム統合

### Hannah Hill への連絡は Matt（SM）に委任提案（3/10 判断）
- Hannah Hill = SM、Matt = SM。SM-to-SM が自然なチャネル
- 次ステップはビジネス判断（AU でやるか、Full Scope に進むか）を含む → DT スコープ外
- DT 側でレポート + 確認事項リストを用意済み。Matt がそのまま共有可能
- 必要なら同席可

### Sunit gut check の方針変更（3/10）
- 推奨が Prime Ellis 経由に確定 → Event Cinemas SHA256 のフルレビュー不要
- SHA256 Critical 2件の判定妥当性のみ DM で非同期確認に切替

### Bullseye API（3/10 完了）
- AU 対応済みと判断。Full Scope へ進む場合はプロトタイプで要検証

## 重要リンク

### ARC 過去事例
- Wicked PES: https://console.harmony.a2z.com/arc/#/campaigns/universal-pictures-wicked-o
- Superman PES: https://console.harmony.a2z.com/arc/#/campaigns/anyone-can-be-super-warner-b

### Asana
- TEX Global Intake: https://app.asana.com/1/8442528107068/project/1212641864720082/task/1213411601791772?focus=true
- BIL-E Intake Task: https://app.asana.com/1/8442528107068/task/1213466153419679
- M&M's Spotto ASR (参考): https://app.asana.com/1/8442528107068/project/1199343345138382/task/1212335750973364

### 社内 Wiki
- PES Wiki: https://w.amazon.com/bin/view/PrimeEarlyScreenings/
- Ellis Wiki: https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/
- Ellis Blueprint CX Constructs: https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/BlueprintCXConstructs/
- Amazon Pay Prime Ellis Program: https://w.amazon.com/bin/view/AmazonPay/PrimeEllisProgram/
- LWA Products (PrimePass): https://w.amazon.com/bin/view/IdentityServices/Products/LWA/
- LWA 3P Authorization: https://w.amazon.com/bin/view/IdentityServices/3PAuthZ/
- BIL-E NA Wiki: https://w.amazon.com/bin/view/BIL-E/NA/
- AmazonAdsSecurity Wiki: https://w.amazon.com/bin/view/AmazonAdsSecurity/

### その他
- BIL-E NA Intake Form: https://form.asana.com/?k=yteEaKgwZq9qEZa3mNL-KQ&d=8442528107068
- AU BIL Team WIP: https://quip-amazon.com/DbiAAG32tGjS

## 関連トピック

- `2026-02-23_sse-prototypes` — BIL-TEX AU デモ環境（同じ AU BIL コンテキスト）
- `2026-02-26_cat-decoder-tech-case-study` — Mars Dine CDK コード解析（JWT HS256 比較に使用）
