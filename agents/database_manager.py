"""
Database Manager Agent — Queries and serves structured YAML databases.

This agent loads all YAML databases (races, monsters, factions, powers,
vehicles, items, worlds, technology, EVA suits) and provides query
methods that other agents and the orchestrator can use to pull relevant
data during chapter writing. No internet access required — everything
is self-contained in the local database files.
"""

from pathlib import Path
from typing import Optional

import yaml

from agents.base_agent import BaseAgent
from config import PROJECT_ROOT


# Database directory
DATABASES_DIR = PROJECT_ROOT / "databases"


class DatabaseManager(BaseAgent):
    """
    Manages structured YAML databases for the novel writing system.

    Provides:
      - Loading all databases from disk
      - Querying by category, tier, name, race, type
      - Building context strings for other agents
      - Searching across all databases
    """

    name = "Database Manager"
    role = "Database Query & Context Provider"
    temperature = 0.10
    max_tokens = 4000
    system_prompt = (
        "You are a database query assistant for the RP Conversion novel. "
        "Your job is to find and return relevant database entries based on "
        "queries about races, monsters, factions, powers, vehicles, items, "
        "worlds, technology, and EVA suits. Return structured, detailed "
        "information that prose writers and lore judges can use. "
        "Always include tier, stats, descriptions, and lore notes when available."
    )

    def __init__(self) -> None:
        super().__init__()
        self._databases: dict = {}
        self._loaded = False

    def load_databases(self) -> dict:
        """Load all YAML databases from disk into memory."""
        self._databases = {}
        if not DATABASES_DIR.exists():
            return self._databases

        for category_dir in sorted(DATABASES_DIR.iterdir()):
            if not category_dir.is_dir():
                continue
            category = category_dir.name
            self._databases[category] = {}
            for yaml_file in sorted(category_dir.glob("*.yaml")):
                try:
                    with open(yaml_file, "r", encoding="utf-8") as f:
                        data = yaml.safe_load(f)
                    if data:
                        self._databases[category][yaml_file.stem] = data
                except (yaml.YAMLError, OSError):
                    pass

        self._loaded = True
        return self._databases

    def ensure_loaded(self) -> None:
        """Load databases if not already loaded."""
        if not self._loaded:
            self.load_databases()

    def get_categories(self) -> list:
        """Return list of available database categories."""
        self.ensure_loaded()
        return list(self._databases.keys())

    def get_files_in_category(self, category: str) -> list:
        """Return list of database files in a category."""
        self.ensure_loaded()
        cat = self._databases.get(category, {})
        return list(cat.keys())

    def get_database(self, category: str, filename: str) -> dict:
        """Get a specific database file's contents."""
        self.ensure_loaded()
        return self._databases.get(category, {}).get(filename, {})

    def get_full_category(self, category: str) -> dict:
        """Get all databases in a category."""
        self.ensure_loaded()
        return self._databases.get(category, {})

    def query_by_tier(self, tier: int, category: str = "") -> list:
        """
        Find all entries matching a specific tier across databases.

        Args:
            tier: The tier to search for.
            category: Optional category filter.

        Returns:
            List of matching entries with source info.
        """
        self.ensure_loaded()
        results: list = []
        categories = (
            {category: self._databases[category]}
            if category and category in self._databases
            else self._databases
        )

        for cat_name, cat_data in categories.items():
            for file_name, file_data in cat_data.items():
                self._search_dict_for_tier(
                    file_data, tier, cat_name, file_name, results
                )
        return results

    def query_by_name(self, name: str, category: str = "") -> list:
        """
        Search for entries by name (case-insensitive partial match).

        Args:
            name: Search term to match against entry names.
            category: Optional category filter.

        Returns:
            List of matching entries with source info.
        """
        self.ensure_loaded()
        results: list = []
        name_lower = name.lower()
        categories = (
            {category: self._databases[category]}
            if category and category in self._databases
            else self._databases
        )

        for cat_name, cat_data in categories.items():
            for file_name, file_data in cat_data.items():
                self._search_dict_for_name(
                    file_data, name_lower, cat_name, file_name, results
                )
        return results

    def query_by_race(self, race: str) -> list:
        """Find all entries associated with a specific race/species."""
        self.ensure_loaded()
        results: list = []
        race_lower = race.lower()

        for cat_name, cat_data in self._databases.items():
            for file_name, file_data in cat_data.items():
                self._search_dict_for_field(
                    file_data, "race", race_lower, cat_name, file_name, results
                )
        return results

    def query_by_type(self, entry_type: str, category: str = "") -> list:
        """Find all entries of a specific type."""
        self.ensure_loaded()
        results: list = []
        type_lower = entry_type.lower()
        categories = (
            {category: self._databases[category]}
            if category and category in self._databases
            else self._databases
        )

        for cat_name, cat_data in categories.items():
            for file_name, file_data in cat_data.items():
                self._search_dict_for_field(
                    file_data, "type", type_lower, cat_name, file_name, results
                )
        return results

    def get_stats_summary(self) -> dict:
        """Get a summary of all loaded databases."""
        self.ensure_loaded()
        summary: dict = {}
        for cat_name, cat_data in self._databases.items():
            summary[cat_name] = {
                "files": list(cat_data.keys()),
                "file_count": len(cat_data),
            }
        total_files = sum(s["file_count"] for s in summary.values())
        summary["_total"] = {
            "categories": len(self._databases),
            "total_files": total_files,
        }
        return summary

    def build_context_for_chapter(
        self,
        chapter_num: int,
        location: str = "",
        creatures_needed: bool = False,
        vehicles_needed: bool = False,
        factions_needed: bool = False,
        tier_range: Optional[tuple] = None,
    ) -> str:
        """
        Build a database context string for chapter writing.

        Selects relevant database entries based on chapter parameters
        and returns them as a formatted context string that can be
        injected into agent prompts.
        """
        self.ensure_loaded()
        sections: list = []

        sections.append("## DATABASE CONTEXT")

        if creatures_needed and tier_range:
            sections.append("### CREATURES IN TIER RANGE")
            for tier in range(tier_range[0], tier_range[1] + 1):
                entries = self.query_by_tier(tier, "monsters")
                for entry in entries[:5]:
                    sections.append(
                        f"- {entry.get('name', 'Unknown')} "
                        f"(Tier {tier}): {entry.get('description', '')[:200]}"
                    )

        if vehicles_needed:
            sections.append("### VEHICLE REFERENCE")
            vehicle_data = self.get_full_category("vehicles")
            for fname, fdata in vehicle_data.items():
                desc = fdata.get("description", fdata.get("category", ""))
                if isinstance(desc, str):
                    sections.append(f"- {fname}: {desc[:200]}")

        if factions_needed:
            sections.append("### FACTION REFERENCE")
            faction_data = self.get_full_category("factions")
            for fname, fdata in faction_data.items():
                desc = fdata.get("description", fdata.get("category", ""))
                if isinstance(desc, str):
                    sections.append(f"- {fname}: {desc[:200]}")

        if location:
            sections.append(f"### LOCATION: {location}")
            loc_results = self.query_by_name(location, "worlds")
            for entry in loc_results[:3]:
                sections.append(yaml.dump(entry, default_flow_style=False)[:500])

        return "\n\n".join(sections)

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build a query prompt for the database manager."""
        query = str(kwargs.get("query", ""))
        category = str(kwargs.get("category", ""))
        tier = kwargs.get("tier")

        parts = []
        if context:
            parts.append(f"## CONTEXT\n{context}")

        parts.append("## DATABASE QUERY")
        if query:
            parts.append(f"Search for: {query}")
        if category:
            parts.append(f"Category: {category}")
        if tier is not None:
            parts.append(f"Tier: {tier}")

        # Include available categories
        parts.append(f"\nAvailable categories: {', '.join(self.get_categories())}")

        return "\n".join(parts)

    def parse_result(self, raw_output: str) -> dict:
        """Parse query results."""
        return {
            "status": "complete",
            "output": raw_output,
        }

    # ── Internal Search Helpers ──────────────────────────────

    def _search_dict_for_tier(
        self, data: object, tier: int,
        category: str, filename: str, results: list
    ) -> None:
        """Recursively search a dict/list for entries matching a tier."""
        if isinstance(data, dict):
            if data.get("tier") == tier:
                results.append({
                    **data,
                    "_source_category": category,
                    "_source_file": filename,
                })
            for value in data.values():
                self._search_dict_for_tier(
                    value, tier, category, filename, results
                )
        elif isinstance(data, list):
            for item in data:
                self._search_dict_for_tier(
                    item, tier, category, filename, results
                )

    def _search_dict_for_name(
        self, data: object, name_lower: str,
        category: str, filename: str, results: list
    ) -> None:
        """Recursively search for entries matching a name."""
        if isinstance(data, dict):
            entry_name = data.get("name", "")
            if isinstance(entry_name, str) and name_lower in entry_name.lower():
                results.append({
                    **data,
                    "_source_category": category,
                    "_source_file": filename,
                })
            for value in data.values():
                self._search_dict_for_name(
                    value, name_lower, category, filename, results
                )
        elif isinstance(data, list):
            for item in data:
                self._search_dict_for_name(
                    item, name_lower, category, filename, results
                )

    def _search_dict_for_field(
        self, data: object, field: str, value_lower: str,
        category: str, filename: str, results: list
    ) -> None:
        """Recursively search for entries where a field matches a value."""
        if isinstance(data, dict):
            field_val = data.get(field, "")
            if isinstance(field_val, str) and value_lower in field_val.lower():
                results.append({
                    **data,
                    "_source_category": category,
                    "_source_file": filename,
                })
            for value in data.values():
                self._search_dict_for_field(
                    value, field, value_lower, category, filename, results
                )
        elif isinstance(data, list):
            for item in data:
                self._search_dict_for_field(
                    item, field, value_lower, category, filename, results
                )
