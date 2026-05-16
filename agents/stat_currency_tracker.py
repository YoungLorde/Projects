"""
Stat & Currency Tracker — Parses chapter prose for stat, currency,
and progression changes, validates the math, and returns structured
updates to be applied to the story state.

Works at two levels:
  1. Local extraction: regex-based parsing of System notification blocks
     for explicit stat gains, RP earned/spent, level-ups, tier changes,
     and assimilation stage advances. No AI call needed.
  2. AI-level analysis: sends prose to an AI for deeper extraction of
     implicit changes (e.g., "Mohamed felt stronger" might imply a
     pending stat change). Used in full-quality pipelines.
"""

import re
from typing import Optional

from agents.base_agent import BaseAgent
from config import DEFAULT_STORY_STATE


# Patterns for extracting changes from System notification blocks
_STAT_GAIN = re.compile(
    r"\+\s*(\d+)\s+(STR|AGI|END|INT|PER|LCK|SYS|VIT|WIS)",
    re.IGNORECASE,
)
_RP_EARNED = re.compile(
    r"(?:(?:earned|gained|received|acquired)\s+(\d[\d,]*)\s*RP"
    r"|RP\s*(?:earned|gained|received)\s*[:\-]?\s*(\d[\d,]*)\s*RP?)",
    re.IGNORECASE,
)
_RP_SPENT = re.compile(
    r"(?:spent|used|consumed|invested|paid)\s+(\d[\d,]*)\s*RP",
    re.IGNORECASE,
)
_LEVEL_UP = re.compile(
    r"level(?:ed)?\s*(?:up)?\s*(?:to)?\s*(\d+)",
    re.IGNORECASE,
)
_RANK_UP = re.compile(
    r"rank(?:ed)?\s*(?:up)?\s*(?:to)?\s*[:\-]?\s*(.+)",
    re.IGNORECASE,
)
_VEHICLE_TIER = re.compile(
    r"vehicle\s*tier\s*(?:up|upgraded|advanced)?\s*(?:to)?\s*(\d+)",
    re.IGNORECASE,
)
_ASSIMILATION = re.compile(
    r"assimilation\s*(?:stage|phase)?\s*(?:advanced|progressed|upgraded)?"
    r"\s*(?:to)?\s*[:\-]?\s*(.+)",
    re.IGNORECASE,
)

# Valid stat names (canonical uppercase)
VALID_STATS = {"STR", "AGI", "END", "INT", "PER", "LCK", "SYS", "VIT", "WIS"}

# Valid assimilation stages in order
ASSIMILATION_STAGES = [
    "Interface Sync",
    "Data Bleed",
    "Core Integration",
    "Symbiote Phase",
    "Full Fusion",
    "Transcendence",
]


class StatCurrencyTracker(BaseAgent):
    """Parses prose for stat/currency/progression changes and validates them."""

    name = "Stat & Currency Tracker"
    role = "Stat, Currency & Progression Tracker"
    temperature = 0.15
    max_tokens = 2000

    system_prompt = (
        "You are a stat and currency tracker for the novel RP Conversion. "
        "Your job is to analyze chapter prose and extract ALL changes to:\n\n"
        "1. **Stats**: STR, AGI, END, INT, PER, LCK, SYS, VIT, WIS\n"
        "   - Look for explicit gains (+N STAT) in System notifications\n"
        "   - Look for implicit stat changes described in narrative\n"
        "2. **Currency (RP)**: RP earned, RP spent, net balance change\n"
        "   - Track RP earned from kills, quests, discoveries, etc.\n"
        "   - Track RP spent on upgrades, abilities, vehicle tiers\n"
        "3. **Level & Rank**: Level-ups and rank promotions\n"
        "4. **Vehicle Progression**: Tier advances, upgrades installed\n"
        "5. **Zero AI**: Tier changes, personality stage changes\n"
        "6. **Assimilation Stage**: Mohamed's System Assimilation progress\n\n"
        "Response format:\n"
        "```\n"
        "STAT_CHANGES:\n"
        "  - STAT: +N (reason)\n"
        "CURRENCY:\n"
        "  RP_EARNED: N (source)\n"
        "  RP_SPENT: N (purpose)\n"
        "  NET_CHANGE: +/-N\n"
        "LEVEL: N (if changed, else UNCHANGED)\n"
        "RANK: value (if changed, else UNCHANGED)\n"
        "VEHICLE_TIER: N (if changed, else UNCHANGED)\n"
        "ASSIMILATION: stage (if changed, else UNCHANGED)\n"
        "VALIDATION: OK or ISSUES_FOUND\n"
        "ISSUES: (list any math errors or inconsistencies)\n"
        "```\n\n"
        "Be precise. Only report changes that actually occur in the prose. "
        "If no changes occurred in a category, mark it UNCHANGED."
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the stat tracking prompt."""
        prose = kwargs.get("prose", "")
        chapter_num = kwargs.get("chapter_num", "unknown")
        current_state = kwargs.get("current_state", {})

        state_summary = ""
        if current_state:
            mohamed = current_state.get("mohamed", {})
            stats = mohamed.get("stats", {})
            state_summary = (
                f"Current State (before this chapter):\n"
                f"  Level: {mohamed.get('level', '?')}\n"
                f"  Rank: {mohamed.get('rank', '?')}\n"
                f"  RP Balance: {mohamed.get('rp_balance', '?')}\n"
                f"  RP Multiplier: {mohamed.get('rp_multiplier', '?')}\n"
                f"  Assimilation: {mohamed.get('assimilation_stage', '?')}\n"
                f"  Stats: {stats}\n"
                f"  Vehicle Tier: "
                f"{current_state.get('vehicle', {}).get('tier', '?')}\n"
                f"  Zero AI Tier: "
                f"{current_state.get('zero_ai', {}).get('tier', '?')}\n"
            )

        instruction = (
            f"Analyze Chapter {chapter_num} and extract all stat, currency, "
            f"and progression changes.\n\n"
            f"{state_summary}\n"
            f"## CHAPTER PROSE\n{prose[:6000]}"
        )
        return self.format_instruction(context, instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse the AI tracker output into structured changes."""
        output = raw_output.strip()
        result: dict = {
            "status": "pass",
            "output": output,
            "stat_changes": {},
            "rp_earned": 0,
            "rp_spent": 0,
            "rp_net": 0,
            "level": None,
            "rank": None,
            "vehicle_tier": None,
            "assimilation": None,
            "issues": [],
        }

        for line in output.split("\n"):
            line = line.strip()
            # Parse stat changes
            stat_match = re.match(
                r"-\s*(STR|AGI|END|INT|PER|LCK|SYS|VIT|WIS)\s*:\s*\+?(-?\d+)",
                line, re.IGNORECASE,
            )
            if stat_match:
                stat_name = stat_match.group(1).upper()
                change = int(stat_match.group(2))
                result["stat_changes"][stat_name] = change

            # Parse RP
            if "RP_EARNED:" in line:
                m = re.search(r"RP_EARNED:\s*(\d+)", line)
                if m:
                    result["rp_earned"] = int(m.group(1))
            if "RP_SPENT:" in line:
                m = re.search(r"RP_SPENT:\s*(\d+)", line)
                if m:
                    result["rp_spent"] = int(m.group(1))

            # Parse level
            if line.startswith("LEVEL:") and "UNCHANGED" not in line:
                m = re.search(r"LEVEL:\s*(\d+)", line)
                if m:
                    result["level"] = int(m.group(1))

            # Parse rank
            if line.startswith("RANK:") and "UNCHANGED" not in line:
                result["rank"] = line.split(":", 1)[1].strip()

            # Parse vehicle tier
            if line.startswith("VEHICLE_TIER:") and "UNCHANGED" not in line:
                m = re.search(r"VEHICLE_TIER:\s*(\d+)", line)
                if m:
                    result["vehicle_tier"] = int(m.group(1))

            # Parse assimilation
            if line.startswith("ASSIMILATION:") and "UNCHANGED" not in line:
                result["assimilation"] = line.split(":", 1)[1].strip()

            # Parse issues
            if line.startswith("ISSUES:") or line.startswith("- ISSUE:"):
                issue = line.split(":", 1)[1].strip() if ":" in line else ""
                if issue and issue.lower() != "none":
                    result["issues"].append(issue)

        if "ISSUES_FOUND" in output or result["issues"]:
            result["status"] = "issues_found"

        result["rp_net"] = result["rp_earned"] - result["rp_spent"]
        return result

    def extract_changes(self, prose: str) -> dict:
        """
        Local extraction of stat/currency changes from prose.

        Parses System notification blocks and narrative text for explicit
        stat gains, RP changes, level-ups, tier changes, etc.

        Args:
            prose: The chapter prose to analyze.

        Returns:
            Dict with extracted changes.
        """
        changes: dict = {
            "stat_changes": {},
            "rp_earned": 0,
            "rp_spent": 0,
            "rp_net": 0,
            "level_up": None,
            "rank_up": None,
            "vehicle_tier": None,
            "assimilation": None,
            "raw_extractions": [],
        }

        # Extract stat gains
        for match in _STAT_GAIN.finditer(prose):
            amount = int(match.group(1))
            stat = match.group(2).upper()
            if stat in VALID_STATS:
                changes["stat_changes"][stat] = (
                    changes["stat_changes"].get(stat, 0) + amount
                )
                changes["raw_extractions"].append(
                    f"+{amount} {stat}"
                )

        # Extract RP earned
        for match in _RP_EARNED.finditer(prose):
            raw = match.group(1) or match.group(2)
            amount = int(raw.replace(",", ""))
            changes["rp_earned"] += amount
            changes["raw_extractions"].append(
                f"Earned {amount} RP"
            )

        # Extract RP spent
        for match in _RP_SPENT.finditer(prose):
            amount = int(match.group(1).replace(",", ""))
            changes["rp_spent"] += amount
            changes["raw_extractions"].append(
                f"Spent {amount} RP"
            )

        # Extract level-ups
        for match in _LEVEL_UP.finditer(prose):
            new_level = int(match.group(1))
            changes["level_up"] = new_level
            changes["raw_extractions"].append(
                f"Level up to {new_level}"
            )

        # Extract rank-ups
        for match in _RANK_UP.finditer(prose):
            new_rank = match.group(1).strip().rstrip(".")
            if new_rank and len(new_rank) < 50:
                changes["rank_up"] = new_rank
                changes["raw_extractions"].append(
                    f"Rank up to {new_rank}"
                )

        # Extract vehicle tier changes
        for match in _VEHICLE_TIER.finditer(prose):
            new_tier = int(match.group(1))
            changes["vehicle_tier"] = new_tier
            changes["raw_extractions"].append(
                f"Vehicle tier to {new_tier}"
            )

        # Extract assimilation stage changes
        for match in _ASSIMILATION.finditer(prose):
            stage = match.group(1).strip().rstrip(".")
            if stage and len(stage) < 60:
                changes["assimilation"] = stage
                changes["raw_extractions"].append(
                    f"Assimilation stage: {stage}"
                )

        changes["rp_net"] = changes["rp_earned"] - changes["rp_spent"]
        return changes

    def validate_math(
        self,
        changes: dict,
        current_state: Optional[dict] = None,
    ) -> dict:
        """
        Validate that extracted changes are mathematically consistent
        with the current story state.

        Args:
            changes: Dict from extract_changes().
            current_state: Current story state dict (from MemoryManager).

        Returns:
            Dict with validation results.
        """
        if current_state is None:
            current_state = dict(DEFAULT_STORY_STATE)

        mohamed = current_state.get("mohamed", {})
        current_stats = mohamed.get("stats", {})
        current_level = mohamed.get("level", 1)
        current_rp = mohamed.get("rp_balance", 0)
        current_vehicle_tier = current_state.get("vehicle", {}).get("tier", 0)
        current_assimilation = mohamed.get(
            "assimilation_stage", "Interface Sync"
        )

        issues: list = []
        warnings: list = []

        # Validate stat changes (no stat should go below 0)
        for stat, change in changes.get("stat_changes", {}).items():
            current_val = current_stats.get(stat, 0)
            new_val = current_val + change
            if new_val < 0:
                issues.append(
                    f"{stat} would go to {new_val} "
                    f"(current {current_val} + {change})"
                )
            if change > 50:
                warnings.append(
                    f"{stat} +{change} is unusually large — verify"
                )

        # Validate RP balance
        rp_net = changes.get("rp_net", 0)
        new_rp = current_rp + rp_net
        if new_rp < 0:
            issues.append(
                f"RP balance would go to {new_rp} "
                f"(current {current_rp} + net {rp_net})"
            )
        if changes.get("rp_earned", 0) > 100000:
            warnings.append(
                f"RP earned ({changes['rp_earned']}) is unusually large"
            )

        # Validate level-up (should only go up, not down)
        new_level = changes.get("level_up")
        if new_level is not None:
            if new_level <= current_level:
                issues.append(
                    f"Level would decrease from {current_level} "
                    f"to {new_level}"
                )
            if new_level > current_level + 10:
                warnings.append(
                    f"Level jump of {new_level - current_level} "
                    f"levels in one chapter is large"
                )

        # Validate vehicle tier (should only go up)
        new_tier = changes.get("vehicle_tier")
        if new_tier is not None:
            if new_tier < current_vehicle_tier:
                issues.append(
                    f"Vehicle tier would decrease from "
                    f"{current_vehicle_tier} to {new_tier}"
                )

        # Validate assimilation stage order
        new_assimilation = changes.get("assimilation")
        if new_assimilation and new_assimilation in ASSIMILATION_STAGES:
            current_idx = (
                ASSIMILATION_STAGES.index(current_assimilation)
                if current_assimilation in ASSIMILATION_STAGES
                else -1
            )
            new_idx = ASSIMILATION_STAGES.index(new_assimilation)
            if new_idx < current_idx:
                issues.append(
                    f"Assimilation would regress from "
                    f"'{current_assimilation}' to '{new_assimilation}'"
                )
            if new_idx > current_idx + 1:
                warnings.append(
                    f"Assimilation skipping stages from "
                    f"'{current_assimilation}' to '{new_assimilation}'"
                )

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "warnings": warnings,
        }

    def build_state_update(
        self,
        changes: dict,
        current_state: Optional[dict] = None,
    ) -> dict:
        """
        Build a state update dict from extracted changes.

        This dict can be passed directly to MemoryManager.update_state()
        or Orchestrator.update_story_state().

        Args:
            changes: Dict from extract_changes().
            current_state: Current state (for computing new values).

        Returns:
            Dict suitable for update_state().
        """
        if current_state is None:
            current_state = dict(DEFAULT_STORY_STATE)

        mohamed = current_state.get("mohamed", {})
        current_stats = mohamed.get("stats", {})
        current_rp = mohamed.get("rp_balance", 0)

        update: dict = {}
        mohamed_update: dict = {}

        # Apply stat changes
        if changes.get("stat_changes"):
            new_stats = dict(current_stats)
            for stat, change in changes["stat_changes"].items():
                new_stats[stat] = new_stats.get(stat, 0) + change
            mohamed_update["stats"] = new_stats

        # Apply RP changes
        rp_net = changes.get("rp_net", 0)
        if rp_net != 0:
            mohamed_update["rp_balance"] = current_rp + rp_net

        # Apply level-up
        if changes.get("level_up") is not None:
            mohamed_update["level"] = changes["level_up"]

        # Apply rank-up
        if changes.get("rank_up") is not None:
            mohamed_update["rank"] = changes["rank_up"]

        # Apply assimilation change
        if changes.get("assimilation") is not None:
            mohamed_update["assimilation_stage"] = changes["assimilation"]

        if mohamed_update:
            update["mohamed"] = mohamed_update

        # Apply vehicle tier change
        if changes.get("vehicle_tier") is not None:
            update["vehicle"] = {"tier": changes["vehicle_tier"]}

        return update
