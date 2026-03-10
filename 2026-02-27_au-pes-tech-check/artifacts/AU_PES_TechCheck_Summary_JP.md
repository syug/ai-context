# AU Prime Early Screenings -- Tech Check サマリー

**日付:** 2026-03-10
**作成者:** Shugo Saito (DT)
**インテーク:** ENT | AU | Prime Early Screenings | Australia Pilot (T2, DT Resource)
**フルレポート:** artifacts/AU_PES_TechCheck_Report_JP.md 参照（V3, 2026-03-10）

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
| 1. US PES 技術レビュー | **レビュー完了** | LWA + Prime Ellis が基盤。US DT（Kelly Prudente, 2026-03-03）により検証済み |
| 2. AU 実現可能性 | **実現可能** | LWA は AU（FE リージョン）で確認済み。PrimePass と Ellis の AU 対応は要検証 |
| 3. Event Cinemas 提案 | **不採用** | Critical リスク 2件: 秘密鍵の外部共有 + MemberId の PII 露出 |

### 推奨アプローチ

| 優先度 | アプローチ | タイムライン | ステータス |
|--------|-----------|-------------|-----------|
| **最もシンプル** | LWA のみ -- Prime 認証のみ（`prime:benefit_status`）。オファー管理は Event Cinemas 側の責任 | 2-4 週間 | LWA AU 確認済み |
| **第一推奨** | LWA + Prime Ellis（Fandango モデル）-- OAuth 2.0 標準、US PES で実績あり | 8-12 週間 | **US 検証済み** |
| **代替** | Ellis Prime Offer Code CX（ODEON モデル）-- LWA 統合不要、ライトウェイト | 4-6 週間 | AU 対応は要確認 |
| 補完的 | Bullseye API -- Brand Store 内での Prime 会員向けコンテンツ表示制御 | 1-2 週間 | AU 対応確認済み |

> **注記（V4）：** LWA のみが最もシンプルな構成 — Amazon は Prime 認証のみ提供、Event Cinemas がオファー管理を担当。Ellis は Amazon 側でオファーをコントロールするためのオプション。必要な管理レベルは Hannah Hill に確認。

**推奨アプローチに対するリスク:**

- PrimePass（`prime:benefit_status` スコープ、Prime Ellis 内）の AU マーケットプレイス対応が未検証
- Ellis Prime Offer Code CX の AU マーケットプレイス対応が未確認
- Amazon Pay が AU で利用不可 -- Ellis「Embedded Store CX」（Grubhub モデル）は使用不可。上記アプローチには影響なし

### Next Steps

1. **Hannah Hill (hannahnl) に連絡** -- US PES プログラムリード（Kelly が推薦）。Ellis/LWA 技術的確認事項の全てのエントリーポイント。エンゲージメントプロセスを把握する -- US では Fandango/Atom が **Prime Ellis チームと LWA チームの両方**と密接に連携していた（Kelly 証言）。両チームへのエンゲージ方法を学び、US の learnings を AU に適用する
   - **Prime Ellis チーム:** Prime のオフ Amazon パートナーシッププログラムを管理 -- オファーライフサイクル、資格ルール、パートナーオンボーディング、Verify/Redeem API
   - **LWA チーム（Identity Services）:** Login with Amazon を管理 -- OAuth 2.0 認証、`prime:benefit_status` スコープによる Prime 会員判定
   - **核心的な質問:** US PES でなぜ Ellis を使ったのか？Pure LWA（`prime:benefit_status` のみ）では不十分だったのか？
2. **Hannah 経由で US PES の Ellis 機能利用範囲を確認** -- US PES が実際に使用している Ellis 機能（Verify/Redeem API、在庫管理、重複利用防止）と、Fandango が独自に実装している機能を確認。Fandango/PES は Ellis Blueprint CX Wiki に未掲載（カスタム統合の可能性）
3. **Hannah 経由で Ellis AU 対応 & PrimePass AU 対応を確認** -- Ellis チーム（Joshua Huang, Principal PMT）と Identity Services チームに繋いでもらう
4. **BIL-E エンジニアバリデーション** -- Sunit Guldas (gulsunit) に SHA256 Critical 判定の gut check を依頼（Slack DM 送信済み、返信待ち）

---

## アクションアイテム

### 依頼スコープ内（Tech Check として必要）

| # | アクション | 担当 | 優先度 | ステータス |
|---|----------|------|--------|-----------|
| 1 | gulsunit SHA256 Critical 判定の gut check | gulsunit（Sunit Guldas） | Medium | 🔄 Slack DM 送信済み（2026-03-10）、返信待ち |
| 2 | mjlb への Tech Check 結果共有 | Shugo（DT） | — | ⬜ 未着手（2026-03-11 Sync 予定） |
| 3 | 推奨順位の見直し（Fandango model vs ODEON model） | Shugo（DT） | Medium | ⬜ 未着手 |
| 5 | kellypru に US PES 詳細を確認 | Shugo（DT） | High | ✅ 完了（2026-03-03） |

### 次フェーズ（必須 — 進行に必要）

| # | アクション | 担当 | 優先度 | ステータス |
|---|----------|------|--------|-----------|
| 6 | Hannah Hill (hannahnl) に連絡 — US PES プログラムリード（Kelly が推薦）。Ellis/LWA 技術的確認事項の全てのエントリーポイント | Shugo（DT） | **最優先 — Next** | ⬜ 未着手 |
| 6a | Hannah 経由: US PES エンゲージメントプロセスと AU に適用可能な learnings を把握。US では Fandango が**2チーム**と連携: **Prime Ellis チーム**（オフ Amazon パートナーシップ / オファー管理）と **LWA チーム**（Identity Services / OAuth 認証 + `prime:benefit_status`）。両チームへのエンゲージ方法を確認 | Hannah Hill | 最優先 | ⬜ 未着手 |
| 6b | Hannah 経由: US PES における Ellis 機能の実際の利用範囲を確認 — Fandango が実際に使っている機能（Verify/Redeem API、在庫管理、重複利用防止）と独自実装の切り分け。**核心的な質問: そもそも Ellis が必要だった理由は何か。Pure LWA（`prime:benefit_status` のみ）では不十分だった点は何か** | Hannah Hill | 最優先 | ⬜ 未着手 |
| 6c | Hannah 経由: Ellis の AU マーケット対応を確認 — Ellis チーム（Joshua Huang, Principal PMT）に繋いでもらう or 直接確認 | Hannah Hill / Ellis チーム | 最優先 | ⬜ 未着手 |
| 6d | Hannah 経由: PrimePass（`prime:benefit_status` スコープ）の AU 対応を確認 — Identity Services チームに繋いでもらう or 直接確認 | Hannah Hill / Identity Services | 最優先 | ⬜ 未着手 |
| 7 | Event Cinemas に Ellis/LWA モデルを逆提案 | AU BIL チーム | #6c & #6d 確認後 | ⬜ 未着手 |
| 8 | Full Scope 提出を検討 | AU BIL チーム | 上記確認後 | ⬜ 未着手 |

### Nice-to-have / Add-on

| # | アクション | 担当 | 優先度 | ステータス |
|---|----------|------|--------|-----------|
| 4 | Bullseye API の AU 対応 | BIL-E / Shugo | Medium | ✅ AU 対応済みと判断。Full Scope へ進む場合はプロトタイプで要検証 |
| 9 | Quip AU BIL Team WIP の PES セクション確認 | Shugo（DT） | Medium | 確認済み（3/10）— PES 関連は断片的な言及のみ、詳細な技術議論なし |
| 10 | Ellis チームとのエンゲージメント — Amazon 側でオファー管理が必要な場合、または Hannah 確認後に Ellis が必要と判明した場合 | Hannah Hill / Ellis チーム | Low | ⬜ 未着手 — #6b の結果次第 |

---

## Key Contacts

| 役割 | 名前 | コンテキスト |
|------|------|-------------|
| US PES プログラムリード | Hannah Hill (hannahnl) | Kelly 推薦。Ellis/LWA チームへのエントリーポイント |
| US DT（検証済み） | Kelly Prudente (kellypru) | US PES 技術詳細を確認済み |
| Ads Security Engineer | Sunit Guldas (gulsunit) | SHA256 gut check（DM 送信済み、返信待ち） |
| Ellis Principal PMT | Joshua Huang | Ellis AU 対応確認（Hannah 経由） |

---

*フルレポートは artifacts/AU_PES_TechCheck_Report_JP.md を参照*
