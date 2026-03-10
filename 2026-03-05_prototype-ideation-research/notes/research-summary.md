# FY26 Prototype Ideation Research — 2026-03-05

## Context
FY26 Goal #1: Innovative Ad Experiences & Prototyping (Kingpin #1078451)
- 2 innovative ad experiences across PV / Alexa / FireTV
- 2 prototypes per DT per quarter (PARC documented)

## Research Areas

### 1. WebSocket / MessageRoom (Completed — Low Priority)
- PARC: 3 existing prototypes (WebSocket Playground, Fire TV second screen websockets, Coca Cola Holiday)
- Brand Gateway MessageRoom: `@amzn/brand-gateway-client` by BIL-E
  - Wiki: https://w.amazon.com/bin/view/BIL-E/AmazonBrandMessageRoom/
  - API: `MessageRoom.start()` / `.join(roomId)` / `.broadcast()` / `.send(clientId, data)`
  - Max 8 connections/room, ticket-based auth, `amazon.com/bgw/invoke/message-room`
- Maltesers Duos brief ("Indecision Duel"): technically feasible with existing stack, no challenge
- **Decision: WebSocket direction shelved. Focus on PV + AI instead.**

### 2. Audio Fingerprinting x Prime Video (Primary Focus)
- **PARC: 0 existing prototypes** — First-of-its-kind opportunity
- Concept: mobile listens to TV audio → identifies PV content + exact timestamp → triggers second screen content
- **AI models NOT needed** — traditional DSP (Shazam-style) is superior for exact-match + timestamp
- Related PARC: "Fidelity Peek Portfolio SSE" (aleckunk/harfine) does time-code based sync, not audio

#### Key Findings
- Shazam algorithm (Wang 2003): FFT → constellation map → combinatorial hashing → time-offset alignment
- Works with 3-5 sec audio, returns content_id + exact timestamp
- Long-form content (30min-2hr movies) fully supported:
  - ~3.6MB per 2hr movie, ~36GB for 10K movies
  - Longer content = more landmarks = higher match confidence

#### Tool Candidates
| Tool | Notes |
|------|-------|
| **Olaf** | C/WASM, runs in browser, 100K tracks in 15GB, best for prototype |
| **Dejavu** | Python, Shazam impl, 100% accuracy at 5sec, good reference |
| **ACRCloud** | Commercial, already has "Second Screen Sync" product |

#### Recommended Architecture
```
Phone Mic → Web Audio API (3-5sec) → FFT + peak extraction (WASM, client-side)
  → send fingerprint hashes (~200-500 bytes) to server
  → hash table lookup (~10-50ms) → return content_id + timestamp
  → trigger second screen content
```
- Initial ID: 3-5sec capture
- Ongoing: local time tracking, re-verify every 30-60sec

### 3. AI/HuggingFace Models (To Research)
- Unique/interesting models for EC2 hosting
- Not yet researched this session

## Next Steps
- [ ] Olaf WASM prototype — browser-based audio fingerprinting PoC
- [ ] PV content indexing pipeline design
- [ ] HuggingFace model exploration for other prototype ideas
- [ ] Fidelity SSE (aleckunk/harfine) — review as reference for PV second screen UX
