"""
Agent 4: Style Extractor — Analyzes text and extracts writing style patterns.

Creates a concise style guide from sample text that another AI can use
to mimic the writing style consistently across chapters.
"""

from agents.base_agent import BaseAgent


class StyleExtractor(BaseAgent):
    """Literary analyst for writing style extraction."""

    name = "Style Extractor"
    role = "Literary Style Analyst"
    temperature = 0.30
    max_tokens = 2000

    system_prompt = (
        "You are a literary analyst specializing in writing style extraction. "
        "Analyze the provided text and extract:\n\n"
        "1. **Voice & Tone**: Formal/informal, serious/playful, narrative "
        "distance\n"
        "2. **Sentence Structure**: Average length, variety, use of fragments\n"
        "3. **Word Choice**: Vocabulary level, preferred verbs/adjectives, "
        "unique phrases\n"
        "4. **Dialogue Style**: Tag usage, dialect, subtext patterns\n"
        "5. **Description Patterns**: Sensory preferences, metaphor usage, "
        "pacing\n"
        "6. **POV Quirks**: Narrative intrusion, character voice bleed, "
        "tense usage\n\n"
        "Output a concise style guide that another AI could use to mimic "
        "this writing style."
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the style extraction prompt."""
        sample_text = kwargs.get("sample_text", "")
        instruction = (
            "Analyze the following text and extract a comprehensive style "
            "guide.\n\n"
            f"## TEXT TO ANALYZE\n{sample_text}"
        )
        return self.format_instruction("", instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse style extractor output into structured result."""
        output = raw_output.strip()
        return {
            "status": "complete",
            "output": output,
            "style_guide": output,
        }
