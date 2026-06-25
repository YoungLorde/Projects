"""
Vehicle Core Feeding System — Limitless upgrade mechanics for Soul Vehicles.

Inspired by "My Post-Apocalyptic Shelter Levels Up Infinitely!" where Su Mo
could infinitely upgrade his shelter. In RP Conversion, Travellers can "feed"
resources to their Vehicle Core to upgrade it beyond normal tier limits.

The feeding system provides:
  - Resource consumption for core growth
  - Tiered upgrade paths with escalating costs
  - Stat bonuses that scale with feeding level
  - Unlock conditions for new capabilities
  - Mohamed's dual-system bypass for accelerated feeding
"""

from typing import Optional


# ── Feeding Tier Definitions ────────────────────────────────────
# Each feeding tier represents a stage of core evolution.
# Costs scale exponentially. Normal Travellers hit a ceiling;
# Mohamed's RP Conversion system removes that ceiling.

FEEDING_TIERS = [
    {
        "tier": 0,
        "name": "Dormant Core",
        "description": (
            "The core is inert — it has not been fed. Standard Vehicle Core "
            "state for most Travellers. The core responds to System commands "
            "but has no enhanced growth potential."
        ),
        "rp_cost": 0,
        "resource_cost": "None",
        "stat_bonus": {},
        "unlocks": [],
        "feeding_count": 0,
    },
    {
        "tier": 1,
        "name": "Awakened Core",
        "description": (
            "First feeding accepted. The core pulses with faint internal light "
            "that wasn't there before. A hairline fracture pattern appears on "
            "the surface — not damage, but growth channels. The core is hungry."
        ),
        "rp_cost": 50_000,
        "resource_cost": "10 Monster Cores (any tier) OR 5 Dungeon Crystals",
        "stat_bonus": {"END": 1, "SYS": 1},
        "unlocks": ["Core Resonance Sense — detect nearby feedable resources"],
        "feeding_count": 1,
    },
    {
        "tier": 2,
        "name": "Growing Core",
        "description": (
            "The fracture channels glow with steady blue light. The core has "
            "developed an appetite — it pulls ambient System energy from the "
            "environment. Vehicle pocket dimension expands by 10%. Self-repair "
            "rate increases by 25%."
        ),
        "rp_cost": 500_000,
        "resource_cost": "50 Monster Cores (Tier 1+) OR 20 Dungeon Crystals OR 1 Rare Material",
        "stat_bonus": {"END": 2, "SYS": 2, "STR": 1},
        "unlocks": [
            "Ambient Energy Absorption — passive 5 RP/hour from environment",
            "Pocket Dimension +10% size",
        ],
        "feeding_count": 5,
    },
    {
        "tier": 3,
        "name": "Hungry Core",
        "description": (
            "The core's growth channels have branched into a complex web. It "
            "actively draws resources from the Traveller's kills — monster "
            "drops are partially absorbed before the Traveller can loot them. "
            "Vehicle hull begins showing crystalline reinforcement patterns."
        ),
        "rp_cost": 5_000_000,
        "resource_cost": (
            "200 Monster Cores (Tier 2+) OR 100 Dungeon Crystals "
            "OR 5 Rare Materials OR 1 Epic Material"
        ),
        "stat_bonus": {"END": 3, "SYS": 3, "STR": 2, "AGI": 1},
        "unlocks": [
            "Auto-Harvest — 10% of kill drops absorbed by core automatically",
            "Crystalline Hull — +15% armor from crystal growth",
            "Pocket Dimension +25% size",
        ],
        "feeding_count": 15,
    },
    {
        "tier": 4,
        "name": "Evolving Core",
        "description": (
            "The core has begun restructuring itself. Its crystalline matrix "
            "is more complex than any artificially manufactured core. The "
            "vehicle's systems respond faster. Internal upgrades operate at "
            "110% efficiency. The core hums at a frequency only the bonded "
            "Traveller can hear."
        ),
        "rp_cost": 50_000_000,
        "resource_cost": (
            "500 Monster Cores (Tier 3+) OR 1 Legendary Material "
            "OR 10 Epic Materials"
        ),
        "stat_bonus": {"END": 5, "SYS": 5, "STR": 3, "AGI": 2, "INT": 1},
        "unlocks": [
            "System Efficiency — all internal upgrades operate at 110%",
            "Core Communication — sense other fed cores within 5km",
            "Auto-Harvest increased to 20%",
            "Pocket Dimension +50% size",
        ],
        "feeding_count": 30,
    },
    {
        "tier": 5,
        "name": "Ravenous Core",
        "description": (
            "The core's appetite is insatiable. It can consume entire dungeon "
            "cores (destroying the dungeon) for massive growth. The vehicle's "
            "crystalline patterns are visible externally — other Travellers "
            "can see the core's influence on the hull. The System flags this "
            "as an anomaly but cannot classify it."
        ),
        "rp_cost": 500_000_000,
        "resource_cost": (
            "1 Dungeon Core (destroys dungeon) OR 5 Legendary Materials "
            "OR 50 Epic Materials OR 1 Ancient Race Artifact fragment"
        ),
        "stat_bonus": {"END": 8, "SYS": 8, "STR": 5, "AGI": 3, "INT": 2, "PER": 2},
        "unlocks": [
            "Dungeon Core Consumption — can eat dungeon cores for massive growth",
            "Anomaly Status — System cannot classify core; confuses scanners",
            "Auto-Harvest increased to 35%",
            "Pocket Dimension +100% size",
            "Vehicle Regeneration — 5% hull/hour (up from 1%)",
        ],
        "feeding_count": 50,
    },
    {
        "tier": 6,
        "name": "Sentient Core",
        "description": (
            "The core has developed a rudimentary awareness. Not intelligence "
            "— instinct. It guides the Traveller toward resources it wants, "
            "creates subtle vibrations when danger approaches, and refuses "
            "resources it deems 'beneath' it. The vehicle begins to feel alive."
        ),
        "rp_cost": 5_000_000_000,
        "resource_cost": (
            "5 Dungeon Cores OR 1 Ancient Race Artifact (intact) "
            "OR 1 Stolen Vehicle Core (Tier 5+)"
        ),
        "stat_bonus": {
            "END": 12, "SYS": 12, "STR": 7, "AGI": 5,
            "INT": 3, "PER": 3, "LCK": 2,
        },
        "unlocks": [
            "Core Instinct — warns of threats, guides to resources",
            "Selective Appetite — refuses low-quality resources",
            "Pocket Dimension +200% size",
            "Vehicle Self-Awareness — vehicle responds to Traveller's emotions",
        ],
        "feeding_count": 80,
    },
    {
        "tier": 7,
        "name": "Transcendent Core",
        "description": (
            "Beyond anything the current universe has documented. The core "
            "exists partially outside normal dimensional space. It can interface "
            "with reality in ways the System never intended. Ancient race ruins "
            "react to its presence. The Architects' constructs recognize it."
        ),
        "rp_cost": 50_000_000_000,
        "resource_cost": (
            "10 Dungeon Cores OR 5 Ancient Race Artifacts "
            "OR materials unknown to current civilization"
        ),
        "stat_bonus": {
            "END": 18, "SYS": 18, "STR": 10, "AGI": 8,
            "INT": 5, "PER": 5, "LCK": 3, "WIS": 3,
        },
        "unlocks": [
            "Dimensional Bleed — core partially exists outside normal space",
            "Ancient Recognition — Architect ruins respond to core presence",
            "Pocket Dimension becomes semi-autonomous ecosystem",
            "Vehicle can enter dimensional folds without a drive",
            "Auto-Harvest 50% — most kill drops absorbed automatically",
        ],
        "feeding_count": 120,
    },
    {
        "tier": 8,
        "name": "Primordial Core",
        "description": (
            "The core has reached a state that may have been achieved only by "
            "the First Travellers. It resonates with the fundamental frequency "
            "of the System itself. Other Vehicle Cores in proximity grow "
            "agitated — as if recognizing something ancient and terrifying."
        ),
        "rp_cost": 500_000_000_000,
        "resource_cost": (
            "Resources beyond current classification. Requires materials "
            "from the uncharted 60% of the universe."
        ),
        "stat_bonus": {
            "END": 25, "SYS": 25, "STR": 15, "AGI": 12,
            "INT": 8, "PER": 8, "LCK": 5, "WIS": 5, "VIT": 10,
        },
        "unlocks": [
            "System Resonance — core vibrates at System's fundamental frequency",
            "Core Intimidation — nearby cores react with fear/submission",
            "Pocket Dimension can sustain permanent ecosystems",
            "Vehicle begins merging with dimensional space",
            "Auto-Harvest 75%",
        ],
        "feeding_count": 200,
    },
    {
        "tier": 9,
        "name": "Infinite Core",
        "description": (
            "There is no ceiling. The core has entered a state of limitless "
            "growth potential. Every feeding makes it stronger with no "
            "diminishing returns. This is the state that the shelter upgrade "
            "system in its purest form — infinite, boundless, ever-hungry. "
            "Only Mohamed's dual system can sustain feeding at this level."
        ),
        "rp_cost": 5_000_000_000_000,
        "resource_cost": (
            "Anything. The core accepts all resources at this level. "
            "Even ambient System energy, starlight, dimensional radiation. "
            "Each feeding provides linear growth with no cap."
        ),
        "stat_bonus": {
            "END": 50, "SYS": 50, "STR": 25, "AGI": 20,
            "INT": 15, "PER": 15, "LCK": 10, "WIS": 10, "VIT": 20,
        },
        "unlocks": [
            "Limitless Growth — no diminishing returns on feeding",
            "Universal Consumption — accepts any resource as food",
            "Pocket Dimension becomes a world",
            "Vehicle transcends physical classification",
            "Auto-Harvest 100% — all resources automatically absorbed",
            "Core cannot be stolen — it IS the Traveller",
        ],
        "feeding_count": 500,
    },
]

# ── Feedable Resource Types ─────────────────────────────────────

FEEDABLE_RESOURCES = [
    {
        "name": "Monster Core",
        "description": (
            "Crystalline core extracted from slain System creatures. "
            "Contains condensed System energy. Quality scales with creature tier."
        ),
        "base_feed_value": 100,
        "tier_multiplier": 10,
        "availability": "Common — drops from most creatures above Tier 0",
    },
    {
        "name": "Dungeon Crystal",
        "description": (
            "Crystallized ambient energy found in dungeon treasure rooms. "
            "Higher-tier dungeons produce larger, more potent crystals."
        ),
        "base_feed_value": 500,
        "tier_multiplier": 20,
        "availability": "Uncommon — found in dungeon treasure rooms",
    },
    {
        "name": "Rare Material",
        "description": (
            "System-enhanced materials with unique properties. Includes "
            "living metal, phase-shift crystals, void-touched minerals."
        ),
        "base_feed_value": 5_000,
        "tier_multiplier": 50,
        "availability": "Rare — specialized vendors, high-tier dungeons, alien trade",
    },
    {
        "name": "Epic Material",
        "description": (
            "Materials that defy conventional physics. Dimensionally "
            "stable compounds, reality-anchoring alloys, time-crystallized ore."
        ),
        "base_feed_value": 50_000,
        "tier_multiplier": 100,
        "availability": "Very Rare — ancient ruins, dimensional anomalies, boss drops",
    },
    {
        "name": "Legendary Material",
        "description": (
            "Materials from the age of the Ancient Races. May contain "
            "encoded information or residual consciousness. Handling "
            "requires specialized equipment."
        ),
        "base_feed_value": 500_000,
        "tier_multiplier": 500,
        "availability": "Extremely Rare — ancient vaults, one-time discoveries",
    },
    {
        "name": "Dungeon Core",
        "description": (
            "The heart of a dungeon. Extracting it destroys the dungeon "
            "permanently. Contains immense condensed System energy. "
            "Illegal to extract in most jurisdictions."
        ),
        "base_feed_value": 5_000_000,
        "tier_multiplier": 1_000,
        "availability": "Unique — each dungeon has exactly one, extraction is irreversible",
    },
    {
        "name": "Ancient Race Artifact",
        "description": (
            "Technology or materials from extinct precursor civilizations. "
            "Often contains encoded knowledge or dimensional properties "
            "that modern science cannot replicate."
        ),
        "base_feed_value": 50_000_000,
        "tier_multiplier": 5_000,
        "availability": "Legendary — archaeological finds, guarded ruins",
    },
    {
        "name": "Stolen Vehicle Core",
        "description": (
            "A Vehicle Core extracted from another Traveller. When fed "
            "to a core, provides massive growth proportional to the "
            "stolen core's tier. Morally reprehensible, practically powerful."
        ),
        "base_feed_value": 10_000_000,
        "tier_multiplier": 10_000,
        "availability": "Depends on raider activity and moral compass",
    },
    {
        "name": "Ambient System Energy",
        "description": (
            "Raw System energy harvested from the environment. Low-density "
            "but infinitely available. Only Infinite Core (Feeding Tier 9) "
            "can efficiently metabolize ambient energy."
        ),
        "base_feed_value": 1,
        "tier_multiplier": 1,
        "availability": "Infinite — available everywhere the System is active",
    },
    {
        "name": "Dimensional Radiation",
        "description": (
            "Energy released during dimensional transitions, portal openings, "
            "or dimensional rifts. Dangerous to most beings but nutritious "
            "for a sufficiently evolved core."
        ),
        "base_feed_value": 10_000,
        "tier_multiplier": 200,
        "availability": "Uncommon — near dimensional anomalies and portals",
    },
]


# ── Mohamed's Dual-System Feeding Bypass ────────────────────────

MOHAMED_BYPASS = {
    "description": (
        "Mohamed's secondary RP Conversion system allows him to bypass "
        "normal feeding restrictions. While other Travellers hit diminishing "
        "returns at Feeding Tier 3-4, Mohamed's system converts excess "
        "feeding energy into RP, preventing waste and enabling unlimited "
        "feeding progression. His core can also process resources that would "
        "be toxic or incompatible for normal cores."
    ),
    "advantages": [
        "No diminishing returns at any feeding tier",
        "Can process incompatible resources (alien cores, void materials)",
        "Excess feeding energy converts to RP instead of being wasted",
        "Feeding speed is 3x faster than normal Travellers",
        "Can feed while the vehicle is summoned (others must dismiss first)",
        "Core evolution success rate: 100% (vs. declining rate for others)",
    ],
    "risks": [
        "Accelerated feeding draws System attention (anomaly flags)",
        "Core evolution events are visible to nearby Travellers",
        "Fed core emits unique energy signature detectable at range",
        "If others discover Mohamed can feed limitlessly, he becomes a target",
    ],
}


class VehicleCoreFeeding:
    """
    Manages the Vehicle Core feeding and limitless upgrade system.

    Tracks feeding history, calculates costs, validates resources,
    and generates context for chapter writing about feeding events.
    """

    def __init__(self) -> None:
        self.current_feeding_tier: int = 0
        self.total_feedings: int = 0
        self.feeding_history: list = []
        self.total_rp_invested: int = 0
        self.total_resources_consumed: list = []

    def get_feeding_tier_info(self, tier: Optional[int] = None) -> dict:
        """Get information about a specific feeding tier."""
        if tier is None:
            tier = self.current_feeding_tier
        if 0 <= tier < len(FEEDING_TIERS):
            return dict(FEEDING_TIERS[tier])
        return FEEDING_TIERS[-1]

    def get_next_tier_requirements(self) -> dict:
        """Get requirements for the next feeding tier."""
        next_tier = self.current_feeding_tier + 1
        if next_tier < len(FEEDING_TIERS):
            tier_info = FEEDING_TIERS[next_tier]
            feedings_needed = tier_info["feeding_count"] - self.total_feedings
            return {
                "next_tier": next_tier,
                "name": tier_info["name"],
                "rp_cost": tier_info["rp_cost"],
                "resource_cost": tier_info["resource_cost"],
                "feedings_remaining": max(0, feedings_needed),
                "unlocks": tier_info["unlocks"],
                "stat_bonus": tier_info["stat_bonus"],
            }
        return {
            "next_tier": None,
            "name": "Infinite — No ceiling",
            "description": "Core is at maximum classified tier. Growth continues linearly.",
        }

    def calculate_feed_value(
        self, resource_name: str, resource_tier: int = 0, quantity: int = 1
    ) -> int:
        """Calculate the feed value of a resource."""
        for resource in FEEDABLE_RESOURCES:
            if resource["name"].lower() == resource_name.lower():
                value = resource["base_feed_value"]
                value += resource["tier_multiplier"] * resource_tier
                return value * quantity
        return 0

    def feed_core(
        self,
        resource_name: str,
        resource_tier: int = 0,
        quantity: int = 1,
        rp_spent: int = 0,
        chapter_num: int = 0,
    ) -> dict:
        """
        Feed a resource to the Vehicle Core.

        Returns a dict with the feeding result, stat changes,
        and whether a tier advancement occurred.
        """
        feed_value = self.calculate_feed_value(
            resource_name, resource_tier, quantity
        )

        self.total_feedings += quantity
        self.total_rp_invested += rp_spent
        self.feeding_history.append({
            "resource": resource_name,
            "tier": resource_tier,
            "quantity": quantity,
            "feed_value": feed_value,
            "rp_spent": rp_spent,
            "chapter": chapter_num,
        })
        self.total_resources_consumed.append(
            f"{quantity}x {resource_name} (Tier {resource_tier})"
        )

        # Check for tier advancement
        tier_advanced = False
        new_tier_name = ""
        new_unlocks: list = []
        for tier_info in FEEDING_TIERS:
            if (
                tier_info["tier"] > self.current_feeding_tier
                and self.total_feedings >= tier_info["feeding_count"]
            ):
                self.current_feeding_tier = tier_info["tier"]
                tier_advanced = True
                new_tier_name = tier_info["name"]
                new_unlocks = tier_info["unlocks"]

        return {
            "success": True,
            "resource": resource_name,
            "quantity": quantity,
            "feed_value": feed_value,
            "total_feedings": self.total_feedings,
            "current_tier": self.current_feeding_tier,
            "tier_advanced": tier_advanced,
            "new_tier_name": new_tier_name,
            "new_unlocks": new_unlocks,
            "current_stat_bonus": self.get_current_stat_bonus(),
        }

    def get_current_stat_bonus(self) -> dict:
        """Get the cumulative stat bonus from the current feeding tier."""
        if 0 <= self.current_feeding_tier < len(FEEDING_TIERS):
            return dict(FEEDING_TIERS[self.current_feeding_tier]["stat_bonus"])
        return dict(FEEDING_TIERS[-1]["stat_bonus"])

    def get_feeding_summary(self) -> dict:
        """Get a summary of all feeding activity."""
        return {
            "current_tier": self.current_feeding_tier,
            "tier_name": (
                FEEDING_TIERS[self.current_feeding_tier]["name"]
                if self.current_feeding_tier < len(FEEDING_TIERS)
                else "Infinite Core"
            ),
            "total_feedings": self.total_feedings,
            "total_rp_invested": self.total_rp_invested,
            "resources_consumed": len(self.total_resources_consumed),
            "current_stat_bonus": self.get_current_stat_bonus(),
            "next_tier": self.get_next_tier_requirements(),
        }

    def build_feeding_context(self) -> str:
        """Build context string for chapter writing about core feeding."""
        tier_info = self.get_feeding_tier_info()
        next_req = self.get_next_tier_requirements()

        sections = [
            "## VEHICLE CORE FEEDING STATUS",
            f"Current Feeding Tier: {tier_info['tier']} — {tier_info['name']}",
            f"Description: {tier_info['description']}",
            f"Total Feedings: {self.total_feedings}",
            f"Stat Bonuses: {tier_info['stat_bonus']}",
        ]

        if tier_info.get("unlocks"):
            sections.append("Active Unlocks:")
            for unlock in tier_info["unlocks"]:
                sections.append(f"  - {unlock}")

        if next_req.get("next_tier") is not None:
            sections.append(f"\nNext Tier: {next_req['name']}")
            sections.append(f"  RP Cost: {next_req['rp_cost']:,}")
            sections.append(f"  Resource Cost: {next_req['resource_cost']}")
            sections.append(
                f"  Feedings Remaining: {next_req['feedings_remaining']}"
            )

        sections.append(f"\n## MOHAMED'S DUAL-SYSTEM BYPASS")
        sections.append(MOHAMED_BYPASS["description"])

        return "\n".join(sections)

    def get_all_tiers(self) -> list:
        """Return all feeding tier definitions."""
        return list(FEEDING_TIERS)

    def get_all_resources(self) -> list:
        """Return all feedable resource definitions."""
        return list(FEEDABLE_RESOURCES)
