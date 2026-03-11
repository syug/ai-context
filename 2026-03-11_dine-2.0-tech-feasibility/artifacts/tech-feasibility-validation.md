# Mars Dine 2.0 — Tech Feasibility Validation

| | |
|---|---|
| **Project** | Mars Dine 2.0 — "Ignored to Adored" 2026 Campaign |
| **Brief** | Dine 2.0 Ignored to Adored V3.pptx (31 slides) |
| **Author** | Chris Wilson, Head of Brand Innovation Lab ANZ |
| **Validation Date** | 2026-03-11 |
| **Status** | Presented to client, awaiting feedback |

---

## Background / Timeline

1. **2025**: Mars Dine "Cat Decoder" campaign — successful launch establishing the "Ignored to Adored" brand platform. Interactive tool that decoded cat behavior and directed owners to Dine meals.

2. **2026 planning (Agency phase)**: Mars Inc. x Publicis developed an initial concept called **"Amazon Dine Video" / "pspspsuedoscience"** (17-slide PDF brief). The agency proposed a premium Prime Video partnership that would embed cat-attracting sounds (pspsps noises, jingles, purrs, meows) directly into Prime Video content as an alternate audio track — essentially a "cat-friendly audio option" similar to choosing a different language. The concept included:
   - A curated "cat-friendly genre" section within Amazon Prime (BTYB branded row)
   - Interactive pre-roll ads inviting cat owners to opt in to the cat-friendly audio
   - PR amplification via a 12-day connection challenge
   - Extensions: Prime sign-ups unlocking free 12 days of Dine; exclusive Amazon Music channel with cat-loved sounds
   - Amplification: First impression takeover, sponsorship alignments for specific titles, QR-enabled "paws ads"

3. **Agency ideas rejected by AU BIL** — Luke Thistleton (AU BIL Creative Lead) provided the following feedback to the agency (Warren & Leah at Publicis), shared via Slack DM on 2026-02-10:

   **Strategic reason (primary):** *"The 'cat-dubbed media' idea essentially reverses [the Cat Decoder] logic. It isn't solving a cat-owner problem or demonstrating the product; it's a novelty mechanic that momentarily amuses humans while stimulating the cat. The brand becomes a sponsor of a trick rather than the cause of a behavioural outcome. One idea makes the food the reason the relationship improves; the other makes the ad the entertainment and the product incidental, so it generates attention but not belief."*

   **Technical reason (secondary):** *"Re executions: this could only be achieved in the form of an ad i.e. a filmed TVC. Currently no capability to incorporate audio directly into the platform in these ways."*

4. **Cat Decoder re-run considered** — team discussed re-running the 2025 Cat Decoder for 2026.

5. **New ideas developed** — final decision to create fresh concepts, resulting in 3 ideas in "Ignored to Adored V3."

6. **2026-03-11**: Presented to client by AU BIL creative team.

7. **Current**: Awaiting client feedback.

> **Note**: The agency's "pspspsuedoscience" concept shares significant DNA with BIL's Idea 03 ("Dinner and a Show") — both center on cat-attracting audio during Prime Video viewing. BIL's version pivoted from embedding audio in PV content to a second-screen companion experience, which is more technically feasible.

---

## 2026 Strategic Shift

| 2025 | 2026 |
|------|------|
| Cat Decoder: "Ignored to Adored" at **feed-time** | Extend adoration **beyond mealtime** |
| Dine helps owners *read* their cats | Dine helps owners *feel closer* to their cats |
| Interpreting connection | Enabling connection |

---

## Three Ideas Overview

| | Idea 01: Cat Love Keyboard | Idea 02: Adore Des Chats | Idea 03: Dinner and a Show |
|---|---|---|---|
| **Concept** | 90s love-ballad digital keyboard for composing cat serenades | Limited-edition fragrance to win cat affection via Pavlovian conditioning | Second-screen audio bath for cats while watching Prime Video |
| **Core Tech** | Web Audio API, Brand Store | Physical product manufacturing, Brand Store | Second-screen sync, Web Audio API |
| **Science** | David Teie species-specific music research | Silver Vine, Valerian Root, Catnip (olfactory) | Feline acoustic research (auditory) |
| **Commercial Hook** | Shared tracks earn discount for 12-Day Dine Meal Challenge | Fragrance free with challenge completion | Longer usage unlocks Dine discounts |

---

## Idea 01: Cat Love Keyboard — "Music to move your feline friend"

### Brief Summary

A 90s slow-jam love-ballad-inspired digital keyboard (mobile web experience at Amazon.com/DineKeyboard) that lets owners compose personalised serenades for their cat. Built on actual research into species-specific music for cats (David Teie, *Applied Animal Behaviour Science*).

### Mechanics (from brief)

1. Visit Amazon.com/DineKeyboard; phone becomes the Cat Love Keyboard
2. Select backing track, layer cat-appealing sounds (purr loops, bird chirps, Dine can opening sound)
3. Play live for the cat, save, share back to Dine brand store
4. Shared tracks earn a discount code for the 12-Day Dine Meal Challenge
5. Shared tracks contribute to a Dine Cat Love Playlist on Amazon Music, promoted via Amazon Alexa

### Science (from brief)

Based on David Teie research — rhythm based on cat biology (purring vibrations, suckling rhythms, grooming patterns), sliding pitches matching cat vocalisations, frequency range of 300-3,000Hz matching feline vocal range, familiar life sounds (purring, grooming, bird chirps).

### Creative Territory

90s love-ballad nostalgia. Potential fictional mascot "Meow-ceal Bolton" with a Russian Blue cat. Works across TikTok/Reels (sound-on environments), influencer content, Prime Video media, Amazon DSP, custom brand store.

### Overall Feasibility: Yellow

Core interactive keyboard (Web Audio API + Brand Store) is **Green**. Amazon Music UGC pipeline is a **Red** blocker.

### Key Risks

| Risk | Severity | Detail |
|------|----------|--------|
| Amazon Music UGC pipeline | Red | No mechanism exists for user-generated audio to enter Amazon Music playlists. All existing cases (Vitaminwater, Cocktail Cabinet) use pre-curated playlists only |
| iOS WebView audio | Yellow | WKWebView requires user gesture for AudioContext initialization. Solvable with UX design ("tap to start") |
| Cross-team dependencies | Yellow | BIL-E + Amazon Music + Alexa + Promotions — each adds timeline risk |
| Mobile audio latency | Yellow | Low-end Android devices may introduce 50ms+ delay. Keyboard tap-to-sound interaction demands low latency |
| ANZ Brand Store | Yellow | All found precedents are US/UK/EU/JP. Custom Brand Store experience on amazon.com.au needs verification |

### Arc/Parc Precedents

| Campaign | Relevance | Link |
|----------|-----------|------|
| **Ad Council "When You Can't Say It, Play It"** | Closest conceptual match — users shared songs via Amazon Music + Alexa, 2.6M shares. Award-winning. **Key difference:** users selected songs from Amazon Music's **existing 100M-track catalog**; no user-generated audio was uploaded to Amazon Music. Validates "Amazon Music as campaign channel" but NOT "UGC audio ingestion" | [Arc](https://console.harmony.a2z.com/arc/#/campaigns/ad-council-when-you-cant-say-it) |
| **Coca-Cola Holiday Second Screen Sync** | React app with audio context management (background music + sound effects) on Brand Store. Directly proves Web Audio API works in BIL infrastructure | [Parc](https://console.harmony.a2z.com/parc/#/prototypes/bil-second-screen-sync) |
| **Vitaminwater Sonic Nourishment** | Product scan unlocking branded Amazon Music playlists per flavour. **Key difference:** playlists were **pre-curated from existing catalog**, not populated by user-generated content. Validates branded playlist concept but not UGC contribution | [Arc](https://console.harmony.a2z.com/arc/#/campaigns/vitaminwater-sonic-nourishment) |
| **Calma Zampa Alexa Skill** | Pet-focused Alexa skill (dogs) that plays calming music playlists. Lambda+S3+CloudFront architecture. Relevant as pet-wellness + audio + Alexa precedent | [Parc](https://console.harmony.a2z.com/parc/#/prototypes/alexa-skill-weather-forecast) |
| **Iris Plaza Packed Rice 2.0** | Second-screen FTV with interactive quiz leading to discount coupon code on Brand Store. Proves interaction-to-coupon-code pipeline. +265% purchase conversion | [Arc](https://console.harmony.a2z.com/arc/#/campaigns/iris-plaza-packed-rice-1) |

### Component Assessment

| Component | Feasibility | Notes |
|-----------|------------|-------|
| Mobile web audio keyboard (Web Audio API) | Green | Well-supported. Coca-Cola prototype validates audio in Brand Store React apps |
| Brand Store hosting | Green | Strongly validated across multiple campaigns. Custom slug (amazon.com/DineKeyboard) achievable |
| Sound library (purr loops, chirps, can opening) | Green | Pre-recorded samples via Web Audio API. Host on S3/CloudFront |
| Save & share compositions | Yellow | URL-encoded recipe approach avoids server-side audio rendering and moderation |
| Amazon Music playlist integration | Yellow | Pre-curated playlist: validated. UGC contribution to playlist: **blocked** |
| UGC-to-Amazon Music pipeline | Red | No mechanism exists. Requires distributor/label partnership for content ingestion |
| Alexa integration | Yellow | Custom Skill (4-6 weeks) or Alexa Theme (lighter, faster). Verify AU locale support |
| Discount code generation | Green-Yellow | Validated by Oral-B and Iris Plaza. Requires Amazon Promotions code pool |

### Recommended Pivots

1. **Decouple Amazon Music from UGC** — keyboard experience (Brand Store) and playlist (professionally produced cat music) as separate tracks
2. **Preset sound grid (12-16 sounds)** instead of free synthesis — eliminates moderation, simplifies sharing to URL parameters
3. **Alexa Theme over custom Skill** — Barbie precedent (292K downloads), lighter approval
4. **Phase the build** — Phase 1: keyboard + discount code (no cross-team blockers). Phase 2: Amazon Music curated playlist + Alexa theme

---

## Idea 02: Adore Des Chats — "The fragrance felines can't ignore"

### Brief Summary

A limited-edition fragrance designed to win cat affection, free with the 12-Day Dine Feeding Challenge. Uses classical conditioning (Pavlov's principle) — spray at mealtimes and relaxation moments to build positive scent associations. Custom bottle inspired by the iconic Dine can with gold atomiser spray.

### Key Fragrance Notes (from brief)

1. **Silver Vine (Actinidine):** ~80% of cats respond (including non-catnip responders). Human profile: mild woody, tea-like.
2. **Valerian Root (Actinidine & Valerenic):** Gently stimulates then relaxes cats. Human profile: warm, musky, woody.
3. **Catnip (Nepetalactone):** 50-70% of cats respond strongly. Human profile: soft mint.

### Conditioning Mechanic (from brief)

Spray at mealtimes + relaxation on the couch. Over time, scent becomes associated with the positive anticipation of Dine food, transferring that excitement into affectionate snuggling.

### Creative Territory

Luxury fragrance advertising tropes (tongue-in-cheek French voiceover). Behind-the-scenes content showing fragrance development and cat testing. Works across Prime Video, influencer program, PR, brand store, Amazon DSP.

### Overall Feasibility: Yellow

Digital components (Brand Store, PV, DSP, Influencer) all **Green**. Physical fragrance product is the **Red** risk vector.

### Key Risks

| Risk | Severity | Detail |
|------|----------|--------|
| Product safety | Red | Cats highly sensitive to essential oils. Carrier formulation (alcohol, fixatives, synthetic compounds) needs veterinary toxicology review. Catnip/Silver Vine/Valerian themselves are generally safe |
| Regulatory (APVMA) | Red | Product marketed to affect animal behavior may require registration as veterinary chemical product. Registration timeline: 6-12 months |
| Manufacturing lead time | Red | Custom bottle (Dine can-inspired + gold atomiser) requires industrial design, mold creation, production run. Minimum 12-16 weeks |
| Fulfillment | Yellow | BIL doesn't typically ship physical products. Alcohol-based fragrance may have FBA dangerous goods restrictions |
| Challenge completion tracking | Yellow | No native Amazon mechanism to verify 12-day feeding behavior. Purchase-based proxy is simplest |
| TGA implications | Yellow | If therapeutic claims made (e.g., "calms cats"), TGA classification could be triggered. Pavlovian framing likely avoids this |

### Arc/Parc Precedents

| Campaign | Relevance |
|----------|-----------|
| **Nespresso x The Weeknd Vinyl** | Closest precedent. Limited-edition physical collectible tied to purchase. Brand-produced (not BIL). Distributed via pop-up + sweepstakes. $6.8M campaign |
| **Mars Pedigree Buy 1 Feed 1** | Pet food + purchase-linked mechanic + collective progress tracker on Brand Store |
| **OPTIMUM Product Selector** | ANZ pet food Brand Store campaign. +97% monthly sales |
| **P&G Oral-B Pop-Up Store** | Physical activation + online gamification + progressive discount redemption |
| **Nissan Dare to Defy** | PV brand-funded documentary + BTS content production workflow |

### Component Assessment

| Component | Feasibility | Notes |
|-----------|------------|-------|
| Brand Store custom experience | Green | Well-proven. Challenge tracker, product showcase, fragrance story |
| Prime Video media integration | Green | Standard media buy |
| Content production (luxury ad parody + BTS) | Green | Standard BIL production. French VO parody is creative, not technically complex |
| Amazon DSP + Influencer Program | Green | Standard activation channels |
| 12-Day Challenge tracking | Yellow | Options: purchase-based proxy (simplest), daily check-in (complex), honor system |
| Reward redemption flow | Yellow | Options: promo code to ASIN, external fulfillment via 3PL, sweepstakes for limited quantity |
| Physical fragrance manufacturing | Red | Regulatory, safety, sourcing, and lead time risks. Silver vine primarily sourced from East Asia |
| Fulfillment/logistics | Yellow | Glass bottle = fragile + hazardous material (alcohol content) |

### Recommended Pivots

1. **Limited PR/influencer seeding (50-200 units)** — general challenge completers receive digital reward
2. **Brand (Purina/Nestle) owns manufacturing** — BIL role: creative concept + media + Brand Store. Mirrors Nespresso model
3. **Purchase-triggered challenge** — "Buy Dine 12-pack = challenge complete." Verifiable via purchase data
4. **Sweepstakes for physical distribution** — all completers enter draw for limited-edition fragrance
5. **Start regulatory assessment at pitch stage** — APVMA timeline could derail campaign entirely if delayed

### Regulatory Constraints

- **APVMA**: Product affecting animal behavior may need registration (6-12 months)
- **AICIS**: Cosmetic/fragrance ingredient compliance for Australian market
- **ACCC**: Marketing claims about "winning cat affection" need substantiation
- **Cat welfare**: BTS content showing "cat testing" must comply with animal welfare standards

---

## Idea 03: Dinner and a Show — "Make a date to settle in and snuggle"

### Brief Summary

Evolution of the earlier "PSPSPS" / agency concept, reworked to be more consumer-ready. After feeding their cat Dine, owners watch Prime Video while a second-screen experience on their phone plays a gentle audio bath designed specifically for cats — helping them relax and snuggle.

### Mechanics (from brief)

1. Feed cat Dine, settle in for Prime Video
2. Launch Dine "Dinner and a Show" second-screen experience on phone, place nearby
3. Phone plays cat-specific audio (brief claims sounds above human hearing range, 20kHz+, up to 65kHz for cats — **see critical assessment below**)
4. App auto-adjusts volume/soundscapes dynamically to match the show
5. Longer usage unlocks small discounts on Dine products

### Science Claim (from brief)

Cats hear up to 65kHz (humans max at 20kHz). High-frequency sounds capture cat attention while being inaudible to owners, allowing an uninterrupted shared moment. **Note: This claim is technically problematic — see High-Frequency Audio Assessment below.**

### Creative Territory

"Dinner and a show" as universal dating ritual, reframed for cat-owner relationships. Content angles: awkward first dates, grand romantic gestures, feline "dating experts." Natural influencer integration (cat date nights), Prime Video romantic show integrations.

### Overall Feasibility: Yellow/Red (Yellow with pivot)

Second-screen infrastructure is **Green** with strong precedent. The ultrasonic audio premise (20kHz+) is **physically impossible** on consumer smartphones.

### CRITICAL: High-Frequency Audio Assessment

**The brief claims the phone would play sounds "above human hearing range, 20kHz+, up to 65kHz for cats." This is physically impossible on consumer hardware.**

| Device | Spec Upper Limit | Practical Upper Limit |
|--------|-------------------|----------------------|
| Smartphone speaker | ~20kHz | 12-16kHz |
| TV built-in speaker | ~20kHz | 12-15kHz |
| Amazon Echo (w/ tweeter) | ~20kHz | 18-20kHz |
| Echo Dot | ~20kHz | 15-18kHz |
| Bookshelf speakers | ~20-22kHz | 20kHz |

**Why it fails:**
- Smartphone speaker drivers (7-15mm) cannot vibrate at 20kHz+ with meaningful SPL
- Standard DACs at 44.1/48kHz yield Nyquist max of ~22-24kHz theoretical — speaker can't reproduce even that
- Amplifier design optimized for 100Hz-16kHz, actively filters ultrasonic content
- 65kHz would require 128kHz+ sampling rate and specialized transducers — nonexistent in consumer devices

**What IS possible:**
- **8-18kHz range**: cats hear well, humans 30+ find hard to hear (age-related hearing loss)
- **Cat-sensitive sweet spot (~2-8kHz)**: audible to humans but can be designed as pleasant ambient sound
- **Species-specific music patterns** (Teie/Snowdon research): known calming effects, fully audible to humans

### Key Risks

| Risk | Severity | Detail |
|------|----------|--------|
| Ultrasonic playback | Red | Physically impossible on smartphone speakers. Pitch must be corrected |
| Prime Video sync mechanism | Yellow | No public PV API. Fidelity SSE is closest precedent but still in progress |
| Content licensing | Yellow | Show-specific sync requires licensing arrangements or generic "mood matching" |
| Battery impact | Yellow | Continuous audio + WebSocket. Design for 30-60 min max sessions |

### Arc/Parc Precedents

| Campaign | Relevance | Link |
|----------|-----------|------|
| **Coca-Cola Second Screen Sync** | Direct precedent. WebSocket mobile-to-Fire TV real-time sync via BIL-E MessageRoom package. Production-deployed | [Parc](https://console.harmony.a2z.com/parc/#/prototypes/bil-second-screen-sync) |
| **Fidelity Peek Portfolio SSE** | Closest analog. Second-screen companion synced to PV playback of "The Summer I Turned Pretty." Scene-aware content delivery via SSE. Built by aleckunk (TEX) | [Parc](https://console.harmony.a2z.com/parc/#/prototypes/fidelity-peek-portfolio-sse) |
| **Web Audio Spatialization** | Web Audio API spatial audio prototype. Demonstrates BIL browser-based audio manipulation capability | [Parc](https://console.harmony.a2z.com/parc/#/prototypes/web-audio-spatialization-imme) |

### Component Assessment

| Component | Feasibility | Notes |
|-----------|------------|-------|
| Second-screen mobile experience | Green | Strong precedent: Coca-Cola (deployed), Fidelity SSE (in progress) |
| Prime Video content sync | Yellow | Fidelity SSE demonstrates scene-aware sync. No public PV API — sync likely manual or via audio fingerprinting |
| Dynamic audio adjustment | Yellow | Web Audio API supports real-time manipulation (Spatialization prototype). Challenge: knowing what's playing on PV |
| High-frequency audio (20kHz+) | Red | Physically impossible on smartphone speakers |
| Usage tracking + progressive discount | Yellow | Session tracking straightforward. Discount codes need backend + Promotions integration |
| Brand Store / app hosting | Green | Proven across many campaigns. ADLP deployment avoids App Store |

### Recommended Pivots

1. **Reframe audio concept (mandatory)**: "ultrasonic cat-only audio" becomes "scientifically-designed calming soundscapes optimized for cats." The 8-18kHz range is practical and still less noticeable to adult humans
2. **Mood matching over frame-sync**: user selects genre/mood, cat audio adjusts accordingly. Avoids PV API dependency
3. **Reuse Coca-Cola WebSocket/MessageRoom stack**: production-ready architecture, contact jtransu for handoff
4. **Brand Store Web App**: no App Store approval, QR code on Dine packaging for access
5. **Consider Echo as playback device**: better speaker quality (18-20kHz), Alexa ecosystem integration, natural fit

### Key Contacts for Follow-up

| Area | Alias | Context |
|------|-------|---------|
| Second Screen Sync (Coca-Cola) | jtransu | Built FTV + mobile WebSocket architecture |
| Fidelity PV Second Screen | aleckunk | Building PV companion SSE prototype (TEX) |
| Web Audio Spatialization | graleigh | Built browser spatial audio prototype |

---

## Cross-Idea Comparison

| | Idea 01: Cat Love Keyboard | Idea 02: Adore Des Chats | Idea 03: Dinner and a Show |
|---|---|---|---|
| **Overall** | Yellow | Yellow | Yellow/Red -> Yellow with pivot |
| **Top Blocker** | Amazon Music UGC doesn't exist | Physical product regulatory (APVMA 6-12mo) | Ultrasonic impossible on smartphones |
| **Precedent Strength** | Strong (Ad Council, Coca-Cola, Vitaminwater) | Moderate (Nespresso Vinyl) | Strong (Coca-Cola, Fidelity SSE) |
| **Pivot Difficulty** | Low (decouple UGC from playlist) | Medium (brand owns manufacturing) | Low-Medium (reframe audio concept) |
| **Speed to Market** | Fastest (Phase 1 is digital-only) | Slowest (physical product lead time) | Medium (PV team coordination) |
| **Cross-team Deps** | Medium (Amazon Music, Alexa) | Low-Medium (brand-side heavy) | Medium-High (PV team, BIL-E) |
| **Creative Impact** | High (interactive, shareable) | Very High (tangible, PR-worthy) | High (novel second-screen use) |

### Recommended Priority (Tech perspective)

**Idea 01 > Idea 03 > Idea 02**

- **Idea 01** has the most proven tech stack and fastest path to launch (Phase 1 digital-only)
- **Idea 03** has strong infra precedent but needs audio concept reframe and PV team buy-in
- **Idea 02** has the highest creative impact but physical product introduces regulatory and manufacturing timeline risk that is largely outside BIL's control

---

## Next Steps

- [ ] Await client feedback on which idea(s) to pursue
- [ ] Verify ANZ Brand Store custom experience availability (BIL-E)
- [ ] If Idea 01: Confirm Alexa Theme AU locale support
- [ ] If Idea 02: Engage APVMA regulatory counsel immediately; align with Purina/Nestle on manufacturing ownership
- [ ] If Idea 03: Connect with jtransu (Second Screen Sync) and aleckunk (Fidelity PV SSE); reframe ultrasonic claim in pitch materials
- [ ] All ideas: Confirm Amazon Promotions discount code infrastructure for AU marketplace
