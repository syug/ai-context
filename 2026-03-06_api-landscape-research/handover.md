# Handover Document
**Topic:** Public API Landscape リサーチ — Spotify Web API 類似調査 + PV API
**Date:** 2026-03-07
**Status:** 完了

---

## 背景

Matt Bryant が Slack DM で Spotify Web API を共有し「Imagine if we had something like this :cry:」とコメント。これをきっかけに、Amazon社内外の類似APIを網羅的に調査した。

## 現在の状況

### 調査完了・レポート保存済み

#### 1. API Deep Dive Report（14 API比較）
- **Tier 1（深掘り）:** Spotify Web API、Twitch API、IMDb API、Amazon Music Web API (Phoenix)
- **Tier 2（概要比較）:** Amazon Ads API、Apple Music API (MusicKit)、PA-API 5.0、SP-API
- **Tier 3（ニッチ）:** Last.fm、MusicBrainz、Genius、Shazam、Deezer、SoundCloud

主要発見:
- **Twitch API** が Amazon傘下で最もSpotifyに近い（140+エンドポイント、優秀なドキュメント）
- **IMDb API** が GraphQL ベースでメディアメタデータの宝庫
- **Amazon Music Web API (Phoenix)** が Closed Beta で存在（api.music.amazon.dev）。BILがパートナーリスト
- **Spotify の Audio Features/Analysis は唯一無二** — 他APIに代替なし

#### 2. Prime Video API Landscape
- **Prime Video に Spotify のような Public API は存在しない**（Netflix/Disney+/Max も同様）
- 社内 API surface は豊富:
  - IVA (Interactive Video Ads) — Shoppable/Pause Ads、Add to Cart エンドポイント
  - Shop the Show — 二画面同期コマース、145タイトル+TNF対応
  - SDP (Sports Data Platform) — Static/Real-Time/Matching/Distribution API
  - Fire TV Integration SDK — 唯一の公開開発者プログラム
- 競合比較: Rokuのみ公開開発者プログラムあり

### Matt Bryant への返信
- IMDb API リンク共有 + "we really want that level of APIs for PV, at least for internal usage" — 送信済み

## 成果物一覧

```
2026-03-06_api-landscape-research/
├── artifacts/
├── notes/
│   ├── api-deep-dive-report.md   (34KB) — 14 API 深掘り比較レポート
│   └── prime-video-api-research.md (21KB) — PV API Landscape レポート
└── handover.md
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| - | - | - | 全て完了 |

## 重要な判断ログ

- Agent による Google Drive への Write が権限問題で繰り返し失敗。メインスレッドから Python で JSONL output を解析し Write tool content を抽出して保存する方法で解決
- Asana にも調査結果サマリをコメント記録。html_text の `<br>` `<ul><li>` は Asana でタグがそのまま表示される問題あり → `\n` と `•` を使うフォーマットに修正

## 関連トピック

- `2026-03-05_slack-catchup` — Matt Bryant の DM がきっかけ
- `2026-02-26_tex-prime-video-sse-initiative` — PV API 調査は TEX SSE Initiative にも関連
- `2026-02-23_sse-prototypes` — PV 広告 API（IVA等）はプロトタイプ活用の可能性あり
