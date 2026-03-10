# PV Live Sports API Discovery -- Strategy v2
**Date:** 2026-03-09
**Author:** saitshug
**Status:** Draft -- Bindu sync (3/11) で議論

---

## Stakeholders

### Amazon Ads
Amazon Ads組織全体として、差別化された広告体験で売り上げを上げたい。

### BIL TEX (我々)
Prime Video Live Sports APIをBrand Gateway経由で利用可能にし、BIL Podsのキャンペーン実施にコミットしたい。
- **RACI:** A=Mirko, R=Shugo+Bindu

### BIL Pods (AU, JP, EU, US/CA/LATAM, MENA)
Prime Video Live Sports APIを利用するクリエイティブアイデアをブランドに売り込み、実施にこぎつけ、クリエイティビティを示したい。

### BIL-E
Brand GatewayをOwnする組織横断のエンジニアリングチーム。BIL Pods/TEXをできる限りサポートしたいが、一方で、キャンペーンバイキャンペーンの技術実装にリソースを使いたくない。
- **条件:** 正当なビジネスオポチュニティがあり、リソース投下の価値があること。複数Pod横断のユースケースが求められる（Bindu指摘: Harishは1案件だけでは動かない）。

### SDP (Sports Data Platform)
Prime Video Live Sports API の**技術基盤**をOwnするエンジニアリングチーム。データの取得・保存・配信を担う。

**組織:**
```
PV Live Events Tech WW
  Director: Imran Mohammed (mohimra, L8, Seattle)
    Sr. Mgr: Rudy Jivaraj (mjivaraj, L7, Austin) -- SDP全体
      SDM: Anand Kumaravel (anandkvl, Chicago) -- SDP Core (データ取得・配信)
      SDM: 他チーム (Genesis, LECE, SPIN, Almanac)
```

**スコープ:** 技術的なデータアクセスとAPI提供。Anandが「全広告主で利用可能」と言ったのはこのレイヤー。

**注意:** SDPはデータプロバイダーからデータを取得・正規化する技術基盤であり、データの商用ライセンスは管轄外。

### PV BD (Prime Video Business Development) -- NEW
SDPデータの**商用ライセンス**を管理し、データプロバイダーとの契約・交渉窓口を担う。

**組織:**
```
PV Devices-BD Tech & Product
  Sr. Mgr: Nina Pablo (ninapabl, L7, Seattle)
    Sr. BD Mgr: Jonathan Yi (yijonatj, L6, Arlington VA) -- ライセンス担当
    他BD: Fitz, Emily Dole, 他6名
```

**スコープ:** 3Pデータプロバイダー（Sportradar等）との商用利用ライセンス交渉。Editorial useは標準化済みだが、commercial useは個別交渉が必要。

**Jonathan Yiの初期肩書き（2024/01入社時）:** "Tech Bus Dev - Licensing" -- ライセンスが専門領域。

### SDP と PV BD の関係

```
                  +-- mikehopk (SVP, Prime Video & Amazon Studios) --+
                  |                                                   |
          PV Live Events Tech WW                       PV Devices-BD Tech & Product
          (エンジニアリング)                              (ビジネスデベロップメント)
                  |                                                   |
        mohimra (Director, L8)                              ninapabl (Sr. Mgr, L7)
                  |                                                   |
        mjivaraj (Sr. Mgr, L7)                              yijonatj (Sr. BD Mgr, L6)
                  |
        anandkvl (SDM) -- SDP Core
```

**同じPV傘下だが別組織。** SDPが技術基盤を構築・運用し、PV BDがデータプロバイダーとのビジネス関係（ライセンス・契約）を管理する。我々がSDPデータを商用利用するには、**両方のチームとの調整が必要。**

### Data Providers (3P)
SDPにデータを提供する外部企業。Sportradar が主要プロバイダーとして確認されている。

**構造:** 1プロバイダーが複数スポーツをカバー（例: Sportradarはサッカー、バスケ、テニス等を横断）。ただし、リーグや地域によってプロバイダーが異なる可能性あり。

**Jonathan Yi の "case-by-case" の意味（メール 3/7 原文分析）:**

> "it's definitely not a 1-size-fits-all type of model and the providers typically want to figure out the full scope of use case and potential reach before they do their calculus on how much to charge."

これは以下の3軸で個別交渉が発生することを意味する:

| 軸 | 説明 | 例 |
|----|------|-----|
| **Use Case（用途）** | データを何に使うか。表示方法、インタラクション、トリガーの仕組み | スコア表示、予測ゲーム、動的商品推薦 |
| **Reach（リーチ）** | どれだけのユーザーに届くか。地域・規模 | US全体、AU限定、グローバル |
| **Data Scope（データ範囲）** | どのスポーツ・リーグ・データ種別を使うか | NBAリアルタイムスコア、クリケット選手統計 |

つまり「NBAのリアルタイムスコアをUS Brand Storeで表示する」と「サッカーW杯のプレイバイプレイをグローバルsidecastで使う」は**別々の交渉案件**になる可能性が高い。

**重要:** この交渉はPV BD (Jonathan Yi) を通じて行われる。我々がプロバイダーに直接コンタクトするのではなく、PV BDが仲介する。

---

## Goals（3層）

### Layer 1: 技術 (Tech)
Live Sports APIのBGW統合を完了させ、技術的ブロッカーがゼロの状態にする。
- **担当:** BIL-E (実装) + SDP Core (API提供・オンボーディング)
- **前提条件:** BIL-E Intake Request の受理

### Layer 2: 商用ライセンス (Commercial Licensing)
BIL Podsが参照できるライセンス・コスト・SOPのマッピングを完成させる。
- **担当:** PV BD (Jonathan Yi) との連携 + TEX (マッピング作成)
- **成果物:** データ x プロバイダー x 商用利用条件のテーブル

### Layer 3: リーガル・アドポリシー (Legal & Ad Policy)
広告としてスポーツデータを利用する際の法的・ポリシー的ブロッカーを洗い出し、対処する。

考えられるブロッカー:

| カテゴリ | リスク | 確認先 |
|---------|--------|--------|
| **データプロバイダーのライセンス条項** | 商用利用の制限（Jonathan Yiが指摘済み） | PV BD |
| **スポーツリーグのIP権利** | チームロゴ、選手画像、リーグ名称の広告利用 | PV BD / Legal |
| **Amazon Ads ポリシー** | スポーツデータを広告クリエイティブに使用する際のAdsポリシー準拠 | BIL Legal / Ad Policy |
| **ロケール別法規制** | ベッティング風ゲーミフィケーション（Quip記載のユースケース#1）はギャンブル規制に抵触する可能性 | 各ロケールのBIL Legal |
| **プライバシー・データ保護** | ユーザーの予測データ等を収集する場合のGDPR/プライバシー | Legal |
| **リアルタイムデータの正確性** | 誤ったスコア表示等による広告主・消費者への影響、責任の所在 | SDP Core + Legal |

**注:** Marikoが指摘した「ライセンシー問題」はLayer 2とLayer 3の両方にまたがる可能性が高い（JP固有のスポーツライセンシー構造）。

---

## Key Components

### Tech: Live Sports API x BGW統合
- SDP Core が提供する API を、Brand Gateway 経由で BIL Pods が利用可能にする
- BIL-E が実装主体
- SDP側の技術的ブロッカーの確認が必要（オンボーディングプロセス）

### Cost: 商用利用のコスト
- データプロバイダーごとに個別交渉（Jonathan Yi: "not a 1-size-fits-all"）
- 交渉は PV BD 経由
- コスト構造は use case x reach x data scope の3軸で決まる
- 標準的な価格表は存在しない可能性が高い（プロバイダーが個別に算出）
- **コスト負担者の確定が必要:** BIL / 広告主 / PV？

### Legal & Policy
- Layer 3 のテーブル参照
- ロケールごとの法規制チェック（特にベッティング風ユースケース）
- Amazon Ads ポリシーとの整合性確認

---

## Approaches

### (A) SSE的アプローチ -- Focus and Go Through

ビジネスアナリシスから優先でアンロックすべきLive Sportsを解析し、1-3個の優先スポーツを設定。

例:
- NBAデータのUS/AU利用（Chris Wilson: AU NBA中心で400k USD）
- クリケットのAU利用（ただし2026年は有力クリケットなし -- Chris Wilson指摘）
- サッカー（Champions League）のEU利用（EU Endemics $3MM/yr -- Mirko）

そのデータプロバイダーに絞り:
1. PV BD経由でデータプロバイダーとの商用利用交渉
2. 広告オポチュニティを定義しアタックリスト作成

### (B) 事前準備アプローチ -- Comprehensive Preparation

**技術的ブロッカーをゼロにし、かつ商用利用の全体像をマッピングしておく。**

#### 技術面（Layer 1）

BIL-E側の条件:
- 正しくビジネスオポチュニティがあり、リソース投下の価値がある
- Mirkoが準備中のビジネスインパクト（EU $3MM, AU 400k, US PoC実績）でアンロック可能と思われる
- **ただし JP 見積もり未回答、MENA 数字なし — ビジネスケースはまだ完成していない**

SDP側の条件:
- オンボーディングプロセスの確認が必要
- SDP Core Wiki: SIMテンプレート → intake queue (401d9a3a-52b8-498c-b754-d15efb71b6b6) で開始
- Slack: #sdp-contact
- 技術的ブロッカーの有無を確認

#### 商用ライセンス面（Layer 2）

商用利用は、使いたいデータごとに必要なステップを定義しきることで、BIL Podsが参照し、残り必要なアクションを実行できる状態にしておく。

**BIL PodsのSMが知る必要があること:**
- 特定のデータ利用にかかるコスト
- 利用開始のためのSOPとタイムライン
- ライセンス・リーガル・アドポリシーのブロッカー有無

**TEXでアクションが必要なこと:**
1. 全データのリストを取得 -- 既知: https://holly.prime-video.amazon.dev/onboarded-stats
2. 各データのデータプロバイダーを取得 -- **SDP Coreに問い合わせ**（技術的マッピング）
3. 各データプロバイダーの**商用利用窓口を特定** -- **PV BD (Jonathan Yi) に問い合わせ**（プロバイダーへの直接コンタクトではなく、PV BDが仲介）
4. 商用利用のために必要なステップを確認:
   - 商用利用に必要なコスト（use case x reach x data scopeの3軸で変動）
   - ライセンス条件
   - タイムライン
5. 全てをマッピングしたテーブルを作成

#### リーガル・アドポリシー面（Layer 3）

1. Amazon Ads ポリシーチームに、スポーツリアルタイムデータの広告利用に関するポリシーガイダンスを確認
2. ロケール別の法規制チェック（特にベッティング風ゲーミフィケーション）
3. スポーツリーグのIP利用制限の確認（ロゴ、選手画像等）
4. 各ブロッカーをマッピングテーブルに追加

---

## Approach (B) Next Steps

### Immediate（今週 -- Bindu sync後）

1. **Bindu sync (3/11)** -- 方針すり合わせ、Jonathan Yiコール段取り、BIL-E Intake現状確認
2. **Jonathan Yiコール段取り** -- Bindu + Jonathan Yi で実施（TZ制約: London-Arlington 重なりあり）。saitshugはメールCC+非同期フォロー。アジェンダ:
   - editorial vs commercial の境界線（PoCは editorial 扱いか？）
   - プロバイダーとの交渉フロー（PV BDの役割確認）
   - データ x プロバイダーのマッピング入手可否
3. **Discovery Doc 更新** -- Jonathan Yiのライセンス回答を反映

### Short-term（1-2週間）

4. **SDP Coreに問い合わせ:**
   - オンボーディングにあたり、技術的ブロッカーはないか
   - 各データのデータプロバイダーリストの取得
   - 問い合わせ先: #sdp-contact or SIM intake queue
5. **BIL-E Intake Request 準備** -- Bindu syncで方針確定後、ビジネスケース（Mirko収集中のインパクト数字）と合わせて提出
6. **Mirkoにライセンス問題エスカレーション** -- Jonathan Yiコール結果を共有

### Medium-term（2-4週間）

7. **PV BD経由で商用利用条件の確認** -- Jonathan Yiコール結果に基づき
8. **マッピングテーブル作成** -- データ x プロバイダー x 商用利用条件 x リーガル/ポリシー
9. **BIL Legal / Ad Policy チェック開始** -- ユースケース定義が固まり次第

---

## Open Questions（Bindu sync + Jonathan Yi コールで確認）

1. PoCやデモは editorial use の範囲で進められるか？ → Jonathan Yi
2. プロバイダーとの交渉フローは？ PV BD が完全に仲介するのか、SDP経由でもアクセス可能か？ → Jonathan Yi / Bindu
3. データ x プロバイダーのマッピングは既に存在するか？ → SDP Core / Jonathan Yi
4. コスト負担は誰か？ BIL / 広告主 / PV？ → Mirko / Jonathan Yi
5. BIL-E Intake は Bindu 側で既に動いていることがあるか？ → Bindu
6. JP のライセンシー問題の詳細は？ → Mariko
