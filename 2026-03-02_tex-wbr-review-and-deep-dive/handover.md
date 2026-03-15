# Handover Document
**Topic:** TEX WBR & Weekly Meeting 定期レビュー
**Date:** 2026-03-13
**Status:** 進行中（Weekly Routine 確立、WBR W11読み込み完了）

---

## 背景
TEXチームのWBR・Weekly Meetingの定期レビューを体系化。元々はWBR PDFの単発レビュー（3/2-3/3）から始まり、3/12に週次ルーティンとして `/weekly` スキルを構築。WBR（BIL/TEX隔週交互）とTEX Weekly Meeting（毎週）のチェックを自動化する仕組みを整備した。

## 現在の状況

### `/weekly` スキル — 構築完了（3/12）
- パス: `~/.claude/skills/weekly/SKILL.md`
- サブコマンド: `/weekly`, `/weekly wbr`, `/weekly meeting`, `/weekly all`, `/weekly status`
- 奇数週/偶数週の自動判定（ISO週番号）
  - 奇数週: TEX NA WBR + TEX EU/APAC/MENA WBR + WW TEX WBR
  - 偶数週: WW BIL WBR
- `/daily` との連携: 曜日別リマインド提案（SKILL.md内に記載、`/daily` への実装は未着手）
- **WBR Highlights作成（奇数週金曜）**: 3/13追加。自分の活動からHighlight/Lowlightを作成しNotionに記録。ケイデンス表とStep D1の金曜奇数週に追加済み

### WBR W11 読み込み（3/12 奇数週）

**TEX NA WBR:**
- Amazon Canvas API Onboarding — PV watch history + CustomerME オンボーディング承認済み。BGW 背後にホスティング計画
- Mobile CX / SSE — LMDT と SSE flow finalization、STS onboarding へ
- 8th Wall (AB Library) — distributed binary engine リリース、法務確認中
- 8Ps FY26 残り優先順: Preferred Extension Program, Unified Metrics Hub, TEX Iterations as PN platform

**TEX EU/APAC/MENA WBR:**
- (AU) M&M's Sports x Australian Open — AWS Rekognition Custom Labels、初の ML/CV 実装
- (MENA) Sonos — $100K → $818K、immersive audio experience
- PV Live Sports API — Bindu が SDP 統合 feasibility 完了（36 sports, 432 leagues）
- PAWS Deprecation — Retail プロモーションシステム廃止、代替 capabilities 低下リスク
- DT Hiring — L5 backfill、IT/UK sourcing 開始

**WW TEX WBR:**
- 3/12分は未記入（会議前）。02/26内容:
- BIL CMS Beta → Q2 GA、Security Review が critical path
- OBA Tier 1 拡大検討（PVS以外のFTVスポンサー）
- AI-Accelerated Prototyping (US XD) — Claude で 4時間 hi-fi prototype

### TEX EU Weekly Meeting（3/11）
- Billy: Nova Act prototype + BrandPushNotificationService demo
- Francesco: PV API Discovery + Nespresso 3D scrollytelling
- Bindu: PV Live Sports data Discovery
- Lowlight: WebFlow accessibility

### TEX Info Sources 更新（3/12）
- ミーティングケイデンステーブルを `TEX-Info-Sources.md` に追記完了

### Meeting PDF 場所確認（3/12）
- APAC DT Huddle PDF が 2/19 以降未更新（3週間古い）→ 再エクスポート必要
- ディレクトリ構成分析: 現構造維持推奨（`QBR:MBR:WBR` → `Reviews`、`Meeting Agenda` → `Meetings` へのリネームは任意改善）

### WBR深掘り（3/2-3/3 — 過去セッション）
- 4トピック深掘り完了: Canvas API=STS比喩、FAST=ASRパイプライン、PetArmor=AI Pet Recs、Olly=LLMなし
- 詳細は history/ 参照

## 成果物一覧
```
2026-03-02_tex-wbr-review-and-deep-dive/
├── handover.md（本ファイル）
├── history/
│   ├── 2026-03-02_handover.md（初回版）
│   ├── 2026-03-03_handover.md（深掘り完了版）
│   ├── 2026-03-05_handover.md（OP1分離前）
│   └── 2026-03-06_handover.md（Weekly Routine化前）
├── notes/
│   ├── fast-research-findings.md
│   ├── petarmor-campaign-research.md
│   ├── canvas-api-research.md
│   ├── olly-hny-backend-research.md
│   ├── au-op1-planning-2027-jp.md（コピーは bil-op1-planning-fy27 にも）
│   └── au-op1-brainstorm-prep.md（コピーは bil-op1-planning-fy27 にも）
└── artifacts/（なし）

別成果物:
├── ~/.claude/skills/weekly/SKILL.md（/weekly スキル）
└── TEX-Info-Sources.md（ケイデンステーブル追記）
```

## アクションアイテム
| # | 期限 | アクション | ステータス |
|---|------|-----------|----------|
| 1 | - | `/daily` に曜日別 `/weekly` リマインド連携を実装 | 未着手 |
| 7 | ✅ | `/weekly` に WBR Highlights作成（奇数週金曜）を追加 | 完了(3/13) |
| 2 | - | APAC DT Huddle PDF 再エクスポート（Loop → PDF） | 未着手 |
| 3 | 来週 | WW TEX WBR 3/12分を再読み込み（会議後に更新される） | 未着手 |
| 4 | 来週火 | BIL WBR 読み込み（偶数週 W12） | 未着手 |
| 5 | - | aleckunkに確認: Phase 2スコープ、FAST onboarding、ASR filing | 未着手（前回から継続） |
| 6 | - | ディレクトリリネーム検討（QBR:MBR:WBR → Reviews 等） | 保留 |

## 重要な判断ログ
- **Weekly Routine のスキル化**: `/daily` に統合せず、独立スキル `/weekly` + `/daily` からのリマインドのハイブリッド方式を採用（C案）。理由: daily の肥大化防止 + weekly 単体での完結性確保
- **ディレクトリ構成**: WBR と Meeting Agenda の統合は見送り。現構造維持を推奨（WBR同士の横断比較しやすさを優先）
- **Deep Dive 優先候補（W11）**: 1) PV Live Sports API（live-sports-api-discovery と直結）、2) PAWS Deprecation（システミックリスク）、3) Canvas API Onboarding（パーソナライゼーション基盤）

## 関連トピック
- `2026-03-06_bil-op1-planning-fy27` — OP1プランニング（本トピックから分離）
- `2026-02-26_tex-prime-video-sse-initiative` — SSE Initiative
- `2026-03-09_tex-prime-video-live-sports-api-discovery` — PV Live Sports API（WBR Deep Dive候補と直結）
- `2026-03-04_au-bil-pv-growth-engagement` — Sean Dylkeミーティング結果
- `2026-02-23_sse-prototypes` — SSEプロトタイプ（Fidelity + SSE Viewer）
- `2026-02-26_cat-decoder-tech-case-study` — Cat Decoder
- `2026-02-25_tex-survey-analysis` — TEX FY26 Survey分析
- `2026-02-23_bil-q4-qbr-revenue-analysis` — BIL Q4 QBRレベニュー解析
- `2026-02-24_tex-info-sources-update` — Info-Sourcesテーブル（ケイデンス追記済み）
- `2026-03-03_daily-task-management` — Daily Task Management（`/weekly` 連携先）
- `2026-03-11_dine-2.0-tech-feasibility` — Dine 2.0（M&M's AU Rekognition の関連技術）
