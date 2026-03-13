# Draft Reply to Julia Sampaio — Final

**Subject:** RE: UK Arla Campaign -- AI on CLP: Learning from your MARS experience

---

Hi Julia,

Thanks for reaching out -- great to hear about the Arla "Morning Wins Worth Celebrating" concept! Happy to share what we learned from the MARS "For You Who Did That Thing You Did" (FYWDTTYD) campaign in AU. I'll walk through your questions from a technical perspective below. Luke can add context on the business/ops side.

---

## 1. AI Approval Process

There are three parallel approval tracks: Amazon internal (Legal/PR), ASR (security review), and client-side approval. Since 2026, GenAI campaigns that don't handle user training data are classified as "Orange" under ASR, which allows self-certification -- a significantly streamlined process compared to what we went through with MARS.

We ran **three parallel approval tracks** simultaneously:

- **Internal Amazon approvals** (Legal/PR/Business) -- submitted via `approvals.amazon.com`. We connected with local Legal and PR early in pre-sales.
- **Amazon Security Review (ASR)** -- our application was classified as **Red** (the highest security tier), which required a dedicated security reviewer from the GenAI AppSec team. On top of the standard ASR tasks, we had **12 additional GenAI-specific tasks** including: Review Training Data, Review AI Model, Prompt Data Sanitization, Andon Cord review, FAST (Framework for AI Security Testing) onboarding, AI Response Logging, Guardrails validation, Siloed Sessions validation, and Bug Bounty onboarding.
- **Client external approval** -- Mars Inc.'s global legal/security team needed to separately approve the use of GenAI. This was a distinct track from UX/UI approval and ended up being the longest lead item.

**Critical point on ASR classification:** The reason we were classified as Red was that we accepted **free-form text input** from customers. Under Amazon's data classification policy, free-form input = Undefined Customer Data (UCD) = Critical data = Red ASR. This is probably the single most important thing to understand early in your design phase (more on this in Q4).

**2026 update:** The ASR landscape has improved significantly since 2024. Applications that don't handle user data or training can now be classified as **Orange** and self-certified, removing the need for a dedicated InfoSec reviewer. Whether you qualify for Orange depends heavily on your input design -- see Q4.

---

## 2. Approval Timeline

End-to-end, ours took over 3 months -- the bottleneck was client GenAI approval (3+ months), not the Amazon-side reviews (Legal/PR ~3 weeks, ASR 4-6 weeks). If your design qualifies for Orange ASR in 2026, the ASR portion can be reduced to days.

To give you a concrete reference point: our MARS project ASR application was created on March 11 2024, the GenAI AppSec team got involved around July 19 (confirmed by Slack channel creation), and we released on August 29. The actual ASR review period was roughly 6 weeks -- honestly, this was tight. I'd recommend allowing 2-3 months for the ASR review process if possible.

| Track | Duration | Notes |
|-------|----------|-------|
| Internal Legal/PR | ~3 weeks | Relatively straightforward once documentation was prepared |
| ASR (Security Review) | 4-6 weeks | Self-service 2-3 weeks, then InfoSec review 2-3 weeks. DT effort: ~90 hours (45h standard + 45h GenAI-specific) |
| Client GenAI approval | **3+ months** | Significantly longer than expected. Mars's global team required detailed AI documentation before sign-off |

The ASR review involved multiple stages: self-service checklist, DACE data classification, GenAI-Sec team consultation, security engineer assignment, and then the actual review (architecture, threat model, code review, pen test). Total DT scoping for the entire project was 405 hours.

**My advice:** Start the client GenAI approval track as early as possible -- it's separate from UX/UI approval and can easily become the critical path. Based on our experience, I'd recommend allocating 2-3 months specifically for the ASR + client approval workstream.

**2026 update:** If your design qualifies for Orange ASR (pre-defined inputs only), you can self-certify with FAST automated testing. This cuts the ASR portion from 4-6 weeks down to days. The client approval timeline, however, will still depend on Arla's internal processes.

---

## 3. Input Handling & Guardrails

We did not use real-time human moderation. Instead, we built a six-layer automated guardrail system (frontend validation through Bedrock Guardrails to output constraints), combined with exhaustive pre-launch testing (FAST + pen testing + stakeholder UAT) and an Andon Cord kill-switch for immediate shutdown if needed.

We implemented a **multi-layered defense architecture** with six distinct layers. I reviewed our codebase to give you specifics:

**Layer 1 -- Frontend:**
- 100-character input limit (hard-enforced in UI and validated server-side)
- Mandatory T&C checkbox with explicit PII disclaimer: *"You agree that you will not enter sensitive personal data of another individual"*
- Transparency notice: *"Prompts and results may be reviewed through automated and manual methods for abuse prevention"*
- AI purpose disclaimer: *"AI powered for entertainment purposes"*

**Layer 2 -- Network:**
- AWS WAF with 6 rules: Common Rule Set, Known Bad Inputs, IP Reputation List, Anonymous IP List, Bot Control, and IP-based rate limiting (2,000 requests per 5 minutes)
- WAF logs encrypted with KMS, retained for 5 years

**Layer 3 -- API Gateway:**
- Lambda Authorizer (origin whitelist + token verification)
- Request Validator with strict schema (`additionalProperties: false` in beta/prod)
- Throttling: 30 req/s, burst 20

**Layer 4 -- Application-level input validation:**
- Five-stage sanitization pipeline: 100-char truncation, lowercase, multi-byte punctuation normalization, emoji stripping, URI encoding, CRLF removal
- User input wrapped in a structured XML-style prompt template before being sent to the model (this prevents prompt injection by isolating user text from instructions)

**Layer 5 -- Amazon Bedrock Guardrails (all set to maximum strength):**
- Content Filters: all 6 categories at HIGH (Hate, Sexual, Violence, Insults, Misconduct, Prompt Attack)
- Denied Topics: 28 topics (5 built-in + 23 custom including Alcohol, Brand safety, Celebrities, Competitors, Copyright, Politics, Religion, Security, etc.)
- Word Filters: 1,494 blocked words/phrases across multiple languages (competitor brand names, extremist terms, profanity, etc. -- auto-generated from a managed Excel spreadsheet)
- PII Filters: **all PII categories set to BLOCK** (General, IT, Finance, US/Canada/UK-specific) plus custom regex patterns

**Layer 6 -- Output control:**
- LLM response constrained to exactly **YES / NO / BLOCKED** -- no raw model text was ever surfaced to customers. Any unexpected output automatically defaults to NO.
- All requests and responses logged to a dedicated DynamoDB table (KMS-encrypted, point-in-time recovery enabled) capturing: input, prompt, answer, LLM output text, citations, guardrail actions, and timestamps

**Andon Cord (mandatory for ASR):**
- Lambda environment variable that instantly disables all AI functionality (returns 503). Documented SOP and demo recording were explicitly required during the security review.

**Important note on moderation approach:**
We did **not** implement real-time human moderation of inputs/outputs. Instead, we relied on three pillars:

1. **Robust automated guardrails** (the six-layer architecture above) -- these handle content filtering and safety enforcement in real time without human intervention
2. **Exhaustive pre-launch testing** -- FAST automated prompt security testing (Hydra-based in beta), penetration testing by the GenAI AppSec team as part of ASR, and hands-on UAT by all stakeholders (client, Legal, PR, DT) to validate guardrail effectiveness against real-world prompts
3. **Incident response planning** -- we created a formal Incident Response Plan (ISR) documenting escalation paths, responsible parties, and procedures, paired with the Andon Cord kill-switch for immediate AI shutdown if needed

**Post-launch monitoring:**
- **CloudWatch alarms** -- four CloudTrail-based alarms (console sign-in failures, authorization failures, CloudTrail config changes, IAM policy changes) with SNS email notifications to the team distribution list. These provide automated alerting on infrastructure/security anomalies.
- **CloudWatch Dashboard** -- WAF log monitoring dashboard embedded in Wiki for visibility across the team
- **DynamoDB full logging** -- every request/response pair stored in the `BedrockResponseTable` (KMS-encrypted, PITR-enabled), enabling post-hoc analysis of all AI interactions
- Weekly batch review of collected inputs/outputs
- Bi-weekly manual data review by the BIL team

---

## 4. Pre-defined vs. Free-form Input

Yes, we discussed this. We chose free-form input with multi-layer guardrails because pre-defined prompts alone couldn't meet the client's creative requirements -- and if we'd gone with pre-defined only, there would have been no real need for an LLM. The trade-off was accepting Red ASR classification. For 2026, pre-defined prompts only = Orange ASR = self-certification, which is a strategically strong path.

This is where the biggest design trade-off lies, and it directly impacts your security classification and approval timeline.

We did consider restricting inputs to pre-defined prompts as a Plan B. However, we concluded that pre-defined prompts would only **partially satisfy the client's creative requirements** -- the experience would have been significantly weaker as a creative solution. The Mars campaign needed customers to describe their own personal achievements in free text, which is inherently open-ended. Moreover, if we had gone with pre-defined prompts only, **there would have been no real need to use an LLM at all** -- a simple lookup table or rule-based system could have handled it. The whole point of bringing in an LLM was its ability to interpret and classify free-form natural language input.

**Our approach (MARS):** We accepted free-form text input (up to 100 characters) but constrained the output to exactly three possible responses (YES / NO / BLOCKED). The raw LLM response was never shown to customers. Think of it as: free input -> AI classification -> pre-defined output.

**The consequence:** Because we accepted free-form input, the data was classified as **Undefined Customer Data (UCD) = Critical**, which triggered a **Red ASR classification**. This meant: mandatory security reviewer, manual prompt testing, ~90 hours of DT security work, 4-6 week ASR timeline, and the full multi-layer guardrails setup I described in Q3. Importantly, disclaimers or UI warnings do NOT lower the data classification -- it's the presence of the free-form input field itself that determines UCD.

**The alternative (recommended for 2026):** If you restrict input to **pre-defined prompts only** (allow-list approach), the data is not classified as UCD. This means your ASR classification stays at **Orange**, which allows **self-certification** -- no dedicated security reviewer, FAST automated testing is sufficient, and the timeline is dramatically shorter. And it's worth noting: if you go this route, you may not even need an LLM -- depending on the complexity of your jingle generation, a template-based approach could suffice. But if you do want creative variation even within pre-defined categories, an LLM can still add value.

**Your DT team's instinct is correct.** Their initial feedback that you "may need to use pre-defined messages/prompts rather than fully open user input" is actually a strategically sound recommendation -- not just for technical safety, but because it fundamentally changes your security classification and approval path.

**My recommendation -- phased approach:**
- **V1:** Pre-defined prompts only -> Orange ASR -> self-certify -> faster launch
- **V2 (if needed):** Add free-form input -> Red ASR -> full security review

This is exactly the pattern that the NA TEX team has been following with recent campaigns.

---

## 5. AI Model & Infrastructure

We used Anthropic Claude 3 Sonnet on Amazon Bedrock with a RAG setup (Knowledge Bases + OpenSearch Serverless), temperature set to 0.0 for fully deterministic responses. Everything was hosted within Amazon infrastructure -- external AI APIs are not permitted under Bedrock requirements.

| Component | What we used |
|-----------|-------------|
| Foundation Model | **Anthropic Claude 3 Sonnet** on Amazon Bedrock |
| Embedding | Cohere Embed English v3 (for Knowledge Base indexing) |
| RAG | Amazon Bedrock Knowledge Bases + Amazon OpenSearch Serverless |
| Guardrails | Amazon Bedrock Guardrails (native, CDK-managed) |
| Compute | AWS Lambda |
| API | API Gateway (REST) |
| Database | DynamoDB (prompt/response logging, KMS-encrypted) |
| Storage | S3 (knowledge base data source + CloudTrail logs) |
| Security | AWS WAF, CloudWatch (6 log groups), CloudTrail |
| Region | us-west-2 (Oregon) |
| IaC | CDK Pipeline, 3 environments (dev/beta/prod) |

Key technical decisions:
- **Temperature: 0.0** (fully deterministic, no randomness in responses)
- **RAG over fine-tuning** -- fine-tuning with a small dataset was deemed to increase hallucination risk
- **Single-turn only** -- no multi-turn conversation, no session persistence (simplifies the "Siloed Sessions" ASR requirement)
- **FAST integration** in the beta environment for automated prompt security testing (Hydra-based)
- Everything hosted within Amazon infrastructure (Bedrock requirement -- external AI APIs are not permitted)

For your Arla jingle generation, the model choice would likely be different (you'd need a more capable model for creative text generation rather than classification), but the infrastructure pattern and security architecture would be very similar.

---

## 6. Documentation

Yes -- there are several internal resources I can point you to, plus I can share the MARS-specific Quip documents (AI tool overview, ASR kickoff, incident response plan, guardrails spreadsheet) if helpful.

Here are the key internal resources to get started:

| Resource | Link |
|----------|------|
| ASR Profiles & Classification Rules | https://w.amazon.com/bin/view/Infosec/Proactive_Security/Dev/SecurityReviewTooling/ASR/Profiles/ |
| FAST Framework (v2) | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/ |
| FAST Integration SOP (BIL TEX) | https://quip-amazon.com/FhvFAKBxf6Tu/SOP-FAST-Integration |
| Generative AI for Campaign (guide I wrote) | https://quip-amazon.com/aa1OAHdOJgua/Generative-AI-for-Campaign |
| BIL Approved AI Tools | https://w.amazon.com/bin/view/BIL-E/NA/BIL-AI-Tools |
| GenAI Security Standard (policy) | https://policy.a2z.com/docs/613805/publication |
| Andon Cord Guidance | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Guidance/Andon_Cords/ |

I can also share the MARS-specific Quip documents (AI tool overview, ASR kickoff, incident response plan, guardrails spreadsheet, monitoring runbook) if that would be helpful -- just let me know.

---

## 7. Lessons Learned

Two biggest takeaways: start client GenAI approval from day one (ours took 3+ months and became the critical path), and understand the free-form input = Red ASR chain before committing to your input design -- that single decision shapes your entire security timeline.

1. **Client GenAI approval takes much longer than expected.** Ours took 3+ months (vs. weeks for UX/UI). Start this track in parallel from day one and prepare a detailed AI overview document for the client early.

2. **Free-form input = Red ASR. Full stop.** Understand the UCD -> Critical -> Red chain before committing to your input design. This single decision determines your entire security timeline and DT workload. Disclaimers don't help -- it's the input field itself that triggers UCD classification.

3. **ASR is a significant effort.** 4-6 weeks, ~90 hours of DT work, 12 GenAI-specific tasks. DACE data classification should be completed early as it's a prerequisite.

4. **Andon Cord is mandatory.** You need an instant kill-switch for the AI functionality, with a documented SOP and recorded demo. This was non-negotiable in our ASR.

5. **Word/competitor blocking is imperfect.** Even with 1,494 blocked words including 50+ competitor names, misspellings slip through. Guardrails asset management (denied topics, word lists, PII patterns) requires ongoing maintenance -- we built an automated pipeline from Excel spreadsheets to Bedrock config to manage this.

6. **FAST onboarding can be bumpy.** We encountered a `ResponseMissingError` and had to navigate a v1 to v2 migration mid-project. Budget time for integration issues.

7. **Log everything separately.** All prompts and responses must be stored in a dedicated, encrypted datastore (not just CloudWatch). This is both an ASR requirement and essential for post-launch monitoring.

8. **Design for constraint.** Our strongest safety measure was constraining the output to YES/NO/BLOCKED -- by never surfacing raw LLM text, we eliminated an entire category of risks. Consider what the "minimum viable AI output" is for your jingle feature.

---

## Recommended next steps

Since our MARS campaign in 2024, the process has evolved considerably. For the most up-to-date guidance on the Orange/FAST self-certification path, I'd strongly recommend reaching out to **Alec Kunkle (aleckunk@)** on the NA TEX team -- he has been leading the most recent AI on CLP implementations and can walk you through the current process and tooling.

From our side, happy to:
- Share the MARS Quip documentation package
- Walk through the architecture in more detail on a call
- Review your DT team's proposed architecture from a security/ASR perspective

We're in AEDT (Sydney), so mornings our time / late afternoon your time tends to work well for calls.

Best,
Shugo
