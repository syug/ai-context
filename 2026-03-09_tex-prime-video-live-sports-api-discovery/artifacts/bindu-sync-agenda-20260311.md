# Bindu Sync -- アジェンダ

**日時:** 2026-03-11 19:00-19:30 AEDT (8:00-8:30 GMT)
**参加者:** Shugo, Bindu
**目的:** PV Live Sports API Discovery -- ライセンス問題を踏まえた方針すり合わせ

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

---

## 議題1: Jonathan Yi コールの段取り (10min)

### 論点

- **誰がコールを設定するか?** Bindu? Shugo? Mirkoも入れるか?
- **TZ:** Jonathan Yi は Arlington, VA (EST/EDT) -- Bindu (London) との重なりは十分あり。Shugoは非同期フォローでOKか?
- **いつまでに実施?** 今週中が望ましい（Mirkoが ETA を求めている）

### Jonathan Yi コールで確認すべき質問リスト

Mirkoの3要求に対応させて整理:

**1. プロセス（ライセンス申請フロー）**
- 商用利用ライセンスの申請フローはどうなっているか?
- PV BD が完全に仲介するのか、我々がプロバイダーと直接やり取りする場面はあるか?
- 申請に必要なインプット（use case定義、リーチ見積もり等）は何か?

**2. POCs（担当窓口）**
- データプロバイダーごとに担当BDが異なるか? Jonathan Yiが一元窓口か?
- SDP Core (Anand) との役割分担は?（技術オンボーディング vs ライセンス）

**3. ETA（タイムライン）**
- 商用ライセンス交渉の典型的なタイムラインは?（週単位? 月単位?）
- 全プロバイダー横断か、スポーツ/プロバイダー単位で個別に進むのか?

**追加確認事項:**
- PoC/デモは editorial use の範囲で進められるか?（Chicken-and-Egg 回避の鍵）
- データ x プロバイダーのマッピングは既に存在するか?（Holly の onboarded-stats 以上の情報）
- コスト負担者は誰になるか?（BIL / 広告主 / PV?）

---

## 議題2: BIL-E Intake Request (8min)

### 現在の状態

- BIL-E (Harish) は「1案件では動かない。複数Pod横断の例が必要」（Bindu 1月指摘）
- Mirkoがグローバルビジネスインパクトを収集中 → ビジネスケースの材料は揃いつつある

### ビジネスケースの強さ

| Pod | 金額 | 状態 |
|-----|------|------|
| EU Endemics | $3MM/yr | Mirko記載済み |
| AU | $400k/yr | Chris Wilson回答済み |
| US | 金額なし、PoC実行中 | Fitz/Kevin回答済み |
| JP | 未回答 | Mariko: ポジティブだが壁が高い |
| MENA | 数字なし | ポテンシャル言及のみ |

### 議論ポイント

- **Intake を出すタイミングは?** JP/MENAの回答を待つか、EU+AU+USで十分か?
- **Intake の中身:** ライセンス問題が未解決の状態で技術Intakeを出してよいか? それとも並行して進めるか?
- **Bindu側で既にIntakeに向けて動いていることはあるか?**

### 正しいフロー（確認）

Business justification 収集 → **Bindu sync（今ここ）** → BIL-E Intake Request → BIL-E が SDP オンボーディング + BGW インテグレーション実行

---

## 議題3: 技術 PoC 方針 (5min)

### Chicken-and-Egg 回避戦略

- 動くものがないとプロバイダーとのライセンス交渉も進まない
- PoC/デモを editorial/internal use の範囲で先行させる
- Jonathan Yi コールで「PoCは editorial 扱いか」を確認するのが最優先

### PoC のスコープ案

- SDP API への技術的接続テスト（BIL-E Intake 前に可能か?）
- Brand Gateway 経由でのデータ取得デモ
- 1スポーツ（例: NBA）に絞った小規模プロトタイプ

### 議論ポイント

- BIL-E Intake なしで SDP Core と直接テスト接続は可能か?（#sdp-contact / SIM intake queue）
- PoC の成果物をライセンス交渉のレバレッジにできるか?

---

## Next Steps / アクションアイテム

| # | アクション | 担当 | 期限 |
|---|-----------|------|------|
| 1 | Jonathan Yi コールを設定 | ___ | ___ |
| 2 | Jonathan Yi コールのアジェンダ作成・共有 | ___ | ___ |
| 3 | BIL-E Intake Request ドラフト | ___ | ___ |
| 4 | Mirkoへライセンス状況アップデート | ___ | ___ |
| 5 | SDP Core 技術問い合わせ（#sdp-contact） | ___ | ___ |
| 6 | ___ | ___ | ___ |

---

*Strategy v2 参照: pv-live-sports-api-strategy-v2.md*
