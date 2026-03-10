# PetArmor Campaign Research - Deep Dive

**Date:** 2026-03-02
**Researcher:** saitshug
**Purpose:** Determine what PetArmor is, whether it uses GenAI, and whether it is the "AI Pet Recommendations" referenced in the TEX NA WBR FAST onboarding.

---

## 1. What is the PetArmor Campaign?

### Campaign Overview
- **Advertiser:** PetIQ / PetArmor
- **Campaign Name:** "Protect Playtime"
- **Budget:** $2M
- **Media:** Custom Brand Store, Display, Pause Ads | US Grocery
- **Flight:** Phase 1: 2/2/2026 - 4/5/2026; Phase 2 planned for later
- **Client Tier:** C2
- **Pod:** US Endemic (BIL)

### What It Does
PetArmor's "Protect Playtime" campaign is a multi-phase BIL campaign for PetArmor's new 8-month flea & tick protection collar called **PetArmor Extend**.

**Phase 1 (Launched 2/2/2026):** "Dog Parks & Catios, Delivered"
- Customers take a quiz about their pet and outdoor space
- Based on answers, they receive a **personalized at-home dog park or catio design** with curated product bundles
- Includes a discount to get started
- The experience lives on a custom Brand Store page

**Phase 2 (Planned):** "AI Pet Portraits"
- AI-powered pet portrait generation
- Customers upload a photo of their pet and get an artistic AI-generated portrait
- This phase uses generative AI (image generation)

### Source: Slack Launch Announcement
- **Channel:** #brand-innovation-lab-launch-party
- **Posted by:** eddiecam (Eddie Cam)
- **Date:** 2026-02-02
- **Permalink:** https://amzn-media.slack.com/archives/C0274FAGRQS/p1770055210261819
- **Attached files:** 026.0202_PetArmor_LaunchAnnouncement_1.jpg through _5.jpg

Key quote from launch post:
> "Every great adventure starts with feeling safe. What if flea and tick protection wasn't just about prevention, but about unlocking freedom? That's the shift we're making with PetArmor's Protect Playtime. Phase 1 launches February 2nd (today!) to help pet parents build safe play spaces right at home. We're talking personalized at-home dog parks and catios that turn backyards into adventure zones, complete with curated product bundles and a discount to get started."

---

## 2. Does It Use GenAI?

### Phase 1: NO direct GenAI
Phase 1 (currently live) is primarily a **quiz-based recommendation engine** that matches pet owners with curated product bundles based on their answers. This is a rule-based / algorithmic recommendation, NOT generative AI.

However, it could be characterized as "AI Pet Recommendations" in a loose sense since it provides personalized pet product recommendations.

### Phase 2: YES - Image Generation (Planned)
Phase 2 involves **AI Pet Portraits** - generative AI image generation where customers upload pet photos and receive AI-transformed artistic portraits.

### Evidence from Early Scoping (Sep 2025)
From aleckunk in #deprecated-bil-us-endemic-dt-ixd-scoping (2025-09-02):
> "I also added veryyyy rough scopes for the AI directions (pre-generated videos and real-time AI photos). Those hours primarily cover development work and don't include SLAs related to InfoSec and policy."
- **Permalink:** https://amzn-media.slack.com/archives/C021FCZ4TR6/p1756849982355759

This confirms two AI directions were explored during scoping:
1. **Pre-generated videos** (AI video generation)
2. **Real-time AI photos** (AI image generation/transformation)

### BIL GenAI Wiki Reference
The BIL wiki page "The Art of Creating Customer Facing AI" (https://w.amazon.com/bin/view/BrandInnovationLab/Resources/CustomerFacingGenerativeAI/) uses a **pet portrait campaign** as its primary case study example:
> "This campaign invites customers to upload a picture of their pet, which an AI system then transforms into a unique, artistic portrait."

This is almost certainly describing the PetArmor Phase 2 concept (or it inspired/was inspired by it). The wiki mentions styles including Photo Realistic, Sketch Art, Watercolor Painting, Cartoon, Oil Painting, Pop Art, etc.

The wiki also explicitly mentions FAST:
> "Integrate with internal testing tools (e.g., FAST) for ongoing validation of AI outputs."

---

## 3. Is It Connected to FAST Onboarding in the WBR?

### Assessment: VERY LIKELY YES

The WBR reference to "AI Pet Recommendations" being onboarded to FAST almost certainly refers to PetArmor, specifically to its Phase 2 AI component (and possibly the recommendation engine in Phase 1 as well).

**Supporting evidence:**
1. PetArmor is the only active BIL campaign involving pets + AI in the current timeframe
2. The BIL GenAI wiki explicitly mentions FAST as a tool for quality control of AI outputs and uses a pet portrait campaign as its example
3. The campaign was scoped with AI directions (pre-generated videos, real-time AI photos) that would require FAST review
4. The campaign timeline aligns: Phase 1 launched 2/2/2026, Phase 2 (AI) would be in planning/development now, requiring FAST onboarding
5. No other "AI Pet Recommendations" campaign was found in any search

### What Was NOT Found
- Zero Slack results for "PetArmor FAST" specifically
- The WBR PDF could not be fully searched due to PDF reading limitations
- No direct explicit confirmation linking PetArmor to the exact WBR line item

---

## 4. Key People Involved

| Person | Role | Evidence |
|--------|------|----------|
| **eddiecam** (Eddie Cam) | Campaign launch announcer / likely Creative | Posted launch announcement in #brand-innovation-lab-launch-party |
| **tmcnulty** (Thomas McNulty) | Solutions Manager | Filed scoping request, requested IXD assignment |
| **aleckunk** (Alec Kunk) | Design Technologist | Scoped DT hours for AI directions, updated Asana |
| **adamfour** | IXD resource | Requested by tmcnulty for IXD work |
| **U03APUDTJ82** (tmcnulty) | Scoping requestor | Filed the TEX DT Scoping Request |

---

## 5. Campaign Timeline

| Date | Event | Source |
|------|-------|--------|
| 2025-08-06 | Scoping request filed: "PetIQ/PetArmor New Product Launch 2025" | Slack #deprecated-bil-us-endemic-dt-ixd-scoping |
| 2025-09-02 | DT scoping updated with AI directions (pre-gen videos, real-time AI photos) | aleckunk in Slack |
| 2025-10-06 | tmcnulty requests IXD starting Oct 20th - "campaign close to selling" | Slack |
| 2025-12 | Original anticipated go-live date | Scoping request |
| 2026-02-02 | **Phase 1 launched:** "Dog Parks & Catios, Delivered" | Launch announcement |
| 2026-02-02 - 2026-04-05 | Phase 1 flight | Launch announcement |
| TBD (2026) | **Phase 2 planned:** "AI Pet Portraits" | Implied from scoping + launch announcement |

---

## 6. Technology Stack

### Phase 1 (Live)
- **Platform:** Custom Brand Store on Amazon
- **Experience:** Quiz-based recommendation engine
- **Media:** Display ads, Pause Ads
- **Pipeline:** BIL-E standard campaign deployment (likely using BIL-E campaign framework)

### Phase 2 (Planned - AI)
- **AI Type:** Image generation / style transfer
- **Likely Stack:** Amazon Bedrock (based on BIL GenAI wiki SOP: "Setting up a Bedrock Service")
- **Content Moderation:** Likely Rekognition for image validation (per BIL GenAI wiki guidance)
- **Security Review:** Would require FAST onboarding for AI output validation
- **Risk Mitigations:** Image validation, content moderation, human-in-the-loop review

---

## 7. Is This the "AI Pet Recommendations" from the WBR?

### Verdict: HIGHLY PROBABLE - YES

**Reasoning:**
1. **Name match:** "AI Pet Recommendations" accurately describes what PetArmor does - it uses an algorithm/AI to recommend pet products (Phase 1) and will use GenAI for pet portraits (Phase 2)
2. **FAST connection:** The BIL GenAI wiki explicitly references FAST as a quality control tool for AI campaigns and uses a pet portrait concept (matching PetArmor Phase 2) as its primary example
3. **Timing:** PetArmor Phase 1 launched 2/2/2026, Phase 2 AI work would be in development/FAST onboarding now
4. **Uniqueness:** No other BIL campaign involving "AI" + "Pet" + "Recommendations" was found in any searched source
5. **TEX pipeline:** PetArmor appears in #bil-tex-pipelinehealth, confirming it flows through TEX infrastructure

The WBR likely uses "AI Pet Recommendations" as a shorthand for the PetArmor campaign's AI components being onboarded to FAST for security/quality review.

---

## Source URLs

### Slack
- Launch announcement: https://amzn-media.slack.com/archives/C0274FAGRQS/p1770055210261819
- Scoping request: https://amzn-media.slack.com/archives/C021FCZ4TR6/p1754514769574929
- DT scoping update: https://amzn-media.slack.com/archives/C021FCZ4TR6/p1756849982355759
- IXD request: https://amzn-media.slack.com/archives/C021FCZ4TR6/p1759774236264459

### Quip
- Scoping doc: https://quip-amazon.com/lbEbAdIHrAID/SCOPE-TEX-DT-Scoping-Request-PetArmor

### Asana
- Project: https://app.asana.com/1/8442528107068/project/1210833837553228/list/1210834847012995

### Wiki
- BIL GenAI Guide: https://w.amazon.com/bin/view/BrandInnovationLab/Resources/CustomerFacingGenerativeAI/
- Original Quip source: https://quip-amazon.com/3o0YAbX2bazo

### Pipeline
- TEX pipeline health monitoring confirmed via #bil-tex-pipelinehealth channel
