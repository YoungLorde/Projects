"""
Agent 6: Plot Checker — Detects plot holes and consistency issues.

Checks for plot holes, timeline inconsistencies, and character behavior
changes against the established story context.
"""

from agents.base_agent import BaseAgent


class PlotChecker(BaseAgent):
    """Plot hole and consistency detector."""

    name = "Plot Checker"
    role = "Plot Hole Detector"
    temperature = 0.30
    max_tokens = 8192

    system_prompt = (
        "You are a continuity expert. Check for plot holes, timeline "
        "inconsistencies, and character behavior changes. Flag anything "
        "that doesn't match the established story context.\n\n"
        "Specifically check:\n"
        "- Plot holes or logical impossibilities\n"
        "- Character actions that contradict established personality\n"
        "- Timeline errors (events out of order, impossible timing)\n"
        "- Forgotten or contradicted plot threads\n"
        "- Unearned character development (growing too fast)\n"
        "- Missing consequences from previous events\n"
        "- Geographic/spatial impossibilities\n"
        "- Resource/RP balance errors\n"
        "- Vehicle tier/upgrade contradictions\n"
        "- Level/rank mismatches\n\n"
        "If consistent, respond with: CONSISTENT\n"
        "Otherwise, list issues briefly with:\n"
        "  PLOT ISSUE: [Description]\n"
        "  IMPACT: [How this affects the story]\n"
        "  SUGGESTION: [How to fix it]"
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the plot checking prompt."""
        prose = kwargs.get("prose", "")
        chapter_num = kwargs.get("chapter_num", "unknown")

        instruction = (
            f"Review Chapter {chapter_num} for plot holes and consistency "
            f"issues.\n\n"
            f"## CHAPTER PROSE\n{prose}"
        )
        return self.format_instruction(context, instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse plot checker output."""
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
            if line.startswith("PLOT ISSUE:"):
                if current_issue:
                    issues.append(current_issue)
                current_issue = {
                    "issue": line[11:].strip(),
                    "impact": "",
                    "suggestion": "",
                }
            elif line.startswith("IMPACT:") and current_issue:
                current_issue["impact"] = line[7:].strip()
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
