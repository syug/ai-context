# FY27 OP1 FAQs -- APAC/MENA Draft v1

**Date:** 2026-03-09
**Author:** Saito Shugo (TEX APAC)
**Note:** This draft covers the APAC/MENA column. APAC = AU + JP (primary); MENA = supplementary (not Shugo's direct scope). Mirko will integrate into the unified narrative.

---

## Q1: What are the key initiatives you're prioritizing this year and why?

**Sufficiency:** Sufficient

We are prioritizing three interconnected initiatives for APAC in FY27:

1. **Prime Video Ad Innovation** -- Building new ad experiences around PV content, including Second Screen Experience (SSE) via Curated Collection Pages, audio fingerprinting-based content sync, and exploring Sterling/X-Ray integrations as they become available in AU. PV Sponsorship drove 97% margin globally in FY25 and AU PV revenue doubled YoY to $4.8M, making this our highest-ROI innovation surface.

2. **Live Sports API Enablement** -- Unlocking PV Sports Data Platform (SDP) for BIL Pods globally via Brand Gateway integration. AU alone estimates $400K/yr (NBA-focused), EU Endemics $3MM/yr. Currently navigating a 2-layer blocker: technical access is open but commercial licensing is editorial-only, requiring PV BD negotiation.

3. **AI-Powered Operational Efficiency** -- Deploying AI tools to address the scoping/proposal bottleneck identified in our FY26 Pod survey (67% response rate, 8/12 members). Key prototypes include an AI Scoping & Feasibility Assistant (Tier 1), Tech Concept Idea Repository for JP BIL's pre-sales needs, and a "Repository of Skills/MCPs" for standardized AI tooling across the Pod.

**Why these three:** They align with the L10 Kingpin evaluation criteria (Ad Innovation weighting), address the top pain points from our survey (PV integration depth, scoping inefficiency, canvas constraints), and leverage APAC's unique position as the first non-US market for several PV features.

**Sources:** context-gathering.md, bil-op1-planning-fy27, tex-prime-video-sse-initiative, tex-survey-analysis, prototype-ideation-research, live-sports-api-discovery
**Gaps:** None significant -- well-covered across multiple handovers.

---

## Q2: What lessons from last year are you using to inform decisions this year and in FY27?

**Sufficiency:** Sufficient

Four key lessons from FY26 are shaping our FY27 approach:

1. **Tier 2 > Tier 1 for revenue efficiency (AU):** AU BIL's OP1 brainstorm concluded that Tier 2 sponsorships ($500K avg, scalable to $700K-$1M) deliver better ROI than chasing Tier 1 mega-deals. This shifts our brief-first approach and directly impacts which prototypes we prioritize (scalable, reusable experiences over bespoke builds).

2. **Agency-originated opportunities underperform:** 95% of PV deals come through media agencies, but success rates are low. FY27 will focus on brand-direct relationships with senior seller involvement, which correlates with higher close rates.

3. **AU/JP have fundamentally different AI adoption patterns:** Our survey revealed AU leans operational (Title Matcher, scoping tools) while JP leans creative (AI-assisted ideation, Amazon Review experiences). Tool development must respect this divergence rather than force a one-size-fits-all approach.

4. **Cross-org integration is the unlock:** The US Holiday Sponsorship ($42.4MM Pan-Amazon first) proved that BIL + XCM/Retail integration creates outsized value. JP BIL is already pursuing this with XCM collaboration (LEGO Holiday JP+AU, Amazon Beauty Festival $1.2MM). We need to systematize this for APAC.

**Sources:** bil-op1-planning-fy27, tex-survey-analysis, bil-q4-qbr-revenue-analysis
**Gaps:** None -- strong data backing from QBR analysis and brainstorm outcomes.

---

## Q3: What are you choosing NOT to do and why?

**Sufficiency:** Moderate

1. **Not pursuing WebSocket/real-time gaming prototypes** -- Our prototype research concluded that WebSocket-based experiences (e.g., Maltesers Indecision Duel) use existing BIL-E stacks (Brand Gateway MessageRoom) with no technical challenge. Three PARC precedents exist. Innovation value is low; we're redirecting to audio fingerprinting + PV integration, which is first-of-its-kind.

2. **Not chasing agency-originated PV opportunities (AU)** -- Per AU OP1 decision. Success rate is too low and consumes disproportionate time.

3. **Not building AI models for audio content matching** -- Research showed traditional DSP (Shazam-style fingerprinting) outperforms AI for exact content+timestamp identification. AI is better at "what is this sound" but worse at "which recording at which position." We're using Olaf (WASM, browser-compatible) instead.

4. **Not investing in MENA-specific prototypes** [TBD] -- MENA BIL revenue is $1.2M (0.18% of WW). Until the market scales, APAC TEX resources are best allocated to AU/JP where impact is measurable.

**Sources:** prototype-ideation-research, bil-op1-planning-fy27
**Gaps:** MENA "not to do" rationale needs Mirko's input -- we don't have MENA OP1 planning data yet. [requires confirmation]

---

## Q4: What are the biggest risks to achieving your plan?

**Sufficiency:** Moderate

1. **PV Live Sports API licensing deadlock:** The commercial licensing layer (PV BD, Jonathan Yi) is currently editorial-only. If we can't negotiate commercial use rights, the Live Sports API initiative stalls. Mitigation: Chicken-and-egg avoidance -- build PoC under editorial/internal use, then negotiate per-campaign. Bindu sync scheduled 3/11.

2. **PV technical team access bottlenecks:** Multiple SSE opportunities (Title Pages, X-Ray, Sterling AU rollout) are blocked pending technical team introductions from Sean Dylke. CMS/content delivery details remain opaque. Mitigation: Curated Collection Pages (most accessible) as the first entry point.

3. **MENA Pod engagement gap:** Zero survey responses from MENA (aayuda, hmmushah). Tier decisions without MENA input are incomplete per our multi-agent review. Mitigation: Direct outreach planned but not yet executed.

4. **JP BIL early-stage pipeline:** JP PVS is still at 1-pager stage (Mariko/Shun), not yet flowing to ADs. Brand Sponsorship/XCM collaboration is in business conversation stage. Tech intervention may be premature. [requires confirmation -- Mariko's latest status needed]

5. **Resource allocation tension:** Discovery target of 8 prototypes/person/year vs. campaign delivery demands. JP currently has slight resource surplus in Core BIL, but this shifts as PVS ramps.

**Sources:** live-sports-api-discovery, tex-prime-video-sse-initiative, tex-survey-analysis, au-bil-pv-growth-engagement
**Gaps:** JP pipeline risk assessment is based on 3/4 data -- needs refresh. MENA risks are largely unknown.

---

## Q5: How are you using GenAI to move faster?

**Sufficiency:** Moderate

1. **Multi-agent review workflow for strategic planning:** We used Claude + Gemini + Kiro (Amazon Q) to cross-validate our FY26 Pod survey analysis, catching single-model biases and producing a more robust prototype prioritization. This surfaced 6 new pain points and 2 new prototype candidates that a single-model analysis missed.

2. **AI Scoping & Feasibility Assistant (Tier 1 prototype):** Addressing the #1 operational pain point (scoping/proposal bottleneck). Converts creative ideas to feasibility assessments and proposal drafts. AU has existing tools (Title Matcher V1) to extend; JP requires greenfield build.

3. **"Repository of Skills/MCPs" concept (from Shun Akeda):** Standardizing AI tool configurations across the Pod while allowing personal optimization. Addresses the "everyone uses different tools differently" problem. [requires confirmation -- not yet scoped as a formal prototype]

4. **Tech Concept Idea Repository (JP request):** Mariko's #1 ask -- a deployable concept repository for PV campaign ideas to reduce pre-sales lead time. Combines AI curation with historical campaign data.

5. **Session-level GenAI for operational work:** Using Claude Code for context synthesis, handover management, multi-source research, and document drafting (e.g., this FAQ itself). [requires confirmation -- how much to disclose about personal tooling]

**Sources:** tex-survey-analysis, prototype-ideation-research
**Gaps:** Missing concrete metrics on time savings. No formal measurement of GenAI impact yet. EU comparison data would strengthen this answer. "MiK complement" framing (from AU OP1 Topic 4 prep) is ready but Topic 4 discussion hasn't happened yet.

---

## Q6: What assumptions is your plan based on?

**Sufficiency:** Thin

1. **PV content slate remains strong in APAC:** AU expects S2 release clusters, NRL acquisition negotiation ($200M ask), Tomb Raider, God of War. Full-year content slate to be received in 1-2 months. If content pipeline weakens, PV sponsorship opportunities shrink proportionally.

2. **Sterling and SSE features will roll out to AU as planned:** Sean Dylke indicated Sterling is on AU's roadmap "this year" but this is unconfirmed. Our PV ad innovation plan depends on these features becoming available.

3. **BIL-E will support Live Sports API integration:** Bindu's team requires multi-Pod justification. We're building the business case ($400K AU + $3MM EU + US PoC), but BIL-E intake approval is not guaranteed.

4. **APAC ad market continues to grow:** AU Amazon Ads projected to reach $400M total. BIL AU doubled YoY to $4.8M in FY25. We assume this trajectory holds. [requires confirmation -- FY27 specific targets from leadership]

5. **Team composition remains stable:** JP BIL has one member on extended leave (jifuruya). We assume no further attrition. [requires confirmation]

6. **60/40 Ad Innovation vs Ops Efficiency split is endorsed:** Our recommended resource allocation. Not yet validated by leadership. [requires confirmation]

**Sources:** bil-op1-planning-fy27, au-bil-pv-growth-engagement, live-sports-api-discovery, bil-q4-qbr-revenue-analysis
**Gaps:** No FY27-specific revenue targets for APAC. PV content slate not finalized. Sterling AU timeline unconfirmed. Leadership endorsement of 60/40 split pending. This is the weakest answer -- mostly directional assumptions without hard commitments from stakeholders.

---

## Q7: How will you measure success of your team, product, or program?

**Sufficiency:** Thin

1. **Prototype impact (Kingpin #1078451):** Number of prototypes shipped, prototype-to-production conversion rate, and revenue attributed to prototype-enabled campaigns. Target: maintain 8 prototypes/person/year Discovery pace. [requires confirmation -- exact Kingpin metrics]

2. **PV Sponsorship revenue growth (APAC):** AU PV from $3.2M toward $4.3M target. JP PVS Tier 1 campaign closure (at least 1 per Mariko's goal). [requires confirmation -- FY27 specific targets]

3. **Ad Innovation vs Ops Efficiency KPI separation:** Per multi-agent review recommendation, track Ad Innovation impact (revenue attribution, campaign wins enabled) separately from Ops Efficiency impact (time saved, throughput increase). Framework defined but KPIs not yet formalized. [requires confirmation]

4. **Pod survey follow-up scores:** Measure improvement in identified pain points (scoping inefficiency, canvas constraints, PV integration depth) in a mid-year pulse check.

5. **Live Sports API adoption:** Number of Pods with active API access, campaigns using live data, incremental revenue from sports-data-enabled experiences.

**Sources:** tex-survey-analysis, bil-op1-planning-fy27, bil-q4-qbr-revenue-analysis
**Gaps:** No concrete FY27 APAC KPI targets. Kingpin evaluation criteria details missing. Need leadership input on success metrics. This answer needs the most work -- we have frameworks but not numbers.

---

## Q8: What dependencies do you have on other teams?

**Sufficiency:** Sufficient

1. **PV Core SEA/ANZ Growth (Sean Dylke):** Technical team introductions for Title Pages, X-Ray, Sterling. CMS/content delivery understanding. Sterling AU rollout timeline confirmation. Currently waiting on Sean's follow-up.

2. **SDP Core (Anand Kumaravel) / PV BD (Jonathan Yi):** Live Sports API technical access and commercial licensing. The 2-layer problem (tech access = open, commercial license = editorial only) requires coordinated resolution. Bindu sync 3/11.

3. **BIL-E (Bindu/Harish):** Brand Gateway integration for SDP. BIL-E requires multi-Pod business justification before intake. Relationship managed through Bindu.

4. **XCM (Jo Shoesmith org):** Cross-org sponsorship integration (Pan-Amazon model). JP BIL already engaging (Mariko, 3/3 XCM member involvement). AU exploring similar approach.

5. **BPS/Twitch (Chris Ott, Melbourne):** Now under BIL umbrella (since Aug 2025 integration). Coordination on seller incentive models and specialist seller placement for PV.

6. **STS (ikejannaI):** STS Proxy API APAC availability is the sole remaining blocker for SSE initiative. Status: not yet contacted.

**Sources:** live-sports-api-discovery, tex-prime-video-sse-initiative, au-bil-pv-growth-engagement, bil-op1-planning-fy27
**Gaps:** STS APAC status completely unknown. ikejannaI contact not initiated. Otherwise well-documented.

---

## Q9: What are your top "paper cuts" and what are you doing to solve them?

**Sufficiency:** Moderate

1. **Scoping/proposal pipeline bottleneck:** The idea-to-proposal conversion is slow and manual. Multiple survey respondents flagged this. Solution: AI Scoping & Feasibility Assistant (Tier 1 prototype, Q1-Q2 target). AU can extend existing Title Matcher V1; JP needs greenfield build (6-12 month timeline difference).

2. **New ad product/tech awareness gap in BIL Pods:** Shun Akeda (JP CD) flagged that BIL teams don't have visibility into new advertising capabilities (Interactive Video Ads, etc.) early enough to incorporate into proposals. Solution: Tech Concept Idea Repository + regular TEX-to-BIL briefings. [requires confirmation -- format not yet defined]

3. **PV API access opacity:** Getting access to PV data (metadata, live sports, content schedules) requires navigating multiple teams and approval layers. No single entry point exists. Solution: Live Sports API Discovery is the first systematic attempt to map and unlock these APIs.

4. **Canvas constraints differ by market:** AU has no Fire TV ad support, making 2nd Screen the only PV integration canvas. JP has different constraints. Global standard experience design is difficult. Solution: Market-specific prototype tracks rather than one-size-fits-all.

5. **MENA information gap:** Zero Pod survey responses, no OP1 planning input. TEX cannot effectively serve a market it has no signal from. Solution: Direct outreach to aayuda/hmmushah (Slack messages drafted but not yet sent). [requires confirmation -- escalation path if no response]

**Sources:** tex-survey-analysis, prototype-ideation-research, live-sports-api-discovery
**Gaps:** Paper cuts #2 and #5 have identified problems but underdefined solutions. Need more concrete action plans.

---

## Q10: What "dogs not barking" worry you and how are you proactively addressing them?

**Sufficiency:** Thin

1. **JP BIL revenue decline (-16% YoY):** JP BIL dropped from positive growth to -16% in FY25 while every other region grew. This isn't being loudly discussed but is a structural concern. JP PVS is still at 1-pager stage and the "Sales Struggle + licensee problem" Mariko flagged for Live Sports suggests deeper go-to-market challenges. Proactive: TEX is embedding earlier in JP pre-sales (Idea Repository, PVS ideation support) to improve win rates.

2. **Twitch/BPS revenue decline (-14% YoY):** Twitch Ads revenue is trending down globally. BPS was integrated into BIL in Aug 2025, but the revenue trajectory hasn't improved. If this continues, BIL's non-PV revenue base erodes. Proactive: [requires confirmation -- no specific APAC Twitch strategy identified]

3. **PV Sponsorship concentration risk:** PV Sponsorship grew 795% YoY to $265M at 97% margin -- it's now 42% of WW BIL revenue. APAC's plan is heavily PV-weighted. If PV content quality or subscriber growth stalls, this entire strategy is exposed. Proactive: maintaining Core BIL + XCM/Retail diversification as a hedge.

4. **Discovery target vs. business impact disconnect:** 8 prototypes/person/year is a throughput metric, not an impact metric. The evaluation criteria for what constitutes "business impact" are unclear (Mariko flagged this). If leadership shifts to outcome-based measurement, throughput-optimized teams may underperform. Proactive: proposing Ad Innovation vs Ops Efficiency KPI separation framework.

5. **GenAI backlash in creative teams:** AU OP1 prep identified that some team members (Luke, MiK) have reservations about AI replacing creative work. The "MiK complement" framing is prepared but Topic 4 discussion hasn't happened yet. If not managed, AI adoption in the Pod stalls. [requires confirmation -- Topic 4/5 outcomes needed]

**Sources:** bil-q4-qbr-revenue-analysis, bil-op1-planning-fy27, tex-survey-analysis, live-sports-api-discovery
**Gaps:** This is the most speculative answer. Dogs-not-barking by nature require inference. JP revenue decline root cause is not well-understood. Twitch strategy is absent. Need Mirko's global perspective to validate these concerns.

---

## Summary: Input Sufficiency Matrix

| # | Question | Sufficiency | Primary Sources | Gaps |
|---|----------|-------------|-----------------|------|
| 1 | Key initiatives | **Sufficient** | All 8 sources | None |
| 2 | Lessons from last year | **Sufficient** | bil-op1, survey, qbr | None |
| 3 | NOT doing | **Moderate** | prototype-ideation, bil-op1 | MENA rationale missing |
| 4 | Biggest risks | **Moderate** | live-sports, sse, survey | JP pipeline freshness, MENA unknown |
| 5 | GenAI usage | **Moderate** | survey, prototype-ideation | No time-savings metrics, Topic 4 undiscussed |
| 6 | Assumptions | **Thin** | bil-op1, pv-growth, qbr | No FY27 targets, Sterling unconfirmed, leadership endorsement pending |
| 7 | Measuring success | **Thin** | survey, bil-op1, qbr | No concrete KPIs/targets, Kingpin criteria unknown |
| 8 | Dependencies | **Sufficient** | live-sports, sse, pv-growth, bil-op1 | STS APAC status unknown |
| 9 | Paper cuts | **Moderate** | survey, prototype, live-sports | Solutions for #2 and #5 underdefined |
| 10 | Dogs not barking | **Thin** | qbr, bil-op1, survey, live-sports | Speculative; JP decline root cause, Twitch strategy absent |

### Priority Actions to Fill Gaps

1. **[Critical] Obtain FY27 APAC revenue targets and Kingpin metrics** -- Q6 and Q7 cannot be finalized without these. Source: Mirko or Chris Wilson.
2. **[High] Confirm AU OP1 Topic 4/5 outcomes** -- Q5 (GenAI) and Q10 (AI backlash) need the results. Source: next AU OP1 session.
3. **[High] Get JP OP1 input** -- Q4 (JP pipeline risk), Q6 (JP assumptions), Q10 (JP revenue decline) are all thin on JP-specific strategy. Source: Mariko/Shun.
4. **[Medium] Collect MENA signal** -- Q3 (not doing), Q4 (risks), Q9 (paper cuts) all note MENA gap. Source: aayuda/hmmushah outreach.
5. **[Medium] Sterling AU timeline confirmation** -- Q6 assumption #2. Source: Sean Dylke follow-up.
6. **[Low] GenAI time-savings data** -- Q5 would benefit from quantified impact. Source: internal measurement.
