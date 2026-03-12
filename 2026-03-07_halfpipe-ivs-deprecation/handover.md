# Handover Document
**Topic:** Halfpipe Live Video IVS コンポーネント廃止判断
**Date:** 2026-03-12
**Status:** 進行中（Mariko フォローアップ中 — Amazon Live/Twitch 代替可能か確認）

---

## 背景
BIL-Eが2026年11月までに全Halfpipeコンポーネントを廃止予定。BIL TEX EUがオーナーの「Live Video-IVS-2024-edition」コンポーネントについて、廃止 or Webflow移行を3/30までに決定する必要がある。Mirko Cappaiが Asana上でShugo/Billyにメンションし、Amazon Live以外のライブストリーミングニーズの有無を質問したのが発端。

## 現在の状況

### コンポーネント使用状況
- 使用ページ: 0件 / 訪問数: 0
- Component Owner: BIL TEX EU
- Asanaタスク: https://app.asana.com/1/8442528107068/project/1213527661372673/task/1213539247162724

### Asana上のやり取り（3件）
1. **Mirko Cappai** (3/5): Amazon Live以外でのライブストリーミングの可能性とWebflowコンポーネントの必要性を質問
2. **Billy Kwok** (3/5): Amazon Live未提供ロケール（MENA等）ではまだ必要。FireTVのIVS Webflowは別議論
3. **Shugo Saito** (3/6): AU/MENAは過去事例なく需要低（Twitch等代替あり）、JPはAmazon Live移行済み or Twitch利用なのでnice-to-have。Leigh/Kaiyiにメンションして意見求めた

### Slack（Chris/Mariko/Aayushi グループDM — C0AJSBTJFR9）
1. **Shugo** (3/10): IVS 廃止について3つの選択肢（Amazon Live / Twitch / IVS）を提示し、需要確認
2. **Mariko Ito** (3/11): JP Livestreaming に2026年需要あり。PVS + フルファネルキャンペーンコンセプトに組み込み済み。「unique full-funnel campaign designs that can only be executed on Amazon, as well as concepts leveraging Prime Video IP」
3. **Shugo** (3/12): フォローアップ — Amazon Live / Twitch で代替可能か、IVS でなければ実現できないユースケースがあるか確認。Beauty Festival = Amazon Live、Fuji Rock = Twitch の実績を提示

### JP における Live Streaming の代替手段
| 手段 | 利用可能 | 過去実績 |
|------|---------|---------|
| Amazon Live Player | JP ○ | Beauty Festival |
| Twitch Embedded Player | JP ○ | Fuji Rock |
| IVS Player (Halfpipe) | 廃止対象 | — |

## 成果物一覧
なし（Asanaコメント + Slackメッセージのみ）

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | 3/18 | Asanaチケットの Acknowledge | **完了** |
| 2 | 3/10 | Slack でChris/Mariko/Aayushiに確認メッセージ送信 | **完了**（グループDM） |
| 3 | — | Mariko フォローアップ — Amazon Live/Twitch 代替可能か確認 | **送信済み、返信待ち** |
| 4 | — | Leigh/Kaiyi からのAsana返信を待つ | 未回答 |
| 5 | 3/30 | Migration Decision を確定（Deprecate or Webflow移行） | 未着手 |

## 重要な判断ログ
- 使用ページ0件のため、Deprecateが自然な選択肢
- JPは Amazon Live / Twitch の2つの代替手段が利用可能
- **Mariko（JP SM Lead）が JP Livestreaming 需要ありと回答（3/11）** — ただしこれは「Livestreaming 一般」の需要であり、「IVS でなければダメ」とは言っていない
- Amazon Live / Twitch で代替可能であれば IVS は Deprecate、代替不可のユースケースがあれば Webflow migration を検討
- Slackメッセージは Chris/Mariko/Aayushi の Group DM（C0AJSBTJFR9）に送信

## 関連トピック
- `2026-03-08_halfpipe-deprecation` — Halfpipe 全体の APAC POC 対応（本トピックの親トピック）
