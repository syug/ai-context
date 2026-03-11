# BIL-TEX-PetArmor-ProtectPlaytime-CDK FAST/ASR/GenAI調査結果

## 調査日: 2026-03-11

## 結論

**FAST統合・ASR・GenAIセキュリティ関連のコードは一切存在しない。**

このリポジトリはCCLP（Custom Campaign Landing Page）パイプライン用の標準テンプレートであり、
静的サイト（Brand Store）のS3+CloudFrontデプロイに特化している。
GenAI機能を含まないため、FAST/ASR統合は不要・未実装。

## リポジトリ構造

```
BIL-TEX-PetArmor-ProtectPlaytime-CDK/
├── lib/
│   ├── app.ts          # パイプライン定義（メイン）
│   └── accounts.ts     # AWSアカウントマッピング
├── Packaging/
│   └── CloudFormation.yml  # CDK出力のパッケージング
├── package.json
├── brazil.ion
└── cdk.json
```

## 依存関係

- `@amzn/pipelines` ^4.0.109 — Amazonパイプライン構成ライブラリ
- `@amzn/cclp-pipeline-constructs` ^1.0.0 — CCLP専用CDKコンストラクト
- `aws-cdk-lib` ^2.175.0
- CDKプラグイン: `@amzn/aws-cdk-isengard`, `@amzn/aws-cdk-conduit`

## パイプライン構成（app.ts）

- パイプライン名: `BIL-TEX-PetArmor-ProtectPlaytime`
- パイプラインID: `8752105`
- バージョンセット: `BIL-TEX-PetArmor-ProtectPlaytime/development`
- Bindle: `amzn1.bindle.resource.ejdvcxjh6adsej7ngqla`
- 通知先: `aleckunk@amazon.com`

### ステージ構成

1. **Gamma** (us-east-1, account 896349135024)
   - インテグレーションテスト: `BIL-TEX-PetArmor-ProtectPlaytime-Tests` パッケージ
   - アクセシビリティテスト（AAE）: 3つのscan ID、pipeline blocking有効
2. **Prod** (us-east-1, account 872247758570)
   - インテグレーションテスト・AAEなし

### 承認ワークフローステップ

パイプラインに含まれるのは以下のみ:
- `integrationTestsApprovalWorkflowStep` — Hydra Cypress E2Eテスト
- `accessibilityApprovalWorkflowStep` — AAE（Amazon Accessibility Evaluator）
- `CodeReviewVerificationApprovalWorkflowStep` — CR検証（オプション、現在未使用）

**FASTApprovalWorkflowStep は存在しない。**

## CCLP-Pipelines-CDK-Constructs の調査

パイプラインの実装を担うライブラリも全ファイルを確認:

### 検索対象キーワードと結果

| キーワード | 該当 | 備考 |
|-----------|------|------|
| FAST | なし | FASTThickClient, GenAISecurityPromptsService 等の参照なし |
| ASR | なし | Application Security Review の言及なし |
| GenAI / GenAISecurity | なし | GenAI関連のimportや設定なし |
| CloudAuth | なし | CloudAuth設定なし |
| Hydra | あり | テスト実行基盤として使用（FAST無関係） |
| prompt | なし | プロンプト関連なし |
| security | あり | WAF/Firewall設定のみ（FAST無関係） |

### Hydra統合（integration-test-stack.ts）

Hydraは `@amzn/hydra` パッケージの `IntegrationTest` コンストラクトとして使用。
用途はCypressベースのE2Eテスト実行であり、FAST/GenAIセキュリティとは無関係。

```typescript
this.integTest = new IntegrationTest(this, 'IntegrationTest', {
  stepName: `Hydra Cypress Test - ${stage}`,
  testContainer: {
    imageArtifactName: testPackage.name,
    environmentVariables: {
      SSM_PARAMETER_NAME: parameterName,
      AWS_REGION: region,
      BASE_URL: baseUrl?.toString() || '',
    },
  },
  testPackageName: testPackage.name,
  computeTimeout: MAX_TIMEOUT,
  timeout: MAX_TIMEOUT.toMilliseconds(),
});
```

### セキュリティ関連（cclp-firewall-stack.ts）

WAFv2 WebACLによるCloudFrontファイアウォール。AWS Managed Rule Groupsを使用:
- AWSManagedRulesCommonRuleSet
- AWSManagedRulesKnownBadInputsRuleSet
- AWSManagedRulesSQLiRuleSet
- AWSManagedRulesLinuxRuleSet / UnixRuleSet / WindowsRuleSet
- AWSManagedRulesAnonymousIpList
- AWSManagedRulesBotControlRuleSet
- AWSManagedRulesAdminProtectionRuleSet

これはWebアプリ保護用のWAFであり、GenAIセキュリティとは無関係。

### Mote CDK（セキュリティコンプライアンス）

`@amzn/motecdk` のSecure*コンストラクト（SecureBucket, SecureDistribution, SecureRole等）を使用。
これはAmazonの内部セキュリティコンプライアンスライブラリで、FAST/ASRとは別系統。

## まとめ

このCDKリポジトリはCCLP（静的キャンペーンページ）のCI/CDパイプライン定義であり:
- GenAI機能を一切含まない
- FAST統合コードは存在しない
- ASR関連の設定やコメントもない
- CloudAuth設定もない
- Hydraは純粋にE2Eテスト用途

**AI on CLPの参考としてFAST統合パターンを探す場合、別のリポジトリ（GenAI機能を含むサービスのCDK）を調査する必要がある。**
