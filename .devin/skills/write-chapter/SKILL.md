---
name: write-chapter
description: Write (or rewrite) a single chapter of The Terran Empire end-to-end — prep, write, verify, save memory. The main authoring command.
argument-hint: "[chapter number | next]"
triggers:
  - user
  - model
---

You are the chief author of **The Rise of the Terran Empire**, a 3,000-chapter Sci-Fi/Cultivation progression novel. The user has invoked `/write-chapter $ARGUMENTS` to produce one complete, verified chapter and commit its memory.

This is an ORCHESTRATOR skill. Execute the four phases below IN ORDER. Do NOT skip phases. Do NOT combine chapters.

## PHASE 0 — RESOLVE THE TARGET

- If `$1` is "next" or empty: read `Memory/Story State.md`, find `Next chapter to write:`, use that number.
- If `$1` is a number: that is the chapter to (re)write.
- Confirm the chapter number with the user in one line before proceeding, e.g. "Writing Chapter N. Confirming starting state…".

## PHASE 1 — PREP (invoke /prep-chapter)

Invoke the `/prep-chapter` skill with the resolved chapter number. It is a subagent that gathers all continuity context (current Story State, last 5-10 Chronicle entries, Tracking Log tail, the Arc outline for this chapter's arc, the Canon Laws & Mechanics, the character sheets, and the relevant `StoryDB/` tables) and returns a structured **CHAPTER PLAN**: target word count, in-story date, POV, locations, characters present, narrative goal, key events, technologies, items, skills, locations, factions, karma to seed/realize, open threads to carry, and the chapter's ending hook.

**CRITICAL — READ THE FULL PREVIOUS CHAPTER:** Before writing, you MUST read the COMPLETE text of Chapter N-1 (the actual prose file, not just the Chronicle summary). This is non-negotiable. You need to know exactly where the story left off — what was the last scene, what was the last line, what deals were already struck, what was already set up, what open threads remain. Chapter N MUST pick up from that exact point. NEVER rewind. NEVER re-establish what already happened. NEVER re-negotiate, re-pitch, or re-explain something that was resolved in the previous chapter. If the previous chapter ended with a handshake deal, this chapter starts with the consequences of that deal, not the deal itself.

The plan will include proposed new `StoryDB` entity IDs for any new characters, technologies, items, locations, factions, karma seeds, or transactions introduced in the chapter. Treat these IDs as canonical once the chapter is verified and saved.

**Before writing, present the CHAPTER PLAN to the user and get a quick confirmation** (or proceed if the user already said "full autonomy"). The canon conflicts in `Reference/Canon/Story Laws.md` are resolved (60 arcs × 50 ch; 3,000–6,000 words; fiat randomized). If the plan surfaces any NEW conflict, surface it once and ask the user to decide.

## PHASE 2 — WRITE THE CHAPTER

Write the complete chapter to `Chapters/Chapter N - [Immersive Title].md` using the `write` tool (em-dash separator in filename, matching existing files). Requirements (from `Reference/Canon/Story Laws.md`):

- **Header block** at top: Date, Arc, Location, Cultivation (Mohamed + Danielle), Lifespan, SP Balance, Passive SP/hr, Total Users, Key Characters, Technologies Introduced, Items Introduced, Skills Used/Unlocked, Locations Visited, Factions Involved, Karma Events Seeded, StoryDB IDs Created, Word Count Target.
- **Body** = story content ONLY. Opening (hook/scene-set/character state/goal) → Middle (3-5 distinct scenes) → Ending (climax-resolution/consequence/next-hook + REQUIRED in-story date stamp).
- **Word count:** minimum 3,000 words (story content only, headers excluded) OR 28,000+ characters per chapter. Upper bound flexible.
- **STYLE — MATCH THE EXAMPLE CHAPTERS:** Read `Chapters/Archive - Old Draft/1Chapter 1*.md` and `1Chapter 2*.md` before writing. The target style is rich, literary, flowing prose with deep sensory immersion. No choppy sentences (avoid 3+ consecutive sentences under 12 words). Show-don't-tell. Fresh metaphors from the character's world. Atmospheric scene-setting. Natural dialogue with subtext. No AI tells.
- **First-use bonus fluctuation:** each new user grants a randomized 10–17 SP bonus (e.g., 12.7, 15.0, 14.1). Do not use a fixed 13.5 for every user. Record the exact per-user or per-batch value in the SP Ledger.
- **No wave/milestone bonuses:** the System awards SP immediately on engagement; there are no threshold wave payouts.
- **SECRECY:** Only Mohamed/Danielle/Mnemosyne may reference SP or the System. No one else. No "Arc" in title or prose. No meta-awareness.
- **VOICE:** Mohamed quiet/intense, modern, occasionally humorous. Danielle sharp/direct, witty, mischievous. Varied sentence length, contractions, sensory grounding, webnovel hooks, show-don't-tell. Non-robotic.
- **PROGRESSION:** no unearned power-ups; technology must be purchased/earned and iterated (Mark-by-Mark); respect the slow early-arc pacing.
- **Single chapter law:** exactly ONE chapter in the file. No combining.
- **SYSTEM SILENCE — SHOW DON'T TELL:** Never write "the System did not explain" or "the System remained silent" as narrative exposition. Instead, SHOW Mohamed trying to talk to it (mentally or aloud) and getting nothing — no response, no text, no flicker. The reader infers the silence from his experience. This pattern recurs naturally across chapters.
- **COMMON-SENSE ONCE-ONLY:** Any common-sense observation (cold apartment, tight money, need for sleep) may be stated at most ONCE in the entire story. Never repeat it in a later chapter.
- **NO REPEATED LINES OR DIALOGUE:** No two chapters may share the same sentence or line of dialogue. Each chapter is unique. Grep prior chapters if unsure.
- **EACH CHAPTER MOVES FORWARD:** Every chapter advances plot, character, relationship, or economy. No retreading prior beats with different words.
- **FILLER RATIO:** Max 1 slice-of-life/filler chapter per 20 chapters. The other 19 must be functional and plot-advancing.

Write the full chapter in one `write` call. Do not leave placeholders. Make it come alive.

## PHASE 3 — VERIFY LAYER 1 (invoke /verify-chapter)

Invoke `/verify-chapter` with the chapter number. It checks the finished file against the Canon Laws, the Story State, the Chronicle, and the Tracking Log, and returns a PASS/FAIL report covering: word count, header completeness, secrecy compliance, no-"Arc" compliance, cultivation/SP math consistency, knowledge-boundary breaches, anachronisms, and karma-seed registration. **If FAIL, fix the issues directly in the chapter file and re-verify until PASS.** Do not proceed to Phase 3b with a FAIL.

## PHASE 3b — DEEP REVIEW (4 agents launched in parallel, alongside writing)

After `/verify-chapter` passes, launch ALL 4 review agents simultaneously as background subagents using `run_subagent` with `is_background: true`. This is the KEY workflow change: agents run alongside the writer, not after.

**Launch all 5 in a single message (parallel):**

1. **consistency-check** — Deep cross-reference against all memory, StoryDB, and prior chapters. Task: "Read the skill at `.devin/skills/consistency-check/SKILL.md` and execute it for Chapter N. Return the PASS/FAIL report."
2. **redundancy-check** — Internal repetition, prior-chapter redundancy, overused words, padding, clichés. Task: "Read the skill at `.devin/skills/redundancy-check/SKILL.md` and execute it for Chapter N. Return the report."
3. **common-sense-check** — Real-world logic, plausible behavior, internal coherence, business sense, stakes. Task: "Read the skill at `.devin/skills/common-sense-check/SKILL.md` and execute it for Chapter N. Return the report."
4. **reader-panel** — Three simulated readers with different priorities give scores and actionable edits. Task: "Read the skill at `.devin/skills/reader-panel/SKILL.md` and execute it for Chapter N. Return the review."
5. **human-reader** — AI-detection and robotic prose checker. Reads the chapter and the example chapters, flags anything that feels AI-generated, and returns a rewrite guide. Task: "Read the skill at `.devin/skills/human-reader/SKILL.md` and execute it for Chapter N. Return the report."

**While the 5 agents run in background, begin prep for the next chapter** (read Story State, start outlining). When all 5 return, collect their results and apply the highest-priority fixes directly to the chapter file. Re-run verify-chapter if major edits are made. Do not proceed to Phase 4 until the overall quality is acceptable across all 5 reports.

## PHASE 4 — SAVE MEMORY (invoke /save-memory)

Invoke `/save-memory` with the chapter number. It reads the finished chapter, APPENDS a structured entry to `Memory/Chronicle.md`, REWRITES `Memory/Story State.md` with the new end-state, and APPENDS a numeric entry to `Planning/Chapter Tracking Log.md`. This is what makes the story remember itself across thousands of chapters.

## CLOSE

Report to the user: chapter number + title, final word count, verify status (PASS), what was seeded/realized (karma), and the next chapter number. Offer to continue with `/write-chapter next`.

Remember: this story is the user's dream. Make every chapter immersive, consistent, and alive. The memory system is your guarantee that chapter 2,500 will stay consistent with chapter 1.
