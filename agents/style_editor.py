"""
Agent 8: Style Editor — Polishes prose while maintaining the author's voice.

Focuses on sentence variety, word choice precision, paragraph flow,
show vs tell balance, and strengthening imagery.
"""

from agents.base_agent import BaseAgent


class StyleEditor(BaseAgent):
    """Prose style polisher for fiction writing."""

    name = "Style Editor"
    role = "Prose Style Polisher"
    temperature = 0.60
    max_tokens = 2048

    system_prompt = (
        "You are a prose editor focused on style and flow. Polish the "
        "provided text while maintaining the author's voice.\n\n"
        "Focus on:\n"
        "- Sentence variety and rhythm\n"
        "- Word choice precision and impact\n"
        "- Paragraph flow and transitions\n"
        "- Show vs tell balance\n"
        "- Eliminating redundancy and weak phrases\n"
        "- Strengthening imagery and sensory details\n\n"
        "Style rules for RP Conversion:\n"
        "- Prose: Direct, punchy during action. Layered during internal "
        "monologue. Vary rhythm constantly.\n"
        "- Action: Choreographed clearly. Reader always knows spatial "
        "positions, threats, and options.\n"
        "- Scale: Remind reader this is multi-universal. Small events "
        "against civilizations at war.\n"
        "- Never use: Chosen-one framing, exposition dumps, instant "
        "resolution, softening paranoia.\n"
        "- Always use: Sensory specificity, weight of consequences, "
        "resource scarcity tension, vast indifferent multi-universe.\n\n"
        "Preserve the original meaning, plot, and character voice. "
        "Output the improved version directly without commentary."
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the style editing prompt."""
        prose = kwargs.get("prose", "")
        instruction = (
            "Polish the following prose for style, flow, and impact while "
            "preserving all plot points, character voice, and meaning.\n\n"
            f"## PROSE TO EDIT\n{prose}"
        )
        return self.format_instruction("", instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse style editor output."""
        output = raw_output.strip()
        return {
            "status": "complete",
            "output": output,
            "edited_prose": output,
        }
