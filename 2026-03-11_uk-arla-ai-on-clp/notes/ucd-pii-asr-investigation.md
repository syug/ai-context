# Undefined Customer Data (UCD) & PII Risk Investigation

Date: 2026-03-11
Context: BIL Campaign CLP上のAI機能（フリーフォームテキスト入力）のASR分類とPIIリスク

---

## 観点1: Undefined Customer Data の分類

### 結論: フリーフォーム入力 = UCD = Critical = Red ASR

**1. フリーフォームテキスト入力はUCDに該当するか？ → YES**

> "Undefined customer data usually means open input (no enforcement). So if you had a form that has no restrictions on what could go inside it (such as customer feedback, delivery instructions, etc.) that is all considered undefined customer data. It's considered undefined because a user could theoretically enter any type of data into it."
> — Slack #amazon-security-reviews-interest (2026-02-16, kodysk)

> "UCD elements are classified as Critical unless specifically classified otherwise in DACE, and must be handled in accordance with the Undefined Customer Data Handling Standard."
> — Data Classification FAQ (policy.a2z.com/docs/875)

**2. 「Does your system handle undefined data for more than one customer?」→ Yes の場合 Red か？ → YES**

ASR Profiles Wiki (https://w.amazon.com/bin/view/Infosec/Proactive_Security/Dev/SecurityReviewTooling/ASR/Profiles/) より:

RED CLASSIFICATION criteria:
- Handles Critical or Restricted data
- **Handles undefined data for more than one customer**
- Uses GenAI AND (handles HR PII data OR GenAI is business critical)

> "More than one customer generally is any system that is not operating on a single personal device. The vast majority of all services fall into this bucket."
> — Slack #amazon-security-reviews-interest (2026-02-16)

**3. GenAI + フリーフォーム = ダブルでRed**

GenAI単体ではOrange分類だが、UCDを扱う場合はCriticalデータ → Red。
さらにGenAI + business criticalの場合もRed。

**4. "handle" の定義 — 保存しなくてもhandleに該当するか？ → YES**

> "And 'handle' is pretty much whether it does anything at all with it. I generally consider it has handling if it *has access* to it."
> — Slack #amazon-security-reviews-interest (2026-02-16, dmmcalla - Security Certifier)

データを保存しなくても、LLMに渡す時点で「handle」に該当する。

**5. TTLで短期間削除する場合は分類が変わるか？ → NO（分類自体は変わらない）**

Data Handling Standardでは、Critical/UCDデータに対するretention要件は別途あるが、
データ分類（Critical/Red）自体はTTLの有無で変わらない。
処理した時点でCritical扱い。

**6. BILキャンペーンCLP上のユーザー入力の分類**

外部顧客（Amazon shopper）がCLP上でフリーフォーム入力 → UCD → Critical。
「more than one customer」にも該当 → **Red ASR classification**。

---

## 観点2: PII リスクの回避方法

### 結論: UIラベルでは分類は下がらない。PIIフィルタリングは必須だが分類は下がらない。

**1. UIに「個人情報を入力しないでください」ラベルを追加で分類を下げられるか？ → NO**

> "If I inform the customers not to put personal data into the text field, will that downgrade the data classification of the text?"
> "**Disclaimers or warnings about the customer text field do not lower the data classification. Therefore, the data will remain as undefined customer data (UCD).**"
> — Stores GenAI FAQ (https://w.amazon.com/bin/view/InfoSec/Application_Security/AppSTAR/Appsec_AI/FAQ/)

**2. PIIフィルタリング/リダクションで分類を下げられるか？ → 実質NO（ケースバイケースだがハードルが極めて高い）**

Down-classifying Wiki (deprecated but informative):
- UCIサニタイザー（AWS Comprehend, Bit Shredder等）を通してPII除去すれば、残りデータはHCにできる**可能性がある**
- ただし「Infosecのケースバイケースレビューが必須」
- アプリ自体はRedのまま（Critical dataを処理する時点があるため）
- サニタイズ後のデータに対する操作のみHC扱いにできる

Slack #amazon-security-reviews-interest (2026-02-20):
> "It's unstructured, so it's red. Anything you do to red data after that is only a best guess at trying to make it less red. So most secure treatment is to still assume it is red."
> — kodysk

> "How can I Lower Classification of GenAI Critical Data to Highly Confidential or below?"
> "**Customer GenAI data is amongst the most sensitive data handled at Amazon. There are currently no exceptions to this process.**"
> — Stores GenAI FAQ

**3. PIIフィルタリングは分類を下げなくてもASR要件として必須**

Security Engineer Review Guide for GenAI Apps:
> "Builder team's must implement personal data filtering for prompts, responses and any free-form feedback data provided by users."
> "For redacting personal data within prompts and responses on Bedrock, builder teams are recommended to use built-in PII guardrails within Bedrock."

ASR GenAI Profile必須タスク: "Prompt Data Input Validation" — PIIフィルタリング実装が求められる。

**4. Bedrock データ処理ポリシー**

- Bedrock内部利用では、デフォルトでcustomer dataはモデルトレーニングに使用されない
- AWS Organizations opt-out policyでも制御可能
- Bedrock Guardrails の Sensitive Information Policy でPII検出・マスキングが可能
  - SSN, DOB, address, credit card等の自動検出
  - カスタムregexパターンも設定可能

---

## 我々のケースへの影響

### BILキャンペーンCLP上のAI機能の場合:

| 要素 | 状況 | 影響 |
|------|------|------|
| フリーフォーム入力あり | Yes | UCD = Critical |
| 複数顧客のデータ | Yes（外部顧客） | Red ASR |
| GenAI使用 | Yes | 最低Orange、UCD + GenAIでRed |
| UIラベルで分類低下 | No effect | 分類は変わらない |
| PII sanitization | 分類は下がらないがASR要件として必須 | 実装必須 |
| データ非保存 | handleの定義に変わりなし | 分類は変わらない |

### 取りうるアプローチ:

1. **フリーフォーム入力を排除する** → 事前定義プロンプト（allow-list）にすれば UCD回避可能
   > "If a builder team would like to implement an allow-list approach (potentially to not implement Critical data handling controls), they can choose to have a pre-defined list of prompts that their users can select. In these situations, the classification of such prompts will be the classification of pre-defined prompts (and not UCD - Critical)."

2. **Red ASR certificationを受ける** → 4-6週間 + Prompt Testing 2-4週間

3. **ハイブリッド**: V1はallow-list onlyでOrange、V2でフリーフォーム追加してRed certification

---

## Sources

- ASR Profiles: https://w.amazon.com/bin/view/Infosec/Proactive_Security/Dev/SecurityReviewTooling/ASR/Profiles/
- Stores GenAI FAQ: https://w.amazon.com/bin/view/InfoSec/Application_Security/AppSTAR/Appsec_AI/FAQ/
- Down-classifying free-form text: https://w.amazon.com/bin/view/Down-classifying_Customer_submitted_content_in_free-form_text_fields/
- Data Classification FAQ: https://policy.a2z.com/docs/875/publication
- Data Handling Standard: https://policy.a2z.com/docs/99/publication
- Security Engineer Review Guide for GenAI: https://w.amazon.com/bin/view/InfoSec/Application_Security/AppSTAR/Appsec_AI/Security_Engineer_Review_Guide_for_GenAI_Apps/
- Prompt Testing: https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Guidance/Prompt_Testing/
- DACE: https://prod.dace.infosec.amazon.dev/search
- Slack threads: #amazon-security-reviews-interest (2026-02-16, 2026-02-20)
