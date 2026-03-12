# AU Prime Early Screenings -- Tech Check Summary

**Date:** 2026-03-11
**Prepared by:** Shugo Saito (DT)
**Intake:** ENT | AU | Prime Early Screenings | Australia Pilot (T2, DT Resource)

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
| Task 1. US PES User Flow & Technical Review | **Reviewed** | LWA-based integration |
| Task 2. AU Prime Authentication Feasibility | **Feasible (pending confirmations)** | LWA confirmed for AU (FE region) |
| Task 3. Event Cinemas Proposal | **Reject** | 2 Critical risks: pre-shared key exposure + MemberId PII leakage |

### Recommended Approach

**LWA (Login with Amazon)** -- OAuth 2.0 standard, proven in US PES.

**Pending confirmation (Hannah Hill):**

- End-to-end steps taken in US PES
- How to engage the Prime Ellis / LWA teams

### Next Steps

- **Contact Hannah Hill (hannahnl)** -- Confirm the end-to-end steps taken in US PES and how to engage the Prime Ellis / LWA teams
- **Ads Security Engineer validation** -- Sunit Guldas (gulsunit) gut check on Task 3 SHA256 Critical findings (Slack DM sent, awaiting response)

---

## Task Details

### Task 1: US PES User Flow & Technical Review

- US operates with Fandango as the ticketing partner
- User flow: Brand Store → Fandango redirect → LWA Prime authentication → ticket purchase
- Fandango/Atom performed LWA integration with support from the Prime Ellis and LWA teams
  - (*) No authentication implementation required on the DT side
- Hannah Hill (hannahnl, US PES Program Lead) led this process

### Task 2: AU Prime Authentication Feasibility

- LWA is confirmed for AU (FE region: JP, SG, AU) (*)
  - (*) Whether PrimePass (`prime:benefit_status` scope) works in AU needs confirmation
- 3P Prime authentication may require engagement with the Prime Ellis team
  - (*) PBS Onboarding Wiki states "Third Party Integration should go through Prime Ellis"

### Task 3: Event Cinemas Proposal Gut Check

- Evaluated Event Cinemas' proposed SHA256-based authentication method
- **Critical 1:** Pre-shared key exposure -- violates Amazon key management policy; key leakage enables full forgery
- **Critical 2:** MemberId PII leakage -- Amazon internal customer identifier exposed directly to external party (LWA uses Directed ID for protection)
- **Conclusion:** Rejected. However, this does not reject Event Cinemas as a partner -- counter-proposing a switch to LWA-based integration
- Formal gut check by Ads Security Engineer (Sunit Guldas) awaiting response

---

## Key Contacts

| Role | Name | Context |
|------|------|---------|
| US PES Program Lead | Hannah Hill (hannahnl) | Entry point for Ellis/LWA teams |
| US DT (validated) | Kelly Prudente (kellypru) | Confirmed US PES technical details |
| Ads Security Engineer | Sunit Guldas (gulsunit) | SHA256 gut check (DM sent, awaiting response) |
