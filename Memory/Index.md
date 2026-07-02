# THE RISE OF THE TERRAN EMPIRE

## Memory System — Index & Operator Guide

---

## WHAT THIS IS

The Memory system is the project's long-term recall layer. A 3,000-chapter novel cannot be held in any single context window. These files let the writing skills reconstruct continuity from compact, structured memory rather than re-reading every chapter.

---

## THE FOUR LAYERS

### Layer 1 — The Chronicle (`Chronicle.md`)
The **chronological event log**. One structured entry per completed chapter, appended in order. This is the "saver": `/save-memory` writes here after every chapter. It records key events, state changes, relationship shifts, knowledge-boundary updates, karma seeds/realizations, open threads, and notable prose details to keep consistent.

### Layer 2 — The Story State (`Story State.md`)
The **current end-state snapshot**. A compact "where are we right now" file, rewritten in place after each chapter. Every new chapter reads this FIRST to know its starting point (date, cultivation, SP, users, characters, tech, secrecy, karma, open threads).

### Layer 3 — The Tracking Log (`Planning/Chapter Tracking Log.md`)
The **numeric ledger**. End-of-chapter statistics per chapter (date, cultivation, SP balance, fiat, passive SP/hr, users, purchases, mana stone tier, VIRA version). This already exists in `Planning/` and is kept in sync by `/save-memory`.

### Layer 4 — The Story Database (`StoryDB/`)
The **deep, long-form advancement database**. While the three layers above give the current state and chronology, `StoryDB/` holds the sprawling tables that accumulate across 3,000 chapters: every character, technology, item, skill, location, faction, transaction, karma seed, and timeline anchor. It is the queryable "library card catalogue" and ledger for the entire story. See `StoryDB/INDEX.md` for the full catalog.

---

## HOW THE SKILLS USE MEMORY

| Skill | Reads | Writes |
|-------|-------|--------|
| `/prep-chapter N` | Story State + last 5-10 Chronicle entries + Tracking Log + Arc guide + Laws | (writes a chapter plan to memory of session, not to file) |
| `/write-chapter N` | everything `/prep` gathered | the chapter file in `Chapters/` |
| `/verify-chapter N` | the new chapter vs. Story State + Chronicle + Laws | a verification report |
| `/save-memory` | the completed chapter | Chronicle (append), Story State (rewrite), Tracking Log (append) |
| `/recall "<query>"` | Chronicle + Tracking Log (+ Reference/*) | returns matches chronologically |
| `/status` | Story State + Tracking Log + StoryDB | prints current state |
| `/query-db` | StoryDB | search any database table by keyword, ID, status, or chapter range |

---

## WHY THIS WORKS ACROSS 3,000 CHAPTERS

- **Chronicle entries are compact** (~15-25 lines each). 3,000 entries ≈ a single large file that is greppable by keyword, character, technology, or karma-seed ID.
- **Story State is always current** — a new chapter never has to read history to know its starting numbers; it reads one small file.
- **`/recall` is targeted** — instead of re-reading 300 chapters, you query "Danielle" or "Tier 3 mana stone" or "karma seed #47" and get every mention in order.
- **Nothing is lost** — the full chapter prose stays in `Chapters/`; the Chronicle is the index/memory of it.

---

## KARMA SEED TRACKING (CRITICAL)

Every foreshadowing hook planted in a chapter is logged in the Chronicle as `Karma seeded: #<id> [description] (payoff: Arc X / ~Ch Y)`. When it pays off, the realizing chapter logs `Karma realized: #<id>`. `/recall "karma seed #<id>"` reconstructs the full cause-effect chain. This is how the "every seed pays off" mandate is enforced across thousands of chapters.

---

## DIRECTORY

```
Memory/
├── Index.md          (this file)
├── Chronicle.md      (chronological event log — appended per chapter)
└── Story State.md    (current end-state snapshot — rewritten per chapter)

Planning/
└── Chapter Tracking Log.md   (numeric ledger — appended per chapter)

StoryDB/
├── INDEX.md
├── Registry.md
├── Characters/       (Cast, Relationships, Knowledge Boundaries)
├── System/           (Technologies, Items, Skills, Missions, Achievements)
├── World/            (Locations, Factions, Timeline)
└── Economy/          (SP Ledger, Fiat Ledger, Market Metrics, User Milestones)
```
