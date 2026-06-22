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

-- Rarity scale shared by characters, items, materials, and enemies.
CREATE TABLE IF NOT EXISTS rarity_category (
    id             TEXT PRIMARY KEY,
    name           TEXT NOT NULL,
    rank           INTEGER NOT NULL,
    color          TEXT,
    drop_weight    REAL,
    value_mult     REAL,
    stat_roll_mult REAL,
    description    TEXT
);

-- Tiered, auto-converting currency chain (Bronze -> Mythril).
CREATE TABLE IF NOT EXISTS currency_tier (
    id              TEXT PRIMARY KEY,
    name            TEXT NOT NULL,
    tier            INTEGER NOT NULL,
    per_next        INTEGER,            -- amount that converts into 1 of `next`
    next_id         TEXT,               -- next currency up the chain
    value_in_bronze REAL,              -- absolute value of 1 unit in Bronze
    description     TEXT
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
    shop_type               TEXT,
    rarity                  TEXT REFERENCES rarity_category(id),
    recruitable             INTEGER NOT NULL DEFAULT 0,  -- boolean (0/1)
    can_level               INTEGER NOT NULL DEFAULT 0,  -- boolean (0/1)
    can_die                 INTEGER NOT NULL DEFAULT 0,  -- boolean (0/1)
    archetype               TEXT,
    base_stats              TEXT                    -- JSON object of stat -> value
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

-- ---------------------------------------------------------------------------
-- Progression & world data
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS phases (
    idx         INTEGER PRIMARY KEY,     -- phase index 1..45
    id          TEXT UNIQUE NOT NULL,
    name        TEXT NOT NULL,
    band        TEXT,
    req         TEXT,
    unlocks     TEXT
);

CREATE TABLE IF NOT EXISTS buildings (
    id            TEXT PRIMARY KEY,
    name          TEXT NOT NULL,
    tier          INTEGER,
    pop_capacity  INTEGER,
    upgrade_to    TEXT,
    unlocks       TEXT                    -- JSON array
);

CREATE TABLE IF NOT EXISTS dungeons (
    idx          INTEGER PRIMARY KEY,
    id           TEXT UNIQUE NOT NULL,
    name         TEXT NOT NULL,
    level_band   TEXT,
    unlock_phase INTEGER,
    max_rarity   TEXT REFERENCES rarity_category(id),
    boss         TEXT,
    world_boss   TEXT
);

CREATE TABLE IF NOT EXISTS enemies (
    id          TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    family      TEXT,
    base_hp     INTEGER,
    base_atk    INTEGER,
    base_xp     INTEGER,
    rank_band   TEXT,
    traits      TEXT,                     -- JSON array
    drop_theme  TEXT,
    kind        TEXT                      -- enemy | boss | world_boss
);

CREATE TABLE IF NOT EXISTS animals (
    id          TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    type        TEXT,
    habitat     TEXT,
    tameable    INTEGER NOT NULL DEFAULT 0,
    yields      TEXT,
    role        TEXT
);

-- Materials catalog (base + exotic), each tagged with reasons for existing.
CREATE TABLE IF NOT EXISTS materials (
    id          TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    category    TEXT,                     -- base | exotic
    subtype     TEXT,
    tier        INTEGER,
    rarity      TEXT REFERENCES rarity_category(id),
    cost        INTEGER,
    currency    TEXT,
    reasons     TEXT,                     -- JSON array of reason tags
    source      TEXT,
    use_note    TEXT,
    description TEXT,
    perm_stat   TEXT,                     -- for permanent_stat_boost mats
    perm_gain   INTEGER
);

CREATE TABLE IF NOT EXISTS quests (
    id               TEXT PRIMARY KEY,
    name             TEXT NOT NULL,
    type             TEXT,
    giver            TEXT,                -- character id
    phase            INTEGER,
    objective        TEXT,
    unlock_condition TEXT,
    rewards          TEXT,                -- JSON
    repeatable       INTEGER NOT NULL DEFAULT 0,
    hidden           INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS achievements (
    id          TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    description TEXT,
    category    TEXT,
    condition   TEXT,
    reward      TEXT,                     -- JSON
    points      INTEGER,
    hidden      INTEGER NOT NULL DEFAULT 0
);

-- ---------------------------------------------------------------------------
-- Additional helpful views
-- ---------------------------------------------------------------------------

-- Recruitable companions (can be added to the player's party / delegated to jobs).
CREATE VIEW IF NOT EXISTS recruitable_companions AS
    SELECT id, name, role, role_category, rarity, archetype, base_stats
    FROM characters WHERE recruitable = 1;

-- Mortal NPCs (those who can permanently die).
CREATE VIEW IF NOT EXISTS mortal_npcs AS
    SELECT id, name, role, rarity, persistence FROM characters WHERE can_die = 1;

-- All hidden content (secret quests + achievements) in one place.
CREATE VIEW IF NOT EXISTS hidden_content AS
    SELECT id, name, 'quest' AS kind, unlock_condition AS condition FROM quests WHERE hidden = 1
    UNION ALL
    SELECT id, name, 'achievement' AS kind, condition FROM achievements WHERE hidden = 1;

-- Permanent stat-boost materials.
CREATE VIEW IF NOT EXISTS permanent_boost_materials AS
    SELECT id, name, rarity, perm_stat, perm_gain, source
    FROM materials WHERE reasons LIKE '%permanent_stat_boost%';
