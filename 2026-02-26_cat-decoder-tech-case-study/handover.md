# Handover Document
**Topic:** Mars Dine Cat Decoder テックケーススタディ + ASG Scale-to-Zero 運用整備
**Date:** 2026-03-08
**Status:** 進行中

---

## 背景

TEXインターナル向けテックケーススタディ・プレゼン動画制作プロジェクト。対象は **Mars Dine Cat Decoder** — AU市場向けキャットフードキャンペーン（AI動画生成）。

3/5 のセッションで EC2 ASG の Scale-to-Zero を本番実装・検証。3/8 のセッションで ASG 起動コスト確認（~$31-38 USD/日）、Lukeからの連絡待ちでスタンバイ状態。

---

## 現在の状況

### ASG 状態（3/8 時点）

- **現在: Idle モード（Desired: 0）** — GPU インスタンス停止中、コストゼロ
- 3/8 に一時的に Desired: 1 に設定 → コスト確認後即リバート（Desired: 0）
- ASG 名: `MarsDineMindReaderServiceProd-MindReaderStack-VideoRenderClusterVideoRenderAutoScalingGroupASGE979BBA1-JxyzuwdhJrsj`

### コスト見積もり

| 期間 | On-Demand 概算（gr6.4xlarge / Sydney） |
|------|---------------------------------------|
| 1時間 | ~$1.30–1.60 USD |
| 1日（24h） | ~$31–38 USD |
| 1週間 | ~$220–270 USD |
| 1ヶ月（730h） | ~$950–1,300 USD |

### ASG Scale-to-Zero（3/5 完了）

4つの CR で段階的に修正・デプロイ:

| CR | 内容 | 状態 |
|---|---|---|
| CR-258091308 | スケーリングポリシー変更（10msg→1msg トリガー） | ✅ マージ・デプロイ済み |
| CR-258105410 | SQS メトリクス名修正（ハードコード→組み込みメソッド） | ✅ マージ・デプロイ済み |
| CR-258134912 | 無限ループ修正（ScaleUp 閾値 >=0 → >=1） | ✅ マージ・デプロイ済み |
| CR-258142848 | 運用手順書（CDKコメント + README 3モード） | 🔄 レビュー待ち |

### E2E 検証結果
- キュー1件 → ScaleUp アラーム発火 → EC2 自動起動 ✅
- キュー処理完了（3件） → 6分後スケールダウン → 0台 ✅
- 無限ループなし ✅
- GPU コールドスタート: 約10分（gr6.4xlarge）

### 3つの運用モード

| モード | min/max/desired | 用途 | 切り替え方法 |
|--------|----------------|------|-------------|
| Idle（デフォルト） | 0/1/0 | コスト節約、SQSで自動スケール | CDKデフォルト |
| Demo | 1/1/1 | Award/デモ、常時1台 | CLI `set-desired-capacity` |
| Campaign | 10/20/10 | 本番キャンペーン、10-20台自動スケール | CDK変更+デプロイ |

### Demo モード切替手順

```bash
# 1. クレデンシャル取得
cd /Users/saitshug/Development/repos/brazil-ws/BIL-TEX-APAC-MarsDine-MindReader/src/BIL-TEX-APAC-MarsDine-MindReaderCDK
brazil-build run updateCredential:prod

# 2. Demo モード ON（起動）
AWS_PROFILE=default aws autoscaling set-desired-capacity \
  --auto-scaling-group-name "MarsDineMindReaderServiceProd-MindReaderStack-VideoRenderClusterVideoRenderAutoScalingGroupASGE979BBA1-JxyzuwdhJrsj" \
  --desired-capacity 1 --region ap-southeast-2

# 3. Idle モード（停止）
AWS_PROFILE=default aws autoscaling set-desired-capacity \
  --auto-scaling-group-name "MarsDineMindReaderServiceProd-MindReaderStack-VideoRenderClusterVideoRenderAutoScalingGroupASGE979BBA1-JxyzuwdhJrsj" \
  --desired-capacity 0 --region ap-southeast-2
```

### 技術アーキテクチャ（検証済み）

```
User → CloudFront → API Gateway + WAF
                        ↓
                   Lambda x11 (TypeScript/Node.js 18.x)
                        ↓
        ┌───────────────┼───────────────┐
   Rekognition    SQS Queue      DynamoDB
   (猫検証)        ↓            (セッション管理)
              EC2 GPU ASG
              (gr6.4xlarge)
              FasterLivePortrait
              (Docker)
                   ↓
              S3 + CloudFront
              (動画配信)
```

### AWSアカウント・リージョン
- Prod: `988444123671` / ap-southeast-2 (Sydney)
- Beta: `406833061738` / ap-southeast-2
- Dev: `354488063304` / ap-southeast-2
- Pipeline: 7581534

### AWS クレデンシャル
```bash
# CDKパッケージディレクトリで実行
brazil-build run updateCredential:prod
# → default プロファイルに IibsAdminAccess ロールが設定される
# → AWS_PROFILE=default で ASG/SQS/CloudWatch 操作可能
# 注意: aki プロファイル(AWS_PROFILE env var)は別アカウント(bedrock用)、ASG権限なし
```

---

## 成果物一覧

```
2026-02-26_cat-decoder-tech-case-study/
├── handover.md                  ← このファイル
├── history/
│   ├── 2026-02-26_handover.md   ← 旧バージョン（圧縮）
│   └── 2026-03-05_handover.md   ← 旧バージョン（圧縮）
├── artifacts/
└── notes/
```

### コードベース成果物
- `lib/constructs/video-render-cluster.ts` — ScaleUp/Down ポリシー修正、メトリクス名修正
- `lib/stacks/mind-reader-stack.ts` — ASG 容量設定 + 3モード運用コメント
- `README.md` — ASG Operations セクション（CLI手順 + 3モード表）

### 外部成果物
- OneDrive: `/Projects/2026/TEX/Discovery/Tech Case Study - Mars Dine Cat Decoder/` (11ファイル)
- CDK Repo: `BIL-TEX-APAC-MarsDine-MindReaderCDK` (mainline)

---

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|----------|-----------|
| 1 | - | CR-258142848 マージ（ドキュメントのみ、インフラ変更なし） | レビュー待ち |
| 2 | Luke連絡待ち | Demo モードに切り替え（CLI: `set-desired-capacity 1`） | 待機中 |
| 3 | Award後 | Idle モードに戻す（CLI: `set-desired-capacity 0`） | 未着手 |
| 4 | TBD | テックケーススタディ プレゼン動画の構成決定・制作 | 未着手 |
| 5 | TBD | AI承認プロセス（AI Legal, AI Security, Mars AI Council）のストーリーまとめ | 未着手 |

---

## 重要な判断ログ

### 2026-02-26: コンテクスト収集完了
- OneDrive 11ファイル、CDKリポ構造、Quip 3ドキュメント読み込み
- プレゼン方向性: テックフォーカス、3P AI統合 + AI承認プロセス強調

### 2026-03-05: Scale-to-Zero 実装・4段階修正
- 当初のスケーリングポリシー（10msg閾値）は scale-to-zero に不適切 → 1msg に変更
- SQS メトリクス名がハードコードで間違っていた → 組み込みメソッドに変更（タイポ防止）
- ScaleUp 閾値 >=0 が無限ループの原因 → `{ upper: 0, change: 0 }, { lower: 1, change: +1 }` で threshold=1 に
- GPU コールドスタート ~10min のため、Award/デモ時は常時1台（Demo モード）を推奨
- Auto-scaling は SQS キュー深度ベースで正常動作を E2E 検証済み

### 2026-03-08: コスト確認・スタンバイ判断
- GPU インスタンス On-Demand ~$31-38 USD/日 → 常時起動はコスト高
- 一時的に Desired:1 に設定後、コスト確認を受けて即 Desired:0 にリバート
- Lukeからの Award エントリー連絡を待ってから Demo モードに切り替える方針に決定

---

## 関連トピック

- `daily-task-management` — Croc Awards エントリー管理
