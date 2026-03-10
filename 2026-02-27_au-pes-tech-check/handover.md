# Handover Document
**Topic:** AU Prime Early Screenings Tech Check — Event Cinemas パートナーシップ技術評価
**Date:** 2026-03-10
**Status:** 進行中（Ellis CX リサーチ完了・推奨順位再検討中 + gulsunit gut check返信待ち + Hannah Hill 連絡予定）

---

## 背景

AU BIL チーム（Matt Bryant/mjlb, Chris Wilson/wilsnup）から DT（Shugo Saito）にアサインされた Tech Check チケット。Prime Early Screenings (PES) をオーストラリアで Event Cinemas と実施するための技術評価。Asana: ENT | AU | Prime Early Screenings | Australia Pilot（TEX Global Intake, T2, DT Resource）。

PES は US で Fandango と提携して運用されているプログラムで、Prime 会員に映画の先行上映チケットを提供する。Fandango が AU で運営していないため、Event Cinemas を代替パートナーとして検討中。

プロジェクトは非常に初期段階で、IO 未署名のプロアクティブな探索。Event Cinemas から Amazon との API 連携に関する技術プロポーザルを受け取った段階。

## 現在の状況

### リサーチ・検証・レポート — 完了
- Task 1/2/3 + 最終レポートが PDF で完成済み
- 結論: Event Cinemas の SHA256 提案は不採用（Critical 2件）
- 推奨: LWA + PrimePass（第一推奨）、Ellis Prime Offer Code CX（第二推奨）
- Slack/Quip/Internal Wiki/Internal Search でクロスチェック実施、主要クレームは概ね正確と確認
- Ellis Wiki に "WW Updates in Progress" を発見 — AU 展開の可能性を強化

### Tech Check レポート — V2 作成完了（3/4）🆕
- V1（2/27）: 初版。EN/JP の MD レポート
- **V2（3/4）:** Kelly のバリデーション + 構造改善。主な変更:
  - 「US DT バリデーション」セクション追加
  - PrimePass / Prime Ellis の関係性修正（別選択肢 → 補完関係）
  - 第一推奨を「LWA + Prime Ellis」にリネーム + US 検証済みバッジ
  - ソースセクションを Tier 1-5 の出所帰属付きに全面書き換え
  - インライン出所マーカー追加（重要事実に `[Tier X: ...]` タグ）
  - Hannah Hill をキーステークホルダーに追加
  - **エグゼクティブサマリー再構成:** Purpose → Task Results → Recommended Approach（リスク統合）→ Next Steps
  - Amazon Pay 制約の記述矛盾修正（Embedded Store CX のみ影響、Fandango モデルには影響なし）
  - Task 1 サマリー行修正（EN: "Understanding" → "Review user flow"、JP: "技術構成を理解する" → "ユーザーフロー & 技術詳細をレビューする"）
  - 2回のレビューサイクルで計 Critical 1件 + Medium 9件 + Low 7件を修正

### Ellis Blueprint CX Constructs リサーチ — 完了（3/5）🆕
- Ellis Wiki を直接確認し、**5つの Blueprint CX Construct** を特定:
  1. Online Offers（Grubhub+, Calm）— LWA + Ellis API、6-8週
  2. Partner Promotions（LinkedIn, Starbucks）— API統合不要
  3. Pre-Verification（UNiDAYS）— LWA + Ellis API、4-6週
  4. Prime Offer Code — Transactional / Account Linking（**Odeon Cinemas**, Peet's Coffee）— 4-6週
  5. Embedded Store（Grubhub）— Amazon Pay + Ellis API、最も深い統合
- **重要な発見 1**: Fandango / PES / PrimePass は Blueprint CX Constructs Wiki に一切記載なし
  - US Fandango/PES 統合は Blueprint 外のカスタム統合の可能性が高い
  - 再現手順が標準化されておらず、Hannah Hill に聞かないと詳細不明
- **重要な発見 2**: LWA と Amazon Pay は完全に独立したサービス（依存関係なし）
  - Amazon Pay が必要なのは Embedded Store CX（Grubhub model）のみ
  - 推奨アプローチ（LWA + PrimePass / Offer Code CX）は Amazon Pay 不要
  - V2 レポートの「Amazon Pay 不可 → Fandango model 再現不可」は不正確 → 修正必要
- **推奨順位再検討**: ODEON model が PES AU により適合する可能性
  - Odeon = UK 映画館チェーン、Blueprint CX として標準化済み
  - Fandango model は Blueprint 外（ドキュメント未整備、再現コスト不透明）
  - 統合コスト・期間ともに Offer Code CX が有利（4-6週 vs 8-12週、LWA不要）
- リサーチノート EN/JP を notes/ に保存済み

### Kelly Prudente (kellypru) からの回答 — 完了（3/3）🆕
- **3/3 にフォローアップ DM 送信 → 即日返信あり**
- US PES は **LWA + Prime Ellis** の組み合わせで実現（Tech Check の推奨通り）
- Fandango/Atom が自社サイト上で LWA を実装、LWA チームがサポート
- LWA の scope `prime:benefit_status` で Prime 会員判定 — これが PrimePass の実体
- **キーパーソン: Hannah Hill (hannahnl)** — Kelly の SM。Fandango 連携を主導した張本人
  - Prime Ellis チーム + LWA チームとの連携方法を知っている
  - 「彼女に連絡して全ステップを理解すべき」と Kelly が推奨
- US Telent（現 US Entertainment + Beauty）が amazon.com でのチケット販売を企画していたが保留中の可能性
- 3P 経由（Event Cinemas のケース）なら US PES の実績（Wicked, Superman, D&D 等）の learnings がそのまま使える
- Kelly にお礼の返信送信済み

### Ads Security レビュー — gulsunit 🆕
- Harish Bharani (hbbharan, **BIL-VAR Sr. TPM**, SEA40 Seattle) が 3/2 に返信: **Sunit Guldas (gulsunit, Ads Security Security Engineer II, JFK14 New York) を推薦**
- 「Sunit がエキスパートなので彼と進めろ。メールして自分を CC に入れてくれ」
- **3/3 に gulsunit にメール送信済み**（CC: hbbharan）— Tech Check レビュー依頼、Asana リンク付き
- **3/3 に gulsunit に Slack DM 送信済み** — メール送った旨のヘッズアップ
- **3/3 に Asana タスク (1213466153419679) にコメント投稿済み** — gulsunit 向けのレビュー依頼 + Kelly からの US PES 確認情報
  - ⚠️ 初回投稿は HTML 二重エスケープ問題あり → プレーンテキストで再投稿済み（3/3）
- **3/3 Harish が Asana コメント:** Sunit と直接話し、Shugo がオンラインになり次第 Slack で対応するとのこと
- **3/4 Sunit DM:** 「帰宅したら ping する」
- **3/9 Sunit DM:** 「忘れてた、今日話せる？」
- **3/10 方針変更:** 推奨がPrime Ellis経由に固まり、フルセキュリティレビューは不要に。SHA256 Critical 2件の判定妥当性のみSlack DMで非同期確認に切替、DM送信済み — 返信待ち

### mjlb（Matt Bryant）への US SM 連携依頼 — 方針変更
- Kelly から Hannah Hill (hannahnl) が直接のキーパーソンと判明
- Matt 経由ではなく Hannah に直接連絡する方が効率的

## 成果物一覧

```
Google Drive .ai/2026-02-27_au-pes-tech-check/
├── handover.md                              ← 本ファイル
├── history/
│   ├── 2026-02-27_handover.md               ← 旧バージョン（圧縮アーカイブ）
│   ├── 2026-03-02_handover.md               ← 旧バージョン（圧縮アーカイブ）
│   └── 2026-03-03_handover.md               ← 旧バージョン（圧縮アーカイブ）🆕
├── artifacts/
│   ├── AU_PES_TechCheck_Report_EN.md        ← Tech Check レポート V1（英語版）
│   ├── AU_PES_TechCheck_Report_JP.md        ← Tech Check レポート V1（日本語版）
│   ├── AU_PES_TechCheck_Report_EN_V2.md     ← Tech Check レポート V2（英語版）🆕
│   └── AU_PES_TechCheck_Report_JP_V2.md     ← Tech Check レポート V2（日本語版）🆕
└── notes/
    ├── verification-report.md               ← Slack/Quip/Wiki 検証レポート
    ├── ellis-cx-patterns-research-EN.md     ← Ellis CX リサーチ（英語版）🆕
    └── ellis-cx-patterns-research-JP.md     ← Ellis CX リサーチ（日本語版）🆕

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
    ├── AU_PES_TechCheck_Final.pdf
    ├── AU_PES_TechCheck_Report_EN_V2.md     ← Tech Check レポート V2（英語版）🆕
    └── AU_PES_TechCheck_Report_JP_V2.md     ← Tech Check レポート V2（日本語版）🆕
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|---|---|---|
| 1 | **最優先** | **Hannah Hill (hannahnl) に連絡** — US PES エンゲージメントプロセス・learnings を把握 | ⬜ 未着手 |
| 2 | 最優先 | Ellis の AU 対応を確認 → Ellis チーム（Joshua Huang）Hannah Hill 経由 | ⬜ 未着手 |
| 3 | — | gulsunit の SHA256 Critical判定 gut check | 🔄 Slack DM送信済み(3/10) — 返信待ち |
| 4 | Medium | Bullseye API の AU 対応を確認 → BIL Tech | ⬜ 未着手 |
| 5 | Ellis確認後 | Event Cinemas に LWA/Ellis モデルを逆提案 | ⬜ 未着手 |
| 6 | 上記確認後 | Full Scope 提出を検討 | ⬜ 未着手 |
| 7 | Medium | Quip AU BIL Team WIP の PES セクション確認 | ⬜ 未着手 |
| 8 | — | mjlb への Tech Check 結果共有 | ⬜ 未着手 |
| 9 | Next | **V2 レポートの Amazon Pay 記述を修正** | ⬜ 未着手 🆕 |
| 10 | Next | **推奨順位の見直し** — Fandango model vs ODEON model の優先度再検討 | ⬜ 未着手 🆕 |
| 11 | Low | **Ellis CX リサーチノートの修正** — 「6つの Blueprint」→「5つ」に訂正 | ⬜ 未着手 🆕 |
| 12 | — | Tech Check レポート V2 EN/JP 作成 + レビュー修正 | ✅ 完了（3/4） |
| 10 | — | kellypru に DM — US PES 技術詳細確認 | ✅ 完了（3/3 返信あり） |
| 11 | — | BIL-E NA Intake Form 提出 | ✅ 完了（2/27） |
| 12 | — | hbbharan に DM + BIL-E レビュー方針転換 | ✅ 完了（3/2） |
| 13 | — | gulsunit にメール・DM・Asana コメント送信 | ✅ 完了（3/3） |
| 14 | — | Asana コメント HTML 問題修正 | ✅ 完了（3/3） |

## 重要な判断ログ

### Event Cinemas SHA256 提案 → 不採用
- Critical 1: 秘密鍵の外部共有（Amazon 鍵管理ポリシー抵触）
- Critical 2: MemberId の PII 露出（PrimePass は Directed ID で保護）
- Event Cinemas 自体は却下しない → LWA/Ellis モデルへの切替を逆提案

### 推奨アプローチ（V1 → V2 での変遷）
- V1 第一推奨: LWA + PrimePass（Fandango モデル）、V1 第二推奨: Ellis Prime Offer Code CX（ODEON モデル）
- **V2 修正:** 第一推奨を「LWA + **Prime Ellis**」にリネーム（Kelly 証言で PrimePass が Prime Ellis の一部と判明）
- 両者は「代替」ではなく「フル統合 vs ライトウェイト統合」の関係
- 元リサーチでは Ellis が第一推奨だったが、LWA の方が実現可能性が高いと判断して順位を変更

### BIL-E レビュー依頼の方針転換（3/2）
- 当初: BIL-E NA Intake Form で「正式なセキュリティ評価」として提出 → Harish が ASR と解釈
- 実際のニーズ: 正式な ASR ではなく、エンジニアによる Tech Check 結果のバリデーション
- M&M's Spotto ASR（Asana: 1212335750973364）で Dylan Brandt が担当したような、エンジニアレベルのフィードバック
- Harish の回答: gulsunit（Sunit Guldas）がエキスパート → 彼と進めるべき

### US PES 実態の確認（3/3 Kelly 回答）🆕
- Fandango/Atom は **LWA + Prime Ellis** で統合（Tech Check の LWA + PrimePass 推奨と一致）
- LWA scope `prime:benefit_status` が Prime 会員判定の実体
- DT は直接関与せず、LWA チームと Fandango が直接やりとり
- **Hannah Hill (hannahnl)** が US PES を主導 → AU のキーパーソンとして連絡すべき
- US Telent の amazon.com チケット販売企画は保留中の可能性

### PrimePass / Prime Ellis の関係性修正（3/4）🆕
- V1 では「LWA + PrimePass」と「Ellis Prime Offer Code CX」を**別選択肢**として提示していた
- Kelly の Tier 1 証言により、US では **LWA と Prime Ellis が補完的に動作** していることが判明
- PrimePass（`prime:benefit_status` スコープ）は Prime Ellis エコシステムの一機能である可能性が高い
- V2 ではこの関係性を修正: フル統合（LWA + Prime Ellis）とライトウェイト統合（Ellis Offer Code CX のみ）の2オプション
- **Tech Check の結論（SHA256 不採用、LWA ベースに切替）は正しい** — ズレていたのは Ellis の位置づけのみ
- Hannah Hill に確認して確定すべき事項

### Tech Check レポート V2 の情報出所ティア制（3/4）🆕
- V2 でソースセクションを 5 段階のティアに分類して全面書き換え
- Tier 1（直接証言: Kelly DM）> Tier 2（社内 Wiki）> Tier 3（Slack 観察）> Tier 4（コード解析）> Tier 5（外部資料）
- 理由: 情報の出所によってコンテクストとの関連性が桁違い。Kelly からの直接証言が最も重みが大きい
- 本文中にもインライン出所マーカー `[Tier X: ...]` を追加し、読者が各事実主張を検証可能に

### Tech Check V2 レポートのレビュー・構造改善（3/4）🆕
- EN/JP 両方に対して整合性レビューを実施（各 agent が独立にレビュー）
- Critical 1件: Amazon Pay 制約の記述矛盾（「Fandango モデル移植不可」→ 実際は影響なし）
- エグゼクティブサマリーを再構成: 1テーブルに全部入れる形式 → Purpose / Task Results / Recommended Approach（リスク統合）/ Next Steps に分離
- Key Risks を独立セクションから Recommended Approach の直下に移動（推奨に対するリスクとして紐付け）
- Next Steps の優先順位変更: Hannah Hill への連絡を最優先に（Kelly の推奨に基づく）、PrimePass AU 確認は確認先不明のため削除

### Asana API html_text の問題（3/3）🆕 → 修正済み
- `asana_comment_write` の `html_text` パラメータが二重エスケープされ、HTML タグがそのまま表示された
- **原因:** MCP ツールが HTML を再エスケープする仕様。`text`（プレーンテキスト）パラメータを使えば問題なし
- **対応:** プレーンテキストで再投稿済み（旧コメントは Asana API で削除不可のため残存）

### LWA と Amazon Pay は独立したサービス（3/5 確認）🆕
- Amazon Pay が LWA を認証基盤として利用していた（逆ではない）。2017年「LwA Decoupling」で分離推進
- Amazon Pay が必要なのは Embedded Store CX（Grubhub model）のみ — Amazonアプリ内で3P商品を購入するパターン
- 推奨アプローチ（LWA + PrimePass / Offer Code CX）は Amazon Pay 不要
- V2 レポートの Task 2 制約テーブル「Cannot directly replicate the US Fandango model」は不正確 → 修正必要

### Fandango/PES は Ellis Blueprint CX 外のカスタム統合（3/5 発見）🆕
- Ellis Blueprint CX Constructs Wiki（5タブ）に Fandango / PES / PrimePass の記載なし
- Blueprint CX は 5 パターン（Online Offers, Partner Promotions, Pre-Verification, Prime Offer Code, Embedded Store）
- Odeon Cinemas は Prime Offer Code (Transactional) のパイロットパートナーとして正式に記載
- Fandango model は再現手順が標準化されていない → Hannah Hill への確認が不可欠

### 推奨順位の再検討が必要（3/5 検討中）🆕
- ODEON model（Prime Offer Code Transactional）が PES AU により適合する根拠:
  1. 映画館の直接先例（Odeon = UK 映画館チェーン、2023/12 ローンチ）
  2. Blueprint CX として標準化済み（ドキュメント・API 整備済み）
  3. 統合コストが低い（Verify + Redeem API のみ、LWA 不要）
  4. 統合期間が短い（4-6 週 vs 8-12 週）
- Fandango model は理想的だが再現コストが不透明（Blueprint 外）

### Sunit gut check の方針変更（3/10）🆕
- 当初: フルセキュリティレビューとしてコールを予定（Harish (BIL-VAR Sr. TPM) 経由で紹介）
- 変更後: 推奨がPrime Ellis経由に固まり、Event Cinemas SHA256提案を進める予定がないため、フルレビューは不要に
- SHA256 Critical 2件（秘密鍵外部共有 + MemberId PII露出）の判定妥当性のみ、Slack DMで非同期確認に切替
- Sunit (Ads Security, Security Engineer II, JFK14 New York) に3/10 DM送信済み、返信待ち

### 検証で確認できなかった事項
- PrimePass の AU 動作検証 — Prime Ellis / Identity Services チームに確認が必要
- Ellis Wiki "WW Updates in Progress" — AU が対象かは Ellis チーム（Joshua Huang, Principal PMT）に確認が必要

## 重要リンク

- Asana Intake (TEX Global): https://app.asana.com/1/8442528107068/project/1212641864720082/task/1213411601791772?focus=true
- Asana BIL-E Intake Task: https://app.asana.com/1/8442528107068/task/1213466153419679
- M&M's Spotto ASR (参考): https://app.asana.com/1/8442528107068/project/1199343345138382/task/1212335750973364
- BIL-E NA Intake Form: https://form.asana.com/?k=yteEaKgwZq9qEZa3mNL-KQ&d=8442528107068
- BIL-E NA Wiki: https://w.amazon.com/bin/view/BIL-E/NA/
- AmazonAdsSecurity Wiki: https://w.amazon.com/bin/view/AmazonAdsSecurity/
- PES Wiki: https://w.amazon.com/bin/view/PrimeEarlyScreenings/
- Ellis Wiki: https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/
- Ellis Blueprint CX Constructs: https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/BlueprintCXConstructs/
- Amazon Pay Prime Ellis Program: https://w.amazon.com/bin/view/AmazonPay/PrimeEllisProgram/
- LWA Products (PrimePass): https://w.amazon.com/bin/view/IdentityServices/Products/LWA/
- LWA 3P Authorization: https://w.amazon.com/bin/view/IdentityServices/3PAuthZ/
- AU BIL Team WIP: https://quip-amazon.com/DbiAAG32tGjS

## 関連トピック

- `2026-02-23_sse-prototypes` — BIL-TEX AU デモ環境（同じ AU BIL コンテキスト）
- `2026-02-26_cat-decoder-tech-case-study` — Mars Dine CDK コード解析（JWT HS256 比較に使用）
