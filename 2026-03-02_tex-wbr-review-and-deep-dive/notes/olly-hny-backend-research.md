# Olly HNY Brand Store - Backend/AI Research Findings

**Date**: 2026-03-02
**Researcher**: Claude Code
**Frontend Repo**: `BIL-TEX-Unilever-Olly-HappyNewYou2025`

## Executive Summary

**The Olly Happy New You 2025 Brand Store campaign is a purely static frontend application with NO separate backend repository, NO Lambda functions, and NO LLM/AI integration (Bedrock, SageMaker, etc.).** It is a React-based single-page application deployed to CloudFront/S3, injected into Amazon Brand Store pages via custom code snippets.

---

## 1. Is there a separate backend/CDK repo for Olly HNY?

**NO.**

Evidence:
- The repo-info page shows only **one** version set consuming this package: `CCLPPipelinesCampaignPagesArchive/development` (source: releases page)
- The primary version set is `BIL-TEX-Unilever-Olly-HappyNewYou2025/development`
- There is no CDK directory, infra directory, or `cdk.json` in the repo tree
- The `brazil.ion` file defines a simple build that outputs to `dist/` (public_dir) - standard static asset output
- The deployment mechanism (`Build-Tools/Deploy.mjs`) uploads built JS/CSS to Media Central (Wharf) and generates freeform HTML - this is a static asset deployment, not a service deployment
- The `quick-deploy.cmd.cjs` uploads to S3 + CloudFront invalidation - purely static hosting
- The `package.json` only has `@aws-sdk/client-cloudfront` in devDependencies (for deployment tooling), not for runtime
- InternalCodeSearch was denied, so I could not do a broader `BIL*CDK` or `HappyNewYou` repository search. This is a gap.

**Infrastructure**: Two CloudFront distributions:
- Gamma: `E3CF4AF6M3S05O` -> `d1t9krnwnmlcq.cloudfront.net`
- Prod: `E1YCMNN3VDOQPO` -> `d1a2mgbnwo0lue.cloudfront.net`

These are standard CCLP (Custom Campaign Landing Page) infrastructure, likely provisioned by the shared `CCLP-Pipelines-CDK-Constructs` pipeline.

## 2. Does the frontend make any API calls to a custom backend?

**NO custom backend API calls.** All API calls are to existing Amazon platform services:

### API Calls Found:

1. **Amazon Live Widget API** (platform service, not custom):
   - `LiveStatusTracker.tsx` calls:
     - `/live/api/widget?pageTypeId=channel&widgetId=widget-010&showId={channelId}` (upcoming broadcasts)
     - `/live/api/widget?pageTypeId=channel&widgetId=widget-020&showId={channelId}` (past broadcasts)
   - These are same-origin relative URLs hitting amazon.com's existing Amazon Live widget endpoints

2. **Rewards/Moments API** (platform service, not custom):
   - `RewardsContext.tsx` calls:
     - `https://${window.location.host}/moments/event/view/{CAMPAIGN_ID}/isCustomerEligible` (POST)
     - `https://${window.location.host}/moments/event/view/{CAMPAIGN_ID}/qualifyCustomer` (POST)
   - Campaign ID: `704c381e-3800-49f4-8f22-2066e7d1d20d`
   - Note: `HAS_REWARDS = false` in config, so this feature is disabled

3. **NotifyMe/RemindMe API** (platform service, not custom):
   - `notifyMe.ts` calls:
     - DEV: `https://api.us-east-1.beta.proxy.live.amazon.com/csrf/generator`
     - PROD: `https://api.us-east-1.prod.proxy.live.amazon.com/notifymeservice/reminderonbroadcastlist`
   - These are Amazon Live's reminder/notification service

4. **Generic GET helper** (`src/utils/index.ts`):
   - `getRequest()` - a simple fetch wrapper, only used by the NotifyMe utility

### What DOESN'T exist:
- No `fetch()` or `axios` calls to any custom API Gateway or Lambda endpoint
- No WebSocket connections
- No GraphQL queries
- No custom REST API endpoints

## 3. Is there any evidence of Bedrock, SageMaker, or other AI/ML service integration?

**ABSOLUTELY NONE.**

Searched through every source file. No references to:
- Amazon Bedrock
- Amazon SageMaker
- Any LLM or AI model invocation
- `bedrock-runtime`
- `InvokeModel`
- `invoke-model`
- Any AI-generated content endpoints
- Any prompt/completion patterns

The dependencies in `package.json` contain zero AI/ML related packages:
- Only AWS SDK usage is `@aws-sdk/client-cloudfront` (devDep for deployment) and `aws-sdk` (devDep for S3 deployment)
- Runtime dependencies are purely UI: React, styled-components, framer-motion, i18next, and Amazon internal UI libraries (`@amzn/tina-*`, `@amzn/adt-*`)

## 4. Architecture Summary: Purely Static Frontend

The Olly HNY campaign is a **static React SPA** with:

### Features (all client-side):
- **Wellness Wheel**: A spinning wheel UI with 4 product variants x 4 products = 16 cards. All data is hardcoded in `src/data/products.ts` and `src/data/wheelData.ts`
- **Amazon Live Integration**: Embeds Amazon Live stream via platform APIs (not custom)
- **Alexa Theme**: Simple link to `https://www.amazon.com/dp/B0DNST8KKF`
- **Amazon Music Playlist**: Embedded iframe from `music.amazon.com`
- **Product Shopping**: Uses `@amzn/tina-*` (Tina UI hooks) for Add-to-Cart functionality - this is Amazon's standard Brand Store product widget
- **Rewards**: Uses Amazon's Moments/Rewards platform service (currently disabled via `HAS_REWARDS = false`)
- **Metrics**: Uses `@amzn/adt-metrics-react` for custom metric tracking
- **Social Sharing**: Client-side clipboard and native share API
- **i18n**: English and Spanish translations (static JSON files)

### Deployment:
- Built with Vite + React + TypeScript
- Assets uploaded to Media Central (Wharf) or directly to S3
- Served via CloudFront
- Injected into Brand Store pages via custom code snippet (`stores-code-prod.html`)

### Author:
- Nathan Crenshaw (`natcren`) - https://phonetool.amazon.com/users/natcren
- Team: `us-bil-tex`

## Source URLs

- Repo tree: https://code.amazon.com/packages/BIL-TEX-Unilever-Olly-HappyNewYou2025/trees/mainline
- package.json: https://code.amazon.com/packages/BIL-TEX-Unilever-Olly-HappyNewYou2025/blobs/mainline/--/package.json
- Config: https://code.amazon.com/packages/BIL-TEX-Unilever-Olly-HappyNewYou2025/blobs/mainline/--/src/config/index.ts
- RewardsContext: https://code.amazon.com/packages/BIL-TEX-Unilever-Olly-HappyNewYou2025/blobs/mainline/--/src/store/rewards/RewardsContext.tsx
- LiveStatusTracker: https://code.amazon.com/packages/BIL-TEX-Unilever-Olly-HappyNewYou2025/blobs/mainline/--/src/components/amazonLive/LiveStatusTracker.tsx
- NotifyMe: https://code.amazon.com/packages/BIL-TEX-Unilever-Olly-HappyNewYou2025/blobs/mainline/--/src/utils/notifyMe.ts
- Deploy script: https://code.amazon.com/packages/BIL-TEX-Unilever-Olly-HappyNewYou2025/blobs/mainline/--/Build-Tools/Deploy.mjs
- Releases: https://code.amazon.com/packages/BIL-TEX-Unilever-Olly-HappyNewYou2025/releases
- Prod deployment: https://code.amazon.com/packages/BIL-TEX-Unilever-Olly-HappyNewYou2025/blobs/mainline/--/stores-code-prod.html

## Research Gaps

- `InternalCodeSearch` tool was denied, so I could not perform broader repository searches for:
  - Other `BIL-TEX-Unilever-Olly*` repos
  - `HappyNewYou` in CDK repos
  - `Olly` in any BIL* repos
  - This means there COULD theoretically be a separate backend repo with a different naming convention that I couldn't discover
- However, given the complete absence of any backend API calls in the frontend code, this is extremely unlikely
