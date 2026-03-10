# FAST (Framework for AI Security Testing) - Deep Research Findings

**Date:** 2026-03-02
**Context:** BIL TEX WBR reference to "BIL TEX onboarded to FAST for AI Pet Recommendations"
**Researcher:** Claude (on behalf of BIL TEX Design Technologist)

---

## Executive Summary

FAST does NOT provide self-review or eliminate manual human review for RED-classified GenAI applications. FAST is an **automated security prompt testing framework** that integrates into CI/CD pipelines. It is one of many ASR tasks -- not a replacement for the security review process. GenAI applications still receive RED classification in ASR and still require Security Engineer review. The timeline for GenAI ASR reviews is officially 4-6 weeks per the AppSec AI team's documentation.

---

## 1. Current State of FAST v2

### What FAST v2 Is
- A collection of services providing curated security prompts for automated testing
- Tests for: prompt injection, data exfiltration, PII leakage, remote code execution
- Integrates into CI/CD pipelines via integration tests (Hydra)
- Uses CloudAuth for API authentication
- Supports Java and Python thick clients (both Brazil and Peru build systems)
- Three evaluators as of Oct 2025: Output Validity (OV), PII, and Deflection

### FAST v2 Architecture
- Provides prompts via API -> your app processes them -> FAST scores responses
- Pass/fail based on configurable thresholds (recommended >= 60% across all evaluators)
- Results generate a "report card" for compliance tracking

### Key Limitation: Modality
- **FAST is text-to-text focused.** The framework sends text prompts and evaluates text responses.
- No evidence found of native support for image, video, or multimodal inputs/outputs
- The FAQ and wiki make no mention of image-to-image, image-to-video, or video modality support
- This aligns with the user's 2025 experience getting an exception for Cat Decoder (image-to-video)

### Source URLs
- Main wiki: https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/
- FAST v2 wiki: https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/v2/
- FAST v2 FAQ: https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/v2/FAQ
- FAST Evaluators: https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/FASTEvaluators
- Broadcast video: https://broadcast.amazon.com/videos/1500594

---

## 2. FAST and ASR Classification: Does FAST Enable Self-Review?

### Critical Finding: NO, FAST does NOT enable self-review for GenAI apps

The ASR classification system works as follows:
- **Green, Yellow, Orange** reviews can be **self-certified** by the application owner
- **Red** reviews **require a Security Engineer or Security Certifier** for manual human review
- **GenAI applications are classified as RED** when they answer "yes" to "Does the application use GenAI technology?" in the Profile Task

### What FAST Does Within ASR
FAST is listed as **one of many ASR tasks** for GenAI applications. Specifically:
- "FAST Onboarding for Automated Testing" is a task in the ASR review checklist
- It sits alongside other tasks like: Manual Prompt Testing, Threat Model Review, Code Review, etc.
- FAST handles **automated** prompt testing; Manual Prompt Testing is a **separate** additional requirement

### The AppSec AI Review Process page explicitly states:
> "GenAI application necessitates 21 tasks for a security review, with additional dependencies on Prompt Testing Completion. Due to the added tasks, research, deep dives, and the requirement for prompt testing completion, the time to complete a GenAI security review ranges from **4 weeks to 6 weeks**, depending on the application's size and complexity."

### FAST Does Help But Does NOT Eliminate Manual Review
From the ASR guide for GenAI apps (PaymentRisk/Engineering/GenAI-Aurora/ASR/):
> "FAST Reduces Burden: Onboard to FAST for automated testing and easier recertification"
> "Red Apps Need More Time: Manual prompt testing, security engineer review, and findings remediation extend timelines"

### Source URLs
- Review Process: https://w.amazon.com/bin/view/InfoSec/Application_Security/AppSTAR/Appsec_AI/Review_Process/
- ASR for GenAI: https://w.amazon.com/bin/view/PaymentRisk/Engineering/GenAI-Aurora/ASR/
- AppSec AI FAQ: https://w.amazon.com/bin/view/InfoSec/Application_Security/AppSTAR/Appsec_AI/FAQ/

---

## 3. What "BIL TEX onboarded to FAST" Likely Means

Based on the research, "BIL TEX onboarded to FAST for AI Pet Recommendations" most likely means:

1. **FAST integration tests were added to the deployment pipeline** for the AI Pet Recommendations campaign
2. This involves: CloudAuth onboarding, writing FAST integration tests, adding pipeline approval steps
3. Estimated onboarding effort: 1 hour to 3 days (per FAST v2 documentation)

### What It Does NOT Mean:
- It does NOT mean the ASR review was self-certified
- It does NOT mean the manual human review was eliminated
- It does NOT mean a Security Engineer was not required
- It does NOT mean the 4-6 week ASR timeline was avoided

### What It Does Achieve:
- Automated, repeatable security prompt testing in the pipeline
- Catches regressions automatically on every code change
- Satisfies the "FAST Onboarding for Automated Testing" ASR task
- Makes **recertification** easier (important for campaigns that evolve)
- May help demonstrate security posture to expedite the manual review portions

---

## 4. Current ASR Timeline for GenAI Applications

### Official Timeline (from AppSec AI Review Process wiki, updated ~3 months ago):
- **4-6 weeks** for a complete GenAI security review
- This is for applications classified as RED
- Complex applications (multi-modal, 3P models, agents) may take longer

### Timeline Breakdown by Task:
| Task | Small App | Medium App | Large App | Owner |
|------|-----------|------------|-----------|-------|
| Profile Task | 2-4 Hours | 2-4 Hours | 2-4 Hours | Product Team |
| Privacy Compliance | 1 Hour | 1 Hour | 1 Hour | Product Team |
| Threat Model | 1 Week | 1 Week | Up to 2 Weeks | Product Team |
| Review Threat Model | 1 Week | 1.5 Weeks | Up to 2 Weeks | Security Engineer |
| FAST Onboarding | Listed as task | Listed as task | Listed as task | Product Team |
| Manual Prompt Testing | Required | Required | Required | Security + Product |
| Code Review | Required | Required | Required | Security Engineer |

### Key Insight:
The timeline has improved from the user's historical experience (4-12 weeks) to an official 4-6 weeks, but this is due to process improvements, not FAST enabling self-review.

### Parallel Track Optimization:
> "To expedite the review process, we conduct multiple tasks simultaneously, including Privacy Compliance Review, Incident Response Plan, Onboarding to Prompt Testing, and Pentest Assessment"

---

## 5. RED Classification / Manual Review Status

### No Changes Found to RED Classification for GenAI Apps
- GenAI apps continue to be classified as RED
- RED continues to require Security Engineer or Security Certifier review
- No evidence of any policy change allowing GenAI apps to be classified as Orange
- Misclassifying a GenAI app triggers a Shepherd risk and forces recertification

### FAST's Role in Reducing Review Burden
FAST helps in specific ways:
1. **Satisfies one ASR task** ("FAST Onboarding for Automated Testing")
2. **Ongoing pipeline protection** - catches regressions automatically
3. **Easier recertification** - automated evidence of security testing
4. **Security posture evidence** - report cards show test pass rates

But FAST does NOT:
1. Change the RED classification
2. Eliminate the need for Security Engineer review
3. Remove the Manual Prompt Testing requirement
4. Enable self-certification

---

## 6. Comparison to Historical 4-12 Week Timeline

### The user's historical experience:
- Mars FYWDTTYD (2024): Onboarded to FAST v1, experienced long review cycle
- Mars Cat Decoder (2025): Got FAST v2 exception (image-to-video not supported)

### Current state (2026):
- Official timeline: 4-6 weeks (narrower range than 4-12 weeks)
- FAST v2 has matured significantly (thick clients, better docs, FAQ, office hours)
- New evaluator system (OV, PII, Deflection) with configurable thresholds
- Better parallel task execution to compress timelines
- ASR automation tools being developed (e.g., CampASRAutomation GenAI-powered review)

### Key improvements:
1. **Process maturation** - Better documentation, templates, parallel execution
2. **FAST pipeline integration** - Automated testing reduces manual testing burden
3. **Community support** - #genai-sec-fast-interest Slack channel, office hours
4. **Better tooling** - Thick clients, detailed logging, troubleshooting guides

### What has NOT changed:
1. RED classification for GenAI apps
2. Requirement for Security Engineer review
3. Manual Prompt Testing requirement (separate from FAST)
4. Text-to-text focus of FAST (no multimodal support found)

---

## 7. Recommendations for the User

1. **Clarify the WBR claim:** "BIL TEX onboarded to FAST" means pipeline integration was completed, not that the review process was shortened or self-service
2. **For future campaigns:** Start ASR process during design phase, not at code completion
3. **For multimodal campaigns:** FAST still appears text-focused; image/video campaigns may still need exceptions or alternative testing approaches
4. **Timeline planning:** Plan for 4-6 weeks minimum for GenAI ASR review
5. **Ask the team:** The specific details of what happened with "AI Pet Recommendations" ASR review should be clarified with the BIL TEX team member who completed it

---

## Key Source References

| Source | URL | Last Updated |
|--------|-----|-------------|
| FAST v2 Wiki | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/v2/ | ~3 months ago |
| FAST FAQ | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/Framework/v2/FAQ | ~1 month ago |
| FAST Evaluators | https://w.amazon.com/bin/view/Security/AI-Security/GenAI-Sec/Toolkit/Testing/FASTEvaluators | ~3 months ago |
| AppSec AI Team | https://w.amazon.com/bin/view/InfoSec/Application_Security/AppSTAR/Appsec_AI/ | ~20 days ago |
| Review Process | https://w.amazon.com/bin/view/InfoSec/Application_Security/AppSTAR/Appsec_AI/Review_Process/ | ~3 months ago |
| ASR for GenAI Guide | https://w.amazon.com/bin/view/PaymentRisk/Engineering/GenAI-Aurora/ASR/ | ~1 month ago |
| BuilderHub Golden Path | https://docs.hub.amazon.dev/docs/golden-path/llm-integrated-applications/recommendation/design/7-deployment/security-testing/ | Recent |
| BSC-AI-S2 | https://w.amazon.com/bin/view/InfoSec/Application_Security/AppSTAR/MCCF_AppSec/Guides/BSCs/BSC-AI-S2-Implement-Test-Mechanisms-to-Ensure-Model-Output-Behavior/ | ~3 months ago |
| FAST Broadcast | https://broadcast.amazon.com/videos/1500594 | 2025 |
| Slack Channel | #genai-sec-fast-interest | Active |
| FAST Tickets | https://t.corp.amazon.com/create/templates/436d09c0-a8ed-4ea7-8aa1-6a2eb81cff7c | -- |
| FAST Office Hours | https://office-hour-scheduler.tools.aws.dev/schedule/9d8c5bb8-abdb-4440-ba81-9672e5604f54 | -- |
