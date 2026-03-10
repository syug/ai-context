# AU Prime Early Screenings -- Tech Check Report

**Event Cinemas x Amazon Prime -- Australia Pilot**
**Date:** 2026-02-27
**Status:** Tech Check Complete

---

## Executive Summary

### Purpose

The AU BIL team is evaluating the launch of Prime Early Screenings (PES) in Australia with Event Cinemas as the ticketing partner. This report covers three areas of technical assessment:

1. **Task 1:** Understanding the US PES technical architecture
2. **Task 2:** Assessing Prime authentication feasibility in AU
3. **Task 3:** "Gut Checking" Event Cinemas' proposed authentication method

### Overall Assessment

| Item | Verdict |
|------|---------|
| Event Cinemas SHA256 Proposal | **REJECT** -- 2 Critical risks (pre-shared key exposure + MemberId PII leakage) |
| PES Feasibility in AU | **FEASIBLE** -- but requires a different approach than US |
| Recommended Approach (Primary) | **LWA + PrimePass (Fandango model)** -- proven in US, OAuth 2.0 standard |
| Recommended Approach (Alternative) | **Ellis Prime Offer Code CX (ODEON model)** -- no LWA integration needed, no Amazon Pay needed, 4-6 weeks |

### Key Risks

- PrimePass (`prime:benefit_status` scope) AU marketplace support is unverified
- Ellis Prime Offer Code CX AU marketplace availability is unconfirmed
- Amazon Pay is not available in AU, limiting certain integration patterns

### Top Priority Next Step

Verify Ellis Prime Offer Code CX AU marketplace availability with the Prime Ellis team (whitmeye), and verify PrimePass AU support with the Identity Services team.

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
> -- Kelly Prudente (kellypru), #bil-tech-community / #bil-ww-tex

| Component | Role |
|-----------|------|
| **Login with Amazon (LWA)** | OAuth 2.0 authentication. Shares Prime status with customer consent |
| **PrimePass** | Extended LWA scope. Returns Prime membership as Yes/No |
| **Bullseye API** | Controls Prime-member-only content visibility within Brand Store |
| **Directed ID** | Opaque, per-3P-unique identifier. Amazon's internal MemberId is never exposed externally |

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
| Sr. SM (Wicked) | Hannah Hill (hannahnl) |
| Head of US TelEnt | Rob Alley (alleyrob) |
| Director, BIL | Kate McCagg (kmccagg) |
| VP, Global Prime | Jamil Ghani |
| Sr. PM, Prime Tech | Sonam Kothary |
| Head of AU BIL | Chris Wilson (wilsnup) |
| Sr. SM (AU) | Matt Bryant (mjlb) |

---

## Task 2: AU Prime Authentication Feasibility

### AU-Specific Constraints

| Constraint | Impact |
|-----------|--------|
| Amazon Pay not available in AU | Cannot directly replicate the US Fandango model |
| Fandango not operating in AU | Requires a different ticketing partner (Event Cinemas) |
| LWA AU support | LWA is supported in the FE region (JP, SG, AU) |
| PrimePass AU support | Needs verification (proven in US/UK) |

### Key Findings

#### 1. LWA Australia Support -- CONFIRMED

LWA's internal documentation confirms AU is a supported marketplace under the FE region.

| Region | Marketplaces |
|--------|-------------|
| NA | US, CA, MX, BR |
| EU | DE, FR, IT, ES, NL, BE, UK, IE, SE, PL, IN, ZA |
| **FE** | **JP, SG, AU** |

*Source: Identity Services / LWA Marketplaces to Region Mapping Wiki*

**Technical implication:** AU amazon.com.au accounts route to the FE region LWA authentication portal. The OAuth 2.0 flow itself is functional in AU. However, whether PrimePass (`prime:benefit_status` scope) correctly returns Prime membership status for AU marketplace accounts requires separate verification.

#### 2. PrimePass -- NEEDS VERIFICATION

PrimePass is an LWA scope managed by the Identity Services / 3P AuthZ team.

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

Research revealed a directly applicable precedent: ODEON Cinemas (UK/IE) has been operating a Prime member movie ticket discount program under the Ellis "Prime Offer Code CX" configuration since **December 2023**.

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
| **LWA + PrimePass** (Fandango model) | Yes | No | Needs verification | 8-12 weeks | High | **Priority 1** |
| **Ellis Prime Offer Code CX** (ODEON model) | No | No | Needs verification | 4-6 weeks | High | **Priority 2** |
| **Bullseye API** (complementary) | No | No | Likely supported | 1-2 weeks | High (display only) | Complementary |
| **Event Cinemas SHA256** | No | No | Possible | 2-4 weeks | **CRITICAL RISKS** | **Rejected** |

### Unresolved Verification Items

| # | Item | Contact | Priority |
|---|------|---------|----------|
| 1 | Ellis Prime Offer Code CX AU marketplace availability | Prime Ellis team (whitmeye) | **Critical** |
| 2 | PrimePass AU marketplace support | Identity Services team | High |
| 3 | Bullseye API AU support | BIL Tech team | Medium |
| 4 | Event Cinemas Ellis API integration capability | Event Cinemas tech team | Medium |

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

**Mars Dine MindReader comparison (CDK code analysis):**

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

### Priority 1: LWA + PrimePass (Fandango Model) -- PRIMARY

| Item | Detail |
|------|--------|
| **Approach** | Event Cinemas integrates LWA SDK; PrimePass verifies Prime membership |
| **Why primary** | Proven in US PES (128K+ tickets per event), OAuth 2.0 standard, explicit customer consent, Directed ID protects privacy |
| **AU readiness** | LWA confirmed for FE region (AU). PrimePass AU support needs verification |
| **Timeline** | 8-12 weeks |
| **DT burden** | None (authentication handled by LWA + Event Cinemas) |
| **3P burden** | Medium (LWA SDK integration required) |
| **Pending verification** | PrimePass `prime:benefit_status` scope functionality for AU Prime members |

### Priority 2: Ellis Prime Offer Code CX (ODEON Model) -- ALTERNATIVE

| Item | Detail |
|------|--------|
| **Approach** | Prime members obtain offer codes on Amazon; redeem on Event Cinemas site; verified via Ellis API |
| **Why alternative** | No LWA integration required, no Amazon Pay required, 4-6 week integration, ODEON (UK) cinema precedent since Dec 2023 |
| **AU readiness** | Ellis AU marketplace availability needs verification |
| **Timeline** | 4-6 weeks |
| **DT burden** | None (Ellis team manages authentication) |
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

---

## Action Items

| # | Action | Owner | Priority |
|---|--------|-------|----------|
| 1 | Verify LWA + PrimePass AU support (`prime:benefit_status` scope) | Identity Services team | **Critical** |
| 2 | Verify Ellis Prime Offer Code CX AU marketplace availability | Prime Ellis team (whitmeye) | **Critical** |
| 3 | Verify Bullseye API AU support | BIL Tech team | Medium |
| 4 | Counter-propose Ellis/LWA model to Event Cinemas | AU BIL team -> Event Cinemas | After #1 & #2 |
| 5 | Evaluate Full Scope submission | AU BIL team | After above verifications |

---

## Sources

### Internal Wiki
- Identity Services / 3P AuthZ / Products Using LWA -- PrimePass definition and specifications
- Identity Services / LWA Marketplaces to Region Mapping -- AU confirmed in FE region
- Prime Ellis Team / Offers Launched -- ODEON Cinemas (UK/IE) Prime Offer Code CX case study
- Prime Ellis / Blueprint CX Constructs -- "No LWA integration required", 4-6 week timeline
- Amazon Pay / Prime Ellis Program -- Embedded Store CX (not available in AU)

### Slack
- **#bil-tech-community** -- kellypru: LWA technical options and DT scope clarification for PES
- **#bil-ww-tex** -- kellypru: LWA / Bullseye Prime member verification options
- **#launch-party** -- Wicked: For Good results (PES all-time record)

### Arc / Campaign Documents
- Superman "Anyone Can Be Super" -- Lighthouse campaign
- Wicked "Oz Casts a Spell on Amazon" -- Lighthouse campaign

### Code Analysis
- BIL-TEX-APAC-MarsDine-MindReaderCDK -- jwt-utils/index.ts, cdk-stack.ts (symmetric key handling comparison)

### Attachments
- **[Attachment 1]** Partner API Spec -- Event Cinemas proposal
- **[Attachment 2]** Event Cinemas past case studies (NRMA / CommBank) PDF

### Web
- Login with Amazon Developer Documentation -- Supported Marketplaces
- ODEON Cinemas Prime discount program public information
