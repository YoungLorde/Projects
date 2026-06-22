# Your Chronicle — Game Assets

Asset database for **Your Chronicle**, a click-based idle/incremental RPG.

The world runs on the written word: the player wields a living book (*the
Chronicle*) that turns deeds (clicks) into power. Clicks earn **Ink** (active
currency), Ink accrues into **Lore** (idle/offline currency), and **Main Quests**
from key NPCs move the story between **Chapters**. See
[`data/world_lore.yaml`](data/world_lore.yaml) for the full setting.

## What's in here

| Asset | Count | Source file(s) |
| --- | --- | --- |
| Key Main-Quest givers | 10 | [`data/characters/main_quest_givers.yaml`](data/characters/main_quest_givers.yaml) |
| Support NPCs (vendors, dungeon, service) | 15 | [`data/characters/npcs.yaml`](data/characters/npcs.yaml) |
| Shops | 9 | [`data/shops/shops.yaml`](data/shops/shops.yaml) |
| Weapons | 60 | [`data/shops/weapons.yaml`](data/shops/weapons.yaml) |
| Potions | 55 | [`data/shops/potions.yaml`](data/shops/potions.yaml) |
| Crafting materials | 60 | [`data/shops/materials.yaml`](data/shops/materials.yaml) |

**Total: 25 NPCs + 175 shop items.** The YAML files under `data/` are the source
of truth; `your_chronicle.db` (SQLite) is generated from them.

## Character categorization (partitions)

Every NPC is partitioned by **persistence** — how long they stay relevant as the
player progresses:

| Persistence | Meaning | Example |
| --- | --- | --- |
| `anchor` | Present essentially the whole game | The Chronicler |
| `recurring` | Appears across multiple chapters | Master Selwyn Quill |
| `milestone` | Appears only at major progression gates | Herald Aldous Penmark |
| `transient` | Appears once or twice, then gone | The Stranger in the Margins |
| `seasonal` | Limited-time / event windows only | Madame Coquette Rill |

NPCs are also categorized by **role_category** (`quest_giver`, `trainer`,
`vendor`, `dungeon`, `service`, `faction`, `lore`) and **importance** (`key`,
`major`, `minor`). The `transient_characters` SQL view returns every NPC that
appears once or twice then disappears.

## Building the database

```bash
pip install pyyaml          # one-time
python build_database.py --stats
```

This drops and rebuilds `your_chronicle.db` from the YAML sources and prints a
summary. The schema lives in [`schema.sql`](schema.sql) and includes tables for
`characters`, `character_quests`, `shops`, `items`, the category lookup tables,
and helper views (`transient_characters`, `vendor_overview`).

## Adding a new character

Every new character goes into the database via `add_character.py`, which appends
it to the right YAML file and rebuilds the DB:

```bash
python add_character.py \
    --id CHR-NPC-016 --name "Garrick the Gravedigger" \
    --role "Cemetery Vendor" --role-category vendor \
    --persistence recurring --importance minor \
    --chapters 4 5 6 \
    --backstory "Sells grave goods recovered from the Margins."
```

The script validates the categorization values (persistence / role / importance /
collection) so the partitions stay clean.

## Example queries

```sql
-- All main-quest givers and how long they stick around
SELECT name, role, persistence, appears_in_chapters
FROM characters WHERE gives_main_quest = 1;

-- NPCs that appear once or twice then disappear
SELECT * FROM transient_characters;

-- Each vendor, their shop, and catalog size
SELECT * FROM vendor_overview;

-- The 50+ weapons, cheapest first
SELECT name, tier, rarity, cost, currency, effect
FROM items WHERE shop_type = 'weapons' ORDER BY cost;
```
