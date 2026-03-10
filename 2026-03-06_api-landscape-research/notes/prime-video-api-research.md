# Prime Video API Landscape

**Date:** 2026-03-06
**Author:** Claude (AI Research Agent)
**Context:** BIL-TEX team API landscape research -- Prime Video & adjacent APIs

## Summary

Prime Video's API ecosystem is predominantly internal/partner-only, with no Spotify-like public developer API. The key API surfaces are: (1) **Partner API Gateway** for content supply chain automation with studios/post-houses, (2) **Interactive Video Ads (IVA)** system enabling shoppable/interactive ad overlays via VAST extensions, (3) **Sports Data Platform (SDP)** providing real-time sports metadata for X-Ray and live events, (4) **Fire TV Integration SDK** for 3P app developers, and (5) **Amazon Ads API / DSP** for programmatic ad buying including Streaming TV. Unlike Spotify, Prime Video has no open content/metadata API; IMDb remains the public metadata layer. For BIL-TEX, the highest-value integration points are IVA (interactive branded experiences), Pause Ads, the emerging Second Screen / Shop the Show companion experience, and the Amazon Ads API for programmatic Streaming TV campaigns.

---

## 1. Prime Video Internal APIs

### 1.1 Prime Video Partner API Gateway

- **Overview:** Suite of externally-facing APIs for studios, post-houses, and fulfillment partners to programmatically manage their video catalog and distribute content to Prime Video.
- **Key Capabilities:**
  - Avails API (CRUD operations on content availability/rights -- GA)
  - Offer Status API (view offer status for submitted avails -- coming 2025)
  - Asset Status API (view status of submitted assets -- coming 2025)
  - CEX API (internal: access to CES data)
  - GraphQL Resource Server (internal: query orchestration across resource servers)
- **Architecture:** Federated API framework; requests routed through Partner API Service (PVPartnerApiGateway) to authoritative resource servers.
- **Standards:** MDDF (MovieLabs Digital Distribution Framework) compliant; industry-standard API patterns.
- **Authentication:** OAuth-based partner authentication via API Gateway; permission model with audit logging.
- **Access:** Partner-only (studios, post-houses, media fulfillment centers). Not public.
- **Contact:** pv-partner-apis@amazon.com / Slack: #pv-studio-partner-api-interest
- **Wiki:** https://w.amazon.com/bin/view/PartnerAPI/
- **Launch:** API Gateway launched Dec 2022; ongoing expansion of resource servers.

### 1.2 Interactive Video Ads (IVA) System

- **Overview:** Interactive ad format on Prime Video enabling viewers to engage directly with ads through clickable overlays or QR codes. Viewers can add products to cart, learn more, get quotes, book appointments, etc.
- **Key Components:**
  - **IVA-CTA-Handler Service:** Processes interactive ad clicks from Prime Video clients.
    - Endpoints: `/v1/getAvailableActions` (POST), `/v1/invokeCTA/SMM` (POST, email notification), `/v1/invokeCTA/STP` (POST, mobile+email notification), `/v1/invokeCTA/ATC` (POST, add to Amazon cart)
  - **Ad Rendering:** VAST v3.0 with IVA extensions; supports three rendering formats: Webview (SIMID standard), JSIDF (JavaScript), Native/JSON.
  - **Cortado Service:** Manages interactivity configurations for actions.
  - **Tenor/Renderscript:** Creative rendering pipeline.
- **Ad Formats:**
  - Shoppable Ads (Add to Cart)
  - Discovery Ads (Send to Phone / Learn More)
  - Pause Ads (interactive ads appearing on content pause)
  - Location-Based IVA (zip-code level personalization)
  - Dynamic Creative Optimization (Beta Q2'26)
- **Supply Sources:** Prime Video Premiere, STV Plus, Fire TV Channels, APS publishers (Max, AMC, Discovery+, Crunchyroll, Sling, etc.)
- **Availability:** US (GA), EU5, CA, MX, BR, AU, NZ, JP, IN, NL, SE
- **Access:** Via Amazon DSP (Managed Service and Self-Service). Not a public developer API.
- **Metrics Impact:** +30% brand awareness uplift, +28% purchase intent, +16% detail page views, +36% orders (Kantar study)
- **Wiki:** https://w.amazon.com/bin/view/AdSales/GVA/Products/InteractiveVideoAds/

### 1.3 Sports Data Platform (SDP)

- **Overview:** Source of factual sports data within Prime Video. Acquires, stores, and vends data from authoritative 3P sports data providers.
- **Key Systems:**
  - **Static Data System:** Slowly-changing data (schedules, player/team "trading cards", pre/post-game stats, standings)
  - **Real-Time Data System:** Rapidly-changing in-game data (game status, box scores, play-by-play)
  - **SDP Matching System:** Maps entity identifiers across various sources to canonical SDP IDs
  - **SDP Contribution API:** Enables internal customers to onboard leagues/tournaments
  - **SDP Distribution API:** With AAA capability for client data access
  - **Holly UI:** Data exploration interface (https://holly.prime-video.amazon.dev/)
- **Consumers:** X-Ray (live sports overlays), Live Events Publishing, Amazon Retail, Collection Pages, State Automation
- **Teams:** SDP Core, SDP Genesis (images/entity matching), SDP LECE (engagement/notifications), SDP SPIN, SDP Almanac
- **Access:** Internal only. No public API.
- **Wiki:** https://w.amazon.com/bin/view/Amazon_Video/live_services/SportsDataPlatform/

### 1.4 X-Ray (Prime Video Metadata Overlay)

- **Overview:** Customer-facing feature that provides real-time metadata during content playback -- actor information, music identification, trivia, sports stats. Powered by IMDb data and SDP for sports.
- **Integration Points:**
  - IMDb data pipeline for VOD content metadata
  - SDP for live sports real-time stats and play-by-play
  - Companion/Second Screen experience (ACE Group Sync architecture)
- **Second Screen / Companion Experience:**
  - Uses Watch Party (ACE Group Sync) architecture for cross-device synchronization
  - Cloud-based device discovery via ACN (Asynchronous Client Notifications)
  - Syncs X-Ray content between primary (TV) and secondary (mobile) devices
  - Enables playback control from mobile device
- **Access:** Internal services only. No public API exposure for X-Ray data.
- **Related Broadcast:** https://broadcast.amazon.com/videos/133707 (X-Ray on Live Sports tech talk)

### 1.5 Shop the Show (Second Screen Commerce)

- **Overview:** Synchronized second-screen companion experience enabling customers to browse and purchase products related to what they're watching on Prime Video.
- **How It Works:** While watching STS-enabled PV content, customers open Amazon mobile app and search "shop the show" to access real-time synchronized shopping experience.
- **Coverage:** 145 PV cinematic titles + Thursday Night Football (as of Feb 2025), covering ~18% of PV viewership in the US.
- **Data Sources:** ASV 10-foot specific data, Prime Video's Catalog Decoration Service (CDS)
- **Access:** Internal commerce integration. Not an external API.

### 1.6 Prime Video Ads (PVA) Platform

- **Overview:** Premium streaming TV advertising solution with full-screen, non-skippable video ads within Prime Video content. Launched early 2024.
- **Ad Types:** Pre-roll, mid-roll, post-roll, Pause Ads, Interactive Video Ads, First Impression Takeover, Sponsorships
- **Delivery:** Programmatically through Amazon DSP; supports budgets, frequency caps, audience targeting via 1P signals (shopping, browsing, streaming)
- **Measurement:** Amazon Marketing Cloud (AMC), third-party measurement partners
- **Locales:** US, CA, UK, DE, AT, FR, IT, ES, MX, AU, BR, JP, IN, SE, NL, NZ
- **Access:** Via Amazon DSP (programmatic). Managed Service and Self-Service.

### 1.7 Prime Video Channels (PVC) / Subscriptions

- **Overview:** Add-on subscription service within Prime Video for partners like Max, Paramount+, Discovery+, AMC+, etc.
- **Partner Integration:** Partners integrate content catalog and playback through PV's backend systems.
- **Advertising:** PVC channel ad inventory is separate from PVA; some IVA-enabled endpoints exist for select PVC publishers.
- **Access:** Partner integration only. No public API.

### 1.8 Prime Video Direct (PVD) / Amazon Video Direct (AVD)

- **Overview:** Self-service content distribution platform for indie video providers (formerly AVD, now PVD).
- **Capabilities:** Self-service upload, content compliance review (CRISIS/VIPER), catalog integration, royalty reporting.
- **Integration:** Uses RAMP (Revenue & Monetization Platform) for payments; COOP system for catalog management.
- **Standards:** Supports Amazon XML and MEC (Media Entertainment Core) format for metadata.
- **Access:** Self-service portal for content providers. No public API for programmatic submission.
- **Internal Name:** DVCooper / COOP

---

## 2. Prime Video Public-Facing APIs & Developer Resources

### 2.1 Amazon Ads API (Streaming TV / Video)

- **Overview:** Amazon's advertising API suite includes support for Streaming TV campaigns via Amazon DSP.
- **Capabilities:**
  - Campaign creation, management, reporting for Streaming TV ads (including Prime Video)
  - Sponsored TV (self-service video ads)
  - Amazon Marketing Cloud (AMC) for measurement and analytics
  - Audience targeting using Amazon's 1P signals
- **Authentication:** Login with Amazon (LWA) OAuth 2.0
- **Documentation:** https://advertising.amazon.com/API/docs/en-us (Note: primarily JS-rendered; API docs require authenticated access)
- **Video-Related Products:**
  - Streaming TV ads (Prime Video, Twitch, Fire TV Channels, APD)
  - Streaming TV Plus (bundled reach across all STV supply)
  - Streaming TV Efficient Reach (scaled reach at fixed CPM)
  - Sponsored TV (self-service via Ad Console)
  - Interactive Video Ads (via DSP)
  - Pause Ads (via DSP)
- **Access:** Advertiser/agency accounts required. Public API with registration.

### 2.2 Amazon Publisher Services (APS) - Video

- **Overview:** Header bidding solution for video publishers; enables publishers to monetize video inventory through Amazon's demand.
- **Video Ad Support:** VAST/VPAID compliant; supports pre-roll, mid-roll, post-roll; CTV integration.
- **Prime Video Channels Integration:** APS powers ad delivery for some PVC publishers.
- **Documentation:** https://aps.amazon.com/aps/solutions/video/ (requires account)
- **Access:** Publisher-facing. Registration required.

---

## 3. Adjacent APIs (Fire TV, Ads, Commerce)

### 3.1 Fire TV Integration SDK & APIs

- **Overview:** Comprehensive SDK for 3P app developers building on Fire TV platform.
- **Key APIs:**
  - **Fire TV Integration SDK:** Content personalization (Watch Activity, Watchlist)
  - **Content Launcher API:** Deep linking to content from Fire TV UI (Matter-based standard)
  - **Account Login API:** Authentication status reporting (headless service)
  - **Media Session API:** Voice-enabled transport controls
  - **Catalog Integration:** TIF (TV Input Framework) for linear TV; Live Events integration
  - **Recommendations API:** Content recommendations surfacing
  - **In-App Purchasing API:** Consumables, entitlements, subscriptions
  - **Advertising ID API:** Ad targeting support
  - **DIAL Integration:** Device discovery and launch protocol
  - **A3L SDKs:** Appstore-independent abstraction for auth, location, cloud messaging
- **Fire TV Partner MCP Server (New):** AI-powered platform enabling partners to integrate Fire TV features via natural language queries, automated code generation, and integrated test harness. Reduces integration time from weeks to days.
- **Developer Portal:** https://developer.amazon.com/fire-tv
- **Access:** Public developer documentation. Free registration.

### 3.2 Sonata (Prime Video Storefront Management)

- **Overview:** Internal web application for creating, scheduling, and managing content on the Prime Video storefront.
- **URL:** https://sonata.aka.amazon.com
- **Access:** Internal only.

### 3.3 Spine (Sports Configuration Service)

- **Overview:** Prime Video Sports' centralized configuration management service for feature settings across clients.
- **Capabilities:** Real-time configuration updates via APIs; DynamoDB + ACM backend.
- **Access:** Internal only.

---

## 4. Competitor Streaming Service APIs (Comparison)

### 4.1 Netflix

- **Public API Status:** **Discontinued** (2014). Netflix shut down its public API program.
- **Current State:** No public content/metadata API available. All integrations are partner-specific and bilateral.
- **Partner Integrations:** Device certification program; DIAL protocol (co-developed with YouTube/Google); Open Connect CDN for ISPs.
- **Ad Platform:** Netflix launched ad-supported tier (2022) via Microsoft Advertising partnership; no self-service API for ad buying yet. Uses Microsoft's Xandr for programmatic.
- **For Comparison:** Netflix has zero public API surface -- even more closed than Prime Video.

### 4.2 Disney+ / Hulu / Disney Streaming

- **Public API Status:** **No public API.** Disney does not offer a developer program for Disney+ content or metadata.
- **Ad Platform:** Disney+ ad-supported tier uses Disney's Ad Server (formerly Hulu Ad Manager). Hulu has a self-service ad platform (Hulu Ad Manager) with API access for programmatic buying.
- **Partner Integrations:** Device certification; CTV app integrations.
- **Disney Ad Server API:** Available for programmatic buying through Disney's unified platform (replaces Hulu legacy API).
- **For Comparison:** Hulu historically had more ad API surface than Disney+.

### 4.3 HBO Max / Max (Warner Bros. Discovery)

- **Public API Status:** **No public API.** Max has no developer program or public content API.
- **Ad Platform:** Max launched ad-supported tier (2023); uses WBD's proprietary ad tech stack + third-party partnerships.
- **For Comparison:** Completely closed ecosystem, similar to Netflix.

### 4.4 Paramount+

- **Public API Status:** **No public API.** Paramount+ does not offer public developer APIs.
- **Ad Platform:** Paramount Advertising uses EyeQ platform for programmatic CTV ad buying.
- **For Comparison:** Closed platform; ad buying through Paramount's sales team or programmatic partners.

### 4.5 Roku

- **Public API Status:** **Yes -- Roku has a developer program and APIs.**
- **Key APIs:**
  - **Roku Developer SDK:** BrightScript/SceneGraph for channel development
  - **External Control Protocol (ECP):** REST API for device control, deep linking, search
  - **Roku Advertising Framework (RAF):** Client-side ad insertion SDK
  - **Roku Search API:** Content discovery integration
  - **Roku Pay:** In-channel purchasing/subscriptions
  - **Roku Measurement & Analytics:** Campaign measurement
  - **OneView Ad Platform API:** Programmatic ad buying (self-service)
- **Developer Portal:** https://developer.roku.com
- **Access:** Public developer program. Free registration.
- **For Comparison:** Roku is the most open platform in the streaming space (closest to Spotify's model).

### 4.6 TMDB / JustWatch (Metadata Aggregators)

- **TMDB API:** Free public API for movie/TV metadata, images, ratings. Widely used as a de facto standard for streaming metadata.
  - REST API with API key authentication
  - Rate limits: ~40 requests/10 seconds
  - Covers movies, TV shows, people, images, videos
  - https://developer.themoviedb.org/docs
- **JustWatch:** Streaming availability aggregator. No official public API (unofficial scraping exists).
- **For Comparison:** These serve the role that Netflix/PV public APIs might have served; community-driven alternatives.

---

## 5. BIL/TEX Activation Opportunities

### 5.1 Interactive Video Ads (IVA) -- **HIGH VALUE**

- **Opportunity:** IVA is the most direct path to interactive branded experiences on Prime Video.
- **Capabilities:** Shoppable overlays (Add to Cart), Discovery ads (Learn More / Send to Phone), Location-Based targeting, Deal Badging, Dynamic Creative Optimization (coming Q2'26).
- **TEX Relevance:** Remote-clickable overlays and QR code experiences are fundamentally "brand experience" features. The VAST v3.0 extension model with JSON/JSIDF/Webview rendering options maps well to branded interactive content.
- **Activation:** Via Amazon DSP. Both Managed Service and Self-Service (via Sponsored TV).

### 5.2 Pause Ads -- **HIGH VALUE**

- **Opportunity:** Full-screen branded unit appearing on content pause. Supports interactivity (Add to Cart).
- **TEX Relevance:** Non-intrusive brand moment during "user-generated intermission." High attention, full-screen canvas.
- **Activation:** Via Amazon DSP. Component-based creative in DSP UI.

### 5.3 Second Screen / Shop the Show -- **HIGH VALUE**

- **Opportunity:** Synchronized dual-screen experience connecting TV viewing to mobile shopping.
- **TEX Relevance:** This is the closest analog to Spotify's "Canvas" or "Enhanced Album" concept -- augmented content that adds a commerce layer to viewing.
- **Architecture:** ACE Group Sync (Watch Party infrastructure) could potentially be extended for brand companion experiences.
- **Current Limitation:** Currently limited to 145 titles + TNF. Not yet a general-purpose API.

### 5.4 Live Sports + SDP Integration -- **MEDIUM-HIGH VALUE**

- **Opportunity:** Real-time sports data (play-by-play, stats, box scores) synchronized with live viewing.
- **TEX Relevance:** Brand integration opportunities around key sporting moments (e.g., goals, touchdowns). IVA is already served on live sports (NBA, TNF, UCL).
- **Data Access:** SDP is internal-only, but its outputs power X-Ray experiences that brands can contextually align with.

### 5.5 Fire TV Platform Integration -- **MEDIUM VALUE**

- **Opportunity:** Fire TV's developer SDK provides content integration, deep linking, recommendations, and the new MCP-powered partner integration platform.
- **TEX Relevance:** Brand apps/channels on Fire TV; content launcher deep linking for brand content; potential branded FAST channels.
- **Access:** Public developer program.

### 5.6 Amazon Ads API / DSP Programmatic -- **FOUNDATIONAL**

- **Opportunity:** Programmatic buying of all PV ad inventory through Amazon DSP API.
- **TEX Relevance:** Foundation layer for all PV advertising activations. 1P audience targeting using shopping/browsing/streaming signals.
- **Access:** Public API with advertiser registration.

### 5.7 First Impression Takeover -- **PREMIUM**

- **Opportunity:** 100% SOV of first pre-roll slot across PV catalog on a given day.
- **TEX Relevance:** Maximum brand impact for tentpole moments (product launches, cultural events).
- **Activation:** Via Amazon DSP Managed Service.

---

## 6. Key Gaps vs. Spotify Model

| Dimension | Spotify | Prime Video |
|-----------|---------|-------------|
| **Public Content API** | Yes (Web API) | No (IMDb is separate) |
| **Metadata Access** | Open (tracks, albums, artists, playlists) | Closed (no public catalog API) |
| **User Activity API** | Yes (recently played, top items) | No public equivalent |
| **Developer Ecosystem** | Rich (SDKs, widgets, embeds) | Fire TV SDK only |
| **Ad API** | Spotify Ad Studio API | Amazon Ads API (more mature, broader) |
| **Interactive Formats** | Canvas, Enhanced Albums | IVA, Pause Ads, Shop the Show |
| **Partner Content API** | Spotify for Podcasters API | Partner API Gateway (partner-only) |
| **Streaming Data** | Spotify for Artists analytics | No public equivalent |

**Key Takeaway:** Prime Video operates a "walled garden" model with rich internal APIs but minimal public developer surface. The advertising stack (Amazon DSP/Ads API) is the primary programmatic interface. For BIL-TEX, the advertising and interactive experience APIs (IVA, Pause Ads, Shop the Show) represent the most actionable integration points.

---

## Sources

### Internal Wikis
- https://w.amazon.com/bin/view/PartnerAPI/
- https://w.amazon.com/bin/view/Amazon_Video/Digital_Video_Supply_Chain/Partner_Marketplace/Selection_Management/Rights_Selection_Management/Partner_API/
- https://w.amazon.com/bin/view/AdSales/GVA/Products/InteractiveVideoAds/
- https://w.amazon.com/bin/view/Amazon_Video/live_services/SportsDataPlatform/
- https://w.amazon.com/bin/view/PV_AD%27S_QS_TEAM/IVA%28Intractive_Video_Ads%29/
- https://w.amazon.com/bin/view/V15/Vicuna/Services/IVA-CTA-Handler/
- https://w.amazon.com/bin/view/IAX/Architecture/AdRendering/
- https://w.amazon.com/bin/view/RustLiveIVA/
- https://w.amazon.com/bin/view/Streaming_TV_Ads_Wiki/AdProducts/
- https://w.amazon.com/bin/view/AdsMarketing/productmarketing/commdocs/PrimeVideoads/
- https://w.amazon.com/bin/view/AdsMarketing/productmarketing/commdocs/StreamingTVads/
- https://w.amazon.com/bin/view/AIV_Engagement/Blender/Design/GroupSync/
- https://w.amazon.com/bin/view/AmazonShoppingVideos/10-foot/sts/title-removal/
- https://w.amazon.com/bin/view/AdOps_TRAINING_%26_DEVELOPMENT_HUB/Deals_Amazon_Managed/Pauseads/
- https://w.amazon.com/bin/view/Appstore-AIM/Integrations/Live-TV/
- https://w.amazon.com/bin/view/WIKI/FireTV/

### External
- https://developer.amazon.com/fire-tv (Fire TV Developer Portal)
- https://advertising.amazon.com/API/docs/en-us (Amazon Ads API)
- https://aps.amazon.com/aps/solutions/video/ (Amazon Publisher Services)
