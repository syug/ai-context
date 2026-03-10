# Strategy Document Review — 2026-03-09
**Status:** Bindu syncで議論用

## レビュー対象

saitshug作成の方針案（3/9）— PV Live Sports API Discovery のアプローチ定義

---

## 1. ステークホルダー — PV BD が欠落

**問題:** Jonathan Yi (Sr. BD Manager, WW BD | Prime Video) のチームが記載されていない。

**根拠:** Jonathan Yiのメール（3/7）で、SDPデータの商用ライセンスはPV BDが管理していることが判明。データプロバイダーとの商用利用交渉はPV BDが仲介する。

**現在の構図:**
```
BIL TEX ---> BIL-E (BGW技術統合) ---> SDP (データ技術基盤) ---> Data Providers
                                          |
                                     PV BD (Jonathan Yi)
                                     = ライセンス管理・プロバイダー交渉窓口
```

**追加推奨:**
```
PV BD (Jonathan Yi) - SDPデータの商用ライセンスを管理。
データプロバイダーとの交渉窓口。
editorial use は標準化済みだが、commercial use は PV BD を通じてプロバイダーと個別交渉が必要。
```

## 2. SDP の定義 — 技術基盤 vs ライセンスの区別

**問題:** 「SDP - Prime video Live sports API を Ownしている」は技術面のみ正確。ライセンスは別管轄。

**SDP Wiki原文:**
> "SDP acquires, stores and vends data from authoritative 3p sports data providers."

**2レイヤー:**

| レイヤー | 管轄 | 担当者 | 状態 |
|---------|------|--------|------|
| 技術アクセス | SDP Core | Anand Kumaravel (SDM) | 全広告主OK |
| 商用ライセンス | PV BD | Jonathan Yi (Sr. BD Mgr) | editorial only、commercial は個別交渉 |

**修正案:** 「SDP - 技術基盤として Live Sports API を Own。ただしデータの商用ライセンスは PV BD 管轄」

## 3. Data Providers — 「スポーツ・リーグごと？」への回答

Quip DocとSDP Wikiによると:
- データプロバイダーは Sportradar 等の 3P プロバイダーで、**1社が複数スポーツをカバー**
- Jonathan Yiの「case-by-case」はユースケース単位の交渉を示唆
- マッピングは **プロバイダー x スポーツ/リーグ x ユースケース** の3軸になる可能性

ただし、このマッピングを誰が持っているかが重要:
- SDP → 技術的なデータプロバイダーのマッピングは持っている（Holly UI で確認可能）
- PV BD → 商用ライセンスの条件・窓口を持っている

## 4. ゴール — スコープが狭い

**現在:**
> Live Sports APIのBGW統合を完了させ、技術的ブロッカーがない状態にする。

**問題:** 技術面のみ。Jonathan Yiのメールで判明した商用ライセンスの壁を踏まえると、ゴールは2層必要。

**修正案:**
1. **技術:** BGW統合を完了し、技術的にいつでも使える状態にする
2. **商用:** BIL Podsが参照できるライセンス・コスト・SOPのマッピングを完成させる

## 5. アプローチ(B) Next Steps — 整合性の問題

### 5a. 「BGW統合はすぐにスタートする」

**矛盾:** BIL-Eの条件がまだクリアされていない。

handoverの判断ログ:
- Bindu指摘: Harish（BIL-E）は1案件だけでは不満。複数Pod横断キャンペーン例が必要
- 正しいフロー: Business justification 収集 -> Bindu sync -> BIL-E Intake Request -> BIL-E 実行

Mirkoのビジネスインパクト収集は進行中だが未完了（JP見積もり未回答）。
「すぐにスタート」は BIL-E Intake Request が受理されてからになるはず。

### 5b. 「各データプロバイダの窓口を教えてもらう」

**問題:** SDPに聞いても技術面の窓口しか出てこない可能性が高い。

商用利用の窓口は PV BD (Jonathan Yi) 経由。
Jonathan Yiのメール原文:
> "Let me know if it makes sense to get on a call to discuss further what the team is thinking."

これがまさに商用ライセンス議論の入口。

**修正案:** Next Stepsの問い合わせ先を分ける:
- SDP Core → 技術的ブロッカー確認、データ/プロバイダーのマッピング取得
- PV BD (Jonathan Yi) → 商用利用の条件、プロバイダーとの交渉フロー確認

## 6. Discovery Doc との整合性

Quip Doc の Next Steps:
1. Initiate request for onboarding with SDP core team
2. Initiate request with BIL-E team to onboard the API via Brand gateway service

方針案のアプローチ(B)はこれを包含しつつ、商用ライセンスのマッピングまで拡張している。
方向性は整合しているが、Discovery Doc にはライセンス問題が未反映（Jonathan Yi回答は 3/7）。
Bindu sync 後に Discovery Doc も更新が必要。

## 7. Slack チャネルとの整合性

#tex-discovery-pv-live-sports-api-enablement の流れ:
1. Bindu: SDP マネージャーに確認 -> 全広告主OK（口頭）
2. Mirko: 書面確認を要求
3. Bindu: Anand にメール送信
4. Anand -> Jonathan Yi -> editorial only 回答

方針案はこの流れを正しく反映。
ただし Jonathan Yi の回答はまだチャネルで共有されていない（メールスレッドのみ）。

---

## 総合判定

| 項目 | 判定 | 対応 |
|------|------|------|
| ステークホルダー | **要修正** | PV BD (Jonathan Yi) を追加 |
| SDP定義 | **要補足** | 技術基盤 vs ライセンスの区別を明記 |
| ゴール | **要拡張** | 商用準備も含める |
| アプローチ(A) vs (B) | OK | 論理的に整理されている |
| アプローチ(B) 内容 | **要修正** | プロバイダー直接 -> PV BD 経由に |
| BGW「すぐスタート」 | **要修正** | BIL-E 条件クリア後に |
| プロバイダー窓口 | **要修正** | SDP=技術、PV BD=商用 で分ける |
| Discovery Doc | OK | sync後に更新必要 |
| Slack | OK | 正確 |

## 推奨: Bindu sync で確認すべきこと

1. PV BD との関係 — Bindu は Jonathan Yi とどの程度やり取りしているか？
2. プロバイダーへのアクセス — PV BD 経由のみか、SDP 経由でも可能か？
3. BIL-E Intake の現状 — Bindu 側で既に動いていることはあるか？
4. Discovery Doc の更新方針 — ライセンス問題をどう反映するか
