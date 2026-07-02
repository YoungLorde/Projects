"""
Conflict Resolution State Machine — Tracks active and resolved plot conflicts.

Manages the lifecycle of conflicts from introduction through escalation,
climax, and resolution. Prevents plot threads from being forgotten across
1000+ chapters.
"""

from pathlib import Path
from typing import Optional

import yaml

from config import BOOK1_DIR


CONFLICTS_STATE_FILE = BOOK1_DIR / "conflicts_state.yaml"

# Valid conflict states (lifecycle)
CONFLICT_STATES = [
    "introduced",     # Conflict has been introduced but not yet developed
    "developing",     # Conflict is being developed through events
    "escalating",     # Conflict is intensifying
    "climax",         # Conflict has reached its peak
    "resolving",      # Conflict is being resolved
    "resolved",       # Conflict has been fully resolved
    "dormant",        # Conflict is temporarily inactive (can reactivate)
    "abandoned",      # Conflict was dropped (should be rare — flag these)
]

CONFLICT_TYPES = [
    "personal",       # Character vs character
    "faction",        # Faction vs faction
    "survival",       # Character vs environment/system
    "mystery",        # Unknown threat or puzzle
    "political",      # Power struggles, governance
    "economic",       # Resource conflicts, trade wars
    "existential",    # Species-level or universe-level threats
    "internal",       # Character's internal struggle
]


class ConflictTracker:
    """
    Tracks plot conflicts through their lifecycle.

    Each conflict has:
      - id: Unique identifier
      - name: Brief conflict name
      - type: Conflict type
      - state: Current lifecycle state
      - introduced_chapter: When it was first introduced
      - participants: Characters/factions involved
      - stakes: What's at risk
      - history: State transitions with chapter numbers
      - resolution: How it was resolved (when applicable)
      - related_conflicts: Links to connected conflicts
    """

    def __init__(self) -> None:
        self._conflicts: dict = {}
        self._next_id = 1
        self._load()

    def _load(self) -> None:
        """Load conflict state from disk."""
        if CONFLICTS_STATE_FILE.exists():
            with open(CONFLICTS_STATE_FILE, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                if data:
                    self._conflicts = data.get("conflicts", {})
                    self._next_id = data.get("next_id", 1)

    def _save(self) -> None:
        """Persist conflict state to disk."""
        CONFLICTS_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(CONFLICTS_STATE_FILE, "w", encoding="utf-8") as f:
            yaml.dump(
                {
                    "conflicts": self._conflicts,
                    "next_id": self._next_id,
                },
                f,
                default_flow_style=False,
                sort_keys=False,
            )

    def add_conflict(
        self,
        name: str,
        conflict_type: str = "personal",
        chapter: int = 0,
        participants: Optional[list] = None,
        stakes: str = "",
        description: str = "",
        related: Optional[list] = None,
    ) -> dict:
        """
        Register a new conflict.

        Args:
            name: Brief conflict name (e.g., "Mohamed vs Crimson Harvest Raiders").
            conflict_type: Type from CONFLICT_TYPES.
            chapter: Chapter where the conflict is introduced.
            participants: List of character/faction names involved.
            stakes: What's at risk if the conflict is lost.
            description: Detailed description of the conflict.
            related: List of related conflict IDs.

        Returns:
            The created conflict entry.
        """
        conflict_id = f"CONF-{self._next_id:04d}"
        self._next_id += 1

        entry = {
            "id": conflict_id,
            "name": name,
            "type": conflict_type if conflict_type in CONFLICT_TYPES else "personal",
            "state": "introduced",
            "introduced_chapter": chapter,
            "participants": participants or [],
            "stakes": stakes,
            "description": description,
            "related_conflicts": related or [],
            "history": [
                {
                    "chapter": chapter,
                    "state": "introduced",
                    "event": f"Conflict introduced: {name}",
                }
            ],
            "resolution": "",
        }

        self._conflicts[conflict_id] = entry
        self._save()
        return entry

    def transition(
        self,
        conflict_id: str,
        new_state: str,
        chapter: int,
        event: str = "",
    ) -> dict:
        """
        Transition a conflict to a new state.

        Args:
            conflict_id: The conflict ID.
            new_state: Target state from CONFLICT_STATES.
            chapter: Chapter where the transition occurs.
            event: Description of what caused the transition.

        Returns:
            The updated conflict entry.
        """
        if conflict_id not in self._conflicts:
            return {"error": f"Conflict {conflict_id} not found"}
        if new_state not in CONFLICT_STATES:
            return {"error": f"Invalid state: {new_state}"}

        entry = self._conflicts[conflict_id]
        old_state = entry["state"]
        entry["state"] = new_state
        entry["history"].append({
            "chapter": chapter,
            "state": new_state,
            "from_state": old_state,
            "event": event or f"Transitioned from {old_state} to {new_state}",
        })

        if new_state == "resolved" and not entry["resolution"]:
            entry["resolution"] = event

        self._conflicts[conflict_id] = entry
        self._save()
        return entry

    def resolve(
        self,
        conflict_id: str,
        chapter: int,
        resolution: str,
    ) -> dict:
        """
        Resolve a conflict.

        Args:
            conflict_id: The conflict ID.
            chapter: Chapter where resolution occurs.
            resolution: How the conflict was resolved.

        Returns:
            The updated conflict entry.
        """
        if conflict_id not in self._conflicts:
            return {"error": f"Conflict {conflict_id} not found"}

        entry = self._conflicts[conflict_id]
        entry["resolution"] = resolution
        return self.transition(conflict_id, "resolved", chapter, resolution)

    def get_conflict(self, conflict_id: str) -> dict:
        """Get a specific conflict by ID."""
        return self._conflicts.get(conflict_id, {})

    def get_active_conflicts(self) -> list:
        """Get all conflicts that are not resolved, dormant, or abandoned."""
        active_states = {"introduced", "developing", "escalating", "climax", "resolving"}
        return [
            entry for entry in self._conflicts.values()
            if entry.get("state") in active_states
        ]

    def get_resolved_conflicts(self) -> list:
        """Get all resolved conflicts."""
        return [
            entry for entry in self._conflicts.values()
            if entry.get("state") == "resolved"
        ]

    def get_dormant_conflicts(self) -> list:
        """Get all dormant (temporarily inactive) conflicts."""
        return [
            entry for entry in self._conflicts.values()
            if entry.get("state") == "dormant"
        ]

    def get_conflicts_for_character(self, character: str) -> list:
        """Get all conflicts involving a specific character."""
        char_lower = character.lower().strip()
        results = []
        for entry in self._conflicts.values():
            for p in entry.get("participants", []):
                if p.lower().strip() == char_lower:
                    results.append(entry)
                    break
        return results

    def get_stale_conflicts(self, current_chapter: int, threshold: int = 20) -> list:
        """
        Find conflicts that haven't had activity in N chapters.

        These are potential forgotten plot threads that need attention.

        Args:
            current_chapter: The current chapter number.
            threshold: Number of chapters of inactivity before flagging.

        Returns:
            List of stale conflict entries.
        """
        stale = []
        active_states = {"introduced", "developing", "escalating", "climax", "resolving"}
        for entry in self._conflicts.values():
            if entry.get("state") not in active_states:
                continue
            history = entry.get("history", [])
            if not history:
                continue
            last_chapter = max(h.get("chapter", 0) for h in history)
            if current_chapter - last_chapter >= threshold:
                stale.append({
                    **entry,
                    "chapters_since_activity": current_chapter - last_chapter,
                })
        return stale

    def build_conflict_context(self, current_chapter: int = 0) -> str:
        """
        Build a context string of active conflicts for agent prompts.

        Returns:
            Formatted string listing active conflicts with their states.
        """
        sections = ["## ACTIVE PLOT CONFLICTS"]

        active = self.get_active_conflicts()
        if not active:
            sections.append("No active conflicts.")
            return "\n\n".join(sections)

        for conflict in active:
            lines = [
                f"### {conflict.get('name', 'Unknown')} [{conflict.get('id', '')}]",
                f"- Type: {conflict.get('type', 'unknown')}",
                f"- State: {conflict.get('state', 'unknown')}",
                f"- Participants: {', '.join(conflict.get('participants', []))}",
                f"- Stakes: {conflict.get('stakes', 'unknown')}",
            ]
            history = conflict.get("history", [])
            if history:
                last = history[-1]
                lines.append(
                    f"- Last activity: Ch.{last.get('chapter', '?')} — "
                    f"{last.get('event', 'Unknown event')}"
                )
            sections.append("\n".join(lines))

        # Flag stale conflicts
        if current_chapter > 0:
            stale = self.get_stale_conflicts(current_chapter)
            if stale:
                sections.append("### WARNING: STALE CONFLICTS (no activity 20+ chapters)")
                for s in stale:
                    sections.append(
                        f"- {s.get('name', '?')} [{s.get('id', '')}] — "
                        f"{s.get('chapters_since_activity', '?')} chapters inactive"
                    )

        return "\n\n".join(sections)

    def get_stats(self) -> dict:
        """Get summary stats about tracked conflicts."""
        total = len(self._conflicts)
        by_state: dict = {}
        by_type: dict = {}
        for entry in self._conflicts.values():
            s = entry.get("state", "unknown")
            t = entry.get("type", "unknown")
            by_state[s] = by_state.get(s, 0) + 1
            by_type[t] = by_type.get(t, 0) + 1
        return {
            "total_conflicts": total,
            "by_state": by_state,
            "by_type": by_type,
        }
