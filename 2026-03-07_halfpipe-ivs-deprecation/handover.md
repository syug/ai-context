# Handover Document
**Topic:** Halfpipe Live Video IVS コンポーネント廃止判断
**Date:** 2026-03-13
**Status:** 進行中（JP: Deprecateほぼ確定（Mariko了承、他メンバーヒアリング中）、MENA: IVS必須、AU: Chris回答待ち）

---

## 背景
BIL-Eが2026年11月までに全Halfpipeコンポーネントを廃止予定。BIL TEX EUがオーナーの「Live Video-IVS-2024-edition」コンポーネントについて、廃止 or Webflow移行を3/30までに決定する必要がある。Mirko Cappaiが Asana上でShugo/Billyにメンションし、Amazon Live以外のライブストリーミングニーズの有無を質問したのが発端。

## 現在の状況

### コンポーネント使用状況
- 使用ページ: 0件 / 訪問数: 0（データ上。MENAは実際にIVS使用中だがFerryService経由でないため検出されていない可能性）
- Component Owner: BIL TEX EU
- Asanaタスク: https://app.asana.com/1/8442528107068/project/1213527661372673/task/1213539247162724

### Asana上のやり取り
1. **Mirko Cappai** (3/5): Amazon Live以外でのライブストリーミングの可能性とWebflowコンポーネントの必要性を質問
2. **Billy Kwok** (3/5): Amazon Live未提供ロケール（MENA等）ではまだ必要。FireTVのIVS Webflowは別議論
3. **Shugo Saito** (3/6): AU/MENAは過去事例なく需要低、JPはAmazon Live/Twitch代替あり
4. **Shugo Saito** (3/12): APAC/MENA SM Leads からのアップデート — MENA: IVS 実使用中・Amazon Live非対応、JP: 需要あるが代替あり、AU: 需要低

### Slack（Chris/Mariko/Aayushi グループDM — C0AJSBTJFR9）
1. **Shugo** (3/10): IVS 廃止について3つの選択肢（Amazon Live / Twitch / IVS）を提示し、需要確認
2. **Mariko Ito** (3/11): JP Livestreaming に2026年需要あり。PVS + フルファネルキャンペーンコンセプトに組み込み済み
3. **Shugo** (3/12): JP フォローアップ — Amazon Live / Twitch で代替可能か確認。Beauty Festival = Amazon Live、Fuji Rock = Twitch の実績を提示
4. **Chris Wilson** (3/12, 口頭): MENA で IVS を実際に使用中と報告
5. **Shugo** (3/12, ドラフト): Amazon Live は US/JP/IN のみ対応（AU/MENA非対応）を共有 + AU の需要を Chris に確認

### Amazon Live 対応マーケット
- **対応:** US, JP, IN のみ
- **非対応:** AU, MENA, EU, その他
- ソース: https://advertising.amazon.com/solutions/products/amazon-live

### リージョン別状況

| リージョン | IVS需要 | Amazon Live | Twitch | 判断 |
|---|---|---|---|---|
| MENA | **実使用中** | 非対応 | 要確認 | **Webflow migration が必要** |
| JP | 需要あり（PVS連携） | 対応 | 対応 | 代替可能なら Deprecate、確認中 |
| AU | 低（過去実績なし） | 非対応 | 対応 | Chris 回答待ち |

## 成果物一覧
なし（Asanaコメント + Slackメッセージのみ）

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | 3/18 | Asanaチケットの Acknowledge | **完了** |
| 2 | 3/10 | Slack でChris/Mariko/Aayushiに確認メッセージ送信 | **完了** |
| 3 | 3/12 | Asana に MENA/JP/AU 状況コメント | **完了** |
| 4 | 3/12 | Amazon Live 対応マーケット確認 | **完了**（US/JP/IN のみ） |
| 5 | — | Mariko — JP IVS Deprecate でおそらく問題なし、他メンバーにヒアリング中 | アップデート待ち |
| 6 | — | Chris — AU の IVS 需要確認（グループDM ドラフト済み） | 送信待ち |
| 7 | — | Leigh/Kaiyi からのAsana返信を待つ | 未回答 |
| 8 | 3/30 | Migration Decision を確定 | 未着手 |

## 重要な判断ログ
- 使用ページ0件（データ上）だが、MENA で実際に IVS を使用中（Chris 情報 3/12）
- **Amazon Live は AU/MENA 非対応** — MENA にとって IVS が唯一の Amazon ネイティブ Live Streaming ソリューション
- **MENA の状況から Webflow migration が必要になる可能性が高い** — Billy の最初のコメント（3/5）とも整合
- JP は Amazon Live / Twitch の2つの代替手段が利用可能。Mariko が需要ありと回答したが、IVS 固有のニーズかは確認中
- **Mariko 最終回答（3/13 DM）:** 「IVS Deprecation で問題ないと思う、他メンバーにヒアリング後アップデートする」→ JP は Deprecate 方向確定的
- AU は需要低い見込み（過去実績なし）だが Chris に最終確認中

## 関連トピック
- `2026-03-08_halfpipe-deprecation` — Halfpipe 全体の APAC POC 対応（本トピックの親トピック）
