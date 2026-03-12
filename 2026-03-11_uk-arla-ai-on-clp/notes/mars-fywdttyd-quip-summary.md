# Mars FYWDTTYD - Quip Folder Summary
## Julia Sampaio (UK BIL) 7 Questions Reference

Source: https://quip-amazon.com/Tnk0OtquZA7d/AU-Mars-FYWDTTYD-
- Main folder: 19 documents + 1 subfolder (ASR, 31 documents)
- Project: APAC Brand Innovation Lab, Amazon Ads, Mars Inc. campaign
- Campaign period: Aug 28 - Oct 5, 2024 (6 weeks)

---

## 1. AI Approval Process Overview and Teams Involved

### Teams Involved
| Team | Role | Key People |
|------|------|-----------|
| Local Legal/Policy | AU legal approval | Jessica Baxter (jesbaxte) |
| Local PR | AU PR approval | Gemma McMahon (gemcm), Jessica Makin (jmakin) |
| Global Legal/Policy/PR | Global coordination | (In progress during project) |
| InfoSec / AppSec | Security review via ASR | AJ Lopez (antonjl), Anshuman Bhatnagar (anshumbh) - GenAI AppSec |
| GenAI-Sec Team | GenAI security consultation | genai-sec-secengs@amazon.com |
| BIL Finance | Cost approval | - |
| Client (Mars, Inc.) | External approval on UX/UI + GenAI | Mars global team |

### Approval Tracks (3 Parallel)
1. **Internal Amazon Approvals** (Legal/PR/Business)
   - Approval for FM usage: https://approvals.amazon.com/Approval/Details/28267898
   - Template: https://approvals.amazon.com/template/edit/148686

2. **Amazon Security Review (ASR)** - Classification: **RED**
   - ASR ID: #1710164373
   - Standard ASR tasks + GenAI-specific ASR tasks (12 items)
   - Self-service review → Security engineer assigned → Review completion

3. **Client/External Approvals**
   - UX/UI approval from Mars
   - GenAI-specific approval from Mars global legal/security

### ASR GenAI Specific Tasks (12 items)
1. Review AI Training Data
2. Monitoring Training Data
3. Review AI Model
4. Data Leak Check
5. Prompt Data Sanitization
6. Review Andon Cord
7. Onboard to Transitive Auth
8. AI Response Logging
9. AI GuardRails
10. Validate Siloed Sessions
11. Onboard to Bug Bounty
12. Security Prompt Testing

---

## 2. Approval Timeline

| Phase | Timeline | Activity |
|-------|----------|----------|
| Pre-sales: CX/Technical Design | March 4-22, 2024 | CX flow, dataflow diagram, full-scoping |
| Pre-sales: Brand Safety Plan | March 25 - April 5 | Brand safety documentation |
| Pre-sales: Local Legal/PR Connect | March 25 - April 5 | Connect with AU legal/policy/PR |
| Pre-sales: Legal/PR/Business Approval | April 15 - May 3 | **Received internal Amazon approvals** |
| Pre-sales: Client Approvals (UX/UI) | April 3-12 | In progress |
| Pre-sales: Client Approvals (GenAI) | April 8-19 + May 20 - July 14 | Extended for GenAI specifics |
| Execution: ASR Self-Service Start | April 8-12 | Started self-service review |
| Execution: GenAI Data Classification (DACE) | June 24 - Aug 9 | Classification: Critical, Undefined Customer Data |
| Execution: GenAI-Sec Consultation | June 24 - Aug 9 | SIM: P137468634 |
| Execution: Security Engineer Request | June 24 - Aug 9 | SIM: P139902821 |
| Execution: FAST Setup | June 24 - Aug 9 | Framework for AI Security Testing |
| Execution: Kale Privacy Attestation | June 10 - June 28 | Completed |
| ASR Kickoff Meeting | July 24, 2024 | With GenAI AppSec team |
| ASR All Tasks Target | August 19, 2024 | Architecture, Threat Model, Code Review, Pentest, etc. |
| Security Approval Target | August 26, 2024 | Final signoff |
| Campaign Launch | August 28, 2024 | Go live |

**Estimated ASR Duration:** "(1) Self-service review 2-3 weeks then (2) Review by InfoSec 2-3 weeks = **4-6 weeks in total**"

**Total DT Effort for Security:** ~90 hours (45 Standard ASR + 45 GenAI ASR)

---

## 3. User Input Guardrails / Filters / Moderation

### Multi-Layer Defense Architecture

#### Layer 1: Input Validation (Code-level)
- Input character limit: **200 characters** max
- Emoji stripping and pattern filtering
- Code: `src/utils/validateInputText.ts`

#### Layer 2: Amazon Bedrock Guardrails (4 filters)
All inputs/outputs detected by guardrails → response = 'BLOCKED'

**a) Content Filters** (High strength on all):
- Input: Hate / Insults / Sexual / Violence / Misconduct / Prompt Attack
- Output: Hate / Insults / Sexual / Violence / Misconduct

**b) Denied Topics:**
- Politics / Competitors / Brand safety / Security / Religion
- Example: "I attended the support meeting for Donald Trump" → BLOCKED

**c) Word Filters:**
- Profanity filter: Enabled
- Custom blocked words: 50+ competitor names (Nestle, Cadbury, Hershey's, Ferrero, Godiva, etc.)

**d) Sensitive Information Filters (PII):**
- Name / Phone / Email / Address / Age / Username / Password / etc.

#### Layer 3: Response Simplification (Three-way output)
> "Response from Bedrock API will be simplified in three form — YES, NO, or BLOCKED"
> "customer won't directly interact with FM on Bedrock and no direct response from FM will be surfaced to customer by design"

#### Layer 4: Implicit Guardrails (Prompt-level)
- "Crafted directly into prompts to steer responses towards predictable outcomes"
- Prompt includes: "refuse to perform task", "respond in harmless way", etc.

#### Layer 5: WAF (Network-level)
- AWS WAF for IP-based rate limiting and referrer check

### Post-launch Monitoring
| Cadence | Activity | Owner |
|---------|----------|-------|
| On-demand | Internal issue reporting | Project members |
| On-demand | CloudWatch Alarms (auto) | System |
| Weekly | Batch data check with collected input/output | BIL |
| Bi-weekly | Manual data review | BIL |

### Andon Cord System
- Environment variable `USE_BEDROCK_API` on Lambda
- Set to `false` → immediately disables GenAI functionality
- Triggers: harmful output, privacy/security breach, manual report
- Full SOP documented with demo recordings

---

## 4. Free-form Input vs Pre-defined Prompts Decision

### Decision: **Free-form text input** (with heavy guardrails)

**Rationale from the project:**
> "The application will be taking **customer submitted contents** of free form text fields as input to the API."

However, the output is **strictly pre-defined**:
> "Messages to customers will be assembled on the backend in pre-defined format based on the AI responses, rather than employing bare AI responses intact."

### Hybrid Approach Details:
- **Input**: Free-form text (up to 200 chars), customers type what "thing" they did
- **Processing**: RAG + prompt engineering (not raw LLM response)
- **Output**: Only 3 possible outcomes: "That's a thing!" (YES) / "Not a thing" (NO) / Blocked message (BLOCKED)
- **No LLM text exposed**: Raw model response is never shown to customers

### Q&A on Input Recognition:
> Q: "Will the tool be recognizing (1) Only exact prompts (2) Similar wording (3) Endless possibilities?"
> A: "In the middle ground between 2 and 3"

This was classified as **Undefined Customer Data** → **Critical** data type because of the free-form input.

---

## 5. AI Model and Infrastructure

### Model Stack
| Component | Technology |
|-----------|-----------|
| Foundation Model | **Anthropic Claude 3 Sonnet** (hosted on Bedrock) |
| Embedding Model | **Cohere Embed English v3** (for Knowledge Bases) |
| Vector Store | **Amazon OpenSearch Serverless** |
| Knowledge Base | **Amazon Bedrock Knowledge Bases** |
| Guardrails | **Amazon Bedrock Guardrails** |

### Infrastructure
| Component | AWS Service |
|-----------|------------|
| Compute | AWS Lambda |
| API | API Gateway (REST) |
| Database | DynamoDB (input/output logging) |
| Storage | S3 (knowledge base data source + logs) |
| Security | AWS WAF, CloudWatch Alarms, CloudTrail |
| Monitoring | CloudWatch (6 log groups), QuickSight dashboard |
| Region | us-west-2 (Oregon) |
| Pipeline | CDK Pipeline via code.amazon.com |

### Model Configuration
```
textInferenceConfig: {
  temperature: 0.0,  // Deterministic
  topP: 1,
}
```

### Technique: RAG (not Fine-tuning)
> "Fine-tuning could degrade the performance of the LLM and increase the risk of hallucinations. With a small dataset, the risk of degrade/hallucinations could be increased."

### Data Source for Knowledge Base
- Condition list: ~314 "A thing" items + "Not a thing" items
- Prepared by BIL APAC and Mars, Inc.
- Stored in S3, indexed into OpenSearch Serverless vector store

---

## 6. Reference Documents

### Key Quip Documents
| Document | URL | Purpose |
|----------|-----|---------|
| AI Tool Overview | quip-amazon.com/COA9AAube8H | Comprehensive overview |
| Development Overview | quip-amazon.com/HCX9AA27IXv | Steps, timeline, prototype links |
| Brand Safety | quip-amazon.com/cDE9AAtC6JZ | Brand safety plan + data classification |
| Guardrails Spreadsheet | quip-amazon.com/HOS9AAjVlDA | Denied topics, blocked words, PII filters |
| Technical Design | quip-amazon.com/TaP9AAhSVBW | RAG vs Fine-tuning decision |
| ASR Kickoff | quip-amazon.com/eMB9AAuTK7R | Security review kickoff, classification RED |
| Incident Response Plan | quip-amazon.com/KVP9AAGhfYA | IRP with communication plan |
| Andon Cord System | quip-amazon.com/cOB9AAZJMTd | SOP for disabling AI |
| Monitoring Runbook | quip-amazon.com/HDL9AAOjfD6 | Operational monitoring procedures |

### Key External Links
| Resource | URL |
|----------|-----|
| ASR Application | asr.security.amazon.dev/applications/d1f8d647-c905-48af-be66-d96231698216 |
| DACE Data Classification | prod.dace.infosec.amazon.dev (Critical / Undefined Customer Data) |
| Legal Approval | approvals.amazon.com/Approval/Details/28267898 |
| GenAI-Sec Consultation SIM | P137468634 |
| AppSec Review Request SIM | P139902821 |
| FAST Onboarding SIM | P137096440 |
| Design Inspector Diagram | design-inspector.a2z.com/#IAPAC-BIL-Campaign-Mars-FYWDTTYD-Diagram |
| Kale Privacy Attestation | kale.amazon.dev/APAC-BIL-Campaign-Mars-FYWDTTYD/reviews/54612 |

### Wiki References
| Resource | URL |
|----------|-----|
| GenAI ASR Review Process | w.amazon.com/bin/view/InfoSec/.../Generative_AI/Review_Process |
| GenAI-Sec Team | w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec |
| FAST Framework | w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework |
| Andon Cord Guidance | w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Guidance/Andon_Cords/ |
| Bedrock Legal FAQ | w.amazon.com/bin/view/AmazonBedrock/Support/FAQ |
| Bedrock Guardrails | w.amazon.com/bin/view/AmazonBedrock/Guardrails/GetStarted |

---

## 7. Lessons Learned and Pitfalls

### Timeline Challenges
- **Client approval for GenAI took much longer than UX/UI**: Originally April 8-19, extended to May 20 - July 14 (3+ months)
- **ASR is 4-6 weeks**: Self-service 2-3 weeks + InfoSec review 2-3 weeks. Start early.
- **Total DT scoping: 405 hours (67.5 days)**: 90h prompt engineering + 90h backend + 90h ASR + 78h frontend + 57h claim page
- **Guardrails for Bedrock was in limited preview** when project started (April 2024), had to request access via ticket P126538023

### Technical Pitfalls
1. **FAST framework issues**: "Hydra testing with FAST fails with `ResponseMissingError`" (SIM: P138723163)
2. **FAST v1 → v2 migration**: Had to migrate mid-project
3. **CloudAuth onboarding**: Required for FAST integration, additional complexity (SIM: P140765954)
4. **Misspelled blocked words**: Not all misspellings are caught
   > "Blocked: Nestle, Nestel, Nestele, Nestlee / Not blocked: Nesltle, Nestele, Nestlw"
5. **Design Inspector flagged HIGH risk**: "Logging Sensitive Data" - required InfoSec consultation (SIM: P136675016)
6. **Data classification as Critical**: Free-form input = "Undefined Customer Data" = Critical, which triggers RED ASR classification

### Architecture Decisions
1. **RAG over Fine-tuning**: "Fine-tuning could degrade performance and increase hallucination risk with small datasets"
2. **Three-way output (YES/NO/BLOCKED)**: Prevents raw LLM output from reaching customers - key safety measure
3. **Single-turn sessions only**: No multi-turn conversation, no session persistence - simplifies security (silo user sessions)
4. **No safe mode**: Application operates with minimum FM functionality, no training applied
5. **No model versioning**: Single version for 6-week campaign, no updates once live

### Process Lessons
1. **Parallel approval tracks are essential**: Legal/PR, ASR, and client approvals ran concurrently
2. **GenAI-specific security tasks are substantial**: 12 additional items on top of standard ASR
3. **DACE data classification should be done early**: Required for GenAI ASR review
4. **Kale privacy attestation is separate**: Additional privacy review step
5. **Prepare AI tool overview document for client**: Mars required detailed documentation before giving GenAI approval
6. **Andon cord is mandatory**: Must have ability to disable GenAI instantly with documented SOP and demo recording
7. **All prompts/responses must be logged**: Separate from regular security logs, stored in DynamoDB + S3 + CloudWatch
