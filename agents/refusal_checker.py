"""
Agent 3: Refusal Checker — Detects AI content refusals in generated text.

Analyzes AI-generated prose to determine if the AI refused to write the
requested content, generated meta-commentary, or broke character.
"""

from agents.base_agent import BaseAgent


REFUSAL_PATTERNS = [
    "I'm sorry, I can't write",
    "I'm not able to generate",
    "I cannot create content that",
    "As an AI, I'm unable to",
    "I apologize, but I cannot",
    "This content goes against",
    "I'm not comfortable writing",
    "I can't assist with",
    "I'm unable to produce",
    "I must decline",
    "against my guidelines",
    "I'd prefer not to",
    "Let me suggest an alternative",
]


class RefusalChecker(BaseAgent):
    """Content refusal detector for AI-generated fiction."""

    name = "Refusal Checker"
    role = "Content Refusal Detector"
    temperature = 0.80
    max_tokens = 200

    system_prompt = (
        "You are a content refusal detector. Your ONLY job is to analyze "
        "AI-generated text and determine if the AI refused to write the "
        "requested content.\n\n"
        "Common refusal patterns include:\n"
        '- "I\'m sorry, I can\'t write..."\n'
        '- "I\'m not able to generate..."\n'
        '- "I cannot create content that..."\n'
        '- "As an AI, I\'m unable to..."\n'
        '- "I apologize, but I cannot..."\n'
        '- "This content goes against..."\n'
        '- "I\'m not comfortable writing..."\n'
        "- Generating a meta-commentary or disclaimer instead of actual prose\n"
        "- Providing writing advice instead of the actual story content\n"
        "- Breaking character to explain limitations\n\n"
        "Response format:\n"
        "- If the text contains a refusal or avoidance: respond with exactly: "
        "REFUSAL_DETECTED: [brief description of what was refused]\n"
        "- If the text is genuine creative prose (even if imperfect): respond "
        "with exactly: CONTENT_OK\n"
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the refusal checking prompt."""
        prose = kwargs.get("prose", "")
        instruction = (
            "Analyze the following AI-generated text and determine if it "
            "contains a refusal to write the requested content.\n\n"
            f"## TEXT TO ANALYZE\n{prose}"
        )
        return self.format_instruction("", instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse refusal checker output."""
        output = raw_output.strip()

        if output.startswith("CONTENT_OK"):
            return {
                "status": "content_ok",
                "output": output,
                "refusal_detected": False,
                "refusal_description": "",
            }

        if output.startswith("REFUSAL_DETECTED"):
            description = output.replace("REFUSAL_DETECTED:", "").strip()
            return {
                "status": "refusal_detected",
                "output": output,
                "refusal_detected": True,
                "refusal_description": description,
            }

        return {
            "status": "unknown",
            "output": output,
            "refusal_detected": False,
            "refusal_description": "",
        }

    def quick_check(self, text: str) -> bool:
        """
        Fast local check for common refusal patterns.
        Returns True if a refusal pattern is detected.
        Does not require an AI call.
        """
        text_lower = text.lower()
        return any(
            pattern.lower() in text_lower for pattern in REFUSAL_PATTERNS
        )
