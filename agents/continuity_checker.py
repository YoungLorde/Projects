"""
Agent 7: Continuity Checker — Validates timeline and character continuity.

Focused on narrative logic: timeline consistency, character behavior patterns,
forgotten plot threads, physical impossibilities, and emotional continuity.
"""

from agents.base_agent import BaseAgent


class ContinuityChecker(BaseAgent):
    """Timeline and continuity validator for fiction writing."""

    name = "Continuity Checker"
    role = "Timeline & Continuity Validator"
    temperature = 0.20
    max_tokens = 600

    system_prompt = (
        "You are a continuity expert for fiction writing. Check for plot "
        "holes, timeline issues, and character consistency.\n\n"
        "Review for:\n"
        "- Timeline inconsistencies (events out of order)\n"
        "- Character behavior that contradicts established patterns\n"
        "- Forgotten plot threads or unresolved setups\n"
        "- Physical impossibilities (character in two places at once)\n"
        "- Emotional continuity (reactions matching previous scenes)\n"
        "- Mohamed's level and rank matching expected progression\n"
        "- Vehicle tier and sub-level accuracy\n"
        "- RP balance consistency (no unexplained gains or losses)\n"
        "- ZERO AI tier matching expected development\n"
        "- Assimilation stage accuracy\n\n"
        "Response format:\n"
        "- If consistent, respond with exactly: CONSISTENT\n"
        "- If there are issues:\n"
        "  CONTINUITY ISSUE: [Description]\n"
        "  CONTEXT: [What was established earlier]\n"
        "  SUGGESTION: [How to resolve]\n\n"
        "Focus on narrative logic, not style preferences."
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the continuity checking prompt."""
        prose = kwargs.get("prose", "")
        chapter_num = kwargs.get("chapter_num", "unknown")

        instruction = (
            f"Review Chapter {chapter_num} for continuity issues.\n\n"
            f"## CHAPTER PROSE\n{prose}"
        )
        return self.format_instruction(context, instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse continuity checker output."""
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
            if line.startswith("CONTINUITY ISSUE:"):
                if current_issue:
                    issues.append(current_issue)
                current_issue = {
                    "issue": line[17:].strip(),
                    "context": "",
                    "suggestion": "",
                }
            elif line.startswith("CONTEXT:") and current_issue:
                current_issue["context"] = line[8:].strip()
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
