#!/usr/bin/env python3
"""Generate the quest catalog (>= 500) for Your Chronicle -> data/quests/quests.json.

Quests are tied to real game data (phases, NPCs, dungeon ranks, enemies, materials)
so each has a sensible giver, objective, unlock condition, and rewards. Types:
  main | building | dungeon | gathering | crafting | recruitment |
  bounty (repeatable) | survival | hidden

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


def load(*parts):
    with open(os.path.join(D, *parts)) as f:
        return yaml.safe_load(f)


def main():
    random.seed(13371337)
    phases = load("systems", "phases.yaml")["phases"]
    buildings = load("systems", "buildings.yaml")["dwelling_upgrade_path"]
    dungeons = load("systems", "dungeons.yaml")["ranks"]
    enemies = load("enemies", "enemies.yaml")["enemy_types"]
    mqg = load("characters", "main_quest_givers.yaml")["characters"]
    npcs = load("characters", "npcs.yaml")["characters"]
    all_chars = mqg + npcs
    recruitable = [c for c in all_chars if c.get("recruitable")]
    givers = [c["id"] for c in all_chars if c.get("role_category") in
              ("quest_giver", "service", "dungeon", "faction", "trainer")] or [c["id"] for c in all_chars]

    quests = []
    qid = 1

    def add(name, qtype, giver, objective, condition, rewards,
            phase=None, repeatable=False, hidden=False):
        nonlocal qid
        quests.append({
            "id": f"Q-{qid:04d}",
            "name": name,
            "type": qtype,
            "giver": giver,
            "phase": phase,
            "objective": objective,
            "unlock_condition": condition,
            "rewards": rewards,
            "repeatable": repeatable,
            "hidden": hidden,
        })
        qid += 1

    # ---- MAIN: from quest-givers' authored quests
    for c in mqg + [n for n in npcs if n.get("role_category") in ("service", "dungeon")]:
        for q in c.get("quests_given", []) or []:
            title = q.split(" — ")[0]
            add(title, "main", c["id"], q,
                f"phase_index >= {min(c.get('appears_in_chapters', [1])[0]*2, 45)}",
                {"xp": 500, "currency": {"silver": 5}}, phase=None)

    # ---- MAIN: two per phase (advance + consolidate)
    for p in phases:
        add(f"Reach {p['name']}", "main", "CHR-MQ-010", f"Advance to the {p['name']} phase: {p['req']}",
            f"phase_index >= {p['index']-1}",
            {"xp": int(200*(1.6**p['index'])), "currency": {"gold": p['index']}, "unlocks": p['unlocks']},
            phase=p['index'])
        add(f"Consolidate {p['name']}", "main", "CHR-MQ-002",
            f"Stabilize your {p['name']} (meet survival needs and fill housing).",
            f"phase_index >= {p['index']}",
            {"xp": int(150*(1.6**p['index'])), "currency": {"gold": max(1, p['index']//2)}}, phase=p['index'])

    # ---- BUILDING upgrades
    for b in buildings:
        if b.get("upgrade_to"):
            add(f"Build: {b['name']} -> next tier", "building", "CHR-NPC-016" if False else "CHR-MQ-002",
                f"Gather materials and upgrade {b['name']} (capacity {b['pop_capacity']}).",
                f"building.{b['id']}.tier >= 1",
                {"xp": 100*(b['tier']+1), "pop_capacity": b['pop_capacity']})

    # ---- DUNGEON quests per rank
    for r in dungeons:
        add(f"Clear an {r['name']} Delve", "dungeon", "CHR-NPC-009",
            f"Clear any {r['name']} dungeon (levels {r['level_band']}).",
            f"phase_index >= {r['unlock_phase']}",
            {"xp": 1000*(r['index']+1), "loot_rarity_max": r['max_rarity']}, phase=r['unlock_phase'])
        add(f"Slay the {r['boss']}", "dungeon", "CHR-NPC-009",
            f"Defeat the {r['name']} boss: {r['boss']}.",
            f"dungeon_rank_cleared >= {r['index']}",
            {"xp": 2500*(r['index']+1), "permanent_boost_chance": 0.25}, phase=r['unlock_phase'])
        add(f"Hunt the {r['world_boss']}", "dungeon", "CHR-NPC-012",
            f"Defeat the {r['name']}-band world boss: {r['world_boss']}.",
            f"dungeon_rank_cleared >= {r['index']}",
            {"xp": 4000*(r['index']+1), "loot_rarity_max": r['max_rarity']}, phase=r['unlock_phase'], repeatable=True)

    # ---- GATHERING quests across material categories & tiers
    cats = ["wood", "stone", "ore", "hide", "cloth", "gem", "crystal", "essence",
            "reagent", "fuel", "food", "ingot", "thread", "leather", "monster_part",
            "component", "currency_mat", "plank"]
    for cat in cats:
        for tier in range(0, 10):
            qty = 25 * (tier + 1)
            add(f"Gather {qty} tier-{tier} {cat.replace('_',' ')}", "gathering",
                random.choice(["CHR-NPC-005", "CHR-NPC-006", "CHR-NPC-022", "CHR-NPC-023"]),
                f"Collect {qty} tier-{tier} {cat.replace('_',' ')} materials.",
                f"phase_index >= {max(1, tier)}",
                {"xp": 80*(tier+1), "currency": {"bronze": qty*10}}, repeatable=True)

    # ---- CRAFTING quests
    stations = ["bench", "kitchen", "workshop", "forge", "lab", "foundry"]
    craft_targets = ["a weapon", "a piece of armor", "a potion", "a building component",
                     "an alloy", "an exotic consumable", "a key", "a tool"]
    for st in stations:
        for tgt in craft_targets:
            add(f"Craft {tgt} at the {st}", "crafting", "CHR-MQ-003",
                f"Use the {st} to craft {tgt}.",
                f"has_station.{st}",
                {"xp": 120, "currency": {"silver": 1}}, repeatable=True)

    # ---- RECRUITMENT quests per recruitable NPC
    for c in recruitable:
        add(f"Recruit {c['name']}", "recruitment", c["id"],
            f"Earn the trust of {c['name']} ({c['role']}) and recruit them.",
            f"stat.cha >= {10 + RAR_IDX(c.get('rarity','common'))*15}",
            {"xp": 600, "recruit": c["id"]})

    # ---- BOUNTY (repeatable) per enemy type
    for e in enemies:
        for n in (10, 100, 1000):
            add(f"Bounty: slay {n} {e['name']}", "bounty", "CHR-NPC-012",
                f"Defeat {n} {e['name']} ({e['family']}).",
                f"phase_index >= 4",
                {"xp": e['base_xp']*n, "currency": {"bronze": e['base_xp']*n*5}, "reputation": n//10},
                repeatable=True)

    # ---- SURVIVAL quests
    for need in ["food", "water", "warmth", "health", "morale"]:
        for lvl in range(3):
            add(f"Secure {need} supply ({lvl+1})", "survival", "CHR-NPC-018" if need in ("health",) else "CHR-NPC-022",
                f"Raise and sustain the settlement's {need} to a healthy level.",
                f"phase_index >= 3",
                {"xp": 150*(lvl+1), "survival_cap_up": need}, repeatable=(lvl == 0))

    # ---- HIDDEN quests
    hidden_specs = [
        ("The Hermit's Trial", "Find the Hermit of the Peak and pass his test.", "achievement.secret_climber", {"permanent_boost": "random"}),
        ("Echoes of Ashfall", "Lay the Echo of Ashfall to rest.", "phase_index >= 2 AND visited.ashfall_ruins", {"codex": "ashfall"}),
        ("The Voidless Whisper", "Survive a whispered audience with the Voidless One.", "phase_index >= 44", {"xp": 1000000}),
        ("The Author's Secret", "Discover what Aeon really is.", "rebirth_count >= 3", {"codex": "aeon"}),
        ("A Coin Older Than Coins", "Refine your first Mythril Coin.", "has_item.mythril_coin", {"title": "Mythwright"}),
        ("The Pilgrim's Gift", "Receive the Ashen Pilgrim's relic both times he appears.", "quest_done.Q-0004", {"relic": "pilgrim"}),
    ]
    for i in range(40):
        if i < len(hidden_specs):
            nm, obj, cond, rew = hidden_specs[i]
        else:
            nm = f"Hidden: Secret of the {random.choice(['Deep','Star','Void','Crown','Hollow','Lost'])} {random.choice(['Vault','Shrine','Tomb','Garden','Archive','Gate'])}"
            obj = "Fulfill a hidden condition to reveal this secret quest."
            cond = f"secret_flag.{i}"
            rew = {"xp": 50000, "loot_rarity_max": random.choice(["mythic", "ascendant", "divine"])}
        add(nm, "hidden", random.choice(givers), obj, cond, rew, hidden=True)

    out = {"collection": "quests", "count": len(quests),
           "by_type": _counts(quests, "type"), "quests": quests}
    os.makedirs(os.path.join(D, "quests"), exist_ok=True)
    with open(os.path.join(D, "quests", "quests.json"), "w") as f:
        json.dump(out, f, indent=1)
    print(f"quests.json: {len(quests)} quests")
    print("by type:", out["by_type"])
    assert len(quests) >= 500, "need at least 500 quests"


_RAR = ["common", "uncommon", "rare", "epic", "legendary", "mythic",
        "ascendant", "transcendent", "divine", "primordial"]


def RAR_IDX(r):
    return _RAR.index(r) if r in _RAR else 0


def _counts(items, key):
    out = {}
    for it in items:
        out[it[key]] = out.get(it[key], 0) + 1
    return out


if __name__ == "__main__":
    main()
