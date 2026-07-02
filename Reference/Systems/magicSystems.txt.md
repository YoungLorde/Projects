export interface MagicSystem {  
id: string;  
name: string;  
type: 'immortal' | 'runic' | 'aether';  
description: string;  
source: string;  
powerLevels: {  
level: number;  
name: string;  
description: string;  
abilities: string[];  
}[];  
cultivationStages: {  
stage: number;  
name: string;  
description: string;  
requirements: string[];  
breakthrough: string;  
}[];  
techniques: {  
id: string;  
name: string;  
type: string;  
description: string;  
requirements: number;  
effects: string[];  
}[];  
resources: {  
name: string;  
type: string;  
rarity: string;  
uses: string[];  
}[];  
}

export const magicSystems: MagicSystem[] = [  
{  
id: 'immortal_cultivation',  
name: 'Immortal Cultivation',  
type: 'immortal',  
description: 'Ancient art of refining qi to achieve immortality and godhood',  
source: 'Heaven and Earth Qi',  
powerLevels: [  
{  
level: 1,  
name: 'Qi Gathering',  
description: 'Foundation stage - sensing and gathering qi',  
abilities: ['Qi sensing', 'Basic cultivation', 'Body strengthening', 'Extended lifespan']  
},  
{  
level: 2,  
name: 'Foundation Establishment',  
description: 'Building qi foundation in dantian',  
abilities: ['Qi manipulation', 'Basic techniques', 'Flight', 'Qi weapons']  
},  
{  
level: 3,  
name: 'Core Formation',  
description: 'Forming spiritual core',  
abilities: ['Domain creation', 'Soul attacks', 'Advanced techniques', 'Spatial manipulation']  
},  
{  
level: 4,  
name: 'Nascent Soul',  
description: 'Forming nascent immortal soul',  
abilities: ['Soul projection', 'Reincarnation', 'Law comprehension', 'Reality influence']  
},  
{  
level: 5,  
name: 'Immortal Ascension',  
description: 'True immortality achieved',  
abilities: ['Immortality', 'Law mastery', 'World creation', 'Omniscience']  
}  
],  
cultivationStages: [  
{  
stage: 1,  
name: 'Mortal',  
description: 'Beginning of cultivation journey',  
requirements: ['Spiritual roots', 'Cultivation manual', 'Qi source'],  
breakthrough: 'Open meridians and sense qi'  
},  
{  
stage: 2,  
name: 'Qi Condensation',  
description: 'Condensing qi in dantian',  
requirements: ['Qi gathering technique', 'Purified qi', 'Mental focus'],  
breakthrough: 'Form liquid qi core'  
},  
{  
stage: 3,  
name: 'Foundation',  
description: 'Building cultivation foundation',  
requirements: ['Liquid qi core', 'Foundation pill', 'Enlightenment'],  
breakthrough: 'Compress qi into solid foundation'  
},  
{  
stage: 4,  
name: 'Golden Core',  
description: 'Forming golden core of power',  
requirements: ['Solid foundation', 'Heavenly tribulation', 'Karma purification'],  
breakthrough: 'Survive heavenly tribulation'  
},  
{  
stage: 5,  
name: 'Nascent Soul',  
description: 'Birth of immortal soul',  
requirements: ['Golden core', 'Soul formation technique', 'Spiritual enlightenment'],  
breakthrough: 'Form nascent soul from core'  
}  
],  
techniques: [  
{  
id: 'qi_gathering',  
name: 'Qi Gathering Technique',  
type: 'Foundation',  
description: 'Basic technique to absorb qi from environment',  
requirements: 1,  
effects: ['Qi absorption', 'Body purification', 'Extended lifespan']  
},  
{  
id: 'sword_intent',  
name: 'Sword Intent',  
type: 'Combat',  
description: 'Infuse sword with qi and will',  
requirements: 2,  
effects: ['Sword qi projection', 'Intent pressure', 'Cutting space']  
},  
{  
id: 'domain_creation',  
name: 'Domain Creation',  
type: 'Advanced',  
description: 'Create personal domain of power',  
requirements: 3,  
effects: ['Reality control', 'Law manifestation', 'Absolute defense']  
},  
{  
id: 'soul_formation',  
name: 'Soul Formation',  
type: 'Spiritual',  
description: 'Form and strengthen immortal soul',  
requirements: 4,  
effects: ['Soul projection', 'Reincarnation', 'Soul attacks']  
}  
],  
resources: [  
{  
name: 'Spirit Stones',  
type: 'Energy',  
rarity: 'Common',  
uses: ['Cultivation fuel', 'Formation power', 'Trade currency']  
},  
{  
name: 'Foundation Pills',  
type: 'Consumable',  
rarity: 'Uncommon',  
uses: ['Breakthrough aid', 'Qi purification', 'Foundation building']  
},  
{  
name: 'Heavenly Tribulation Lightning',  
type: 'Natural',  
rarity: 'Rare',  
uses: ['Body tempering', 'Soul forging', 'Law comprehension']  
},  
{  
name: 'Immortal Herbs',  
type: 'Material',  
rarity: 'Epic',  
uses: ['Pill crafting', 'Breakthrough aid', 'Life extension']  
}  
]  
},  
{  
id: 'rune_magic',  
name: 'Runic Magic',  
type: 'runic',  
description: 'Ancient system of magical symbols and patterns',  
source: 'Universal language of creation',  
powerLevels: [  
{  
level: 1,  
name: 'Rune Apprentice',  
description: 'Learning basic rune shapes and meanings',  
abilities: ['Rune identification', 'Basic inscription', 'Simple enchantments', 'Rune reading']  
},  
{  
level: 2,  
name: 'Rune Adept',  
description: 'Combining runes for complex effects',  
abilities: ['Rune combinations', 'Enchanting', 'Ward creation', 'Rune crafting']  
},  
{  
level: 3,  
name: 'Rune Master',  
description: 'Creating new rune patterns',  
abilities: ['Rune invention', 'Complex arrays', 'Living runes', 'Rune golems']  
},  
{  
level: 4,  
name: 'Rune Grandmaster',  
description: 'Understanding rune origins',  
abilities: ['Primordial runes', 'Reality inscription', 'Law encoding', 'Rune worlds']  
},  
{  
level: 5,  
name: 'Rune Sovereign',  
description: 'Becoming one with the rune system',  
abilities: ['Rune divinity', 'Creation rewriting', 'Omnirunic sight', 'Eternal inscription']  
}  
],  
cultivationStages: [  
{  
stage: 1,  
name: 'Initiate',  
description: 'First exposure to runes',  
requirements: ['Rune manual', 'Mana sensitivity', 'Learning aptitude'],  
breakthrough: 'Successfully inscribe first rune'  
},  
{  
stage: 2,  
name: 'Scribe',  
description: 'Practicing rune inscription',  
requirements: ['Basic runes', 'Inscription tools', 'Mana control'],  
breakthrough: 'Create working rune array'  
},  
{  
stage: 3,  
name: 'Weaver',  
description: 'Combining runes into patterns',  
requirements: ['Rune mastery', 'Pattern understanding', 'Spatial awareness'],  
breakthrough: 'Invent new rune combination'  
},  
{  
stage: 4,  
name: 'Architect',  
description: 'Designing complex rune systems',  
requirements: ['Pattern mastery', 'Law knowledge', 'Creative insight'],  
breakthrough: 'Create self-sustaining rune system'  
},  
{  
stage: 5,  
name: 'Origin',  
description: 'Understanding rune origins',  
requirements: ['System mastery', 'Primordial knowledge', 'Enlightenment'],  
breakthrough: 'Comprehend primordial rune'  
}  
],  
techniques: [  
{  
id: 'basic_inscription',  
name: 'Basic Inscription',  
type: 'Foundation',  
description: 'Inscribe simple runes on objects',  
requirements: 1,  
effects: ['Object enhancement', 'Simple enchantments', 'Rune storage']  
},  
{  
id: 'rune_array',  
name: 'Rune Array',  
type: 'Advanced',  
description: 'Create patterns of interconnected runes',  
requirements: 2,  
effects: ['Complex effects', 'Area enchantment', 'Automated systems']  
},  
{  
id: 'living_rune',  
name: 'Living Rune',  
type: 'Master',  
description: 'Create self-aware rune constructs',  
requirements: 3,  
effects: ['Rune golems', 'Autonomous enchantments', 'Rune spirits']  
},  
{  
id: 'primordial_inscription',  
name: 'Primordial Inscription',  
type: 'Transcendent',  
description: 'Inscribe reality-altering runes',  
requirements: 4,  
effects: ['Law alteration', 'Creation editing', 'Reality rewriting']  
}  
],  
resources: [  
{  
name: 'Rune Stones',  
type: 'Material',  
rarity: 'Common',  
uses: ['Rune inscription', 'Mana storage', 'Array components']  
},  
{  
name: 'Mana Crystals',  
type: 'Energy',  
rarity: 'Uncommon',  
uses: ['Power source', 'Rune activation', 'Enchantment fuel']  
},  
{  
name: 'Ancient Tablets',  
type: 'Knowledge',  
rarity: 'Rare',  
uses: ['Rune learning', 'Pattern discovery', 'Ancient techniques']  
},  
{  
name: 'Primordial Essence',  
type: 'Material',  
rarity: 'Legendary',  
uses: ['Origin runes', 'Reality editing', 'Divine inscription']  
}  
]  
},  
{  
id: 'aether_magic',  
name: 'Aether Magic',  
type: 'aether',  
description: 'Manipulation of the fundamental aether energy',  
source: 'Aether realm between dimensions',  
powerLevels: [  
{  
level: 1,  
name: 'Aether Sensitive',  
description: 'Can sense and manipulate aether',  
abilities: ['Aether sensing', 'Basic manipulation', 'Shield creation', 'Minor teleportation']  
},  
{  
level: 2,  
name: 'Aether Weaver',  
description: 'Weaving aether into spells',  
abilities: ['Spell weaving', 'Aether constructs', 'Dimensional sight', 'Aether travel']  
},  
{  
level: 3,  
name: 'Aether Master',  
description: 'Master of aether manipulation',  
abilities: ['Aether domain', 'Reality bending', 'Dimension creation', 'Time manipulation']  
},  
{  
level: 4,  
name: 'Aether Lord',  
description: 'Ruler of aether realms',  
abilities: ['Dimensional lordship', 'Aether sovereignty', 'Law overriding', 'Existence editing']  
},  
{  
level: 5,  
name: 'Aether Sovereign',  
description: 'One with the aether',  
abilities: ['Omnipresence', 'Omniscience', 'Omnipotence', 'Eternal existence']  
}  
],  
cultivationStages: [  
{  
stage: 1,  
name: 'Awakening',  
description: 'First aether sensitivity',  
requirements: ['Aether affinity', 'Mental awakening', 'Soul purity'],  
breakthrough: 'Successfully sense aether'  
},  
{  
stage: 2,  
name: 'Channeling',  
description: 'Channeling aether through body',  
requirements: ['Aether sensitivity', 'Body purification', 'Focus training'],  
breakthrough: 'Form aether channels'  
},  
{  
stage: 3,  
name: 'Weaving',  
description: 'Weaving aether into patterns',  
requirements: ['Aether channels', 'Pattern knowledge', 'Creative ability'],  
breakthrough: 'Create stable aether construct'  
},  
{  
stage: 4,  
name: 'Manifestation',  
description: 'Manifesting aether reality',  
requirements: ['Weaving mastery', 'Willpower', 'Understanding'],  
breakthrough: 'Manifest personal aether domain'  
},  
{  
stage: 5,  
name: 'Ascension',  
description: 'Becoming aether itself',  
requirements: ['Domain mastery', 'Soul transcendence', 'Enlightenment'],  
breakthrough: 'Merge with aether'  
}  
],  
techniques: [  
{  
id: 'aether_sensing',  
name: 'Aether Sensing',  
type: 'Foundation',  
description: 'Sense aether in environment',  
requirements: 1,  
effects: ['Aether detection', 'Energy reading', 'Dimensional sight']  
},  
{  
id: 'aether_shield',  
name: 'Aether Shield',  
type: 'Defense',  
description: 'Create protective aether barrier',  
requirements: 1,  
effects: ['Defense', 'Reflection', 'Absorption']  
},  
{  
id: 'aether_construct',  
name: 'Aether Construct',  
type: 'Creation',  
description: 'Create objects from aether',  
requirements: 2,  
effects: ['Object creation', 'Temporary items', 'Aether tools']  
},  
{  
id: 'dimensional_step',  
name: 'Dimensional Step',  
type: 'Movement',  
description: 'Step between dimensions',  
requirements: 2,  
effects: ['Teleportation', 'Dimension travel', 'Space folding']  
},  
{  
id: 'aether_domain',  
name: 'Aether Domain',  
type: 'Advanced',  
description: 'Create personal aether space',  
requirements: 3,  
effects: ['Reality control', 'Law bending', 'Time manipulation']  
}  
],  
resources: [  
{  
name: 'Aether Crystals',  
type: 'Energy',  
rarity: 'Common',  
uses: ['Aether fuel', 'Spell power', 'Construct material']  
},  
{  
name: 'Dimensional Essence',  
type: 'Material',  
rarity: 'Uncommon',  
uses: ['Dimensional magic', 'Space manipulation', 'Portal creation']  
},  
{  
name: 'Aether Cores',  
type: 'Material',  
rarity: 'Rare',  
uses: ['Power amplification', 'Domain creation', 'Advanced spells']  
},  
{  
name: 'Primordial Aether',  
type: 'Material',  
rarity: 'Legendary',  
uses: ['Reality creation', 'Existence editing', 'Divine power']  
}  
]  
}  
];

export function getMagicSystem(id: string): MagicSystem | undefined {  
return magicSystems.find((system) => system.id === id);  
}

export function getMagicSystemsByType(type: MagicSystem['type']): MagicSystem[] {  
return magicSystems.filter((system) => system.type === type);  
}