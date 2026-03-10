# AU Prime Early Screenings -- Tech Check Report

**Event Cinemas x Amazon Prime -- Australia Pilot**
**Date:** 2026-02-27 (initial) | 2026-03-10 (last updated, V4)
**Status:** Tech Check Complete -- US Validation Received

---

## Executive Summary

### Purpose

The AU BIL team is evaluating the launch of Prime Early Screenings (PES) in Australia with Event Cinemas as the ticketing partner. This report covers three areas of technical assessment:

1. **Task 1:** Review US PES user flow and technical details
2. **Task 2:** Assess Prime authentication feasibility in AU
3. **Task 3:** "Gut check" Event Cinemas' proposed authentication method

### Task Results

| Task | Verdict | Summary |
|------|---------|---------|
| 1. US PES Technical Review | **Reviewed** | LWA + Prime Ellis is the foundation. Validated by US DT (Kelly Prudente, 2026-03-03) |
| 2. AU Feasibility | **Feasible** | LWA confirmed for AU (FE region). PrimePass and Ellis AU support need verification |
| 3. Event Cinemas Proposal | **Reject** | 2 Critical risks: pre-shared key exposure + MemberId PII leakage |

### Recommended Approach

| Priority | Approach | Timeline | Status |
|----------|----------|----------|--------|
| **Simplest** | LWA Only — Prime authentication only (`prime:benefit_status`). Offer management is Event Cinemas' responsibility | 2-4 weeks | LWA confirmed; PrimePass AU TBD |
| **Primary** | LWA + Prime Ellis (Fandango model) — OAuth 2.0 standard, proven in US PES | 8-12 weeks | **US Validated** |
| **Alternative** | Ellis Prime Offer Code CX (ODEON model) — No LWA integration needed, lightweight | 4-6 weeks | AU availability TBD |
| Complementary | Bullseye API — Prime-only content visibility in Brand Store | 1-2 weeks | AU-supported (confirmed) |

> **Note on approach progression (V4):** LWA Only is the simplest possible configuration — Amazon provides Prime authentication only, and Event Cinemas handles all offer management (ticket inventory, redemption limits, duplicate prevention) on their side. Adding Ellis (Priority 1 or Alternative) provides Amazon-side offer lifecycle control. The choice depends on how much control Amazon needs over the offer — clarify with Hannah Hill.

**Risks to recommended approach:**

- PrimePass (`prime:benefit_status` scope, within Prime Ellis) AU marketplace support is unverified
- Ellis Prime Offer Code CX AU marketplace availability is unconfirmed
- Amazon Pay is not available in AU — rules out Ellis "Embedded Store CX" (Grubhub model); does not block the above approaches

### Next Steps

- **Contact Hannah Hill (hannahnl)** — US PES program lead (recommended by Kelly). Entry point for all Ellis/LWA technical questions. Understand full engagement process — in the US, Fandango/Atom worked closely with **both the Prime Ellis team and the LWA team** (per Kelly's testimony). Learn how to engage both teams and apply US learnings to AU
  - **Prime Ellis team:** Manages the Prime off-Amazon partnership program — offer lifecycle, eligibility rules, partner onboarding, Verify/Redeem APIs
  - **LWA team (Identity Services):** Manages Login with Amazon — OAuth 2.0 authentication, `prime:benefit_status` scope for Prime membership verification
  - **Key question:** Why did US PES use Ellis at all? Would pure LWA (`prime:benefit_status` only) have been sufficient? If Event Cinemas handles offer management independently, Ellis may not be required
- **Clarify US PES Ellis feature usage via Hannah** — Confirm which Ellis features US PES actually uses (Verify/Redeem APIs, inventory management, duplicate redemption prevention) versus what Fandango implements independently. Fandango/PES is not listed in Ellis Blueprint CX Wiki, suggesting a custom integration
- **Verify PrimePass AU support via Hannah** — Connect with Identity Services team (see Action Items)
- **Ads Security Engineer validation** — Sunit Guldas (gulsunit) gut check on SHA256 Critical findings (Slack DM sent, awaiting response)

---

## Task 1: US PES User Flow & Technical Review

### Program Overview

Prime Early Screenings (PES) is a program offering Amazon Prime members early-access movie screening tickets. In the US, the program operates with Fandango as the ticketing partner, with BIL handling creative production and TelEnt leading the program.

### US Track Record

| Film | Tickets Sold | Box Office |
|------|-------------|------------|
| Wicked (2024) | 128,000 | $2.5M |
| Superman (2025) | 144,000 | $2.9M |
| Wicked: For Good (2025) | -- | $3.26M (opening day -- PES all-time record) |

_[Tier 3: Slack #launch-party] [Tier 4: Arc campaign documents]_

### US User Flow (5 Steps)

| Step | Action | Details |
|------|--------|---------|
| 1 | **Entry Points** | H1 (Homepage Hero), Fire TV, Prime Video, Ads, Social media drive traffic to Brand Store |
| 2 | **Brand Store Page** | Central hub with ticket CTA, trailer, merch, Alexa themes. Superman BSP: 1.38M PV, 256K ticket click-outs |
| 3 | **Fandango Redirect** | Ticket purchase CTA click redirects to Fandango's ticket purchase page (external link-out) |
| 4 | **LWA Prime Verification** | Fandango uses Login with Amazon to verify Prime membership status. BIL/DT implements zero auth logic |
| 5 | **Ticket Purchase** | Completed on Fandango platform. Superman included Round-Up donation feature (first integration) |

### Technical Architecture

> *"From a DT perspective, we did nothing for member authentication. That was handled by the third-party ticket partner (Atom/Fandango) working with the Login with Amazon team."*
> -- Kelly Prudente (kellypru), #bil-tech-community / #bil-ww-tex [Tier 1: Direct testimony]

| Component | Role |
|-----------|------|
| **Login with Amazon (LWA)** | OAuth 2.0 authentication. Shares Prime status with customer consent |
| **PrimePass** | LWA extended scope (`prime:benefit_status`). Returns Prime membership as Yes/No. Part of the Prime Ellis ecosystem. *Confirmed by Kelly Prudente (US DT), 2026-03-03, that Fandango/Atom integrated using this scope* [Tier 2: Identity Services Wiki] [Tier 1: Kelly DM 2026-03-03] |
| **Bullseye API** | Controls Prime-member-only content visibility within Brand Store |
| **Directed ID** | Opaque, per-3P-unique identifier. Amazon's internal MemberId is never exposed externally [Tier 2: Identity Services Wiki] |

### US PES Security Design Principles

- **Explicit customer consent:** OAuth consent screen requires customer approval
- **Minimal data sharing:** Only Prime status (Yes/No) is shared; no personal information
- **Directed ID:** Different identifier per 3P partner; cross-site tracking not possible
- **Standards compliance:** OAuth 2.0 / OpenID Connect

### Key Stakeholders (US PES)

| Role | Name |
|------|------|
| DT (Wicked/Superman) | Kelly Prudente (kellypru) |
| Principal DT, Non-Endemic | Rawle Curtis (rawcur) |
| DT (Superman) | Dima Kyrylov (dimakyry) |
| **Hannah Hill (hannahnl)** | Sr. SM, US TelEnt — US PES Program Lead. Key contact for AU engagement process. Led Fandango integration for Wicked and Superman campaigns |
| Head of US TelEnt | Rob Alley (alleyrob) |
| Director, BIL | Kate McCagg (kmccagg) |
| VP, Global Prime | Jamil Ghani |
| Sr. PM, Prime Tech | Sonam Kothary |
| Head of AU BIL | Chris Wilson (wilsnup) |
| Sr. SM (AU) | Matt Bryant (mjlb) |

---

## US DT Validation (2026-03-03)

_This section validates the Task 1 findings above and informs the recommendations in later sections._

### Source
Kelly Prudente (kellypru), US DT (Wicked/Superman campaign lead), via Slack DM on 2026-03-03.

### Key Confirmations

1. **Fandango/Atom used LWA + Prime Ellis integration** -- Both onboarded with Login with Amazon (LWA) and worked closely with both the LWA team and the Prime Ellis team [Tier 1: Kelly DM 2026-03-03]
2. **`prime:benefit_status` scope confirmed** -- LWA passes Prime membership status via this scope. This is the mechanism that enables 3P partners to determine Prime eligibility [Tier 1: Kelly DM 2026-03-03]
3. **3P-led implementation** -- The integration was on fandango.com/atom.com, implemented by their developers. LWA team members helped them through the process [Tier 1: Kelly DM 2026-03-03]
4. **Strict Prime exclusive offer rules** -- In the US, labeling something as a Prime exclusive offer requires LWA onboarding, as LWA can pass the "is Prime member" parameter securely and accurately [Tier 1: Kelly DM 2026-03-03]
5. **Hannah Hill (hannahnl) led the initiative** -- Kelly's SM was "pretty key in leading this." Recommended as the contact to understand all steps taken and how to engage the Prime Ellis + LWA teams [Tier 1: Kelly DM 2026-03-03]

### PrimePass / Prime Ellis Relationship -- Clarification

V1 of this report presented "LWA + PrimePass" and "Ellis Prime Offer Code CX" as two separate alternatives. Kelly's validation reveals a more nuanced picture:

- **PrimePass** (`prime:benefit_status` scope) is the LWA mechanism for Prime membership verification
- **Prime Ellis** is the broader platform for Prime off-Amazon experiences
- In the US Fandango case, **both LWA and Prime Ellis worked together** -- they are complementary, not alternatives

This means:
- **Full integration (Fandango model):** LWA authentication + Prime Ellis platform = the proven US approach
- **Lightweight integration (ODEON model):** Ellis Prime Offer Code CX only = no LWA needed, code-based verification

Both options remain valid for AU. The choice depends on Event Cinemas' technical capability and desired user experience.

### Fandango API Integration Project (US)
- US Telent (now US Entertainment + Beauty, after reorg) had planned to bring ticketing to amazon.com as an E2E purchase flow
- Status: Likely still on hold [Tier 1: Kelly DM 2026-03-03]
- Not directly relevant to AU's 3P model, but US PES learnings (Wicked, Superman, D&D, etc.) are 100% applicable

### LWA Developer Resources
- 3P onboarding guidance: https://developer.amazon.com/docs/login-with-amazon/web-docs.html
- LWA scopes portal: https://console.harmony.a2z.com/lwa-tools-portal/scopes

---

## Task 2: AU Prime Authentication Feasibility

### AU-Specific Constraints

| Constraint | Impact |
|-----------|--------|
| Amazon Pay not available in AU | Rules out Ellis 'Embedded Store CX' (Grubhub model); does not block LWA + Prime Ellis (Fandango model) |
| Fandango not operating in AU | Requires a different ticketing partner (Event Cinemas) |
| LWA AU support | LWA is supported in the FE region (JP, SG, AU) |
| PrimePass AU support | Needs verification (proven in US/UK) |

### Key Findings

#### 1. LWA Australia Support -- CONFIRMED

LWA's internal documentation confirms AU is a supported marketplace under the FE region. [Tier 2: LWA Marketplaces Wiki]

| Region | Marketplaces |
|--------|-------------|
| NA | US, CA, MX, BR |
| EU | DE, FR, IT, ES, NL, BE, UK, IE, SE, PL, IN, ZA |
| **FE** | **JP, SG, AU** |

*Source: Identity Services / LWA Marketplaces to Region Mapping Wiki*

**Technical implication:** AU amazon.com.au accounts route to the FE region LWA authentication portal. The OAuth 2.0 flow itself is functional in AU. However, whether PrimePass (`prime:benefit_status` scope) correctly returns Prime membership status for AU marketplace accounts requires separate verification.

> **Note (V4):** LWA with `prime:benefit_status` is sufficient for Prime authentication on its own. If Event Cinemas manages offer lifecycle (ticket inventory, redemption limits, duplicate prevention) independently, no Ellis integration is required on the Amazon side. Ellis is an additional layer for Amazon-side offer control, not a prerequisite for authentication.

#### 2. PrimePass -- NEEDS VERIFICATION

PrimePass is an LWA scope managed by the Identity Services / 3P AuthZ team. [Tier 2: Identity Services Wiki]

- **Domain:** `prime`
- **Scope:** `prime:benefit_status`
- **Returns:** Customer's Amazon Prime membership status (Yes/No only)
- **Customer identification:** Directed ID (opaque, per-3P-unique identifier; not Amazon's internal MemberId)
- **Consent:** Explicit customer consent screen via OAuth flow

**Unverified for AU:**
- Whether the scope returns valid data for AU marketplace Prime members
- Whether AU Prime's internal data structure is compatible with PrimePass's expected format

#### 3. Amazon Pay in AU -- NOT AVAILABLE

Amazon Pay is not supported in the AU marketplace. This means the Ellis "Embedded Store CX" (Grubhub model) cannot be used in AU. However, the "Prime Offer Code CX" (ODEON model) does not require Amazon Pay, so this constraint does not block the recommended approach.

#### 4. ODEON Cinemas (UK) Precedent -- KEY DISCOVERY

Research revealed a directly applicable precedent: ODEON Cinemas (UK/IE) has been operating a Prime member movie ticket discount program under the Ellis "Prime Offer Code CX" configuration since **December 2023**. [Tier 2: Ellis Wiki]

| Item | Details |
|------|---------|
| Partner | ODEON Cinemas |
| Region | UK / IE |
| Target | All Prime |
| Configuration | Prime Offer Code CX |
| Offer | Prime members get 2 tickets for GBP 10 / EUR 10 (46%+ discount), Mon-Thu |
| Launch Date | 7 December 2023 |
| Ellis Offer Page | amazon.co.uk/odeon |

**Prime Offer Code CX Flow:**

1. Prime member obtains an offer code on the Amazon site/app
2. Member enters the code on the Event Cinemas site
3. Event Cinemas verifies the code via Ellis API (Verify Code)
4. Verification succeeds -> ticket purchase -> Ellis API (Redeem Code) marks code as used

**Key advantages from Blueprint CX Constructs:**

| Feature | Detail |
|---------|--------|
| No LWA integration required | "No Login with Amazon (LWA) API integration required" -- explicitly stated |
| No Amazon Pay required | Completely bypasses the AU Amazon Pay constraint |
| Lightweight integration | Event Cinemas only needs to integrate Ellis API (Verify Code / Redeem Code) |
| Integration timeline | 4-6 weeks (vs. 8-12 weeks for LWA + PrimePass) |
| Built-in reporting | Redeem Code API tracks code usage |

### Authentication Method Comparison Matrix

| Method | LWA Required | Amazon Pay Required | AU Support | Integration Timeline | Security | Recommendation |
|--------|:---:|:---:|:---:|:---:|:---:|:---:|
| **LWA Only** (Prime auth only) | Yes | No | Needs verification (LWA confirmed for AU; PrimePass AU support TBD) | 2-4 weeks | High | **Priority 0 -- SIMPLEST** |
| **LWA + Prime Ellis** (Fandango model) | Yes | No | Needs verification | 8-12 weeks | High | **Priority 1 -- US VALIDATED** |
| **Ellis Prime Offer Code CX** (ODEON model) | No | No | Needs verification | 4-6 weeks | High | **Priority 2** |
| **Bullseye API** (complementary) | No | No | AU-supported (confirmed) | 1-2 weeks | High (display only) | Complementary |
| **Event Cinemas SHA256** | No | No | Possible | 2-4 weeks | **CRITICAL RISKS** | **Rejected** |

### Unresolved Verification Items

| # | Item | Contact | Priority |
|---|------|---------|----------|
| 1 | Ellis Prime Offer Code CX AU marketplace availability | Ellis team (Joshua Huang) via Hannah Hill | **Critical** |
| 2 | PrimePass AU marketplace support | Identity Services team | High |
| 4 | Event Cinemas Ellis API integration capability | Event Cinemas tech team | Medium |

*Note: Bullseye API AU support (#3) was resolved on 2026-03-10 — confirmed AU-supported.*

---

## Task 3: Event Cinemas Proposal Gut Check

### Proposed Flow

Event Cinemas (under the EVT Group) proposed a SHA256-based authentication method:

```
Amazon Prime member authentication
  -> SHA256 token generation: SHA256(MemberId + Expires + SecretKey)
  -> HTTP GET redirect to Event Cinemas
  -> Token "decryption" and expiry validation
  -> Early screening ticket purchase
```

**Redirect URL:** `https://www.eventcinemas.com.au/prime#prime_token={encryptedToken}`

**Token payload:**
```json
{
  "MemberId": "{uniqueMemberId}",
  "Expires": "{utcExpiryTime in ISO 8601 format}"
}
```

### Critical Risks (2)

#### Critical 1: Pre-Shared Key Model (Secret Key Shared with External Company)

Event Cinemas' SHA256 method requires Amazon and Event Cinemas to **hold the same secret key**.

| Risk | Detail |
|------|--------|
| Key leakage = full forgery | If the key leaks on Event Cinemas' side, any third party can generate valid tokens |
| No non-repudiation | Cryptographically impossible to prove who generated a token |
| Key rotation difficulty | Both parties must change the key simultaneously (high operational burden) |
| Amazon policy conflict | Likely violates Amazon's key management policies restricting external sharing of secret keys |

**Mars Dine MindReader comparison (CDK code analysis):** [Tier 4: CDK Code Analysis]

Mars Dine also uses JWT HS256 (symmetric key), but with a critical difference:

- Mars Dine: Key stored in AWS Secrets Manager, used only within Lambda, **never shared externally**
- Mars Dine: KMS encryption (JWTSecretKey) with dual protection
- Mars Dine: Automatic rotation (every 30 days, RotationSchedule implemented)
- Event Cinemas proposal: Key **must be handed to an external company**

#### Critical 2: MemberId PII Exposure

The token payload contains `"MemberId": "{uniqueMemberId}"`, directly exposing Amazon's internal customer identifier to an external company.

| Risk | Detail |
|------|--------|
| PII external sharing | Amazon's customer identifier shared directly with an external company |
| No customer consent | Automatic redirect with no explicit customer consent process |
| Tracking risk | MemberId enables tracking of Amazon customers' behavior |
| No data retention control | Amazon cannot control how Event Cinemas stores or uses the MemberId |

**Contrast with LWA + PrimePass:**

- PrimePass shares **only** Prime membership status (Yes/No)
- Customer identification uses **Directed ID** (opaque, per-3P-unique identifier)
- **Explicit customer consent screen** via OAuth flow
- Amazon's internal MemberId is **never exposed externally**

### High Risks (3)

| # | Risk | Detail |
|---|------|--------|
| 1 | **Non-standard specification** | Does not comply with OAuth 2.0, JWT (RFC 7519), or OpenID Connect. Requires individual security review (AppSec burden), no standard libraries available, custom implementation and maintenance needed |
| 2 | **Replay attack vulnerability** | No nonce mechanism. Token can be reused unlimited times within the expiry window (2-10 minutes). JWT provides `jti` (JWT ID) claim for uniqueness; SHA256 hash has no such mechanism |
| 3 | **Cryptographic terminology confusion** | Spec describes SHA256 as "encryption" and verification as "decryption." SHA256 is a one-way hash function, not encryption. This suggests concerns about Event Cinemas' understanding of cryptographic principles |

### Conditional / Incomplete Items

| # | Item | Verdict |
|---|------|---------|
| 1 | Token expiry (2-10 min) | Range is reasonable, but no replay attack protection |
| 2 | URL fragment usage (`#`) | Fragment not sent to server (good), but accessible via JavaScript and browser history (XSS risk) |
| 3 | Purchase confirmation webhook | Marked as "optional" -- insufficient for PES reporting requirements |

### Pass Items

| Item | Note |
|------|------|
| TLS 1.2+ | Industry standard. However, transport-layer encryption does not substitute for application-layer security |

### NRMA / CommBank Precedent Applicability

Event Cinemas cited two precedents (My NRMA, CommBank Yello). **These are not applicable to Amazon:**

1. NRMA / CommBank are **domestic Australian companies**; Amazon is a global enterprise with fundamentally different security/privacy requirements
2. Amazon already has **PrimePass / Ellis** -- purpose-built official 3P integration mechanisms
3. Amazon's data privacy policies restrict external sharing of customer identifiers
4. Amazon's security review process (AppSec) is stringent regarding custom cryptographic implementations
5. PII cross-border transfer regulations (AU Privacy Act + Amazon internal policies) apply

### Overall Assessment Matrix

| # | Evaluation Item | Verdict | Severity |
|---|----------------|---------|----------|
| 1 | Encryption method (SHA256 PSK) | **FAIL** | Critical |
| 2 | MemberId external exposure | **FAIL** | Critical |
| 3 | Standards compliance | **FAIL** | High |
| 4 | Replay attack resistance | **FAIL** | High |
| 5 | Cryptographic understanding | **Concern** | High |
| 6 | Token expiry | Conditional | Medium |
| 7 | Redirect URL structure | Conditional | Medium |
| 8 | Transport security (TLS 1.2+) | **Pass** | -- |
| 9 | Purchase confirmation webhook | Incomplete | Medium |
| 10 | Precedent applicability | N/A | -- |

### Gut Check Conclusion

Event Cinemas' proposal **does not meet Amazon's security and privacy requirements**. The two Critical risks (pre-shared key exposure + MemberId PII leakage) are fundamental design issues that cannot be resolved through parameter tuning (e.g., shortening expiry windows).

> **Important:** This does NOT mean Event Cinemas is rejected as a partner. If Event Cinemas is willing to switch to Amazon's existing infrastructure (Ellis / LWA), the partnership is technically feasible. The ODEON Cinemas (UK) precedent is directly applicable.

---

## Recommendations

**DT burden for all recommended approaches: None.** Authentication is handled by LWA and/or Ellis — no custom DT development required.

### Priority 0: LWA Only -- SIMPLEST CONFIGURATION

> **New in V4:** Based on the Event Cinemas proposal structure (Event Cinemas handles all ticketing and offer management), the minimum Amazon-side requirement is Prime authentication only.

| Item | Detail |
|------|--------|
| **Approach** | Event Cinemas integrates LWA SDK; uses `prime:benefit_status` scope to verify Prime membership. All offer management (ticket inventory, redemption limits, duplicate prevention) handled by Event Cinemas |
| **Why simplest** | Minimum integration footprint on both sides. Amazon provides authentication only; Event Cinemas owns the offer lifecycle |
| **AU readiness** | LWA confirmed for FE region (AU). PrimePass AU support needs verification |
| **Timeline** | 2-4 weeks (LWA SDK integration only) |
| **3P burden** | Low-Medium (LWA SDK integration + self-managed offer logic) |
| **Pending verification** | PrimePass `prime:benefit_status` scope functionality for AU Prime members |
| **When to choose** | Event Cinemas is willing and capable of managing the full offer lifecycle independently |

### Priority 1: LWA + Prime Ellis (Fandango Model) -- PRIMARY -- US VALIDATED

> **Validated by US DT:** Kelly Prudente (kellypru) confirmed on 2026-03-03 that Fandango/Atom used LWA + Prime Ellis integration for US PES campaigns (Wicked, Superman). This is the proven architecture.

> **Note on Ellis feature scope (V3):** Throughout this report, Ellis capabilities such as Verify/Redeem APIs, offer lifecycle management, inventory control, and duplicate redemption prevention are described based on Ellis platform documentation (Tier 2: Wiki sources). **It has not been confirmed which of these features US PES actually utilizes.** Kelly Prudente's testimony (Tier 1) confirmed "LWA + Prime Ellis" as the integration model, but did not specify which Ellis features Fandango uses versus implements independently. Additionally, Fandango/PES is not listed in the Ellis Blueprint CX Wiki (suggesting a custom integration outside the standard patterns). Confirmation of US PES's actual Ellis feature usage is required from Hannah Hill (hannahnl) -- see Action Items.

| Item | Detail |
|------|--------|
| **Approach** | Event Cinemas integrates LWA SDK; Prime Ellis platform verifies Prime membership via `prime:benefit_status` scope |
| **Why primary** | Proven in US PES (128K+ tickets per event), OAuth 2.0 standard, explicit customer consent, Directed ID protects privacy. **US DT validated.** |
| **AU readiness** | LWA confirmed for FE region (AU). PrimePass AU support needs verification. Prime Ellis team involvement is confirmed (not just LWA) |
| **Timeline** | 8-12 weeks |
| **3P burden** | Medium (LWA SDK integration required) |
| **Pending verification** | PrimePass `prime:benefit_status` scope functionality for AU Prime members |

### Priority 2: Ellis Prime Offer Code CX (ODEON Model) -- ALTERNATIVE

> **Note:** This is a subset of the Prime Ellis platform, using code-based verification without LWA.

| Item | Detail |
|------|--------|
| **Approach** | Prime members obtain offer codes on Amazon; redeem on Event Cinemas site; verified via Ellis API |
| **Why alternative** | No LWA integration required, no Amazon Pay required, 4-6 week integration, ODEON (UK) cinema precedent since Dec 2023 |
| **AU readiness** | Ellis AU marketplace availability needs verification |
| **Timeline** | 4-6 weeks |
| **3P burden** | Low (only Ellis API: Verify Code + Redeem Code) |
| **Pending verification** | Ellis Prime Offer Code CX AU marketplace availability |

### Priority 3: Bullseye API (Complementary)

| Item | Detail |
|------|--------|
| **Approach** | Use Amazon Brand Gateway segment API to control Prime-only content display in Brand Store |
| **Role** | Complementary to Priority 1 or 2; not a standalone authentication method |
| **Use case** | Show ticket CTA only to Prime members within Brand Store |
| **Timeline** | 1-2 weeks |

### Counter-Proposal to Event Cinemas

Event Cinemas' SHA256 proposal is rejected, but this **does not reject Event Cinemas as a partner**. The counter-proposal:

- Event Cinemas' technical work is limited to **two Ellis API endpoints only** (Verify Code / Redeem Code)
- No custom encryption implementation required
- Integration timeline: **4-6 weeks**
- Reporting is **built into the Ellis API**
- Direct precedent: **ODEON Cinemas (UK)** has been operating this exact model since December 2023

> **Note (V4):** In addition to the ODEON model counter-proposal above, a simpler option exists: LWA Only (Priority 0), where Event Cinemas handles all offer management independently and Amazon provides Prime authentication only. This may be the most practical starting point if Event Cinemas prefers to retain control of their ticketing workflow. See Recommendations for details.

> **Note:** The Ellis API capabilities listed above (Verify Code, Redeem Code, built-in reporting) are based on Ellis platform documentation. The ODEON model is a confirmed Ellis Blueprint CX pattern. However, for the Fandango/US PES model (Priority 1), the extent to which Ellis manages inventory, duplicate prevention, and offer lifecycle -- versus Fandango managing these independently -- is unconfirmed and requires verification with Hannah Hill.

---

## Action Items

### In Scope (Tech Check Deliverables)

| # | Action | Owner | Priority | Status |
|---|--------|-------|----------|--------|
| 1 | gulsunit SHA256 Critical findings gut check | gulsunit (Sunit Guldas) | Medium | In progress — Slack DM sent (2026-03-10), awaiting response |
| 2 | Share Tech Check results with mjlb | Shugo (DT) | — | Pending (scheduled sync 2026-03-11) |
| 3 | Review recommendation priority order (Fandango model vs ODEON model) | Shugo (DT) | Medium | Pending |
| 5 | Contact kellypru for US PES details | Shugo (DT) | High | Complete (2026-03-03) |

### Next Phase (Essential — Required to Proceed)

| # | Action | Owner | Priority | Status |
|---|--------|-------|----------|--------|
| 6 | Contact Hannah Hill (hannahnl) — US PES program lead (recommended by Kelly). Entry point for all Ellis/LWA technical questions (Note: SM-to-SM outreach via Matt Bryant proposed for initial contact) | Shugo (DT) | **Critical — Next** | Pending |
| 6a | Via Hannah: Understand US PES engagement process and learnings applicable to AU. In the US, Fandango worked with **two teams**: **Prime Ellis team** (off-Amazon partnership / offer management) and **LWA team** (Identity Services / OAuth authentication + `prime:benefit_status`). Learn how to engage both teams for AU | Hannah Hill | Critical | Pending |
| 6b | Via Hannah: Clarify US PES Ellis feature usage — which features does Fandango actually use (Verify/Redeem API, inventory management, duplicate redemption prevention) vs implement independently? **Core question: why was Ellis needed at all? Would pure LWA (`prime:benefit_status` only) have been insufficient?** | Hannah Hill | Critical | Pending |
| 6c | Via Hannah: Verify PrimePass (`prime:benefit_status` scope) AU support — connect with Identity Services team or confirm directly | Hannah Hill / Identity Services | Critical | Pending |
| 7 | Counter-propose Ellis/LWA model to Event Cinemas | AU BIL team | After #6c | Pending |
| 8 | Evaluate Full Scope submission | AU BIL team | After above | Pending |

### Nice-to-have / Add-on

| # | Action | Owner | Priority | Status |
|---|--------|-------|----------|--------|
| 4 | Bullseye API AU support | BIL-E / Shugo | Medium | Complete — confirmed AU-supported. Verify in prototype if proceeding to Full Scope |
| 9 | Check Quip AU BIL Team WIP PES section | Shugo (DT) | Medium | Confirmed (3/10) — PES references are fragmentary mentions only, no detailed technical discussions found |
| 10 | Ellis team engagement + AU availability verification — Required if Amazon needs offer lifecycle control (usage tracking, ticket limits, duplicate prevention), or if Hannah Hill confirms Ellis is necessary for PES. Connect via Hannah to Ellis team (Joshua Huang, Principal PMT) to verify AU marketplace support | Hannah Hill / Ellis team | Low | Pending — depends on #6b outcome |

---

## Sources & Provenance

Information sources are categorized by reliability tier. Higher-tier sources carry more weight due to direct involvement in the subject matter.

### Tier 1: Direct Testimony (Highest Weight)
First-hand accounts from people directly involved in US PES implementation.

| Source | Channel | Date | Key Information Provided |
|--------|---------|------|------------------------|
| **Kelly Prudente (kellypru)** -- US DT, Wicked/Superman campaign lead | Slack DM | 2026-03-03 | Fandango/Atom used LWA + Prime Ellis integration; `prime:benefit_status` scope for Prime verification; Hannah Hill led the initiative; US PES learnings applicable to AU 3P model |
| **Kelly Prudente (kellypru)** | Slack #bil-tech-community | 2026-02 (observed) | "From a DT perspective, we did nothing for member authentication. That was handled by the third-party ticket partner (Atom/Fandango) working with the Login with Amazon team." |
| **Kelly Prudente (kellypru)** | Slack #bil-ww-tex | 2026-02 (observed) | LWA / Bullseye Prime member verification options for PES |

### Tier 2: Internal Documentation (High Weight)
Official Amazon internal wikis and tools. Verified by AI-assisted research, not from direct human testimony.

| Source | URL | Key Information |
|--------|-----|-----------------|
| Identity Services / 3P AuthZ Wiki | https://w.amazon.com/bin/view/IdentityServices/3PAuthZ/ | PrimePass definition: `prime:benefit_status` scope, Directed ID mechanism |
| Identity Services / LWA Marketplaces | https://w.amazon.com/bin/view/IdentityServices/Products/LWA/ | AU confirmed in FE region (JP, SG, AU) for LWA support |
| LWA 3P Authorization Wiki | https://w.amazon.com/bin/view/IdentityServices/3PAuthZ/ | LWA scope details and 3P authorization framework |
| Prime Ellis Team / Offers Launched | https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/ | ODEON Cinemas (UK/IE) Prime Offer Code CX case study, "WW Updates in Progress" |
| Prime Ellis / Blueprint CX Constructs | https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/ | "No LWA integration required" for Offer Code CX, 4-6 week timeline |
| PES Wiki | https://w.amazon.com/bin/view/PrimeEarlyScreenings/ | PES program overview and US track record |
| BIL-E NA Wiki | https://w.amazon.com/bin/view/BIL-E/NA/ | BIL-E intake process and security review framework |
| AmazonAdsSecurity Wiki | https://w.amazon.com/bin/view/AmazonAdsSecurity/ | Ads security consultation process (referenced by Harish) |
| LWA Developer Docs (Public) | https://developer.amazon.com/docs/login-with-amazon/web-docs.html | 3P onboarding guidance (referenced by Kelly as what Fandango followed) |
| LWA Scopes Portal (Internal) | https://console.harmony.a2z.com/lwa-tools-portal/scopes | Available LWA scopes including `prime:benefit_status` (referenced by Kelly) |

### Tier 3: Slack Channel Observations (Medium Weight)
Information observed in public Slack channels. Not directly provided to us -- extracted by AI research from channel history.

| Channel | Key Information | Note |
|---------|----------------|------|
| #bil-tech-community | kellypru's comments on LWA/PES technical options | Observed, not direct testimony |
| #bil-ww-tex | kellypru's comments on Bullseye/LWA verification | Observed, not direct testimony |
| #launch-party | Wicked: For Good results (PES all-time record $3.26M opening day) | Public channel announcement |
| **Harish Bharani (hbbharan)** -- BIL-E Engineering Lead | Slack DM + Asana comment (2026-02-28, 2026-03-03) | Recommended Sunit Guldas (gulsunit) as the Ads Security Engineer for tech check validation |

### Tier 4: Code Analysis & Campaign Documents (Supporting)
Technical analysis and campaign reference materials.

| Source | Key Information |
|--------|-----------------|
| BIL-TEX-APAC-MarsDine-MindReaderCDK (jwt-utils/index.ts, cdk-stack.ts) | JWT HS256 symmetric key handling comparison -- Mars Dine keeps keys in Secrets Manager, never shares externally. Used to contrast with Event Cinemas' pre-shared key proposal |
| Arc: Superman "Anyone Can Be Super" | Lighthouse campaign reference -- PES ticket sales data |
| Arc: Wicked "Oz Casts a Spell on Amazon" | Lighthouse campaign reference -- PES ticket sales data |

### Tier 5: External / Attachments

| Source | Key Information |
|--------|-----------------|
| Event Cinemas Partner API Spec (PDF attachment) | SHA256 authentication proposal under review |
| Event Cinemas past case studies -- NRMA / CommBank (PDF attachment) | Precedent claims (assessed as not applicable to Amazon) |
| ODEON Cinemas Prime discount program (public web) | Public confirmation of ODEON Prime offer program |

### Provenance Notes

- **Tier 1 sources (Kelly) carry the highest weight** because she was directly involved in US PES implementation and has first-hand knowledge of how Fandango/Atom integrated with LWA + Prime Ellis
- **The PrimePass / Prime Ellis relationship clarification (V2)** was derived from Kelly's Tier 1 testimony. V1's separation of these as alternatives was based on Tier 2 wiki research which, while accurate about each component individually, did not capture how they work together in practice
- **Wiki sources (Tier 2)** were found through AI-assisted internal search. While official documentation, they describe capabilities in isolation and may not reflect actual implementation patterns
- **Slack observations (Tier 3)** are Kelly's own words but were observed in channel history rather than provided directly in response to our questions. The same information was later confirmed via direct DM (elevated to Tier 1)
- **(V3) Ellis feature descriptions (Verify/Redeem API, inventory management, duplicate prevention)** are sourced from Tier 2 wiki documentation describing Ellis platform capabilities. Kelly's Tier 1 testimony confirmed "LWA + Prime Ellis" as the integration model but did not detail which specific Ellis features Fandango utilizes. Fandango/PES is absent from the Ellis Blueprint CX Wiki, suggesting a custom integration. Until confirmed by Hannah Hill, Ellis features referenced in this report should be read as platform capabilities, not as confirmed US PES implementation details

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| V1 | 2026-02-27 | Initial tech check report |
| V2 | 2026-03-04 | US DT validation (Kelly Prudente): confirmed LWA + Prime Ellis integration, `prime:benefit_status` scope, Hannah Hill as key contact. PrimePass/Prime Ellis relationship clarified. Action items updated. + structural fixes (table ordering, Amazon Pay constraint clarification, source attribution) |
| V3 | 2026-03-10 (morning) | Added caveat notes distinguishing Ellis platform capabilities (Tier 2 documentation) from confirmed US PES usage (Tier 1 testimony). Fandango/PES not listed in Ellis Blueprint CX Wiki -- custom integration possible. Added action item to clarify actual Ellis feature usage with Hannah Hill (hannahnl) |
| V4 | 2026-03-10 (afternoon) | LWA-only approach clarification: Ellis is not required for authentication -- it is an optional offer management layer. Added Priority 0 (LWA Only) as simplest configuration when Event Cinemas manages offer lifecycle independently. Added key question for Hannah Hill: why did US PES use Ellis? Would pure LWA have sufficed? |
