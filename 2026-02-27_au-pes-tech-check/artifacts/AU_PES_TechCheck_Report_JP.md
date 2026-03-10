# AU Prime Early Screenings -- Tech Check レポート

**Event Cinemas x Amazon Prime -- オーストラリアパイロット**
**日付:** 2026-02-27
**ステータス:** Tech Check 完了

---

## エグゼクティブサマリー

### 目的

AU BIL チームが Prime Early Screenings (PES) をオーストラリアで Event Cinemas をチケット販売パートナーとして実施するにあたり、以下の3点を技術的に評価する。

1. **Task 1:** US PES の技術構成を理解する
2. **Task 2:** AU での Prime 認証の実現可能性を検証する
3. **Task 3:** Event Cinemas の提案を "Gut Check" する

### 総合評価

| 項目 | 判定 |
|------|------|
| Event Cinemas の SHA256 提案 | **不採用** -- Critical リスク 2件（秘密鍵の外部共有 + MemberId の PII 露出） |
| AU での PES 実現可能性 | **実現可能** -- ただし US とは異なるアプローチが必要 |
| 推奨アプローチ（第一推奨） | **LWA + PrimePass（Fandango モデル）** -- US で実績あり、OAuth 2.0 標準 |
| 推奨アプローチ（代替） | **Ellis Prime Offer Code CX（ODEON モデル）** -- LWA 統合不要、Amazon Pay 不要、4-6 週間 |

### 主要リスク

- PrimePass（`prime:benefit_status` スコープ）の AU マーケットプレイス対応が未検証
- Ellis Prime Offer Code CX の AU マーケットプレイス対応が未確認
- Amazon Pay が AU で利用不可のため、一部の統合パターンが制限される

### 最重要 Next Step

Ellis Prime Offer Code CX の AU マーケットプレイス対応可否を Prime Ellis チーム（whitmeye）に確認し、PrimePass の AU 対応を Identity Services チームに確認する。

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
> -- Kelly Prudente (kellypru), #bil-tech-community / #bil-ww-tex

| コンポーネント | 役割 |
|-------------|------|
| **Login with Amazon (LWA)** | OAuth 2.0 認証。顧客の同意を得て Prime ステータスを共有 |
| **PrimePass** | LWA の拡張スコープ。Prime 会員かどうかの Yes/No を返す |
| **Bullseye API** | Brand Store 内で Prime 会員向けコンテンツを表示制御 |
| **Directed ID** | 3P ごとにユニークな不透明な識別子。Amazon の内部 MemberId は外部に出ない |

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
| Head of US TelEnt | Rob Alley (alleyrob) |
| Director, BIL | Kate McCagg (kmccagg) |
| VP, Global Prime | Jamil Ghani |
| Sr. PM, Prime Tech | Sonam Kothary |
| Head of AU BIL | Chris Wilson (wilsnup) |
| Sr. SM (AU) | Matt Bryant (mjlb) |

---

## Task 2: AU Prime 認証の実現可能性

### AU 固有の制約

| 制約 | 影響 |
|------|------|
| Amazon Pay が AU 未対応 | US の Fandango モデルをそのまま移植不可 |
| Fandango が AU 未展開 | 別のチケット販売パートナーが必要（Event Cinemas） |
| LWA の AU 対応 | LWA は FE リージョン（JP, SG, AU）をサポート |
| PrimePass の AU 対応 | 要確認（US/UK で実績あり） |

### 主要発見事項

#### 1. LWA のオーストラリア対応 -- 確認済み

LWA の内部ドキュメントにより、AU は正式にサポートされているマーケットプレイスであることを確認。

| リージョン | マーケットプレイス |
|-----------|-----------------|
| NA | US, CA, MX, BR |
| EU | DE, FR, IT, ES, NL, BE, UK, IE, SE, PL, IN, ZA |
| **FE** | **JP, SG, AU** |

*ソース: Identity Services / LWA Marketplaces to Region Mapping Wiki*

**技術的含意:** AU の amazon.com.au アカウントは FE リージョンの LWA 認証ポータルにルーティングされる。OAuth 2.0 フロー自体は AU で動作可能。ただし、PrimePass（`prime:benefit_status` スコープ）が AU マーケットプレイスの Prime 会員ステータスを正しく返すかは別途検証が必要。

#### 2. PrimePass -- 要検証

PrimePass は Identity Services / 3P AuthZ チームが管理する LWA のスコープ。

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

リサーチの結果、ODEON Cinemas（UK/IE）が Ellis プログラムの「Prime Offer Code CX」構成で Prime 会員向け映画チケット割引を **2023年12月** から実施中であることを確認。

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
| LWA 統合不要 | "No Login with Amazon (LWA) API integration required" -- 明記 |
| Amazon Pay 不要 | AU で Amazon Pay が使えない制約を完全に回避 |
| 統合作業が軽量 | Event Cinemas の技術作業は Ellis API（Verify Code / Redeem Code）のみ |
| 統合タイムライン | 4-6 週間（LWA + PrimePass の場合は 8-12 週間） |
| レポーティング内蔵 | Redeem Code API でコード使用を追跡可能 |

### 認証方式の比較マトリクス

| 方式 | LWA 必要 | Amazon Pay 必要 | AU 対応 | 統合期間 | セキュリティ | 推奨度 |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| **LWA + PrimePass**（Fandango モデル） | 必要 | 不要 | 要確認 | 8-12 週 | 高 | **第一推奨** |
| **Ellis Prime Offer Code CX**（ODEON モデル） | 不要 | 不要 | 要確認 | 4-6 週 | 高 | **第二推奨** |
| **Bullseye API**（補完的） | 不要 | 不要 | 対応見込み | 1-2 週 | 高（表示制御のみ） | 補完的 |
| **Event Cinemas SHA256** | 不要 | 不要 | 対応可能 | 2-4 週 | **Critical リスクあり** | **不採用** |

### 未解決の検証事項

| # | 項目 | 確認先 | 優先度 |
|---|------|--------|--------|
| 1 | Ellis Prime Offer Code CX の AU マーケットプレイス対応 | Prime Ellis チーム（whitmeye） | **最優先** |
| 2 | PrimePass の AU マーケットプレイス対応 | Identity Services チーム | High |
| 3 | Bullseye API の AU 対応 | BIL Tech チーム | Medium |
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

**Mars Dine MindReader との比較（CDK コード解析結果）:**

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

### 第一推奨: LWA + PrimePass（Fandango モデル） -- 主要推奨

| 項目 | 詳細 |
|------|------|
| **アプローチ** | Event Cinemas が LWA SDK を統合し、PrimePass で Prime 会員ステータスを検証 |
| **主要推奨の理由** | US PES で実績あり（イベントあたり 128K+ チケット）、OAuth 2.0 標準、顧客の明示的同意、Directed ID でプライバシー保護 |
| **AU 対応状況** | LWA は FE リージョン（AU）で確認済み。PrimePass の AU 対応は要検証 |
| **タイムライン** | 8-12 週間 |
| **DT 負担** | なし（認証は LWA + Event Cinemas が担当） |
| **3P 負担** | 中（LWA SDK 統合が必要） |
| **未検証事項** | PrimePass `prime:benefit_status` スコープの AU Prime 会員に対する動作 |

### 第二推奨: Ellis Prime Offer Code CX（ODEON モデル） -- 代替

| 項目 | 詳細 |
|------|------|
| **アプローチ** | Prime 会員が Amazon でオファーコードを取得し、Event Cinemas サイトで入力。Ellis API で検証 |
| **代替推奨の理由** | LWA 統合不要、Amazon Pay 不要、4-6 週間で統合可能、ODEON（UK）の映画館前例が 2023年12月から稼働中 |
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

---

## アクションアイテム

| # | アクション | 担当 | 優先度 |
|---|----------|------|--------|
| 1 | LWA + PrimePass の AU 対応を確認（`prime:benefit_status` スコープ） | Identity Services チーム | **最優先** |
| 2 | Ellis Prime Offer Code CX の AU マーケットプレイス対応を確認 | Prime Ellis チーム（whitmeye） | **最優先** |
| 3 | Bullseye API の AU 対応を確認 | BIL Tech チーム | Medium |
| 4 | Event Cinemas に Ellis/LWA モデルを逆提案 | AU BIL チーム -> Event Cinemas | #1 & #2 確認後 |
| 5 | Full Scope 提出を検討 | AU BIL チーム | 上記確認後 |

---

## ソース一覧

### Internal Wiki
- Identity Services / 3P AuthZ / Products Using LWA -- PrimePass の定義と仕様
- Identity Services / LWA Marketplaces to Region Mapping -- AU は FE リージョンで LWA サポート確認
- Prime Ellis Team / Offers Launched -- ODEON Cinemas (UK/IE) の Prime Offer Code CX 事例
- Prime Ellis / Blueprint CX Constructs -- 「LWA 統合不要」、4-6 週間の統合タイムライン
- Amazon Pay / Prime Ellis Program -- Embedded Store CX（AU 非対応）

### Slack
- **#bil-tech-community** -- kellypru: PES における LWA の技術的選択肢と DT 関与範囲の説明
- **#bil-ww-tex** -- kellypru: LWA / Bullseye による Prime 会員検証の技術的選択肢
- **#launch-party** -- Wicked: For Good の実績（PES 史上最高記録）

### Arc / キャンペーンドキュメント
- Superman "Anyone Can Be Super" -- Lighthouse キャンペーン
- Wicked "Oz Casts a Spell on Amazon" -- Lighthouse キャンペーン

### コード解析
- BIL-TEX-APAC-MarsDine-MindReaderCDK -- jwt-utils/index.ts, cdk-stack.ts（対称鍵ハンドリング比較）

### 添付資料
- **[資料 1]** Partner API Spec -- Event Cinemas 提案
- **[資料 2]** Event Cinemas 過去事例（NRMA / CommBank）PDF

### Web
- Login with Amazon Developer Documentation -- Supported Marketplaces
- ODEON Cinemas Prime 割引プログラム公開情報
