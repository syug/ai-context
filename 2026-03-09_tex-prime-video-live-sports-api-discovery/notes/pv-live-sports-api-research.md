# Prime Video Live Sports API — Discovery Research Note

**Date:** 2026-03-04
**Author:** Shugo Saito
**Status:** Discovery in progress

---

## 1. Overview

Prime Video Live Sports API は、Prime Video の Sports Data Platform (SDP) が提供するスポーツデータを広告プロダクトに活用する構想。BIL-TEX として Brand Gateway 経由のオンボーディングプロセスを own & oversee する。

## 2. Mirko's Request (2 channels)

### 2.1 Slack DM (3/3, mirkocap → saitshug + sbindu group DM)

- PV Live Sports API の Brand Gateway オンボーディングプロセス全体を **own & oversee** してほしい
- Legal チェック + PV/BIL-E alignment を担当
- Bindu をサポート
- **"big discovery"** として、四半期に必要な 2つの discovery 分にカウント

### 2.2 Email (3/4, global stakeholders, subject: "[Action Needed] Prime Video Live Sports API")

- BIL-E に技術実装依頼の前に、全リージョンから **ビジネスインパクト見積もりを EOW (3/6) までに** 収集
- **APAC/MENA 担当:** Saito, Shugo & Wilson, Chris

#### Existing replies:

| Respondent | Region | Key Points |
|-----------|--------|------------|
| **Chris Wilson** | AU | NBA中心で **400k USD** 見込み。MENA はポテンシャルありだが数字は出さない |
| **Victor Lu** | — | sidecasting / Game Time Live! に重要。Kyle, Christopher, Patrick をループイン |
| **Patrick Moses** | — | sidecast 内ブランド広告トリガーに活用可能（例: 3ポインター → State Farm スポンサー表示） |

## 3. History / Timeline

| Date | Event |
|------|-------|
| **2025/12** | Gillette 案件で Live Sports API 調査開始 |
| — | Gillette 失注 → 調査中断 |
| — | Mirko: 「案件に関係なく Discovery を続けたい」 |
| — | Bindu: 「BIL-E (Harish) は1案件だけでは動かない。複数Pod横断の例が必要」 |
| **2026/01** | Bindu とフォローアップコール |
| **2026/03/03** | Mirko が Slack DM でオーナーシップ依頼 |
| **2026/03/04** | Mirko がグローバルメールでビジネスインパクト収集開始 (EOW 3/6) |

**BIL-E 動機付けの構造:** Harish (BIL-E) は単一案件では技術リソースを割けない。Mirko のグローバルインパクト収集は、複数Pod横断のビジネスケースを構築してBIL-E の engagement を正当化するためのもの。

## 4. Quip Discovery Doc

**URL:** https://quip-amazon.com/c4cBAcoeV61e/Discovery-Prime-video-Live-sports-API
**Author:** Bindu

### 4.1 SDP (Sports Data Platform)

Prime Video のスポーツデータインフラストラクチャ。Sportradar 等の外部データプロバイダーからデータを取得・配信。

**Scale:** 36 sports / 432 leagues

### 4.2 Data Categories

| Category | Content | Delivery |
|----------|---------|----------|
| **Static Data** | League schedules, team info, logos, player stats, standings | API (GetEntity / BatchGetEntity) |
| **Real-Time Data** | Live scores, game status, play-by-play commentary | Push (FIFO SQS queue), spoiler prevention buffer |
| **Semi-Static Data** | Match lifecycle (scheduled → live → ended etc.) | API |

### 4.3 Use Cases (from Quip)

1. **Betting-style gamification** — リアルタイム予測チャレンジ。試合中にファンがスコアやプレイを予測し、ブランドがスポンサーするポイントやリワードを獲得
2. **Team-linked product bundles** — チームパフォーマンス連動の動的マーチャンダイジング。好調チームのグッズを優先表示
3. **Real-time match info landing pages** — 試合状況に応じたコンテキスチュアルLP。ハーフタイム→スナック広告、試合後→勝利チームグッズ

### 4.4 Next Steps (from Quip, not started)

1. SDP core team へのオンボーディングリクエスト
2. BIL-E team への Brand Gateway 経由オンボーディングリクエスト

### 4.5 Key Links

| Resource | URL |
|----------|-----|
| SDP Wiki | https://w.amazon.com/bin/view/Amazon_Video/live_services/SportsDataPlatform/ |
| Holly UI (データ探索) | https://holly.prime-video.amazon.dev/explore/get-entity |
| Onboarded Stats | https://holly.prime-video.amazon.dev/onboarded-stats |
| API Doc | https://console.harmony.a2z.com/sdpdistributionservice/get-entity-api/API-documentation |
| SDP Core team | https://w.amazon.com/bin/view/Amazon_Video/live_services/SDPCore |

## 5. JP Analysis

### 5.1 SDP Onboarded Leagues (JP-relevant)

| Sport | SDP Onboarded | PV JP Rights | Notes |
|-------|--------------|-------------|-------|
| **Soccer** | J1, J2, J3, 100 Year Vision, WE League | ✅ Exclusive (2023-2032, 10yr, ~200B yen) | ~1,100+ matches/year |
| **Basketball** | B.LEAGUE | ✅ | Growing popularity |
| **Volleyball** | SV.LEAGUE | ✅ | Rebranded from V.LEAGUE 2024-25 |
| **Motorsport** | Super Formula, Super GT | TBC | Both onboarded in SDP |
| **Golf** | LPGA Tour of Japan | TBC | Women's golf popular in JP |
| **Boxing** | Teiken Promotions | ✅ | Major JP boxing promoter |
| **MMA** | UFC, ONE Championship | Partial | International but popular |
| **Baseball** | NPB | ❌ Not in SDP, no PV rights | JP's biggest sport but not available |

### 5.2 Key Insight

**J.League exclusive deal is the anchor.** 2023-2032 の10年独占契約（推定2,000億円規模）により、J1/J2/J3/WEリーグ合わせて年間1,100試合以上のライブスポーツイベントを配信。他リーグと合わせると年間2,000+イベントの可能性。

### 5.3 AU Comparison

Chris Wilson は NBA のみで 400k USD と見積もり。JP は:
- ライブスポーツの規模が桁違いに大きい（NBA = 1リーグ vs JP = 複数リーグ × 1,100+ 試合/年）
- 独占契約のため競合プラットフォームでは実現不可能な差別化要因
- サッカー以外にも B.LEAGUE, SV.LEAGUE, ボクシング等の複数スポーツ

## 6. Actions Taken (3/4)

| # | Action | Status |
|---|--------|--------|
| 1 | Mirko メールスレッドに返信、Mariko Ito (marikoit) を JP 見積もり担当としてループイン | ✅ Done |
| 2 | Mariko に Slack DM でコンテキスト提供（日本語フォローアップ） | ✅ Done |
| 3 | Mariko の JP 見積もり回答待ち | ⏳ Waiting (EOW 3/6) |
| 4 | Mirko DM への返答（オーナーシップ引き受けの可否） | 📋 Pending |

## 7. Open Questions

- JP のビジネスインパクト見積もりはどの程度の粒度が求められるか？（AU の Chris は NBA 単体で 400k USD と具体的な数字を出している）
- SDP オンボーディングプロセスの所要期間・リソース要件は？
- BIL-E Brand Gateway の技術的制約やタイムラインは？
- Legal チェックの範囲（リージョン固有のスポーツデータ規制等）

---

*Last updated: 2026-03-04*
