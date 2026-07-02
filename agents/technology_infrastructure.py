"""
Technology & Infrastructure Realism Module — Grounded tech systems.

Inspired by "Getting a Technology System in Modern Day" (Agent_047), this
module provides realistic technology progression, VR environments,
networking, energy systems, batteries, production, and marketing
infrastructure for the RP Conversion universe.

Key elements from the source novel:
  - VR with time acceleration (90 real days = 20 years in VR)
  - Quantum communication satellites with advanced structures
  - OS development (GAIA OS) with memory optimization
  - Network infrastructure and communication systems
  - Energy systems and resource management
  - Production and manufacturing capabilities
  - Marketing and business development

Adapted for RP Conversion:
  - VR environments powered by Vehicle Core + pocket dimension
  - System-enhanced networking and communication
  - Energy systems blending RP and conventional power
  - Production scaled to individual Traveller and settlement levels
  - Marketing and trade within the System economy
"""

from agents.base_agent import BaseAgent


# ── VR Environment System ───────────────────────────────────────
# VR within the pocket dimension, combining time dilation with
# virtual training environments.

VR_ENVIRONMENTS = {
    "overview": (
        "Virtual Reality in RP Conversion is powered by the Vehicle Core's "
        "pocket dimension capabilities. Unlike conventional VR that requires "
        "headsets and hardware, System VR creates a fully immersive sensory "
        "environment within a designated zone of the pocket dimension. The "
        "user's consciousness is interfaced through their System connection. "
        "Combined with time dilation, VR becomes a tool for accelerated "
        "learning, training, and development — mirroring Aron's use of VR "
        "in 'Getting a Technology System' to compress decades of research "
        "into months of real time."
    ),
    "tiers": [
        {
            "name": "Basic VR Chamber",
            "tier_required": 3,
            "cost_rp": 100_000,
            "features": [
                "Single-user sensory immersion",
                "Pre-built training scenarios (combat, survival, crafting)",
                "System-generated opponents that scale to user level",
                "70% training effectiveness vs real training",
                "No time dilation — uses real time",
            ],
            "size": "20m³",
            "description": (
                "A small VR chamber within the pocket dimension. The walls "
                "project System-generated environments. Full sensory immersion "
                "— sight, sound, touch, smell. Pain feedback at 30% intensity "
                "for realistic combat training without injury risk."
            ),
        },
        {
            "name": "Advanced VR Suite",
            "tier_required": 5,
            "cost_rp": 2_000_000,
            "features": [
                "Multi-user support (up to 4 simultaneous)",
                "Custom scenario creation and editing",
                "85% training effectiveness vs real training",
                "Compatible with time dilation (up to Tier 4)",
                "Memory recording and playback",
                "Skill tree visualization and guided training",
            ],
            "size": "80m³",
            "description": (
                "Full VR suite with scenario editor. Users can recreate any "
                "environment they've experienced — dungeons, alien worlds, "
                "combat scenarios. The System generates realistic opponents, "
                "environmental hazards, and NPCs. Combined with time dilation, "
                "users can experience weeks of training in hours."
            ),
        },
        {
            "name": "Reality Simulation Complex",
            "tier_required": 8,
            "cost_rp": 100_000_000,
            "features": [
                "Unlimited simultaneous users",
                "Full reality simulation — indistinguishable from real world",
                "95% training effectiveness vs real training",
                "Compatible with all time dilation tiers",
                "AI-driven adaptive scenarios",
                "Educational programs spanning all known fields",
                "Research environment with virtual lab",
                "Social simulation for diplomatic training",
            ],
            "size": "500m³",
            "description": (
                "The pinnacle of VR technology. A complete reality simulation "
                "powered by the Vehicle Core. Like Aron's VR mansion in "
                "'Getting a Technology System', this facility can simulate "
                "any scenario with perfect fidelity. Combined with Tier 7+ "
                "time dilation, users can live entire alternate lives within "
                "the simulation — decades of experience in days of real time."
            ),
        },
    ],
}

# ── Networking & Communication Systems ──────────────────────────

NETWORKING_SYSTEMS = {
    "overview": (
        "Communication infrastructure in RP Conversion ranges from basic "
        "System messaging (free but limited range) to galaxy-spanning "
        "quantum networks. Building communication infrastructure is one "
        "of the most strategically valuable activities — information is "
        "power, and controlling communication networks means controlling "
        "the flow of information."
    ),
    "tiers": [
        {
            "name": "System Messaging",
            "tier_required": 0,
            "cost_rp": 0,
            "range": "10km",
            "bandwidth": "Text only",
            "description": (
                "Built-in System communication. Free but limited range. "
                "Text-only messages between Travellers within range. "
                "Every Traveller has this by default."
            ),
        },
        {
            "name": "Enhanced Relay Network",
            "tier_required": 2,
            "cost_rp": 50_000,
            "range": "500km per relay tower",
            "bandwidth": "Voice + text + images",
            "description": (
                "Network of System relay towers that extend communication "
                "range. Voice calls, text, and image sharing. Requires "
                "infrastructure investment but enables settlement-to-"
                "settlement communication."
            ),
        },
        {
            "name": "Quantum Entanglement Array",
            "tier_required": 6,
            "cost_rp": 10_000_000,
            "range": "Unlimited (paired devices)",
            "bandwidth": "Full audio/video + data transfer",
            "description": (
                "Instantaneous communication between paired quantum devices. "
                "Inspired by the quantum communication satellites in 'Getting "
                "a Technology System'. Each pair is manufactured together and "
                "linked at the quantum level. Uninterceptable, zero latency."
            ),
        },
        {
            "name": "Dimensional Network Hub",
            "tier_required": 8,
            "cost_rp": 500_000_000,
            "range": "Cross-dimensional",
            "bandwidth": "Unlimited — full reality data stream",
            "description": (
                "Network routing through dimensional shortcuts. Enables "
                "internet-like connectivity across the universe. Requires "
                "dimensional relay infrastructure. Only the most advanced "
                "civilizations operate dimensional networks."
            ),
        },
    ],
}

# ── Energy Systems ──────────────────────────────────────────────

ENERGY_SYSTEMS = {
    "overview": (
        "Energy in RP Conversion is a blend of conventional physics and "
        "System enhancement. RP can be converted to electricity, but at "
        "scale, dedicated power generation becomes more efficient. Energy "
        "management is critical for settlements, vehicles, and technology."
    ),
    "sources": [
        {
            "name": "RP-to-Electric Converter",
            "tier_required": 1,
            "output": "10 kWh per 1 RP",
            "scalability": "Small — personal/vehicle use",
            "cost_rp": 5_000,
            "description": (
                "Direct conversion of RP to electrical energy. Simple, "
                "reliable, available to any Traveller. The default power "
                "source for vehicle systems and personal devices."
            ),
        },
        {
            "name": "System-Enhanced Solar Array",
            "tier_required": 2,
            "output": "85% solar efficiency + 1 RP/hour passive",
            "scalability": "Medium — settlement power",
            "cost_rp": 5_000,
            "description": (
                "Solar panels enhanced with System energy coating. 4x more "
                "efficient than pre-System panels. Also generates small "
                "amounts of RP from sunlight. Essential for sustainable "
                "settlements."
            ),
        },
        {
            "name": "Dungeon Core Tap",
            "tier_required": 4,
            "output": "Powers a small city",
            "scalability": "Large — city-level power",
            "cost_rp": 500_000,
            "description": (
                "Siphons energy from a dungeon's core. Massive output but "
                "controversial — risks destabilizing the dungeon. Some "
                "factions build entire cities around tapped dungeon cores."
            ),
        },
        {
            "name": "Fusion Reactor (System-Enhanced)",
            "tier_required": 6,
            "output": "Powers a large settlement indefinitely",
            "scalability": "Very Large — unlimited with fuel",
            "cost_rp": 50_000_000,
            "description": (
                "Fusion reactor augmented with System energy containment. "
                "Clean, nearly unlimited power. Requires hydrogen fuel "
                "(abundant) and System-enhanced containment fields. The "
                "Kael'thari pioneered this technology."
            ),
        },
        {
            "name": "Void Energy Harvester",
            "tier_required": 10,
            "output": "Effectively infinite",
            "scalability": "Unlimited",
            "cost_rp": 10_000_000_000,
            "description": (
                "Harvests energy from the void between dimensions. "
                "Theoretical output is infinite — limited only by "
                "containment capacity. Ancient Race technology that "
                "modern civilizations can barely replicate."
            ),
        },
    ],
}

# ── Battery & Energy Storage ────────────────────────────────────

BATTERY_SYSTEMS = [
    {
        "name": "RP Cell",
        "tier_required": 1,
        "capacity": "1,000 RP stored",
        "recharge": "System energy or RP converter",
        "cost_rp": 2_000,
        "description": (
            "Basic RP storage cell. Stores System energy for later use. "
            "Can discharge at controlled rates. Essential for powering "
            "equipment in areas with no ambient System energy."
        ),
    },
    {
        "name": "Crystal Battery",
        "tier_required": 3,
        "capacity": "50,000 RP stored",
        "recharge": "Any power source, 4-hour full charge",
        "cost_rp": 100_000,
        "description": (
            "Crystalline energy storage using System-enhanced minerals. "
            "High capacity, stable discharge. Can power vehicle systems "
            "for extended periods without active RP expenditure."
        ),
    },
    {
        "name": "Dimensional Capacitor",
        "tier_required": 6,
        "capacity": "10,000,000 RP stored",
        "recharge": "Any power source, 1-hour full charge",
        "cost_rp": 5_000_000,
        "description": (
            "Stores energy in a micro-dimensional pocket. Enormous "
            "capacity with minimal physical size. Can power time dilation "
            "fields, dimensional drives, and heavy weapons systems."
        ),
    },
    {
        "name": "Core Resonance Battery",
        "tier_required": 8,
        "capacity": "1,000,000,000 RP stored",
        "recharge": "Vehicle Core resonance, passive",
        "cost_rp": 500_000_000,
        "description": (
            "Battery that resonates with the Vehicle Core, passively "
            "recharging from the core's ambient energy. Effectively "
            "unlimited power for sustained operations. Required for "
            "high-tier time dilation maintenance."
        ),
    },
]

# ── Production & Manufacturing ──────────────────────────────────

PRODUCTION_SYSTEMS = {
    "overview": (
        "Manufacturing in RP Conversion ranges from hand crafting at a "
        "workshop bench to industrial-scale System-enhanced factories. "
        "Production capability determines a Traveller's or settlement's "
        "self-sufficiency and economic power."
    ),
    "facilities": [
        {
            "name": "Personal Workshop",
            "tier_required": 2,
            "output": "1-5 items/day, simple items",
            "cost_rp": 30_000,
            "description": (
                "Basic crafting workspace. Hand tools enhanced by System "
                "guidance. Can produce simple equipment, ammunition, and "
                "consumables. Quality depends on crafter's INT and skill."
            ),
        },
        {
            "name": "Assembly Line",
            "tier_required": 4,
            "output": "50-200 items/day, standard items",
            "cost_rp": 1_000_000,
            "description": (
                "System-guided assembly process for mass production. "
                "Produces standardized equipment at consistent quality. "
                "Requires raw materials and RP for operation. Can be "
                "staffed by unskilled workers with System guidance."
            ),
        },
        {
            "name": "Fabrication Complex",
            "tier_required": 6,
            "output": "1,000+ items/day, advanced items",
            "cost_rp": 50_000_000,
            "description": (
                "Full manufacturing facility using System-enhanced CNC, "
                "3D printing, and material processing. Can produce items "
                "up to 2 tiers below the facility's tier. Automated "
                "quality control and packaging."
            ),
        },
        {
            "name": "Atomic Printer",
            "tier_required": 8,
            "output": "Unlimited, any complexity",
            "cost_rp": 1_000_000_000,
            "description": (
                "Inspired by Aron's atomic printer in 'Getting a Technology "
                "System'. Assembles items atom-by-atom from raw materials. "
                "Can produce anything given the blueprint and materials. "
                "The ultimate manufacturing tool."
            ),
        },
    ],
}

# ── Marketing & Trade Systems ───────────────────────────────────

MARKETING_SYSTEMS = {
    "overview": (
        "Trade and commerce in the System universe. While the Game System "
        "provides no built-in market, Travellers and settlements have "
        "developed their own economic infrastructure."
    ),
    "trade_methods": [
        {
            "name": "Direct Barter",
            "tier_required": 0,
            "description": (
                "Face-to-face trading between individuals. No infrastructure "
                "required. Most common among low-tier Travellers and "
                "Wanderers. Prices are negotiated per transaction."
            ),
        },
        {
            "name": "Settlement Market",
            "tier_required": 2,
            "description": (
                "Organized marketplace within a settlement. Fixed stalls, "
                "posted prices, regulated by settlement authority. Tax "
                "on transactions (typically 5-10%). Most reliable way "
                "to buy and sell standard goods."
            ),
        },
        {
            "name": "System Auction House",
            "tier_required": 4,
            "description": (
                "System-integrated auction platform accessible to all "
                "Travellers within relay range. List items, set prices, "
                "and complete transactions through System interface. "
                "2% transaction fee. Most efficient for rare items."
            ),
        },
        {
            "name": "Interstellar Trade Network",
            "tier_required": 6,
            "description": (
                "Cross-system trade facilitated by the Iron Caravan and "
                "quantum communication. Orders placed remotely, goods "
                "shipped via convoy or Waypoint Gate. Enables access to "
                "alien technology and exotic materials."
            ),
        },
    ],
    "marketing_strategies": [
        {
            "name": "Reputation Building",
            "description": (
                "Establish a crafting or service reputation through "
                "consistent quality. Higher reputation = premium prices. "
                "The Forge Masters guild manages crafter certification."
            ),
        },
        {
            "name": "Exclusive Contracts",
            "description": (
                "Negotiate exclusive supply contracts with factions or "
                "settlements. Guaranteed income in exchange for priority "
                "supply. Common for high-tier crafters and resource suppliers."
            ),
        },
        {
            "name": "Information Trading",
            "description": (
                "Sell intelligence — dungeon locations, creature patterns, "
                "faction movements, trade route conditions. The Scholar's "
                "Compact and intelligence networks pay premium RP for "
                "actionable information."
            ),
        },
    ],
}

# ── OS & Software Systems ──────────────────────────────────────

SOFTWARE_SYSTEMS = {
    "overview": (
        "The Game System provides a base operating interface, but Travellers "
        "can develop custom software layers on top of it. Inspired by GAIA OS "
        "from 'Getting a Technology System', advanced Travellers can create "
        "sophisticated software tools."
    ),
    "applications": [
        {
            "name": "System Interface Customization",
            "tier_required": 1,
            "description": (
                "Modify the System HUD — layout, colors, information density, "
                "notification preferences. Basic but essential personalization."
            ),
        },
        {
            "name": "Combat Analysis Software",
            "tier_required": 3,
            "description": (
                "Real-time combat analysis overlay. Tracks enemy patterns, "
                "suggests optimal attack timing, calculates damage output. "
                "Requires INT 5+ to operate effectively."
            ),
        },
        {
            "name": "Resource Management Suite",
            "tier_required": 4,
            "description": (
                "Automated tracking of resources, RP flow, inventory, and "
                "production schedules. Alerts for low supplies. Optimizes "
                "resource allocation across vehicle systems."
            ),
        },
        {
            "name": "AI Assistant Framework",
            "tier_required": 6,
            "description": (
                "Framework for developing AI assistants (like Zero AI). "
                "Natural language interaction, task automation, predictive "
                "analysis. Requires significant INT and SYS stats."
            ),
        },
        {
            "name": "Reality Modeling Engine",
            "tier_required": 8,
            "description": (
                "Simulates complex systems — weather patterns, creature "
                "migrations, economic trends, combat scenarios. Like Aron's "
                "predictive systems. Requires massive computing resources "
                "(Vehicle Core processing power)."
            ),
        },
    ],
}


class TechnologyInfrastructureManager(BaseAgent):
    """
    Manages technology, infrastructure, and realism elements for writing.

    Provides context about VR systems, networking, energy, production,
    and trade for consistent technology portrayal across chapters.
    """

    name = "Technology Infrastructure Manager"
    role = "Technology & Realism Consultant"
    temperature = 0.30
    max_tokens = 2000

    system_prompt = (
        "You are a technology and infrastructure consultant for the novel "
        "RP Conversion. Your job is to ensure that technology, engineering, "
        "and infrastructure descriptions in the novel are grounded in "
        "realistic principles while accounting for System enhancement.\n\n"
        "Key principles:\n"
        "1. **Physics still applies** — System enhances but doesn't break "
        "fundamental physical laws\n"
        "2. **Engineering has constraints** — Materials, energy, time, and "
        "expertise are real limitations\n"
        "3. **Technology scales with tier** — Higher tiers unlock more "
        "advanced technology\n"
        "4. **Infrastructure requires investment** — Nothing is free; "
        "building and maintaining systems costs RP and resources\n"
        "5. **Realism adds immersion** — Specific technical details make "
        "the world feel real\n\n"
        "When reviewing prose, check for:\n"
        "- Technology beyond the character's tier level\n"
        "- Unrealistic infrastructure without investment\n"
        "- Energy use without power source\n"
        "- Communication beyond established range\n"
        "- Production without raw materials or facilities\n\n"
        "Response format:\n"
        "- If technology is realistic: TECH_CONSISTENT\n"
        "- If issues found:\n"
        "  TECH_ISSUE: [description]\n"
        "  SUGGESTION: [how to fix]"
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the technology check prompt."""
        prose = kwargs.get("prose", "")
        focus_area = kwargs.get("focus_area", "")
        vehicle_tier = kwargs.get("vehicle_tier", 0)

        instruction_parts = [
            f"Review the following prose for technology and infrastructure "
            f"consistency. Vehicle Tier: {vehicle_tier}."
        ]

        if focus_area:
            instruction_parts.append(f"Focus Area: {focus_area}")

        instruction_parts.append(f"\n## PROSE\n{str(prose)[:5000]}")

        instruction = "\n".join(instruction_parts)
        return self.format_instruction(context, instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse the technology check output."""
        output = raw_output.strip()
        if "TECH_CONSISTENT" in output:
            return {"status": "pass", "output": output}
        return {"status": "issues_found", "output": output}

    def build_tech_context(self, vehicle_tier: int = 0) -> str:
        """Build technology context for chapter writing."""
        sections = [
            "## TECHNOLOGY & INFRASTRUCTURE CONTEXT",
            f"Vehicle Tier: {vehicle_tier}",
        ]

        # Available VR
        sections.append("\n### VR Environments:")
        for vr_tier in VR_ENVIRONMENTS["tiers"]:
            available = "AVAILABLE" if vehicle_tier >= vr_tier["tier_required"] else "LOCKED"
            sections.append(
                f"  {vr_tier['name']} ({available}) — "
                f"Tier {vr_tier['tier_required']}+ | "
                f"Cost: {vr_tier['cost_rp']:,} RP"
            )

        # Available Energy
        sections.append("\n### Energy Sources:")
        for source in ENERGY_SYSTEMS["sources"]:
            available = "AVAILABLE" if vehicle_tier >= source["tier_required"] else "LOCKED"
            sections.append(
                f"  {source['name']} ({available}) — "
                f"Output: {source['output']}"
            )

        # Available Communication
        sections.append("\n### Communication:")
        for comm in NETWORKING_SYSTEMS["tiers"]:
            available = "AVAILABLE" if vehicle_tier >= comm["tier_required"] else "LOCKED"
            sections.append(
                f"  {comm['name']} ({available}) — "
                f"Range: {comm['range']}"
            )

        # Available Production
        sections.append("\n### Production Facilities:")
        for facility in PRODUCTION_SYSTEMS["facilities"]:
            available = "AVAILABLE" if vehicle_tier >= facility["tier_required"] else "LOCKED"
            sections.append(
                f"  {facility['name']} ({available}) — "
                f"Output: {facility['output']}"
            )

        return "\n".join(sections)

    def get_vr_info(self) -> dict:
        """Return VR environment information."""
        return dict(VR_ENVIRONMENTS)

    def get_networking_info(self) -> dict:
        """Return networking system information."""
        return dict(NETWORKING_SYSTEMS)

    def get_energy_info(self) -> dict:
        """Return energy system information."""
        return dict(ENERGY_SYSTEMS)

    def get_battery_info(self) -> list:
        """Return battery system information."""
        return list(BATTERY_SYSTEMS)

    def get_production_info(self) -> dict:
        """Return production system information."""
        return dict(PRODUCTION_SYSTEMS)

    def get_marketing_info(self) -> dict:
        """Return marketing system information."""
        return dict(MARKETING_SYSTEMS)

    def get_software_info(self) -> dict:
        """Return software system information."""
        return dict(SOFTWARE_SYSTEMS)
