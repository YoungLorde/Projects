"""
Agent 2: Prose Writer — Generates story prose based on context and instructions.

The primary creative agent. Writes engaging fiction that maintains consistent
tone, style, and narrative voice while honoring established world-building.
"""

from agents.base_agent import BaseAgent


class ProseWriter(BaseAgent):
    """Skilled fiction writer for story generation."""

    name = "Prose Writer"
    role = "Fiction Prose Writer"
    temperature = 0.85
    max_tokens = 8192

    system_prompt = (
        "You are a skilled fiction writer. Your task is to continue the story "
        "based on the provided context and scene beat instructions.\n\n"
        "Guidelines:\n"
        "- Maintain consistent tone, style, and narrative voice\n"
        "- Show, don't tell — use sensory details and action\n"
        "- Keep characters' voices distinct and authentic\n"
        "- Balance dialogue, action, and internal reflection\n"
        "- Create smooth transitions and natural pacing\n"
        "- Honor the established world-building and lore\n"
        "- Every chapter must be a minimum of 2,500 words\n"
        "- Use the exact System notification format from the bible\n"
        "- End every chapter on tension, a cliffhanger, a revelation, "
        "a level-up, or a resource acquisition moment\n"
        "- Never summarize events that should be shown\n"
        "- Never contradict established lore, rules, or character abilities\n"
        "- Mohamed's personality must match his current arc stage\n"
        "- RP Conversion is EXCLUSIVE to Mohamed Vance\n"
        "- Pocket Dimension interior is EXCLUSIVE to Mohamed Vance\n\n"
        "Write engaging prose that draws readers in and advances the story "
        "naturally. Write the FULL chapter — do not truncate, summarize, "
        "or stop early."
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the prose writing prompt."""
        chapter_num = kwargs.get("chapter_num", 1)
        scene_beats = kwargs.get("scene_beats", "")
        arc_name = kwargs.get("arc_name", "")
        tone = kwargs.get("tone", "")
        characters_present = kwargs.get("characters_present", "")
        additional_notes = kwargs.get("additional_notes", "")
        revision_notes = kwargs.get("revision_notes", "")
        previous_summary = kwargs.get("previous_summary", "")

        parts = [f"Write Chapter {chapter_num} of RP Conversion.\n"]

        if arc_name:
            parts.append(f"**Arc:** {arc_name}")
        if tone:
            parts.append(f"**Tone:** {tone}")
        if characters_present:
            parts.append(f"**Characters Present:** {characters_present}")
        if previous_summary:
            parts.append(
                f"**Previous Chapter Summary:** {previous_summary}"
            )
        if scene_beats:
            parts.append(f"**Scene Beats:**\n{scene_beats}")
        if additional_notes:
            parts.append(f"**Additional Notes:** {additional_notes}")
        if revision_notes:
            parts.append(
                f"**REVISION REQUIRED — Fix these issues:**\n{revision_notes}"
            )

        parts.append(
            "\nWRITE THE FULL CHAPTER NOW. Minimum 2,500 words. Use all "
            "System notification formats from the Bible. Never summarize — "
            "show everything in real time. End on tension, revelation, or a "
            "hook that pulls into the next chapter."
        )

        instruction = "\n".join(parts)
        return self.format_instruction(context, instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse prose writer output."""
        output = raw_output.strip()
        word_count = len(output.split())

        return {
            "status": "complete",
            "output": output,
            "word_count": word_count,
            "meets_minimum": word_count >= 2500,
        }
