#!/usr/bin/env python3
"""Generate the bulk material catalogs for Your Chronicle.

Produces two reason-tagged JSON catalogs:
  data/materials/materials.json         (>= 500 base crafting materials)
  data/materials/exotic_materials.json  (>= 500 exotic materials)

Every material is tagged with at least one 'reason' so nothing is filler:
  crafting_recipe | building_component | quest_item | weapon_unlock |
  consumable_boost | permanent_stat_boost | currency_refine

Deterministic (seeded) so output is reproducible and diff-friendly.
"""
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT_DIR = os.path.join(ROOT, "data", "materials")

RARITIES = ["common", "uncommon", "rare", "epic", "legendary",
            "mythic", "ascendant", "transcendent", "divine", "primordial"]
# currency a material refines into / is priced in, by tier band
CURRENCY_BY_TIER = ["bronze", "bronze", "silver", "silver", "gold",
                    "gold", "zenu_stone_gram", "zenu_coin", "mythril_ore_gram", "mythril_coin"]

# ---------------------------------------------------------------- base catalog
# category -> (subtype, tier-adjective list paired by tier, base noun, reasons)
BASE_CATEGORIES = {
    "ore":        ("ore",      "Ore",      ["building_component", "crafting_recipe"]),
    "ingot":      ("ingot",    "Ingot",    ["crafting_recipe", "building_component"]),
    "stone":      ("stone",    "Stone",    ["building_component", "crafting_recipe"]),
    "wood":       ("wood",     "Wood",     ["building_component", "crafting_recipe"]),
    "plank":      ("plank",    "Plank",    ["building_component", "crafting_recipe"]),
    "hide":       ("hide",     "Hide",     ["crafting_recipe"]),
    "leather":    ("leather",  "Leather",  ["crafting_recipe"]),
    "cloth":      ("cloth",    "Cloth",    ["crafting_recipe"]),
    "thread":     ("thread",   "Thread",   ["crafting_recipe"]),
    "gem":        ("gem",      "Gem",      ["weapon_unlock", "crafting_recipe"]),
    "crystal":    ("crystal",  "Crystal",  ["weapon_unlock", "crafting_recipe"]),
    "essence":    ("essence",  "Essence",  ["consumable_boost", "crafting_recipe"]),
    "reagent":    ("reagent",  "Reagent",  ["consumable_boost", "crafting_recipe"]),
    "monster_part": ("monster_part", "Part", ["crafting_recipe", "quest_item"]),
    "component":  ("component", "Component", ["crafting_recipe", "building_component"]),
    "food":       ("food",     "Ration",   ["consumable_boost"]),
    "fuel":       ("fuel",     "Fuel",     ["building_component", "consumable_boost"]),
    "currency_mat": ("currency_mat", "Bar", ["currency_refine"]),
}

# tier-adjective ramp (index 0..9)
TIER_ADJ = ["Crude", "Rough", "Common", "Fine", "Refined",
            "Pristine", "Radiant", "Ascendant", "Transcendent", "Primordial"]

# per-category base nouns to vary names within a tier
NOUNS = {
    "ore":        ["Iron", "Copper", "Tin", "Silverite", "Cobalt", "Mithral", "Adamant", "Voidsteel", "Starforged", "Aether"],
    "ingot":      ["Iron", "Bronze", "Steel", "Silverite", "Cobalt", "Mithral", "Adamant", "Voidsteel", "Starsteel", "Aetherium"],
    "stone":      ["Field", "River", "Granite", "Marble", "Basalt", "Obsidian", "Moon", "Star", "Void", "World"],
    "wood":       ["Pine", "Oak", "Birch", "Ash", "Ironbark", "Heartwood", "Silverleaf", "Sunwood", "Voidwood", "Worldtree"],
    "plank":      ["Pine", "Oak", "Birch", "Ash", "Ironbark", "Heartwood", "Silverleaf", "Sunwood", "Voidwood", "Worldtree"],
    "hide":       ["Rabbit", "Deer", "Boar", "Wolf", "Bear", "Drake", "Wyvern", "Dragon", "Behemoth", "Leviathan"],
    "leather":    ["Soft", "Cured", "Hardened", "Studded", "Reinforced", "Drakehide", "Wyrmskin", "Dragonhide", "Titanhide", "Voidhide"],
    "cloth":      ["Frayed", "Linen", "Wool", "Cotton", "Silk", "Spellsilk", "Moonweave", "Starcloth", "Voidweave", "Worldsilk"],
    "thread":     ["Plant", "Linen", "Wool", "Silk", "Spider", "Spellthread", "Moonthread", "Starthread", "Voidthread", "Fatethread"],
    "gem":        ["Quartz", "Amethyst", "Topaz", "Emerald", "Sapphire", "Ruby", "Diamond", "Starstone", "Voidgem", "Soulgem"],
    "crystal":    ["Dim", "Clear", "Bright", "Charged", "Resonant", "Arcane", "Astral", "Stellar", "Void", "Primal"],
    "essence":    ["Faint", "Lesser", "Vital", "Greater", "Potent", "Pure", "Radiant", "Astral", "Void", "Primordial"],
    "reagent":    ["Bloomroot", "Mossleaf", "Nightcap", "Sunpetal", "Frostbloom", "Dreamspore", "Starblossom", "Voidcap", "Soulroot", "Worldbloom"],
    "monster_part": ["Fang", "Claw", "Scale", "Horn", "Sinew", "Core", "Heartstone", "Soulmark", "Eye", "Crown"],
    "component":  ["Glue", "Whetstone", "Oil", "Catalyst", "Gear", "Circuit", "Alloy Plate", "Power Cell", "Nanopaste", "Quintessence"],
    "food":       ["Berries", "Bread", "Stew", "Roast", "Feast", "Elixir Meal", "Star Ration", "Void Ration", "Ambrosia", "Worldfeast"],
    "fuel":       ["Tinder", "Charcoal", "Coal", "Oil", "Gas", "Plasma Cell", "Fusion Rod", "Antimatter", "Void Fuel", "Starfire"],
    "currency_mat": ["Bronze", "Silver", "Gold", "Electrum", "Platinum", "Zenu Dust", "Zenu Stone", "Zenu Bar", "Mythril Dust", "Mythril"],
}

SOURCES = ["forest", "quarry", "mine", "river", "ruins", "dungeon", "farm",
           "hunting_ground", "space_field", "boss_drop", "vendor", "refining"]


def make_material(idx, category, tier, noun):
    subtype, suffix, reasons = BASE_CATEGORIES[category]
    rarity = RARITIES[min(tier, 9)]
    adj = TIER_ADJ[min(tier, 9)]
    name = f"{adj} {noun} {suffix}".replace("  ", " ").strip()
    currency = CURRENCY_BY_TIER[min(tier, 9)]
    base_cost = int(round((5 * (2.4 ** tier)) * random.uniform(0.8, 1.3)))
    # currency_mat at high tiers are refine inputs
    reasons = list(reasons)
    if category == "currency_mat" and tier >= 5:
        reasons = ["currency_refine"]
    use_note = {
        "building_component": "used to construct/upgrade buildings",
        "crafting_recipe": "ingredient in crafting recipes",
        "weapon_unlock": "socket/empower weapons and gear",
        "consumable_boost": "consumed for a temporary boost",
        "quest_item": "required by one or more quests",
        "currency_refine": "refines into higher-tier currency",
        "permanent_stat_boost": "permanently raises a stat pool",
    }[reasons[0]]
    return {
        "id": f"MAT-{idx:04d}",
        "name": name,
        "category": "base",
        "subtype": subtype,
        "tier": tier,
        "rarity": rarity,
        "cost": base_cost,
        "currency": currency,
        "reasons": reasons,
        "source": random.choice(SOURCES),
        "use_note": use_note,
        "description": f"A tier-{tier} {subtype.replace('_', ' ')} ({rarity}). "
                       f"{adj.lower()} grade {noun.lower()} {suffix.lower()}.",
    }


def gen_base():
    mats = []
    idx = 1
    for category in BASE_CATEGORIES:
        for tier in range(10):
            # 3 named variants per (category, tier) -> 18 cats *10 *3 = 540
            nouns = NOUNS[category]
            for v in range(3):
                noun = nouns[(tier + v) % len(nouns)]
                mats.append(make_material(idx, category, tier, noun))
                idx += 1
    return mats


# ------------------------------------------------------------- exotic catalog
EXOTIC_THEMES = [
    ("Phoenix", "consumable_boost"), ("Dragon", "weapon_unlock"), ("Void", "permanent_stat_boost"),
    ("Star", "weapon_unlock"), ("Soul", "permanent_stat_boost"), ("Time", "consumable_boost"),
    ("Abyssal", "weapon_unlock"), ("Celestial", "permanent_stat_boost"), ("Demon", "weapon_unlock"),
    ("Angel", "consumable_boost"), ("Titan", "permanent_stat_boost"), ("Frost", "weapon_unlock"),
    ("Storm", "weapon_unlock"), ("Blood", "consumable_boost"), ("Spirit", "permanent_stat_boost"),
    ("Chaos", "weapon_unlock"), ("Order", "permanent_stat_boost"), ("Dream", "consumable_boost"),
    ("Nightmare", "consumable_boost"), ("Eternal", "permanent_stat_boost"), ("Primal", "weapon_unlock"),
    ("Cosmic", "permanent_stat_boost"), ("Genesis", "quest_item"), ("Oblivion", "quest_item"),
    ("Astral", "weapon_unlock"),
]
EXOTIC_FORMS = ["Heart", "Core", "Shard", "Fragment", "Essence", "Crystal", "Bloom",
                "Tear", "Ember", "Sigil", "Relic", "Catalyst", "Mote", "Seed", "Dust",
                "Flame", "Feather", "Fang", "Eye", "Crown"]
STAT_TARGETS = ["hp", "atk", "def", "spd", "vit", "int", "lck", "cha", "ldr", "all"]


def make_exotic(idx, theme, form, tier):
    name_theme, reason = theme
    rarity = RARITIES[min(4 + tier // 2, 9)]   # exotics start at legendary-ish
    name = f"{name_theme} {form}"
    currency = CURRENCY_BY_TIER[min(5 + tier // 2, 9)]
    base_cost = int(round((50 * (3.0 ** tier)) * random.uniform(0.8, 1.3)))
    reasons = [reason, "crafting_recipe"]
    extra = {}
    if reason == "permanent_stat_boost":
        stat = random.choice(STAT_TARGETS)
        gain = int(round((5 + tier * 4) * random.uniform(0.8, 1.4)))
        extra = {"perm_stat": stat, "perm_gain": gain}
        use_note = f"permanently +{gain} {stat.upper()} when consumed"
    elif reason == "weapon_unlock":
        use_note = "unlocks/awakens a weapon's hidden power tier"
    elif reason == "consumable_boost":
        use_note = "powerful single-use exotic consumable"
    else:
        use_note = "required by a late-game exotic quest line"
    rec = {
        "id": f"MAT-EX-{idx:04d}",
        "name": name,
        "category": "exotic",
        "subtype": name_theme.lower(),
        "tier": tier,
        "rarity": rarity,
        "cost": base_cost,
        "currency": currency,
        "reasons": reasons,
        "source": random.choice(["boss_drop", "dungeon", "world_boss", "hidden_quest", "space_field", "rebirth_reward"]),
        "use_note": use_note,
        "description": f"An exotic {name_theme.lower()}-attuned {form.lower()} ({rarity}); {use_note}.",
    }
    rec.update(extra)
    return rec


def gen_exotic():
    mats = []
    idx = 1
    for theme in EXOTIC_THEMES:           # 25 themes
        for form in EXOTIC_FORMS:         # 20 forms -> 500
            tier = (idx % 10)
            mats.append(make_exotic(idx, theme, form, tier))
            idx += 1
    return mats


def main():
    random.seed(20240622)
    os.makedirs(OUT_DIR, exist_ok=True)
    base = gen_base()
    random.seed(99887766)
    exotic = gen_exotic()
    with open(os.path.join(OUT_DIR, "materials.json"), "w") as f:
        json.dump({"collection": "materials", "count": len(base), "materials": base}, f, indent=1)
    with open(os.path.join(OUT_DIR, "exotic_materials.json"), "w") as f:
        json.dump({"collection": "exotic_materials", "count": len(exotic), "materials": exotic}, f, indent=1)
    print(f"materials.json: {len(base)} base materials")
    print(f"exotic_materials.json: {len(exotic)} exotic materials")
    # reason coverage sanity
    for cat, data in (("base", base), ("exotic", exotic)):
        assert all(m["reasons"] for m in data), f"{cat}: a material has no reason!"
    print("OK: every material has at least one reason.")


if __name__ == "__main__":
    main()
