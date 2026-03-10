# ATM Org Research: Which Teams Fall Under PV ATM?

Date: 2026-02-27

## Key Finding Summary

**ATM (Ad-Tech & Monetization) is a UX Design team under Prime Video Experience Design (PVXD), NOT a product/engineering org.** It does not "own" any of the 4 teams in question. The 4 teams belong to entirely different org pillars.

---

## ATM Team Details

- **Wiki**: https://w.amazon.com/bin/view/Prime_Video_XD/ATM/
- **Owner LDAP**: pvux-team
- **Charter**: "Building scalable ad experiences that are simple for advertisers and viewers to adopt, feel integrated with the PV experience, and drive action."
- **Lead**: Sarah Yukes (skepa) - Sr. Manager, Ad-Tech & Monetization (ATM)
  - Reports to: Azim Ali (azimali) - Sr. Manager, UX Design, dept "PV Experience Design"
  - Reports to: Kam Keshmiri (kamyark) - VP, Design, PV
  - Reports to: Mike Hopkins (mikehopk) - SVP, Amazon Video and Studios (reports to Jassy)
- **Team composition**: UX Designers, UX Researcher, Design Program Manager (~8 people)
  - Danita Cook - Principal UX Designer
  - Chris-Anne Correa - Sr. UX Designer
  - Erica Laycock - Sr. UX Designer
  - Glenn Cho - Sr. UX Designer
  - Taylor Silva - Sr. UX Designer
  - Christine Kim - UX Designer
  - Isaac Kaufman - Sr. UX Researcher
  - Trashawn Brent - Sr. Design Program Manager

**ATM is the design/UX arm** that works on ad-related CX for Prime Video. It is NOT a product + engineering org that owns products.

---

## The 4 Teams Assessment

### 1. STS (Shop the Show) -- NOT under ATM

- **Betty Tso** (bettyt): Sr.SDM, Shop-the-Show
  - Dept: "Amazon Live - Tech" (#7963)
  - Reports to: John Katsavrias (katsavri) - Director, Software Development
  - Reports to: Wayne Purboo (wpurboo) - **VP, Amazon Shopping Video**
  - Reports to: **Paul Kotas (kotas) - SVP Ads, IMDb, Grand Challenge**
- **Shashank Jain** (shjain): Principal PMT, Shop-the-Show
  - Dept: "Amazon Live - Tech" (#7963)
  - Reports to: Betty Tso (bettyt)
- **Wiki ownership**: amazonshoppingvideos-team (LDAP), gme-shopping-data (POSIX)
- **Org**: Under Paul Kotas (Ads SVP), NOT under Mike Hopkins (PV SVP)
- **Partners listed on STS wiki**: Amazon Ads, Prime Video Shopping, PV Sports Marketing, Amazon Live, Amazon Fast Channel

### 2. IVA (Interactive Video Ads) -- NOT under ATM

- **Wiki**: https://w.amazon.com/bin/view/AdSales/GVA/Products/InteractiveVideoAds/
- **Owner LDAP**: ad-sales-wiki-admins
- **Path**: AdSales > GVA > Products > InteractiveVideoAds
- **Support channel**: #interactive-video-ads-support
- **SIM resolver group**: "Interactive Creative"
- **Org**: Under Ad Sales / GVA (Global Video Ads) organization
- This is part of the broader Amazon Ads organization, specifically the ad products team

### 3. ContextIQ -- NOT under ATM (as a product org)

- No dedicated "ContextIQ" wiki found; contextual targeting is a capability, not a team
- **Contextual targeting on PVA wiki**: https://w.amazon.com/bin/view/PrimeVideoads/Contextual/
- Owned by "ad-sales-wiki-admins" LDAP
- The underlying AI technology is "TitleSense" owned by the **APM Signal team**
- MediaCoRE (Media Content Reasoning Engine) under "Prime Video Content Understanding" is the GenAI content analysis engine that may power scene-level analysis
- Contextual collection curation is managed by APM Signal team and VSGTM
- **Org**: Spread across PV Content Understanding (tech), APM Signal (product), and Ad Sales (GTM)

### 4. X-Ray -- NOT under ATM

- **Wiki**: https://w.amazon.com/bin/view/Amazon_Video/X-Ray/
- **Owner LDAP**: trilee-org
- **Tricia Lee** (trilee): Dir, Partner & Supply Chain
  - Dept: "PV Partner Experience" (#5267)
  - Reports to: Mike Hopkins (mikehopk) - SVP, Amazon Video and Studios
- X-Ray is a Prime Video native feature under the PV org, NOT under Ads or ATM
- Bonus content wiki path: Amazon_Video > X-Ray > VOD > PremiumExperiences > BonusContent

---

## Org Structure Summary

```
Andy Jassy
├── Paul Kotas (SVP Ads, IMDb, Grand Challenge)
│   ├── Wayne Purboo (VP, Amazon Shopping Video)
│   │   └── John Katsavrias (Dir, Software Development)
│   │       └── Betty Tso (Sr.SDM, Shop-the-Show) ← STS team
│   │           └── Shashank Jain (Principal PMT, STS)
│   └── [Ad Sales / GVA org]
│       └── Interactive Video Ads (IVA) ← IVA team
│
└── Mike Hopkins (SVP, Amazon Video and Studios)
    ├── Kam Keshmiri (VP, Design, PV)
    │   └── Azim Ali (Sr. Manager, UX Design)
    │       └── Sarah Yukes (Sr. Manager, ATM) ← ATM team (UX only)
    └── Tricia Lee (Dir, Partner & Supply Chain)
        └── X-Ray team ← X-Ray
```

## Conclusion

**None of the 4 teams fall under ATM.** ATM is a ~8-person UX design team within PV Experience Design. It provides UX/design support for ad experiences on Prime Video but does not own product, engineering, or PMT for any of the 4 products.

- **STS**: Under Ads org (Kotas) > Amazon Shopping Video (Purboo)
- **IVA**: Under Ads org (Kotas) > Ad Sales / GVA
- **ContextIQ**: Not a single team; capability spread across APM Signal, PV Content Understanding, and Ad Sales
- **X-Ray**: Under PV org (Hopkins) > PV Partner Experience
