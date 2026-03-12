# AU Prime Early Screenings -- Tech Check サマリー

**日付:** 2026-03-11
**作成者:** Shugo Saito (DT)
**インテーク:** ENT | AU | Prime Early Screenings | Australia Pilot (T2, DT Resource)

---

## エグゼクティブサマリー

### 目的

AU BIL チームが Prime Early Screenings (PES) をオーストラリアで Event Cinemas をチケット販売パートナーとして実施するにあたり、以下の3点を技術的に評価する。

1. **Task 1:** US PES のユーザーフロー & 技術詳細をレビューする
2. **Task 2:** AU での Prime 認証の実現可能性を検証する
3. **Task 3:** Event Cinemas の提案を技術的に "Gut Check" する

### タスク結果

| タスク | 判定 | サマリー |
|--------|------|---------|
| Task 1. US PES ユーザーフロー & 技術レビュー | **レビュー完了** | LWA ベースの統合 |
| Task 2. AU での Prime 認証の実現可能性 | **実現可能（要確認項目あり）** | LWA は AU（FE リージョン）で確認済み |
| Task 3. Event Cinemas 提案 | **不採用** | Critical リスク 2件: 秘密鍵の外部共有 + MemberId の PII 露出 |

### 推奨アプローチ

**LWA（Login with Amazon）** -- OAuth 2.0 標準、US PES で実績あり。

**要確認事項（Hannah Hill）:**

- US PES で踏んだステップの全体像
- Prime Ellis / LWA チームとのエンゲージ方法

### Next Steps

- **Hannah Hill (hannahnl) に連絡** -- US PES で踏んだステップの全体像と、Prime Ellis / LWA チームとのエンゲージ方法を確認する
- **Ads Security Engineer バリデーション** -- Sunit Guldas (gulsunit) に Task 3 の SHA256 Critical 判定の gut check を依頼（Slack DM 送信済み、返信待ち）

---

## Task 詳細

### Task 1: US PES ユーザーフロー & 技術レビュー

- US では Fandango をチケット販売パートナーとして運用
- ユーザーフロー: Brand Store → Fandango リダイレクト → LWA で Prime 認証 → チケット購入
- Fandango/Atom が Prime Ellis チームと LWA チームのサポートを受け、LWA 統合を行った
  - (*) DT 側での認証実装はなし
- Hannah Hill（hannahnl, US PES プログラムリード）がこのプロセスをリード

### Task 2: AU での Prime 認証の実現可能性

- LWA は AU（FE リージョン: JP, SG, AU）でサポート確認済み（*）
  - (*) PrimePass（`prime:benefit_status` スコープ）が AU で動作するかは要確認
- 3P による Prime 認証は、Prime Ellis チームとのエンゲージメントが必要な可能性あり
  - (*) PBS Onboarding Wiki に「Third Party Integration should go through Prime Ellis」との表記があるため

### Task 3: Event Cinemas 提案の Gut Check

- Event Cinemas が提案した SHA256 ベースの認証方式を評価
- **Critical 1:** 秘密鍵の外部共有 — Amazon の鍵管理ポリシー抵触、鍵漏洩で完全な偽造が可能
- **Critical 2:** MemberId の PII 露出 — Amazon 内部顧客識別子が外部に直接渡る（LWA は Directed ID で保護）
- **結論:** 不採用。ただし Event Cinemas をパートナーとして却下するものではなく、LWA ベースの統合への切替を逆提案
- Ads Security Engineer（Sunit Guldas）による正式な gut check は返信待ち

---

## Key Contacts

| 役割 | 名前 | コンテキスト |
|------|------|-------------|
| US PES プログラムリード | Hannah Hill (hannahnl) | Ellis/LWA チームへのエントリーポイント |
| US DT（検証済み） | Kelly Prudente (kellypru) | US PES 技術詳細を確認済み |
| Ads Security Engineer | Sunit Guldas (gulsunit) | SHA256 gut check（DM 送信済み、返信待ち） |
