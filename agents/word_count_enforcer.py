"""
Word Count Enforcer — Validates and enforces minimum word count requirements.

Counts only actual prose words, excluding markdown headers, blank lines,
System notification markers, and formatting characters. Targets 10,000 words
per chapter with a minimum of 3,500.
"""

import re

from agents.base_agent import BaseAgent
from config import (
    MIN_WORD_COUNT,
    MIN_READING_TIME_MINUTES,
    TARGET_WORD_COUNT,
    WORDS_PER_MINUTE,
)


def count_prose_words(text: str) -> dict:
    """
    Count actual prose words in text, excluding:
    - Blank/whitespace-only lines
    - Markdown headers (lines starting with #)
    - Horizontal rules (---, ***, ___)
    - Bold/italic markdown markers (**, *, __)
    - Chapter title meta lines
    - "Word Count:" meta lines

    Returns a dict with word_count, line_count, paragraph_count,
    avg_words_per_paragraph, reading_time_minutes.
    """
    lines = text.split("\n")
    prose_words = 0
    prose_lines = 0
    paragraph_count = 0
    current_paragraph_words = 0
    paragraph_word_counts = []

    for line in lines:
        stripped = line.strip()

        # Skip blank lines
        if not stripped:
            if current_paragraph_words > 0:
                paragraph_word_counts.append(current_paragraph_words)
                paragraph_count += 1
                current_paragraph_words = 0
            continue

        # Skip markdown headers
        if stripped.startswith("#"):
            continue

        # Skip horizontal rules
        if re.match(r"^[-*_]{3,}\s*$", stripped):
            continue

        # Skip "— End of Chapter X —" lines
        if re.match(r"^\*{0,2}—\s*End of Chapter", stripped):
            continue

        # Skip "Word Count:" meta lines
        if stripped.startswith("*Word Count:") or stripped.startswith(
            "Word Count:"
        ):
            continue

        # Clean markdown formatting before counting
        cleaned = stripped
        # Remove bold/italic markers
        cleaned = re.sub(r"\*{1,3}", "", cleaned)
        cleaned = re.sub(r"_{1,2}", "", cleaned)
        # Remove inline code
        cleaned = re.sub(r"`[^`]*`", "", cleaned)
        # Remove link syntax but keep text
        cleaned = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", cleaned)

        words = cleaned.split()
        word_count = len(words)

        if word_count > 0:
            prose_words += word_count
            prose_lines += 1
            current_paragraph_words += word_count

    # Final paragraph
    if current_paragraph_words > 0:
        paragraph_word_counts.append(current_paragraph_words)
        paragraph_count += 1

    avg_per_paragraph = (
        sum(paragraph_word_counts) / len(paragraph_word_counts)
        if paragraph_word_counts
        else 0
    )
    reading_time = prose_words / WORDS_PER_MINUTE if WORDS_PER_MINUTE > 0 else 0

    return {
        "word_count": prose_words,
        "prose_lines": prose_lines,
        "paragraph_count": paragraph_count,
        "avg_words_per_paragraph": round(avg_per_paragraph, 1),
        "reading_time_minutes": round(reading_time, 1),
        "paragraph_word_counts": paragraph_word_counts,
    }


class WordCountEnforcer(BaseAgent):
    """Word count validator and enforcement agent."""

    name = "Word Count Enforcer"
    role = "Word Count Validator"
    temperature = 0.10
    max_tokens = 500

    system_prompt = (
        "You are a word count enforcer for the novel RP Conversion. "
        "Your job is to verify that generated prose meets the "
        f"minimum word count requirement of {MIN_WORD_COUNT} words "
        f"(target: {TARGET_WORD_COUNT} words, "
        f"minimum reading time: {MIN_READING_TIME_MINUTES} minutes).\n\n"
        "IMPORTANT: Count only actual prose words. Do NOT count:\n"
        "- Blank lines or whitespace\n"
        "- Markdown headers (# lines)\n"
        "- Formatting characters (**, *, __)\n"
        "- System notification markers\n"
        "- Stat block lines\n\n"
        "Paragraphs should be THICK — averaging 80+ words per paragraph.\n"
        "Chapters should aim for dense, immersive prose with:\n"
        "- Detailed sensory descriptions\n"
        "- Internal monologue and psychological depth\n"
        "- World-building woven into action\n"
        "- Character reactions and emotional processing\n\n"
        "If the word count is met:\n"
        "  Respond: WORD_COUNT_OK: [actual count] words "
        f"(target: {TARGET_WORD_COUNT})\n"
        f"  READING_TIME: [X] minutes\n"
        f"  DEPTH_SCORE: [assessment]\n\n"
        "If the word count is NOT met:\n"
        "  Respond: WORD_COUNT_FAIL: [actual count] / "
        f"{MIN_WORD_COUNT} minimum\n"
        "  DEFICIT: [number] words short\n"
        "  SUGGESTION: [specific suggestions for extending — use deeper "
        "psychological exploration, environmental detail, character "
        "interactions, System lore exposition, tactical analysis, "
        "inner conflict, sensory immersion, or secondary storylines]"
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the word count check prompt."""
        prose = kwargs.get("prose", "")
        if not isinstance(prose, str):
            prose = str(prose)
        stats = count_prose_words(prose)
        instruction = (
            f"The following prose contains {stats['word_count']} actual "
            f"prose words across {stats['paragraph_count']} paragraphs "
            f"(avg {stats['avg_words_per_paragraph']} words/paragraph). "
            f"Estimated reading time: {stats['reading_time_minutes']} min.\n"
            f"The minimum requirement is {MIN_WORD_COUNT} words. "
            f"Target is {TARGET_WORD_COUNT} words.\n"
            f"Minimum reading time: {MIN_READING_TIME_MINUTES} minutes.\n\n"
            f"Verify and provide guidance if needed."
        )
        return self.format_instruction("", instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse word count enforcer output."""
        output = raw_output.strip()
        return {
            "status": "pass" if "WORD_COUNT_OK" in output else "fail",
            "output": output,
            "meets_minimum": "WORD_COUNT_OK" in output,
        }

    def check(self, prose: str, minimum: int = MIN_WORD_COUNT) -> dict:
        """
        Local word count check — no AI call needed.
        Uses accurate prose word counting (excludes headers, blanks,
        formatting).

        Args:
            prose: The text to check.
            minimum: Minimum word count (default from config).

        Returns:
            Dict with detailed word count analysis.
        """
        stats = count_prose_words(prose)
        word_count = stats["word_count"]
        deficit = max(0, minimum - word_count)
        target_deficit = max(0, TARGET_WORD_COUNT - word_count)

        thin_paragraphs = [
            i + 1
            for i, wc in enumerate(stats["paragraph_word_counts"])
            if 0 < wc < 40
        ]

        return {
            "word_count": word_count,
            "minimum": minimum,
            "target": TARGET_WORD_COUNT,
            "meets_minimum": word_count >= minimum,
            "meets_target": word_count >= TARGET_WORD_COUNT,
            "deficit": deficit,
            "target_deficit": target_deficit,
            "paragraph_count": stats["paragraph_count"],
            "avg_words_per_paragraph": stats["avg_words_per_paragraph"],
            "reading_time_minutes": stats["reading_time_minutes"],
            "meets_reading_time": (
                stats["reading_time_minutes"] >= MIN_READING_TIME_MINUTES
            ),
            "thin_paragraphs": thin_paragraphs,
            "depth_warnings": self._get_depth_warnings(stats),
            "status": "pass" if word_count >= minimum else "fail",
            "passed": word_count >= minimum,
        }

    def _get_depth_warnings(self, stats: dict) -> list:
        """Generate warnings about prose depth issues."""
        warnings = []
        if stats["avg_words_per_paragraph"] < 40:
            warnings.append(
                f"Thin paragraphs: avg {stats['avg_words_per_paragraph']} "
                f"words/paragraph (target: 80+). Add more description, "
                f"internal monologue, and sensory detail."
            )
        if stats["reading_time_minutes"] < MIN_READING_TIME_MINUTES:
            warnings.append(
                f"Short reading time: {stats['reading_time_minutes']} min "
                f"(target: {MIN_READING_TIME_MINUTES}+ min). "
                f"Need ~{MIN_READING_TIME_MINUTES * WORDS_PER_MINUTE} words "
                f"for target reading time."
            )
        if stats["word_count"] < TARGET_WORD_COUNT:
            pct = round(stats["word_count"] / TARGET_WORD_COUNT * 100)
            warnings.append(
                f"Below target: {stats['word_count']}/{TARGET_WORD_COUNT} "
                f"words ({pct}%). Chase the 10K word target with deeper "
                f"exploration of character psychology, world mechanics, "
                f"tactical situations, and environmental immersion."
            )
        short_paras = [
            wc for wc in stats["paragraph_word_counts"] if 0 < wc < 20
        ]
        if len(short_paras) > 3:
            warnings.append(
                f"{len(short_paras)} very short paragraphs (<20 words). "
                f"Merge short paragraphs or expand with detail."
            )
        return warnings
