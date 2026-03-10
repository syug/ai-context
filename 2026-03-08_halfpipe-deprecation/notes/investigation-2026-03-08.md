# Halfpipe Deprecation Investigation - 2026-03-08

## Background

BIL-E (Leon Pahole, Mirko Cappai) is deprecating Halfpipe by November 12, 2026.
All active components must be migrated or deprecated by that date.
Component owners are being contacted to make migration decisions.

- Asana project: BIL Halfpipe Deprecation (1213527661372673)
- Slack channel: #halfpipe-migration-or-deprecation (C0AJV89EPSR)
- Wiki: https://w.amazon.com/bin/view/Halfpipe/Deprecation/
- Interest list: halfpipe-deprecation-interest@amazon.com

## Key People

- **Leon Pahole** - Project owner (BIL-E)
- **Mirko Cappai** - Task assignment, coordination (BIL-E)
- **Shugo Saito (saitshug)** - APAC POC

## Deadlines

| Date | Action |
|------|--------|
| March 13 (Fri) | Acknowledge tickets (original "next Friday" from Mar 6 post) |
| March 18 | All tickets completed; data re-evaluation |
| March 30 | Migration decision due |
| November 12, 2026 | Final deadline - no pages should use Halfpipe |

## Items Related to Shugo (6 total)

### A. Directly Assigned (by Mirko) - 3 tasks

1. **Shopping Guide v2** - Awaiting Acknowledgement
2. **Tutorial example spacer** - Awaiting Acknowledgement
3. **JPHeroCarouselAnchor** - Awaiting Acknowledgement

### B. Mentions (Leon/Mirko asking about JP usage) - 3 tasks

4. **Reviews** - Leon: "one JP page is using this. Can we deprecate the page to deprecate the Halfpipe?" (Reminder email received 3/9)
5. **AXA Social Share** - Leon: "this is used on one page with very little visits, could we deprecate the page?"
6. **ImageComparisonSlider** - Mirko: "Used in JP Shugo Saito and Idia (Leon Pahole)"

### Also noted (assigned to others, JP-related)

- **Multi-asin hero showcase** (1213536673583070) - Assigned to Leigh (graleigh), JP only, 1 page (317,968 visits/30d, KATE store), Awaiting Acknowledgement

## Migration Options (from task descriptions)

1. **Deprecate** - Component no longer needed; pages using it must be deprecated or have component removed
2. **Move to AWLS** - Creates widget in Amazon Stores Builder; best for scale/customer-facing reusability
3. **Move to Webflow Native** - Functionality exists in Webflow designer (no code needed)
4. **Webflow Custom Code Component** - For custom logic; NOT ready until after Q1

## Required Actions

For each assigned task:
1. Acknowledge the ticket (comment on it)
2. Check with SM Lead whether pages need to remain live
   - If not needed: take them down
   - If needed: ask SM Lead to onboard to auto-deprecation
3. Check "Pods currently using" field and coordinate with other DTs
4. Update "Migration Decision" column

For each mention:
- Respond to Leon/Mirko with JP page deprecation decision after checking with SM Lead

## Board Sections (workflow)

Awaiting Acknowledgement -> Acknowledged -> Decision Made -> Migration in progress -> Migration Complete -> Deprecated
