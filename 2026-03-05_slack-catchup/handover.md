# Handover Document
**Topic:** Slack未読チェック・チーム情報キャッチアップ（継続）
**Date:** 2026-03-11
**Status:** 進行中

---

## 背景

Slack未読メッセージの継続的な整理。3/5セッションで au-bil と team-au-and-mena-bil を消化。3/7セッションで追加チャンネル（bil-ww-tex, bil-ww-tex-dt）と複数のDM対応を実施。3/11セッションで4チャンネル+DM2件を再確認。

## 現在の状況

### 確認済みチャンネル

#### #au-bil（C046RU6T2H0）— 3/11確認済み
- **Alexa+ 移行問題（Matt Bryant, 3/9）:** Alexa+ローンチに伴い新規Alexaスキル開発が非推奨化。Census（8/11）向けAlexaスキルの政府提案が困難に。Matt がSonnar（NZ vendor）にコスト確認中、Country Managerにもエスカレーション中
- **"Ignored to Adored" デッキ（Rich Price → Luke, 3/10）:** Dine 2.0 V3.pptx 共有。Chris Wilson が事前送付を却下（「always present」）
- **Howatson AI "Unicorn"（Matt Bryant, 3/10）:** AIクリエイティブプラットフォーム。キャンペーンクリエイティブのリサイズ自動化、$5kから
- （3/5確認分）Matt → Shugo: Pizza Studio Tamaki シドニーCBDオープン / Hyundai / Specsavers / Awards / Telstra 等

#### #team-au-and-mena-bil（C089K992M5E）— 3/11確認済み
- Chris Wilson PV講演ドラフト（"Meh to Memorable"）に Aayushi Dadhich がスレッド返信（3/9）
- （3/7確認分）Chris Weekly Update: Spider Noir x Hyundai ピッチ勝利（予算削減で不実施）、MENAのAbu Dhabi/Galaxy/Arla対応、2027計画開始

#### #bil-ww-tex（C03JTNMC9MF）— 3/11確認済み
- **Fitz Maro:** L5 DT募集（NYC 1名 + London 1名）。リファラル・LinkedInシェア依頼
- **Kasey Yang:** NA TEX向けWBR（Loop文書）記入リマインダー
- （3/7確認分）Francesco: Daily Unlocks Webflowテンプレート / Fitz: Anthropic デザインリード Jenny Wen ポッドキャスト / Alex Mejias: 組織アップデート / Kasey Yang: プロトタイプ外部公開方法 / Mirko: マイクロインタラクション集 / Fitz: Q1 PARCプロトタイプ目標リマインダー

#### #bil-ww-tex-dt（C09A95SHCPQ）— 3/11確認済み
- 3/7以降の新規メッセージなし
- （3/7確認分）Nathan Crenshaw: 3Dアクセシビリティ議論

### DM対応

#### Matt Bryant DM（D07Q52SMS6A）— 3/11確認・新規なし
- （3/7時点）Spotify Web API 共有 → API Landscape Research に発展（返信済み）

#### Matt Roberts グループDM（C0AJQFX1VLK）— 3/11確認・新規なし
- メンバー: robsmat, mjlb, lukthis, saitshug, larsluke
- Lego SB広告エラーへの返信ドラフト作成済み（未送信）

### OpenClaw on Amazon Lightsail
- bil-ai / tex-dt-signals 向けドラフトは Slack に存在（ユーザーが手動作成済み・未送信）

### 未確認チャンネル
- au-advertising, その他多数のチャンネルが残存

## 成果物一覧

（なし — 情報消化・DM対応のセッション）

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | - | Matt に Pizza Studio Tamaki の返信 | 未完了（優先度低） |
| 2 | - | Matt Roberts グループDM返信の送信確認 | 未完了（緊急性低下・新規メッセージなし） |
| 3 | - | Chris Wilson PV講演ドラフトの閲覧（Aayushiスレッド返信あり） | 未完了 |
| 4 | - | OpenClaw ドラフトの送信（bil-ai / tex-dt-signals） | 未完了 |
| 5 | - | 残りの未読チャンネルの消化 | 未完了 |
| 6 | - | Mirko の PV Live Sports API メッセージへの対応（別トピック: tex-sse） | 進行中（別トピックで対応中） |
| 7 | - | Alexa+ 移行問題のフォローアップ（Matt/Chris の対応状況をウォッチ） | 新規 |

## 重要な判断ログ

- Slack チャンネル名の fuzzy 検索は現 API では直接サポートされていない。チャンネルID特定に迂回フローが必要
- bil-ai（390人, private）はセミフォーマル英語、tex-dt-signals（96人, public）は超カジュアル・URLドロップ主体 — 投稿トーンを使い分ける必要あり
- SharePoint docx は MCP 経由ではアクセス不可（401）。ブラウザSSO経由のみ
- Alexa+ 移行はCensus案件に直接影響。Shugo直接のアクション不要だが、Matt/Chrisの動向をウォッチしておく

## 関連トピック

- `2026-03-06_api-landscape-research` — Matt Bryant の Spotify Web API 共有をきっかけに発展した API 調査
- `2026-02-26_tex-prime-video-sse-initiative` — Mirko の PV Live Sports API メッセージ
- `2026-03-03_daily-task-management` — Daily Log 運用
