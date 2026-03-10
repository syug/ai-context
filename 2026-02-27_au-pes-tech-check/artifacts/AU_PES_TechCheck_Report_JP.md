# AU Prime Early Screenings -- Tech Check レポート

**Event Cinemas x Amazon Prime -- オーストラリアパイロット**
**日付:** 2026-03-04
**ステータス:** Tech Check 完了 — US バリデーション取得済み

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
| **最もシンプル** | LWA のみ — Prime 認証のみ（`prime:benefit_status`）。オファー管理は Event Cinemas 側の責任 | 2-4 週間 | LWA AU 確認済み |
| **第一推奨** | LWA + Prime Ellis（Fandango モデル）— OAuth 2.0 標準、US PES で実績あり | 8-12 週間 | **US 検証済み** |
| **代替** | Ellis Prime Offer Code CX（ODEON モデル）— LWA 統合不要、ライトウェイト | 4-6 週間 | AU 対応は要確認 |
| 補完的 | Bullseye API — Brand Store 内での Prime 会員向けコンテンツ表示制御 | 1-2 週間 | AU 対応確認済み |

> **アプローチの段階的構成に関する注記（V4）：** LWA のみが最もシンプルな構成 — Amazon は Prime 認証のみを提供し、Event Cinemas がオファー管理（チケット在庫、利用上限、重複防止）を全て自前で行う。Ellis を追加（第一推奨または代替）すると Amazon 側でオファーライフサイクルの管理が可能になる。どのレベルの管理が必要かは Hannah Hill に確認。

**推奨アプローチに対するリスク:**

- PrimePass（`prime:benefit_status` スコープ、Prime Ellis 内）の AU マーケットプレイス対応が未検証
- Ellis Prime Offer Code CX の AU マーケットプレイス対応が未確認
- Amazon Pay が AU で利用不可 — Ellis「Embedded Store CX」（Grubhub モデル）は使用不可。上記アプローチには影響なし

### Next Steps

1. **Hannah Hill (hannahnl) に連絡** — US PES プログラムリード（Kelly が推薦）。Ellis/LWA 技術的確認事項の全てのエントリーポイント。エンゲージメントプロセスを把握する — US では Fandango/Atom が **Prime Ellis チームと LWA チームの両方**と密接に連携していた（Kelly 証言）。両チームへのエンゲージ方法を学び、US の learnings を AU に適用する
   - **Prime Ellis チーム:** Prime のオフ Amazon パートナーシッププログラムを管理 — オファーライフサイクル、資格ルール、パートナーオンボーディング、Verify/Redeem API
   - **LWA チーム（Identity Services）:** Login with Amazon を管理 — OAuth 2.0 認証、`prime:benefit_status` スコープによる Prime 会員判定
   - **核心的な質問:** US PES でなぜ Ellis を使ったのか？Pure LWA（`prime:benefit_status` のみ）では不十分だったのか？Event Cinemas が独自にオファー管理を行う前提なら、Ellis は不要な可能性がある
2. **Hannah 経由で US PES の Ellis 機能利用範囲を確認** — US PES が実際に使用している Ellis 機能（Verify/Redeem API、在庫管理、重複利用防止）と、Fandango が独自に実装している機能を確認。Fandango/PES は Ellis Blueprint CX Wiki に未掲載（カスタム統合の可能性）
3. **Hannah 経由で PrimePass AU 対応を確認** — Identity Services チームに繋いでもらう
4. **BIL-E エンジニアバリデーション** — Sunit Guldas (gulsunit) に SHA256 Critical 判定の gut check を依頼（Slack DM 送信済み、返信待ち）

---

## Task 1: US PES ユーザーフロー & 技術レビュー

### プログラム概要

Prime Early Screenings (PES) は、Amazon Prime 会員に新作映画の先行上映チケットを提供するプログラム。US では Fandango をチケット販売パートナーとして運用しており、BIL が制作を担当、TelEnt チームが主導している。

### US の実績

| 映画 | チケット枚数 | Box Office |
|------|-------------|------------|
| Wicked (2024) | 128,000枚 | $2.5M |
| Superman (2025) | 144,000枚 | $2.9M |
| Wicked: For Good (2025) | -- | $3.26M（初日 -- PES 史上最高記録） |

_[Tier 3: Slack #launch-party] [Tier 4: Arc キャンペーンドキュメント]_

### US ユーザーフロー（5ステップ）

| ステップ | アクション | 詳細 |
|---------|---------|------|
| 1 | **エントリーポイント** | H1（Homepage Hero）、Fire TV、Prime Video、広告、SNS から Brand Store ページへ誘導 |
| 2 | **Brand Store ページ** | チケット CTA、トレーラー、グッズ、Alexa Theme 等を集約する中央ハブ。Superman BSP: 1.38M PV、256K チケットクリックアウト |
| 3 | **Fandango リダイレクト** | チケット購入 CTA クリックで Fandango のチケット購入ページへ遷移（外部リンクアウト） |
| 4 | **LWA Prime 検証** | Fandango が Login with Amazon を使用して Prime 会員ステータスを検証。BIL/DT 側での認証実装はなし |
| 5 | **チケット購入** | Fandango プラットフォーム上で完結。Superman では Round-Up 寄付機能も初統合 |

### 技術アーキテクチャ

> *「DT の観点から会員認証のために行ったことは何もない。それはサードパーティのチケットパートナー（Atom / Fandango）と Login with Amazon チームが連携して行っている。」*
> -- Kelly Prudente (kellypru), #bil-tech-community / #bil-ww-tex [Tier 1: 直接証言]

| コンポーネント | 役割 |
|-------------|------|
| **Login with Amazon (LWA)** | OAuth 2.0 認証。顧客の同意を得て Prime ステータスを共有 |
| **PrimePass** | LWA の拡張スコープ（`prime:benefit_status`）。Prime 会員かどうかの Yes/No を返す [Tier 2: Identity Services Wiki]。Prime Ellis エコシステムの一部。Kelly Prudente（US DT）により Fandango/Atom がこのスコープで統合していることが確認済み [Tier 1: Kelly DM 2026-03-03] |
| **Bullseye API** | Brand Store 内で Prime 会員向けコンテンツを表示制御 |
| **Directed ID** | 3P ごとにユニークな不透明な識別子。Amazon の内部 MemberId は外部に出ない [Tier 2: Identity Services Wiki] |

### US PES のセキュリティ設計原則

- **顧客の明示的な同意:** OAuth 同意画面で顧客が許可
- **最小限のデータ共有:** Prime ステータス（Yes/No）のみ。個人情報は共有しない
- **Directed ID:** 3P ごとに異なる識別子。クロスサイトトラッキング不可
- **標準規格準拠:** OAuth 2.0 / OpenID Connect

### キーステークホルダー（US PES）

| 役割 | 名前 |
|------|------|
| DT（Wicked/Superman） | Kelly Prudente (kellypru) |
| Principal DT, Non-Endemic | Rawle Curtis (rawcur) |
| DT（Superman） | Dima Kyrylov (dimakyry) |
| Sr. SM（Wicked） | Hannah Hill (hannahnl) |
| US PES プログラムリード | Hannah Hill (hannahnl) — **AU エンゲージメントプロセスの主要連絡先** |
| Head of US TelEnt | Rob Alley (alleyrob) |
| Director, BIL | Kate McCagg (kmccagg) |
| VP, Global Prime | Jamil Ghani |
| Sr. PM, Prime Tech | Sonam Kothary |
| Head of AU BIL | Chris Wilson (wilsnup) |
| Sr. SM (AU) | Matt Bryant (mjlb) |

---

## US DT バリデーション（2026-03-03）

_本セクションは Task 1 の発見事項を検証し、後続セクションの推奨事項の根拠となる。_

### ソース
Kelly Prudente (kellypru)、US DT（Wicked/Superman キャンペーン担当）。2026-03-03 に Slack DM で確認。

### 主要確認事項

1. **Fandango/Atom は LWA + Prime Ellis で統合** — 両者とも Login with Amazon (LWA) でオンボーディングし、LWA チームと Prime Ellis チームの両方と密接に連携 [Tier 1: Kelly DM 2026-03-03]
2. **`prime:benefit_status` スコープ確認済み** — LWA がこのスコープで Prime 会員ステータスを渡す。これが 3P パートナーが Prime 資格を判定するメカニズム [Tier 1: Kelly DM 2026-03-03]
3. **3P 主導の実装** — 統合は fandango.com / atom.com 上で行われ、彼らのデベロッパーが実装。LWA チームメンバーがプロセスをサポート [Tier 1: Kelly DM 2026-03-03]
4. **Prime exclusive offer の厳格なルール** — US では Prime exclusive offer のラベルを付けるには LWA オンボーディングが必須。LWA が「Prime 会員かどうか」のパラメータを安全かつ正確に渡せるため [Tier 1: Kelly DM 2026-03-03]
5. **Hannah Hill (hannahnl) がイニシアティブをリード** — Kelly の SM が「このイニシアティブのリーダーシップを取った」。Prime Ellis + LWA チームとのエンゲージ方法を含む全ステップを理解するための連絡先として推奨 [Tier 1: Kelly DM 2026-03-03]

### PrimePass / Prime Ellis の関係性 — 修正

V1 では「LWA + PrimePass」と「Ellis Prime Offer Code CX」を2つの別々の選択肢として提示していた。Kelly のバリデーションにより、より詳細な全体像が明らかになった [Tier 1: Kelly DM 2026-03-03]:

- **PrimePass**（`prime:benefit_status` スコープ）は Prime 会員検証のための LWA メカニズム
- **Prime Ellis** は Prime オフ Amazon 体験のためのより広いプラットフォーム
- US の Fandango ケースでは、**LWA と Prime Ellis が連携して動作** — 代替関係ではなく補完関係

これにより:
- **フル統合（Fandango モデル）:** LWA 認証 + Prime Ellis プラットフォーム = US で実証済みのアプローチ
- **ライトウェイト統合（ODEON モデル）:** Ellis Prime Offer Code CX のみ = LWA 不要、コードベースの検証

AU では両方のオプションが有効。Event Cinemas の技術力と求めるユーザー体験に応じて選択する。

### Fandango API 統合プロジェクト（US）
- US Telent（reorg 後は US Entertainment + Beauty）が amazon.com 上にチケット販売の E2E 購入フローを構築する計画があった
- ステータス: おそらくまだ保留中 [Tier 1: Kelly DM 2026-03-03]
- AU の 3P モデルには直接関係ないが、US PES の learnings（Wicked, Superman, D&D 等）は 100% 適用可能 [Tier 1: Kelly DM 2026-03-03]

### LWA 開発者リソース
- 3P オンボーディングガイダンス: https://developer.amazon.com/docs/login-with-amazon/web-docs.html
- LWA スコープポータル: https://console.harmony.a2z.com/lwa-tools-portal/scopes

---

## Task 2: AU Prime 認証の実現可能性

### AU 固有の制約

| 制約 | 影響 |
|------|------|
| Amazon Pay が AU 未対応 | Ellis「Embedded Store CX」（Grubhub モデル）は使用不可。LWA + Prime Ellis（Fandango モデル）には影響なし |
| Fandango が AU 未展開 | 別のチケット販売パートナーが必要（Event Cinemas） |
| LWA の AU 対応 | LWA は FE リージョン（JP, SG, AU）をサポート [Tier 2: LWA Wiki] |
| PrimePass の AU 対応 | 要確認（US/UK で実績あり） |

### 主要発見事項

#### 1. LWA のオーストラリア対応 -- 確認済み

LWA の内部ドキュメントにより、AU は正式にサポートされているマーケットプレイスであることを確認。

| リージョン | マーケットプレイス |
|-----------|-----------------|
| NA | US, CA, MX, BR |
| EU | DE, FR, IT, ES, NL, BE, UK, IE, SE, PL, IN, ZA |
| **FE** | **JP, SG, AU** |

*ソース: Identity Services / LWA Marketplaces to Region Mapping Wiki* [Tier 2: LWA Marketplaces Wiki]

**技術的含意:** AU の amazon.com.au アカウントは FE リージョンの LWA 認証ポータルにルーティングされる。OAuth 2.0 フロー自体は AU で動作可能。ただし、PrimePass（`prime:benefit_status` スコープ）が AU マーケットプレイスの Prime 会員ステータスを正しく返すかは別途検証が必要。

> **注記（V4）：** LWA の `prime:benefit_status` だけで Prime 認証は完結する。Event Cinemas がオファーライフサイクル（チケット在庫、利用上限、重複防止）を自前で管理する場合、Amazon 側に Ellis の統合は不要。Ellis は Amazon 側でオファーを管理するための追加レイヤーであり、認証の前提条件ではない。

#### 2. PrimePass -- 要検証

PrimePass は Identity Services / 3P AuthZ チームが管理する LWA のスコープ。[Tier 2: Identity Services Wiki]

- **ドメイン:** `prime`
- **スコープ:** `prime:benefit_status`
- **返却データ:** Amazon Prime 会員ステータス（Yes/No のみ）
- **顧客識別:** Directed ID（3P ごとにユニークな不透明な識別子。Amazon の内部 MemberId ではない）
- **同意:** 明示的な顧客同意画面あり（OAuth フロー）

**AU での未確認事項:**
- スコープが AU マーケットプレイスの Prime 会員に対して有効なデータを返すか
- AU Prime の内部データ構造が PrimePass の期待するフォーマットと互換性があるか

#### 3. Amazon Pay の AU 非対応

Amazon Pay は AU マーケットプレイスでは利用不可。これは Ellis の「Embedded Store CX」（Grubhub モデル）が AU では使えないことを意味する。ただし、「Prime Offer Code CX」（ODEON モデル）は Amazon Pay を必要としないため、推奨アプローチへの影響はない。

#### 4. ODEON Cinemas（UK）の前例 -- 最大の発見

リサーチの結果、ODEON Cinemas（UK/IE）が Ellis プログラムの「Prime Offer Code CX」構成で Prime 会員向け映画チケット割引を **2023年12月** から実施中であることを確認。[Tier 2: Ellis Wiki]

| 項目 | 詳細 |
|------|------|
| パートナー | ODEON Cinemas |
| 地域 | UK / IE |
| 対象 | All Prime |
| 構成 | Prime Offer Code CX |
| オファー内容 | Prime 会員は月1回、2枚 GBP 10 / EUR 10（通常比 46%+ 割引）で映画チケットを購入可能（月〜木） |
| ローンチ日 | 2023年12月7日 |
| Ellis Offer Page | amazon.co.uk/odeon |

**Prime Offer Code CX のフロー:**

1. Prime 会員が Amazon サイト/アプリでオファーコードを取得
2. Event Cinemas サイトでコードを入力
3. Event Cinemas が Ellis API（Verify Code）でコード検証
4. 検証成功 -> チケット購入 -> Ellis API（Redeem Code）で使用済みに

**Blueprint CX Constructs からの主要メリット:**

| 特徴 | 詳細 |
|------|------|
| LWA 統合不要 | "No Login with Amazon (LWA) API integration required" -- 明記 [Tier 2: Ellis Wiki] |
| Amazon Pay 不要 | AU で Amazon Pay が使えない制約を完全に回避 |
| 統合作業が軽量 | Event Cinemas の技術作業は Ellis API（Verify Code / Redeem Code）のみ |
| 統合タイムライン | 4-6 週間（LWA + PrimePass の場合は 8-12 週間） |
| レポーティング内蔵 | Redeem Code API でコード使用を追跡可能 |

### 認証方式の比較マトリクス

| 方式 | LWA 必要 | Amazon Pay 必要 | AU 対応 | 統合期間 | セキュリティ | 推奨度 |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| **LWA のみ**（Prime 認証のみ） | 必要 | 不要 | LWA AU 確認済み; PrimePass 要検証 | 2-4 週 | 高 | **最もシンプル** |
| **LWA + Prime Ellis**（Fandango モデル） | 必要 | 不要 | 要確認 | 8-12 週 | 高 | **第一推奨 — US 検証済み** |
| **Ellis Prime Offer Code CX**（ODEON モデル） | 不要 | 不要 | 要確認 | 4-6 週 | 高 | **第二推奨** |
| **Bullseye API**（補完的） | 不要 | 不要 | AU 対応確認済み | 1-2 週 | 高（表示制御のみ） | 補完的 |
| **Event Cinemas SHA256** | 不要 | 不要 | 対応可能 | 2-4 週 | **Critical リスクあり** | **不採用** |

### 未解決の検証事項

| # | 項目 | 確認先 | 優先度 |
|---|------|--------|--------|
| 1 | Ellis Prime Offer Code CX の AU マーケットプレイス対応 | Ellis チーム（Joshua Huang）Hannah Hill 経由 | **最優先** |
| 2 | PrimePass の AU マーケットプレイス対応 | Identity Services チーム | High |
| 3 | ~~Bullseye API の AU 対応~~ | BIL Tech チーム | ~~Medium~~ — **解決済み**（AU 対応確認済み） |
| 4 | Event Cinemas の Ellis API 統合能力 | Event Cinemas 技術チーム | Medium |

---

## Task 3: Event Cinemas 提案の Gut Check

### 提案フローの概要

Event Cinemas（EVT グループ傘下）が提案した SHA256 ベースの認証方式:

```
Amazon Prime 会員認証
  -> SHA256 トークン生成: SHA256(MemberId + Expires + SecretKey)
  -> HTTP GET で Event Cinemas へリダイレクト
  -> トークン「復号」・有効期限検証
  -> 先行上映チケット購入
```

**リダイレクト URL:** `https://www.eventcinemas.com.au/prime#prime_token={encryptedToken}`

**トークンペイロード:**
```json
{
  "MemberId": "{uniqueMemberId}",
  "Expires": "{utcExpiryTime in ISO 8601 format}"
}
```

### Critical リスク（2件）

#### Critical 1: 秘密鍵の外部共有（Pre-Shared Key モデル）

Event Cinemas の SHA256 方式では、Amazon と Event Cinemas が **同じ秘密鍵（SecretKey）を保持** する必要がある。

| リスク | 詳細 |
|--------|------|
| 鍵漏洩 = 完全な偽造 | Event Cinemas 側で鍵が漏洩した場合、第三者が有効なトークンを生成可能 |
| 否認不可能性の欠如 | 誰がトークンを生成したか暗号学的に証明できない |
| 鍵ローテーションの困難 | 両者で同時に鍵を変更する必要がある（運用負荷大） |
| Amazon ポリシー抵触 | Amazon の鍵管理ポリシーは秘密鍵の外部共有を制限 |

**Mars Dine MindReader との比較（CDK コード解析結果）:** [Tier 4: CDK コード解析]

Mars Dine も JWT HS256（対称鍵）を使用しているが、決定的な違いがある:

- Mars Dine: 鍵は AWS Secrets Manager に格納、Lambda 内でのみ使用、**外部に渡さない**
- Mars Dine: KMS 暗号化（JWTSecretKey）で二重保護
- Mars Dine: 自動ローテーション（30日ごと、RotationSchedule 実装済み）
- Event Cinemas 提案: 鍵を **外部企業に渡す** 必要がある

#### Critical 2: MemberId の外部露出（PII リスク）

トークンペイロードに `"MemberId": "{uniqueMemberId}"` が含まれ、Amazon の内部顧客識別子が外部企業に直接露出する。

| リスク | 詳細 |
|--------|------|
| PII の外部共有 | Amazon の顧客識別子を外部企業に直接渡す |
| 顧客の同意なし | 自動リダイレクトのため、顧客の明示的な同意プロセスがない |
| トラッキングリスク | MemberId を使って Amazon 顧客の行動を追跡可能 |
| データ保持の制御不能 | Event Cinemas 側での MemberId の保持・利用を Amazon が制御できない |

**LWA + PrimePass との比較:**

- PrimePass: 共有されるのは Prime 会員ステータス（Yes/No）**のみ**
- PrimePass: 顧客識別には **Directed ID**（3P ごとにユニークな不透明な識別子）を使用
- PrimePass: 顧客の **明示的な同意画面** あり（OAuth 同意フロー）
- PrimePass: Amazon の内部 MemberId は **一切外部に出ない**

### High リスク（3件）

| # | リスク | 詳細 |
|---|--------|------|
| 1 | **独自仕様** | OAuth 2.0、JWT（RFC 7519）、OpenID Connect のいずれにも準拠しない独自仕様。個別セキュリティレビュー必要（AppSec 負荷増）、標準ライブラリ使用不可、カスタム実装と保守が必要 |
| 2 | **リプレイ攻撃への脆弱性** | nonce（使い捨て値）の仕組みがない。有効期限内（2-10分）にトークンを何度でも再利用可能。JWT なら `jti`（JWT ID）クレームで一意性を保証できるが、SHA256 ハッシュにはそのメカニズムがない |
| 3 | **暗号技術の用語混乱** | SHA256 を「暗号化」、検証を「復号」と表現。SHA256 は一方向ハッシュ関数であり暗号化ではない。Event Cinemas 側の暗号技術に対する理解度への懸念を示唆 |

### Conditional / Incomplete（条件付き / 未完了）項目

| # | 項目 | 判定 |
|---|------|------|
| 1 | トークン有効期限（2-10分） | 範囲は妥当だが、リプレイ攻撃対策なし |
| 2 | URL フラグメント使用（`#`） | サーバーログには残りにくいが、JavaScript からアクセス可能（XSS リスク） |
| 3 | 購入確認 Webhook | 「オプション」は不十分 -- PES のレポーティング要件が未定義 |

### Pass 項目

| 項目 | 備考 |
|------|------|
| TLS 1.2+ | 業界標準。ただしトランスポート層の暗号化であり、アプリケーション層のセキュリティを代替するものではない |

### NRMA / CommBank 事例の適用可能性

Event Cinemas が提示した 2 つの前例（My NRMA、CommBank Yello）は **Amazon には適用不可**:

1. NRMA / CommBank は **オーストラリアの国内企業同士** の連携。Amazon は **グローバル企業** でセキュリティ/プライバシー要件が根本的に異なる
2. Amazon には既に **PrimePass / Ellis** という公式な 3P 連携の仕組みが存在する
3. Amazon のデータプライバシーポリシーは顧客識別子の外部共有を制限
4. Amazon のセキュリティレビュープロセス（AppSec）は独自仕様の暗号化方式に厳しい
5. PII の越境移転に関する規制（AU Privacy Act + Amazon 内部ポリシー）が適用される

### 総合評価マトリクス

| # | 評価項目 | 判定 | 深刻度 |
|---|---------|------|--------|
| 1 | 暗号化方式（SHA256 PSK） | **Fail** | Critical |
| 2 | MemberId の外部露出 | **Fail** | Critical |
| 3 | 標準規格準拠 | **Fail** | High |
| 4 | リプレイ攻撃耐性 | **Fail** | High |
| 5 | 暗号技術の理解度 | **Concern** | High |
| 6 | トークン有効期限 | Conditional | Medium |
| 7 | リダイレクト URL 構造 | Conditional | Medium |
| 8 | 通信セキュリティ（TLS 1.2+） | **Pass** | -- |
| 9 | 購入確認 Webhook | Incomplete | Medium |
| 10 | 前例の適用性 | N/A | -- |

### Gut Check 結論

Event Cinemas の提案は、**Amazon のセキュリティ/プライバシー要件を満たさない**。2つの Critical リスク（秘密鍵の外部共有 + MemberId の PII 露出）は設計の根本に関わるため、パラメータ調整（有効期限の短縮等）では解決できない。

> **重要:** これは Event Cinemas をパートナーとして却下することを意味しない。Event Cinemas が Amazon の既存インフラ（Ellis / LWA）での統合に切り替える意思があれば、技術的には実現可能。ODEON Cinemas (UK) の前例が直接的に適用できる。

---

## 推奨事項

### 最もシンプル: LWA のみ -- 最小構成

> **V4 で追加:** Event Cinemas のプロポーザル構造（Event Cinemas が全てのチケット販売・オファー管理を自前で行う）をベースにすると、Amazon 側に必要なのは Prime 認証のみ。

| 項目 | 詳細 |
|------|------|
| **アプローチ** | Event Cinemas が LWA SDK を統合し、`prime:benefit_status` スコープで Prime 会員ステータスを検証。オファー管理（チケット在庫、利用上限、重複防止）は全て Event Cinemas が担当 |
| **最もシンプルな理由** | 両者の統合作業が最小限。Amazon は認証のみ提供、Event Cinemas がオファーライフサイクルを完全に所有 |
| **AU 対応状況** | LWA は FE リージョン（AU）で確認済み。PrimePass の AU 対応は要検証 |
| **タイムライン** | 2-4 週間（LWA SDK 統合のみ） |
| **DT 負担** | なし |
| **3P 負担** | 低〜中（LWA SDK 統合 + 自前のオファー管理ロジック） |
| **未検証事項** | PrimePass `prime:benefit_status` スコープの AU Prime 会員に対する動作 |
| **選択する条件** | Event Cinemas がオファーライフサイクルを独自に管理する意思と能力がある場合 |

### 第一推奨: LWA + Prime Ellis（Fandango モデル） -- 主要推奨 -- US 検証済み

> **US DT により検証済み** — Kelly Prudente（US DT）が 2026-03-03 に LWA + Prime Ellis 統合が Fandango/Atom で使用されていることを確認。Prime Ellis チームの関与が確認された。

> **Ellis 機能範囲に関する注記（V3）：** 本レポートでは Ellis の機能（Verify/Redeem API、オファーライフサイクル管理、在庫管理、重複利用防止等）を Ellis プラットフォームのドキュメント（Tier 2: Wiki ソース）に基づいて記述している。**US PES がこれらの機能を実際にどこまで使用しているかは未確認。** Kelly Prudente の証言（Tier 1）は「LWA + Prime Ellis」を統合モデルとして確認したが、Ellis のどの機能を Fandango が利用し、どの機能を Fandango が独自に実装しているかは言及していない。また、Fandango/PES は Ellis Blueprint CX Wiki に掲載されておらず（標準パターン外のカスタム統合の可能性）。US PES における Ellis 機能の実際の利用範囲は Hannah Hill (hannahnl) への確認が必要 -- アクションアイテム参照。

| 項目 | 詳細 |
|------|------|
| **アプローチ** | Event Cinemas が LWA SDK を統合し、PrimePass で Prime 会員ステータスを検証。Prime Ellis プラットフォームと連携 |
| **主要推奨の理由** | US PES で実績あり（イベントあたり 128K+ チケット）、OAuth 2.0 標準、顧客の明示的同意、Directed ID でプライバシー保護。US DT バリデーション取得済み |
| **AU 対応状況** | LWA は FE リージョン（AU）で確認済み。PrimePass の AU 対応は要検証 |
| **タイムライン** | 8-12 週間 |
| **DT 負担** | なし（認証は LWA + Event Cinemas が担当） |
| **3P 負担** | 中（LWA SDK 統合が必要） |
| **未検証事項** | PrimePass `prime:benefit_status` スコープの AU Prime 会員に対する動作 |

### 第二推奨: Ellis Prime Offer Code CX（ODEON モデル） -- 代替

> **注記:** これは Prime Ellis プラットフォームのサブセットで、LWA なしのコードベース検証。

| 項目 | 詳細 |
|------|------|
| **アプローチ** | Prime 会員が Amazon でオファーコードを取得し、Event Cinemas サイトで入力。Ellis API で検証 |
| **代替推奨の理由** | LWA 統合不要、Amazon Pay 不要、4-6 週間で統合可能 [Tier 2: Ellis Wiki]、ODEON（UK）の映画館前例が 2023年12月から稼働中 [Tier 2: Ellis Wiki] |
| **AU 対応状況** | Ellis の AU マーケットプレイス対応は要確認 |
| **タイムライン** | 4-6 週間 |
| **DT 負担** | なし（Ellis チームが認証を管理） |
| **3P 負担** | 低（Ellis API: Verify Code + Redeem Code のみ） |
| **未検証事項** | Ellis Prime Offer Code CX の AU マーケットプレイス対応可否 |

### 第三推奨: Bullseye API（補完的）

| 項目 | 詳細 |
|------|------|
| **アプローチ** | Amazon Brand Gateway セグメント API で Brand Store 内の Prime 会員向け表示制御 |
| **役割** | 第一推奨または第二推奨の補完。単独では認証方式にならない |
| **ユースケース** | Brand Store 内で Prime 会員にのみチケット CTA を表示 |
| **タイムライン** | 1-2 週間 |

### Event Cinemas への逆提案

Event Cinemas の SHA256 提案は不採用とするが、これは **Event Cinemas をパートナーとして却下するものではない**。逆提案のポイント:

- Event Cinemas の技術作業は **Ellis API の 2 つのエンドポイントのみ**（Verify Code / Redeem Code）
- 独自の暗号化実装は不要
- 統合タイムライン: **4-6 週間**
- レポーティングは **Ellis API に内蔵**
- 直接的な前例: **ODEON Cinemas（UK）** が 2023年12月からまさにこのモデルで稼働中

> **注記:** 上記の Ellis API 機能（Verify Code、Redeem Code、レポーティング内蔵）は Ellis プラットフォームのドキュメントに基づく。ODEON モデルは確認済みの Ellis Blueprint CX パターンである。ただし、Fandango/US PES モデル（第一推奨）については、在庫管理・重複防止・オファーライフサイクルのどこまでを Ellis が管理し、どこまでを Fandango が独自に実装しているかは未確認であり、Hannah Hill への確認が必要。

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
| 6d | Hannah 経由: PrimePass（`prime:benefit_status` スコープ）の AU 対応を確認 — Identity Services チームに繋いでもらう or 直接確認 | Hannah Hill / Identity Services | 最優先 | ⬜ 未着手 |
| 7 | Event Cinemas に Ellis/LWA モデルを逆提案 | AU BIL チーム | #6d 確認後 | ⬜ 未着手 |
| 8 | Full Scope 提出を検討 | AU BIL チーム | 上記確認後 | ⬜ 未着手 |

### Nice-to-have / Add-on

| # | アクション | 担当 | 優先度 | ステータス |
|---|----------|------|--------|-----------|
| 4 | Bullseye API の AU 対応 | BIL-E / Shugo | Medium | ✅ AU 対応済みと判断。Full Scope へ進む場合はプロトタイプで要検証 |
| 9 | Quip AU BIL Team WIP の PES セクション確認 | Shugo（DT） | Medium | 確認済み（3/10）— PES 関連は断片的な言及のみ、詳細な技術議論なし |
| 10 | Ellis チームとのエンゲージメント + AU 対応確認 — Amazon 側でオファー管理（利用者追跡、上限枚数、重複防止等）が必要な場合、または Hannah 確認後に Ellis が必要と判明した場合。Hannah 経由で Ellis チーム（Joshua Huang, Principal PMT）に接続し、AU マーケット対応を確認 | Hannah Hill / Ellis チーム | Low | ⬜ 未着手 — #6b の結果次第 |

---

## ソース & 情報の出所

情報ソースを信頼性のティアで分類。上位ティアの情報ほど、対象に直接関与しているため重みが大きい。

### Tier 1: 直接証言（最高重み）
US PES の実装に直接関与した人物からの一次情報。

| ソース | チャンネル | 日付 | 提供された主要情報 |
|--------|-----------|------|-------------------|
| **Kelly Prudente (kellypru)** — US DT、Wicked/Superman キャンペーンリード | Slack DM | 2026-03-03 | Fandango/Atom は LWA + Prime Ellis で統合、`prime:benefit_status` スコープで Prime 検証、Hannah Hill がイニシアティブをリード、US PES の learnings は AU の 3P モデルに 100% 適用可能 |
| **Kelly Prudente (kellypru)** | Slack #bil-tech-community | 2026-02（観察） | 「DT の観点から会員認証のために行ったことは何もない。それはサードパーティのチケットパートナー（Atom / Fandango）と Login with Amazon チームが連携して行っている。」 |
| **Kelly Prudente (kellypru)** | Slack #bil-ww-tex | 2026-02（観察） | LWA / Bullseye による Prime 会員検証の技術的選択肢 |
| **Harish Bharani (hbbharan)** — BIL-E エンジニアリングリード | Slack DM + Asana コメント | 2026-02-28, 2026-03-03 | Sunit Guldas (gulsunit) を BIL-E セキュリティエキスパートとして推薦 |

### Tier 2: 内部ドキュメント（高い重み）
Amazon 公式の社内 Wiki・ツール。AI アシストリサーチで発見・検証。人からの直接証言ではない。

| ソース | URL | 主要情報 |
|--------|-----|---------|
| Identity Services / 3P AuthZ Wiki | https://w.amazon.com/bin/view/IdentityServices/3PAuthZ/ | PrimePass 定義: `prime:benefit_status` スコープ、Directed ID メカニズム |
| Identity Services / LWA Marketplaces | https://w.amazon.com/bin/view/IdentityServices/Products/LWA/ | AU は FE リージョン（JP, SG, AU）で LWA サポート確認 |
| LWA 3P Authorization Wiki | https://w.amazon.com/bin/view/IdentityServices/3PAuthZ/ | LWA スコープ詳細と 3P 認可フレームワーク |
| Prime Ellis Team / Offers Launched | https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/ | ODEON Cinemas (UK/IE) の Prime Offer Code CX 事例、"WW Updates in Progress" |
| Prime Ellis / Blueprint CX Constructs | https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/ | Offer Code CX は「LWA 統合不要」、4-6 週間のタイムライン |
| PES Wiki | https://w.amazon.com/bin/view/PrimeEarlyScreenings/ | PES プログラム概要と US の実績 |
| BIL-E NA Wiki | https://w.amazon.com/bin/view/BIL-E/NA/ | BIL-E インテークプロセスとセキュリティレビューフレームワーク |
| AmazonAdsSecurity Wiki | https://w.amazon.com/bin/view/AmazonAdsSecurity/ | Ads セキュリティ相談プロセス（Harish が参照） |
| LWA Developer Docs（公開） | https://developer.amazon.com/docs/login-with-amazon/web-docs.html | 3P オンボーディングガイダンス（Kelly が「Fandango がこれに従った」と言及） |
| LWA Scopes Portal（社内） | https://console.harmony.a2z.com/lwa-tools-portal/scopes | `prime:benefit_status` を含む利用可能な LWA スコープ（Kelly が言及） |

### Tier 3: Slack チャンネル観察（中程度の重み）
公開 Slack チャンネルで観察された情報。直接提供されたものではなく、AI リサーチでチャンネル履歴から抽出。

| チャンネル | 主要情報 | 備考 |
|-----------|---------|------|
| #bil-tech-community | kellypru の LWA/PES 技術オプションに関するコメント | 観察、直接証言ではない |
| #bil-ww-tex | kellypru の Bullseye/LWA 検証に関するコメント | 観察、直接証言ではない |
| #launch-party | Wicked: For Good の実績（PES 史上最高記録 $3.26M 初日） | 公開チャンネルでのアナウンス |

### Tier 4: コード解析 & キャンペーンドキュメント（補助的）

| ソース | 主要情報 |
|--------|---------|
| BIL-TEX-APAC-MarsDine-MindReaderCDK (jwt-utils/index.ts, cdk-stack.ts) | JWT HS256 対称鍵ハンドリング比較 — Mars Dine は Secrets Manager に格納、外部に渡さない。Event Cinemas の秘密鍵共有提案との対比に使用 |
| Arc: Superman "Anyone Can Be Super" | Lighthouse キャンペーン参照 — PES チケット販売データ |
| Arc: Wicked "Oz Casts a Spell on Amazon" | Lighthouse キャンペーン参照 — PES チケット販売データ |

### Tier 5: 外部 / 添付資料

| ソース | 主要情報 |
|--------|---------|
| Event Cinemas Partner API Spec（PDF 添付） | レビュー対象の SHA256 認証提案 |
| Event Cinemas 過去事例 — NRMA / CommBank（PDF 添付） | 前例の主張（Amazon には適用不可と評価） |
| ODEON Cinemas Prime 割引プログラム（公開 Web） | ODEON Prime オファープログラムの公開情報 |

### 出所に関する注記

- **Tier 1 ソース（Kelly）が最も重みが大きい** — US PES の実装に直接関与しており、Fandango/Atom が LWA + Prime Ellis とどう統合したかの一次情報を持っている
- **PrimePass / Prime Ellis の関係性修正（V2）** は Kelly の Tier 1 証言に基づく。V1 でこれらを別選択肢として分離していたのは Tier 2 の Wiki リサーチに基づいており、各コンポーネントの説明としては正確だったが、実際の運用でどう連携しているかは捉えていなかった
- **Wiki ソース（Tier 2）** は AI アシストの社内検索で発見。公式ドキュメントだが、機能を個別に説明しており、実際の実装パターンを反映していない場合がある
- **Slack 観察（Tier 3）** は Kelly 自身の発言だが、チャンネル履歴から観察したもので、我々の質問に対して直接提供されたものではない。同じ情報は後に DM で直接確認された（Tier 1 に昇格）
- **（V3）Ellis 機能の記述（Verify/Redeem API、在庫管理、重複防止等）** は Tier 2 の Wiki ドキュメントに基づく Ellis プラットフォームの能力記述である。Kelly の Tier 1 証言は「LWA + Prime Ellis」を統合モデルとして確認したが、Fandango が Ellis のどの機能を利用しているかの詳細は含まれていない。Fandango/PES は Ellis Blueprint CX Wiki に未掲載であり、カスタム統合の可能性がある。Hannah Hill に確認されるまで、本レポートの Ellis 機能への言及はプラットフォームの能力として読むべきであり、US PES の実装詳細として確認されたものではない

---

## バージョン履歴

| バージョン | 日付 | 変更内容 |
|-----------|------|---------|
| V1 | 2026-02-27 | 初版 Tech Check レポート |
| V2 | 2026-03-04 | US DT バリデーション（Kelly Prudente）: LWA + Prime Ellis 統合確認、`prime:benefit_status` スコープ確認、Hannah Hill がキーコンタクト。PrimePass/Prime Ellis の関係性を修正。アクションアイテム更新。＋構造修正（テーブル順序、Amazon Pay 制約の明確化、ソース帰属追加） |
| V3 | 2026-03-10 | Ellis プラットフォームの能力（Tier 2 ドキュメント）と US PES での確認済み利用（Tier 1 証言）を区別する注記を追加。Fandango/PES は Ellis Blueprint CX Wiki に未掲載 -- カスタム統合の可能性。Hannah Hill (hannahnl) への Ellis 機能利用範囲の確認をアクションアイテムに追加 |
| V4 | 2026-03-10 | LWA のみアプローチの明確化: Ellis は認証に不要、オファー管理のオプション。Event Cinemas がオファーライフサイクルを独自管理する前提での最もシンプルな構成（LWA Only）を Priority 0 として追加。Hannah Hill への核心的な質問を追加: US PES で Ellis を使った理由は？Pure LWA では不十分だったのか？ |
