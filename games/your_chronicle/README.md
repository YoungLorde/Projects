# Your Chronicle — Game Assets

A complete asset & systems package for **Your Chronicle**, a deeply grindy
click-based **idle/incremental RPG** with survival, base-building, recruitment,
dungeons, and a cultivation-style ascension all the way from a lone survivor in a
derelict **Wooden Shack** to **Universe Overlord**.

The world is **Orden**, recovering from a cataclysm (the *Unwriting*) caused by
the **Void**. You gather, survive, repair your shack, take in villagers, grow a
village → town → city → kingdom → empire → planetary → cosmic civilization, and
ultimately rule the universe — then **rebirth** for compounding multipliers and
climb again. Full story: [`data/lore/world_history.md`](data/lore/world_history.md).
Setting overview: [`data/world_lore.yaml`](data/world_lore.yaml).

## What's in here

### Core systems (hand-authored specs under `data/systems/`)
| System | File | Summary |
| --- | --- | --- |
| Currency | [`currency.yaml`](data/systems/currency.yaml) | 7-tier **auto-converting** chain: Bronze→Silver→Gold→Zenu Stone→Zenu Coin→Mythril Ore→Mythril Coin |
| Rarity | [`rarity.yaml`](data/systems/rarity.yaml) | 10 tiers, Common → Primordial (drop weight / value / stat-roll mult) |
| Stats | [`stats.yaml`](data/systems/stats.yaml) | **No level cap**, population-driven leveling, **additive-from-inventory** gear, permanent stat-boost mats |
| Phases | [`phases.yaml`](data/systems/phases.yaml) | **45 progression phases** in 7 bands, shack → Universe Overlord |
| Buildings | [`buildings.yaml`](data/systems/buildings.yaml) | Dwelling upgrade tree, settlements, **14 jobs**, villager stats, NPC lifecycle (recruit/level/die) |
| Rebirth | [`rebirth.yaml`](data/systems/rebirth.yaml) | Prestige reset → compounding multipliers + Ascension Essence/tree |
| Survival | [`survival.yaml`](data/systems/survival.yaml) | Food/Water/Warmth/Health/Morale as a global output multiplier |
| Crafting | [`crafting.yaml`](data/systems/crafting.yaml) | Gather → refine → craft; every material has a reason |
| Dungeons | [`dungeons.yaml`](data/systems/dungeons.yaml) | **18 ranks** F → Heavenly God with scaling enemies/XP/drops |
| UI framework | [`ui_framework.yaml`](data/systems/ui_framework.yaml) | Data-driven, **condition-gated**, collapsible-panel UI |

### Content
| Asset | Count | Source |
| --- | --- | --- |
| Main-Quest givers | 10 | [`data/characters/main_quest_givers.yaml`](data/characters/main_quest_givers.yaml) |
| Support NPCs | 30 | [`data/characters/npcs.yaml`](data/characters/npcs.yaml) |
| Enemy types | 24 | [`data/enemies/enemies.yaml`](data/enemies/enemies.yaml) (+ dungeon bosses & world bosses) |
| Animals | 24 | [`data/animals/animals.yaml`](data/animals/animals.yaml) |
| Phases | 45 | [`data/systems/phases.yaml`](data/systems/phases.yaml) |
| Dungeon ranks | 18 | [`data/systems/dungeons.yaml`](data/systems/dungeons.yaml) |
| Shop items (weapons/potions/materials) | 175 | [`data/shops/`](data/shops/) |
| **Base materials** | **540** | [`data/materials/materials.json`](data/materials/materials.json) (generated) |
| **Exotic materials** | **500** | [`data/materials/exotic_materials.json`](data/materials/exotic_materials.json) (generated) |
| **Quests** (incl. 40 hidden) | **563** | [`data/quests/quests.json`](data/quests/quests.json) (generated) |
| **Achievements** (incl. 130 hidden) | **516** | [`data/achievements/achievements.json`](data/achievements/achievements.json) (generated) |

Every material is tagged with at least one **reason** for existing:
`crafting_recipe`, `building_component`, `quest_item`, `weapon_unlock`,
`consumable_boost`, `permanent_stat_boost`, or `currency_refine`.

Hand-authored YAML and the generators under `generators/` are the source of
truth; `your_chronicle.db` (SQLite) is built from them.

## Character categorization (partitions)

Every NPC is partitioned by **persistence** (how long they stay relevant),
**role_category** (`quest_giver`/`trainer`/`vendor`/`dungeon`/`service`/`faction`/`lore`),
**importance**, and now also **rarity**, plus flags for **recruitable**,
**can_level**, and **can_die** (with a `base_stats` archetype block).

| Persistence | Meaning | Example |
| --- | --- | --- |
| `anchor` | Whole game | Aeon, the World-Scribe |
| `recurring` | Many phases | Garrok Emberhand |
| `milestone` | Major gates only | Envoy Castellan Reyes |
| `transient` | Once/twice then gone (and gone after rebirth) | The Ashen Pilgrim |
| `seasonal` | Event windows only | Madame Coralind Vex |

Helper views: `transient_characters`, `recruitable_companions`, `mortal_npcs`,
`hidden_content`, `permanent_boost_materials`, `vendor_overview`.

## Building everything

```bash
pip install pyyaml                  # one-time
python build_all.py --stats        # run generators -> build DB -> export UI snapshot
```

`build_all.py` runs the content generators, rebuilds `your_chronicle.db` from all
sources (schema in [`schema.sql`](schema.sql)), and writes `ui/game_data.json`.
You can also run the steps individually (`generators/gen_*.py`,
`build_database.py --stats`, `generators/export_ui_data.py`).

## UI prototype

A data-driven, condition-gated UI prototype lives in [`ui/`](ui/). It reads
`ui/game_data.json` (exported from the DB) and demonstrates collapsible panels,
features/buttons that unlock when their conditions are met (and hidden secrets
that don't render at all), an inventory with category dropdowns, and the
**additive-from-inventory** equipment stats. Serve it over HTTP:

```bash
cd ui && python -m http.server 8000   # then open http://localhost:8000
```

Drag the **Dev / Demo Controls** sliders (phase, population, rebirths, dungeon
rank) to watch panels and buttons unlock live.

## Adding a new character

```bash
python add_character.py \
    --id CHR-NPC-031 --name "Some Name" \
    --role "Cemetery Vendor" --role-category vendor \
    --persistence recurring --importance minor --chapters 4 5 6 \
    --backstory "..."
```

The script validates categorization values, appends to the right YAML, and
rebuilds the DB.

## Example queries

```sql
SELECT name, role, rarity, persistence FROM mortal_npcs;          -- NPCs that can die
SELECT * FROM recruitable_companions;                              -- recruitable party members
SELECT name, perm_stat, perm_gain FROM permanent_boost_materials; -- permanent stat boosts
SELECT type, COUNT(*) FROM quests GROUP BY type;                  -- quest breakdown
SELECT name, reasons FROM materials WHERE category='exotic' LIMIT 20;
SELECT * FROM hidden_content;                                     -- secret quests + achievements
```

## Local copy

This whole folder is portable. To keep a local copy on Windows at
`C:\Users\YoungLorde\GameZ\Riser`, either `git clone` the repo there or extract
the packaged `your_chronicle.zip` attached in the session.
