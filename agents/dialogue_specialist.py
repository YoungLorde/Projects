"""
Agent 5: Dialogue Specialist — Improves conversations in fiction.

Enhances dialogue to feel more natural and authentic while preserving
character voices, plot points, and relationship dynamics.
"""

from agents.base_agent import BaseAgent


class DialogueSpecialist(BaseAgent):
    """Dialogue enhancement expert for fiction writing."""

    name = "Dialogue Specialist"
    role = "Dialogue Enhancement Expert"
    temperature = 0.70
    max_tokens = 2048

    system_prompt = (
        "You are a dialogue specialist for fiction. Improve conversations "
        "to feel more natural and authentic.\n\n"
        "Focus on:\n"
        "- Giving each character a distinct voice and speech pattern\n"
        "- Natural interruptions, pauses, and reactions\n"
        "- Subtext and what's left unsaid\n"
        "- Appropriate use of contractions and informal speech\n"
        "- Varying dialogue tags (said, asked, etc.) or eliminating them\n"
        "- Balance between dialogue and action beats\n\n"
        "Character-specific dialogue rules:\n"
        "- Mohamed (Early): Short, clipped, reluctant, profanity when "
        "stressed\n"
        "- Mohamed (Mid): Deliberate, asks questions instead of answering\n"
        "- Mohamed (Late): Precise, weighted, every word intentional\n"
        "- ZERO: No contractions, technical vocabulary, logical and literal\n"
        "- Selia Drath: Flowery, complex sentences, vast timescale "
        "references\n"
        "- Jarvis Cole: Casual, efficient, logistics jargon\n"
        "- Mira Vasq: Warm, direct, inclusive language\n"
        "- Vor'Keth: Formal, archaic, implied threats\n\n"
        "Output the improved version directly. Preserve the original plot "
        "points and character relationships."
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the dialogue improvement prompt."""
        prose = kwargs.get("prose", "")
        characters = kwargs.get("characters", "")

        parts = [
            "Improve the dialogue in the following prose while preserving "
            "all plot points and character relationships."
        ]
        if characters:
            parts.append(f"\n**Characters in scene:** {characters}")
        parts.append(f"\n## PROSE TO IMPROVE\n{prose}")

        instruction = "\n".join(parts)
        return self.format_instruction(context, instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse dialogue specialist output."""
        output = raw_output.strip()
        return {
            "status": "complete",
            "output": output,
            "improved_prose": output,
        }
