#!/usr/bin/env python3
"""Generate the achievement catalog (>= 500) -> data/achievements/achievements.json.

Includes normal AND hidden achievements (revealed only when their condition is met).
Each has a machine-checkable condition expressed in the UI condition grammar.
Deterministic (seeded).
"""
import json
import os
import random

try:
    import yaml
except ImportError:
    raise SystemExit("pyyaml required: pip install pyyaml")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
D = os.path.join(ROOT, "data")


def load(*p):
    with open(os.path.join(D, *p)) as f:
        return yaml.safe_load(f)


def human(n):
    units = ["", "K", "M", "B", "T", "Qa", "Qi"]
    i = 0
    n = float(n)
    while n >= 1000 and i < len(units) - 1:
        n /= 1000.0
        i += 1
    return (f"{n:.0f}{units[i]}" if n == int(n) else f"{n:.1f}{units[i]}")


def main():
    random.seed(424242)
    phases = load("systems", "phases.yaml")["phases"]
    buildings = load("systems", "buildings.yaml")["dwelling_upgrade_path"]
    dungeons = load("systems", "dungeons.yaml")["ranks"]
    enemies = load("enemies", "enemies.yaml")["enemy_types"]
    rarities = [r["id"] for r in load("systems", "rarity.yaml")["tiers"]]
    recruitable = [c for c in load("characters", "npcs.yaml")["characters"] +
                   load("characters", "main_quest_givers.yaml")["characters"]
                   if c.get("recruitable")]

    achs = []
    aid = 1

    def add(name, desc, category, condition, reward, points=10, hidden=False):
        nonlocal aid
        achs.append({
            "id": f"ACH-{aid:04d}",
            "name": name,
            "description": desc,
            "category": category,
            "condition": condition,
            "reward": reward,
            "points": points,
            "hidden": hidden,
        })
        aid += 1

    # progression: per phase
    for p in phases:
        add(f"{p['name']} Achieved", f"Reach the {p['name']} phase.", "progression",
            f"phase_index >= {p['index']}", {"all_gain_mult": 1.01}, points=10 + p['index'])

    # population milestones
    for n in [2, 5, 10, 25, 50, 100, 250, 500, 1000, 5000, 10000, 100000,
              1000000, 100000000, 1000000000, 1000000000000]:
        add(f"Population {human(n)}", f"Reach a total population of {human(n)}.",
            "population", f"population >= {n}", {"xp_mult": 1.01}, points=10)

    # currency milestones
    for cur in ["bronze", "silver", "gold", "zenu_coin", "mythril_coin"]:
        for n in [100, 10000, 1000000, 100000000]:
            add(f"Hoard {human(n)} {cur.replace('_',' ').title()}",
                f"Accumulate {human(n)} {cur}.", "currency",
                f"currency.{cur} >= {n}", {"all_gain_mult": 1.005}, points=10)

    # buildings
    for b in buildings:
        add(f"Built: {b['name']}", f"Construct the {b['name']}.", "building",
            f"building.{b['id']}.tier >= 1", {"pop_cap_mult": 1.01}, points=15)

    # dungeon clears + bosses + world bosses
    for r in dungeons:
        add(f"{r['name']} Conqueror", f"Clear an {r['name']} dungeon.", "dungeon",
            f"dungeon_rank_cleared >= {r['index']}", {"drop_mult": 1.01}, points=20)
        add(f"Slayer of {r['boss']}", f"Defeat the {r['boss']}.", "boss",
            f"killed_boss.{r['id']}", {"drop_mult": 1.02}, points=25)
        add(f"World Bane: {r['world_boss']}", f"Defeat the world boss {r['world_boss']}.",
            "world_boss", f"killed_world_boss.{r['id']}", {"all_gain_mult": 1.02}, points=30)
        add(f"Flawless: {r['name']}", f"Clear an {r['name']} dungeon without taking damage.",
            "dungeon", f"flawless_clear.{r['id']}", {"def_mult": 1.03}, points=30)
        add(f"Speedrun: {r['name']}", f"Clear an {r['name']} dungeon in record time.",
            "dungeon", f"speed_clear.{r['id']}", {"spd_mult": 1.03}, points=30)

    # enemy kill counts
    for e in enemies:
        for n in (100, 1000, 10000, 100000, 1000000):
            add(f"{e['name']} Hunter {human(n)}", f"Defeat {human(n)} {e['name']}.",
                "slayer", f"kills.{e['id']} >= {n}", {"atk_mult": 1.005}, points=10)

    # crafting counts
    for n in [1, 10, 100, 1000, 10000]:
        add(f"Crafter {human(n)}", f"Craft {human(n)} items.", "crafting",
            f"items_crafted >= {n}", {"int_mult": 1.01}, points=10)
    for st in ["bench", "kitchen", "workshop", "forge", "lab", "foundry"]:
        add(f"Master of the {st.title()}", f"Craft 100 items at the {st}.", "crafting",
            f"crafted_at.{st} >= 100", {"craft_speed_mult": 1.05}, points=15)

    # recruitment + companions
    for n in [1, 3, 5, 10, 20, 50]:
        add(f"Leader of {n}", f"Have {n} recruited companions at once.", "recruitment",
            f"recruited_count >= {n}", {"ldr_mult": 1.02}, points=15)
    for c in recruitable:
        add(f"Bond: {c['name']}", f"Recruit {c['name']}.", "recruitment",
            f"recruited.{c['id']}", {"cha_mult": 1.01}, points=15)

    # death / loss
    for n in [1, 10, 100]:
        add(f"Mourner {human(n)}", f"Lose {human(n)} villagers/companions to death.",
            "loss", f"deaths >= {n}", {"vit_mult": 1.01}, points=10)

    # rebirth
    for n in [1, 2, 3, 5, 10, 25, 50, 100]:
        add(f"Reborn x{n}", f"Rebirth {n} time(s).", "rebirth",
            f"rebirth_count >= {n}", {"all_gain_mult": 1.05}, points=25)

    # collection / rarity
    for rar in rarities:
        add(f"Collector: {rar.title()}", f"Own an item of {rar} rarity.", "collection",
            f"owns_rarity.{rar}", {"lck_mult": 1.01}, points=15)
        add(f"Hoarder: {rar.title()}", f"Own 50 items of {rar} rarity.", "collection",
            f"owns_rarity_count.{rar} >= 50", {"lck_mult": 1.02}, points=20)

    # survival
    for need in ["food", "water", "warmth", "health", "morale"]:
        add(f"Provider: {need.title()}", f"Keep {need} maxed for a full day.", "survival",
            f"need_maxed_days.{need} >= 1", {"survival_mult": 1.02}, points=10)
        add(f"Self-Sufficient: {need.title()}", f"Fully automate {need} via delegation.",
            "survival", f"need_automated.{need}", {"survival_mult": 1.03}, points=15)

    # ---- HIDDEN achievements
    hidden_named = [
        ("The Hermit's Student", "Train with the Hermit of the Peak.", "trained_with.CHR-NPC-028"),
        ("Never Forgotten", "Witness the Echo of Ashfall.", "met.CHR-NPC-029"),
        ("Two Words from a Dead King", "Meet the Ashen Pilgrim both times.", "met_twice.CHR-MQ-004"),
        ("Stared Into the Void", "Survive the Voidless One's audience.", "survived.CHR-NPC-030"),
        ("Unwrite the Unwritten", "Defeat the final world boss, The Unwritten.", "killed_world_boss.HGOD"),
        ("Author of Worlds", "Become the Universe Overlord.", "phase_index >= 45"),
        ("Idle Emperor", "Earn a Gold while fully idle/offline.", "idle_currency.gold >= 1"),
        ("Pacifist's Paradox", "Reach phase 5 without losing a single villager.", "phase_index >= 5 AND deaths == 0"),
        ("Glass Cannon", "Have ATK 100x your DEF.", "stat.atk >= 100 * stat.def"),
        ("One With the Pen", "Rebirth after becoming Universe Overlord.", "rebirth_count >= 1 AND max_phase >= 45"),
    ]
    for i in range(130):
        if i < len(hidden_named):
            nm, desc, cond = hidden_named[i]
        else:
            nm = f"Secret: {random.choice(['Whisper','Glimmer','Shadow','Spark','Omen','Relic'])} of the {random.choice(['Deep','Stars','Void','Hollow','Crown','Dawn'])}"
            desc = "A hidden achievement unlocked by a secret condition."
            cond = f"secret_flag.ach.{i}"
        add(nm, desc, "secret", cond, {"all_gain_mult": 1.03,
            "loot_rarity_max": random.choice(["mythic", "ascendant", "divine", "primordial"])},
            points=50, hidden=True)

    out = {"collection": "achievements", "count": len(achs),
           "hidden_count": sum(1 for a in achs if a["hidden"]),
           "by_category": _counts(achs, "category"), "achievements": achs}
    os.makedirs(os.path.join(D, "achievements"), exist_ok=True)
    with open(os.path.join(D, "achievements", "achievements.json"), "w") as f:
        json.dump(out, f, indent=1)
    print(f"achievements.json: {len(achs)} achievements ({out['hidden_count']} hidden)")
    print("by category:", out["by_category"])
    assert len(achs) >= 500, "need at least 500 achievements"


def _counts(items, key):
    out = {}
    for it in items:
        out[it[key]] = out.get(it[key], 0) + 1
    return out


if __name__ == "__main__":
    main()
