# Reply to Julia Sampaio — Concise Email Version

**Subject:** RE: UK Arla Campaign -- AI on CLP: Learning from your MARS experience

---

## 1. AI Approval Process

There are three parallel approval tracks:

- **Amazon internal** (Legal/PR) -- submitted via `approvals.amazon.com`
- **Amazon Security Review (ASR)** -- our app was classified as **Red** (highest tier) because we accepted free-form text input. This required a dedicated security reviewer and 12 GenAI-specific tasks
- **Client external** -- Mars's global legal/security team needed to separately approve GenAI use. This ended up being the longest lead item

**Key 2026 update:** GenAI campaigns that don't handle free-form user input are now classified as **Orange** under ASR, which allows self-certification -- a dramatically simpler process. Whether you qualify depends on your input design (see Q4).

---

## 2. Approval Timeline

| Track | Duration | Notes |
|-------|----------|-------|
| Internal Legal/PR | ~3 weeks | Straightforward once docs are prepared |
| ASR (Security Review) | 4-6 weeks | ~90 hours DT effort (standard + GenAI-specific) |
| Client GenAI approval | **3+ months** | Significantly longer than expected -- became our critical path |

For reference, our MARS project timeline: ASR application created March 11 2024, GenAI AppSec team engaged ~July 19, and we released August 29. The actual ASR review period was roughly 6 weeks -- it was tight. I'd recommend allowing 2-3 months for the ASR review process.

**My advice:** Start the client GenAI approval track as early as possible -- it's separate from UX/UI approval and will likely be your bottleneck.

**2026 update:** If your design qualifies for Orange ASR (pre-defined inputs only), the ASR portion drops from weeks to days via FAST self-certification.

---

## 3. Input Handling & Guardrails

We did **not** use real-time human moderation. Instead, we relied on three pillars:

1. **Multi-layer automated guardrails** -- six layers from frontend validation through AWS WAF, API Gateway controls, application-level sanitization, Amazon Bedrock Guardrails (content filters, denied topics, word filters, PII blocking), to output constraints (responses locked to YES/NO/BLOCKED only -- no raw LLM text ever surfaced to customers)
2. **Exhaustive pre-launch testing** -- FAST automated prompt security testing, penetration testing by GenAI AppSec, and hands-on UAT by all stakeholders
3. **Incident response** -- formal response plan + **Andon Cord** kill-switch for immediate AI shutdown (mandatory for ASR)

---

## 4. Pre-defined vs. Free-form Input

This is probably the most important design decision for your campaign.

We chose free-form input (up to 100 characters) with multi-layer guardrails because pre-defined prompts alone couldn't meet the client's creative requirements -- and if we'd gone pre-defined only, there would have been no real need for an LLM. The trade-off: **free-form input = Undefined Customer Data (UCD) = Red ASR classification**, with all the additional security overhead that entails. Disclaimers or UI warnings do NOT change this classification -- it's the input field itself.

**For 2026, my recommendation -- phased approach:**
- **V1:** Pre-defined prompts only -> Orange ASR -> self-certify -> faster launch
- **V2 (if needed):** Add free-form input -> Red ASR -> full security review

Your DT team's instinct that you "may need to use pre-defined messages/prompts" is strategically sound -- it fundamentally changes your security classification and approval path.

---

## 5. AI Model & Infrastructure

We used **Anthropic Claude 3 Sonnet** on Amazon Bedrock with a RAG setup (Knowledge Bases + OpenSearch Serverless). Key technical decisions: temperature set to **0.0** (fully deterministic), single-turn only (no conversation persistence), and everything hosted within Amazon infrastructure (external AI APIs are not permitted under Bedrock requirements). Infrastructure: Lambda, API Gateway, DynamoDB for logging, CDK Pipeline across 3 environments.

For your jingle generation, the model choice would likely differ (creative generation vs. our classification use case), but the infrastructure pattern and security architecture would be very similar.

---

## 6. Documentation

Key internal resources:

| Resource | Link |
|----------|------|
| ASR Profiles & Classification Rules | https://w.amazon.com/bin/view/Infosec/Proactive_Security/Dev/SecurityReviewTooling/ASR/Profiles/ |
| FAST Framework (v2) | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/ |
| FAST Integration SOP (BIL TEX) | https://quip-amazon.com/FhvFAKBxf6Tu/SOP-FAST-Integration |
| Generative AI for Campaign (guide I wrote) | https://quip-amazon.com/aa1OAHdOJgua/Generative-AI-for-Campaign |
| BIL Approved AI Tools | https://w.amazon.com/bin/view/BIL-E/NA/BIL-AI-Tools |
| GenAI Security Standard (policy) | https://policy.a2z.com/docs/613805/publication |
| Andon Cord Guidance | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Guidance/Andon_Cords/ |

---

## 7. Lessons Learned

1. **Start client GenAI approval from day one.** Ours took 3+ months and became the critical path. Prepare a detailed AI overview document for the client early.
2. **Free-form input = Red ASR. Full stop.** Understand this chain before committing to your input design -- it determines your entire security timeline.
3. **Andon Cord is mandatory.** You need an instant kill-switch with documented SOP and recorded demo. Non-negotiable in ASR.
4. **Design for constraint.** Our strongest safety measure was never surfacing raw LLM text. Consider what the "minimum viable AI output" is for your jingle feature.

