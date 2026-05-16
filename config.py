"""
Global configuration for the RP Conversion Novel Writing System.
All paths, defaults, and agent settings are centralized here.
"""

from pathlib import Path

# ── Project Root ──────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent

# ── Directory Paths ───────────────────────────────────────────
GUIDES_DIR = PROJECT_ROOT / "guides"
BOOKS_DIR = PROJECT_ROOT / "books"
BOOK1_DIR = BOOKS_DIR / "rp_conversion"
CHAPTERS_DIR = BOOK1_DIR / "chapters"
OUTLINES_DIR = BOOK1_DIR / "outlines"
DRAFTS_DIR = BOOK1_DIR / "drafts"
MEMORY_BANK_DIR = PROJECT_ROOT / "memory_bank"
AGENTS_DIR = PROJECT_ROOT / "agents"
PIPELINES_DIR = PROJECT_ROOT / "pipelines"

# ── Memory Bank Sub-Directories ──────────────────────────────
LORE_DIR = MEMORY_BANK_DIR / "lore"
CHARACTERS_DIR = MEMORY_BANK_DIR / "characters"
FACTIONS_DIR = MEMORY_BANK_DIR / "factions"
SPECIES_DIR = MEMORY_BANK_DIR / "species"
VEHICLES_DIR = MEMORY_BANK_DIR / "vehicles"
SYSTEMS_DIR = MEMORY_BANK_DIR / "systems"
CONFLICTS_DIR = MEMORY_BANK_DIR / "conflicts"
LOCATIONS_DIR = MEMORY_BANK_DIR / "locations"

# ── Key Files ─────────────────────────────────────────────────
MASTER_BIBLE = GUIDES_DIR / "master_novel_bible.md"
STORY_GUIDE = GUIDES_DIR / "story_guide_overview.md"
CHAPTER_GUIDE = GUIDES_DIR / "chapter_guide.md"

# ── Novel Defaults ────────────────────────────────────────────
NOVEL_TITLE = "RP Conversion"
MIN_WORD_COUNT = 2500
DEFAULT_BOOK = "rp_conversion"

# ── State Tracking File ──────────────────────────────────────
STATE_FILE = BOOK1_DIR / "story_state.yaml"

# ── Default Story State ──────────────────────────────────────
DEFAULT_STORY_STATE = {
    "current_chapter": 0,
    "mohamed": {
        "level": 1,
        "rank": "Scavenger",
        "stats": {
            "STR": 5, "AGI": 5, "END": 5,
            "INT": 4, "PER": 5, "LCK": 7, "SYS": 1,
        },
        "rp_balance": 0,
        "rp_multiplier": 1.0,
        "assimilation_stage": "Interface Sync",
    },
    "vehicle": {
        "tier": 0,
        "sub_level": "Starter",
        "upgrades_installed": [],
        "exterior_stage": "Starter Mini Van",
        "pocket_dimension_stage": 0,
    },
    "zero_ai": {
        "tier": 0,
        "personality_stage": "Not Installed",
    },
    "location": "Earth - Unknown Zone",
    "arc": 1,
    "arc_name": "Day Zero",
    "active_plot_threads": [],
    "characters_introduced": ["Mohamed Vance"],
    "chapter_summaries": {},
}

# ── Agent Configurations ─────────────────────────────────────

AGENT_CONFIGS = {
    "lore_judge": {
        "name": "Lore Judge",
        "role": "Lore Consistency Checker",
        "temperature": 0.20,
        "max_tokens": 2048,
    },
    "prose_writer": {
        "name": "Prose Writer",
        "role": "Fiction Prose Writer",
        "temperature": 0.85,
        "max_tokens": 8192,
    },
    "refusal_checker": {
        "name": "Refusal Checker",
        "role": "Content Refusal Detector",
        "temperature": 0.80,
        "max_tokens": 200,
    },
    "style_extractor": {
        "name": "Style Extractor",
        "role": "Literary Style Analyst",
        "temperature": 0.30,
        "max_tokens": 2000,
    },
    "dialogue_specialist": {
        "name": "Dialogue Specialist",
        "role": "Dialogue Enhancement Expert",
        "temperature": 0.70,
        "max_tokens": 2048,
    },
    "plot_checker": {
        "name": "Plot Checker",
        "role": "Plot Hole Detector",
        "temperature": 0.30,
        "max_tokens": 8192,
    },
    "continuity_checker": {
        "name": "Continuity Checker",
        "role": "Timeline & Continuity Validator",
        "temperature": 0.20,
        "max_tokens": 600,
    },
    "style_editor": {
        "name": "Style Editor",
        "role": "Prose Style Polisher",
        "temperature": 0.60,
        "max_tokens": 2048,
    },
    "scene_beat_generator": {
        "name": "Scene Beat Generator",
        "role": "Scene Planning Assistant",
        "temperature": 0.75,
        "max_tokens": 1500,
    },
    "summarizer": {
        "name": "Summarizer",
        "role": "Narrative Summarizer",
        "temperature": 0.30,
        "max_tokens": 2000,
    },
    "outline_generator": {
        "name": "Outline Generator",
        "role": "Story Structure Planner",
        "temperature": 0.70,
        "max_tokens": 6000,
    },
    "word_count_enforcer": {
        "name": "Word Count Enforcer",
        "role": "Word Count Validator",
        "temperature": 0.10,
        "max_tokens": 500,
    },
    "parameter_enforcer": {
        "name": "Parameter Enforcer",
        "role": "Parameter Compliance Validator",
        "temperature": 0.10,
        "max_tokens": 1000,
    },
    "stat_currency_tracker": {
        "name": "Stat & Currency Tracker",
        "role": "Stat, Currency & Progression Tracker",
        "temperature": 0.15,
        "max_tokens": 2000,
    },
}

# ── Pipeline Configurations ──────────────────────────────────

PIPELINE_CONFIGS = {
    "quality_prose_with_revision": {
        "name": "Quality Prose with Revision",
        "description": (
            "Writes prose, checks lore, revises if issues found. "
            "Best quality for lore-heavy stories."
        ),
        "steps": ["summarizer", "prose_writer", "lore_judge", "prose_writer"],
    },
    "quick_draft": {
        "name": "Quick Draft",
        "description": (
            "Direct prose generation without validation. "
            "Fast but no quality checks."
        ),
        "steps": ["prose_writer"],
    },
    "polished_output": {
        "name": "Polished Output",
        "description": (
            "Writes prose then polishes for style. "
            "Good for final-draft quality."
        ),
        "steps": ["prose_writer", "style_editor"],
    },
    "dialogue_polish": {
        "name": "Dialogue Polish",
        "description": (
            "Writes prose then improves dialogue. "
            "Good for dialogue-heavy scenes."
        ),
        "steps": ["prose_writer", "dialogue_specialist"],
    },
    "full_quality": {
        "name": "Full Quality Pipeline",
        "description": (
            "Maximum quality. Summarize, write, lore check, "
            "continuity check, revise, track stats."
        ),
        "steps": [
            "summarizer", "prose_writer", "lore_judge",
            "continuity_checker", "prose_writer",
            "stat_currency_tracker",
        ],
    },
    "quality_with_lore_check": {
        "name": "Quality Prose with Lore Check",
        "description": (
            "Writes prose, validates against lorebook. "
            "Streams the prose output."
        ),
        "steps": ["summarizer", "prose_writer", "lore_judge"],
    },
    "push_prompt_self_correction": {
        "name": "Push Prompt Self-Correction",
        "description": (
            "Writes prose, checks for AI refusal, "
            "re-prompts if refusal detected."
        ),
        "steps": ["summarizer", "prose_writer", "refusal_checker", "prose_writer"],
    },
}
