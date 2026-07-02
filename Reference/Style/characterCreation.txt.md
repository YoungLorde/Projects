export interface CharacterClass {  
id: string;  
name: string;  
description: string;  
primaryStats: string[];  
secondaryStats: string[];  
startingSkills: string[];  
equipment: string[];  
role: 'combat' | 'magic' | 'stealth' | 'support' | 'social' | 'craft';  
}

export interface Skill {  
id: string;  
name: string;  
description: string;  
category: 'combat' | 'magic' | 'stealth' | 'social' | 'craft' | 'knowledge';  
levels: {  
level: number;  
name: string;  
description: string;  
}[];  
}

export interface Equipment {  
id: string;  
name: string;  
type: 'weapon' | 'armor' | 'accessory' | 'tool' | 'consumable';  
rarity: 'common' | 'uncommon' | 'rare' | 'epic' | 'legendary';  
description: string;  
stats: Record;  
}

export interface StartingLocation {  
id: string;  
name: string;  
description: string;  
type: 'city' | 'village' | 'wilderness' | 'dungeon' | 'fortress' | 'academy';  
benefits: string[];  
challenges: string[];  
availableResources: string[];  
}

export interface Companion {  
id: string;  
name: string;  
species: string;  
role: string;  
description: string;  
abilities: string[];  
personality: string;  
loyalty: number;  
}

export const characterClasses: CharacterClass[] = [  
{  
id: 'warrior',  
name: 'Warrior',  
description: 'Master of martial combat and physical prowess',  
primaryStats: ['Strength', 'Vitality'],  
secondaryStats: ['Dexterity', 'Willpower'],  
startingSkills: ['sword_mastery', 'shield_basics', 'intimidation'],  
equipment: ['iron_sword', 'leather_armor', 'wooden_shield'],  
role: 'combat'  
},  
{  
id: 'mage',  
name: 'Mage',  
description: 'Wielder of arcane magic and mystical knowledge',  
primaryStats: ['Intelligence', 'Wisdom'],  
secondaryStats: ['Willpower', 'Charisma'],  
startingSkills: ['arcane_basics', 'mana_control', 'spellcraft'],  
equipment: ['apprentice_staff', 'scholar_robes', 'mana_potion'],  
role: 'magic'  
},  
{  
id: 'rogue',  
name: 'Rogue',  
description: 'Master of stealth, precision, and guile',  
primaryStats: ['Dexterity', 'Agility'],  
secondaryStats: ['Perception', 'Charisma'],  
startingSkills: ['stealth_basics', 'lockpicking', 'sleight_of_hand'],  
equipment: ['dagger', 'leather_armor', 'thieves_tools'],  
role: 'stealth'  
},  
{  
id: 'cleric',  
name: 'Cleric',  
description: 'Divine servant with healing and protective powers',  
primaryStats: ['Wisdom', 'Charisma'],  
secondaryStats: ['Willpower', 'Vitality'],  
startingSkills: ['divine_magic', 'healing_basics', 'faith'],  
equipment: ['mace', 'chainmail', 'holy_symbol'],  
role: 'support'  
},  
{  
id: 'ranger',  
name: 'Ranger',  
description: 'Expert hunter and tracker of the wild',  
primaryStats: ['Dexterity', 'Perception'],  
secondaryStats: ['Agility', 'Vitality'],  
startingSkills: ['archery', 'tracking', 'survival'],  
equipment: ['shortbow', 'leather_armor', 'hunting_knife'],  
role: 'combat'  
},  
{  
id: 'bard',  
name: 'Bard',  
description: 'Inspiring performer and master of lore',  
primaryStats: ['Charisma', 'Intelligence'],  
secondaryStats: ['Dexterity', 'Wisdom'],  
startingSkills: ['performance', 'persuasion', 'lore'],  
equipment: ['lute', 'travel_clothes', 'dagger'],  
role: 'social'  
},  
{  
id: 'paladin',  
name: 'Paladin',  
description: 'Holy warrior combining martial and divine power',  
primaryStats: ['Strength', 'Charisma'],  
secondaryStats: ['Willpower', 'Vitality'],  
startingSkills: ['divine_magic', 'sword_mastery', 'leadership'],  
equipment: ['holy_sword', 'plate_armor', 'holy_symbol'],  
role: 'combat'  
},  
{  
id: 'monk',  
name: 'Monk',  
description: 'Disciplined martial artist with inner power',  
primaryStats: ['Agility', 'Willpower'],  
secondaryStats: ['Dexterity', 'Perception'],  
startingSkills: ['unarmed_combat', 'meditation', 'discipline'],  
equipment: ['monk_robes', 'prayer_beads', 'bo_staff'],  
role: 'combat'  
},  
{  
id: 'druid',  
name: 'Druid',  
description: 'Guardian of nature with shapeshifting abilities',  
primaryStats: ['Wisdom', 'Vitality'],  
secondaryStats: ['Intelligence', 'Perception'],  
startingSkills: ['nature_magic', 'shapeshifting', 'herbalism'],  
equipment: ['druid_staff', 'leather_armor', 'herb_pouch'],  
role: 'magic'  
},  
{  
id: 'necromancer',  
name: 'Necromancer',  
description: 'Master of death and dark magic',  
primaryStats: ['Intelligence', 'Willpower'],  
secondaryStats: ['Charisma', 'Perception'],  
startingSkills: ['death_magic', 'summoning', 'soul_manipulation'],  
equipment: ['bone_staff', 'dark_robes', 'soul_gem'],  
role: 'magic'  
},  
{  
id: 'alchemist',  
name: 'Alchemist',  
description: 'Scientific magic user and potion brewer',  
primaryStats: ['Intelligence', 'Dexterity'],  
secondaryStats: ['Perception', 'Wisdom'],  
startingSkills: ['potion_brewing', 'transmutation', 'chemistry'],  
equipment: ['alchemists_kit', 'lab_coat', 'potion_vials'],  
role: 'craft'  
},  
{  
id: 'engineer',  
name: 'Engineer',  
description: 'Builder of mechanical devices and inventions',  
primaryStats: ['Intelligence', 'Dexterity'],  
secondaryStats: ['Perception', 'Strength'],  
startingSkills: ['mechanics', 'construction', 'invention'],  
equipment: ['toolkit', 'blueprints', 'wrench'],  
role: 'craft'  
}  
];

export const skills: Skill[] = [  
{  
id: 'sword_mastery',  
name: 'Sword Mastery',  
description: 'Proficiency with bladed weapons',  
category: 'combat',  
levels: [  
{ level: 1, name: 'Novice', description: 'Basic sword handling' },  
{ level: 2, name: 'Apprentice', description: 'Can perform basic techniques' },  
{ level: 3, name: 'Expert', description: 'Advanced combat maneuvers' },  
{ level: 4, name: 'Master', description: 'Legendary swordsmanship' },  
{ level: 5, name: 'Grandmaster', description: 'Unmatched blade mastery' }  
]  
},  
{  
id: 'arcane_basics',  
name: 'Arcane Basics',  
description: 'Fundamental magical knowledge',  
category: 'magic',  
levels: [  
{ level: 1, name: 'Novice', description: 'Can sense magical energy' },  
{ level: 2, name: 'Apprentice', description: 'Basic spell casting' },  
{ level: 3, name: 'Expert', description: 'Complex magical workings' },  
{ level: 4, name: 'Master', description: 'Powerful spell mastery' },  
{ level: 5, name: 'Archmage', description: 'Reality-warping magic' }  
]  
},  
{  
id: 'stealth_basics',  
name: 'Stealth',  
description: 'Ability to move unseen and unheard',  
category: 'stealth',  
levels: [  
{ level: 1, name: 'Novice', description: 'Basic hiding' },  
{ level: 2, name: 'Apprentice', description: 'Silent movement' },  
{ level: 3, name: 'Expert', description: 'Shadow blending' },  
{ level: 4, name: 'Master', description: 'Vanishing act' },  
{ level: 5, name: 'Ghost', description: 'Perfect invisibility' }  
]  
},  
{  
id: 'persuasion',  
name: 'Persuasion',  
description: 'Ability to influence others',  
category: 'social',  
levels: [  
{ level: 1, name: 'Novice', description: 'Basic convincing' },  
{ level: 2, name: 'Apprentice', description: 'Skilled negotiation' },  
{ level: 3, name: 'Expert', description: 'Master diplomat' },  
{ level: 4, name: 'Master', description: 'Silver tongue' },  
{ level: 5, name: 'Legend', description: 'Irresistible charm' }  
]  
},  
{  
id: 'potion_brewing',  
name: 'Potion Brewing',  
description: 'Creating magical consumables',  
category: 'craft',  
levels: [  
{ level: 1, name: 'Novice', description: 'Simple mixtures' },  
{ level: 2, name: 'Apprentice', description: 'Basic potions' },  
{ level: 3, name: 'Expert', description: 'Complex brews' },  
{ level: 4, name: 'Master', description: 'Legendary elixirs' },  
{ level: 5, name: 'Alchemist', description: 'Transmutation mastery' }  
]  
},  
{  
id: 'tracking',  
name: 'Tracking',  
description: 'Following trails and signs',  
category: 'knowledge',  
levels: [  
{ level: 1, name: 'Novice', description: 'Basic trail reading' },  
{ level: 2, name: 'Apprentice', description: 'Animal tracking' },  
{ level: 3, name: 'Expert', description: 'Expert hunter' },  
{ level: 4, name: 'Master', description: 'Legendary tracker' },  
{ level: 5, name: 'Ranger', description: 'Nature awareness' }  
]  
}  
];

export const equipment: Equipment[] = [  
{  
id: 'iron_sword',  
name: 'Iron Sword',  
type: 'weapon',  
rarity: 'common',  
description: 'Standard iron blade',  
stats: { damage: 10, speed: 5 }  
},  
{  
id: 'steel_sword',  
name: 'Steel Sword',  
type: 'weapon',  
rarity: 'uncommon',  
description: 'High-quality steel blade',  
stats: { damage: 15, speed: 6 }  
},  
{  
id: 'flame_blade',  
name: 'Flame Blade',  
type: 'weapon',  
rarity: 'rare',  
description: 'Sword enchanted with fire',  
stats: { damage: 20, fireDamage: 10, speed: 5 }  
},  
{  
id: 'leather_armor',  
name: 'Leather Armor',  
type: 'armor',  
rarity: 'common',  
description: 'Basic leather protection',  
stats: { defense: 5, agility: 0 }  
},  
{  
id: 'chainmail',  
name: 'Chainmail',  
type: 'armor',  
rarity: 'uncommon',  
description: 'Interlocked metal rings',  
stats: { defense: 10, agility: -2 }  
},  
{  
id: 'plate_armor',  
name: 'Plate Armor',  
type: 'armor',  
rarity: 'rare',  
description: 'Full metal plate protection',  
stats: { defense: 20, agility: -5 }  
},  
{  
id: 'mana_potion',  
name: 'Mana Potion',  
type: 'consumable',  
rarity: 'common',  
description: 'Restores magical energy',  
stats: { manaRestore: 50 }  
},  
{  
id: 'health_potion',  
name: 'Health Potion',  
type: 'consumable',  
rarity: 'common',  
description: 'Restores health',  
stats: { healthRestore: 50 }  
}  
];

export const startingLocations: StartingLocation[] = [  
{  
id: 'capital_city',  
name: 'Capital City',  
description: 'Grand metropolis at the heart of the kingdom',  
type: 'city',  
benefits: ['Access to guilds', 'Markets', 'Training facilities', 'Information networks'],  
challenges: ['High cost of living', 'Crime', 'Political intrigue', 'Crowds'],  
availableResources: ['Weapons', 'Armor', 'Magic items', 'Information', 'Services']  
},  
{  
id: 'frontier_town',  
name: 'Frontier Town',  
description: 'Settlement on the edge of civilization',  
type: 'village',  
benefits: ['Adventure opportunities', 'Lower costs', 'Community bonds', 'Freedom'],  
challenges: ['Limited resources', 'Dangerous wildlife', 'Isolation', 'Basic amenities'],  
availableResources: ['Basic equipment', 'Local knowledge', 'Hunting grounds', 'Trade routes']  
},  
{  
id: 'military_academy',  
name: 'Military Academy',  
description: 'Elite training institution for warriors',  
type: 'academy',  
benefits: ['Expert training', 'Discipline', 'Equipment access', 'Connections'],  
challenges: ['Strict rules', 'Intense competition', 'Limited freedom', 'Hierarchy'],  
availableResources: ['Weapons training', 'Tactical knowledge', 'Physical conditioning', 'Leadership skills']  
},  
{  
id: 'magic_tower',  
name: 'Magic Tower',  
description: 'Ancient tower of arcane study',  
type: 'academy',  
benefits: ['Magical knowledge', 'Spell access', 'Research materials', 'Mentors'],  
challenges: ['Isolation', 'Dangerous experiments', 'Rigorous study', 'Magical hazards'],  
availableResources: ['Spellbooks', 'Magical components', 'Laboratories', 'Ancient texts']  
},  
{  
id: 'forest_village',  
name: 'Forest Village',  
description: 'Settlement deep within ancient woods',  
type: 'village',  
benefits: ['Natural resources', 'Druidic knowledge', 'Harmony with nature', 'Stealth training'],  
challenges: ['Limited technology', 'Wilderness dangers', 'Isolation', 'Supernatural threats'],  
availableResources: ['Herbs', 'Wood', 'Animal companions', 'Nature magic']  
},  
{  
id: 'port_city',  
name: 'Port City',  
description: 'Coastal hub of trade and travel',  
type: 'city',  
benefits: ['Trade access', 'Travel opportunities', 'Cultural diversity', 'Naval skills'],  
challenges: ['Pirates', 'Smuggling', 'Political tension', 'Weather risks'],  
availableResources: ['Exotic goods', 'Ships', 'Sea creatures', 'Foreign knowledge']  
}  
];

export const companions: Companion[] = [  
{  
id: 'faithful_dog',  
name: 'Faithful Dog',  
species: 'Canine',  
role: 'Scout/Companion',  
description: 'Loyal canine companion with keen senses',  
abilities: ['Enhanced smell', 'Tracking', 'Loyalty boost', 'Alertness'],  
personality: 'Loyal, friendly, protective',  
loyalty: 100  
},  
{  
id: 'familiar_cat',  
name: 'Familiar Cat',  
species: 'Feline',  
role: 'Scout/Stealth',  
description: 'Magical cat companion with stealth abilities',  
abilities: ['Stealth', 'Night vision', 'Curiosity', 'Agility'],  
personality: 'Independent, curious, mysterious',  
loyalty: 70  
},  
{  
id: 'battle_horse',  
name: 'Battle Horse',  
species: 'Equine',  
role: 'Mount/Combat',  
description: 'Trained warhorse for combat and travel',  
abilities: ['Speed', 'Carry capacity', 'Combat training', 'Endurance'],  
personality: 'Brave, disciplined, strong',  
loyalty: 85  
},  
{  
id: 'owl_familiar',  
name: 'Owl Familiar',  
species: 'Avian',  
role: 'Scout/Magic',  
description: 'Magical owl with enhanced perception',  
abilities: ['Flight', 'Night vision', 'Silent flight', 'Magic sensitivity'],  
personality: 'Wise, observant, nocturnal',  
loyalty: 80  
},  
{  
id: 'golem_servant',  
name: 'Golem Servant',  
species: 'Construct',  
role: 'Tank/Labor',  
description: 'Animated construct for protection and labor',  
abilities: ['Strength', 'Durability', 'Obedience', 'No fatigue'],  
personality: 'Obedient, silent, unthinking',  
loyalty: 100  
},  
{  
id: 'spirit_guide',  
name: 'Spirit Guide',  
species: 'Spirit',  
role: 'Guide/Magic',  
description: 'Ethereal being with ancient knowledge',  
abilities: ['Invisibility', 'Intangibility', 'Ancient wisdom', 'Magic resistance'],  
personality: 'Mysterious, wise, enigmatic',  
loyalty: 60  
}  
];