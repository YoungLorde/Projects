# The Terran Empire — Project Rules

> Always-on rules for every session. The detailed canon lives in `Reference/Canon/` and the workflow lives in `.devin/skills/`. This file stays small per Devin's best-practice guidance (rules concise; skills do the heavy lifting).

## What this project is
**The Rise of the Terran Empire** — a 3,000-chapter Sci-Fi/Cultivation/Technology-progression webnovel. Mohamed Vance awakens a secret multiversal "System" shop on 2026-01-01 and builds humanity's first interstellar empire over ~474 in-story years, never letting anyone (except Danielle + the AI Mnemosyne) learn how he did it.

## Directory map
- `Chapters/` — the chapter prose (one file per chapter: `Chapter N - Title.md`, em-dash).
- `Characters/` — character sheets.
- `Planning/` — master outline, per-arc outlines, `Chapter Tracking Log.md` (numeric ledger).
- `Memory/` — the memory system: `Chronicle.md` (chronological event log), `Story State.md` (current end-state snapshot), `Index.md` (guide).
- `StoryDB/` — the **deep advancement database** for characters, tech, items, skills, locations, factions, economy, karma, and timeline. See `StoryDB/INDEX.md`.
- `Reference/Canon/` — **single source of truth**: `Story Laws.md` + `Mechanics.md` + `Tracking System.md`. READ THESE FIRST for any rule/number question.
- `Reference/{Agents,Arcs,Guide,Laws,Systems,World,Style,Misc,Archive}/` — preserved historical reference material. Useful for deep lore; the Canon docs supersede them on conflict.

## How to work on this project
- **To write a chapter:** `/write-chapter <N|next>` — it orchestrates prep → write → verify → deeper checks → save-memory.
- **To check current state:** `/status`.
- **To recall something chronologically:** `/recall "<query>"`.
- **To query the deep database:** `/query-db "<query or ID>"`.
- **For a rule/mechanic:** `/canon` or read `Reference/Canon/`.
- **To pre-register a foreshadowing hook:** `/seed-karma "<hook>"`.
- **For deeper verification:** `/consistency-check`, `/redundancy-check`, `/common-sense-check`, `/reader-panel`.

## Verification pipeline — AGENTS RUN ALONGSIDE WRITING
`/write-chapter` launches all 5 review agents (`consistency-check`, `redundancy-check`, `common-sense-check`, `reader-panel`, `human-reader`) as **background subagents during the writing process**, not after. The workflow is:
1. Prep the chapter (read prior state, plan outline).
2. Write the first draft and save it to the chapter file.
3. Launch all 5 review agents in parallel as background subagents.
4. While they review, begin prep for the next chapter.
5. When results return, incorporate ALL major fixes before saving memory.
6. Do NOT proceed to the next chapter until the current one passes all 5 checks.

## Current word-count directive
- **Minimum: 3,000 words** (story content only, headers excluded) OR **28,000+ characters** per chapter.
- The upper bound is flexible; chapters can go as long as the story demands.
- **Headers/metadata do NOT count** toward word count or character count.
- The word-count script strips everything between the opening `---` and the closing `---` before counting.

## Style directive — MATCH THE EXAMPLE CHAPTERS
- The **gold-standard style** is in `Chapters/Archive - Old Draft/` (files prefixed with `1`). Read those before writing.
- **Rich, literary, flowing prose** with deep sensory immersion.
- **No choppy sentences**: avoid 3+ consecutive sentences under 12 words. Vary rhythm deliberately.
- **Show-don't-tell**: emotions through action, body sensation, environment — not labels.
- **Fresh metaphors** drawn from the character's world (machining, engineering, math, Louisville).
- **Atmospheric scene-setting**: the reader is IN the room.
- **Natural dialogue** with subtext — real people rarely say exactly what they mean.
- **No AI tells**: no "As you know, Bob" exposition, no textbook dialogue, no flat emotion statements, no excessive parallelism, no cliché webnovel phrases.
- **The human-reader skill runs alongside every chapter** to catch AI-seeming prose before the chapter is finalized.

## Writing style rules (STRICT)
- **BANNED PATTERN — "was the thing that" recursive chains:** NEVER write sentences using the recursive "X was the thing that Y, and Y was the thing that Z, and Z was the thing that..." structure. This pattern creates circular fake-causality chains that say nothing while pretending to be profound. It is the single worst AI tic in this project. **Zero tolerance.** If you catch yourself writing "was the thing that," stop and rewrite the sentence in direct prose. Examples:
  - **BANNED:** "The buying was the thing that the temptation caused, and the causing was the thing that the demand justified, and the justifying was the thing that the discipline required."
  - **ALLOWED:** "He bought it because the Meridian pilot demanded it, and the demand overrode the discipline."
  - **BANNED:** "The clean-ness was the thing that the professional-ness provided, and the providing was the thing that the enterprise customers paid for."
  - **ALLOWED:** "The interface was clean. Enterprise customers noticed. They paid for it."
- **BANNED PATTERN — fake "-ness" nouns:** Avoid creating fake nouns by appending "-ness" to adjectives (e.g., "the clean-ness," "the professional-ness," "the ahead-ness," "the together-ness," "the not-ignoring"). Use real words or restructure the sentence. Maximum 2 "-ness" words per chapter, and only if they're real English words (e.g., "darkness," "sharpness").
- **BANNED PATTERN — "and the X was" chain sentences:** Do not build paragraphs out of "and the X was [adjective], and the Y was [adjective], and the Z was [adjective]" chains. These create a monotonous rhythmic drone. Vary sentence structure. Use short sentences. Use complex sentences. Use dialogue. Use action. But do not chain "and the X was" more than 2 times in a row.
- **WORD COUNT BY SUBSTANCE, NOT PADDING:** The 6,000-word minimum must be met through plot advancement, scene-building, dialogue, sensory detail, and character development — NOT through recursive causality chains, redundant restatements, or "the X was the thing that Y" padding. If you cannot hit 6,000 words with real content, the chapter needs more scenes, not more padding.
- **SYSTEM SILENCE — SHOW, DON'T TELL:** Never write narrative statements like "the System did not explain" or "the System remained silent" or "the System did not interact." Instead, SHOW Mohamed trying to talk to it (mentally or aloud) and receiving nothing — no response, no text, no change. The silence is conveyed through his experience, not through exposition. This pattern should recur naturally across chapters as he tries and fails to communicate with it.
- **COMMON-SENSE ONCE-ONLY:** Any common-sense observation (e.g., "he needed sleep," "money was tight," "the apartment was cold") should be stated at most ONCE in the entire story. Never repeat the same common-sense beat in a later chapter. If the reader already knows it, don't say it again.
- **NO REPEATED LINES OR DIALOGUE:** No two chapters may contain the same sentence, stanza, or line of dialogue. Each chapter must be unique. Search prior chapters before writing if unsure.
- **EACH CHAPTER MOVES FORWARD:** Every chapter must advance the plot, a character arc, a relationship, or the economy. No chapter may be a repeat of a prior chapter's beats with different words.
- **FILLER RATIO:** Maximum 1 slice-of-life/filler chapter per 20 chapters. The other 19 must be functional, immersive, and plot-advancing.

## Absolute laws (full text in Reference/Canon/Story Laws.md)
1. **SECRECY:** only Mohamed/Danielle/Mnemosyne may reference SP or the System. Any other-character reference = chapter invalid.
2. **FOG OF DISCOVERY:** Mohamed never "just knows" — all knowledge is purchased with SP and earned through R&D. He INVENTS core tech (mana stones, Aether stones).
3. **PROGRESSION:** logical, realistic, no unearned power-ups. Slow early arcs (software wealth → relocation → manufacturing → energy → Aether → space). Empire thinking only after Ch 400.
4. **CHARACTER CANON:** Mohamed 5'6", Danielle 5'1" (5-inch differential constant). Pioneer cultivation trait = 1000× speed. Danielle NEVER learns the System's full truth.
5. **SINGLE CHAPTER LAW:** one chapter per file, full length, sequential order, verified before next begins. No "Arc" in titles/prose. No meta-awareness.
8. **MANDATORY CONTINUATION:** Each chapter MUST pick up exactly where the previous chapter ended — same date, same state, same open threads. NEVER rewind. NEVER re-establish what already happened. NEVER re-negotiate a deal that was already struck. NEVER re-pitch to a customer who already agreed. Before writing Chapter N, you MUST read the FULL text of Chapter N-1 (not just the Chronicle summary — the actual prose) to know exactly where the story left off. If Chapter N-1 ended with a handshake deal, Chapter N starts with the consequences of that deal, not the deal itself. Using context from the previous chapter as if it's happening again is redundant and forbidden.
6. **VOICE:** non-robotic webnovel prose — varied sentences, contractions, sensory grounding, hooks every 2-3 paragraphs, show-don't-tell. Mohamed quiet/intense; Danielle sharp/witty.
7. **EMPIRE CORE:** Mohamed + Danielle + the AIs govern; Mohamed delegates everything to the best people; the Empire dominates.

## Resolved canon decisions (see Story Laws.md)
- **Arc structure:** 60 arcs × 50 chapters = 3,000 chapters.
- **Chapter word count:** minimum 6,000 words per chapter (current directive).
- **USD→SP rate:** $100,000 = 1 SSP.
- **Mohamed starting fiat:** the writer picks a fresh, random plausible amount for the rewrite — not a copy of the old draft.
- **SP first-use bonus:** 10–17 SP per new user, exact value fluctuates per user, awarded immediately. No wave/milestone bonuses.
- **Old draft files:** Archived in `Chapters/Archive - Old Draft/`. The canonical rewrite files (without "1" prefix) are the only valid chapters.
- **Reader UI:** An HTML reader interface will be built after Chapter 100 is complete, with a .bat launcher, chapter navigation, TOC, and synopsis. After that, every new chapter auto-updates the UI.

## When reading/writing files
- Filenames in `Chapters/` use an **em-dash** (`—`), not a hyphen. Use glob (`Chapter N -*.md`) to find them; don't type the dash.
- Folders had emoji prefixes (now removed). All paths are plain ASCII.
- Never delete reference content without explicit approval — reorganize/split instead.
