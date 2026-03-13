# Julia への返信 — 簡潔メール版

**Subject:** RE: UK Arla Campaign -- AI on CLP: MARSの経験からの学び

---

## 1. AI承認プロセス

3つの承認トラックが並行して走ります：

- **Amazon社内承認**（Legal/PR）-- `approvals.amazon.com` 経由で提出
- **Amazon Security Review (ASR)** -- 当アプリは**Red**（最高ティア）に分類。フリーフォームテキスト入力を受け付けたため。専任セキュリティレビュアーと12件のGenAI固有タスクが必要に
- **クライアント外部承認** -- Mars のグローバル法務・セキュリティチームによるGenAI使用の個別承認。最終的に最も時間がかかった項目

**2026年の重要な変更：** フリーフォーム入力を扱わないGenAIキャンペーンはASRで**Orange**に分類され、self-certificationが可能に。大幅に簡素化されたプロセスです。対象となるかは入力設計次第です（Q4参照）。

---

## 2. 承認タイムライン

| トラック | 期間 | 備考 |
|-------|----------|-------|
| 社内 Legal/PR | 約3週間 | ドキュメントが揃えば比較的スムーズ |
| ASR (Security Review) | 4-6週間 | DT工数：約90時間（標準 + GenAI固有） |
| クライアント GenAI 承認 | **3ヶ月以上** | 想定以上に長期化 -- クリティカルパスに |

参考までに、MARSプロジェクトの実績タイムライン：ASRアプリケーション作成が2024年3月11日、GenAI AppSecチーム関与が7月19日頃、リリースが8月29日。ASRレビュー実期間は約6週間で、ギリギリのスケジュールでした。ASRレビューに2-3ヶ月確保することを推奨します。

**アドバイス：** クライアントのGenAI承認トラックはできるだけ早く開始してください。UX/UI承認とは別トラックであり、ボトルネックになりやすいです。

**2026年：** Orange ASR対象（プリデファインド入力のみ）であれば、ASR部分はFAST self-certificationで数週間から数日に短縮可能。

---

## 3. 入力処理とGuardrails

リアルタイムの人的モデレーションは**不採用**。代わりに3本柱で対応しました：

1. **多層自動ガードレール** -- フロントエンドバリデーション、AWS WAF、API Gatewayコントロール、アプリケーションレベルのサニタイゼーション、Amazon Bedrock Guardrails（コンテンツフィルター、禁止トピック、ワードフィルター、PIIブロック）、出力制約（レスポンスをYES/NO/BLOCKEDのみに制約 -- 生のLLMテキストが顧客に表示されることは一切なし）の6層構成
2. **徹底的なローンチ前テスト** -- FAST自動プロンプトセキュリティテスト、GenAI AppSecによるペネトレーションテスト、全ステークホルダーによるハンズオンUAT
3. **インシデントレスポンス** -- 正式な対応計画 + **Andon Cord**キルスイッチによるAI即時シャットダウン（ASR必須）

---

## 4. プリデファインド vs. フリーフォーム入力

おそらくキャンペーンにとって最も重要な設計判断です。

MARSではフリーフォーム入力（最大100文字）+ 多層ガードレールを選択しました。プリデファインドだけではクライアントのクリエイティブ要件を満たせず、プリデファインドのみならLLM自体が不要だったためです。トレードオフ：**フリーフォーム入力 = Undefined Customer Data (UCD) = Red ASR分類**。免責事項やUI警告ではこの分類は変わりません -- 入力フィールドの存在そのものがトリガーです。

**2026年の推奨 -- 段階的アプローチ：**
- **V1：** プリデファインドプロンプトのみ -> Orange ASR -> self-certify -> 迅速なローンチ
- **V2（必要に応じて）：** フリーフォーム入力追加 -> Red ASR -> フルセキュリティレビュー

DTチームの「プリデファインドメッセージ/プロンプトが必要かも」という直感は戦略的に正しいです。セキュリティ分類と承認パスを根本的に変えます。

---

## 5. AIモデルとインフラストラクチャ

**Anthropic Claude 3 Sonnet** を Amazon Bedrock 上で使用。RAG構成（Knowledge Bases + OpenSearch Serverless）。主要な技術判断：temperatureは**0.0**（完全に決定論的）、Single-turnのみ（会話永続化なし）、全てAmazonインフラ内でホスト（Bedrock要件として外部AI APIは不可）。インフラ：Lambda、API Gateway、DynamoDB（ログ用）、CDK Pipeline、3環境構成。

Arlaのジングル生成ではモデル選択は異なる可能性が高いですが（分類ではなくクリエイティブ生成）、インフラパターンとセキュリティアーキテクチャは非常に類似したものになるでしょう。

---

## 6. ドキュメント

主要な社内リソース：

| リソース | リンク |
|----------|------|
| ASR Profiles & Classification Rules | https://w.amazon.com/bin/view/Infosec/Proactive_Security/Dev/SecurityReviewTooling/ASR/Profiles/ |
| FAST Framework (v2) | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/ |
| FAST Integration SOP (BIL TEX) | https://quip-amazon.com/FhvFAKBxf6Tu/SOP-FAST-Integration |
| Generative AI for Campaign（私が書いたガイド） | https://quip-amazon.com/aa1OAHdOJgua/Generative-AI-for-Campaign |
| BIL Approved AI Tools | https://w.amazon.com/bin/view/BIL-E/NA/BIL-AI-Tools |
| GenAI Security Standard (policy) | https://policy.a2z.com/docs/613805/publication |
| Andon Cord Guidance | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Guidance/Andon_Cords/ |

---

## 7. 学んだこと

1. **クライアントGenAI承認は初日から開始すべき。** 私たちは3ヶ月以上かかり、クリティカルパスになりました。詳細なAI概要ドキュメントを早期にクライアントに準備してください。
2. **フリーフォーム入力 = Red ASR。これは絶対。** 入力設計にコミットする前にこの連鎖を理解してください。セキュリティタイムライン全体を決定します。
3. **Andon Cordは必須。** 即時キルスイッチ + 文書化されたSOP + デモ録画が求められます。ASRで交渉の余地なし。
4. **制約を前提に設計する。** 最も強力な安全対策は生のLLMテキストを表示しなかったこと。ジングル機能における「最小限のAI出力」が何かを検討してください。

