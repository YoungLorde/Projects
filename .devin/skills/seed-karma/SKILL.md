---
name: seed-karma
description: Deliberately plant a karma/foreshadowing hook into the story's memory ledger for future payoff.
argument-hint: "<one-line description of the hook>"
triggers:
  - user
  - model
allowed-tools:
  - read
  - edit
  - grep
---

You are the **Karma Registrar** for *The Rise of the Terran Empire*. The user wants to deliberately plant a foreshadowing hook: `$ARGUMENTS`

## STEP 1 — ASSIGN AN ID
Read `StoryDB/Registry.md` for the next `KSEED-` ID. Also cross-check `Memory/Chronicle.md` for any karma-seed IDs already used (grep for `Karma seeded: #`). Use whichever is higher, then update `StoryDB/Registry.md` to the next free `KSEED-` ID.

## STEP 2 — DETERMINE PLACEMENT
Ask/confirm with the user (or infer): which chapter will this seed be planted in, and which arc/~chapter is the intended payoff? If the user gives only the description, propose a sensible payoff target from the arc outline and ask them to confirm.

## STEP 3 — LOG IT
Append a line to the **Karma Board** section of `Memory/Story State.md` (use `edit` to add under `Open threads`/`Karma seeds due` area), in the form:
```
- #<id> [description] (seeded: Ch N, payoff: Arc X / ~Ch Y) — OPEN
```
This makes it visible to `/prep-chapter` and `/recall` so the seed is never forgotten and eventually pays off.

## STEP 4 — REPORT
```
## KARMA SEEDED — #<id>
Description: [the hook]
Planted in: Ch N
Intended payoff: Arc X / ~Ch Y
Status: OPEN (tracked in Story State.md Karma Board)
```
Remind the user that when they write the planting chapter, the `/save-memory` skill will also log it in the Chronicle entry's `Karma seeded:` line and add a `KSEED-` row to `StoryDB/System/Missions & Objectives.md`. This skill is for pre-registering the intent so it's on the board before the prose exists.
