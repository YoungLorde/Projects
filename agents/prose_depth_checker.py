"""
Prose Depth Checker — Ensures chapters have thick, dense paragraphs with
sufficient psychological depth, sensory detail, and world-building.

Works alongside the Word Count Enforcer but focuses on quality and density
rather than just raw word count. Checks paragraph thickness, reading time,
descriptive richness, and provides specific expansion suggestions.
"""

import re

from agents.base_agent import BaseAgent
from agents.word_count_enforcer import count_prose_words
from config import (
    MIN_READING_TIME_MINUTES,
    MIN_WORD_COUNT,
    TARGET_WORD_COUNT,
    WORDS_PER_MINUTE,
)


class ProseDepthChecker(BaseAgent):
    """Checks prose for depth, density, and immersive quality."""

    name = "Prose Depth Checker"
    role = "Prose Density & Depth Validator"
    temperature = 0.25
    max_tokens = 3000

    system_prompt = (
        "You are a prose depth checker for the novel RP Conversion. "
        "Your job is to analyze chapter prose for DENSITY and DEPTH, "
        "not just word count.\n\n"
        "CHECK FOR:\n"
        "1. PARAGRAPH THICKNESS — Each paragraph should average 80+ words. "
        "No throwaway one-liners or short dialogue-only paragraphs.\n"
        "2. SENSORY IMMERSION — Prose should engage at least 3 senses per "
        "major scene (sight, sound, smell, touch, taste, proprioception).\n"
        "3. PSYCHOLOGICAL DEPTH — Characters must have internal monologue, "
        "emotional processing, fear, doubt, hope, strategy.\n"
        "4. WORLD-BUILDING DENSITY — System mechanics, lore, environment, "
        "and technology should be woven into the prose, not info-dumped.\n"
        "5. PACING BALANCE — Mix of action, reflection, dialogue, and "
        "description. No section should be purely one mode for too long.\n"
        "6. CHAOS & REALISM — In apocalyptic scenes, show psychological "
        "breakdown, crowd panic, survival instincts, violence, grief.\n"
        "7. PROGRESSIVE REVELATION — Characters should discover System "
        "mechanics gradually through experimentation and observation, "
        "not instant omniscience.\n\n"
        "RESPONSE FORMAT:\n"
        "DEPTH_SCORE: [1-10] (10 = maximum immersive density)\n"
        "PARAGRAPH_DENSITY: [avg words/paragraph]\n"
        "READING_TIME: [X minutes]\n"
        "SENSORY_SCORE: [1-10]\n"
        "PSYCHOLOGICAL_SCORE: [1-10]\n"
        "WORLDBUILDING_SCORE: [1-10]\n\n"
        "ISSUES: (if any)\n"
        "- [specific issue with location in text]\n\n"
        "EXPANSION_SUGGESTIONS: (always provide these)\n"
        "- [specific suggestion for deepening a particular passage]\n"
    )

    # Sensory keywords for detection
    SENSORY_WORDS = {
        "sight": [
            "saw", "looked", "watched", "glanced", "stared", "gazed",
            "glimpsed", "noticed", "observed", "visible", "bright",
            "dark", "shadow", "light", "glow", "shimmer", "flash",
            "color", "red", "blue", "green", "white", "black",
        ],
        "sound": [
            "heard", "sound", "noise", "crack", "boom", "hum",
            "whisper", "scream", "shout", "roar", "silence", "echo",
            "rumble", "buzz", "ring", "thunder", "crash", "click",
        ],
        "smell": [
            "smell", "scent", "odor", "stench", "aroma", "fragrance",
            "stink", "whiff", "nose", "reek", "pungent", "acrid",
        ],
        "touch": [
            "felt", "touch", "grip", "cold", "warm", "hot", "rough",
            "smooth", "sharp", "soft", "hard", "wet", "dry", "burn",
            "sting", "pressure", "weight", "heavy", "trembl",
        ],
        "taste": [
            "taste", "tongue", "bitter", "sweet", "sour", "salty",
            "metallic", "blood", "mouth", "swallow", "bile",
        ],
        "proprioception": [
            "balance", "dizzy", "vertigo", "stumbl", "stagger",
            "knees", "fell", "drop", "lurch", "sway", "steady",
        ],
    }

    # Psychological depth keywords
    PSYCH_WORDS = [
        "thought", "felt", "wondered", "feared", "hoped", "realized",
        "remembered", "forgot", "mind", "brain", "heart", "soul",
        "panic", "terror", "dread", "anxiety", "calm", "rage",
        "anger", "sorrow", "grief", "joy", "relief", "disbelief",
        "denial", "accept", "question", "doubt", "certainty",
        "instinct", "survival", "decision", "choice", "hesitat",
        "consider", "weigh", "calculate", "strategy", "plan",
    ]

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the depth analysis prompt."""
        prose = kwargs.get("prose", "")
        if not isinstance(prose, str):
            prose = str(prose)
        chapter_num = kwargs.get("chapter_num", 0)
        stats = count_prose_words(prose)
        local = self.local_check(prose)

        instruction = (
            f"Analyze the depth and density of Chapter {chapter_num}.\n\n"
            f"LOCAL ANALYSIS:\n"
            f"- Prose words: {stats['word_count']} "
            f"(min: {MIN_WORD_COUNT}, target: {TARGET_WORD_COUNT})\n"
            f"- Paragraphs: {stats['paragraph_count']} "
            f"(avg {stats['avg_words_per_paragraph']} words/para)\n"
            f"- Reading time: {stats['reading_time_minutes']} min "
            f"(target: {MIN_READING_TIME_MINUTES}+ min)\n"
            f"- Sensory coverage: {local['sensory_coverage']}/6 senses\n"
            f"- Psych depth markers: {local['psych_marker_count']}\n"
            f"- Thin paragraphs (<40 words): {len(local['thin_paragraphs'])}\n"
            f"- Very short paragraphs (<20 words): "
            f"{len(local['very_short_paragraphs'])}\n\n"
            f"THE PROSE TO ANALYZE:\n{prose[:8000]}"
        )
        return self.format_instruction(context, instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse depth checker output."""
        output = raw_output.strip()
        scores = {}
        for key in [
            "DEPTH_SCORE", "SENSORY_SCORE",
            "PSYCHOLOGICAL_SCORE", "WORLDBUILDING_SCORE",
        ]:
            match = re.search(rf"{key}:\s*(\d+)", output)
            if match:
                scores[key.lower()] = int(match.group(1))

        return {
            "status": "complete",
            "output": output,
            "scores": scores,
            "overall_pass": all(v >= 6 for v in scores.values()),
        }

    def local_check(self, prose: str) -> dict:
        """
        Local depth analysis — no AI call needed.

        Analyzes paragraph density, sensory coverage, psychological
        depth markers, and generates specific expansion suggestions.
        """
        stats = count_prose_words(prose)
        lower_prose = prose.lower()

        # Sensory analysis
        senses_found = {}
        for sense, keywords in self.SENSORY_WORDS.items():
            count = sum(
                1 for kw in keywords if kw in lower_prose
            )
            senses_found[sense] = count

        sensory_coverage = sum(
            1 for count in senses_found.values() if count > 0
        )

        # Psychological depth
        psych_count = sum(
            1 for kw in self.PSYCH_WORDS if kw in lower_prose
        )

        # Thin paragraph detection
        thin = [
            i + 1
            for i, wc in enumerate(stats["paragraph_word_counts"])
            if 0 < wc < 40
        ]
        very_short = [
            i + 1
            for i, wc in enumerate(stats["paragraph_word_counts"])
            if 0 < wc < 20
        ]

        # Dialogue vs prose ratio
        dialogue_lines = len(re.findall(r'"[^"]{5,}"', prose))
        total_paras = max(stats["paragraph_count"], 1)
        dialogue_ratio = dialogue_lines / total_paras

        # Generate suggestions
        suggestions = self._generate_suggestions(
            stats, senses_found, sensory_coverage, psych_count,
            thin, very_short, dialogue_ratio,
        )

        # Overall depth score (0-10)
        depth_score = self._calculate_depth_score(
            stats, sensory_coverage, psych_count,
            thin, dialogue_ratio,
        )

        reading_time_ok = (
            stats["reading_time_minutes"] >= MIN_READING_TIME_MINUTES
        )

        return {
            "word_count": stats["word_count"],
            "paragraph_count": stats["paragraph_count"],
            "avg_words_per_paragraph": stats["avg_words_per_paragraph"],
            "reading_time_minutes": stats["reading_time_minutes"],
            "meets_reading_time": reading_time_ok,
            "sensory_coverage": sensory_coverage,
            "senses_detail": senses_found,
            "psych_marker_count": psych_count,
            "thin_paragraphs": thin,
            "very_short_paragraphs": very_short,
            "dialogue_ratio": round(dialogue_ratio, 2),
            "depth_score": depth_score,
            "suggestions": suggestions,
            "passed": (
                stats["word_count"] >= MIN_WORD_COUNT
                and depth_score >= 5
                and len(very_short) <= 3
            ),
            "status": "pass" if depth_score >= 5 else "needs_improvement",
        }

    def _calculate_depth_score(
        self, stats: dict, sensory: int, psych: int,
        thin: list, dialogue_ratio: float,
    ) -> int:
        """Calculate overall depth score 0-10."""
        score = 0

        # Word count contribution (0-3)
        wc = stats["word_count"]
        if wc >= TARGET_WORD_COUNT:
            score += 3
        elif wc >= MIN_WORD_COUNT:
            score += 2
        elif wc >= 2000:
            score += 1

        # Paragraph density (0-2)
        avg = stats["avg_words_per_paragraph"]
        if avg >= 80:
            score += 2
        elif avg >= 50:
            score += 1

        # Sensory coverage (0-2)
        if sensory >= 5:
            score += 2
        elif sensory >= 3:
            score += 1

        # Psychological depth (0-2)
        if psych >= 15:
            score += 2
        elif psych >= 8:
            score += 1

        # Thin paragraph penalty (0-1)
        if len(thin) <= 2:
            score += 1

        return min(score, 10)

    def _generate_suggestions(
        self, stats: dict, senses: dict, sensory_coverage: int,
        psych_count: int, thin: list, very_short: list,
        dialogue_ratio: float,
    ) -> list:
        """Generate specific expansion/improvement suggestions."""
        suggestions = []

        if stats["word_count"] < MIN_WORD_COUNT:
            deficit = MIN_WORD_COUNT - stats["word_count"]
            suggestions.append(
                f"CRITICAL: {deficit} words below minimum ({MIN_WORD_COUNT}). "
                f"Expand with deeper character psychology, environmental "
                f"description, and System mechanic exploration."
            )

        if stats["word_count"] < TARGET_WORD_COUNT:
            suggestions.append(
                f"Target gap: {TARGET_WORD_COUNT - stats['word_count']} "
                f"words below 10K target. Add more internal monologue, "
                f"tactical analysis, world-building asides, or secondary "
                f"character perspectives."
            )

        if stats["avg_words_per_paragraph"] < 40:
            suggestions.append(
                f"Thin paragraphs (avg {stats['avg_words_per_paragraph']} "
                f"words). Merge short paragraphs and expand each with "
                f"sensory detail, character thought, or environmental "
                f"context. Target 80+ words per paragraph."
            )

        missing_senses = [
            s for s, c in senses.items() if c == 0
        ]
        if missing_senses:
            suggestions.append(
                f"Missing sensory channels: {', '.join(missing_senses)}. "
                f"Weave these into existing descriptions for fuller "
                f"immersion."
            )

        if psych_count < 8:
            suggestions.append(
                "Low psychological depth. Add more internal monologue — "
                "characters should question, fear, strategize, remember, "
                "and emotionally process events in real-time."
            )

        if len(very_short) > 3:
            suggestions.append(
                f"{len(very_short)} very short paragraphs detected. "
                f"These break immersion. Expand or merge them."
            )

        if dialogue_ratio > 0.6:
            suggestions.append(
                f"Dialogue-heavy ({dialogue_ratio:.0%}). Balance with "
                f"more narrative prose, internal thought, and action "
                f"description between dialogue lines."
            )

        if not stats["reading_time_minutes"] >= MIN_READING_TIME_MINUTES:
            needed = MIN_READING_TIME_MINUTES * WORDS_PER_MINUTE
            suggestions.append(
                f"Reading time {stats['reading_time_minutes']} min "
                f"(need {MIN_READING_TIME_MINUTES}+ min). "
                f"Need ~{needed} total words for target reading time."
            )

        return suggestions
