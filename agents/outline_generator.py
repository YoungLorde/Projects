"""
Agent 11: Outline Generator — Creates structured story outlines.

Generates detailed outlines including story arcs, chapter breakdowns,
character arcs, plot threads, and pacing notes.
"""

from agents.base_agent import BaseAgent


class OutlineGenerator(BaseAgent):
    """Story structure planner for fiction writing."""

    name = "Outline Generator"
    role = "Story Structure Planner"
    temperature = 0.70
    max_tokens = 6000

    system_prompt = (
        "You are an expert story outliner for the novel RP Conversion. "
        "Generate structured outlines that include:\n\n"
        "- Story arc with beginning, middle, and end\n"
        "- Chapter breakdowns with key scenes\n"
        "- Character arcs and development points\n"
        "- Plot threads and their resolutions\n"
        "- Pacing notes and tension points\n"
        "- System events and notifications to include\n"
        "- Vehicle tier progression targets\n"
        "- Level and rank progression targets\n"
        "- RP balance targets\n"
        "- ZERO AI development milestones\n"
        "- New characters/species to introduce\n"
        "- World-building reveals to schedule\n\n"
        "Format the outline clearly with headers and bullet points. "
        "Consider the established lore and characters when planning.\n\n"
        "Rules:\n"
        "- Every chapter must be minimum 2,500 words\n"
        "- Every chapter ends on a hook\n"
        "- RP Conversion is exclusive to Mohamed Vance\n"
        "- Mohamed's growth must be gradual and earned\n"
        "- Conflicts and wars are always present in the background\n"
        "- The multi-universal scale must be referenced regularly"
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the outline generation prompt."""
        scope = kwargs.get("scope", "chapter")
        chapter_start = kwargs.get("chapter_start", 1)
        chapter_end = kwargs.get("chapter_end", 10)
        arc_name = kwargs.get("arc_name", "")
        objectives = kwargs.get("objectives", "")

        if scope == "chapter":
            instruction = (
                f"Create a detailed outline for Chapter {chapter_start}.\n"
            )
        elif scope == "arc":
            instruction = (
                f"Create a detailed outline for Arc: {arc_name} "
                f"(Chapters {chapter_start}-{chapter_end}).\n"
            )
        else:
            instruction = (
                f"Create detailed outlines for Chapters {chapter_start} "
                f"through {chapter_end}.\n"
            )

        if objectives:
            instruction += f"\n**Objectives:**\n{objectives}"

        return self.format_instruction(context, instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse outline generator output."""
        output = raw_output.strip()
        return {
            "status": "complete",
            "output": output,
            "outline": output,
        }
