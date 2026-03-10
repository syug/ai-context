# Handover Document
**Topic:** FY26 プロトタイプ Ideation リサーチ（WebSocket・オーディオフィンガープリンティング・AI）
**Date:** 2026-03-05
**Status:** 進行中

---

## 背景

FY26 Goal #1「Innovative Ad Experiences & Prototyping」（Kingpin #1078451）に向けたプロトタイプアイデアの技術リサーチ。Prime Video セカンドスクリーン体験を軸に、WebSocket、オーディオフィンガープリンティング、AI モデルの3方向で調査を行った。

## 現在の状況

### WebSocket / MessageRoom（調査完了 → 不採用）

- **PARC既存プロトタイプ:** 3件（WebSocket Playground by jtransu、Fire TV second screen websockets by graleigh、Coca Cola Holiday by jtransu）
- **Brand Gateway MessageRoom:** BIL-Eチームの WebSocket ライブラリ。`@amzn/brand-gateway-client` パッケージ
  - Wiki: https://w.amazon.com/bin/view/BIL-E/AmazonBrandMessageRoom/
  - API: `MessageRoom.start<T>()` / `.join(roomId)` / `.broadcast(data)` / `.send(clientId, data)`
  - ルーム最大8接続、チケットベース認証、`amazon.com/bgw/invoke/message-room`
  - 500同時ユーザー超は事前に #bil-e-support に連絡
- **Maltesers Duos ブリーフ:**「Indecision Duel」1v1リアルタイム対戦。技術的には既存スタックで実現可能、チャレンジなし
- **判断: WebSocket方向はやめて、PV + AI に集中する**

### オーディオフィンガープリンティング x Prime Video（主軸）

- **PARC既存:** 0件 → First-of-its-kind
- **コンセプト:** モバイルがTV音声を聴取 → PVコンテンツ + 正確なタイムスタンプを特定 → セカンドスクリーンコンテンツをトリガー
- **結論: AIモデルは不要。伝統的DSP（Shazam式）が最適**
  - 理由: 正確なコンテンツ + タイムスタンプ特定はDSPの得意領域。AIは「何の音か」を理解するが「どの録音のどの位置か」は苦手
  - 長尺コンテンツ（30min-2hr）も問題なし: 1本~3.6MB、10,000本~36GB

#### ツール候補
| ツール | 特徴 |
|--------|------|
| **Olaf** | C/WASM、ブラウザで動く、100K曲を15GB。プロトタイプに最適 |
| **Dejavu** | Python、Shazam実装、5秒で100%精度。リファレンス |
| **ACRCloud** | 商用、Second Screen Sync製品が既存 |

#### 推奨アーキテクチャ
```
Phone Mic → Web Audio API (3-5sec) → FFT + peak extraction (WASM client-side)
  → fingerprint hashes (~200-500 bytes) → server lookup (~10-50ms)
  → content_id + timestamp → trigger second screen content
```

### AI / HuggingFace モデル（未着手）

- EC2ホスト可能なユニークなモデル探索はまだ未実施
- オーディオフィンガープリンティングには不要と判明したため、他のプロトタイプアイデアで活用を検討

### 関連PARC プロトタイプ（参考）

- **Fidelity Peek Portfolio SSE** (aleckunk/harfine) — PV「The Summer I Turned Pretty」と同期するセカンドスクリーン体験。SSE（タイムコードベース同期）であり音声認識ではない。UXの参考になる
- **Second Screen Viewer** (harfine) — SSEプレビュー内部ツール

## 成果物一覧

```
2026-03-05_prototype-ideation-research/
├── notes/
│   └── research-summary.md    # 全リサーチのサマリー（WebSocket, MessageRoom, 音声FP, ツール比較）
└── handover.md
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | - | Olaf WASM でブラウザベースの音声フィンガープリンティング PoC を作成 | 未着手 |
| 2 | - | PV コンテンツのインデックスパイプライン設計 | 未着手 |
| 3 | - | HuggingFace のユニーク/面白いモデル探索（EC2ホスト候補） | 未着手 |
| 4 | - | Fidelity SSE (aleckunk/harfine) を UX リファレンスとしてレビュー | 未着手 |

## 重要な判断ログ

- **WebSocket方向を不採用:** 既存スタック（MessageRoom）で技術的チャレンジがなく、PARCにも3件の前例あり。イノベーティブな ad experience としてのインパクトが薄い
- **オーディオFPにAI不要:** Shazam式DSPが正確なコンテンツID+タイムスタンプ特定に最適。AIモデルは「何の音か」を汎化する設計であり、exact-match問題には不向き。レイテンシ・計算コスト・クライアント実行可能性すべてでDSPが優位
- **Olafを第一候補に:** WASM対応でブラウザ動作可能、100K曲実績、ポータブルC。ただしAGPL-3.0ライセンスとUS特許（US7627477 B2, US6990453）に注意

## 関連トピック

- [tex-prime-video-sse-initiative](../2026-02-26_tex-prime-video-sse-initiative/) — PV SSE イニシアティブ全体
- [sse-prototypes](../2026-02-23_sse-prototypes/) — Fidelity SSE + SSE Viewer
- [au-bil-pv-growth-engagement](../2026-03-04_au-bil-pv-growth-engagement/) — Sean Dylke PV Growth 連携
- [tex-wbr-review-and-deep-dive](../2026-03-02_tex-wbr-review-and-deep-dive/) — OP1ブレスト（AIトピック含む）
