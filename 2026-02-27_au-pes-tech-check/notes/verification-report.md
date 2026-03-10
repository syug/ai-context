# AU Prime Early Screenings — Tech Check 検証レポート
Date: 2026-02-27

## 概要
AU BIL の Prime Early Screenings (PES) Tech Check に関する既存リサーチ（Smith Research）の内容を、Slack、Quip、Internal Wiki、Internal Search の各ソースでクロスチェックした結果。

## リサーチサマリ

### 全体結論
- Event Cinemas の SHA256 提案 → 🔴 不採用（Critical 2件: 秘密鍵の外部共有 + MemberId の PII 露出）
- AU での PES 実現 → ✅ 可能（ただし US とは異なるアプローチが必要）
- 推奨: 🥇 Ellis Prime Offer Code CX（ODEON モデル）

### Task 1: US PES の技術構成
- BIL/DT は認証ロジック実装ゼロ。Fandango 側が LWA SDK を統合し Prime 会員認証を処理
- Amazon 側は Brand Store Page（チケット CTA）のみ提供
- 実績: Superman 144K枚/$2.9M BO、Wicked for Good 初日$3.26M
- ステークホルダー: kellypru（DT）, rawcur（Principal DT）, hannahnl（Sr. SM）, alleyrob（US TelEnt Head）

### Task 2: AU 認証フィージビリティ
- LWA は AU 対応（FE リージョン: JP, SG, AU）✅
- PrimePass (prime:benefit_status スコープ) の AU 動作は要検証 ⚠️
- Amazon Pay は AU 非対応 ❌ → Fandango モデルそのまま移植不可
- **最大の発見:** ODEON Cinemas (UK) が Ellis Prime Offer Code CX で映画チケット割引を 2023/12 から実施中
  - LWA 統合不要、Amazon Pay 不要、4-6 週間で統合可能
  - Event Cinemas → Ellis API (Verify Code / Redeem Code) のみ統合

### Task 3: Event Cinemas 提案 Gut Check
- 🔴 Critical 1: SHA256 PSK モデル → 秘密鍵を外部企業と共有（Amazon 鍵管理ポリシー抵触）
- 🔴 Critical 2: MemberId がトークンに含まれ PII 露出（PrimePass は Directed ID で保護）
- 🟡 High: 独自仕様（OAuth/JWT 非準拠）、リプレイ攻撃脆弱性、暗号技術の理解度懸念（SHA256 を「暗号化」と表現）
- ただし Event Cinemas 自体は却下しない → Ellis モデルへの切替を逆提案

## 検証結果

### Slack 検証
| 検索クエリ | 結果 | 所見 |
|---|---|---|
| "Prime Early Screenings"（完全一致） | 0件 | AU での PES 議論は Slack 上に存在しない |
| "Event Cinemas" | 2件 | 個人チケット転売と Sony Foundation 企業スクリーニング（PES 無関係） |
| "Login with Prime" | 1件 | Music Unlimited UI テストのみ（映画館無関係） |
| "PES Australia" / "PES AU" | 0件 | 技術インフラ用語の PES（Policy Enforcement System）のみヒット |
| Superman PES | 確認 | #ad-sales-high-five で $5M WB 案件として確認。Fandango 経由 |

**結論: AU PES パイロットは極めて初期段階。Slack での議論はまだ発生していない。**

### Internal Wiki 検証
| ページ | 所見 |
|---|---|
| PES Wiki (w.amazon.com/bin/view/PrimeEarlyScreenings/) | ✅ 確認。bil-us-telent 所有。US プログラムのみ記載。AU/国際展開の記述なし |
| PES Eligibility | $3M 最低メディア支出、2,000+ 劇場、$300M+ BO 予測。完全に US 基準 |
| PES FAQs | 年間 8-9 回、4 週間間隔、$3M 必須。3P スタジオと MGM の区別あり |
| Ellis Wiki (PrimeTeam/PrimeOffAmazon/Ellis/) | ✅ ODEON Cinemas 確認。**"WW Updates in Progress"** — worldwide 展開を示唆 |

### Quip 検証
| ドキュメント | 所見 |
|---|---|
| AUxMENA BIL 2026 OP1 Early share | AU BIL 戦略文書。PES/Ellis/ODEON の記載なし |
| AU BIL Team WIP | 137K 文字の大規模文書。screening/cinema/ticket の検索ヒットあり。要ブラウザ確認 |

### 主要クレームの検証状況
| リサーチのクレーム | 検証結果 | 判定 |
|---|---|---|
| US PES は Fandango + LWA で運用 | Wiki + Slack + FAQs で確認 | ✅ 正確 |
| BIL/DT は認証ロジック実装ゼロ | kellypru の Slack 発言として引用。PES Wiki 構造から整合 | ⚠️ 蓋然性高い |
| LWA は AU (FE リージョン) 対応 | Wiki 引用。LWA 公式でも AU サポートは既知 | ⚠️ 蓋然性高い |
| ODEON Cinemas が Ellis で映画チケット運用 | Ellis Wiki で確認 | ✅ 正確 |
| Ellis は "WW Updates in Progress" | Ellis Wiki で確認 | ✅ 正確 |
| Amazon Pay AU 非対応 | 一般的に既知事実 | ✅ 正確 |
| Event Cinemas 提案に Critical リスク 2 件 | 技術的分析として妥当 | ✅ 合理的 |
| PES Eligibility は $3M/$300M+ BO | PES Eligibility Wiki で完全一致 | ✅ 正確 |

### 検証で発見された追加情報
1. **Ellis Wiki に "WW Updates in Progress"** — リサーチでは言及されていなかった重要情報。Ellis の worldwide 展開が進行中であることは、AU への Ellis 適用可能性を強化
2. **PES の年間枠は 8-9 回、$3M 最低支出** — AU パイロットがこの枠組みにどう位置づけられるかは不明
3. **Quip "AU BIL Team WIP"** — 137K 文字の大規模文書に screening/cinema/ticket の記述あり。要ブラウザ確認

## アクションアイテム（優先順）

| # | アクション | 担当 | 優先度 | 備考 |
|---|---|---|---|---|
| 1 | Ellis Prime Offer Code CX の AU 対応を確認 | → Prime Ellis チーム (whitmeye) | 🔴 最優先 | Ellis Wiki "WW Updates in Progress" が追い風 |
| 2 | PrimePass (prime:benefit_status) の AU 対応を確認 | → Identity Services / 3P AuthZ | 🟡 High | Ellis が使えない場合のフォールバック |
| 3 | Bullseye API の AU 対応を確認 | → BIL Tech チーム | 🟡 Medium | Brand Store 内の表示制御用 |
| 4 | Event Cinemas に Ellis モデルを逆提案 | → AU BIL (mjlb/wilsnup) | Ellis 確認後 | 技術作業は Ellis API 2 エンドポイントのみ |
| 5 | Full Scope 提出を検討 | → AU BIL チーム | 上記確認後 | |
| 6 | Quip "AU BIL Team WIP" の PES 関連セクション確認 | → Shugo | 🟡 Medium | ブラウザで直接確認 |

## ソース一覧

### Smith Research
- SUMMARY - ENT | AU | Prime Early Screenings | Australia Pilot.pdf
- TASK1 - US Prime Early Screenings — ユーザーフロー & 技術詳細レビュー.pdf
- Task2_AU_Prime_Auth_Feasibility.pdf
- Task3_EventCinemas_GutCheck.pdf
- AU_PES_TechCheck_Final.pdf

### 元資料（Intake 添付）
- Amazon_Prime_Preview_Partner_API_Spec.pdf
- Event Cinemas Ticket Partner Customer Journey.pdf
- Wicked_CLP_Screenshot.png

### 検証ソース
- Slack 検索: "Prime Early Screenings", "Event Cinemas", "Login with Prime", "PES Australia" 等
- Wiki: PrimeEarlyScreenings/, EligibilityRequirements/, faqs/, saleshub/, PESCalendar/, PrimeTeam/PrimeOffAmazon/Ellis/
- Quip: AUxMENA BIL 2026 OP1 (ifAZAxiYsnAn), AU BIL Team WIP (DbiAAG32tGjS)
- Internal Search: ALL domain, WIKI domain
