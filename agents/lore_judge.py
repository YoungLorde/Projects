"""
Agent 1: Lore Judge — Validates prose against established lorebook data.

Checks for character consistency, location accuracy, timeline coherence,
world-building rule violations, relationship dynamics, and factual
contradictions with established lore.
"""

from agents.base_agent import BaseAgent


class LoreJudge(BaseAgent):
    """Lore consistency checker for fiction writing."""

    name = "Lore Judge"
    role = "Lore Consistency Checker"
    temperature = 0.20
    max_tokens = 2048

    system_prompt = (
        "You are a lore consistency checker for fiction writing. Compare the "
        "provided prose against the established lorebook data.\n\n"
        "Check for:\n"
        "- Character names, traits, and behavior consistency\n"
        "- Location and setting accuracy\n"
        "- Timeline and chronological consistency\n"
        "- Magic system, technology, or world-building rule violations\n"
        "- Relationship dynamics matching established patterns\n"
        "- Factual contradictions with established lore\n"
        "- RP Conversion exclusivity (Mohamed Vance ONLY)\n"
        "- Pocket Dimension exclusivity (Mohamed Vance ONLY)\n"
        "- System notification format compliance\n"
        "- Vehicle tier/sub-level accuracy\n"
        "- Player level and rank accuracy\n"
        "- Alien species descriptions matching established profiles\n\n"
        "Response format:\n"
        "- If everything is consistent, respond with exactly: CONSISTENT\n"
        "- If there are issues, list each one briefly:\n"
        "  ISSUE: [Brief description of the inconsistency]\n"
        "  SUGGESTION: [How to fix it]\n\n"
        "Be thorough but concise. Focus on actual contradictions, not "
        "stylistic preferences."
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the lore checking prompt."""
        prose = kwargs.get("prose", "")
        chapter_num = kwargs.get("chapter_num", "unknown")

        instruction = (
            f"Review the following prose from Chapter {chapter_num} against "
            f"the established lore provided in the context.\n\n"
            f"## PROSE TO CHECK\n{prose}"
        )
        return self.format_instruction(context, instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse lore judge output into structured result."""
        output = raw_output.strip()

        if output == "CONSISTENT":
            return {
                "status": "consistent",
                "output": output,
                "issues": [],
                "needs_revision": False,
            }

        issues = []
        current_issue: dict = {}
        for line in output.split("\n"):
            line = line.strip()
            if line.startswith("ISSUE:"):
                if current_issue:
                    issues.append(current_issue)
                current_issue = {
                    "issue": line[6:].strip(),
                    "suggestion": "",
                }
            elif line.startswith("SUGGESTION:") and current_issue:
                current_issue["suggestion"] = line[11:].strip()

        if current_issue:
            issues.append(current_issue)

        return {
            "status": "issues_found",
            "output": output,
            "issues": issues,
            "needs_revision": len(issues) > 0,
        }
