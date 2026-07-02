# THE RISE OF THE TERRAN EMPIRE

## StoryDB — The Deep Story Advancement Database

### A queryable, long-form database for characters, technologies, items, skills, locations, factions, economy, karma, and timeline

---

## WHAT THIS IS

StoryDB is the **deep, structured data layer** of the project. While the `Memory/` files hold the *current state* and *chronological log*, StoryDB holds the *long tables* that accumulate across 3,000 chapters: every character, every technology, every item, every SP transaction, every location, every faction, every seeded karma hook.

If `Memory/` is the journal, `StoryDB/` is the library card catalogue and ledger.

This database is inspired by the deep, ever-expanding system logs in novels like *Getting a Technology System in Modern Day* — tables that start small and grow into a sprawling record of progression.

---

## WHY THIS EXISTS

A 3,000-chapter novel generates thousands of:
- Characters (hundreds of named cast members)
- Technologies and product versions (Mark-by-Mark iteration)
- Items, products, artifacts (Mana Stones, Aether Stones, ships, weapons)
- Skills, abilities, cultivation techniques (System Shop + discovered)
- Locations (apartments, facilities, VR universes, planets, galaxies)
- Factions (companies, governments, alien species, Empire ministries)
- Economic transactions (SP, fiat, market cap)
- Karma seeds and payoffs (foreshadowing chains)
- Timeline anchor events

Trying to remember all of these from the Chronicle alone is too slow. StoryDB keeps them in tables that are **machine-greppable, human-readable, and append-friendly**.

---

## DATABASE CATALOG

| File | Entity | What it tracks | ID prefix |
| ------ | -------- | ---------------- | ----------- |
| `Characters/Cast.md` | Characters | All named characters, status, cultivation, aliases, arcs | `CHAR-` |
| `Characters/Relationships.md` | Relationships | Who knows whom, trust scores, relationship dynamics | `REL-` |
| `Characters/Knowledge Boundaries.md` | Knowledge | What each character knows about System, SP, cultivation, tech | `KNOW-` |
| `System/Technologies.md` | Technologies | Tech tree — every tech, version, dependency, chapter introduced | `TECH-` |
| `System/Items & Products.md` | Items | Items, products, artifacts, materials, tiers | `ITEM-` |
| `System/Skills & Abilities.md` | Skills | Skills, cultivation techniques, purchased abilities, ranks | `SKILL-` |
| `System/Missions & Objectives.md` | Missions | Story objectives, quests, arcs, Empire milestones | `MISS-` |
| `System/Achievements.md` | Achievements | Unlocks, titles, milestone flags | `ACH-` |
| `World/Locations.md` | Locations | All physical and virtual locations, facilities, universes | `LOC-` |
| `World/Factions & Organizations.md` | Factions | Companies, governments, species, Empire factions | `FACT-` |
| `World/Timeline Master.md` | Timeline | Major anchor events, arcs, era boundaries | `TIME-` |
| `Economy/SP Ledger.md` | SP transactions | Every SP gain/purchase with chapter and balance | `SP-` |
| `Economy/Fiat Ledger.md` | Fiat transactions | Every USD transaction, company, market event | `FIAT-` |
| `Economy/Market Metrics.md` | Market data | Vance Global cap, company valuations, rankings | `MKT-` |
| `Economy/User Milestones.md` | User growth | Product/user counts by chapter, milestones | `USER-` |
| `Registry.md` | ID registry | Next free ID for every prefix | — |

---

## DESIGN RULES

1. **Stable IDs.** Once an entity is assigned `CHAR-001` or `TECH-042`, it keeps that ID forever. IDs are never reused.
2. **Append-only.** New rows are appended to the bottom of tables. Never insert into the middle; never delete rows (mark them `Obsolete` or `Destroyed` instead).
3. **Status column.** Every entity has a `Status` field: `Active`, `Inactive`, `Planned`, `Prototype`, `Obsolete`, `Destroyed`, `Dead`, `Lost`, etc.
4. **Chapter columns.** Every table has `Ch Introduced` and `Ch Last Updated` columns. These are what the `/query-db` skill searches.
5. **No prose.** Tables are data only. Prose lives in `Chapters/` and the Chronicle.
6. **Greppable.** Tables are plain markdown so `grep` and the `/query-db` skill can scan them quickly.
7. **ID registry.** `Registry.md` is the single source of truth for the next ID in each category. When a new entity is created, increment it.

---

## HOW THE SKILLS USE STORYDB

| Skill | Uses StoryDB to... |
| ------- | ------------------- |
| `/prep-chapter` | Query current tech tree, active characters, open karma seeds, and known locations before planning the chapter. |
| `/write-chapter` | Reference the tech tree, item tiers, and character voices while writing. |
| `/verify-chapter` | Cross-check that new entities are assigned valid IDs, that no duplicate IDs exist, and that math/state matches the database. |
| `/save-memory` | Append new entities to StoryDB tables, update existing rows, and record transactions in ledgers. |
| `/query-db` | Search any table by keyword, ID, status, chapter range, or entity type. |
| `/recall` | Chronological memory queries (complements StoryDB's tabular view). |

---

## MAINTENANCE CHECKLIST (after every chapter)

When `/save-memory` runs, it must also check StoryDB for:
- [ ] Any new named character → add row to `Characters/Cast.md` and bump `CHAR-` registry.
- [ ] Any new or upgraded technology → add/update row in `System/Technologies.md` and bump `TECH-` registry.
- [ ] Any new item/product/artifact → add row in `System/Items & Products.md` and bump `ITEM-` registry.
- [ ] Any new skill/ability/cultivation technique → add row in `System/Skills & Abilities.md` and bump `SKILL-` registry.
- [ ] Any new karma seed → add row in `System/Missions & Objectives.md` (or `Memory/Chronicle.md` if preferred) and bump `MISS-` or `KSEED-` registry.
- [ ] Any new location/facility/planet/universe → add row in `World/Locations.md` and bump `LOC-` registry.
- [ ] Any new faction/company/government/species → add row in `World/Factions & Organizations.md` and bump `FACT-` registry.
- [ ] Any SP transaction (grant, passive income, purchase, first-use bonus) → add row in `Economy/SP Ledger.md` and bump `SP-` registry.
- [ ] Any USD transaction or market event → add row in `Economy/Fiat Ledger.md` and bump `FIAT-` registry.
- [ ] Any market-cap milestone → add row in `Economy/Market Metrics.md` and bump `MKT-` registry.
- [ ] Any user-count milestone → add row in `Economy/User Milestones.md` and bump `USER-` registry.
- [ ] Update `Registry.md` with the next free ID for every touched prefix.

---

## INTEGRATION WITH MEMORY

- `Memory/Story State.md` is the **current snapshot** (what exists *right now*).
- `Memory/Chronicle.md` is the **chronological narrative** (what happened *when*).
- `StoryDB/` is the **complete ledger** (every entity, every version, every transaction, every relationship).

Together they form the memory-retention stack:
```
Chapters/     → prose
Memory/       → state + chronology
StoryDB/      → deep tables + ledgers
Reference/    → rules + lore
```

---

> **TIP:** If you are unsure whether an entity already exists, run `/query-db <name>` before creating a new row. Duplicate IDs are a verification failure.
