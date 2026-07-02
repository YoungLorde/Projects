# THE RISE OF THE TERRAN EMPIRE

## CANON — Tracking & Agent System (Consolidated)

### How the old 25 static agent specs became one robust, executable, memory-backed system

---

> **STATUS:** This document defines the **new tracking system**. The original 25 agent specification files in `Reference/Agents/` are preserved as historical reference (they contain valuable detail tables). This file explains how they are now consolidated into a single robust, memory-backed, skill-driven system that actually runs instead of sitting as static docs.

---

## THE PROBLEM WITH THE OLD SYSTEM

The original framework defined ~25 "agents" as static markdown specs (MASTER_LAW listed 18 mandatory pre-writing docs). For a human or a single AI session this is unusable at 3,000 chapters: you cannot re-read 18 long specs before every chapter, and the "agents" never actually executed — they were just checklists hoping to be followed. They also overlapped heavily (Currency↔Technology, Timeline↔Cultivation, etc.) and used inconsistent arc counts (12 / 31 / 60).

## THE NEW SYSTEM — THREE LAYERS

### Layer 1: Canon (the rules, consolidated & deduplicated)
- `Reference/Canon/Story Laws.md` — every absolute law, deduplicated, with a Conflicts table.
- `Reference/Canon/Mechanics.md` — every formula/table (SP, cultivation, mana stones, VR, tech, world, knowledge boundaries, karma).
- **Replaces** the need to read MASTER_LAW + SINGLE_CHAPTER_LAW + STORY_CONSISTENCY_CHECKER + CONTINUITY_AGENT + the 8 tracker specs + CURRENCY/CULTIVATION/TECH agents every time. One read, ~20KB total, instead of ~250KB.

### Layer 2: Memory (the state, live & compact)
- `Memory/Story State.md` — current end-state (rewritten per chapter). The single "where are we" file.
- `Memory/Chronicle.md` — chronological event log (appended per chapter). The "what has happened" file; greppable.
- `Planning/Chapter Tracking Log.md` — numeric ledger (appended per chapter). The "exact numbers" file.
- **Replaces** the per-agent state-tracking sections that would each need updating manually and could drift out of sync. One coherent snapshot + one append-only log.

### Layer 3: Skills (the agents, now executable)
The old static agent specs become **Devin skills** that actually run:

| Old agent spec(s) | New skill | Role |
|-------------------|-----------|------|
| MASTER_LAW + CHAPTER_WRITING_PROTOCOL + STORY_CONSISTENCY_CHECKER + all checkers | `write-chapter` | Orchestrator: prep→write→verify→save |
| (continuity gathering, all 8 trackers' "read previous" steps) | `prep-chapter` | Gathers state + produces the chapter plan |
| STORY_CONSISTENCY_CHECKER + CONTINUITY + CHARACTER_IMMERSION + GUIDE_CHECKER + CURRENT_ARC_GUIDE_CHECKER + CROSS_REFERENCE + MATH_VERIFICATION + SP_CALCULATION + WORD_COUNT_CHECKER + TITLE_DOUBLE_CHECKER | `verify-chapter` | One consolidated PASS/FAIL gate |
| (the "update all agents after chapter" step) | `save-memory` | Writes Chronicle + Story State + Tracking Log + StoryDB |
| KARMA_AGENT (query side) + RESEARCH_AGENT (lookup) | `recall` | Chronological memory query |
| TIMELINE + CURRENCY + CULTIVATION + WORLD + RELATIONSHIP (status view) | `status` | Current-state snapshot |
| MASTER_STORY_GUIDE + STORY_DIRECTIVE (reference) | `canon` | Rule/mechanic lookup |
| KARMA_AGENT (registration side) | `seed-karma` | Pre-register foreshadowing hooks |
| (deep database lookup) | `query-db` | Search the StoryDB tables |

### Layer 4: StoryDB (the deep, ever-growing advancement database)
The new `StoryDB/` directory holds the long tables that a 3,000-chapter novel generates:

- `Characters/Cast.md` — every named character with status, cultivation, role.
- `Characters/Relationships.md` — trust matrix between characters.
- `Characters/Knowledge Boundaries.md` — secrecy grid per character.
- `System/Technologies.md` — tech tree, versions, dependencies, chapters.
- `System/Items & Products.md` — items, artifacts, tiers, quantities.
- `System/Skills & Abilities.md` — skills, techniques, purchased abilities.
- `System/Missions & Objectives.md` — missions and karma seed registry.
- `System/Achievements.md` — milestone unlocks.
- `World/Locations.md` — locations, facilities, VR universes, planets.
- `World/Factions & Organizations.md` — companies, governments, species, Empire factions.
- `World/Timeline Master.md` — major era/anchor events.
- `Economy/SP Ledger.md` — every SP transaction.
- `Economy/Fiat Ledger.md` — every USD/valuation transaction.
- `Economy/Market Metrics.md` — market cap and rank milestones.
- `Economy/User Milestones.md` — product user counts.
- `Registry.md` — master ID registry for all prefixes.

Skills load the relevant tables when gathering context, and `save-memory` updates them after each chapter.

---

## THE CANONICAL STORY STATE SCHEMA

`Memory/Story State.md` is rewritten after each chapter using this schema (keep field names stable so skills parse them):

- **Position:** last completed chapter, next chapter, current arc (name + Ch range), in-story date
- **Characters:** per character — cultivation (rank/level/%), lifespan, age, SP (if allowed), fiat, location, psychological state, knowledge-of-System (yes/no/partial), public cover
- **Economy & Scale:** total users, passive SP/hr, companies, facilities
- **Technology:** acquired, VR worlds, manufacturing, mana stone tier, AI/Mnemosyne version
- **Secrecy:** who knows about the System (the allowed list)
- **Karma Board:** open seeds (#id, description, payoff target) + realized (moved off)
- **Open Threads:** unresolved subplots carried forward

## THE UPDATE SEQUENCE (respects dependencies)

After each chapter, `save-memory` updates in this order:
1. **Timeline** (date) → 2. **Currency** (SP/fiat/users) → 3. **Cultivation** (rank/level) → 4. **Technology** (new/iterated) → 5. **Infrastructure** (facilities/staff) → 6. **World** (public opinion/market) → 7. **Relationship** (trust/knowledge boundaries) → 8. **Karma** (seeds/realizations).

This order respects the cross-agent dependencies (cultivation enables tech use; currency enables purchases; tech enables infrastructure; etc.) identified in the original agents.

## CROSS-VALIDATION RULES (enforced by verify-chapter)

- Can't use Tier N tech without the SP purchase that bought it (Currency↔Technology).
- Can't have Rank R+1 abilities at Rank R (Cultivation internal).
- Can't mention SP in front of a character not on the allowed secrecy list (Currency↔Relationship).
- Can't deploy tech before its dependency tech appeared (Technology tree).
- Can't regress dates/numbers vs the previous chapter (Timeline↔all).
- Mohamed/Danielle rank advances only at Level 99 (Cultivation).
- Knowledge-boundary breaches flagged (Relationship).
- Karma "realized" claims must reference a real prior seed ID (Karma↔Chronicle).
- **Fiat consistency:** every income (salary, revenue) and expense (food, supplies, rent, equipment) in a chapter must appear in `Economy/Fiat Ledger.md`; the chapter's stated USD balance must match the ledger's running balance.
- **Shop-price consistency:** every System Shop price mentioned in prose must match the canonical exponential price scale in `Mechanics.md` §1.5; every looked-at or purchased blueprint must be recorded in `System/Technologies.md`.
- **No alien knowledge:** Mohamed has no knowledge of aliens in early arcs; no alien references in Chapter 1–50 prose.
- **No milestone/wave bonuses:** the System awards SP immediately per new user/engagement; no 100-user, 1,000-user, or threshold wave payouts exist.
- **First-use fluctuation:** a first-use bonus is a random value in the 10–17 SP range per unique user; exact amounts may vary (e.g., 12.7, 15.0, 14.1). The ledger must use the specific value, not a fixed average.
- **Broad SP generation:** SP is awarded for any meaningful engagement with a Mohamed-built product, technology, technique, or cultivation resource.
- **Notebook secrecy:** any physical notebook entries written by Mohamed must not reveal the System, SP, or the shop; verify before saving each chapter.

## WHY THIS IS STRONGER

1. **It executes.** Skills run the checks; the old specs just described checks.
2. **One read, not eighteen.** Canon is ~20KB consolidated vs ~250KB scattered.
3. **Memory is compact & greppable.** 3,000 Chronicle entries fit in one searchable file; Story State is always current; you never re-read 300 chapters to know your starting numbers.
4. **Single coherent state** — no drift between 8 separately-maintained agent ledgers.
5. **Karma is enforced by ID** across the whole timeline — the "every seed pays off" mandate becomes mechanically trackable.
6. **Arc-count-agnostic** — works whether the user settles on 12, 31, or 60 arcs.
