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


def seed_rarity(conn: sqlite3.Connection) -> None:
    doc = load_yaml(DATA / "systems" / "rarity.yaml")
    for t in doc.get("tiers", []):
        conn.execute(
            """INSERT OR REPLACE INTO rarity_category
               (id, name, rank, color, drop_weight, value_mult, stat_roll_mult, description)
               VALUES (?,?,?,?,?,?,?,?)""",
            (t["id"], t["name"], t["rank"], t.get("color"), t.get("drop_weight"),
             t.get("value_mult"), t.get("stat_roll_mult"), t.get("description")),
        )


def seed_currency(conn: sqlite3.Connection) -> None:
    doc = load_yaml(DATA / "systems" / "currency.yaml")
    for t in doc.get("tiers", []):
        conn.execute(
            """INSERT OR REPLACE INTO currency_tier
               (id, name, tier, per_next, next_id, value_in_bronze, description)
               VALUES (?,?,?,?,?,?,?)""",
            (t["id"], t["name"], t["tier"], t.get("per_next"), t.get("next"),
             t.get("value_in_bronze"), t.get("description")),
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
            appearance, backstory, lore_notes, rewards_theme, shop_id, shop_type,
            rarity, recruitable, can_level, can_die, archetype, base_stats
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
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
            c.get("rarity"), as_bool_int(c.get("recruitable")),
            as_bool_int(c.get("can_level")), as_bool_int(c.get("can_die")),
            c.get("archetype"),
            json.dumps(c.get("base_stats")) if c.get("base_stats") else None,
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
            i.get("effect"), i.get("use_note") or i.get("use"), i.get("description"),
        ),
    )


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def seed_world_data(conn: sqlite3.Connection) -> None:
    # phases
    for p in load_yaml(DATA / "systems" / "phases.yaml").get("phases", []):
        conn.execute(
            "INSERT OR REPLACE INTO phases (idx, id, name, band, req, unlocks) VALUES (?,?,?,?,?,?)",
            (p["index"], p["id"], p["name"], p.get("band"), p.get("req"), p.get("unlocks")),
        )
    # buildings
    for b in load_yaml(DATA / "systems" / "buildings.yaml").get("dwelling_upgrade_path", []):
        conn.execute(
            "INSERT OR REPLACE INTO buildings (id, name, tier, pop_capacity, upgrade_to, unlocks) VALUES (?,?,?,?,?,?)",
            (b["id"], b["name"], b.get("tier"), b.get("pop_capacity"),
             b.get("upgrade_to"), json.dumps(b.get("unlocks", []))),
        )
    # dungeons
    for r in load_yaml(DATA / "systems" / "dungeons.yaml").get("ranks", []):
        conn.execute(
            "INSERT OR REPLACE INTO dungeons (idx, id, name, level_band, unlock_phase, max_rarity, boss, world_boss) VALUES (?,?,?,?,?,?,?,?)",
            (r["index"], r["id"], r["name"], r.get("level_band"), r.get("unlock_phase"),
             r.get("max_rarity"), r.get("boss"), r.get("world_boss")),
        )
    # enemies (types + bosses + world bosses)
    edoc = load_yaml(DATA / "enemies" / "enemies.yaml")
    for e in edoc.get("enemy_types", []):
        conn.execute(
            "INSERT OR REPLACE INTO enemies (id, name, family, base_hp, base_atk, base_xp, rank_band, traits, drop_theme, kind) VALUES (?,?,?,?,?,?,?,?,?,?)",
            (e["id"], e["name"], e.get("family"), e.get("base_hp"), e.get("base_atk"),
             e.get("base_xp"), e.get("rank_band"), json.dumps(e.get("traits", [])),
             e.get("drop_theme"), "enemy"),
        )
    for b in edoc.get("dungeon_bosses", []):
        conn.execute(
            "INSERT OR REPLACE INTO enemies (id, name, family, rank_band, kind) VALUES (?,?,?,?,?)",
            (b["id"], b["name"], b.get("enemy_family"), b.get("rank"), "boss"),
        )
    for w in edoc.get("world_bosses", []):
        conn.execute(
            "INSERT OR REPLACE INTO enemies (id, name, rank_band, kind) VALUES (?,?,?,?)",
            (w["id"], w["name"], w.get("rank_band"), "world_boss"),
        )
    # animals
    for a in load_yaml(DATA / "animals" / "animals.yaml").get("animals", []):
        conn.execute(
            "INSERT OR REPLACE INTO animals (id, name, type, habitat, tameable, yields, role) VALUES (?,?,?,?,?,?,?)",
            (a["id"], a["name"], a.get("type"), a.get("habitat"),
             as_bool_int(a.get("tameable")), a.get("yields"), a.get("role")),
        )
    # materials (base + exotic JSON catalogs)
    for fname in ("materials.json", "exotic_materials.json"):
        for m in load_json(DATA / "materials" / fname).get("materials", []):
            conn.execute(
                """INSERT OR REPLACE INTO materials
                   (id, name, category, subtype, tier, rarity, cost, currency,
                    reasons, source, use_note, description, perm_stat, perm_gain)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (m["id"], m["name"], m.get("category"), m.get("subtype"), m.get("tier"),
                 m.get("rarity"), m.get("cost"), m.get("currency"),
                 json.dumps(m.get("reasons", [])), m.get("source"), m.get("use_note"),
                 m.get("description"), m.get("perm_stat"), m.get("perm_gain")),
            )
    # quests
    for q in load_json(DATA / "quests" / "quests.json").get("quests", []):
        conn.execute(
            """INSERT OR REPLACE INTO quests
               (id, name, type, giver, phase, objective, unlock_condition, rewards, repeatable, hidden)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (q["id"], q["name"], q.get("type"), q.get("giver"), q.get("phase"),
             q.get("objective"), q.get("unlock_condition"), json.dumps(q.get("rewards")),
             as_bool_int(q.get("repeatable")), as_bool_int(q.get("hidden"))),
        )
    # achievements
    for a in load_json(DATA / "achievements" / "achievements.json").get("achievements", []):
        conn.execute(
            """INSERT OR REPLACE INTO achievements
               (id, name, description, category, condition, reward, points, hidden)
               VALUES (?,?,?,?,?,?,?,?)""",
            (a["id"], a["name"], a.get("description"), a.get("category"),
             a.get("condition"), json.dumps(a.get("reward")), a.get("points"),
             as_bool_int(a.get("hidden"))),
        )


def build() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.executescript(SCHEMA.read_text(encoding="utf-8"))

        world = load_yaml(DATA / "world_lore.yaml")
        seed_categories(conn, world)
        seed_rarity(conn)
        seed_currency(conn)

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

        seed_world_data(conn)

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
        print(f"\nTotal shop items: {total_items}")

        recruitable = conn.execute("SELECT COUNT(*) FROM characters WHERE recruitable=1").fetchone()[0]
        mortal = conn.execute("SELECT COUNT(*) FROM characters WHERE can_die=1").fetchone()[0]
        print(f"\nRecruitable NPCs: {recruitable} | Mortal (can die): {mortal}")

        def count(t):
            return conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

        print("\nWorld data tables:")
        for t in ("phases", "buildings", "dungeons", "enemies", "animals",
                  "materials", "quests", "achievements", "rarity_category", "currency_tier"):
            print(f"  {t:<18} {count(t)}")

        base_mat = conn.execute("SELECT COUNT(*) FROM materials WHERE category='base'").fetchone()[0]
        exotic_mat = conn.execute("SELECT COUNT(*) FROM materials WHERE category='exotic'").fetchone()[0]
        print(f"\nMaterials: {base_mat} base + {exotic_mat} exotic")

        hidden_q = conn.execute("SELECT COUNT(*) FROM quests WHERE hidden=1").fetchone()[0]
        hidden_a = conn.execute("SELECT COUNT(*) FROM achievements WHERE hidden=1").fetchone()[0]
        print(f"Hidden content: {hidden_q} quests + {hidden_a} achievements")

        print("\nQuests by type:")
        for row in conn.execute("SELECT type, COUNT(*) n FROM quests GROUP BY type ORDER BY n DESC"):
            print(f"  {row['type']:<14} {row['n']}")

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
