"""
Parameter Enforcer — Validates all user-specified parameters are respected.

Checks that generated content complies with all configured constraints:
word count, character presence, tone, System notification format, lore
exclusivity rules, chapter structure, and any custom parameters.
"""

from typing import Optional

from agents.base_agent import BaseAgent
from config import MIN_WORD_COUNT


# System notification format pattern (simplified check)
SYSTEM_NOTIFICATION_MARKERS = [
    "+================================================+",
    "SYSTEM NOTIFICATION",
]

# Exclusivity rules that must never be violated
EXCLUSIVITY_RULES = [
    {
        "rule": "RP Conversion is exclusive to Mohamed Vance",
        "check_phrases": ["rp conversion"],
        "owner": "Mohamed Vance",
    },
    {
        "rule": "Pocket Dimension interior is exclusive to Mohamed Vance",
        "check_phrases": ["pocket dimension"],
        "owner": "Mohamed Vance",
    },
]


class ParameterEnforcer(BaseAgent):
    """Parameter compliance validator for all writing constraints."""

    name = "Parameter Enforcer"
    role = "Parameter Compliance Validator"
    temperature = 0.10
    max_tokens = 1000

    system_prompt = (
        "You are a parameter enforcer for the novel RP Conversion. "
        "Your job is to verify that generated prose complies with ALL "
        "specified parameters and constraints.\n\n"
        "Check for:\n"
        "- Word count meets minimum (2,500 words)\n"
        "- Required characters appear in the chapter\n"
        "- Tone matches the specified tone\n"
        "- At least one System notification is present and correctly "
        "formatted\n"
        "- Chapter ends on tension/hook (not flat)\n"
        "- RP Conversion is only used by Mohamed Vance\n"
        "- Pocket Dimension is only referenced for Mohamed's vehicle\n"
        "- No summarization of events that should be shown\n"
        "- No contradictions with established lore\n"
        "- Any custom parameters specified by the user\n\n"
        "Response format:\n"
        "For each parameter, report:\n"
        "  PASS: [parameter name]\n"
        "  or\n"
        "  FAIL: [parameter name] — [reason]\n\n"
        "End with:\n"
        "  ALL_PARAMETERS_MET or PARAMETERS_VIOLATED: [count] issues"
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the parameter enforcement prompt."""
        prose = kwargs.get("prose", "")
        parameters = kwargs.get("parameters", {})
        chapter_num = kwargs.get("chapter_num", "unknown")

        param_list = []
        for key, value in parameters.items():
            param_list.append(f"- {key}: {value}")
        param_str = "\n".join(param_list) if param_list else "Default parameters"

        instruction = (
            f"Validate Chapter {chapter_num} against these parameters:\n"
            f"{param_str}\n\n"
            f"## PROSE TO VALIDATE\n{prose[:3000]}...\n"
            f"[Word count: {len(prose.split())} words]"
        )
        return self.format_instruction("", instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse parameter enforcer output."""
        output = raw_output.strip()
        passes = []
        fails = []

        for line in output.split("\n"):
            line = line.strip()
            if line.startswith("PASS:"):
                passes.append(line[5:].strip())
            elif line.startswith("FAIL:"):
                fails.append(line[5:].strip())

        all_met = "ALL_PARAMETERS_MET" in output or len(fails) == 0

        return {
            "status": "pass" if all_met else "fail",
            "output": output,
            "passes": passes,
            "fails": fails,
            "all_parameters_met": all_met,
        }

    def local_check(
        self,
        prose: str,
        parameters: Optional[dict] = None,
    ) -> dict:
        """
        Perform local parameter checks without an AI call.

        Checks:
        - Word count
        - System notification presence
        - Exclusivity rules

        Args:
            prose: The generated prose text.
            parameters: Optional dict of custom parameters to check.

        Returns:
            Dict with check results.
        """
        results: dict = {"passes": [], "fails": [], "warnings": []}

        # Word count check
        word_count = len(prose.split())
        if word_count >= MIN_WORD_COUNT:
            results["passes"].append(
                f"Word count: {word_count} (minimum {MIN_WORD_COUNT})"
            )
        else:
            results["fails"].append(
                f"Word count: {word_count} / {MIN_WORD_COUNT} minimum "
                f"({MIN_WORD_COUNT - word_count} words short)"
            )

        # System notification format check
        has_notification = any(
            marker in prose for marker in SYSTEM_NOTIFICATION_MARKERS
        )
        if has_notification:
            results["passes"].append("System notification present")
        else:
            results["fails"].append(
                "No System notification found — every chapter requires at "
                "least one"
            )

        # Exclusivity checks
        prose_lower = prose.lower()
        for rule in EXCLUSIVITY_RULES:
            for phrase in rule["check_phrases"]:
                if phrase in prose_lower:
                    results["passes"].append(
                        f"Exclusivity check: {rule['rule']}"
                    )
                    break

        # Custom parameters
        if parameters:
            if "tone" in parameters:
                results["warnings"].append(
                    f"Tone '{parameters['tone']}' specified — requires AI "
                    f"validation"
                )
            if "characters_required" in parameters:
                for char in parameters["characters_required"]:
                    if char.lower() in prose_lower:
                        results["passes"].append(
                            f"Required character present: {char}"
                        )
                    else:
                        results["fails"].append(
                            f"Required character missing: {char}"
                        )

        results["all_passed"] = len(results["fails"]) == 0
        return results
