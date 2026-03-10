# Public API Landscape Research -- Spotify Web API と類似APIの深掘り比較

**Date:** 2026-03-06
**Context:** Matt Bryant (BIL) が Spotify Web API を共有 ("Imagine if we had something like this") → Amazon社内外の類似API調査
**Author:** AI Research Agent

---

## Executive Summary

Spotify Web APIは「開発者に愛されるAPI」の代名詞であり、その成功要因は(1)包括的なエンドポイント設計、(2)OAuth 2.0ベースのシンプルな認証、(3)優れたドキュメントとインタラクティブなPlayground、(4)活発な開発者コミュニティにある。Amazon傘下ではTwitch APIが最もSpotifyに近い設計思想を持ち、156+エンドポイント・EventSubリアルタイム通知・充実したCLIツールを備える。Amazon Music Web API (Phoenix)はClosed Betaながら同様のアーキテクチャを志向しており、Playback API追加やBeReal/Tesla連携など戦略的パートナーシップが進行中。IMDbはGraphQL + AWS Data Exchangeのエンタープライズモデルで、セルフサービス型DXとは異なるアプローチを取る。BIL/TEXにとっては、Spotify/Twitch型のDXをAmazon Musicエコシステムで実現することが最大の機会であり、PA-API後継のCreators APIの動向も注視すべきである。

---

## 機能比較マトリクス

| API | 種別 | エンドポイント数 | 認証 | レート制限 | 料金 | SDK | GraphQL | リアルタイム | DXスコア |
|-----|------|-----------------|------|-----------|------|-----|---------|-------------|---------|
| **Spotify Web API** | 音楽 | 80+ | OAuth 2.0 (3フロー) | 非公開 (クォータ制) | 無料 | なし (公式) | No | No | ★★★★★ |
| **Twitch API** | ライブ配信 | 156+ | OAuth 2.0 + JWT | あり (動的) | 無料 | CLI | No | EventSub | ★★★★☆ |
| **IMDb API** | エンタメメタデータ | N/A (GraphQL) | AWS Data Exchange | 不明 | 有料 (要問合せ) | なし | Yes | No | ★★☆☆☆ |
| **Amazon Music (Phoenix)** | 音楽 | 30+推定 | OAuth 2.0 (LWA) | TPS制限あり | Closed Beta | なし | No | No | ★★★☆☆ |
| **Amazon Ads API** | 広告 | 100+推定 | OAuth 2.0 (LWA) | あり | 無料 | Java/Python/JS | No | No | ★★★☆☆ |
| **Apple Music (MusicKit)** | 音楽 | 60+推定 | JWT + User Token | 非公開 | 無料 | Swift/JS/Android | No | No | ★★★★☆ |
| **PA-API 5.0** | Eコマース | 4 | AWS Sig V4 | あり | 無料 | 複数言語 | No | No | ★★★☆☆ |
| **SP-API** | マーケットプレイス | 200+ | OAuth 2.0 (LWA) | API別 | 無料 | 5言語 | 一部 | EventBridge | ★★★☆☆ |
| **Last.fm** | 音楽メタデータ | 59 | API Key + セッション | 非公開 | 無料 | なし | No | No | ★★★☆☆ |
| **MusicBrainz** | 音楽メタデータ | 13エンティティ | なし/OAuth2 | 1req/sec | 無料 | なし | No | No | ★★★☆☆ |
| **Genius** | 歌詞 | 10+推定 | OAuth 2.0 | 不明 | 無料 | なし | No | No | ★★☆☆☆ |
| **Shazam** | 音声認識 | 5+推定 | RapidAPI Key | プラン別 | Freemium | なし | No | No | ★★☆☆☆ |
| **Deezer** | 音楽 | 40+推定 | OAuth 2.0 | 不明 | 無料 | なし | No | No | ★★☆☆☆ |
| **SoundCloud** | 音楽 | 20+ | OAuth 2.1 (PKCE) | あり | 無料 | iOS/Android Kit | No | No | ★★★☆☆ |

---

## Tier 1: 深掘り分析

### 1. Spotify Web API

#### 概要・ポジショニング
Spotifyの楽曲メタデータ取得、プレイリスト管理、再生制御を外部アプリケーションから行うためのREST API。個人開発者からエンタープライズまで幅広く利用され、「API DXのゴールドスタンダード」として開発者コミュニティで高く評価されている。

#### エンドポイント一覧（主要カテゴリ）

| カテゴリ | 代表的エンドポイント | 説明 |
|---------|---------------------|------|
| **Albums** | GET /albums/{id}, GET /albums/{id}/tracks | アルバムメタデータ、トラック一覧 |
| **Artists** | GET /artists/{id}/top-tracks, /related-artists | アーティスト情報、関連アーティスト |
| **Tracks** | GET /audio-features/{id}, /audio-analysis/{id} | 楽曲の音響特徴量（テンポ、キー、エネルギー等） |
| **Playlists** | POST /playlists, PUT /playlists/{id}/tracks | プレイリストCRUD |
| **Search** | GET /search?type=track,artist,album | 横断検索 |
| **Player** | PUT /me/player/play, /pause, /next | 再生制御（Premium必須） |
| **Recommendations** | GET /recommendations?seed_tracks=... | パーソナライズ推薦 |
| **Shows/Episodes** | GET /shows/{id} | ポッドキャストコンテンツ |
| **Audiobooks** | GET /audiobooks/{id} | オーディオブック |
| **Users** | GET /me/top/tracks, /me/top/artists | ユーザーの嗜好データ |

#### 認証方式

| フロー | 用途 | 特徴 |
|--------|------|------|
| **Authorization Code** | サーバーサイドアプリ | 標準的なOAuth 2.0、リフレッシュトークン対応 |
| **Authorization Code + PKCE** | SPAやモバイル | セキュリティ強化版、公開クライアント向け |
| **Client Credentials** | サーバー間通信 | ユーザーコンテキスト不要、カタログデータ取得のみ |
| ~~Implicit Grant~~ | 廃止 | セキュリティ上の理由で非推奨 |

#### レート制限・クォータ
- 具体的な数値は非公開だが「Quota Modes」の概念が存在
- Development Modeと拡張モードがあり、2026年2月にDev Mode変更が実施された
- 一般的に報告されている値: アプリあたり約100リクエスト/30秒（ローリングウィンドウ）

#### 料金体系
- **完全無料**（API利用料なし）
- Spotify Premium（月額$11.99）が再生制御エンドポイントの利用に必要
- 商用利用にはSpotify Developer Terms of Service準拠が必要

#### SDK・ツール
- **公式SDK:** なし（これは意図的な設計判断。REST APIの品質が高いためSDK不要という思想）
- **公式Web Playback SDK:** ブラウザ上でSpotify再生を組み込むためのSDK
- **Developer Dashboard:** アプリ管理、クレデンシャル発行
- **コミュニティSDK:** spotipy (Python, GitHub 17k+ stars), spotify-web-api-ts-sdk (TypeScript, 公式に近い)

#### ドキュメント品質
- **構造:** Concepts / Tutorials / How-Tos / Reference の4層構造
- **Getting Started:** プロフィールデータ表示のハンズオンチュートリアル
- **OpenAPI仕様:** 完全なAPI仕様がOpenAPI形式で公開
- **コードサンプル:** cURL + 主要言語のサンプル
- **Changelog:** 定期的な更新履歴
- **評価: 業界最高水準のドキュメント**

#### 開発者コミュニティ
- **Spotify Developer Forum:** 公式コミュニティフォーラム
- **GitHub:** 公式リポジトリ + 膨大なコミュニティプロジェクト
- **Stack Overflow:** [spotify] タグで活発な議論

#### ユニークな機能
1. **Audio Features API:** 楽曲の音響特徴量（danceability, energy, valence, tempo等）を数値で取得。音楽分析やムードベースの推薦に不可欠
2. **Audio Analysis API:** 楽曲のセクション、ビート、バー、ティンブレの詳細分析データ
3. **Recommendation Engine API:** seed_tracks/artists/genres + tunable attributes（min/max/target）でパーソナライズ推薦
4. **Cross-Device Playback Transfer:** デバイス間での再生移行
5. **Queue Management:** 再生キューの操作

#### 制限・課題
- Premium必須（再生制御）
- AI/MLモデルのトレーニングへのデータ使用禁止
- ストリームリッピング禁止
- ダウンロード促進禁止
- Implicit Grant廃止に伴うマイグレーション負荷
- 30秒プレビューの単独サービス化禁止

#### BIL/TEXでの活用可能性
- **ブランド体験プロトタイプ:** Audio Features APIを活用したムードベースの広告体験
- **インタラクティブ広告:** プレイリスト作成を組み込んだブランドキャンペーン
- **データ分析:** 音楽嗜好データとターゲティングの連携可能性
- **リファレンスアーキテクチャ:** DX設計のベンチマーク

---

### 2. Twitch API

#### 概要・ポジショニング
Amazon傘下のライブストリーミングプラットフォームTwitchが提供するREST API。配信管理、チャット操作、視聴者エンゲージメント、アナリティクスなど、ライブコンテンツエコシステム全体をカバー。**Amazon傘下で最もSpotify Web APIに近いDX品質**を実現している。

#### エンドポイント一覧（全30カテゴリ、156+エンドポイント）

| カテゴリ | EP数 | 代表的エンドポイント |
|---------|------|---------------------|
| **Ads** | 3 | Start Commercial, Get/Snooze Ad Schedule |
| **Analytics** | 2 | Extension/Game Analytics |
| **Bits** | 3 | Leaderboard, Cheermotes, Transactions |
| **Channels** | 4 | Get/Modify Channel Info, Editors, Followers |
| **Channel Points** | 6 | Custom Rewards CRUD, Redemptions |
| **Charity** | 2 | Campaign, Donations |
| **Chat** | 15 | Chatters, Emotes, Badges, Send Message/Announcement/Shoutout |
| **Clips** | 4 | Create/Get Clips, Downloads |
| **Conduits** | 6 | Conduit/Shard CRUD |
| **Extensions** | 11 | Config, Secrets, PubSub, Bits Products |
| **EventSub** | 3 | Subscription CRUD |
| **Games** | 2 | Top Games, Game Search |
| **Guest Star (Beta)** | 11 | Session/Invite/Slot Management |
| **Moderation** | 21 | AutoMod, Bans, Blocked Terms, Shield Mode, Warnings |
| **Polls** | 3 | Get/Create/End Poll |
| **Predictions** | 3 | Get/Create/End Prediction |
| **Raids** | 2 | Start/Cancel Raid |
| **Schedule** | 5 | Schedule CRUD, iCalendar |
| **Search** | 2 | Categories, Channels |
| **Streams** | 5 | Stream Key, Markers, Followed Streams |
| **Subscriptions** | 2 | Broadcaster Subs, User Sub Check |
| **Tags** | 2 | All/Stream Tags |
| **Teams** | 2 | Channel/Team Info |
| **Users** | 9 | User CRUD, Block List, Extensions |
| **Videos** | 2 | Get/Delete Videos |
| **Whispers** | 1 | Send Whisper |

#### 認証方式

| 方式 | 用途 |
|------|------|
| **OAuth 2.0 (Authorization Code)** | ユーザーアクション（チャット送信、チャネル管理等） |
| **OAuth 2.0 (Client Credentials)** | App Access Token（公開データ取得） |
| **JWT (JSON Web Tokens)** | Extensions専用（Extension Secret署名） |

- スコープベースの細粒度パーミッション（`channel:edit:commercial`, `chat:read`, `moderator:read:followers`等）
- エンドポイントごとにUser/App Access Tokenの要件が明確に文書化

#### レート制限・クォータ
- **動的レート制限:** ヘッダーで残りリクエスト数を返却
- **一般的な値:** 800ポイント/分（App Access Token）、ユーザートークンは異なる
- **レスポンスヘッダー:** `Ratelimit-Limit`, `Ratelimit-Remaining`, `Ratelimit-Reset`

#### 料金体系
- **完全無料**（API利用料なし）
- Twitch Partners/Affiliatesプログラムとは独立

#### SDK・ツール
- **Twitch CLI:** 公式コマンドラインツール。API呼び出し、OAuthトークン取得、EventSubテスト、リソース管理が可能
- **公式SDK:** なし（CLIが代替）
- **コミュニティSDK:** tmi.js (Chat), TwitchLib (.NET), pytwitchapi (Python) 等多数

#### ドキュメント品質
- **Getting Started:** 「Call your first Twitch API in minutes」-- 即座にAPI体験可能
- **構造:** Concepts / Tutorials / Reference / Guides
- **API Reference:** 全エンドポイントの詳細仕様（リクエスト/レスポンス例付き）
- **Breaking Changes Policy:** 変更プロセスが明確に文書化
- **ステータスダッシュボード:** devstatus.twitch.tv
- **評価: Spotifyに匹敵する高品質**

#### 開発者コミュニティ
- **TwitchDev Chat:** link.twitch.tv/devchat（Discord相当）
- **Twitter/X:** @twitchdev
- **GitHub:** github.com/twitchdev
- **TwitchCon:** 年次開発者カンファレンス
- **Meetups:** コミュニティミートアッププログラム
- **開発者ブログ:** 定期更新
- **開発者ショーケース:** コミュニティプロジェクト紹介

#### ユニークな機能
1. **EventSub:** Webhookベースのリアルタイムイベント通知システム。ポーリング不要で、配信開始・チャンネルポイント引換・サブスクリプション等のイベントをリアルタイム受信
2. **Extensions:** Twitch独自の拡張機能システム。配信画面上にインタラクティブなオーバーレイやパネルを追加可能
3. **Channel Points:** カスタムリワードの作成・管理。視聴者エンゲージメントの独自メカニクス
4. **Predictions/Polls:** ライブ配信中のリアルタイム投票・予測機能
5. **Drops:** ゲーム内アイテムの視聴報酬配布システム
6. **Hype Train:** チャネルのエンゲージメントスパイク検出
7. **Guest Star (Beta):** ゲスト出演管理機能

#### 制限・課題
- Extensions開発にはJWT署名の理解が必要
- 一部のエンドポイントがBeta段階
- レート制限の動的変動により予測が困難
- Chatbot開発にはIRC/WebSocket接続が別途必要

#### BIL/TEXでの活用可能性
- **ライブコマース体験:** Channel Points + Predictions を活用したインタラクティブ広告
- **Extensions:** ブランドスポンサーのカスタムオーバーレイ
- **EventSub:** リアルタイムキャンペーンのトリガー（特定チャネルイベントに連動した広告配信）
- **Drops連携:** ブランドコラボのデジタルアイテム配布
- **DXリファレンス:** Amazon傘下で最も洗練されたAPIとして、社内API設計のベンチマーク

---

### 3. IMDb API

#### 概要・ポジショニング
世界最大の映画・TV・エンターテインメントデータベースIMDbのデータをGraphQL APIとバルクデータで提供。AWS Data Exchange経由の**エンタープライズ向けB2Bサービス**であり、セルフサービス型のデベロッパーAPIとは根本的に異なるアプローチを取る。

#### エンドポイント一覧
GraphQLベースのため固定エンドポイントではなく、クエリでデータを取得：

| データドメイン | 内容 |
|--------------|------|
| **Titles** | 映画・TVシリーズ・ゲーム等のメタデータ（1,000万+タイトル） |
| **Names** | キャスト・クルー情報（1,400万+人物） |
| **Ratings** | ユーザー評価（月間2.5億+訪問者のデータ） |
| **Box Office** | Box Office Mojoとの統合データ（日次・週末・週次・累計興行収入） |
| **Popularity** | 人気度メーター（タイトル・プロフェッショナルのランキング） |
| **Reviews** | ユーザーレビュー |
| **Parents Guide** | コンテンツ警告（暴力・性的表現等の深刻度評価） |
| **Trivia & Goofs** | トリビア・ミス情報 |

#### 認証方式
- AWS Data Exchange サブスクリプション経由
- AWS IAM認証（Data Exchange APIコール）
- セルフサービスのAPIキー発行なし

#### レート制限・クォータ
- 非公開（AWS Data Exchangeの契約条件に依存）

#### 料金体系

| ティア | 内容 |
|-------|------|
| **IMDb Ratings** | 基本タイトルデータ + 1-10スター評価 |
| **IMDb Essential Metadata** | 拡張メタデータ + 名前情報 |
| **IMDb + Box Office Mojo** | Essential + 興行収入データ |
| **Add-On Datasets** | Popularity, Reviews, Parents Guide, Trivia等 |

- 価格は非公開、営業問い合わせベース
- 無料トライアルの記載なし

#### SDK・ツール
- 専用SDKなし
- AWS SDKを通じたData Exchangeアクセス
- GraphQLクエリはスキーマドキュメントに基づいて構築

#### ドキュメント品質
- developer.imdb.com にスキーマドキュメントあり
- セルフサービス型のPlaygroundやインタラクティブドキュメントは限定的
- 評価: エンタープライズ品質だが開発者フレンドリーではない

#### 開発者コミュニティ
- 公開コミュニティなし（B2Bモデルのため）
- サポートはIMDbコンタクトフォーム経由

#### ユニークな機能
1. **世界最大のエンタメデータベース:** 1,000万+タイトル、1,400万+人物のカバレッジ
2. **GraphQLアーキテクチャ:** 必要なデータのみを柔軟に取得
3. **Box Office Mojo統合:** 興行収入データの唯一の信頼できるソース
4. **日次データ更新:** 全データプロダクトが毎日更新
5. **Popularity Meters:** リアルタイムのトレンドランキング

#### 制限・課題
- セルフサービスサインアップ不可（営業経由）
- AWS Data Exchange必須（直接API不可）
- 価格非公開
- 個人開発者やスタートアップには事実上アクセス不可
- GraphQLスキーマの公開ドキュメントが限定的

#### BIL/TEXでの活用可能性
- **コンテンツメタデータ連携:** Prime Videoキャンペーンでの映画/TV情報自動取得
- **トレンドデータ:** Popularityメーターを活用したリアルタイムコンテンツ推薦
- **Box Officeデータ:** 映画プロモーション効果の測定
- **Amazon社内連携:** AWS Data Exchange経由でAmazon社内チームは比較的容易にアクセス可能

---

### 4. Amazon Music Web API (Phoenix)

#### 概要・ポジショニング
Amazon Musicのカタログデータ取得、ユーザーライブラリ管理、再生制御を外部パートナーに提供するREST API。内部コードネーム「Phoenix」。旧Garuda APIからの後継として設計され、よりシンプルな統合・高速なオンボーディング・パートナーの自律性を目指す。**現在Closed Beta。**

#### エンドポイント一覧

| カテゴリ | 代表的エンドポイント | ステータス |
|---------|---------------------|-----------|
| **Catalog - Albums** | アルバムメタデータ | GA (Beta) |
| **Catalog - Artist** | アーティスト情報 | GA (Beta) |
| **Catalog - Track** | トラック情報 | GA (Beta) |
| **Catalog - Browse** | ブラウズ/ディスカバリー | GA (Beta) |
| **Catalog - Podcast** | ポッドキャストコンテンツ | GA (Beta) |
| **Catalog - Station** | ステーション | GA (Beta) |
| **Search** | カタログ横断検索 | GA (Beta) |
| **Views** | 最適化されたUIデータ | GA (Beta) |
| **User** | ユーザーライブラリ | 要パーミッション |
| **Playlist** | プレイリストCRUD | 要パーミッション |
| **Player / Playback** | 再生制御、キュー管理 | 2023年10月追加 |
| **Market** | マーケット情報 | GA (Beta) |

#### 内部Wiki情報（Amazon社内）

**3P Web API & Developer Portal (2022年12月Wiki)**
- 2022年にDeveloper Portal (`developer.amazon.com/docs/music/`) とWeb APIを公式ローンチ
- 10+パートナーがオンボード済みまたは進行中: TuneMyMusic, BandsInTown, Linkfire, Found.ee等
- それまではAPIドキュメントが非公開で、Solutions Architectがメール経由で仕様を手動共有していた
- Click-through法的合意によるオンボーディング簡略化
- クラウドネイティブ技術で構築、スケーラブルで信頼性の高いAPIを目指す

**Playback API (2023年10月Wiki)**
- Ubiquity PlatformチームがPlayback APIを2023年10月6日にローンチ
- 1P/3P両方で本番稼働、3Pはフィードバック収集までBeta
- キュー管理・キュー作成・DRM・アップセルフローをサポート
- 音楽とポッドキャストの統合再生APIを単一インターフェースで提供
- **戦略的パートナーシップ:**
  - **BeReal:** Alphaパートナー。投稿に再生中の楽曲をタグ付け（YAコミュニティへの入口）
  - **Tesla:** 2024年にAmazon Music車載統合を目指し、WebPlayback SDKをBD APEXチームが構築
  - **BIL (Brand Innovation Lab):** Wyclef JeanのPaper Rightを使ったFire TVカスタムランディングページ。TIAA #retirementinequalityキャンペーンで楽曲ストリームごとに$1寄付
- Garuda APIからの全パートナー移行を促進（Sonos含む）
- 内部Slack: #music-3p-interest

#### 認証方式
- **Login With Amazon (LWA):** OAuth 2.0 Bearer Token
- **x-api-key:** Security Profile ID（Client IDとは異なる、Amazon Music Serviceによる有効化が必要）
- スコープ: `profile` 等

#### レート制限・クォータ
- TPS (Transactions Per Second) 制限あり
- 429レスポンスで「Too Many Requests」
- 指数バックオフ推奨
- 具体的数値は非公開、上限変更はAmazon Music POCに連絡

#### 料金体系
- Closed Betaのため非公開
- パートナー向け無料アクセスと推定

#### SDK・ツール
- 公式SDKなし
- RESTful APIで標準HTTPクライアントから利用可能
- Developer Forum: community.amazondeveloper.com
- WebPlayback SDK: BD APEXチームがTesla統合用に構築中（社内）

#### ドキュメント品質
- developer.amazon.com上に構造化されたドキュメント
- スキーマ、エラーコード、リクエストヘッダーの説明あり
- cURLサンプル提供
- 「Preview status」の注記あり（内容変更の可能性）
- 多言語対応（英語・日本語・中国語）

#### ユニークな機能
1. **Views API:** UIに最適化されたデータ取得。キャッシュ戦略による高速レスポンス
2. **統合Playback:** 音楽・ポッドキャスト・ステーションを単一APIで再生
3. **Deep Linking:** Amazon Musicアプリへの直接リンク
4. **Playlist Transfer:** 他サービスからのプレイリスト移行
5. **全ティアサポート:** Free/Prime/Unlimited全サブスクリプションティアに対応

#### 制限・課題
- **Closed Beta:** 承認済みパートナーのみアクセス可能
- Security Profile IDの事前有効化が必要（セルフサービスではない）
- ドキュメントがPreview状態で変更の可能性あり
- Device APIがdeprecated
- 公開開発者コミュニティが未成熟

#### BIL/TEXでの活用可能性
- **直接的な活用実績あり:** BILが既にPlayback APIを使用（Wyclef Jean / TIAAキャンペーン）
- **ブランドキャンペーン:** 楽曲再生をトリガーとしたインタラクティブ広告体験
- **プレイリスト連携:** ブランドキュレーションプレイリストの作成・共有
- **ストリーミング連動寄付:** 再生回数連動のチャリティキャンペーン
- **Fire TV統合:** カスタムランディングページでの音楽体験

---

## Tier 2: 概要比較

### 5. Amazon Ads API

**概要:** Amazon広告プラットフォームのプログラマティックアクセスAPI。Sponsored Products/Brands/Display、DSP、Amazon Attribution等を管理。

**比較ポイント:**
| 項目 | 詳細 |
|------|------|
| 認証 | Login With Amazon (LWA) OAuth 2.0 |
| エンドポイント | 100+推定。Campaigns, Ad Groups, Keywords, Targets, Reports, Audiences |
| SDK | Java, Python, JavaScript (公式) |
| 料金 | 無料（広告費用は別途） |
| レート制限 | API別に設定 |
| ユニーク機能 | Amazon Attribution（外部トラフィック測定）、DSP API、Brand Metrics |
| DX課題 | ドキュメントがJavaScript依存で静的レンダリングが困難、認証フローが複雑 |

**BIL/TEX関連:** BILチームの中核ツール。広告キャンペーンの自動化、レポーティング、DSP連携で直接活用。

---

### 6. Apple Music API (MusicKit)

**概要:** Apple Musicのカタログデータ取得・ユーザーライブラリ管理・再生制御を提供。iOS/macOS/tvOS/watchOS/visionOS/Web/Androidの全プラットフォーム対応が強み。Spotifyの直接競合。

**比較ポイント:**
| 項目 | 詳細 |
|------|------|
| 認証 | Developer Token (JWT署名) + User Token (Apple Music認証) |
| プラットフォーム | Swift (MusicKit), JavaScript (MusicKit JS Beta), Android SDK |
| 料金 | 無料（Apple Developer Program $99/年が前提） |
| ユニーク機能 | Apple Music Replay（年間統計）、Trial Membership提供機能、visionOS対応 |
| DX | Apple純正フレームワークは高品質。Web/Androidは成熟度が低い |
| 制限 | MusicKit JS未だBeta、Android版は2ライブラリ分離、レート制限非公開 |

**Spotifyとの主な差異:**
- Spotifyは全プラットフォームで統一REST API → MusicKitはプラットフォーム別SDK
- SpotifyはAudio Features/Analysis APIが強力 → Apple Musicに相当機能なし
- Apple MusicはAffiliate Programでマネタイズ可能
- Apple MusicはReplay（Spotify Wrapped的機能）のAPI提供

---

### 7. PA-API 5.0 (Product Advertising API)

**概要:** Amazonアソシエイト（アフィリエイト）向けの商品データAPI。商品検索、ASIN詳細、価格・在庫情報を取得。

**重要:** **2026年4月30日で廃止予定。Creators APIへの移行が必要。**

**比較ポイント:**
| 項目 | 詳細 |
|------|------|
| エンドポイント | 4つのみ（GetItems, SearchItems, GetBrowseNodes, GetVariations） |
| 認証 | Amazon Associate認証 + AWS Signature V4 |
| 料金 | 完全無料 |
| SDK | 複数言語対応 + Scratchpad（テストツール） |
| ユニーク機能 | 22リージョン対応、Prime判定、販売ランク |
| 制限 | POST限定、廃止予定、「もうメンテされていない」との記載 |

**BIL/TEX関連:** 商品メタデータ取得の基盤だが、Creators API移行後の機能変更に注意。

---

### 8. SP-API (Selling Partner API)

**概要:** Amazon最大規模のAPI群。セラー・ベンダー向けの注文管理、出品、フルフィルメント、財務、レポート等を網羅。旧MWSの後継。

**比較ポイント:**
| 項目 | 詳細 |
|------|------|
| エンドポイント | 200+、25+カテゴリ |
| 認証 | LWA OAuth 2.0 + AWS Sig V4 + RDT (PII用) |
| SDK | C#, Java, JavaScript, Python, PHP |
| 料金 | 無料 |
| ユニーク機能 | Data Kiosk (GraphQL分析)、EventBridge連携、マルチロケーション在庫、SP-API Guard (セキュリティ) |
| DX | 充実したSDK・サンドボックス・レシピだが、認証フローが複雑。リージョン分断 |
| 制限 | 認証3種類の複雑さ、リージョン別認可、PII用RDTワークフロー、サービスプロバイダー承認待ち |

**BIL/TEX関連:** 直接関連は低いが、Amazon APIエコシステムの最大事例として設計パターンの参考になる。Data Kiosk GraphQLは先進的。

---

## Tier 3: ニッチAPI

### 9. Last.fm API
音楽リスニング履歴追跡「Scrobbling」の元祖。59メソッド、13カテゴリ。`track.scrobble`/`track.updateNowPlaying`がコア機能。**コミュニティ駆動の音楽メタデータ**として、類似アーティスト/トラック発見に強い。商用利用は要事前連絡。

### 10. MusicBrainz API
**オープンデータの音楽百科事典。** 13エンティティ（artist, recording, release等）をカバー。Lookup/Browse/Searchの3種リクエスト。**レート制限1リクエスト/秒**と厳格。非商用無料。リレーションシップモデルが非常に豊富で、音楽業界のWikipediaとして機能。

### 11. Genius API
歌詞と楽曲アノテーション（注釈）のプラットフォーム。OAuth 2.0認証。**ユニーク機能: ユーザーが歌詞にアノテーションを付加できるコラボレイティブモデル。** 歌詞の直接的なAPI提供は制限されており、Webスクレイピングとの併用が一般的。

### 12. Shazam API (via RapidAPI)
**オーディオフィンガープリント（音声認識）** が唯一無二の機能。RapidAPI経由で提供。音声サンプルから楽曲を特定するエンドポイントがコア。チャート・推薦機能もあり。Freemiumモデル。Apple傘下。

### 13. Deezer API
フランス発の音楽ストリーミングサービスAPI。OAuth 2.0認証。楽曲・アルバム・アーティスト・プレイリスト等の標準的なエンドポイント。30秒プレビュー再生が特徴的。ドキュメントはログイン必須で、DX面でSpotifyに大きく劣る。

### 14. SoundCloud API
クリエイター中心の音楽プラットフォーム。**OAuth 2.1 (PKCE必須)** と最新認証仕様を採用。**ユニーク機能: タイムスタンプ付きコメント（楽曲の特定時点にコメント可能）、500MBまでのトラックアップロード。** oEmbed対応のウィジェット埋め込みが容易。クリエイターエコノミーとの親和性が高い。

---

## BIL/TEX 活用の視点

### 1. 既存の活用実績を拡大
Amazon Music Phoenix APIは**BILが既に使用実績あり**（Wyclef Jean / TIAAキャンペーン）。Playback APIの公開拡大に伴い、以下のようなキャンペーンが実現可能:
- 楽曲ストリーム連動のチャリティ/寄付キャンペーン
- ブランドキュレーションプレイリスト体験
- Fire TV / Echoデバイス上の音楽インタラクティブ広告

### 2. Twitch APIとの連携
BILのTwitch連携キャンペーンにおいて:
- **Extensions:** ブランドスポンサーオーバーレイ（Amazon商品連動）
- **Channel Points + Predictions:** 視聴者参加型の広告体験
- **Drops:** ブランドデジタルアイテムの配布
- **EventSub:** リアルタイムキャンペーントリガー

### 3. DX設計のベンチマーク
Spotify Web APIとTwitch APIが示す「良いAPI DX」の原則:
- **シンプルな認証:** OAuth 2.0の標準フロー
- **セルフサービスオンボーディング:** ダッシュボードでのアプリ登録
- **インタラクティブドキュメント:** Playground / Try It機能
- **CLIツール:** 開発ワークフローの加速
- **イベント駆動:** ポーリング不要のリアルタイム通知
- **活発なコミュニティ:** フォーラム、Discord、ショーケース

### 4. 複合APIプロトタイプのアイデア

| プロトタイプ | 使用API | コンセプト |
|-------------|---------|-----------|
| **Music-Powered Brand Page** | Amazon Music + IMDb | Prime Video作品のサントラをAmazon Musicで再生するブランドページ |
| **Live Commerce + Music** | Twitch + Amazon Music | ライブ配信中のBGM連動商品推薦 |
| **Mood-Based Ad Targeting** | Spotify Audio Features (参考) | 音楽の「ムード」に合わせた広告クリエイティブ最適化 |
| **Creator Playlist Campaign** | Amazon Music + SoundCloud | インディーアーティストとブランドのコラボプレイリスト |
| **Shazam-to-Buy** | Shazam + PA-API/Creators API | CMの曲をShazamして関連商品をAmazonで購入 |

### 5. Amazon Music API (Phoenix) への提言
Mattの「Imagine if we had something like this」に対するアクションとして:
- **Closed Beta → Public GA推進:** #music-3p-interestでDX改善のフィードバック提供
- **Audio Features的な機能:** 楽曲の音響メタデータ（テンポ、ムード等）があれば広告ターゲティングに直結
- **EventSub相当:** 再生開始/終了イベントのリアルタイム通知があればキャンペーントリガーに使える
- **SDK提供:** 少なくともTypeScript/Python SDKがあればDXが大幅向上

---

## 所感・考察

### Spotifyが「愛される」理由の本質
Spotify Web APIのDXの高さは、単にドキュメントが良いだけではない。**「開発者が想像するユースケースの95%を、APIの組み合わせで実現できる」** という設計の包括性が核心である。Audio Features、Recommendations、Player Control、Playlistの4つの柱が、音楽体験のほぼ全てをカバーしている。

### Amazon Music Phoenix APIの現在地とギャップ
Phoenix APIはSpotifyと同様のエンドポイント構造を持つが、以下のギャップがある:
1. **アクセス性:** Closed Beta vs. セルフサービス
2. **音楽分析データ:** Audio Features/Analysis相当がない
3. **推薦エンジンAPI:** Spotify Recommendations相当がない
4. **開発者コミュニティ:** ほぼ不在 vs. 活発なエコシステム
5. **SDK:** なし vs. コミュニティSDK多数

### Twitch APIの示唆
Twitch APIはAmazon傘下にありながら独自の優れたDXを実現しており、「Amazon傘下でもSpotify級のAPIは作れる」ことを証明している。EventSub、Extensions、CLIといった先進機能は、Amazon Music APIや将来のAmazon APIにも応用可能なパターンを示している。

### GraphQL vs. REST
IMDbはGraphQL、SP-APIのData KioskもGraphQL、一方でSpotify/Twitch/Amazon MusicはREST。音楽・エンタメ系APIでは、**エンドポイントの発見可能性と直感性が重要**であるため、RESTの方がDXに優れる傾向がある。ただし、複雑なリレーションシップクエリにはGraphQLが有利。

### 市場トレンド
- **PA-API 5.0の廃止** (2026年4月) → Creators APIへの移行は新たな機会
- **OAuth 2.1への移行:** SoundCloudが先行（PKCE必須化）
- **リアルタイム化:** EventSub (Twitch) / EventBridge (SP-API) がトレンド
- **AI/ML制限:** Spotify明示的にAIトレーニング禁止 → データ利用規約の厳格化傾向

---

*このレポートは2026年3月6日時点の公開情報および Amazon社内Wiki情報に基づく。各APIの仕様は随時変更される可能性がある。*
