# Handover Document
**Topic:** Halfpipe Live Video IVS コンポーネント廃止判断
**Date:** 2026-03-07
**Status:** 進行中

---

## 背景
BIL-Eが2026年11月までに全Halfpipeコンポーネントを廃止予定。BIL TEX EUがオーナーの「Live Video-IVS-2024-edition」コンポーネントについて、廃止 or Webflow移行を3/30までに決定する必要がある。Mirko Cappaiが Asana上でShugo/Billyにメンションし、Amazon Live以外のライブストリーミングニーズの有無を質問したのが発端。

## 現在の状況

### コンポーネント使用状況
- 使用ページ: 0件 / 訪問数: 0
- Component Owner: BIL TEX EU
- Asanaタスク: https://app.asana.com/1/8442528107068/project/1213527661372673/task/1213539247162724
- Halfpipeコンソール: https://console.harmony.a2z.com/ferryserviceconfigurator/?component=Live%20Video-IVS-2024-edition

### Asana上のやり取り（3件）
1. **Mirko Cappai** (3/5): Amazon Live以外でのライブストリーミングの可能性とWebflowコンポーネントの必要性を質問
2. **Billy Kwok** (3/5): Amazon Live未提供ロケール（MENA等）ではまだ必要。FireTVのIVS Webflowは別議論
3. **Shugo Saito** (3/6): AU/MENAは過去事例なく需要低（Twitch等代替あり）、JPはAmazon Live移行済み or Twitch利用なのでnice-to-have。Leigh/Kaiyiにメンションして意見求めた

### Slack ドラフト
- #team-au-and-mena-bil にドラフト作成済み（Chris/Mariko/Aayushiメンション付き英語版）
- Group DMへの送信を検討したが、Slack APIの制約でcreate_draftではGroup DM新規作成不可
- ユーザーがSlackアプリ上でGroup DMにコピペするか、チャンネルドラフトをそのまま送信するか未決定

## 成果物一覧
なし（Asanaコメント投稿 + Slackドラフト作成のみ）

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | 3/18 | Asanaチケットの Acknowledge（確認応答）— コメント済みで実質完了 | 完了 |
| 2 | - | Slack でChris/Mariko/Aayushiに確認メッセージ送信（ドラフト作成済み、送信待ち） | 未完了 |
| 3 | - | Leigh/Kaiyi からのAsana返信を待つ | 未完了 |
| 4 | 3/30 | Migration Decision を確定（Deprecate or Webflow移行） | 未完了 |

## 重要な判断ログ
- 使用ページ0件のため、Deprecateが自然な選択肢だが、Amazon Live未提供ロケール（AU/MENA）での将来ニーズを念のため確認する方針
- JPは過去事例がBeauty（Amazon Live移行済み）とFuji Rock（Twitch）のため、このコンポーネントは不要と判断
- Slackメッセージはチームチャンネルではなく、3人のGroup DMに送る方が適切と判断（対象者が明確で、他メンバーにはノイズ）
