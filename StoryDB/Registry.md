# THE RISE OF THE TERRAN EMPIRE

## StoryDB — ID Registry

### Master record of next free IDs for every entity category

---

## RULES

- Every new entity in `StoryDB/` must receive a stable ID from this registry.
- IDs are **never reused**.
- After assigning an ID, increment the `Next` counter for that prefix.
- If a chapter introduces multiple entities of the same type, assign them sequentially and update the registry in one batch at the end.

---

## ENTITY ID PREFIXES

| Prefix | Category | File | Next ID |
| -------- | ---------- | ------ | --------- |
| CHAR- | Characters (named cast) | `Characters/Cast.md` | 007 |
| CAMEO- | Cameos / unnamed roles | `Characters/Cast.md` | 012 |
| REL- | Relationships | `Characters/Relationships.md` | 005 |
| KNOW- | Knowledge Boundaries | `Characters/Knowledge Boundaries.md` | 013 |
| TECH- | Technologies | `System/Technologies.md` | 036 |
| ITEM- | Items & Products | `System/Items & Products.md` | 001 |
| SKILL- | Skills & Abilities | `System/Skills & Abilities.md` | 024 |
| MISS- | Missions & Objectives | `System/Missions & Objectives.md` | 006 |
| ACH- | Achievements | `System/Achievements.md` | 002 |
| LOC- | Locations | `World/Locations.md` | 001 |
| FACT- | Factions & Organizations | `World/Factions & Organizations.md` | 001 |
| TIME- | Timeline Anchor Events | `World/Timeline Master.md` | 001 |
| SP- | SP Transactions | `Economy/SP Ledger.md` | 015 |
| FIAT- | Fiat Transactions | `Economy/Fiat Ledger.md` | 026 |
| MKT- | Market Metrics | `Economy/Market Metrics.md` | 001 |
| USER- | User Milestones | `Economy/User Milestones.md` | 013 |
| KSEED- | Karma Seeds | `System/Missions & Objectives.md` | 018 |

---

## ID FORMAT EXAMPLES

- `CHAR-001` — first named character
- `TECH-042` — 42nd technology/version entry
- `SP-0007` — 7th SP transaction
- `LOC-003` — 3rd location
- `KSEED-019` — 19th karma seed

Use leading zeros to keep sorting consistent. Width may expand from 3 to 4 digits when a category exceeds 999 entries.

---

## ASSIGNMENT LOG

| Date | Chapter | Assigned IDs | Updated By |
| ------ | ------- | ------------ | ---------- |
| 2025-12-31 | 0 | Created registry with all prefixes at 001 | Database Setup |
| 2026-01-01 | 1 | CHAR-001 updated; TECH-001, TECH-002, TECH-003; SKILL-001, SKILL-002; MISS-001 completed, MISS-002/003/004 added; ACH-001 unlocked; SP-001/002/003; FIAT-002; KSEED-001/002/003 | /save-memory |
| 2026-01-05 | 2 | CHAR-002, CAMEO-003; REL-001, REL-011, REL-012; KNOW-009, KNOW-010; TECH-004, TECH-005, TECH-006; SKILL-003; SP-004/005/006; FIAT-003/004/005/006/007/008; KSEED-004/005/013; USER-003/004 | /save-memory |
| 2026-01-12 | 3 | CHAR-001 updated; CHAR-003 (Linda Reeves), CHAR-004 (Marcus Webb); CAMEO-001 updated, CAMEO-005/006/007/008/009/010/011; REL-001 updated, REL-013, REL-014; KNOW-009 updated, KNOW-010 updated, KNOW-011, KNOW-012; TECH-004 updated, TECH-006 status Active; SKILL-004; SP-007/008/009; FIAT-007; KSEED-006, KSEED-007, KSEED-014; USER-005 updated | /save-memory |
| 2026-01-19 | 4 | TECH-005 (Active), SKILL-005 (Active), SP-007/008/009b, FIAT-007/008/009/010/011/012/013/014, KSEED-008 (Realized), KSEED-009, KSEED-015, USER-006 | /save-memory |
| 2026-02-01 | 6 | CHAR-005 (Ray Castillo), CHAR-006 (Glen Patterson retroactive); TECH-033/034/035; SKILL-023; SP-012/013/014; FIAT-023/024/025; USER-012; KSEED-016/017; KSEED-012 (Realized) | /save-memory |

<!-- Append new assignment batches below this line. -->
