#!/usr/bin/env python3
"""Export a compact JSON snapshot for the HTML/JS UI prototype.

Reads the built SQLite database and writes ui/game_data.json containing the
slices the prototype needs: currency tiers, rarity tiers, phases, buildings,
dungeons, a sample of materials/quests/achievements, NPCs, and the UI framework
(panels + buttons) parsed from ui_framework.yaml.

Run AFTER build_database.py.
"""
import json
import os
import sqlite3

try:
    import yaml
except ImportError:
    raise SystemExit("pyyaml required")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DB = os.path.join(ROOT, "your_chronicle.db")
UI = os.path.join(ROOT, "ui")
DATA = os.path.join(ROOT, "data")


def rows(conn, sql, *a):
    cur = conn.execute(sql, a)
    cols = [c[0] for c in cur.description]
    return [dict(zip(cols, r)) for r in cur.fetchall()]


def main():
    conn = sqlite3.connect(DB)
    ui_fw = yaml.safe_load(open(os.path.join(DATA, "systems", "ui_framework.yaml")))

    data = {
        "meta": {
            "game": "Your Chronicle",
            "generated_from": "your_chronicle.db",
        },
        "currency": rows(conn, "SELECT * FROM currency_tier ORDER BY tier"),
        "rarity": rows(conn, "SELECT * FROM rarity_category ORDER BY rank"),
        "phases": rows(conn, "SELECT idx,id,name,band,req,unlocks FROM phases ORDER BY idx"),
        "buildings": rows(conn, "SELECT * FROM buildings ORDER BY tier"),
        "dungeons": rows(conn, "SELECT * FROM dungeons ORDER BY idx"),
        "enemies": rows(conn, "SELECT id,name,family,base_hp,base_atk,base_xp,rank_band,kind FROM enemies"),
        "animals": rows(conn, "SELECT * FROM animals"),
        "npcs": rows(conn, "SELECT id,name,role,role_category,persistence,rarity,recruitable,can_die,archetype,base_stats FROM characters ORDER BY id"),
        # samples to keep the UI payload light; full data lives in the DB/JSON
        "materials_sample": rows(conn, "SELECT id,name,category,subtype,tier,rarity,reasons,use_note FROM materials ORDER BY RANDOM() LIMIT 120"),
        "quests_sample": rows(conn, "SELECT id,name,type,giver,phase,objective,unlock_condition,hidden FROM quests WHERE hidden=0 ORDER BY id LIMIT 120"),
        "achievements_sample": rows(conn, "SELECT id,name,description,category,condition,points,hidden FROM achievements WHERE hidden=0 ORDER BY id LIMIT 120"),
        "counts": {
            "characters": rows(conn, "SELECT COUNT(*) n FROM characters")[0]["n"],
            "materials": rows(conn, "SELECT COUNT(*) n FROM materials")[0]["n"],
            "quests": rows(conn, "SELECT COUNT(*) n FROM quests")[0]["n"],
            "achievements": rows(conn, "SELECT COUNT(*) n FROM achievements")[0]["n"],
            "phases": rows(conn, "SELECT COUNT(*) n FROM phases")[0]["n"],
            "dungeons": rows(conn, "SELECT COUNT(*) n FROM dungeons")[0]["n"],
            "enemies": rows(conn, "SELECT COUNT(*) n FROM enemies")[0]["n"],
            "animals": rows(conn, "SELECT COUNT(*) n FROM animals")[0]["n"],
        },
        "ui_framework": {
            "panels": ui_fw.get("panels", []),
            "buttons": ui_fw.get("buttons_examples", []),
            "visibility_states": ui_fw.get("visibility_states", []),
            "condition_grammar": ui_fw.get("condition_grammar", {}),
            "inventory_ui": ui_fw.get("inventory_ui", {}),
        },
    }
    os.makedirs(UI, exist_ok=True)
    with open(os.path.join(UI, "game_data.json"), "w") as f:
        json.dump(data, f, indent=1)
    conn.close()
    print(f"Wrote ui/game_data.json ({sum(data['counts'].values())} indexed records, "
          f"{len(data['ui_framework']['panels'])} panels).")


if __name__ == "__main__":
    main()
