#!/usr/bin/env python3
"""Build the Your Chronicle game-asset SQLite database from the YAML sources.

Usage:
    python build_database.py            # (re)build your_chronicle.db from data/
    python build_database.py --stats    # build, then print a summary report

The YAML files under data/ are the source of truth. This script is idempotent:
it drops and rebuilds the database from scratch every run, so re-running it after
adding a new character/item simply regenerates the database.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
SCHEMA = HERE / "schema.sql"
DB_PATH = HERE / "your_chronicle.db"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def as_bool_int(value) -> int:
    return 1 if value else 0


def seed_categories(conn: sqlite3.Connection, world: dict) -> None:
    legend = world.get("categorization_legend", {})
    for table, key in (
        ("persistence_category", "persistence"),
        ("role_category", "role_category"),
        ("importance_category", "importance"),
    ):
        for entry in legend.get(key, {}).get("values", []):
            if isinstance(entry, dict):
                cid, desc = entry["id"], entry.get("meaning", "")
            else:
                cid, desc = str(entry), ""
            conn.execute(
                f"INSERT OR REPLACE INTO {table} (id, description) VALUES (?, ?)",
                (cid, desc),
            )


def insert_character(conn: sqlite3.Connection, collection: str, c: dict) -> None:
    chapters = c.get("appears_in_chapters") or []
    appearance_count = len(chapters)
    first = c.get("first_appearance_chapter")
    last = c.get("last_appearance_chapter")
    if first is None and chapters:
        first = min(chapters)
    if last is None and chapters:
        last = max(chapters)

    conn.execute(
        """
        INSERT OR REPLACE INTO characters (
            id, name, title, role, collection, role_category, persistence,
            importance, faction, home_location, gives_main_quest,
            appears_in_chapters, first_appearance_chapter, last_appearance_chapter,
            appearance_count, unlock_condition, personality, voice_sample,
            appearance, backstory, lore_notes, rewards_theme, shop_id, shop_type
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        (
            c["id"], c["name"], c.get("title"), c.get("role"), collection,
            c.get("role_category"), c.get("persistence"), c.get("importance"),
            c.get("faction"), c.get("home_location"),
            as_bool_int(c.get("gives_main_quest")),
            json.dumps(chapters), first, last, appearance_count,
            c.get("unlock_condition"), c.get("personality"), c.get("voice_sample"),
            c.get("appearance"), c.get("backstory"), c.get("lore_notes"),
            c.get("rewards_theme"), c.get("shop_id"), c.get("shop_type"),
        ),
    )
    for quest in c.get("quests_given", []) or []:
        conn.execute(
            "INSERT INTO character_quests (character_id, quest) VALUES (?, ?)",
            (c["id"], quest),
        )


def insert_shop(conn: sqlite3.Connection, s: dict) -> None:
    conn.execute(
        """
        INSERT OR REPLACE INTO shops
            (id, name, shop_type, vendor_id, tier_range, location, currency, description)
        VALUES (?,?,?,?,?,?,?,?)
        """,
        (
            s["id"], s["name"], s["shop_type"], s.get("vendor_id"),
            s.get("tier_range"), s.get("location"), s.get("currency"),
            s.get("description"),
        ),
    )


def insert_item(conn: sqlite3.Connection, shop_type: str, i: dict) -> None:
    conn.execute(
        """
        INSERT OR REPLACE INTO items (
            id, name, shop_type, subtype, tier, rarity, cost, currency,
            click_power, idle_power, duration, effect, use_note, description
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        (
            i["id"], i["name"], shop_type, i.get("subtype"), i.get("tier"),
            i.get("rarity"), i.get("cost"), i.get("currency"),
            i.get("click_power"), i.get("idle_power"), i.get("duration"),
            i.get("effect"), i.get("use"), i.get("description"),
        ),
    )


def build() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.executescript(SCHEMA.read_text(encoding="utf-8"))

        world = load_yaml(DATA / "world_lore.yaml")
        seed_categories(conn, world)

        for fname in ("main_quest_givers.yaml", "npcs.yaml"):
            doc = load_yaml(DATA / "characters" / fname)
            collection = doc.get("collection", fname.replace(".yaml", ""))
            for c in doc.get("characters", []):
                insert_character(conn, collection, c)

        shops_doc = load_yaml(DATA / "shops" / "shops.yaml")
        for s in shops_doc.get("shops", []):
            insert_shop(conn, s)

        for fname in ("weapons.yaml", "potions.yaml", "materials.yaml"):
            doc = load_yaml(DATA / "shops" / fname)
            shop_type = doc["shop_type"]
            for i in doc.get("items", []):
                insert_item(conn, shop_type, i)

        conn.commit()
    finally:
        conn.close()


def print_stats() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        print("=" * 60)
        print("YOUR CHRONICLE — asset database summary")
        print("=" * 60)

        total_chars = conn.execute("SELECT COUNT(*) FROM characters").fetchone()[0]
        quest_givers = conn.execute(
            "SELECT COUNT(*) FROM characters WHERE gives_main_quest = 1"
        ).fetchone()[0]
        print(f"\nCharacters: {total_chars} total ({quest_givers} main-quest givers)")

        print("\nBy persistence category (partition):")
        for row in conn.execute(
            "SELECT persistence, COUNT(*) n FROM characters "
            "GROUP BY persistence ORDER BY n DESC"
        ):
            print(f"  {row['persistence']:<12} {row['n']}")

        print("\nBy role category:")
        for row in conn.execute(
            "SELECT role_category, COUNT(*) n FROM characters "
            "GROUP BY role_category ORDER BY n DESC"
        ):
            print(f"  {row['role_category']:<12} {row['n']}")

        print("\nTransient (appear once/twice then gone):")
        for row in conn.execute("SELECT name, role FROM transient_characters"):
            print(f"  - {row['name']} ({row['role']})")

        print("\nShops & catalog sizes:")
        for row in conn.execute(
            "SELECT shop_type, COUNT(*) n FROM items GROUP BY shop_type ORDER BY n DESC"
        ):
            print(f"  {row['shop_type']:<12} {row['n']} items")

        total_items = conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]
        print(f"\nTotal items: {total_items}")
        print("=" * 60)
    finally:
        conn.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the Your Chronicle asset DB.")
    parser.add_argument("--stats", action="store_true", help="print a summary report")
    args = parser.parse_args()
    build()
    print(f"Built {DB_PATH.relative_to(HERE.parent)}")
    if args.stats:
        print_stats()


if __name__ == "__main__":
    main()
