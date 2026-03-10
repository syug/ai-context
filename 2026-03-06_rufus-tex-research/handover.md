# Handover Document
**Topic:** Rufus x BIL TEX リサーチ — ロケール状況・AU/JP展開・Discovery/Prototype調査
**Date:** 2026-03-06
**Status:** 完了

---

## 背景

ユーザーからの依頼で、Amazon AI Shopping Assistant「Rufus」について、BIL TEXの観点から包括的なリサーチを実施。調査対象は (1) 各ロケールでのRufusサポート状況、(2) AU/JP展開ロードマップ、(3) BIL TEXにおけるDiscovery/Prototypeの有無。社内Wiki、Quip、Slack、PARC/ARC、TEX固有ドキュメント（WBR, QBR, OP1, Goals）を横断的に調査した。

## 現在の状況

### Rufus ロケール展開
- **10マーケット稼働中:** US, UK, DE, FR, IT, ES, IN, JP, CA, PT
- Desktop i18nは2025年中頃にEU-5, IN, JP, CAへ展開済み
- 2026年の優先事項はエンゲージメント拡大(3B目標)・マルチクリックアクション・Alexa+統合・既存マーケットfeature parity
- **新マーケット展開は優先されていない**

### AU/JP ステータス
- **JP:** 稼働中（mShop 2024 Q4〜, Desktop 2025中頃〜）。OPTIMA Rufus Andon稼働、ja-JP向けSOP存在
- **AU:** 未ローンチ。Weblab・ロードマップいずれにも記載なし。2026年中のローンチ見込みなし

### BIL TEX Discovery / Prototype
- **Discovery #1:** [Rufus API on Store Landing Pages](https://quip-amazon.com/BeNqA5zo9z9j) — Brand StoreページにRufusチャットウィジェット埋込。Phase 2（公式API onboarding中）
- **Discovery #2:** [Rufus LLM on Bedrock - TEX](https://quip-amazon.com/UH78Av7IMyw9) — Rufus LLMをBedrock経由でTEX独自ユースケースに活用。DEV/PRODアカウント取得済み
- **PARC Prototype:** [Rufus on Stores](https://console.harmony.a2z.com/parc/#/prototypes/rufus-on-stores) — In Progress、"not safe to pitch yet"
- **ARC Campaign:** 0件
- 全てBilly Kwok (billyhkk) 主導のボトムアップ活動。OP1/正式ゴールには未組込

### Kaiyi Wong / APAC調査
- TEX APAC DT Weekly Huddle（2026版・2024-25アーカイブ版）、Quip検索、Slack検索で **KaiyiとRufusの関連は発見できず**
- Kaiyiの活動はキャンペーンストア開発・IMDB unlock・UGS・クリエイティブツールリサーチに集中
- PhoneToolでエイリアス特定できず（退職または別エイリアスの可能性）
- APAC DTチームからのRufus活動は確認できず — EU EndemicsのBilly Kwokが唯一の推進者

## 成果物一覧

```
2026-03-06_rufus-tex-research/
  notes/
    rufus-research.md    — 包括的リサーチレポート（ロケール、Discovery詳細、ソース一覧）
  handover.md            — 本ファイル
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|----------|
| — | — | （なし — 調査完了） | — |

## 重要な判断ログ

- **調査手法:** 4エージェント並列（Wiki/Internal Search、Slack、PARC/ARC、Quip/TEXドキュメント）で網羅性を確保
- **AU Rufus展開の結論:** 公式ロードマップ・Weblab・Andonいずれにも記載なし。Heartboardダッシュボードの存在のみが将来の兆し。明確な「計画なし」ではなく「計画が見当たらない」状態
- **BIL TEX Rufus活動の構造:** Billy Kwok個人のボトムアップ活動であり、組織的な戦略/ゴールとしては未承認。OP1・QBRに言及なし。WBRのみEU Endemicsタスクリストに記載
- **2つのDiscoveryの棲み分け:** #1（API on Stores）はRufusサービスをプロダクトとして統合、#2（LLM on Bedrock）はモデルをBIL独自パイプラインで活用。補完的だが独立したアプローチ

## 関連トピック

- [tex-wbr-review-and-deep-dive](../2026-03-02_tex-wbr-review-and-deep-dive/) — WBRレビューでRufus関連タスクがEU Endemicsに記載
- [bil-op1-planning-fy27](../2026-03-06_bil-op1-planning-fy27/) — OP1にRufus未組込の背景
- [tex-survey-analysis](../2026-02-25_tex-survey-analysis/) — FY26 Discovery Planningサーベイ（Rufusは候補に挙がらず）
- [prototype-ideation-research](../2026-03-05_prototype-ideation-research/) — FY26プロトタイプ候補リサーチ
