# Deep-Sea Bioluminescent Ambient — WebGL2

リアルタイムWebGL2シェーダーで深海の生物発光的有機体を描画するアンビエント映像プログラム。

## 使い方

```
open artifacts/index.html
```

ブラウザで開くだけ。依存ゼロ、サーバー不要。

## 技術構成

- Single HTML file（14.5KB）、WebGL2、外部依存なし
- Fragment shader: Ray marching + SDF
- Simplex 3D noise → FBM → Domain warping
- Jellyfish (2体): hemisphere shell + 8 tentacles + pulse
- Coral clusters (3つ): smin-blended spheres + FBM displacement
- Bokeh particles (15個): hash-based analytical
- Glow accumulation (fake SSS/bloom) + Fresnel rim + volumetric light
- Reinhard tonemap + gamma correction + vignette
- Slow orbiting camera

## パフォーマンスノート

現状、GPU負荷が高い。改善候補:
- 解像度をさらに下げる（0.5x）
- FBMをvalue noiseに簡略化
- オブジェクト数削減
- 2-pass render（低解像度で形状→高解像度でcomposite）

## 参考

- 参考画像: 深海生物発光のデジタルアートインスタレーション（teamLab風）
- 技法: Gemini-CLI + Kiro-CLI + Shadertoy/iq リサーチから統合
