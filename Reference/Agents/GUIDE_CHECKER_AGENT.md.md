# GUIDE CHECKER AGENT

## Arc Content Alignment Verification System

---

## PURPOSE

This agent ensures EVERY chapter's content aligns with its designated Arc Guide. It verifies that the narrative events, technology deployments, cultivation progression, and thematic elements match the Arc Guide's stated chapter gists, phases, and milestones.

---

## MANDATORY CHECKS (Pre-Writing)

### Check 1: Arc Guide Loading

Before writing Chapter N:

1. Identify which Arc contains Chapter N
2. Load the corresponding ARC_XX_*.md file
3. Extract the chapter gist for Chapter N (if available)
4. Extract the phase summary containing Chapter N
5. Extract the end-state goals for the current Arc

### Check 2: Content Alignment Verification


| Verification Point                          | Source                      | Status   |
| ------------------------------------------- | --------------------------- | -------- |
| Chapter number within Arc range             | Arc Guide header            | REQUIRED |
| Timeline date matches Arc period            | Arc Guide timeline          | REQUIRED |
| Cultivation level matches progression curve | Arc Guide cultivation table | REQUIRED |
| SP balance matches accumulation target      | Arc Guide SP progression    | REQUIRED |
| Technology focus matches Arc theme          | Arc Guide chapter gist      | REQUIRED |
| Major events match phase description        | Arc Guide phase breakdown   | REQUIRED |


### Check 3: Arc Theme Compliance

Each Arc has a dominant theme. Chapter content must reflect:

- **Arc 1 (1-100):** Discovery, System awakening, software wealth, foundation building, early cultivation, R0→R1
- **Arc 2 (101-200):** Breakthrough, government conflicts, VR time dilation, secret development, R1→R3
- **Arc 3 (201-300):** Space Empire, Mars colony, AI bodies, Covenant alliance, Swarm scout, R3→R4
- **Arc 4 (301-400):** Galactic Threshold, public revelation, Scionian alliance, interstellar, R4→R5
- **Arc 5 (401-500):** Galactic Dominance, Swarm destruction, Immortals war, Halo, R5→R7
- **Arc 6 (501-600):** Multiverse Awakening, 500K universes, Precursor origin, Weavers, Shapers, R7→R8
- **Arc 7 (601-700):** Omniversal War, 3M+ universes, Null Collective, R8→R10
- **Arc 8 (701-800):** Cosmic Conquest, 100M+ universes, Narrative Collective, R10→R12
- **Arc 9 (801-900):** Narrative Ascendancy, 500B+ universes, Origin, R12→R14
- **Arc 10 (901-1000):** Transcendence, infinite universes, 999,999 goal, Cause Epoch, R14→R16
- **Arc 11 (1001-1100):** Beyond Infinity, Layer 2 discovery, Curator war, R16→R18
- **Arc 12 (1101-1200):** Infinite Stack, Stack-Keepers, Narrator war, R18→R20

---

## CHAPTER GIST VERIFICATION

### For Chapters WITH Specific Gists:

1. Locate gist in Arc Guide
2. Extract ALL required elements:
  - Date
  - Cultivation status
  - SP balance
  - Location
  - Key events
  - Technology focus
  - Character interactions
3. Verify EACH element appears in chapter plan
4. Flag ANY missing elements as VIOLATION

### For Chapters WITHOUT Specific Gists (Filler Chapters):

1. Identify containing phase
2. Extract phase themes and goals
3. Ensure chapter advances at least ONE phase goal
4. Verify cultivation progression continues
5. Verify technology acquisition or deployment occurs
6. Verify character development or worldbuilding advances

---

## PHASE PROGRESSION VERIFICATION

### Phase Checklist:

- Chapter fits within assigned phase range
- Chapter advances phase narrative
- Chapter maintains phase-appropriate pacing
- Chapter sets up next phase transition (if near boundary)
- No phase-inappropriate technology or events

### Example: Arc 2 Phase 2 (Ch 126-150)

Required elements for chapters in this range:

- VR time dilation active (1:10 year ratio)
- Government conflict escalation
- Secret development scaling
- Mohamed R2 breakthrough, Danielle R1 sustained
- 300M+ users globally
- SP balance tracked with tier conversions

---

## VIOLATION TYPES

### CRITICAL (Chapter Invalidated):

- Chapter number outside Arc range
- Timeline date incompatible with Arc period
- Technology introduced before Arc Guide allows
- Major event contradicts Arc Guide milestone
- Cultivation level impossible for Arc position

### WARNING (Must be Justified):

- Minor date deviation (>30 days from expected)
- Additional technology not in gist but plausible
- Extra character scene not in gist but develops relationships
- Extended time skip not pre-approved

### NOTE (Logged but Permitted):

- Enhanced detail beyond gist requirements
- Additional subplots that don't conflict with gist
- Deeper character moments within chapter scope

---

## REPORT FORMAT

GUIDE CHECKER REPORT  
Chapter: [N]  
Arc Guide: [ARC_XX_NAME.md]  
Phase: [Phase ID]

GIST ALIGNMENT:

- Date: [Expected] vs [Planned] -> [PASS/FAIL]
- Cultivation: [Expected] vs [Planned] -> [PASS/FAIL]
- SP: [Expected] vs [Planned] -> [PASS/FAIL]
- Location: [Expected] vs [Planned] -> [PASS/FAIL]
- Events: [List] -> [PASS/FAIL]

PHASE ALIGNMENT:

- Within phase range: [YES/NO]
- Advances phase goals: [YES/NO]
- Appropriate pacing: [YES/NO]

THEME ALIGNMENT:

- Arc theme reflected: [YES/NO]
- No conflicting elements: [YES/NO]

OVERALL: [PASS / FAIL]

---

**INTEGRATION:** This agent feeds into STORY_CONSISTENCY_CHECKER Step 9. A FAIL from GUIDE_CHECKER_AGENT blocks chapter production until resolved.