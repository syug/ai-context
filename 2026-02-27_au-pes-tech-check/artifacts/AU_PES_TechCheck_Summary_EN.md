# AU Prime Early Screenings -- Tech Check Summary

**Date:** 2026-03-10
**Prepared by:** Shugo Saito (DT)
**Intake:** ENT | AU | Prime Early Screenings | Australia Pilot (T2, DT Resource)
**Full Report:** See artifacts/AU_PES_TechCheck_Report_EN.md (V3, 2026-03-10)

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
| **Simplest** | LWA Only -- Prime authentication only (`prime:benefit_status`). Offer management is Event Cinemas' responsibility | 2-4 weeks | LWA AU confirmed |
| **Primary** | LWA + Prime Ellis (Fandango model) -- OAuth 2.0 standard, proven in US PES | 8-12 weeks | **US Validated** |
| **Alternative** | Ellis Prime Offer Code CX (ODEON model) -- No LWA integration needed, lightweight | 4-6 weeks | AU availability TBD |
| Complementary | Bullseye API -- Prime-only content visibility in Brand Store | 1-2 weeks | AU-supported (confirmed) |

> **Note (V4):** LWA Only is the simplest configuration -- Amazon provides Prime authentication only, Event Cinemas handles offer management. Ellis is an optional layer for Amazon-side offer control. Clarify the required level of control with Hannah Hill.

**Risks to recommended approach:**

- PrimePass (`prime:benefit_status` scope, within Prime Ellis) AU marketplace support is unverified
- Ellis Prime Offer Code CX AU marketplace availability is unconfirmed
- Amazon Pay is not available in AU -- rules out Ellis "Embedded Store CX" (Grubhub model); does not block the above approaches

### Next Steps

1. **Contact Hannah Hill (hannahnl)** -- US PES program lead (recommended by Kelly). Entry point for all Ellis/LWA technical questions. Understand full engagement process -- in the US, Fandango/Atom worked closely with **both the Prime Ellis team and the LWA team** (per Kelly's testimony). Learn how to engage both teams and apply US learnings to AU
   - **Prime Ellis team:** Manages the Prime off-Amazon partnership program -- offer lifecycle, eligibility rules, partner onboarding, Verify/Redeem APIs
   - **LWA team (Identity Services):** Manages Login with Amazon -- OAuth 2.0 authentication, `prime:benefit_status` scope for Prime membership verification
   - **Key question:** Why did US PES use Ellis? Would pure LWA (`prime:benefit_status` only) have been sufficient?
2. **Clarify US PES Ellis feature usage via Hannah** -- Confirm which Ellis features US PES actually uses (Verify/Redeem APIs, inventory management, duplicate redemption prevention) versus what Fandango implements independently. Fandango/PES is not listed in Ellis Blueprint CX Wiki, suggesting a custom integration
3. **Verify Ellis AU availability & PrimePass AU support via Hannah** -- Connect with Ellis team (Joshua Huang, Principal PMT) and Identity Services team
4. **BIL-E engineer validation** -- Sunit Guldas (gulsunit) gut check on SHA256 Critical findings (Slack DM sent, awaiting response)

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
| 6 | Contact Hannah Hill (hannahnl) — US PES program lead (recommended by Kelly). Entry point for all Ellis/LWA technical questions | Shugo (DT) | **Critical — Next** | Pending |
| 6a | Via Hannah: Understand US PES engagement process and learnings applicable to AU. In the US, Fandango worked with **two teams**: **Prime Ellis team** (off-Amazon partnership / offer management) and **LWA team** (Identity Services / OAuth authentication + `prime:benefit_status`). Learn how to engage both teams for AU | Hannah Hill | Critical | Pending |
| 6b | Via Hannah: Clarify US PES Ellis feature usage — which features does Fandango actually use (Verify/Redeem API, inventory management, duplicate redemption prevention) vs implement independently? **Core question: why was Ellis needed? Would pure LWA have sufficed?** | Hannah Hill | Critical | Pending |
| 6c | Via Hannah: Verify Ellis AU marketplace availability — connect with Ellis team (Joshua Huang, Principal PMT) or confirm directly | Hannah Hill / Ellis team | Critical | Pending |
| 6d | Via Hannah: Verify PrimePass (`prime:benefit_status` scope) AU support — connect with Identity Services team or confirm directly | Hannah Hill / Identity Services | Critical | Pending |
| 7 | Counter-propose Ellis/LWA model to Event Cinemas | AU BIL team | After #6c & #6d | Pending |
| 8 | Evaluate Full Scope submission | AU BIL team | After above | Pending |

### Nice-to-have / Add-on

| # | Action | Owner | Priority | Status |
|---|--------|-------|----------|--------|
| 4 | Bullseye API AU support | BIL-E / Shugo | Medium | Complete — confirmed AU-supported. Verify in prototype if proceeding to Full Scope |
| 9 | Check Quip AU BIL Team WIP PES section | Shugo (DT) | Medium | Confirmed (3/10) — PES references are fragmentary mentions only, no detailed technical discussions found |
| 10 | Ellis team engagement — if Amazon needs offer lifecycle control, or if Hannah confirms Ellis is required | Hannah Hill / Ellis team | Low | Pending — depends on #6b outcome |

---

## Key Contacts

| Role | Name | Context |
|------|------|---------|
| US PES Program Lead | Hannah Hill (hannahnl) | Kelly recommended. Entry point for Ellis/LWA teams |
| US DT (validated) | Kelly Prudente (kellypru) | Confirmed US PES technical details |
| Ads Security Engineer | Sunit Guldas (gulsunit) | SHA256 gut check (DM sent, awaiting response) |
| Ellis Principal PMT | Joshua Huang | Ellis AU availability (via Hannah) |

---

*Full technical report available in artifacts/AU_PES_TechCheck_Report_EN.md*
