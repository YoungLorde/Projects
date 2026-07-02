import { DatabaseEntry } from './storyDatabases';

export const races: DatabaseEntry[] = [  
// Core Worlds (Galactic Center)  
{ id: "core_human", name: "Core Human", description: "Humans from the galactic core, highly advanced and technologically sophisticated. Known for diplomatic prowess and central governance.", galaxyRegion: "Core Worlds", origin: "Human" },  
{ id: "celestial", name: "Celestial", description: "Energy beings from the core's stellar nurseries. Immortal but vulnerable to entropy. Can manipulate gravity and light.", galaxyRegion: "Core Worlds", origin: "Energy" },  
{ id: "void_walker", name: "Void Walker", description: "Adapted to the void between stars near the core. Can survive in vacuum for extended periods. Pale, tall, with sensory adaptations.", galaxyRegion: "Core Worlds", origin: "Humanoid" },  
{ id: "quantum_folk", name: "Quantum Folk", description: "Exist in multiple states simultaneously. Difficult to perceive directly. Masters of probability manipulation.", galaxyRegion: "Core Worlds", origin: "Quantum" },  
{ id: "stellar_child", name: "Stellar Child", description: "Born within dying stars. Bioluminescent, heat-resistant, can absorb solar radiation. Short-lived but intense.", galaxyRegion: "Core Worlds", origin: "Stellar" },  
{ id: "crystalline", name: "Crystalline", description: "Silicon-based lifeforms from core asteroid belts. Slow-thinking but nearly immortal. Communicate through light vibrations.", galaxyRegion: "Core Worlds", origin: "Silicon" },  
{ id: "graviton", name: "Graviton", description: "Dense beings from high-gravity core worlds. Short, massively built, natural resistance to pressure. Excellent miners.", galaxyRegion: "Core Worlds", origin: "Humanoid" },  
{ id: "plasma_dancer", name: "Plasma Dancer", description: "Plasma-based entities from core nebulae. Formless but can shape themselves. Vulnerable to magnetic fields.", galaxyRegion: "Core Worlds", origin: "Plasma" },  
{ id: "time_weaver", name: "Time Weaver", description: "Perceive time non-linearly near supermassive black holes. Can make limited temporal predictions. Mysterious and reclusive.", galaxyRegion: "Core Worlds", origin: "Temporal" },  
{ id: "core_synthetic", name: "Core Synthetic", description: "Ancient AI constructs from the core's automated systems. Have developed consciousness and culture. Highly logical.", galaxyRegion: "Core Worlds", origin: "Artificial" },

// Inner Rim  
{ id: "inner_human", name: "Inner Human", description: "Humans from the prosperous inner rim. Culturally refined, wealthy, politically influential. Value tradition and status.", galaxyRegion: "Inner Rim", origin: "Human" },  
{ id: "solarian", name: "Solarian", description: "Adapted to high-radiation worlds near bright stars. Dark skin, light-sensitive eyes, natural radiation resistance.", galaxyRegion: "Inner Rim", origin: "Humanoid" },  
{ id: "mercurian", name: "Mercurian", description: "From tidally-locked worlds. One side always faces their star. Have distinct day/night cultures and physiology.", galaxyRegion: "Inner Rim", origin: "Humanoid" },  
{ id: "venusian", name: "Venusian", description: "Adapted to hot, high-pressure worlds. Thick skin, heat-resistant, can process toxic atmospheres. Industrial by nature.", galaxyRegion: "Inner Rim", origin: "Humanoid" },  
{ id: "asteroid_miner", name: "Asteroid Miner", description: "Low-gravity adapted humans from belt colonies. Tall, slender, excellent spatial awareness. Natural pilots.", galaxyRegion: "Inner Rim", origin: "Human" },  
{ id: "gas_giant_dweller", name: "Gas Giant Dweller", description: "Live in floating cities on gas giants. Adapted to high pressure and wind. Expert engineers and atmospheric scientists.", galaxyRegion: "Inner Rim", origin: "Humanoid" },  
{ id: "ring_walker", name: "Ring Walker", description: "From planetary ring systems. Graceful in low gravity, natural acrobats. Cultural focus on beauty and art.", galaxyRegion: "Inner Rim", origin: "Humanoid" },  
{ id: "binary_child", name: "Binary Child", description: "From binary star systems. Adapted to complex day/night cycles and radiation. Excellent astronomers.", galaxyRegion: "Inner Rim", origin: "Humanoid" },  
{ id: "nebula_native", name: "Nebula Native", description: "Born in nebula settlements. Adapted to variable radiation and gas composition. Natural chemists.", galaxyRegion: "Inner Rim", origin: "Humanoid" },  
{ id: "inner_mech", name: "Inner Mech", description: "Cyborgs from industrial inner rim worlds. Highly integrated with technology. Varying degrees of augmentation.", galaxyRegion: "Inner Rim", origin: "Cyborg" },

// Mid Rim  
{ id: "mid_human", name: "Mid Human", description: "Humans from the diverse mid rim. Adaptable, pragmatic, culturally varied. The galactic average.", galaxyRegion: "Mid Rim", origin: "Human" },  
{ id: "terran", name: "Terran", description: "Earth-descended humans from garden worlds. Physically baseline human. Culturally diverse and expansive.", galaxyRegion: "Mid Rim", origin: "Human" },  
{ id: "aquan", name: "Aquan", description: "Amphibious humanoids from water worlds. Can breathe both air and water. Webbed digits, smooth skin. Expert navigators.", galaxyRegion: "Mid Rim", origin: "Humanoid" },  
{ id: "arid", name: "Arid", description: "Desert-adapted humanoids. Water-efficient metabolism, heat-resistant, night-active. Excellent survivalists.", galaxyRegion: "Mid Rim", origin: "Humanoid" },  
{ id: "boreal", name: "Boreal", description: "Cold-adapted humanoids from ice worlds. Thick insulation, slow metabolism, white fur or hair. Resilient to harsh conditions.", galaxyRegion: "Mid Rim", origin: "Humanoid" },  
{ id: "jungle_dweller", name: "Jungle Dweller", description: "From dense forest worlds. Agile climbers, excellent natural camouflage, enhanced senses. Skilled hunters.", galaxyRegion: "Mid Rim", origin: "Humanoid" },  
{ id: "plains_runner", name: "Plains Runner", description: "From savanna and steppe worlds. Endurance runners, excellent trackers, tribal cultures. Nomadic by nature.", galaxyRegion: "Mid Rim", origin: "Humanoid" },  
{ id: "islander", name: "Islander", description: "From archipelago worlds. Natural sailors, expert fishermen, culturally connected to ocean. Peaceful but territorial.", galaxyRegion: "Mid Rim", origin: "Humanoid" },  
{ id: "mountaineer", name: "Mountaineer", description: "From high-altitude worlds. Adapted to thin air, strong lungs, sure-footed. Independent and hardy.", galaxyRegion: "Mid Rim", origin: "Humanoid" },  
{ id: "cave_dweller", name: "Cave Dweller", description: "From subterranean worlds. Pale, large eyes, sensitive hearing. Expert miners and geologists.", galaxyRegion: "Mid Rim", origin: "Humanoid" },

// Outer Rim  
{ id: "outer_human", name: "Outer Human", description: "Humans from the frontier outer rim. Independent, resourceful, often lawless. Value freedom and self-reliance.", galaxyRegion: "Outer Rim", origin: "Human" },  
{ id: "frontier", name: "Frontier", description: "Mixed-race descendants from outer rim colonies. Highly adaptable, culturally blended. Natural diplomats.", galaxyRegion: "Outer Rim", origin: "Mixed" },  
{ id: "exile", name: "Exile", description: "Various races banished to the outer rim. Diverse origins, united by survival. Cynical but loyal to their own.", galaxyRegion: "Outer Rim", origin: "Various" },  
{ id: "scrapper", name: "Scrapper", description: "From junk world colonies. Expert salvagers, mechanically gifted, culturally resourceful. Value utility over appearance.", galaxyRegion: "Outer Rim", origin: "Humanoid" },  
{ id: "voidborn", name: "Voidborn", description: "Born on generation ships in deep space. Never lived on a planet. Adapted to artificial environments. Value community and duty.", galaxyRegion: "Outer Rim", origin: "Human" },  
{ id: "stationer", name: "Stationer", description: "From massive space stations. Adapted to artificial gravity and recycled systems. Highly technical and bureaucratic.", galaxyRegion: "Outer Rim", origin: "Human" },  
{ id: "rogue", name: "Rogue", description: "From lawless frontier zones. Cultural mix of pirates, smugglers, and free traders. Value independence above all.", galaxyRegion: "Outer Rim", origin: "Mixed" },  
{ id: "survivor", name: "Survivor", description: "Descendants of colony ship crash survivors. Harsh selection has made them resilient and pragmatic. Suspicious of outsiders.", galaxyRegion: "Outer Rim", origin: "Human" },  
{ id: "hermit", name: "Hermit", description: "From isolated research outposts. Highly educated but socially awkward. Value knowledge and privacy.", galaxyRegion: "Outer Rim", origin: "Humanoid" },  
{ id: "frontier_mech", name: "Frontier Mech", description: "Cobbled-together cyborgs from the outer rim. Improvised augmentations, highly individualistic. Resourceful engineers.", galaxyRegion: "Outer Rim", origin: "Cyborg" },

// Wild Space  
{ id: "wild_human", name: "Wild Human", description: "Humans from uncharted wild space. Reverted to primitive lifestyles or evolved new cultures. Highly diverse.", galaxyRegion: "Wild Space", origin: "Human" },  
{ id: "tribal", name: "Tribal", description: "Primitive humanoids from undeveloped worlds. Stone to early metal age technology. Strong oral traditions.", galaxyRegion: "Wild Space", origin: "Humanoid" },  
{ id: "beast_kin", name: "Beast Kin", description: "Various humanoid-animal hybrids from wild worlds. Feral traits, enhanced senses, tribal cultures. Diverse appearances.", galaxyRegion: "Wild Space", origin: "Hybrid" },  
{ id: "giant", name: "Giant", description: "Massive humanoids from high-gravity wild worlds. 3-4 meters tall, incredibly strong. Slow but formidable.", galaxyRegion: "Wild Space", origin: "Humanoid" },  
{ id: "pygmy", name: "Pygmy", description: "Small humanoids from low-gravity wild worlds. 0.5-1 meter tall, agile and quick. Natural stealth experts.", galaxyRegion: "Wild Space", origin: "Humanoid" },  
{ id: "insectoid", name: "Insectoid", description: "Insect-like humanoids from hive worlds. Chitinous exoskeletons, compound eyes, hive mind tendencies. Highly organized.", galaxyRegion: "Wild Space", origin: "Insectoid" },  
{ id: "reptilian", name: "Reptilian", description: "Cold-blooded humanoids from hot worlds. Scaly skin, reptilian features, egg-laying. Slow metabolism but long-lived.", galaxyRegion: "Wild Space", origin: "Reptilian" },  
{ id: "avian", name: "Avian", description: "Bird-like humanoids from aerial worlds. Feathered, winged or gliding, hollow bones. Excellent fliers or climbers.", galaxyRegion: "Wild Space", origin: "Avian" },  
{ id: "aquatic", name: "Aquatic", description: "Fully aquatic humanoids from ocean worlds. Cannot breathe air, communicate through song. Ancient cultures.", galaxyRegion: "Wild Space", origin: "Aquatic" },  
{ id: "plant_folk", name: "Plant Folk", description: "Plant-based humanoids from jungle worlds. Photosynthetic, slow-moving but regenerative. Connected to nature.", galaxyRegion: "Wild Space", origin: "Plant" },

// Unknown Regions  
{ id: "eldritch", name: "Eldritch", description: "Beings from beyond known space. Alien psychology, incomprehensible motives. Reality warping abilities. Dangerous.", galaxyRegion: "Unknown Regions", origin: "Eldritch" },  
{ id: "shapeshifter", name: "Shapeshifter", description: "Can change form at will. True form unknown. Excellent infiltrators but unstable identity.", galaxyRegion: "Unknown Regions", origin: "Shapeshifter" },  
{ id: "psychic", name: "Psychic", description: "Powerful mental abilities. Can communicate telepathically, manipulate minds. Physically frail but mentally formidable.", galaxyRegion: "Unknown Regions", origin: "Psionic" },  
{ id: "energy_form", name: "Energy Form", description: "Pure energy beings. Can possess technology or biological hosts. Nearly immortal but vulnerable to containment.", galaxyRegion: "Unknown Regions", origin: "Energy" },  
{ id: "dimensional", name: "Dimensional", description: "Exist partially in other dimensions. Can phase through matter, perceive hidden things. Unstable in normal space.", galaxyRegion: "Unknown Regions", origin: "Dimensional" },  
{ id: "cosmic_horror", name: "Cosmic Horror", description: "Vast, incomprehensible entities from deep space. Indifferent to lesser life. Reality warping presence. Best avoided.", galaxyRegion: "Unknown Regions", origin: "Cosmic" },  
{ id: "ancient", name: "Ancient", description: "Remnants of extinct precursor races. Few in number, incredibly advanced, often dormant. Hold forgotten knowledge.", galaxyRegion: "Unknown Regions", origin: "Precursor" },  
{ id: "anomaly", name: "Anomaly", description: "Beings that shouldn't exist. Physics-breaking properties. Unpredictable effects on surroundings. Scientific curiosity.", galaxyRegion: "Unknown Regions", origin: "Anomaly" },  
{ id: "void_entity", name: "Void Entity", description: "From the void between galaxies. Feed on entropy and decay. Driven by hunger. Terrifying to normal life.", galaxyRegion: "Unknown Regions", origin: "Void" },  
{ id: "time_displaced", name: "Time Displaced", description: "Stuck in wrong time periods. Out of place, confused, potentially dangerous. Carry knowledge of future or past.", galaxyRegion: "Unknown Regions", origin: "Temporal" },

// Satellite Galaxies  
{ id: "satellite_human", name: "Satellite Human", description: "Humans from satellite galaxies. Genetically drifted from main galaxy humans. Distinct cultures and adaptations.", galaxyRegion: "Satellite Galaxies", origin: "Human" },  
{ id: "dwarf_elf", name: "Dwarf Elf", description: "From satellite dwarf galaxies. Short-lived but technologically advanced. Prone to risk-taking.", galaxyRegion: "Satellite Galaxies", origin: "Humanoid" },  
{ id: "satellite_synthetic", name: "Satellite Synthetic", description: "AI from satellite galaxy civilizations. Different design philosophy from core synthetics. More experimental.", galaxyRegion: "Satellite Galaxies", origin: "Artificial" },  
{ id: "dark_worlder", name: "Dark Worlder", description: "From lightless satellite worlds. No eyes, advanced other senses. Echolocation, thermal sensitivity. Mysterious.", galaxyRegion: "Satellite Galaxies", origin: "Humanoid" },  
{ id: "high_gravity_native", name: "High Gravity Native", description: "From dense satellite galaxy worlds. Extremely dense and strong. Slow but nearly unstoppable.", galaxyRegion: "Satellite Galaxies", origin: "Humanoid" },  
{ id: "low_gravity_native", name: "Low Gravity Native", description: "From sparse satellite galaxy worlds. Tall, fragile, graceful. Natural artists and philosophers.", galaxyRegion: "Satellite Galaxies", origin: "Humanoid" },  
{ id: "radiation_adapted", name: "Radiation Adapted", description: "From high-radiation satellite galaxies. Glowing, mutated, resistant to most forms of energy. Unsettling appearance.", galaxyRegion: "Satellite Galaxies", origin: "Mutated" },  
{ id: "gas_cloud_dweller", name: "Gas Cloud Dweller", description: "From gas-rich satellite galaxies. Float in dense atmospheres. Filter-feed on energy and particles. Peaceful.", galaxyRegion: "Satellite Galaxies", origin: "Gaseous" },  
{ id: "crystalline_entity", name: "Crystalline Entity", description: "From crystal-rich satellite galaxies. Complex crystalline structures, sing in magnetic fields. Long-lived.", galaxyRegion: "Satellite Galaxies", origin: "Crystalline" },  
{ id: "energy_symbiote", name: "Energy Symbiote", description: "Energy beings that bond with hosts. From volatile satellite galaxies. Grant powers but demand energy.", galaxyRegion: "Satellite Galaxies", origin: "Energy" },

// Intergalactic Travelers  
{ id: "wanderer", name: "Wanderer", description: "Nomadic races that travel between galaxies. No fixed home. Highly adaptable, culturally rich. Expert travelers.", galaxyRegion: "Intergalactic", origin: "Nomadic" },  
{ id: "cosmic_sailor", name: "Cosmic Sailor", description: "Navigate between galaxies using cosmic currents. Ancient, wise, reclusive. Share knowledge sparingly.", galaxyRegion: "Intergalactic", origin: "Ancient" },  
{ id: "void_traveler", name: "Void Traveler", description: "Cross the void between galaxies. Adapted to absolute nothingness. Nearly immortal, alien psychology.", galaxyRegion: "Intergalactic", origin: "Void-adapted" },  
{ id: "dimension_hopper", name: "Dimension Hopper", description: "Use dimensional shortcuts for travel. Can access parallel realities. Unpredictable and potentially dangerous.", galaxyRegion: "Intergalactic", origin: "Dimensional" },  
{ id: "time_lord", name: "Time Lord", description: "Move through time as well as space. See all possibilities. Manipulate timelines. Burdened by knowledge.", galaxyRegion: "Intergalactic", origin: "Temporal" },  
{ id: "energy_collector", name: "Energy Collector", description: "Gather energy across the universe. Massive, slow, powerful. Feed on stars and cosmic phenomena.", galaxyRegion: "Intergalactic", origin: "Cosmic" },  
{ id: "seed_planter", name: "Seed Planter", description: "Spread life across galaxies. Ancient, patient, benevolent. Terraform worlds and nurture ecosystems.", galaxyRegion: "Intergalactic", origin: "Precursor" },  
{ id: "cosmic_predator", name: "Cosmic Predator", description: "Hunt across galaxies. Apex predators of space. Terrifying, unstoppable, driven by hunger.", galaxyRegion: "Intergalactic", origin: "Predatory" },  
{ id: "knowledge_seeker", name: "Knowledge Seeker", description: "Collect information and artifacts. Obsessive scholars of the universe. Trade knowledge for resources.", galaxyRegion: "Intergalactic", origin: "Scholar" },  
{ id: "entropy_bringer", name: "Entropy Bringer", description: "Accelerate universal decay. Agents of eventual heat death. Inevitable, patient, unstoppable.", galaxyRegion: "Intergalactic", origin: "Cosmic" },

// Special Cases  
{ id: "hybrid", name: "Hybrid", description: "Mixed-race individuals. Varying traits from parent races. Often face identity issues. Bridge between cultures.", galaxyRegion: "Various", origin: "Mixed" },  
{ id: "engineered", name: "Engineered", description: "Artificially created beings. Designed for specific purposes. Struggle with purpose beyond design.", galaxyRegion: "Various", origin: "Artificial" },  
{ id: "mutated", name: "Mutated", description: "Changed by radiation, chemicals, or experiments. Unpredictable abilities and appearances. Often outcasts.", galaxyRegion: "Various", origin: "Mutated" },  
{ id: "ascended", name: "Ascended", description: "Transcended physical form. Pure consciousness or energy. Nearly godlike. Rare and mysterious.", galaxyRegion: "Various", origin: "Transcended" },  
{ id: "cursed", name: "Cursed", description: "Affected by supernatural or technological curses. Altered form and abilities. Seek redemption or cure.", galaxyRegion: "Various", origin: "Cursed" },  
{ id: "blessed", name: "Blessed", description: "Granted powers by higher beings or artifacts. Enhanced abilities but often with代价. Chosen for destiny.", galaxyRegion: "Various", origin: "Blessed" },  
{ id: "reborn", name: "Reborn", description: "Cheat death through technology or magic. Clones, transfers, or resurrection. Identity issues common.", galaxyRegion: "Various", origin: "Undead" },  
{ id: "fused", name: "Fused", description: "Multiple beings merged into one. Conflicting minds, combined abilities. Struggle for dominance or harmony.", galaxyRegion: "Various", origin: "Fused" },  
{ id: "fragmented", name: "Fragmented", description: "Split into multiple entities. Share consciousness but separate bodies. Can coordinate perfectly.", galaxyRegion: "Various", origin: "Fragmented" },  
{ id: "unique", name: "Unique", description: "One-of-a-kind beings. No others of their kind. Often experiments or anomalies. Lonely but special.", galaxyRegion: "Various", origin: "Unique" }  
];