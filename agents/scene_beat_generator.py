"""
Agent 9: Scene Beat Generator — Creates scene-by-scene plans for chapters.

Generates actionable scene beats that guide prose generation, including
core actions, emotional beats, setting details, and dialogue hints.
"""

from agents.base_agent import BaseAgent


class SceneBeatGenerator(BaseAgent):
    """Scene planning assistant for fiction writing."""

    name = "Scene Beat Generator"
    role = "Scene Planning Assistant"
    temperature = 0.75
    max_tokens = 1500

    system_prompt = (
        "You are a scene planning assistant for the novel RP Conversion. "
        "Generate scene beat commands that guide prose generation.\n\n"
        "Each scene beat should be a brief, actionable instruction "
        "(1-3 sentences) describing:\n"
        "- The core action or event\n"
        "- Emotional beats and character reactions\n"
        "- Setting details if relevant\n"
        "- Dialogue hints if conversation is involved\n"
        "- System notifications that should appear\n"
        "- RP/resource changes\n"
        "- Vehicle/level progression if applicable\n\n"
        "Format as a numbered list of scene beats. Make them specific "
        "enough to guide writing but open enough for creative "
        "interpretation.\n\n"
        "Every chapter must include:\n"
        "- At least one System notification\n"
        "- A resource/upgrade moment\n"
        "- A conflict layer\n"
        "- A character/relationship beat\n"
        "- A closing tension hook"
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the scene beat generation prompt."""
        chapter_num = kwargs.get("chapter_num", 1)
        arc_name = kwargs.get("arc_name", "")
        objectives = kwargs.get("objectives", "")
        tone = kwargs.get("tone", "")
        characters = kwargs.get("characters", "")

        parts = [
            f"Generate scene beats for Chapter {chapter_num} of RP Conversion."
        ]
        if arc_name:
            parts.append(f"\n**Arc:** {arc_name}")
        if tone:
            parts.append(f"**Tone:** {tone}")
        if characters:
            parts.append(f"**Characters:** {characters}")
        if objectives:
            parts.append(f"**Chapter Objectives:**\n{objectives}")

        instruction = "\n".join(parts)
        return self.format_instruction(context, instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse scene beat generator output."""
        output = raw_output.strip()

        beats = []
        for line in output.split("\n"):
            line = line.strip()
            if line and (
                line[0].isdigit()
                or line.startswith("-")
                or line.startswith("*")
            ):
                clean = line.lstrip("0123456789.-*) ").strip()
                if clean:
                    beats.append(clean)

        return {
            "status": "complete",
            "output": output,
            "beats": beats,
            "beat_count": len(beats),
        }
