"""
Character Relationship Tracker — Tracks relationships between characters.

Maintains a relationship matrix that records how characters feel about
each other, their history, and how relationships change over time.
Critical for maintaining consistency across 1000+ chapters.
"""

from pathlib import Path
from typing import Optional

import yaml

from config import BOOK1_DIR


RELATIONSHIPS_FILE = BOOK1_DIR / "relationships.yaml"


class RelationshipTracker:
    """
    Tracks character relationships for the RP Conversion novel.

    Stores:
      - Relationship type (ally, enemy, neutral, family, mentor, rival, etc.)
      - Trust level (-100 to 100)
      - History of key interactions
      - Current status
      - Notes for agents
    """

    def __init__(self) -> None:
        self._relationships: dict = {}
        self._load()

    def _load(self) -> None:
        """Load relationships from disk."""
        if RELATIONSHIPS_FILE.exists():
            with open(RELATIONSHIPS_FILE, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                self._relationships = data if data else {}
        else:
            self._relationships = {}

    def _save(self) -> None:
        """Persist relationships to disk."""
        RELATIONSHIPS_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(RELATIONSHIPS_FILE, "w", encoding="utf-8") as f:
            yaml.dump(
                self._relationships,
                f,
                default_flow_style=False,
                sort_keys=False,
            )

    @staticmethod
    def _make_key(char_a: str, char_b: str) -> str:
        """Create a consistent key for a character pair."""
        return f"{char_a.strip()} <-> {char_b.strip()}"

    def set_relationship(
        self,
        char_a: str,
        char_b: str,
        rel_type: str = "neutral",
        trust: int = 0,
        status: str = "active",
        notes: str = "",
    ) -> dict:
        """
        Set or update a relationship between two characters.

        Args:
            char_a: First character name.
            char_b: Second character name.
            rel_type: Type (ally, enemy, neutral, family, mentor, rival,
                      romantic, business, commander, subordinate).
            trust: Trust level from -100 (bitter enemies) to 100 (absolute trust).
            status: Current status (active, strained, broken, developing, unknown).
            notes: Free-form notes about the relationship.

        Returns:
            The updated relationship entry.
        """
        key = self._make_key(char_a, char_b)
        entry = self._relationships.get(key, {
            "characters": [char_a.strip(), char_b.strip()],
            "history": [],
        })
        entry["type"] = rel_type
        entry["trust"] = max(-100, min(100, trust))
        entry["status"] = status
        if notes:
            entry["notes"] = notes
        self._relationships[key] = entry
        self._save()
        return entry

    def add_interaction(
        self,
        char_a: str,
        char_b: str,
        chapter: int,
        description: str,
        trust_change: int = 0,
    ) -> dict:
        """
        Record an interaction between two characters.

        Args:
            char_a: First character name.
            char_b: Second character name.
            chapter: Chapter number where the interaction occurs.
            description: Brief description of the interaction.
            trust_change: How much trust changed (+/- integer).

        Returns:
            The updated relationship entry.
        """
        key = self._make_key(char_a, char_b)
        if key not in self._relationships:
            self.set_relationship(char_a, char_b)

        entry = self._relationships[key]
        entry["history"].append({
            "chapter": chapter,
            "event": description,
            "trust_change": trust_change,
        })

        current_trust = entry.get("trust", 0)
        entry["trust"] = max(-100, min(100, current_trust + trust_change))

        self._relationships[key] = entry
        self._save()
        return entry

    def get_relationship(self, char_a: str, char_b: str) -> dict:
        """Get the relationship between two characters."""
        key = self._make_key(char_a, char_b)
        reverse_key = self._make_key(char_b, char_a)
        return self._relationships.get(
            key, self._relationships.get(reverse_key, {})
        )

    def get_all_relationships_for(self, character: str) -> list:
        """Get all relationships involving a specific character."""
        results = []
        char_lower = character.lower().strip()
        for key, entry in self._relationships.items():
            chars = entry.get("characters", [])
            for c in chars:
                if c.lower() == char_lower:
                    results.append(entry)
                    break
        return results

    def get_all_relationships(self) -> dict:
        """Return the full relationship matrix."""
        return dict(self._relationships)

    def build_relationship_context(self, characters: Optional[list] = None) -> str:
        """
        Build a context string of relationships for agent prompts.

        Args:
            characters: Optional list of character names to filter by.
                       If None, returns all relationships.

        Returns:
            Formatted string of relationship data.
        """
        sections = ["## CHARACTER RELATIONSHIPS"]

        if characters:
            seen = set()
            for char in characters:
                rels = self.get_all_relationships_for(char)
                for rel in rels:
                    key = tuple(sorted(rel.get("characters", [])))
                    if key in seen:
                        continue
                    seen.add(key)
                    sections.append(self._format_relationship(rel))
        else:
            for key, rel in self._relationships.items():
                sections.append(self._format_relationship(rel))

        if len(sections) == 1:
            sections.append("No relationships recorded yet.")

        return "\n\n".join(sections)

    @staticmethod
    def _format_relationship(rel: dict) -> str:
        """Format a single relationship entry as a readable string."""
        chars = rel.get("characters", ["Unknown", "Unknown"])
        lines = [
            f"### {chars[0]} <-> {chars[1]}",
            f"- Type: {rel.get('type', 'unknown')}",
            f"- Trust: {rel.get('trust', 0)}/100",
            f"- Status: {rel.get('status', 'unknown')}",
        ]
        if rel.get("notes"):
            lines.append(f"- Notes: {rel['notes']}")

        history = rel.get("history", [])
        if history:
            lines.append("- Recent history:")
            for event in history[-5:]:
                lines.append(
                    f"  - Ch.{event.get('chapter', '?')}: "
                    f"{event.get('event', '')} "
                    f"(trust {event.get('trust_change', 0):+d})"
                )
        return "\n".join(lines)

    def get_stats(self) -> dict:
        """Get summary stats about tracked relationships."""
        total = len(self._relationships)
        types: dict = {}
        for entry in self._relationships.values():
            t = entry.get("type", "unknown")
            types[t] = types.get(t, 0) + 1
        return {
            "total_relationships": total,
            "by_type": types,
        }
