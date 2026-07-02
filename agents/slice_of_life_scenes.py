"""
Slice-of-Life Scene System — Templates and generation for downtime scenes.

In a 1000+ chapter epic, not every chapter can be action-packed. Slice-of-life
scenes provide:
  - Character development through daily routines
  - Worldbuilding through mundane interactions
  - Pacing control (tension/release cycles)
  - Reader attachment through relatable moments
  - Breather chapters between intense arcs

These scenes typically take place inside Mohamed's vehicle pocket dimension,
at settlements, or during travel downtime.
"""

from agents.base_agent import BaseAgent


# ── Scene Templates ─────────────────────────────────────────────

SLICE_OF_LIFE_TEMPLATES = [
    {
        "id": "SOL-001",
        "name": "Morning Routine",
        "location": "Vehicle Pocket Dimension",
        "description": (
            "Mohamed wakes up in his vehicle's sleeping quarters. Goes through "
            "his morning routine — hygiene, checking System notifications from "
            "overnight, reviewing his stats, eating breakfast. Can include "
            "interactions with Zero AI or passengers."
        ),
        "beats": [
            "Wake up — describe the sleeping quarters and how they've changed with upgrades",
            "System check — review overnight notifications, resource gains, security alerts",
            "Personal hygiene — bathroom scene, reflect on physical changes from stat growth",
            "Breakfast — cooking or eating prepared food, discuss plans for the day",
            "Vehicle check — walk through the pocket dimension, note new features",
        ],
        "character_development": [
            "Show how Mohamed's daily habits have evolved since Day Zero",
            "Internal monologue about goals, fears, and relationships",
            "Compare current comfort to early survival days",
        ],
        "tone": "Calm, introspective, grounding",
        "word_count_target": 2500,
    },
    {
        "id": "SOL-002",
        "name": "Cooking and Meals",
        "location": "Vehicle Kitchen",
        "description": (
            "Mohamed prepares a meal using monster ingredients, System-enhanced "
            "produce, or alien recipes. Cooking scenes reveal character through "
            "the care (or lack thereof) in food preparation. Food buffs provide "
            "a practical reason for detailed cooking scenes."
        ),
        "beats": [
            "Ingredient selection — what's available, what buffs are needed",
            "Cooking process — describe techniques, System-enhanced tools",
            "Food buff activation — System notification of buff gained",
            "Eating — taste, texture, memories associated with food",
            "Cleanup — mundane task that grounds the fantasy world",
        ],
        "character_development": [
            "Show creativity and adaptability through cooking alien ingredients",
            "Share meals with others to deepen relationships",
            "Reflect on how food connects to pre-System memories",
        ],
        "tone": "Warm, domestic, sensory-rich",
        "word_count_target": 2500,
    },
    {
        "id": "SOL-003",
        "name": "Vehicle Maintenance",
        "location": "Vehicle Interior / Workshop",
        "description": (
            "Mohamed performs maintenance on his vehicle — checking systems, "
            "repairing damage, installing minor upgrades, cleaning. This is "
            "the car equivalent of a knight polishing armor. Shows the "
            "relationship between Traveller and Soul Vehicle."
        ),
        "beats": [
            "Inspection — walk around vehicle, note wear and damage",
            "Repair work — hands-on mechanical work with System assistance",
            "Upgrade planning — review available upgrades, costs, priorities",
            "System diagnostics — HUD readout of vehicle stats and status",
            "Bonding — quiet moment with the vehicle, feel the core's pulse",
        ],
        "character_development": [
            "Show mechanical competence growing over time",
            "Vehicle as emotional anchor — home, safety, identity",
            "Zero AI interaction during maintenance",
        ],
        "tone": "Focused, meditative, craftsman-like",
        "word_count_target": 2500,
    },
    {
        "id": "SOL-004",
        "name": "Training Session",
        "location": "EXP Farm / Pocket Dimension",
        "description": (
            "Mohamed trains inside his pocket dimension — combat drills, "
            "stat training, ability practice, or sparring with EXP farm "
            "creatures. Training scenes show growth and can include time "
            "dilation for extended sessions."
        ),
        "beats": [
            "Warm-up — physical preparation, stretch, mental focus",
            "Skill practice — specific techniques, abilities, or stat training",
            "Challenge — push beyond current limits, fail and retry",
            "Breakthrough — small improvement, stat notification",
            "Cool-down — reflect on progress, plan next session",
        ],
        "character_development": [
            "Show discipline and work ethic",
            "Internal monologue about power goals and motivation",
            "Compare current abilities to where he started",
        ],
        "tone": "Determined, physical, growth-oriented",
        "word_count_target": 3000,
    },
    {
        "id": "SOL-005",
        "name": "Settlement Visit",
        "location": "Human Settlement / Trading Post",
        "description": (
            "Mohamed visits a settlement for trading, information gathering, "
            "or socializing. Settlement scenes reveal the state of the world, "
            "introduce side characters, and provide economic context."
        ),
        "beats": [
            "Arrival — describe settlement layout, security, atmosphere",
            "Market — browse goods, check prices, negotiate trades",
            "Information — tavern/gathering place conversations, rumors, news",
            "Interaction — meaningful conversation with a local or side character",
            "Departure — leave with new information, items, or relationships",
        ],
        "character_development": [
            "Show social skills and how others perceive Mohamed",
            "Reveal world state through NPC conversations",
            "Economic decisions reveal priorities and values",
        ],
        "tone": "Social, observant, worldbuilding-rich",
        "word_count_target": 3000,
    },
    {
        "id": "SOL-006",
        "name": "Research and Study",
        "location": "Vehicle Research Terminal / Laboratory",
        "description": (
            "Mohamed researches a topic — System mechanics, enemy weaknesses, "
            "upgrade paths, alien technology, or ancient race mysteries. Study "
            "scenes justify knowledge growth and technology progression."
        ),
        "beats": [
            "Question — what does Mohamed need to learn and why",
            "Research process — databases, experiments, analysis",
            "Discovery — find relevant information, connect dots",
            "Application — plan how to use new knowledge",
            "Record — update personal notes, share findings with allies",
        ],
        "character_development": [
            "Show intellectual curiosity and problem-solving approach",
            "Reveal hidden lore through research discoveries",
            "Connect research to upcoming plot developments",
        ],
        "tone": "Intellectual, curious, discovery-driven",
        "word_count_target": 2500,
    },
    {
        "id": "SOL-007",
        "name": "Night Watch / Stargazing",
        "location": "Vehicle Exterior / Rooftop",
        "description": (
            "Mohamed takes a quiet moment outside his vehicle at night — "
            "watching the stars, reflecting on the journey, or standing "
            "guard. Contemplative scene that provides philosophical depth."
        ),
        "beats": [
            "Setting — describe the night sky, environment, atmosphere",
            "Reflection — think about the journey so far, losses and gains",
            "Observation — notice something in the environment (subtle foreshadowing)",
            "Resolution — make a quiet decision or affirmation",
            "Return — go back inside, ready for what's next",
        ],
        "character_development": [
            "Deep internal monologue about purpose and identity",
            "Process emotional events from recent chapters",
            "Show vulnerability in private moments",
        ],
        "tone": "Contemplative, atmospheric, emotionally honest",
        "word_count_target": 2500,
    },
    {
        "id": "SOL-008",
        "name": "Core Feeding Ritual",
        "location": "Vehicle Interior / Core Chamber",
        "description": (
            "Mohamed feeds resources to his Vehicle Core. The feeding process "
            "is described in sensory detail — the core's reaction, the energy "
            "flow, the changes in the vehicle. A quiet, almost spiritual "
            "scene that reveals the bond between Traveller and core."
        ),
        "beats": [
            "Preparation — gather resources, clear the space, focus",
            "Offering — present resources to the core, describe its reaction",
            "Absorption — the core consumes the resource, energy flows",
            "Transformation — describe changes in the core, new patterns",
            "Assessment — check feeding tier progress, plan next feeding",
        ],
        "character_development": [
            "Show the growing bond between Mohamed and his core",
            "Describe the core's developing personality/instincts",
            "Reflect on the ethics of core feeding (especially if using stolen cores)",
        ],
        "tone": "Ritualistic, sensory, mystical",
        "word_count_target": 2500,
    },
    {
        "id": "SOL-009",
        "name": "Wanderer Encounter",
        "location": "Road / Wilderness / Settlement Edge",
        "description": (
            "Mohamed encounters Wanderers — core-less Travellers who lost "
            "their vehicles. This encounter provides worldbuilding about "
            "the harsh realities of the System world, and reveals Mohamed's "
            "character through how he treats the disadvantaged."
        ),
        "beats": [
            "Discovery — come across Wanderers, assess their condition",
            "Interaction — conversation reveals their story and situation",
            "Decision — help, trade, or move on (character-defining moment)",
            "Consequence — how the decision affects Mohamed and the Wanderers",
            "Reflection — think about the Wanderer system and its injustice",
        ],
        "character_development": [
            "Reveal moral compass through treatment of Wanderers",
            "Explore the Phantom Travelling compulsion firsthand",
            "Create potential recurring characters from Wanderer encounters",
        ],
        "tone": "Empathetic, morally complex, worldbuilding",
        "word_count_target": 3000,
    },
    {
        "id": "SOL-010",
        "name": "System Tinkering",
        "location": "Vehicle Interior",
        "description": (
            "Mohamed experiments with his dual system — testing RP Conversion "
            "mechanics, exploring hidden features, pushing boundaries. These "
            "scenes advance the cheat system subplot and foreshadow future "
            "capabilities."
        ),
        "beats": [
            "Curiosity — notice something unusual about the system interface",
            "Experiment — test a theory about RP Conversion mechanics",
            "Result — discover a new capability or limitation",
            "Caution — check if the Game System detected anything anomalous",
            "Plan — how to use or hide this new knowledge",
        ],
        "character_development": [
            "Show scientific curiosity applied to the dual system",
            "Build tension around discovery risk",
            "Advance the long-term RP Conversion power progression",
        ],
        "tone": "Experimental, tense, discovery-driven",
        "word_count_target": 2500,
    },
    {
        "id": "SOL-011",
        "name": "Travel and Scenery",
        "location": "Open Road / Wilderness",
        "description": (
            "Mohamed drives through the changed landscape. Travel scenes "
            "reveal the state of the world — destroyed cities, mutated "
            "forests, System-altered terrain. The journey itself becomes "
            "the story."
        ),
        "beats": [
            "Departure — leave current location, set course",
            "Landscape — describe the terrain, System-altered environment",
            "Encounter — pass something interesting (ruins, creatures, other Travellers)",
            "Observation — notice environmental storytelling clues",
            "Arrival or camp — reach destination or set up for the night",
        ],
        "character_development": [
            "Show adaptability to the post-System world",
            "Environmental storytelling reveals lore organically",
            "Driving scenes parallel Mohamed's emotional journey",
        ],
        "tone": "Atmospheric, explorative, world-painting",
        "word_count_target": 2500,
    },
    {
        "id": "SOL-012",
        "name": "Inventory Management",
        "location": "Vehicle Cargo Hold / Workshop",
        "description": (
            "Mohamed sorts through his inventory — weapons, materials, loot, "
            "consumables. Inventory scenes are a staple of LitRPG and provide "
            "readers with power tracking and resource management context."
        ),
        "beats": [
            "Overview — current inventory state, what's useful, what's junk",
            "Sorting — organize by category, identify valuable items",
            "Decision — what to keep, sell, feed to core, or craft with",
            "Discovery — find a forgotten item or notice a new use for something",
            "Planning — what items are needed for upcoming challenges",
        ],
        "character_development": [
            "Resource management reveals strategic thinking",
            "Sentimental items reveal emotional attachments",
            "Preparation for future challenges shows foresight",
        ],
        "tone": "Methodical, satisfying, game-like",
        "word_count_target": 2500,
    },
]


# ── Scene Selection Logic ───────────────────────────────────────

PACING_GUIDE = {
    "after_action": [
        "SOL-001",  # Morning Routine (recovery after intense events)
        "SOL-007",  # Night Watch (reflection after combat)
        "SOL-004",  # Training (preparing for next challenge)
    ],
    "between_arcs": [
        "SOL-005",  # Settlement Visit (transition scene)
        "SOL-011",  # Travel and Scenery (physical transition)
        "SOL-006",  # Research (set up next arc)
    ],
    "character_development": [
        "SOL-002",  # Cooking (domestic, relatable)
        "SOL-009",  # Wanderer Encounter (moral depth)
        "SOL-007",  # Night Watch (introspection)
    ],
    "power_progression": [
        "SOL-008",  # Core Feeding Ritual
        "SOL-010",  # System Tinkering
        "SOL-004",  # Training Session
    ],
    "worldbuilding": [
        "SOL-005",  # Settlement Visit
        "SOL-011",  # Travel and Scenery
        "SOL-003",  # Vehicle Maintenance
    ],
    "filler_breather": [
        "SOL-002",  # Cooking
        "SOL-012",  # Inventory Management
        "SOL-001",  # Morning Routine
    ],
}


class SliceOfLifeSceneGenerator(BaseAgent):
    """
    Generates slice-of-life scene prompts for downtime chapters.

    Uses templates to create structured scene beats that maintain
    character consistency and advance subtle plot threads even
    during quiet moments.
    """

    name = "Slice-of-Life Scene Generator"
    role = "Downtime Scene Planner"
    temperature = 0.75
    max_tokens = 3000

    system_prompt = (
        "You are a slice-of-life scene planner for the novel RP Conversion. "
        "Your job is to create detailed, engaging downtime scenes that:\n\n"
        "1. **Ground the fantasy** — Show daily life in a System world\n"
        "2. **Develop character** — Reveal personality through mundane actions\n"
        "3. **Advance subtle plots** — Plant seeds for future developments\n"
        "4. **Control pacing** — Provide breathing room between intense arcs\n"
        "5. **Build world** — Show the lived-in reality of the universe\n\n"
        "Guidelines:\n"
        "- Every scene must have at least one moment of character revelation\n"
        "- Include sensory details (what does the food taste like, what does "
        "the vehicle hum sound like, what does the night sky look like)\n"
        "- Include at least one System notification or stat check per scene\n"
        "- Foreshadow upcoming events subtly through observations or thoughts\n"
        "- Maintain Mohamed's character voice appropriate to his current arc\n"
        "- End on a hook — even quiet scenes should have forward momentum\n\n"
        "Output format:\n"
        "SCENE_TYPE: [template name]\n"
        "LOCATION: [where the scene takes place]\n"
        "TONE: [emotional tone]\n"
        "BEATS:\n"
        "  1. [detailed beat with sensory direction]\n"
        "  2. [beat]\n"
        "  ...\n"
        "CHARACTER_NOTES: [what this scene reveals about Mohamed]\n"
        "FORESHADOWING: [subtle setup for future events]\n"
        "SYSTEM_MOMENT: [where to include a System notification or check]"
    )

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """Build the scene generation prompt."""
        scene_type = kwargs.get("scene_type", "")
        chapter_num = kwargs.get("chapter_num", 0)
        recent_events = kwargs.get("recent_events", "")
        mood = kwargs.get("mood", "")
        pacing_need = kwargs.get("pacing_need", "")

        # Find matching template
        template = None
        if scene_type:
            for t in SLICE_OF_LIFE_TEMPLATES:
                if (
                    t["id"] == scene_type
                    or t["name"].lower() == str(scene_type).lower()
                ):
                    template = t
                    break

        instruction_parts = [
            f"Generate a detailed slice-of-life scene plan for Chapter {chapter_num}."
        ]

        if template:
            instruction_parts.append(f"\nScene Template: {template['name']}")
            instruction_parts.append(f"Location: {template['location']}")
            instruction_parts.append(f"Tone: {template['tone']}")
            instruction_parts.append(f"Description: {template['description']}")
            instruction_parts.append("Suggested Beats:")
            for beat in template["beats"]:
                instruction_parts.append(f"  - {beat}")
            instruction_parts.append("Character Development Focus:")
            for cd in template["character_development"]:
                instruction_parts.append(f"  - {cd}")

        if recent_events:
            instruction_parts.append(f"\nRecent Events: {recent_events}")
        if mood:
            instruction_parts.append(f"Desired Mood: {mood}")
        if pacing_need:
            instruction_parts.append(f"Pacing Need: {pacing_need}")
            if pacing_need in PACING_GUIDE:
                suggested = PACING_GUIDE[pacing_need]
                instruction_parts.append(f"Suggested Templates: {suggested}")

        instruction = "\n".join(instruction_parts)
        return self.format_instruction(context, instruction)

    def parse_result(self, raw_output: str) -> dict:
        """Parse the scene generation output."""
        return {
            "status": "pass",
            "output": raw_output.strip(),
        }

    def get_template(self, template_id: str) -> dict:
        """Get a specific scene template by ID or name."""
        for template in SLICE_OF_LIFE_TEMPLATES:
            if (
                template["id"] == template_id
                or template["name"].lower() == template_id.lower()
            ):
                return dict(template)
        return {}

    def get_all_templates(self) -> list:
        """Return all scene templates."""
        return list(SLICE_OF_LIFE_TEMPLATES)

    def suggest_scene(self, pacing_need: str = "filler_breather") -> list:
        """Suggest appropriate scene templates based on pacing needs."""
        template_ids = PACING_GUIDE.get(pacing_need, PACING_GUIDE["filler_breather"])
        suggestions = []
        for tid in template_ids:
            template = self.get_template(tid)
            if template:
                suggestions.append(template)
        return suggestions

    def get_pacing_categories(self) -> dict:
        """Return all pacing categories and their associated templates."""
        return dict(PACING_GUIDE)
