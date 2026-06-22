-- Your Chronicle — game asset database schema
-- A click-based idle/incremental RPG. This schema stores NPCs (with partitions
-- and categorizations), shops, and shop item catalogs.

PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------------------
-- Reference / lookup tables (the "partitions" and "categorizations")
-- ---------------------------------------------------------------------------

-- Persistence: how long an NPC stays relevant as the player progresses.
-- (anchor, recurring, milestone, transient, seasonal)
CREATE TABLE IF NOT EXISTS persistence_category (
    id          TEXT PRIMARY KEY,
    description TEXT NOT NULL
);

-- Functional role of the NPC in the game's systems.
-- (quest_giver, trainer, vendor, dungeon, service, faction, lore)
CREATE TABLE IF NOT EXISTS role_category (
    id          TEXT PRIMARY KEY,
    description TEXT NOT NULL
);

-- Narrative weight (key, major, minor).
CREATE TABLE IF NOT EXISTS importance_category (
    id          TEXT PRIMARY KEY,
    description TEXT NOT NULL
);

-- ---------------------------------------------------------------------------
-- Characters / NPCs
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS characters (
    id                      TEXT PRIMARY KEY,
    name                    TEXT NOT NULL,
    title                   TEXT,
    role                    TEXT,
    collection              TEXT NOT NULL,          -- main_quest_givers | support_npcs
    role_category           TEXT REFERENCES role_category(id),
    persistence             TEXT REFERENCES persistence_category(id),
    importance              TEXT REFERENCES importance_category(id),
    faction                 TEXT,
    home_location           TEXT,
    gives_main_quest        INTEGER NOT NULL DEFAULT 0,  -- boolean (0/1)
    appears_in_chapters     TEXT,                   -- JSON array, e.g. "[1, 2, 3]"
    first_appearance_chapter INTEGER,
    last_appearance_chapter  INTEGER,
    appearance_count        INTEGER,                -- number of chapters the NPC appears in
    unlock_condition        TEXT,
    personality             TEXT,
    voice_sample            TEXT,
    appearance              TEXT,
    backstory               TEXT,
    lore_notes              TEXT,
    rewards_theme           TEXT,
    shop_id                 TEXT,                   -- set for vendor NPCs
    shop_type               TEXT
);

-- Main quests handed out by quest-giver NPCs (one row per quest).
CREATE TABLE IF NOT EXISTS character_quests (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    character_id TEXT NOT NULL REFERENCES characters(id) ON DELETE CASCADE,
    quest        TEXT NOT NULL
);

-- ---------------------------------------------------------------------------
-- Shops & items
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS shops (
    id          TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    shop_type   TEXT NOT NULL,
    vendor_id   TEXT REFERENCES characters(id),
    tier_range  TEXT,
    location    TEXT,
    currency    TEXT,
    description TEXT
);

CREATE TABLE IF NOT EXISTS items (
    id          TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    shop_type   TEXT NOT NULL,          -- weapons | potions | materials | ...
    subtype     TEXT,
    tier        INTEGER,
    rarity      TEXT,
    cost        INTEGER,
    currency    TEXT,
    click_power INTEGER,                -- weapons: active contribution
    idle_power  INTEGER,                -- weapons: passive contribution
    duration    INTEGER,               -- potions: seconds (0 = instant)
    effect      TEXT,
    use_note    TEXT,                  -- materials: what it feeds into
    description TEXT
);

-- ---------------------------------------------------------------------------
-- Helpful views
-- ---------------------------------------------------------------------------

-- Transient NPCs: those that appear once or twice then disappear.
CREATE VIEW IF NOT EXISTS transient_characters AS
    SELECT id, name, role, persistence, appearance_count, appears_in_chapters
    FROM characters
    WHERE persistence IN ('transient', 'seasonal') OR appearance_count <= 2;

-- Vendors joined to their shop and item counts.
CREATE VIEW IF NOT EXISTS vendor_overview AS
    SELECT c.id AS vendor_id, c.name AS vendor_name, s.id AS shop_id,
           s.name AS shop_name, s.shop_type,
           (SELECT COUNT(*) FROM items i WHERE i.shop_type = s.shop_type) AS catalog_size
    FROM characters c
    JOIN shops s ON s.vendor_id = c.id;
