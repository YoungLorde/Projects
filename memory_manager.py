"""
Memory Manager — Read/write interface for the Memory Bank.

Handles loading and saving story state, reading lore files,
character profiles, faction data, and all persistent memory
needed to maintain consistency across 1000+ chapters.
"""

from pathlib import Path
from typing import Optional

import yaml

from config import (
    CHARACTERS_DIR,
    CHAPTERS_DIR,
    CONFLICTS_DIR,
    DEFAULT_STORY_STATE,
    DRAFTS_DIR,
    FACTIONS_DIR,
    LOCATIONS_DIR,
    LORE_DIR,
    MASTER_BIBLE,
    OUTLINES_DIR,
    SPECIES_DIR,
    STATE_FILE,
    STORY_GUIDE,
    SYSTEMS_DIR,
    VEHICLES_DIR,
)


class MemoryManager:
    """Manages all persistent memory for the novel writing system."""

    def __init__(self) -> None:
        self._state: dict = {}
        self._ensure_directories()

    def _ensure_directories(self) -> None:
        """Create all required directories if they don't exist."""
        for directory in [
            CHAPTERS_DIR, OUTLINES_DIR, DRAFTS_DIR,
            LORE_DIR, CHARACTERS_DIR, FACTIONS_DIR,
            SPECIES_DIR, VEHICLES_DIR, SYSTEMS_DIR,
            CONFLICTS_DIR, LOCATIONS_DIR,
        ]:
            directory.mkdir(parents=True, exist_ok=True)

    # ── State Management ─────────────────────────────────────

    def load_state(self) -> dict:
        """Load the current story state from disk."""
        if STATE_FILE.exists():
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                self._state = yaml.safe_load(f) or {}
        else:
            self._state = dict(DEFAULT_STORY_STATE)
            self.save_state()
        return self._state

    def save_state(self) -> None:
        """Persist the current story state to disk."""
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            yaml.dump(self._state, f, default_flow_style=False, sort_keys=False)

    def get_state(self) -> dict:
        """Return the current in-memory state (load first if empty)."""
        if not self._state:
            self.load_state()
        return self._state

    def update_state(self, updates: dict) -> None:
        """Merge updates into the current state and save."""
        state = self.get_state()
        self._deep_merge(state, updates)
        self.save_state()

    @staticmethod
    def _deep_merge(base: dict, updates: dict) -> None:
        """Recursively merge updates into base dict."""
        for key, value in updates.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                MemoryManager._deep_merge(base[key], value)
            else:
                base[key] = value

    # ── Memory Bank Reading ──────────────────────────────────

    def read_file(self, filepath: Path) -> str:
        """Read a single file and return its contents."""
        if filepath.exists():
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    def read_master_bible(self) -> str:
        """Load the master novel bible."""
        return self.read_file(MASTER_BIBLE)

    def read_story_guide(self) -> str:
        """Load the story guide overview."""
        return self.read_file(STORY_GUIDE)

    def read_all_memory_bank(self) -> dict:
        """Read all memory bank files organized by category."""
        categories = {
            "lore": LORE_DIR,
            "characters": CHARACTERS_DIR,
            "factions": FACTIONS_DIR,
            "species": SPECIES_DIR,
            "vehicles": VEHICLES_DIR,
            "systems": SYSTEMS_DIR,
            "conflicts": CONFLICTS_DIR,
            "locations": LOCATIONS_DIR,
        }
        bank: dict = {}
        for category, directory in categories.items():
            bank[category] = {}
            if directory.exists():
                for file in sorted(directory.glob("*.md")):
                    bank[category][file.stem] = self.read_file(file)
        return bank

    def read_category(self, category: str) -> dict:
        """Read all files in a specific memory bank category."""
        category_dirs = {
            "lore": LORE_DIR,
            "characters": CHARACTERS_DIR,
            "factions": FACTIONS_DIR,
            "species": SPECIES_DIR,
            "vehicles": VEHICLES_DIR,
            "systems": SYSTEMS_DIR,
            "conflicts": CONFLICTS_DIR,
            "locations": LOCATIONS_DIR,
        }
        directory = category_dirs.get(category)
        if directory is None or not directory.exists():
            return {}
        result: dict = {}
        for file in sorted(directory.glob("*.md")):
            result[file.stem] = self.read_file(file)
        return result

    def read_character(self, name: str) -> str:
        """Read a specific character's profile."""
        filename = name.lower().replace(" ", "_") + ".md"
        filepath = CHARACTERS_DIR / filename
        return self.read_file(filepath)

    # ── Chapter Management ───────────────────────────────────

    def get_chapter_count(self) -> int:
        """Return the number of completed chapters."""
        return len(list(CHAPTERS_DIR.glob("chapter_*.md")))

    def get_next_chapter_number(self) -> int:
        """Return the next chapter number to write."""
        return self.get_chapter_count() + 1

    def read_chapter(self, chapter_num: int) -> str:
        """Read a specific chapter."""
        filename = f"chapter_{chapter_num:03d}.md"
        return self.read_file(CHAPTERS_DIR / filename)

    def save_chapter(self, chapter_num: int, content: str) -> Path:
        """Save a completed chapter."""
        filename = f"chapter_{chapter_num:03d}.md"
        filepath = CHAPTERS_DIR / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath

    def read_last_n_chapters(self, n: int = 3) -> list:
        """Read the last N chapters for context."""
        total = self.get_chapter_count()
        chapters = []
        start = max(1, total - n + 1)
        for i in range(start, total + 1):
            content = self.read_chapter(i)
            if content:
                chapters.append({"number": i, "content": content})
        return chapters

    def get_chapter_summary(self, chapter_num: int) -> str:
        """Get the summary for a specific chapter from state."""
        state = self.get_state()
        summaries = state.get("chapter_summaries", {})
        return summaries.get(str(chapter_num), "")

    def save_chapter_summary(self, chapter_num: int, summary: str) -> None:
        """Save a chapter summary to state."""
        state = self.get_state()
        if "chapter_summaries" not in state:
            state["chapter_summaries"] = {}
        state["chapter_summaries"][str(chapter_num)] = summary
        self.save_state()

    # ── Outline Management ───────────────────────────────────

    def save_outline(self, chapter_num: int, content: str) -> Path:
        """Save a chapter outline."""
        filename = f"outline_{chapter_num:03d}.md"
        filepath = OUTLINES_DIR / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath

    def read_outline(self, chapter_num: int) -> str:
        """Read a chapter outline."""
        filename = f"outline_{chapter_num:03d}.md"
        return self.read_file(OUTLINES_DIR / filename)

    # ── Draft Management ─────────────────────────────────────

    def save_draft(self, chapter_num: int, content: str, version: int = 1) -> Path:
        """Save a draft version of a chapter."""
        filename = f"draft_{chapter_num:03d}_v{version}.md"
        filepath = DRAFTS_DIR / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath

    # ── Memory Bank Writing ──────────────────────────────────

    def update_memory_file(self, category: str, filename: str, content: str) -> Path:
        """Write or update a memory bank file."""
        category_dirs = {
            "lore": LORE_DIR,
            "characters": CHARACTERS_DIR,
            "factions": FACTIONS_DIR,
            "species": SPECIES_DIR,
            "vehicles": VEHICLES_DIR,
            "systems": SYSTEMS_DIR,
            "conflicts": CONFLICTS_DIR,
            "locations": LOCATIONS_DIR,
        }
        directory = category_dirs.get(category)
        if directory is None:
            raise ValueError(f"Unknown memory bank category: {category}")
        directory.mkdir(parents=True, exist_ok=True)
        if not filename.endswith(".md"):
            filename += ".md"
        filepath = directory / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath

    # ── Context Building ─────────────────────────────────────

    def build_writing_context(self, chapter_num: Optional[int] = None) -> str:
        """
        Build the full context needed for writing a chapter.
        Includes: state, recent chapters, lore, character data.
        """
        if chapter_num is None:
            chapter_num = self.get_next_chapter_number()

        state = self.get_state()
        sections = []

        # Current story state
        sections.append("## CURRENT STORY STATE")
        sections.append(yaml.dump(state, default_flow_style=False))

        # Recent chapter summaries
        sections.append("## RECENT CHAPTER SUMMARIES")
        for i in range(max(1, chapter_num - 5), chapter_num):
            summary = self.get_chapter_summary(i)
            if summary:
                sections.append(f"### Chapter {i}\n{summary}")

        # Character states
        sections.append("## CHARACTER DATA")
        characters = self.read_category("characters")
        for name, data in characters.items():
            sections.append(f"### {name}\n{data[:2000]}")

        # Active conflicts
        sections.append("## ACTIVE CONFLICTS")
        conflicts = self.read_category("conflicts")
        for name, data in conflicts.items():
            sections.append(f"### {name}\n{data[:1500]}")

        # Current location data
        sections.append("## LOCATION DATA")
        locations = self.read_category("locations")
        for name, data in locations.items():
            sections.append(f"### {name}\n{data[:1500]}")

        # Core systems reference
        sections.append("## SYSTEMS REFERENCE")
        systems = self.read_category("systems")
        for name, data in systems.items():
            sections.append(f"### {name}\n{data[:1500]}")

        # Chapter outline if available
        outline = self.read_outline(chapter_num)
        if outline:
            sections.append(f"## OUTLINE FOR CHAPTER {chapter_num}")
            sections.append(outline)

        return "\n\n".join(sections)

    def build_lore_context(self) -> str:
        """Build lore-specific context for validation agents."""
        sections = []
        for category in ["lore", "systems", "species", "factions"]:
            data = self.read_category(category)
            for name, content in data.items():
                sections.append(f"## {category.upper()}: {name}\n{content}")
        return "\n\n".join(sections)

    def build_character_context(self) -> str:
        """Build character-specific context."""
        sections = []
        characters = self.read_category("characters")
        for name, content in characters.items():
            sections.append(f"## {name}\n{content}")
        return "\n\n".join(sections)
