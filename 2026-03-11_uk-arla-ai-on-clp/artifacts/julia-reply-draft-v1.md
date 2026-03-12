# Draft Reply to Julia Sampaio — v1

**Subject:** RE: UK Arla Campaign — AI on CLP: Learning from your MARS experience

---

Hi Julia,

Thanks for reaching out — great to hear about the Arla campaign concept! Happy to share what we learned from the MARS "For You Who Did That Thing You Did" (FYWDTTYD) campaign. I'll walk through your questions from a technical perspective below.

## 1. AI Approval Process

We had **three parallel approval tracks** running simultaneously:

- **Internal Amazon approvals** (Legal/PR/Business) — submitted via `approvals.amazon.com`. We connected with local Legal and PR early in pre-sales.
- **Amazon Security Review (ASR)** — our application was classified as **Red** (the highest security tier), which required a dedicated security reviewer from the GenAI AppSec team. On top of the standard ASR tasks, we had **12 additional GenAI-specific tasks** including: Review Training Data, Review AI Model, Prompt Data Sanitization, Andon Cord review, FAST (Framework for AI Security Testing) onboarding, AI Response Logging, Guardrails validation, Siloed Sessions validation, and Bug Bounty onboarding.
- **Client external approval** — Mars Inc.'s global legal/security team needed to separately approve the use of GenAI in the campaign. This was a distinct track from UX/UI approval.

**Important note on ASR classification:** The reason we got Red was that we accepted **free-form text input** from customers. Under Amazon's data classification policy, free-form customer input = Undefined Customer Data (UCD) = Critical data = Red ASR. This is probably the single most important thing to understand early in your design process (more on this in Q4).

## 2. Approval Timeline

| Track | Duration | Notes |
|-------|----------|-------|
| Internal Legal/PR | ~3 weeks | Relatively straightforward |
| ASR (Security Review) | 4-6 weeks | Self-service 2-3 weeks, then InfoSec review 2-3 weeks. DT effort: ~90 hours (45h standard + 45h GenAI-specific) |
| Client GenAI approval | **3+ months** | This was significantly longer than expected. Mars's global legal/security team required detailed AI documentation before sign-off |

My advice: **start the client GenAI approval track as early as possible** — it's a separate track from UX/UI approval and can easily become the critical path.

## 3. Input Handling & Guardrails

We implemented a **multi-layered defense architecture**:

**Frontend:**
- 100-character input limit
- T&C checkbox (mandatory) with explicit disclaimer: *"You agree that you will not enter sensitive personal data of another individual"*
- AI purpose disclaimer: *"AI powered for entertainment purposes"*

**Network/API:**
- AWS WAF with 6 rules (IP rate limiting at 2,000 req/5min, bot control, known bad inputs, anonymous IP blocking)
- API Gateway with CORS whitelist, 30 req/s throttling, and request body validation
- Lambda Authorizer with origin whitelist + token verification

**Application:**
- `validateInputText` pipeline: 100-char truncation → lowercase → multi-byte character normalization → emoji stripping → URI encoding → CRLF removal
- Input wrapped in structured prompt template before sending to model

**Amazon Bedrock Guardrails (4 filter categories, all set to HIGH):**
- Content Filters: Hate, Sexual, Violence, Insults, Misconduct, Prompt Attack — all at HIGH strength
- Denied Topics: 28 custom topics (politics, competitors, brand safety, religion, security, prompt injection, etc.)
- Word Filters: 1,494 blocked words across multiple languages (competitor names, extremist terms, profanity, etc.)
- PII Filters: **All PII categories set to BLOCK** (General, IT, Finance, US/Canada/UK-specific)

**Output control:**
- LLM response simplified to **YES / NO / BLOCKED** only — no raw model text was ever surfaced to customers
- Any unexpected output defaults to NO
- All prompts and responses logged to DynamoDB (KMS-encrypted, PITR enabled) for audit

**Andon Cord (mandatory):**
- Environment variable (`USE_BEDROCK_API`) on Lambda — set to `false` to instantly disable all AI functionality
- Full SOP documented with demo recording (this was explicitly required during ASR)

## 4. Pre-defined vs. Free-form

This is where the biggest trade-off lies.

**Our approach (MARS):** We accepted **free-form text input** (up to 100 characters) but constrained the **output** to only three possible responses (YES/NO/BLOCKED). The raw LLM response was never shown to customers. Think of it as: free input → AI classification → pre-defined output.

**The consequence:** Because we accepted free-form input, the data was classified as **Undefined Customer Data (UCD) = Critical**, which triggered a **Red ASR classification**. This meant: mandatory security reviewer assignment, manual prompt testing, ~90 hours of DT security work, and a 4-6 week timeline.

**The alternative (available now):** If you restrict input to **pre-defined prompts only** (an allow-list approach), the data is no longer classified as UCD. This means your ASR classification can stay at **Orange**, which allows **self-certification** — no security reviewer needed, automated FAST testing is sufficient, and the process is significantly faster.

Your DT team's initial feedback that you "may need to use pre-defined messages/prompts rather than fully open user input" is actually a **strategically sound recommendation** — not just from a technical safety perspective, but because it fundamentally changes your security classification and approval timeline.

**My recommendation:** Consider a phased approach:
- **V1:** Pre-defined prompts only → Orange ASR → self-certify → faster launch
- **V2:** Add free-form input if needed → Red ASR → full security review

## 5. AI Model & Infrastructure

| Component | What we used |
|-----------|-------------|
| Foundation Model | **Anthropic Claude 3 Sonnet** on Amazon Bedrock |
| Embedding | Cohere Embed English v3 (for Knowledge Base) |
| RAG | Amazon Bedrock Knowledge Bases + Amazon OpenSearch Serverless |
| Guardrails | Amazon Bedrock Guardrails |
| Compute | AWS Lambda |
| API | API Gateway (REST) |
| Database | DynamoDB (logging) |
| Storage | S3 (knowledge base source + logs) |
| Security | AWS WAF, CloudWatch, CloudTrail |
| Region | us-west-2 |
| IaC | CDK Pipeline |

Key technical decisions:
- **Temperature: 0.0** — fully deterministic responses (no randomness)
- **RAG over fine-tuning** — fine-tuning with a small dataset increases hallucination risk
- **Single-turn only** — no multi-turn conversation, no session persistence (simplifies the "Siloed Sessions" ASR requirement)
- Everything hosted within Amazon infrastructure (Bedrock requirement — no external AI APIs)

## 6. Documentation

Here are the key internal resources to get you started:

| Resource | Link |
|----------|------|
| ASR Profiles & Classification Rules | https://w.amazon.com/bin/view/Infosec/Proactive_Security/Dev/SecurityReviewTooling/ASR/Profiles/ |
| FAST Framework (v2) | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/ |
| FAST Integration SOP (BIL TEX) | https://quip-amazon.com/FhvFAKBxf6Tu/SOP-FAST-Integration |
| Generative AI for Campaign (guide I wrote) | https://quip-amazon.com/aa1OAHdOJgua/Generative-AI-for-Campaign |
| BIL Approved AI Tools | https://w.amazon.com/bin/view/BIL-E/NA/BIL-AI-Tools |
| GenAI Security Standard (policy) | https://policy.a2z.com/docs/613805/publication |
| Andon Cord Guidance | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Guidance/Andon_Cords/ |

I can also share the MARS-specific Quip documents (AI tool overview, ASR kickoff, incident response plan, guardrails spreadsheet) if helpful — just let me know.

## 7. Lessons Learned

1. **Client GenAI approval takes much longer than you'd expect.** Ours took 3+ months (vs. weeks for UX/UI). Start this track in parallel from day one.
2. **Free-form input = Red ASR.** Understand the UCD → Critical → Red chain before committing to your input design. This single decision drives your entire security timeline.
3. **ASR is 4-6 weeks with ~90 hours of DT work.** DACE data classification should be completed early — it's a prerequisite for the GenAI ASR tasks.
4. **Andon Cord is mandatory.** You'll need an instant kill-switch for the AI functionality, with a documented SOP and demo recording.
5. **Competitor name blocking is imperfect.** We blocked 1,494 words including 50+ competitor names, but misspellings slip through. Plan for this.
6. **FAST v2 onboarding can have technical issues.** We hit `ResponseMissingError` and had to navigate a v1→v2 migration mid-project. Budget time for this.
7. **Log everything.** All prompts and responses need to be stored separately from standard security logs, with encryption and point-in-time recovery.

## One more thing — 2026 update

Since our MARS campaign in 2024, the approval landscape has evolved. The NA TEX team has been working on AI on CLP through a newer, streamlined path (FAST onboarding + Orange ASR self-certification). I'd strongly recommend reaching out to **Alec Kunkle (aleckunk@)** on the NA TEX team — he's been leading the most recent AI on CLP work and can walk you through the latest process and tooling.

---

Happy to jump on a call if any of this needs more detail. We're in AEDT (Sydney) so mornings our time / evenings your time tends to work well.

Best,
Shugo
