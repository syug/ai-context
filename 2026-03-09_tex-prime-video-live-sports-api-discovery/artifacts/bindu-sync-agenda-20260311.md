# Bindu Sync -- アジェンダ

**日時:** 2026-03-11 19:00-19:30 AEDT (8:00-8:30 GMT)
**参加者:** Shugo, Bindu
**目的:** PV Live Sports API Discovery -- 2トラック並行戦略の方針すり合わせ

---

## 前提共有 (2min)

前回（1月）からの主な進展:

1. **Mirkoがグローバルでビジネスインパクト収集を開始**（3/3〜）
   - EU $3MM/yr, AU $400k, US PoCあり, JP/MENA未確定
2. **ライセンス問題が顕在化**（3/6-3/7）
   - BinduがSDP Core (Anand) に問い合わせ → PV BD (Jonathan Yi) がループイン
   - Jonathan Yiの回答: SDPデータは現在 **editorial use のみ**。商用利用は未対応で、データプロバイダーが use case / reach / data scope の3軸で個別に課金を算出
   - 技術アクセス（SDP Core管轄）と商用ライセンス（PV BD管轄）は**別レイヤー**
3. **Mirkoの要求3点**（3/10メッセージ）
   - ライセンス申請の**プロセス**を明確にする
   - **POCs**（担当窓口）を特定する
   - **ETA**（タイムライン）を把握する

**提案: 2トラック並行で進める**

```
Track 1 (技術): Biz justification → BIL-E Intake → SDP Onboarding + BGW統合
Track 2 (ライセンス): Jonathan Yi コール → プロセス/POCs/ETA把握 → 商用ライセンス交渉
```

技術アクセスはライセンス解決を待たずに進められる（Anand「全広告主OK」）。
両トラックが合流するのは実キャンペーン実行時。PoC は editorial/internal use で Track 1 のみで走れる。

---

## Track 1: 技術アクセス — BIL-E Intake & SDP Onboarding (15min)

### 1-1. Bindu-Harish 協議状況の共有

- 前回（1月）Bindu経由で確認: Harish (BIL-E) は「1案件では動かない。複数Pod横断の例が必要」
- **1月以降、Bindu-Harish間で何か進展あるか?**

### 1-2. オンボーディングの進め方 — (A) vs (B)

| | (A) 我々主導 | (B) BIL-E主導 |
|---|------------|--------------|
| **流れ** | BIL-E Intake を送りつつ、我々が SDP Onboarding も initiate → 後から BIL-E を巻き込む | BIL-E Intake からスタート → BIL-E が SDP Onboarding を進める |
| **メリット** | スピード。BIL-E の優先度に依存しない | 正規ルート。BIL-E のオーナーシップが明確 |
| **リスク** | BIL-E を飛ばして進めることへの反発 | BIL-E のバックログ次第で遅延 |

**Binduに聞きたいこと:** Harish の性格・チームの状況を踏まえて、どちらが現実的か?

### 1-3. Biz Justification の温度感チェック

現在の数字で Harish を説得できそうか?

| Pod | 金額 | 状態 |
|-----|------|------|
| EU Endemics | $3MM/yr | Mirko記載済み |
| AU | $400k/yr | Chris Wilson回答済み |
| US | 金額なし、PoC実行中 | Fitz/Kevin回答済み |
| JP | 未回答 | Mariko: 壁が高い |
| MENA | 数字なし | ポテンシャルのみ |

- **EU + AU + US PoC実績で十分か?** それとも JP/MENA を待つべきか?
- Bindu の温度感: Harish は動きそうか?

### 1-4. 技術 PoC（Chicken-and-Egg 回避）

- PoC/デモを editorial/internal use の範囲で先行させたい
- BIL-E Intake なしで SDP Core と直接テスト接続は可能か?（#sdp-contact / SIM intake queue）
- PoC の成果物をライセンス交渉のレバレッジにできるか?

---

## Track 2: 商用ライセンス — Jonathan Yi との連携 (10min)

**Jonathan Yi プロフィール:**
- Sr. BD Manager, PV Devices-BD Tech & Product
- alias: yijonatj | L6, Arlington VA (EST/EDT)
- 上司: Nina Pablo (ninapabl, Sr. Mgr, L7, Seattle)
- Bindu が Anand 経由でループインした相手

### 2-1. Jonathan との確認事項すり合わせ

Mirkoの3要求に対応して、Jonathan に確認すべき内容を Bindu と揃える:

**1. プロセス（ライセンス申請フロー）**
- 商用利用ライセンスの申請フローはどうなっているか?
- PV BD が完全に仲介するのか、我々がプロバイダーと直接やり取りする場面はあるか?
- 申請に必要なインプット（use case定義、リーチ見積もり等）は何か?

**2. POCs（担当窓口）**
- データプロバイダーごとに担当BDが異なるか? Jonathan が一元窓口か?
- SDP Core (Anand) との役割分担は?（技術オンボーディング vs ライセンス）

**3. ETA（タイムライン）**
- 商用ライセンス交渉の典型的なタイムラインは?（週単位? 月単位?）
- 全プロバイダー横断か、スポーツ/プロバイダー単位で個別に進むのか?

**追加確認事項:**
- PoC/デモは editorial use の範囲で進められるか?（Chicken-and-Egg 回避の鍵）
- データ x プロバイダーのマッピングは既に存在するか?（Holly の onboarded-stats 以上の情報）
- コスト負担者は誰になるか?（BIL / 広告主 / PV?）

### 2-2. Jonathan との連絡方法の決定

| 方法 | メリット | デメリット |
|------|---------|-----------|
| **コール** | 密度が高い、ニュアンスを掴める | TZ調整が必要 |
| **Slack** | 非同期で進められる、ログが残る | レスポンス遅延リスク |
| **Email** | フォーマル、CCで関係者を巻き込みやすい | ラリーに時間がかかる |

- Jonathan の 3/7 メール原文では「コールを提案」していた
- **Bindu の判断を仰ぎたい:** Jonathan との関係性・コミュニケーションスタイルを踏まえてどれがベストか?

### 2-3. コールの場合 — Bindu にリードをお願いできるか?

- **TZ問題:** Shugo (Sydney AEDT) - Jonathan (Arlington EST) = 15時間差 → 直接コールは非現実的
- **Bindu (London GMT) - Jonathan (Arlington EST)** = 5時間差 → ビジネスアワー重なりあり
- **お願い:** Bindu が Jonathan コールをリード、Shugo はメール CC + 非同期フォロー
- Mirko も入れるべきか?（A=Mirko なので、少なくともCC）

---

## Next Steps / アクションアイテム

| # | アクション | 担当 | 期限 |
|---|-----------|------|------|
| 1 | Jonathan Yi コールを設定 | ___ | ___ |
| 2 | Jonathan Yi コールのアジェンダ作成・共有 | ___ | ___ |
| 3 | BIL-E Intake Request ドラフト | ___ | ___ |
| 4 | SDP Core 技術問い合わせ / PoC initiate | ___ | ___ |
| 5 | Mirkoへライセンス状況アップデート | ___ | ___ |
| 6 | ___ | ___ | ___ |

---

*Strategy v2 参照: pv-live-sports-api-strategy-v2.md*
