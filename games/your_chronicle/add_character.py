#!/usr/bin/env python3
"""Add a new character/NPC to Your Chronicle and rebuild the database.

This is the "every new character we create gets put in the database" workflow.
It appends the character to the appropriate YAML source file (so it stays
version-controlled and human-editable) and then rebuilds your_chronicle.db.

Example:
    python add_character.py \
        --id CHR-NPC-016 --name "Garrick the Gravedigger" \
        --role "Cemetery Vendor" --role-category vendor \
        --persistence recurring --importance minor \
        --collection support_npcs \
        --chapters 4 5 6 \
        --backstory "Sells grave goods recovered from the Margins."

Valid categorizations (partitions):
    persistence : anchor | recurring | milestone | transient | seasonal
    role_category: quest_giver | trainer | vendor | dungeon | service | faction | lore
    importance  : key | major | minor
    collection  : main_quest_givers | support_npcs
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "characters"

VALID = {
    "persistence": {"anchor", "recurring", "milestone", "transient", "seasonal"},
    "role_category": {
        "quest_giver", "trainer", "vendor", "dungeon", "service", "faction", "lore",
    },
    "importance": {"key", "major", "minor"},
    "collection": {"main_quest_givers", "support_npcs"},
}

FILE_FOR_COLLECTION = {
    "main_quest_givers": DATA / "main_quest_givers.yaml",
    "support_npcs": DATA / "npcs.yaml",
}


def validate(field: str, value: str) -> str:
    if value not in VALID[field]:
        sys.exit(
            f"error: invalid {field} '{value}'. "
            f"Valid options: {', '.join(sorted(VALID[field]))}"
        )
    return value


def add_character(args: argparse.Namespace) -> None:
    for field in ("persistence", "role_category", "importance", "collection"):
        validate(field, getattr(args, field))

    target = FILE_FOR_COLLECTION[args.collection]
    doc = yaml.safe_load(target.read_text(encoding="utf-8"))
    doc.setdefault("characters", [])

    existing_ids = {c["id"] for c in doc["characters"]}
    if args.id in existing_ids:
        sys.exit(f"error: character id '{args.id}' already exists in {target.name}")

    character = {
        "id": args.id,
        "name": args.name,
        "title": args.title,
        "role": args.role,
        "role_category": args.role_category,
        "importance": args.importance,
        "persistence": args.persistence,
        "faction": args.faction,
        "home_location": args.location,
        "gives_main_quest": args.collection == "main_quest_givers",
        "appears_in_chapters": args.chapters,
        "personality": args.personality,
        "voice_sample": args.voice,
        "backstory": args.backstory,
        "lore_notes": args.lore,
    }
    if args.shop_id:
        character["shop_id"] = args.shop_id
    if args.shop_type:
        character["shop_type"] = args.shop_type
    if args.quests:
        character["quests_given"] = args.quests

    # drop empty optional fields for a clean YAML entry
    character = {k: v for k, v in character.items() if v not in (None, [], "")}

    doc["characters"].append(character)
    target.write_text(
        yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    print(f"Added {args.name} ({args.id}) to {target.relative_to(HERE)}")

    print("Rebuilding database...")
    subprocess.run([sys.executable, str(HERE / "build_database.py")], check=True)
    print("Done. The new character is now in your_chronicle.db.")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--id", required=True, help="unique id, e.g. CHR-NPC-016")
    p.add_argument("--name", required=True)
    p.add_argument("--role", required=True, help="display role, e.g. 'Cemetery Vendor'")
    p.add_argument("--role-category", required=True, dest="role_category")
    p.add_argument("--persistence", required=True)
    p.add_argument("--importance", default="minor")
    p.add_argument("--collection", default="support_npcs")
    p.add_argument("--title", default=None)
    p.add_argument("--faction", default=None)
    p.add_argument("--location", default=None)
    p.add_argument("--chapters", nargs="*", type=int, default=[], help="chapters the NPC appears in")
    p.add_argument("--personality", default=None)
    p.add_argument("--voice", default=None)
    p.add_argument("--backstory", default=None)
    p.add_argument("--lore", default=None)
    p.add_argument("--shop-id", dest="shop_id", default=None)
    p.add_argument("--shop-type", dest="shop_type", default=None)
    p.add_argument("--quests", nargs="*", default=[], help="main quests this NPC gives")
    add_character(p.parse_args())


if __name__ == "__main__":
    main()
