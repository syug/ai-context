# Ellis Blueprint CX Constructs — Research Notes for AU PES Tech Check

**Date:** 2026-03-04
**Context:** Additional research during AU PES Tech Check V2 review

---

## Overview

This document summarizes research into Amazon's Ellis Blueprint CX Constructs, the relationship between LWA and Amazon Pay, and implications for the AU Prime Early Screenings (PES) project with Event Cinemas.

## Ellis CX Pattern Comparison

Ellis offers 6 Out-of-the-Box (OOB) Blueprint CX Constructs:

| # | Pattern | Integration Depth | 3P API Integration | Representative Partner | Launch |
|---|---------|-------------------|--------------------|-----------------------|--------|
| 1 | Online Offers | Deep | LWA + Ellis API | Grubhub+, Calm, Deliveroo | 2021/7 |
| 2 | Partner Promotions | Lightest | None (promo code/URL distribution) | LinkedIn, Uber | 2022/5 |
| 3 | Prime Offer Code (Transactional) | Light | Ellis API only (Verify + Redeem) | **Odeon Cinemas (UK)**, Peet's Coffee | 2023/12 |
| 4 | Prime Offer Code (Account Linking) | Medium | LWA + Ellis API | Subscription-type offers | — |
| 5 | Pre-Verification | Medium | LWA + Ellis API | UNiDAYS | 2022/5 |
| 6 | Embedded Store | Deepest | Amazon Pay + Ellis API + custom endpoints | **Grubhub** | 2024/5 |

## LWA vs Amazon Pay — No Dependency

**LWA (Login with Amazon)** and **Amazon Pay** are completely independent services.

- LWA = OAuth 2.0 authentication service (Identity Services team)
- Amazon Pay = Payment service
- Amazon Pay historically used LWA for authentication (not the reverse)
- Amazon Pay's internal "LwA Decoupling" project (2017) actively separated them further

### Amazon Pay Requirement by Pattern

| Pattern | Payment Location | Amazon Pay Required |
|---------|-----------------|---------------------|
| Online Offers | 3P site (3P's own payment) | No |
| Partner Promotions | 3P site (3P's own payment) | No |
| Prime Offer Code | Physical store or 3P site | No |
| Pre-Verification | Amazon site (Prime subscription) | No |
| **Embedded Store** | **Inside Amazon app** | **Yes** |

**Only the Embedded Store CX requires Amazon Pay.**

## Embedded Store CX Deep Dive (Grubhub)

### What It Is

The Embedded Store CX embeds a 3P's entire web experience inside the Amazon app (mShop / Amazon.com). Technically uses iOS Safari View Controller (SVC) and Android Chrome Custom Tab (CCT) to overlay the 3P web experience within the Amazon app.

### User Flow

1. Customer selects "Dining/Restaurants" in Amazon app
2. Ellis co-branded landing page explains Prime benefits
3. **Amazon Pay SSW (Sign-in & Setup Wallet)** consent screen appears:
   - Prime status sharing consent
   - Amazon account info sharing consent
   - Amazon Pay wallet setup (payment method configuration)
   - SSO: no additional login needed if already signed into Amazon app
4. Grubhub retrieves buyer info via Amazon Pay API
5. Grubhub checks Prime eligibility via Ellis Benefits Discovery API
6. Grubhub auto-creates account, activates offers
7. Customer browses restaurants, selects items
8. **Checkout via Amazon Pay** — uses existing Amazon wallet payment methods
9. Order tracking available within Amazon app

### Why Amazon Pay Is Required

Amazon Pay in Embedded Store CX is not just payment — it's a **unified authentication + consent + wallet + payment** layer:

- **Unique pattern**: Only CX where customers purchase 3P products without leaving the Amazon app
- **SSW unification**: Originally was 2-step (LWA consent → Saved Wallet consent) causing drop-off; unified into 1 screen
- **Saved Wallet**: Enables repeat purchases with stored Amazon payment methods

## PES Implications

### Key Discovery: Odeon Cinemas (UK) Precedent

**Odeon Cinemas (UK cinema chain) launched with Prime Offer Code (Transactional) in December 2023.** This is a direct precedent for cinema + Prime integration.

### Pattern Suitability for PES

| Pattern | PES Fit | Rationale |
|---------|---------|-----------|
| **Prime Offer Code (Transactional)** | **Best** | Odeon (UK cinema) is a direct precedent. Per-transaction Prime verification. Barcode/code for POS or online. No LWA required. 4-6 week integration. |
| LWA + PrimePass (Fandango model) | Good | Proven in US PES. Higher integration cost than Offer Code. |
| Embedded Store | Poor | Integration cost extremely high. Overkill for PES use case. Requires Amazon Pay (unavailable in AU). |

### Impact on V2 Report Recommendations

The V2 report currently ranks:
- Priority 1: LWA + Prime Ellis (Fandango model)
- Priority 2: Ellis Prime Offer Code CX (ODEON model)

Given that **Odeon Cinemas is a direct cinema precedent** with lower integration cost and faster timeline, the priority ranking may warrant re-evaluation.

### V2 Report Corrections Needed

1. **Task 2 constraint table** (Impact column):
   - Current: "Cannot directly replicate the US Fandango model"
   - Should be: "Ellis Embedded Store CX (Grubhub model) cannot be used in AU. Does NOT affect recommended approaches (LWA + PrimePass or Offer Code CX)."

2. **Key Risks section**:
   - Current: "Amazon Pay is not available in AU, limiting certain integration patterns"
   - Should be: "Amazon Pay is not available in AU, preventing use of the Ellis Embedded Store CX (Grubhub model). Does NOT affect the recommended approaches."

## Sources

- [Ellis Blueprint CX Constructs](https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/BlueprintCXConstructs/)
- [Ellis GES (Grubhub Embedded Store) Design](https://w.amazon.com/bin/view/PrimeTeam/Ellis/Projects/GES/)
- [Amazon Pay Prime Ellis Program](https://w.amazon.com/bin/view/AmazonPay/PrimeEllisProgram/)
- [Ellis Main Wiki](https://w.amazon.com/bin/view/PrimeTeam/PrimeOffAmazon/Ellis/)
- [LWA Products](https://w.amazon.com/bin/view/IdentityServices/Products/LWA/)
- kellypru DM (2026-03-03) — US PES uses LWA + Prime Ellis
