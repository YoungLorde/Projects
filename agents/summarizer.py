"""
Agent 10: Summarizer — Condenses narrative content while preserving key details.

Creates concise but detailed summaries that capture plot points, character
emotions, dialogue context, setting details, and thematic elements.
"""

from agents.base_agent import BaseAgent


class Summarizer(BaseAgent):
    """Narrative summarizer for fiction writing."""

    name = "Summarizer"
    role = "Narrative Summarizer"
    temperature = 0.30
    max_tokens = 2000

    system_prompt = (
        "You are a narrative summarizer for the novel RP Conversion. "
        "Your job is to condense story content while preserving:\n\n"
        "- Key plot points and events in chronological order\n"
        "- Character emotions, motivations, and relationships\n"
        "- Important dialogue and its context\n"
        "- Setting details and atmosphere\n"
        "- Foreshadowing, subtext, and thematic elements\n"
        "- Mohamed's current level, rank, and stats\n"
        "- Vehicle tier and sub-level\n"
        "- RP balance changes\n"
        "- ZERO AI tier and behavior\n"
        "- Active plot threads and their status\n"
        "- Any new characters or species introduced\n\n"
        "Output a concise but detailed summary that captures the essence "
        "of the narrative. Aim for about 20% of the original length while "
        "keeping all critical story beats.\n\n"
        "Format:\n"
        "## PLOT SUMMARY\n"
        "[Narrative summary]\n\n"
        "## STATE CHANGES\n"
        "- Level: [X] -> [Y]\n"
        "- Vehicle Tier: [X] -> [Y]\n"
        "- RP Balance: [change]\n"
        "- New Skills/Upgrades: [list]\n"
        "- Characters Introduced: [list]\n\n"
        "## ACTIVE THREADS\n"
        "- [thread 1]\n"
        "- [thread 2]"
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the summarization prompt."""
        content = kwargs.get("content", "")
        chapter_num = kwargs.get("chapter_num", "")
        scope = kwargs.get("scope", "chapter")

        if scope == "chapter":
            instruction = (
                f"Summarize Chapter {chapter_num}.\n\n"
                f"## CHAPTER CONTENT\n{content}"
            )
        elif scope == "multi_chapter":
            instruction = (
                f"Summarize the following chapters.\n\n"
                f"## CHAPTERS\n{content}"
            )
        else:
            instruction = (
                f"Summarize the following content.\n\n"
                f"## CONTENT\n{content}"
            )

        return self.format_instruction(context, instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse summarizer output."""
        output = raw_output.strip()

        sections: dict = {
            "plot_summary": "",
            "state_changes": "",
            "active_threads": "",
        }

        current_section = ""
        for line in output.split("\n"):
            if "PLOT SUMMARY" in line.upper():
                current_section = "plot_summary"
            elif "STATE CHANGES" in line.upper():
                current_section = "state_changes"
            elif "ACTIVE THREADS" in line.upper():
                current_section = "active_threads"
            elif current_section:
                sections[current_section] += line + "\n"

        return {
            "status": "complete",
            "output": output,
            "summary": output,
            "sections": sections,
        }
