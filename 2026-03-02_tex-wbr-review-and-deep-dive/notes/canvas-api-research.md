# "Amazon Canvas API" Research Findings

## Date: 2026-03-02

## Summary

**There is NO evidence that "Amazon Canvas API" exists as a formal, unified API platform for BIL.** The term "Canvas API" in the WBR most likely refers to the **Shop the Show (STS) API** -- or the phrase "canvas" is being used **metaphorically** to describe Amazon's advertising surfaces collectively.

---

## Detailed Findings

### 1. Slack Search Results

#### "Amazon Canvas API" (exact phrase) -- **0 results**
#### "BIL Canvas" -- **0 results**
#### "Canvas platform API" -- **0 results**
#### "Canvas API onboarding" -- **0 results**
#### "unified API BIL" -- **0 results**
#### "BIL platform API" -- **0 results**
#### "canvas platform" BIL -- **0 results**

#### "Canvas API" (exact phrase) -- **17 results, NONE BIL-related**
All 17 results were about:
- Amazon Nova Canvas (AI image generation model) API
- HTML5 Canvas API (web development)
- SageMaker Canvas
- AWS Console Tela Canvas Module
- General Canvas API (Instructure LMS)

#### "advertising canvas" -- **2 results (metaphorical usage)**
- **Wicked Campaign (2024-10-30)**: "creates a fan-centric experience across the Amazon advertising canvas" -- **metaphorical**, meaning "across Amazon's advertising surfaces"
  - Source: `#brand-innovation-lab-launch-party` by fiogreen
  - URL: https://advertising.amazon.com/library/news/wicked-universal-campaign-launch
- **Retail Gazette article (2025-12-17)**: "expanded its advertising canvas across Prime Video, Twitch, Wondery, Amazon Music, and the retail ..." -- again **metaphorical**
  - Source: `#am-voc-stream` (Google Alert)

### 2. Key Finding: harfine's Message about STS API

**Most relevant message** (2026-02-20, from harfine to saitshug DM):
> "We do have tentative approval now from the Shop the Show team to proceed with using their API on our Brand Store pages... ikejanna is leading BIL's Second Screen Experiences from a product perspective... As for additional resources - I've mostly been diving deep with STS's tech. I've learned a bit about the services they use for their proxy API; so long as we can continue to use the API, I don't think we'd need to onboard to any of these directly"

Key references:
- STS proxy API Quip: https://quip-amazon.com/2wLHA73ayw1n/Shop-the-Show-TEX-Second-Screen-Discovery
- Tech Overview Doc: https://quip-amazon.com/YriZA70zhQBI/2025-VP-Goal-Second-Screen-Tech-Overview-Discovery-Doc
- Customer Session Tracking wiki: https://w.amazon.com/bin/view/Amazon_Video/PV_Playback/Docs/ServicesAPIs/

**This confirms BIL is using the Shop the Show API specifically -- not a broader "Canvas API."**

### 3. "Brand Content API" (BCAPI) -- A Different System Entirely

The Brand Stores team operates a **Brand Content API (BCAPI)** which is:
- An internal API for Brand Stores content management
- Used by Amazon partners to access organic brand experiences
- Part of the "Brand Building Blocks" service
- Onboarding wiki: https://w.amazon.com/bin/view/BBBTech/Development/BCAPIOnboarding/

This is **NOT** what the WBR would call "Canvas API" -- it's infrastructure for Brand Stores content, not a new BIL initiative.

### 4. AWSC-Tela-Canvas -- AWS Console, NOT Advertising

The "AWSC-Tela-Canvas" packages found in internal search are:
- AWSC-Tela-Canvas-Module-API
- AWSC-Tela-Canvas-Module-CDK
- AWSC-Tela-Canvas-Module

These are **AWS Console platform** components (owned by `aws-console-platform` LDAP group), not advertising-related. They power the AWS Console's "Tela" interface framework.

### 5. Anna Ikejiani (ikejanna) -- No Canvas API Mentions

Searches for ikejanna's messages about Canvas or API returned **0 results**. Her role is confirmed as leading "BIL's Second Screen Experiences from a product perspective" (per harfine's message).

### 6. Brand Stores Architecture (for context)

The Brand Stores product suite includes:
- Stores Builder AX (WYSIWYG editor)
- Stores Rendering Engine
- Stores Analytics and Dashboard
- Stores backend APIs (microservices)
- Brand Building Blocks / Brand Content API (BCAPI)

None of these are called "Canvas API."

### 7. "Advertising Canvas" as Marketing Language

The Shoptalk conference recap (2025-03-26, by jhaleluk in `#asv-heard-on-the-street`) uses "canvas" metaphorically:
> "eye opening to gain a deeper understanding of the role of various video formats across the Amazon canvas"

The MENA Brand Stores wiki also uses "canvas" metaphorically:
> "Brand Stores offer brands a variety of benefits spanning brand control, **brand canvas** and Amazon coverage... Stores provide a canvas for the brand to tell their story on Amazon."

---

## Conclusion

**"Amazon Canvas API" as a formal unified API platform does NOT exist based on available evidence.**

The WBR's reference to "Canvas API" most likely means one of two things:

1. **Shop the Show (STS) API** -- The specific API that BIL has tentative approval to use for Second Screen experiences on Brand Store pages. This is the only concrete API that BIL is actively working to integrate.

2. **Metaphorical usage** -- "Canvas" is widely used in Amazon Ads marketing language to mean "the full range of Amazon advertising surfaces" (Prime Video, Twitch, Fire TV, Brand Stores, etc.). The WBR may have used "Canvas API" loosely to describe programmatic access to these surfaces.

There is **no evidence** of a new, broader unified API initiative that would let BIL programmatically interact with multiple Amazon surfaces through a single "Canvas API." The work happening is specifically about using the STS API on Brand Stores.
