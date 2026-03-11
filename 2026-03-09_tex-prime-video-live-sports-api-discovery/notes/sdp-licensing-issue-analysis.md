# SDP Licensing Issue Analysis
**Date:** 2026-03-09
**Status:** 要対応

## 経緯

1. Bindu が SDP Core SDM (Anand Kumaravel, anandkvl) に口頭確認 → 「データは特定スポンサーに紐づいていないので全広告主利用OK」(3/5)
2. Mirko が書面エビデンスを要求 (3/5)
3. Bindu が Anand にメール送信 — ライセンスと社内レビューについて質問 (3/6)
4. Anand が Jonathan Yi (Sr. BD Manager, WW BD | Prime Video, yijonatj@amazon.com, Arlington VA) をループイン (3/7)
5. **Jonathan Yi の回答 (3/7):** データライセンスは現在 PV専用・editorial use に標準化されており、commercial use には対応していない。商用利用はプロバイダーが個別にスコープとリーチを把握して課金額を算出するモデル。コールを提案。

## 2レイヤー問題

| レイヤー | 担当 | 状況 |
|---------|------|------|
| 技術アクセス（SDP Core） | Anand Kumaravel | ✅ 全広告主で利用可能 |
| 商用ライセンス（PV BD） | Jonathan Yi | ❌ editorial only、商用は個別交渉 |

## Chicken-and-Egg 問題と方針

**問題:** 商用ライセンス交渉にはユースケースとリーチの具体化が必要 → 具体化には技術アクセスとデータ利用が必要 → ライセンスが必要...

**方針（saitshug）:** 技術実装（PoC）を先行し、商用ライセンスはキャンペーン単位で対応
- PoCやデモ段階は editorial/internal use の範囲で進められる可能性が高い
- 実際に広告主にデータを使う段階（= commercial use）で初めてライセンス交渉
- データプロバイダー側も「スコープとリーチ」を見たい → 動くものがないと話が進まない

## 未解決の課題

1. **Editorial vs Commercial の境界** — PoCやデモは editorial 扱いでOKか？ → Jonathan Yiに確認必要
2. **ライセンスコスト** — プロバイダーが個別課金する場合、誰が負担？（BIL / 広告主） → Mirkoにエスカレーション
3. ~~**メールCCの問題**~~ — 解決済み。saitshug はスレッドに入っている（3/11確認）
4. **JP見積もりの壁** — Marikoの「Sales Struggle + ライセンシー問題」は今回のJonathan Yi回答と同根の可能性

## 関係者

| 名前 | alias | 役割 | ロケーション | TZ |
|------|-------|------|------------|-----|
| Jonathan Yi | yijonatj | Sr. BD Manager, WW BD PV | Arlington, VA | EDT (UTC-4) |
| Anand Kumaravel | anandkvl | SDM, SDP Core | Chicago | CDT (UTC-5) |
| Bindu S | sbindu | DT, BIL (Discovery co-owner) | London | GMT (UTC+0) |
| Shugo Saito | saitshug | Sr DT (Discovery co-owner) | Sydney | AEDT (UTC+11) |
| Mirko Cappai | mirkocap | Manager (Accountable) | Amsterdam | CET (UTC+1) |
| Kayla Cheney | kacheney | (CC on confirmation) | US West | PDT (UTC-7) |

## タイムゾーン制約

- Sydney↔London: 11時間差。重なり: AEDT 19:00-21:00 = GMT 08:00-10:00
- Sydney↔Arlington: 15時間差。重なり: 深夜のみ（非現実的）
- London↔Arlington: 4時間差。重なり: GMT 13:00-17:00 = EDT 09:00-13:00（余裕あり）
- **3者コールは不可能。** Bindu + Jonathan Yi コール → saitshug は非同期（メールCC）で対応が現実的
