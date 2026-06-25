"""
Pipeline Definitions — Pre-configured agent workflows.

Each pipeline defines a sequence of agents that process content
for different writing needs. Pipelines can be selected by name
when initiating a writing task.
"""

from typing import Optional

# ── Pipeline Definitions ─────────────────────────────────────

PIPELINES: dict = {
    "quality_prose_with_revision": {
        "name": "Quality Prose with Revision",
        "description": (
            "Writes prose, checks lore, revises if issues found. "
            "Best quality for lore-heavy stories."
        ),
        "steps": [
            "summarizer",
            "prose_writer",
            "lore_judge",
            "prose_writer",
        ],
        "tags": ["quality", "lore", "revision"],
    },
    "quick_draft": {
        "name": "Quick Draft",
        "description": (
            "Direct prose generation without validation. "
            "Fast but no quality checks."
        ),
        "steps": ["prose_writer"],
        "tags": ["fast", "draft"],
    },
    "polished_output": {
        "name": "Polished Output",
        "description": (
            "Writes prose then polishes for style. "
            "Good for final-draft quality."
        ),
        "steps": ["prose_writer", "style_editor"],
        "tags": ["quality", "style"],
    },
    "dialogue_polish": {
        "name": "Dialogue Polish",
        "description": (
            "Writes prose then improves dialogue. "
            "Good for dialogue-heavy scenes."
        ),
        "steps": ["prose_writer", "dialogue_specialist"],
        "tags": ["dialogue", "quality"],
    },
    "full_quality": {
        "name": "Full Quality Pipeline",
        "description": (
            "Maximum quality. Summarize, write, lore check, "
            "continuity check, revise, track stats."
        ),
        "steps": [
            "summarizer",
            "prose_writer",
            "lore_judge",
            "continuity_checker",
            "prose_writer",
            "stat_currency_tracker",
        ],
        "tags": ["maximum", "quality", "lore", "continuity", "stats"],
    },
    "quality_with_lore_check": {
        "name": "Quality Prose with Lore Check",
        "description": (
            "Writes prose, validates against lorebook. "
            "Streams the prose output."
        ),
        "steps": ["summarizer", "prose_writer", "lore_judge"],
        "tags": ["quality", "lore", "streaming"],
    },
    "push_prompt_self_correction": {
        "name": "Push Prompt Self-Correction",
        "description": (
            "Writes prose, checks for AI refusal, "
            "re-prompts if refusal detected."
        ),
        "steps": [
            "summarizer",
            "prose_writer",
            "refusal_checker",
            "prose_writer",
        ],
        "tags": ["anti-refusal", "self-correction"],
    },
    "outline_and_write": {
        "name": "Outline Then Write",
        "description": (
            "Generates scene beats first, then writes prose "
            "based on the outline. Good for complex chapters."
        ),
        "steps": [
            "scene_beat_generator",
            "prose_writer",
            "lore_judge",
        ],
        "tags": ["planned", "quality"],
    },
    "full_editorial": {
        "name": "Full Editorial Pipeline",
        "description": (
            "Maximum quality with style and dialogue polish. "
            "Outline, write, check lore, check continuity, "
            "polish style, improve dialogue, track stats."
        ),
        "steps": [
            "summarizer",
            "scene_beat_generator",
            "prose_writer",
            "lore_judge",
            "continuity_checker",
            "prose_writer",
            "style_editor",
            "dialogue_specialist",
            "stat_currency_tracker",
        ],
        "tags": ["maximum", "editorial", "complete", "stats"],
    },
}


def get_pipeline(name: str) -> Optional[dict]:
    """
    Get a pipeline configuration by name.

    Supports both exact keys and fuzzy matching by pipeline display name.

    Args:
        name: Pipeline key or display name.

    Returns:
        Pipeline config dict, or None if not found.
    """
    # Exact key match
    if name in PIPELINES:
        return PIPELINES[name]

    # Fuzzy match by display name
    name_lower = name.lower().strip()
    for key, pipeline in PIPELINES.items():
        if pipeline["name"].lower() == name_lower:
            return pipeline

    # Partial match
    for key, pipeline in PIPELINES.items():
        if name_lower in pipeline["name"].lower() or name_lower in key:
            return pipeline

    return None


def list_pipelines() -> list:
    """Return a list of all available pipelines with their descriptions."""
    return [
        {
            "key": key,
            "name": config["name"],
            "description": config["description"],
            "steps": config["steps"],
            "step_count": len(config["steps"]),
            "tags": config.get("tags", []),
        }
        for key, config in PIPELINES.items()
    ]
