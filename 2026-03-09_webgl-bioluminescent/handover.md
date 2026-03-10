# Handover Document
**Topic:** 深海生物発光アンビエント WebGL プログラム
**Date:** 2026-03-09
**Status:** 進行中（パフォーマンス最適化が必要）

---

## 背景

デジタルアートインスタレーション風の動的アンビエント映像を生成するWebGLプログラムの作成。参考画像は深海の生物発光的有機体（クラゲ・サンゴ風の半透明発光体が暗闇に浮かぶビジュアル）2枚。teamLab風の高品質ビジュアルをリアルタイムシェーダーで実現することが目標。

## 現在の状況

### マルチエージェントプランニング（完了）

3つのAIソースからアイデア・技法を収集:
- **Gemini-CLI** — クリエイティブアイデア: Medusae SDF、KIFS coral、Curl Noise、Fresnel rim、distance-aided glow、4フェーズ実装プラン
- **Kiro-CLI** — アーキテクチャ設計: single-pass ray march、smin融合、domain warping、hash-based analytical particles、パフォーマンスバジェット
- **Web Research (Shadertoy/iq)** — 技法リファレンス: cubic smin、tetrahedron normal、layered domain warping、FBM rotation trick、HDR bloom

### 実装（完了、最適化済み）

単一HTMLファイル（WebGL2、依存ゼロ）で実装完了:
- Ray marching (80 steps) + SDF
- 2体のクラゲ（半球シェル + 8触手 + パルスアニメーション）
- 3つのサンゴクラスター（smin融合 + FBM displacement）
- 15個のボケパーティクル（hash-based、ゆっくり浮遊）
- Glow蓄積（fake SSS/bloom）+ Fresnel rim + volumetric light
- ゆっくりカメラオービット
- シアン/オレンジ/ゴールド/エメラルドのカラーパレット
- Reinhard tonemap + gamma + vignette

### パフォーマンス最適化（適用済みだが不十分）

以下を適用したが、ユーザーからまだ重いとのフィードバック:
- 0.75x解像度スケーリング
- FBM 5→3オクターブ
- Domain warping簡略化（fbm→snoise直接）
- クラゲ3→2、パーティクル30→15
- MAX_STEPS 128→80、epsilon 0.001→0.002
- バウンディングスフィアチェック
- Volumetric隔ステップサンプリング
- アダプティブステップサイズ

## 成果物一覧

```
2026-03-09_webgl-bioluminescent/
├── handover.md
├── artifacts/
│   └── index.html          # WebGL2 単一ファイルプログラム（14.5KB）
└── notes/
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | - | さらなるパフォーマンス最適化（まだ重い） | 未着手 |
| 2 | - | 0.5x解像度 or half-res render + upscale検討 | 未着手 |
| 3 | - | FBMをvalue noiseに簡略化、またはLUT化 | 未着手 |
| 4 | - | クラゲ1体 + コーラル1つに削減して試す | 未着手 |
| 5 | - | 2-pass approach（低解像度で形状→高解像度でcomposite）検討 | 未着手 |

## 重要な判断ログ

- **Single-pass ray march採用**: Multi-pass（FBO）はJS boilerplateが増え単一ファイルの簡潔さを損なうため、single-passでglow蓄積・volumetric・fakeSSS全てをmarchループ内で処理する方式を採用
- **kiro vs kiro-cli**: `kiro`（/usr/local/bin/kiro）はGUIアプリ、`kiro-cli`（~/.toolbox/bin/kiro-cli）がCLIツール。CLIパイプラインは `kiro-cli chat "prompt" --no-interactive`
- **パフォーマンス問題**: 10項目の最適化を適用したが、ユーザー環境ではまだ重い。根本的なアプローチ変更（2-pass、大幅な複雑度削減）が必要かもしれない

## 関連トピック

- 参考画像: `$AI_BASE/../.TemporaryItems/IMG_4905.HEIC`, `IMG_4906.HEIC`（Google Drive .TemporaryItems内）
