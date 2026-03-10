# Handover Document
**Topic:** SSEプロトタイプ（Fidelity + SSE Viewer）のAUデモ環境構築
**Date:** 2026-03-02
**Status:** 進行中

---

## 背景

BIL-TEX チームの2つのプロトタイプ（Fidelity SSE Prototype、SSE Viewer Campaign）をAUリージョンのBrand Storeでデモ可能にする作業。元々USリージョン向けの設定だったものをAU対応し、MediaCentralデプロイで発生する問題を解決する。

TV番組「The Summer I Turned Pretty」Episode 1と連動するFidelity金融教育コンパニオンアプリのデモが目的。

3/2にトピック名を `fidelity-sse-viewer-demo-setup` → `sse-prototypes` にリネーム。Fidelity単体ではなくSSEプロトタイプ群としての位置づけに変更。

## 現在の状況

### 完了した作業

#### 1. vendor.js リンク切れ問題（両プロジェクト）
- Viteのchunk分割で `vendor.js` と `app.js` が分離 → MediaCentralアップロード後にハッシュ化されたファイル名で参照切れ
- **修正**: `manualChunks: () => 'app'` で単一バンドル化
- `upload.js`, `freeform.js`, テンプレートHTMLから vendor参照を削除

#### 2. リージョン設定（SSE Viewer）
- `constants.ts` にAU/USリージョン設定を追加（**デフォルトUS**に変更済み）
- AU: `primevideo.com/region/fe/detail/` / US: `amazon.com/gp/video/detail/`
- `titles.config.json` に `region` フィールド追加。タイトル選択時にリージョンに応じたURLフォーマットを自動切り替え
- `getPrimeVideoUrl(asin, region?)` にリージョン引数追加
- staleなクエリパラム（`pageTypeId=B0DT9CF111`, `qid`）を削除

#### 3. 画像・フォントBase64インライン化（両プロジェクト）
- MediaCentral単体デプロイでは、publicDir内のアセットのパスが壊れる問題
- **修正**: `assetsInlineLimit: 1000000` でアセットをバンドルにインライン化
- Fidelity: 画像10枚を `src/assets/image/` に移動 + `imageMap.ts` で管理、フォント11個を `src/assets/fonts/` からインライン
- SSE Viewer: `phone.png` をES import + inline styleに変更

#### 4. simulated mode自動再生（Fidelity）
- `useAppStore.ts` の `isPlaying` 初期値を `true` に変更

#### 5. ShopTheShow エラー調査
- Brand Store Preview URLに設置済みの `BIL-TEX-Prototype-ShopTheShowCampaign` がcompanion API 401でクラッシュ
- Fidelity/SSE Viewerとは無関係。Brand Store側の既存キャンペーンの問題。

#### 6. トピックリネーム（3/2）
- ディレクトリ: `fidelity-sse-viewer-demo-setup` → `sse-prototypes`
- エイリアス: `fidelity`, `viewer`, `sse-viewer` の3つで到達可能
- workdir: `~/Development/repos/brazil-ws/Prototypes` を紐付け
- 関連トピック（tex-sse-initiative）のクロスリファレンスを更新

### 判明した技術的制約

#### Prime Video iframe埋め込み制約（重大）
- **CMP (Classic Marketplace)**: US/UK/DE/JP → `amazon.{tld}/gp/video/detail/` でPVを提供。Brand Storeと同一オリジンなのでiframe埋め込み可能
- **ROW (Rest of World)**: AU含む → `primevideo.com` でPVを提供。Brand Store（`amazon.com.au`）とは別オリジン → `X-Frame-Options: SAMEORIGIN` でiframeブロック
- **結論: AU版PVのiframe埋め込みは技術的に不可能**

#### Companion API 401
- `https://api.us-east-1.prod.proxy.live.amazon.com/companion/progress` はUS Prime Videoセッションクッキーが必要
- AUからアクセスすると401。AU用エンドポイントは存在しない可能性大
- simulated modeでフォールバック可能（`isPlaying: true` に変更済み）

#### US Prime アカウント問題
- US Brand StoreでUS版タイトルのiframe表示は技術的に可能（同一オリジン）
- ただしPrime会員でないとPV再生不可
- US Prime登録にはUS発行クレカが必要

### constants.ts の `domain` フィールド
- `PrimeViewer.tsx:307` のiframeフォールバックURL構築でのみ使用
- `getPrimeVideoUrl()` がフルURLを返すため実質デッドコード

## 変更ファイル一覧

### BIL-TEX-Fidelity-SSEPrototype
| ファイル | 変更内容 |
|---------|---------|
| `build-tools/vite/vite.config.ts` | `assetsInlineLimit: 1000000` + `manualChunks: () => 'app'` |
| `build-tools/script/freeform.js` | `vendorsBundle` 関連削除 |
| `build-tools/script/upload.js` | `vendor.js` 参照削除 |
| `src/template/index.freeform.html` | vendorsBundle script削除 |
| `src/template/index.outside.freeform.html` | vendorsBundle script削除 |
| `src/store/useAppStore.ts` | `isPlaying: true` |
| `src/style/layout/_font.scss` | フォントパスを `/src/assets/fonts/` に変更 |
| `src/util/asset.ts` | `IMAGE_MAP` import + インラインアセット優先ルックアップ |
| `src/custom.d.ts` | 画像/フォントモジュール宣言追加 |
| `src/assets/image/` | 画像10枚（新規） |
| `src/assets/fonts/` | フォント11個（新規） |
| `src/assets/imageMap.ts` | 画像インポートマップ（新規） |

### BIL-TEX-Prototype-SSE-ViewerCampaign
| ファイル | 変更内容 |
|---------|---------|
| `build-tools/vite/vite.config.ts` | `assetsInlineLimit: 1000000` + `manualChunks: () => 'app'` |
| `build-tools/script/freeform.js` | `vendorsBundle` 関連削除 |
| `build-tools/script/upload.js` | `vendor.js` 参照削除 |
| `src/template/index.freeform.html` | vendorsBundle script削除 |
| `src/template/index.outside.freeform.html` | vendorsBundle script削除 |
| `src/config/constants.ts` | `REGIONS` オブジェクト（AU/US）、`DEFAULT_REGION: 'US'` |
| `src/config/titles.config.json` | `region` フィールド追加、US先頭 |
| `src/util/index.ts` | `getPrimeVideoUrl(asin, region?)` リージョン対応 |
| `src/components/Views/Home/Home.tsx` | リージョン連動URL生成、Brand Store URL `.com` に変更 |
| `src/components/Partials/PrimeViewer/PrimeViewer.tsx` | フォールバックドメインをリージョン設定から取得 |
| `src/components/Partials/MobileViewer/MobileViewer.tsx` | phone.png ES import + inline style |
| `src/components/Partials/SettingsModal/SettingsModal.tsx` | placeholder `.com` に変更 |
| `src/custom.d.ts` | 画像モジュール宣言追加 |
| `src/assets/image/phone.png` | 新規 |

## アクションアイテム

| # | アクション | ステータス |
|---|---|---|
| 1 | US Primeアカウント確保（US発行クレカ必要）またはチーム内テストアカウント | ブロッカー |
| 2 | US Brand Store + US Primeアカウントで完全動作確認 | 未着手（#1待ち） |
| 3 | AU Brand Storeでsimulated mode動作確認（PVなし） | 未着手 |
| 4 | URLパラメータで速度・開始位置制御を追加（`?speed=X&t=Y`） | 提案中 |
| 5 | デモ方式の最終決定（PV iframe vs 録画動画 vs Chrome拡張でヘッダ除去） | 検討中 |
| 6 | 両プロジェクトの変更をコミット・CR作成 | 未着手 |

## 重要な判断ログ

- **vendor.js問題の根本対策**: chunk分割を無効化して単一バンドルに。MediaCentralデプロイではファイル名がハッシュ化されるため、ファイル間の相対参照が壊れる。
- **画像インライン化を選択した理由**: MediaCentral単体デプロイ（CloudFrontなし）のため、アセット個別アップロード+physicalId管理は手間大。Base64インライン化でバンドルサイズは増えるが管理は簡単。
- **プロトタイプロジックは変更しない方針**: ポーリング、フォールバック等の既存ロジックは温存。設定値（URL、初期値）のみ変更。唯一の例外は `isPlaying: true`（simulated mode自動再生のため）。
- **デフォルトUSに変更**: AU companion APIが存在せず、PVもiframe不可のため、USベースで動作確認しAU切り替え可能にする方針に変更。
- **PV配信ドメイン構造**: CMP（US/UK/DE/JP）は `amazon.{tld}` でPV提供 → iframe OK。ROW（AU含む）は `primevideo.com` → iframe NG。社内Wiki「Prime Video Marketplaces, Restrictions, and Customers Geo Information」で確認。
- **Chrome拡張でX-Frame-Options除去**: デモ用回避策として提案中。`--disable-web-security` フラグも選択肢。
- **トピックリネーム (3/2)**: `fidelity-sse-viewer-demo-setup` → `sse-prototypes`。Fidelity単体ではなくSSEプロトタイプ群としての位置づけに整理。

## 関連トピック

- [tex-sse-initiative](../2026-02-26_tex-prime-video-sse-initiative/) — TEX SSE Initiative（SSEリサーチ・Seanミーティング）
- [command-mode-setup](../2026-02-23_command-mode-setup/) — Claude Codeのワークモード設定（同セッションで作業）
