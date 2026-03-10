# Rufus x BIL TEX Research Report

Date: 2026-03-06

## 1. Rufus Overview

- Amazon AI shopping assistant (conversational layer on Amazon search)
- 129M+ MAU (2024)
- S-team target: 208M engagements (2024/12) -> 500M (2025/12) -> 3B (2026/12, +475% YoY)
- Infrastructure: In-house LLM -> Claude 4.0 migration (Project Dune)
- Platforms: mShop (iOS/Android), Desktop, Alexa+

## 2. Locale Support Status

Currently live in **10 marketplaces**:

| Market | Primary | Secondary | Launch |
|---|---|---|---|
| US | en-US | es-US | 2024 Feb (beta) -> mid-2024 GA |
| UK | en-GB | -- | 2024 Q4 |
| DE | de-DE | en-GB | 2024 Q4 |
| FR | fr-FR | -- | 2024 Q4 |
| IT | it-IT | -- | 2024 Q4 |
| ES | es-ES | pt-PT | 2024 Q4 |
| IN | en-IN | -- | 2024 Q4 |
| JP | ja-JP | en-US | 2024 Q4 |
| CA | en-CA | fr-CA | 2024 Q4 |
| PT | (via ES) | pt-PT | 2024 Q4 |

Desktop i18n rolled out mid-2025 to EU-5, IN, JP, CA.

## 3. AU / JP Deployment Status

### Japan -- LIVE
- mShop: 2024 Q4~
- Desktop: mid-2025~
- OPTIMA Rufus Andon operational (JP-specific CTI: C: Alexa Shopping, T: Rufus Intl, I: Japan)
- ja-JP (primary) + en-US (secondary)
- Heartbeat dashboard for customer feedback monitoring
- Rufus Relevance Evaluation SOP exists for ja-JP

### Australia -- NOT LAUNCHED
- Not listed in any Weblab or roadmap
- Heartbeat dashboard exists (possible future signal)
- Nile Andon Cord Service (NAC) supported marketplaces: AU absent
- Rufus smidget experiment weblabs: NA (US, BR, CA, MX), EU, FE (JP only) -- AU absent
- 2026 Rufus priorities: engagement scaling, multi-click actions, Alexa+ integration, existing market feature parity -- NOT new marketplace expansion

## 4. BIL TEX -- Discovery / Prototype

### Discovery #1: Rufus API on Store Landing Pages

- **Quip:** https://quip-amazon.com/BeNqA5zo9z9j
- **Author:** Billy Kwok (billyhkk)
- **Concept:** Embed Rufus chat widget on Brand Store landing pages for brand-contextualized conversational shopping
- **Problem:** BIL clients want AI conversational solutions, but existing tools (Product Selector, Quizzo) lack contextual follow-up. Site-wide Rufus widget is brand-neutral and non-customizable
- **Architecture:** NileCXOrchestratorService (NOS) + NileMainService (NMS/Dune) + NileCachingService (NCS)
- **TPS:** ~1.16 (very low load)
- **Phases:**
  - Phase 1: Done -- Unofficial prototype (UX/feasibility)
  - Phase 2: In Progress -- Official API onboarding with Rufus team
  - Phase 3: Pending -- Pilot integration in BIL campaign
  - Phase 4: Pending -- Code packages and SOP
- **Onboarding tickets:** NMS-13105, NILECX-8768, OrchestratorBug-22
- **Open questions:** Brand promotion vs. customer trust, customization scope, chat history sharing, sponsored disclosure
- **Dune Prompt Tuning:** https://quip-amazon.com/5qjeA4akbvdw
- **Rufus Studio Roadshow:** https://broadcast.amazon.com/channels/98235

### Discovery #2: Rufus LLM on Bedrock - TEX

- **Quip:** https://quip-amazon.com/UH78Av7IMyw9
- **Author:** Billy Kwok (billyhkk)
- **Concept:** Use Rufus LLM (the model itself) via Bedrock for TEX/BIL custom use cases
- **Differentiators:**
  1. Full data ownership (trained from scratch)
  2. Unique training data (web crawl + Amazon internal, ASIN/Brand markup generation)
  3. Multilingual (Godzilla model, multilingual by design)
  4. Inference cost (target $0.625/M tokens, Inf2 optimized)
  5. Science team support (prompt engineering, custom fine-tuning)
  6. Full Amazon ownership (no external license risk)
- **Benchmarks:** Beats Claude 2, GPT-3.5, Mixtral on Shopping/multilingual; loses to GPT-4, Claude-3-Sonnet
- **Models:** Godzilla family x4 (4K context, us-east-1): godzilla-ift-picasso (prod IFT), vision_v1 (multimodal), etc.
- **AWS Access:** DEV (864899849725), PROD (390844762683) -- STS Role Chaining. Acquired.
- **Slack:** #rufus-on-bedrock-clients
- **Contact:** @twalice
- **Wiki:** https://w.amazon.com/bin/view/Search/Nile/StoresLLM/ModelUserGuide/

### Relationship Between the Two Discoveries

| | #1 API on Stores | #2 LLM on Bedrock |
|---|---|---|
| Approach | Rufus services (NOS/NMS/NCS) | Rufus LLM via Bedrock directly |
| Customization | Dune agent config | Full control |
| Guardrails | Built-in from Rufus team | Must build own |
| Cost | NCS caching = low cost | $0.625/M tokens |
| Maturity | Phase 2 (API onboarding) | DEV/PROD accounts acquired |

### PARC Prototype: Rufus on Stores

- **URL:** https://console.harmony.a2z.com/parc/#/prototypes/rufus-on-stores
- **ID:** l5f3YH21E
- **Author:** Billy Kwok (billyhkk)
- **Status:** In Progress
- **Target locales:** AU, CA, DE, ES, FR, IT, JP, MX, UK, US
- **WARNING: "This is not safe to pitch yet"**
- **Preview:** amazon.co.uk Store Page (VPN required)
- **Code repo:** BIL-TEX-Prototype-RufusOnStorePage-Campaign (code.amazon.com)

### ARC Campaigns

- Rufus-related campaigns: **0**

## 5. Infrastructure and Teams

| Item | Details |
|---|---|
| AWS Account | bil-tex-rufus-prod -- owned by Mirko Capello (mirkocap) EU/APAC TEX |
| Code Repo | BIL-TEX-Prototype-RufusOnStorePage-Campaign |
| Alternative | AI Product Selector (PARC) -- more flexible but weaker guardrails. LEGO declined (AI/brand safety concerns) |
| Slack | #rufus-on-bedrock-clients |

## 6. Key People

| Name | Role |
|---|---|
| Billy Kwok (billyhkk) | Prototype owner, both Discoveries lead |
| Mirko Capello (mirkocap) | Infra owner (bil-tex-rufus-prod) |
| Eric Liao (ecliao) | BIL AI |
| Kelly Prudente (kellypru) | AI Product Selector |
| Alex Mejias (amjias) | WW TEX Lead |
| @twalice | Rufus LLM Bedrock contact |

## 7. Business Impact

- Fortune article: Rufus on pace for additional $10B in sales
- Rufus users have 60% higher purchase completion rate
- Strong interest from CPG/Enterprise brands (Andrew Haynes/andrewlh)

## 8. Key Observations

- All BIL TEX Rufus work is **bottom-up initiative by Billy Kwok**, not in OP1/formal goals
- OP1, QBR: No Rufus mentions
- WBR: Rufus API onboarding listed in Billy's EU Endemics task list
- Official Rufus API sign-off still pending as of Nov 2025
- Rufus 2026 roadmap focuses on engagement scaling in existing markets, NOT new market expansion

## 9. Sources

### Quip
- [Discovery] Rufus API on Store Landing Pages: https://quip-amazon.com/BeNqA5zo9z9j
- [Discovery] Rufus LLM on Bedrock - TEX: https://quip-amazon.com/UH78Av7IMyw9
- Dune Prompt Tuning: https://quip-amazon.com/5qjeA4akbvdw

### PARC
- Rufus on Stores: https://console.harmony.a2z.com/parc/#/prototypes/rufus-on-stores

### Wiki
- Rufus International Editorial: https://w.amazon.com/bin/view/Rufuseditorialwiki/external/international/
- Rufus Desktop i18n Weblab: https://w.amazon.com/bin/view/Weblab/BarRaiser/RUFUS_DESKTOP_INTERNATIONALIZAITON_1190921/
- Rufus BTF Locale Expansion: https://w.amazon.com/bin/view/Weblab/BarRaiser/RUFUS_INLINE_BTF_LOCALE_EXPANSION_1265994/
- Rufus Product Marketing: https://w.amazon.com/bin/view/Alexa_Shopping/Rufus/Engagement_Marketing/
- Rufus Kingpin Goals: https://w.amazon.com/bin/view/Users/Bkknapp/Projects/Rufus/
- BIL TEX: https://w.amazon.com/bin/view/BrandInnovationLab/Work_With_Us/Technology_Experience/
- BIL AI: https://w.amazon.com/bin/view/BrandInnovationLab/Resources/GenerativeAI/
- NMS Onboarding: https://w.amazon.com/bin/view/Alexa_Shopping/NileProductEngineering/NileMainService/ClientOnboarding/
- NOS Onboarding: https://w.amazon.com/bin/view/Alexa_Shopping/NileProductEngineering/NileCXOrchestrator/Onboarding/
- NCS Contact: https://w.amazon.com/bin/view/Alexa_Shopping/Nile/NileCachingService/contact-us/
- Rufus LLM Model Guide: https://w.amazon.com/bin/view/Search/Nile/StoresLLM/ModelUserGuide/

### Slack
- #bil-ai (2025-11-05): Rufus prototype discussion thread
- #bil-tex-oncall-rotation (2025-11-13): bil-tex-rufus-prod AWS account
- #bil-eu-apac-tex (2026-02-05): PARC date correction

### Broadcast
- Rufus Studio Roadshow: https://broadcast.amazon.com/channels/98235
