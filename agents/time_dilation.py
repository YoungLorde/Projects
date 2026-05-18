"""
Time Dilation Pocket Dimension System — Exponential time scaling inside vehicles.

Inspired by "Getting a Technology System in Modern Day" where Aron could spend
90 real days but experience 20 years in VR, and by the classic "Hyperbolic Time
Chamber" trope. In RP Conversion, high-tier vehicles unlock a time dilation
field within their pocket dimension.

Time flows faster inside the pocket dimension than outside. The ratio scales
exponentially with investment, and costs scale into millions, billions,
trillions, and quintillions of RP — appropriate for a 1000+ chapter epic.

Key mechanics:
  - Time dilation is a Vehicle Core capability, not a System ability
  - Requires pocket dimension (Tier 1+ vehicle)
  - Base ratio starts at 2:1 (2 hours inside = 1 hour outside)
  - Maximum ratio is theoretically unlimited (Mohamed's dual system)
  - Higher ratios cost exponentially more RP to activate and maintain
  - Time dilation can be used for training, research, crafting, recovery
  - Living things inside experience the dilated time normally
  - Cannot be used offensively (field only works inside pocket dimension)
"""

from typing import Optional


# ── Time Dilation Tiers ─────────────────────────────────────────
# Each tier represents a level of time dilation capability.
# Ratio = hours inside per 1 hour outside.

TIME_DILATION_TIERS = [
    {
        "tier": 0,
        "name": "No Dilation",
        "ratio": "1:1",
        "hours_inside_per_hour_outside": 1,
        "vehicle_tier_required": 0,
        "activation_cost_rp": 0,
        "maintenance_cost_rp_per_hour": 0,
        "description": (
            "Standard time flow. No dilation active. Time inside the pocket "
            "dimension passes at the same rate as outside."
        ),
        "use_cases": [],
    },
    {
        "tier": 1,
        "name": "Minor Dilation",
        "ratio": "2:1",
        "hours_inside_per_hour_outside": 2,
        "vehicle_tier_required": 2,
        "activation_cost_rp": 10_000,
        "maintenance_cost_rp_per_hour": 500,
        "description": (
            "Barely noticeable time difference. 2 hours of work inside "
            "for every 1 hour that passes outside. Useful for short study "
            "sessions or extra sleep. The dilation field feels like a faint "
            "pressure on the ears."
        ),
        "use_cases": [
            "Extra rest and recovery",
            "Short study sessions",
            "Meditation and stat training",
        ],
    },
    {
        "tier": 2,
        "name": "Standard Dilation",
        "ratio": "5:1",
        "hours_inside_per_hour_outside": 5,
        "vehicle_tier_required": 3,
        "activation_cost_rp": 100_000,
        "maintenance_cost_rp_per_hour": 5_000,
        "description": (
            "Meaningful time advantage. 5 hours inside for every 1 outside. "
            "A full workday inside happens in less than 2 hours of real time. "
            "The dilation field causes a subtle visual shimmer at the pocket "
            "dimension boundary."
        ),
        "use_cases": [
            "Extended training sessions",
            "Crafting complex items",
            "Research projects",
            "Recovery from injuries",
        ],
    },
    {
        "tier": 3,
        "name": "Enhanced Dilation",
        "ratio": "10:1",
        "hours_inside_per_hour_outside": 10,
        "vehicle_tier_required": 4,
        "activation_cost_rp": 1_000_000,
        "maintenance_cost_rp_per_hour": 50_000,
        "description": (
            "Significant time compression. 10 hours inside = 1 hour outside. "
            "An entire day of training in under 2.5 hours of real time. "
            "Objects crossing the boundary experience a jarring time "
            "transition. Food brought in stays fresh longer from outside "
            "perspective."
        ),
        "use_cases": [
            "Intensive combat training",
            "Complex multi-step crafting",
            "Multi-day research compressed into hours",
            "Extended medical treatment and recovery",
            "Skill development sprints",
        ],
    },
    {
        "tier": 4,
        "name": "Major Dilation",
        "ratio": "24:1",
        "hours_inside_per_hour_outside": 24,
        "vehicle_tier_required": 5,
        "activation_cost_rp": 10_000_000,
        "maintenance_cost_rp_per_hour": 500_000,
        "description": (
            "One full day inside for every hour outside. A week of intensive "
            "training in just 7 hours of real time. The boundary between "
            "normal and dilated space is visible as a faint golden membrane. "
            "Sounds from outside are pitch-shifted down. This is the tier "
            "where time dilation becomes a strategic military advantage."
        ),
        "use_cases": [
            "Week-long training camps in a single day",
            "Emergency research under time pressure",
            "Mass production of equipment",
            "Strategic planning with extended deliberation",
            "Healing from severe injuries without losing campaign time",
        ],
    },
    {
        "tier": 5,
        "name": "Extreme Dilation",
        "ratio": "100:1",
        "hours_inside_per_hour_outside": 100,
        "vehicle_tier_required": 6,
        "activation_cost_rp": 100_000_000,
        "maintenance_cost_rp_per_hour": 5_000_000,
        "description": (
            "100 hours inside per 1 hour outside. Over 4 days inside for "
            "every hour of real time. A month of work in under 8 hours. "
            "The dilation field is clearly visible — a bubble of golden "
            "light that distorts everything viewed through it. People "
            "inside move imperceptibly fast from outside perspective."
        ),
        "use_cases": [
            "Month-long training regimens compressed into a day",
            "Developing entirely new combat techniques",
            "Building complex structures within the pocket dimension",
            "Extended VR training simulations",
            "Research breakthroughs requiring sustained concentration",
        ],
    },
    {
        "tier": 6,
        "name": "Temporal Compression",
        "ratio": "1,000:1",
        "hours_inside_per_hour_outside": 1_000,
        "vehicle_tier_required": 7,
        "activation_cost_rp": 1_000_000_000,
        "maintenance_cost_rp_per_hour": 50_000_000,
        "description": (
            "1,000 hours (41.7 days) inside per 1 hour outside. A year of "
            "training in under 9 hours. At this level, time dilation becomes "
            "a reality-altering phenomenon. The pocket dimension's internal "
            "physics begin to diverge slightly from external reality. "
            "Long-term exposure may cause Temporal Dissonance — a "
            "psychological condition where the user struggles to reconcile "
            "experienced time with external time."
        ),
        "use_cases": [
            "Year-long skill mastery in a single day",
            "Developing technology generations ahead",
            "Complete VR education programs (inspired by Getting a Technology System)",
            "Raising and training creatures or AI",
            "Building and testing prototypes through multiple iterations",
        ],
        "side_effects": [
            "Temporal Dissonance — psychological adjustment period needed",
            "Aging applies inside (user ages faster relative to outside)",
            "High RP drain on vehicle reserves",
        ],
    },
    {
        "tier": 7,
        "name": "Hyper-Temporal Field",
        "ratio": "10,000:1",
        "hours_inside_per_hour_outside": 10_000,
        "vehicle_tier_required": 8,
        "activation_cost_rp": 10_000_000_000,
        "maintenance_cost_rp_per_hour": 500_000_000,
        "description": (
            "10,000 hours (1.14 years) inside per 1 hour outside. A decade "
            "of experience in under 4 days. This is approaching the realm "
            "of what 'Getting a Technology System in Modern Day' achieved — "
            "Aron's 90 days = 20 years. At this tier, the pocket dimension "
            "must be large enough to sustain long-term habitation. Food "
            "production, water recycling, and entertainment become critical "
            "to prevent mental breakdown."
        ),
        "use_cases": [
            "Decade-long research programs (like Aron's VR research)",
            "Training that fundamentally transforms the user",
            "Creating entire technological civilizations within the dimension",
            "Extended recovery from reality-altering injuries",
            "Studying ancient artifacts for years without external pressure",
        ],
        "side_effects": [
            "Severe Temporal Dissonance — weeks of readjustment",
            "Significant aging relative to peers",
            "Risk of psychological dependency on dilated time",
            "Vehicle core strain — must feed core to sustain",
        ],
    },
    {
        "tier": 8,
        "name": "Temporal Singularity",
        "ratio": "100,000:1",
        "hours_inside_per_hour_outside": 100_000,
        "vehicle_tier_required": 10,
        "activation_cost_rp": 1_000_000_000_000,
        "maintenance_cost_rp_per_hour": 50_000_000_000,
        "description": (
            "100,000 hours (11.4 years) inside per 1 hour outside. A century "
            "of work in under 4 days. At this level, the pocket dimension "
            "becomes a self-sustaining world. Time inside is so compressed "
            "that the boundary membrane appears as a wall of frozen reality "
            "from inside. Only Mythic-tier vehicles can sustain this level. "
            "The RP cost is in the trillions per hour."
        ),
        "use_cases": [
            "Century-scale civilization building",
            "Mastering multiple lifetimes of skills",
            "Creating permanent ecosystems and populations",
            "Advancing technology by centuries",
        ],
        "side_effects": [
            "Extreme aging — user lives decades in subjective time",
            "Complete detachment from external reality",
            "Core may develop sentience from sustained strain",
            "Risk of dimensional instability at boundary",
        ],
    },
    {
        "tier": 9,
        "name": "Eternity Engine",
        "ratio": "1,000,000:1",
        "hours_inside_per_hour_outside": 1_000_000,
        "vehicle_tier_required": 15,
        "activation_cost_rp": 1_000_000_000_000_000,
        "maintenance_cost_rp_per_hour": 1_000_000_000_000,
        "description": (
            "1,000,000 hours (114 years) inside per 1 hour outside. A "
            "millennium in under 4 days. This is theoretical — no known "
            "Traveller has achieved this. The RP cost is in quintillions. "
            "At this tier, the pocket dimension is a universe unto itself. "
            "Only Mohamed's limitless core feeding, combined with his RP "
            "Conversion system, could theoretically sustain this level."
        ),
        "use_cases": [
            "Creating entire civilizations from scratch",
            "Achieving multiple lifetimes of mastery",
            "Building technology that rivals the Ancient Races",
            "Theoretical — endgame content for 1000+ chapter epic",
        ],
        "side_effects": [
            "User effectively lives a separate lifetime inside",
            "May develop entirely different personality from temporal isolation",
            "Pocket dimension may develop its own System-like rules",
            "Dimensional boundaries may become permanent",
        ],
    },
]


# ── Time Dilation Activities ────────────────────────────────────
# What can be done during dilated time.

DILATION_ACTIVITIES = {
    "training": {
        "description": (
            "Physical and combat training under accelerated time. Stat gains "
            "occur at the dilated rate — 10 hours of training in 1 hour of "
            "real time yields 10 hours' worth of stat improvement."
        ),
        "stat_benefit": "Normal training gains multiplied by dilation ratio",
        "requirements": "Training space, targets/equipment within pocket dimension",
    },
    "research": {
        "description": (
            "Scientific and System research. INT-based work benefits enormously "
            "from extended uninterrupted time. Complex problems that would take "
            "months can be solved in hours of real time."
        ),
        "stat_benefit": "Research progress multiplied by dilation ratio",
        "requirements": "Research Terminal or Laboratory upgrade in pocket dimension",
    },
    "crafting": {
        "description": (
            "Extended crafting sessions. Multi-step recipes that require curing, "
            "cooling, or repeated refinement can be completed in a fraction of "
            "the real-world time."
        ),
        "stat_benefit": "Crafting experience multiplied by dilation ratio",
        "requirements": "Workshop upgrade in pocket dimension",
    },
    "recovery": {
        "description": (
            "Healing and recovery from injuries. The body heals at the dilated "
            "rate. A wound that takes a week to heal takes only hours of "
            "external time at Tier 3 dilation."
        ),
        "stat_benefit": "HP recovery multiplied by dilation ratio",
        "requirements": "Medical bay or sleeping quarters in pocket dimension",
    },
    "vr_training": {
        "description": (
            "Virtual Reality training within the pocket dimension. Inspired by "
            "Getting a Technology System in Modern Day, where Aron spent decades "
            "in VR while only days passed in reality. VR environments can "
            "simulate any scenario — combat, survival, exploration, social."
        ),
        "stat_benefit": "VR training provides 75% of real training gains at 10x speed",
        "requirements": "VR Environment upgrade (Tier 4+ vehicle)",
    },
    "slice_of_life": {
        "description": (
            "Relaxation, personal time, hobbies, and character development. "
            "Mohamed can cook, read, exercise, maintain his vehicle, or simply "
            "rest. These scenes are important for pacing in a 1000+ chapter epic."
        ),
        "stat_benefit": "Stress reduction, morale boost, minor passive stat gains",
        "requirements": "Living quarters in pocket dimension",
    },
    "exp_farming": {
        "description": (
            "Using the internal EXP Farm or Pocket Dungeon under time dilation. "
            "Creatures respawn at the dilated rate. A 24-hour dungeon reset "
            "cycle completes in 1 hour of real time at Tier 4 dilation."
        ),
        "stat_benefit": "RP/XP gains multiplied by dilation ratio",
        "requirements": "EXP Farm or Pocket Dungeon upgrade",
    },
}


class TimeDilationSystem:
    """
    Manages the time dilation pocket dimension system.

    Tracks current dilation level, calculates costs, validates requirements,
    and generates context for chapter writing.
    """

    def __init__(self) -> None:
        self.current_tier: int = 0
        self.is_active: bool = False
        self.total_rp_spent_on_dilation: int = 0
        self.total_dilated_hours: int = 0
        self.sessions: list = []

    def get_tier_info(self, tier: Optional[int] = None) -> dict:
        """Get information about a specific dilation tier."""
        if tier is None:
            tier = self.current_tier
        if 0 <= tier < len(TIME_DILATION_TIERS):
            return dict(TIME_DILATION_TIERS[tier])
        return dict(TIME_DILATION_TIERS[-1])

    def get_max_available_tier(self, vehicle_tier: int) -> int:
        """Determine the maximum dilation tier available for a vehicle tier."""
        max_tier = 0
        for td_tier in TIME_DILATION_TIERS:
            if vehicle_tier >= td_tier["vehicle_tier_required"]:
                max_tier = td_tier["tier"]
        return max_tier

    def activate_dilation(
        self,
        tier: int,
        vehicle_tier: int,
        rp_available: int,
        duration_hours: int = 1,
        activity: str = "training",
        chapter_num: int = 0,
    ) -> dict:
        """
        Activate time dilation at the specified tier.

        Returns a dict with activation status, costs, and effective time gained.
        """
        # Validate tier
        if tier < 0 or tier >= len(TIME_DILATION_TIERS):
            return {"success": False, "error": f"Invalid dilation tier: {tier}"}

        tier_info = TIME_DILATION_TIERS[tier]

        # Check vehicle tier requirement
        if vehicle_tier < tier_info["vehicle_tier_required"]:
            return {
                "success": False,
                "error": (
                    f"Vehicle Tier {vehicle_tier} too low. "
                    f"Tier {tier} dilation requires Vehicle Tier "
                    f"{tier_info['vehicle_tier_required']}+"
                ),
            }

        # Calculate cost
        activation_cost = tier_info["activation_cost_rp"]
        maintenance_cost = tier_info["maintenance_cost_rp_per_hour"] * duration_hours
        total_cost = activation_cost + maintenance_cost

        if rp_available < total_cost:
            return {
                "success": False,
                "error": (
                    f"Insufficient RP. Need {total_cost:,} "
                    f"(activation: {activation_cost:,} + "
                    f"maintenance: {maintenance_cost:,}), "
                    f"have {rp_available:,}"
                ),
            }

        # Calculate effective time
        ratio = tier_info["hours_inside_per_hour_outside"]
        effective_hours = duration_hours * ratio

        # Record session
        session = {
            "tier": tier,
            "ratio": tier_info["ratio"],
            "real_hours": duration_hours,
            "effective_hours": effective_hours,
            "rp_cost": total_cost,
            "activity": activity,
            "chapter": chapter_num,
        }
        self.sessions.append(session)
        self.is_active = True
        self.current_tier = tier
        self.total_rp_spent_on_dilation += total_cost
        self.total_dilated_hours += effective_hours

        return {
            "success": True,
            "tier": tier,
            "tier_name": tier_info["name"],
            "ratio": tier_info["ratio"],
            "real_hours": duration_hours,
            "effective_hours": effective_hours,
            "effective_days": round(effective_hours / 24, 1),
            "activation_cost": activation_cost,
            "maintenance_cost": maintenance_cost,
            "total_cost": total_cost,
            "activity": activity,
            "side_effects": tier_info.get("side_effects", []),
        }

    def deactivate_dilation(self) -> dict:
        """Deactivate time dilation."""
        was_active = self.is_active
        self.is_active = False
        self.current_tier = 0
        return {
            "success": True,
            "was_active": was_active,
            "total_sessions": len(self.sessions),
            "total_dilated_hours": self.total_dilated_hours,
            "total_rp_spent": self.total_rp_spent_on_dilation,
        }

    def get_dilation_summary(self) -> dict:
        """Get a summary of all time dilation activity."""
        return {
            "is_active": self.is_active,
            "current_tier": self.current_tier,
            "total_sessions": len(self.sessions),
            "total_dilated_hours": self.total_dilated_hours,
            "total_dilated_days": round(self.total_dilated_hours / 24, 1),
            "total_rp_spent": self.total_rp_spent_on_dilation,
        }

    def build_dilation_context(self, vehicle_tier: int = 0) -> str:
        """Build context string for chapter writing about time dilation."""
        max_tier = self.get_max_available_tier(vehicle_tier)
        max_info = self.get_tier_info(max_tier)

        sections = [
            "## TIME DILATION POCKET DIMENSION",
            f"Max Available Tier: {max_tier} — {max_info['name']}",
            f"Max Ratio: {max_info['ratio']} "
            f"({max_info['hours_inside_per_hour_outside']} hours inside "
            f"per 1 hour outside)",
            f"Currently Active: {'Yes' if self.is_active else 'No'}",
        ]

        if self.is_active:
            current = self.get_tier_info()
            sections.append(f"Active Tier: {current['tier']} — {current['name']}")
            sections.append(f"Active Ratio: {current['ratio']}")

        sections.append("\nAvailable Tiers:")
        for td_tier in TIME_DILATION_TIERS:
            if td_tier["tier"] == 0:
                continue
            available = "AVAILABLE" if vehicle_tier >= td_tier["vehicle_tier_required"] else "LOCKED"
            sections.append(
                f"  Tier {td_tier['tier']}: {td_tier['name']} "
                f"({td_tier['ratio']}) — {available}"
            )
            if available == "LOCKED":
                sections.append(
                    f"    Requires: Vehicle Tier {td_tier['vehicle_tier_required']}"
                )

        sections.append("\nActivities During Dilation:")
        for activity_name, activity_info in DILATION_ACTIVITIES.items():
            sections.append(f"  {activity_name}: {activity_info['description'][:100]}...")

        return "\n".join(sections)

    def get_all_tiers(self) -> list:
        """Return all time dilation tier definitions."""
        return list(TIME_DILATION_TIERS)

    def get_all_activities(self) -> dict:
        """Return all dilation activity definitions."""
        return dict(DILATION_ACTIVITIES)
