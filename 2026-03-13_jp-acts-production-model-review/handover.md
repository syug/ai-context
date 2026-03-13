# Handover Document
**Topic:** JP ACTS Production Model — Mirko からの質問対応（DCS コントラクター権限・ガバナンス）
**Date:** 2026-03-13
**Status:** 進行中（Mirko 質問受領、回答準備中）

---

## 背景

Mirko/Alex/Nathan のグループ DM (C0ALKLXV109) で、JP の DCS コントラクターが BIL キャンペーンのページ制作に関わっていることについて質問が発生。発端は Mirko が DCS チーム（Takuji 配下の WDE コントラクター）にコードリポジトリの権限を付与する件で Shugo に確認を求めたこと。

Shugo が ACTS Production Model（BIL x CCM x DCS の cross-org production model）の Wiki を共有して説明したところ、Mirko から詳細な質問が返ってきた。

### ACTS Production Model とは

- Wiki: https://w.amazon.com/bin/view/JP_AMG_2/Managed_Custom_Solution/BIL_CCM_DCP_Production/
- オーナー: Mariko Ito (marikoit)
- 内容: JP での BIL, CCM, DCS 間の cross-org production model
- 提供メニュー: FireTV Takeover Experience（40MM JPY〜）+ Halfpipe Product Selector（20MM JPY〜、NE 限定）
- DCS コントラクター（Takuji 配下 kamekou 等）が BIL キャンペーンの CLP を制作

## 現在の状況

### Mirko の質問（3/13）

> Was this something that was discussed and agreed at the APAC leadership level? How long has this team been in place and—if you have the data—how much business (revenue or campaign volume) is currently associated with the work they produce? I see risks in having page builders operating outside of our org while delivering pages on our behalf, such as technical alignment (e.g. deprecation of halfpipes), quality and standards, a11y compliancy, security/platform governance, ownership and maintenance etc. I'd like to know more

Mirko の懸念:
1. APAC リーダーシップレベルで合意済みか？
2. チームの稼働期間とビジネス規模（revenue / campaign volume）は？
3. リスク: BIL org 外のビルダーが BIL ページを制作 — 技術整合性（Halfpipe 廃止含む）、品質・標準、a11y コンプライアンス、セキュリティ/プラットフォームガバナンス、オーナーシップ・メンテナンス

### 補足情報

- Halfpipe Product Selector については Mariko が「需要ほぼないのでサービス Close のアナウンスを入れる」と回答済み（3/13 DM）
- Product Selector Self-Service Widget（AWLS）は 2024/12 に GA 済み

## 成果物一覧

なし

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | — | Mirko の質問に回答（Kazuki/Mariko と連携が必要かも） | 未着手 |
| 2 | — | ACTS Production Model の稼働期間・ビジネス規模を調査 | 未着手 |
| 3 | — | Mirko の懸念（ガバナンス・a11y 等）に対する説明準備 | 未着手 |

## 重要な判断ログ

- Mirko はセンシティブなトーンで聞いており、BIL org 外のビルダーによるページ制作に対するガバナンス懸念が中心
- Kazuki（APAC Head）が合意しているはず（ACTS Production Model は JP リーダーシップ発）だが、TEX/Mirko 側には共有されていなかった可能性
- Halfpipe deprecation がきっかけで発覚した副次的なトピック

## 関連トピック

- `2026-03-08_halfpipe-deprecation` — Halfpipe 廃止対応（発端）
