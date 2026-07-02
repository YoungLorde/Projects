---
name: save-memory
description: After a chapter is written/verified, save its memory — append to Chronicle, rewrite Story State, append to Tracking Log, and update the StoryDB database.
argument-hint: "[chapter number]"
triggers:
  - user
  - model
allowed-tools:
  - read
  - edit
  - write
  - grep
  - glob
  - exec
---

You are the **Chronicle Saver** for *The Rise of the Terran Empire*. Chapter $1 has been written and verified. Your job is to record its memory so the story never forgets. You update FOUR things: the Chronicle, the Story State, the Tracking Log, and the StoryDB database. Do all four, then report.

## STEP 1 — READ THE FINISHED CHAPTER
Find `Chapters/Chapter $1 -*.md` (glob for the em-dash filename). Read it fully. Extract:
- The immersive title.
- The header block (date, arc, location, cultivation both, lifespan, SP balance, passive SP/hr, users, key characters, tech introduced, items introduced, skills used/unlocked, locations visited, factions involved, karma events seeded, StoryDB IDs created, word count).
- The actual key events (2-3 most plot-significant things that HAPPENED — concrete, specific).
- State changes (cultivation deltas, SP deltas with the math, fiat, users, tech, mana stone tier, AI/Mnemosyne version).
- Relationship shifts (new bonds, trust changes, introductions, departures).
- Knowledge-boundary updates (who learned what — CRITICAL for secrecy).
- Karma seeded this chapter (assign sequential IDs continuing from the highest ID already in the Chronicle / StoryDB — e.g. if last KSEED was #12, this chapter's first new seed is #13).
- Karma realized this chapter (match to prior seed IDs by reading the Chronicle / StoryDB).
- Open threads at chapter end (unresolved subplots/hooks carried forward).
- Notable prose details to remember (names coined, sensory anchors, signature phrases, character quirks revealed).

Also read `StoryDB/Registry.md` to know the next available IDs for every category.

## STEP 2 — APPEND TO THE CHRONICLE
Use the `edit` tool to append a new entry at the end of `Memory/Chronicle.md` (after the last `### CHAPTER N` block, before any closing marker). Use EXACTLY this format (so it stays machine-greppable):

```
### CHAPTER $1 — [Immersive Title]
- Date (in-story): YYYY-MM-DD
- Arc: [Arc name] (Ch X-Y)
- POV: [character]
- Locations: [where]
- Characters present: [list]
- Key events:
  1. [concrete one-line]
  2. [...]
  3. [...]
- State changes:
  - Cultivation: [Mohamed: Rank X Lvl Y (Z%)] / [Danielle: ...]
  - SP: [balance + delta if changed] (SECRET)
  - Fiat (USD): [public balance]
  - Users: [count]
  - Tech introduced/advanced: [list or "None"]
  - Items introduced: [list or "None"]
  - Skills used/unlocked: [list or "None"]
  - Mana stone tier: [tier]
  - VIRA/Mnemosyne version: [version]
- Relationships: [shifts or "None"]
- Knowledge boundaries: [who learned what or "No change"]
- Karma seeded: [#<id> [desc] (payoff: Arc X / ~Ch Y)]
- Karma realized: [#<id> or "None"]
- Open threads at chapter end: [list or "None"]
- Notable prose details: [names/anchors/quirks or "None"]
- StoryDB IDs created/updated: [list of CHAR-/TECH-/ITEM-/LOC-/FACT-/SP-/FIAT-/KSEED- etc.]
```

## STEP 3 — REWRITE THE STORY STATE
Use the `write` tool to OVERWRITE `Memory/Story State.md` with the new end-state. Keep the SAME schema/field structure as the existing file (so skills can parse it). Update:
- `Last completed chapter:` → $1
- `Next chapter to write:` → $1+1
- `Current arc:` (unchanged unless this was the arc's last chapter)
- `In-story date:` → the chapter's end date
- Every CHARACTER STATE sub-block (cultivation, SP, fiat, location, psychological state, knowledge) for Mohamed, Danielle, Mnemosyne, and any newly introduced characters
- ECONOMY & SCALE (users, passive SP/hr, companies, facilities)
- TECHNOLOGY (acquired, VR worlds, manufacturing)
- SECRECY STATUS (who knows — update as characters learn things)
- KARMA BOARD (open seeds with IDs + their payoff targets; move realized ones out)
- OPEN THREADS (the carried-forward list)

Preserve the explanatory header of Story State.md (purpose note, "how this file is updated" footer) — only swap the data.

## STEP 4 — UPDATE THE STORY DATABASE (StoryDB/)
This is the deep advancement database. Update every relevant table by appending new rows or updating existing rows (Status, Ch Last Updated, Quantity, etc.). Never delete rows; mark obsolete rows as `Obsolete`. Check `StoryDB/Registry.md` before assigning any new ID.

For each new entity introduced in Chapter $1, add a row to the appropriate table:
- **New character** → `StoryDB/Characters/Cast.md`
- **New or shifted relationship** → `StoryDB/Characters/Relationships.md`
- **Knowledge boundary change** → `StoryDB/Characters/Knowledge Boundaries.md`
- **New technology or version** → `StoryDB/System/Technologies.md`
- **New item/product** → `StoryDB/System/Items & Products.md`
- **New skill/ability** → `StoryDB/System/Skills & Abilities.md`
- **New mission objective or karma seed** → `StoryDB/System/Missions & Objectives.md`
- **New achievement unlocked** → `StoryDB/System/Achievements.md`
- **New location or facility** → `StoryDB/World/Locations.md`
- **New faction or org** → `StoryDB/World/Factions & Organizations.md`
- **New timeline anchor** → `StoryDB/World/Timeline Master.md`
- **New SP transaction** → `StoryDB/Economy/SP Ledger.md`
- **New fiat/USD transaction or valuation** → `StoryDB/Economy/Fiat Ledger.md`
- **New market cap/rank** → `StoryDB/Economy/Market Metrics.md`
- **New user milestone** → `StoryDB/Economy/User Milestones.md`

After updating tables, update `StoryDB/Registry.md` to reflect the next free ID for every touched prefix.

## STEP 5 — APPEND TO THE TRACKING LOG
Use the `edit` tool to append a numeric ledger entry at the end of `Planning/Chapter Tracking Log.md`, matching the existing entry format exactly (see e.g. the Chapter 7 block): Date, Cultivation, SP Balance, Fiat Balance, Passive SP/hr, Users, Key Events (2-3 lines), Purchases (item + cost), Mana Stone Tier, VIRA Version, and an SP calculation check line.

## STEP 6 — REPORT
Print a one-block summary:
```
## MEMORY SAVED — Chapter $1
- Chronicle: appended entry (karma seeds #<ids>, realized #<ids>)
- Story State: rewritten (date now YYYY-MM-DD; next chapter = $1+1)
- StoryDB: updated N tables (new IDs: <list>)
- Tracking Log: appended numeric entry
- New open threads: [...]
- Next karma seeds due: [#<id> by ~Ch Y, ...]
```
This is what guarantees chapter 2,500 stays consistent with chapter 1. Be precise — a wrong number saved now becomes a contradiction in 200 chapters.
