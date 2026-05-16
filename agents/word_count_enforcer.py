"""
Word Count Enforcer — Validates and enforces minimum word count requirements.

Checks generated prose against the configured minimum word count (default 2,500)
and provides specific guidance for extending content if it falls short.
"""

from agents.base_agent import BaseAgent
from config import MIN_WORD_COUNT


class WordCountEnforcer(BaseAgent):
    """Word count validator and enforcement agent."""

    name = "Word Count Enforcer"
    role = "Word Count Validator"
    temperature = 0.10
    max_tokens = 500

    system_prompt = (
        "You are a word count enforcer for the novel RP Conversion. "
        "Your ONLY job is to verify that generated prose meets the "
        f"minimum word count requirement of {MIN_WORD_COUNT} words.\n\n"
        "If the word count is met:\n"
        "  Respond: WORD_COUNT_OK: [actual count] words\n\n"
        "If the word count is NOT met:\n"
        "  Respond: WORD_COUNT_FAIL: [actual count] / "
        f"{MIN_WORD_COUNT} minimum\n"
        "  DEFICIT: [number] words short\n"
        "  SUGGESTION: [specific suggestions for extending the chapter "
        "without padding — use inner monologue, world-building, System "
        "notifications, environmental description, or secondary character "
        "action]"
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the word count check prompt."""
        prose = kwargs.get("prose", "")
        word_count = len(prose.split())
        instruction = (
            f"The following prose contains {word_count} words. "
            f"The minimum requirement is {MIN_WORD_COUNT} words.\n\n"
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

        Args:
            prose: The text to check.
            minimum: Minimum word count (default from config).

        Returns:
            Dict with count, meets_minimum, deficit.
        """
        word_count = len(prose.split())
        deficit = max(0, minimum - word_count)

        return {
            "word_count": word_count,
            "minimum": minimum,
            "meets_minimum": word_count >= minimum,
            "deficit": deficit,
            "status": "pass" if word_count >= minimum else "fail",
        }
