## Q1. AI Approval Process

What was the end-to-end process for getting the AI tool approved for use on CLP? Which teams/stakeholders were involved in the review (e.g., Legal, Trust & Safety, AdTech)?

At a high level, there were three parallel approval tracks:
- Amazon internal approval (Legal/PR/Business) -- Submitted via approvals.amazon.com. We engaged local Legal and PR early during the pre-sales stage.
- Amazon Security Review (ASR) -- Our application was classified as Red, which required review by a dedicated reviewer from the GenAI AppSec team. In addition to the standard ASR tasks, there were 12 GenAI-specific tasks.
- Client external approval -- Mars Inc.'s global Legal and Security teams needed to separately approve the use of GenAI. This was a separate track from the UX/UI approval and ended up being the longest lead-time item.

Note on ASR: If your application is classified as Orange or below, you can complete the review via self-service, which significantly shortens the timeline (no human review by an external reviewer is required). As of 2026, if you are not handling Critical/Restricted data -- i.e., using pre-defined messages/prompts -- there is a possibility of being classified as Orange even when leveraging GenAI.

---

## Q2. Approval Timeline

How long did the approval process take from initial proposal to green light? Were there multiple review stages?

The end-to-end process took a minimum of 3+ months. Internal Legal/PR took approximately 3 weeks, ASR took approximately 6 weeks, but the client GenAI approval was the longest bottleneck at 3+ months.

---

## Q3. Input Handling

How did you manage user-generated input? Did you use any guardrails, content filters, or moderation layers to ensure appropriate responses?

We addressed this across five key areas:
- Multi-layered automated guardrails on user input -- Front-end validation, AWS WAF, API Gateway controls, application-level sanitization, and Amazon Bedrock Guardrails (prompt attack detection, content filters, denied topics, word filters, PII blocking)
- Output constraints -- Responses are constrained to YES/NO/BLOCKED only, ensuring that raw LLM text is never displayed to consumers
- Thorough pre-launch testing -- FAST automated prompt security testing, penetration testing by the GenAI AppSec team, and hands-on UAT by all stakeholders
- Incident response -- A formal response plan + Andon Cord kill switch for immediate AI shutdown (required by ASR)
- Full request/response logging and post-hoc monitoring -- Logs stored in DynamoDB and CloudWatch with periodic checks during the campaign flight (weekly + bi-weekly BIL team review). (We did not employ real-time human moderation due to resource constraints.)

---

## Q4. Pre-defined vs. Free-form

Was there ever a discussion about restricting inputs to pre-defined prompts vs. allowing free text? What were the key considerations that led to your approach?

Yes, we discussed this. Restricting inputs to pre-defined prompts was considered as a Plan B, but preset-only inputs could not deliver the creative ideas required by the client. We developed a prototype, validated feasibility, and chose free text + multi-layered guardrails.
* With presets only, the LLM itself becomes unnecessary.
In our use case, instead of restricting input, we applied strictly pre-defined output constraints -- responses are limited to YES/NO/BLOCKED only.

---

## Q5. AI Model & Infrastructure

At a high level, what AI model/service did you use, and was it hosted within Amazon's infrastructure? Were there specific technical requirements from the approval side?

We used a RAG architecture with Anthropic Claude 3 Sonnet on Amazon Bedrock (Knowledge Bases + OpenSearch Serverless), all within Amazon infrastructure in a fully serverless configuration.

- **Model:** Anthropic Claude 3 Sonnet on Amazon Bedrock
- **Embeddings:** Cohere Embed English v3 (for Knowledge Bases)
- **RAG:** Amazon Bedrock Knowledge Bases + Amazon OpenSearch Serverless
- **FAST integration:** FAST Stack + Hydra Stack deployed in the Beta environment. The Prod environment uses the core Bedrock stack only.
- **Approval-side technical requirements:** Legal: Bedrock usage mandatory, individual approval per campaign/model. Security: ASR compliance (FAST onboarding, logging of all prompts/responses, Andon Cord implementation, etc.)

---

## Q6. Documentation

Is there any internal documentation, wiki, or approval template you went through that you could point us to? It would help us get a head start on our own submission.

Here are the relevant documents:

- ASR: https://w.amazon.com/bin/view/Review_Automation/SecurityReviews/
- SDO Information Security Support Portal: https://support.security.amazon.dev/tags
- Mars-related Quip (development): https://quip-amazon.com/Tnk0OtquZA7d/AU-Mars-FYWDTTYD-

---

## Q7. Lessons Learned

Anything you'd do differently or any pitfalls to watch out for in the approval process?

The two biggest lessons: (1) Start the client GenAI approval in parallel from day one (ours took 3+ months), and (2) Reach out to the GenAI AppSec team as early as possible to kick off the ASR process.

---

## Additional Note: Latest Process Updates

The GenAI application approval process has changed considerably since 2024. You may have already been in touch, but we recommend reaching out to Alec Kunkle (aleckunk@) on the TEX team for the latest guidance on the Orange/FAST self-certification path.
