export interface GalacticPower {  
id: string;  
name: string;  
type: 'empire' | 'federation' | 'republic' | 'hegemony' | 'alliance' | 'collective';  
tier: number; // 1-5 power level  
description: string;  
territory: {  
systems: number;  
sectors: number;  
coreWorlds: string[];  
};  
military: {  
fleetSize: string;  
flagshipClasses: string[];  
groundForces: string;  
};  
economy: {  
gdp: string;  
primaryResources: string[];  
tradeRoutes: number;  
};  
technology: {  
level: number; // 1-10  
specialties: string[];  
};  
politics: {  
government: string;  
leader: string;  
stability: number; // 0-100  
allies: string[];  
enemies: string[];  
};  
culture: {  
dominantSpecies: string[];  
values: string[];  
arts: string[];  
};  
}

export interface GalaxyCluster {  
id: string;  
name: string;  
type: 'spiral' | 'elliptical' | 'irregular' | 'dwarf';  
size: string; // in light-years  
galaxyCount: number;  
description: string;  
majorPowers: string[];  
notableFeatures: string[];  
dangers: string[];  
}

export const galacticPowers: GalacticPower[] = [  
{  
id: 'terran_federation',  
name: 'Terran Federation',  
type: 'federation',  
tier: 4,  
description: 'Human-led federation spanning multiple sectors, known for diplomacy and trade',  
territory: {  
systems: 500,  
sectors: 12,  
coreWorlds: ['Earth', 'Mars Colony', 'Centauri Prime', 'New Terra']  
},  
military: {  
fleetSize: '2,500 capital ships',  
flagshipClasses: ['Enterprise-class', 'Defiant-class', 'Dreadnought'],  
groundForces: '50 million personnel'  
},  
economy: {  
gdp: '500 quadrillion credits',  
primaryResources: ['Technology', 'Agriculture', 'Manufacturing', 'Services'],  
tradeRoutes: 500  
},  
technology: {  
level: 8,  
specialties: ['FTL travel', 'Shields', 'Medical tech', 'AI']  
},  
politics: {  
government: 'Representative Democracy',  
leader: 'President Sarah Chen',  
stability: 75,  
allies: ['Vulcan Alliance', 'Andorian Empire'],  
enemies: ['Romulan Star Empire', 'Klingon Empire']  
},  
culture: {  
dominantSpecies: ['Human', 'Vulcan', 'Andorian'],  
values: ['Freedom', 'Diplomacy', 'Exploration', 'Unity'],  
arts: ['Music', 'Literature', 'Holographic entertainment', 'Sports']  
}  
},  
{  
id: 'klingon_empire',  
name: 'Klingon Empire',  
type: 'empire',  
tier: 4,  
description: 'Warrior civilization with strong military tradition and honor code',  
territory: {  
systems: 300,  
sectors: 8,  
coreWorlds: ['Qo\'noS', 'Boreth', 'Ty\'Gokor']  
},  
military: {  
fleetSize: '3,000 capital ships',  
flagshipClasses: ['Bird of Prey', 'Battlecruiser', 'Vor\'cha'],  
groundForces: '100 million personnel'  
},  
economy: {  
gdp: '300 quadrillion credits',  
primaryResources: ['Weapons', 'Ships', 'Minerals', ' slaves'],  
tradeRoutes: 200  
},  
technology: {  
level: 7,  
specialties: ['Weapons', 'Cloaking', 'Ships', 'Combat']  
},  
politics: {  
government: 'Absolute Monarchy',  
leader: 'Chancellor Martok',  
stability: 60,  
allies: ['Romulan Star Empire'],  
enemies: ['Terran Federation', 'Cardassian Union']  
},  
culture: {  
dominantSpecies: ['Klingon'],  
values: ['Honor', 'Combat', 'Loyalty', 'Strength'],  
arts: ['Opera', 'Battle songs', 'Weapon crafting', 'Martial arts']  
}  
},  
{  
id: 'romulan_star_empire',  
name: 'Romulan Star Empire',  
type: 'empire',  
tier: 4,  
description: 'Secretive and manipulative empire with advanced cloaking technology',  
territory: {  
systems: 250,  
sectors: 6,  
coreWorlds: ['Romulus', 'Remus', 'Ch\'Rihan']  
},  
military: {  
fleetSize: '2,000 capital ships',  
flagshipClasses: ['Warbird', 'D\'deridex', 'Scimitar'],  
groundForces: '40 million personnel'  
},  
economy: {  
gdp: '350 quadrillion credits',  
primaryResources: ['Technology', 'Espionage', 'Minerals', 'Energy'],  
tradeRoutes: 150  
},  
technology: {  
level: 9,  
specialties: ['Cloaking', 'Espionage', 'Weapons', 'Ships']  
},  
politics: {  
government: 'Authoritarian Republic',  
leader: 'Praetor Tal\'Aura',  
stability: 55,  
allies: ['Klingon Empire'],  
enemies: ['Terran Federation', 'Vulcan Alliance']  
},  
culture: {  
dominantSpecies: ['Romulan', 'Reman'],  
values: ['Secrecy', 'Duty', 'Order', 'Power'],  
arts: ['Poetry', 'Sculpture', 'Music', 'Architecture']  
}  
},  
{  
id: 'covenant_collective',  
name: 'Covenant Collective',  
type: 'collective',  
tier: 5,  
description: 'Hive mind civilization with shared consciousness and rapid expansion',  
territory: {  
systems: 1000,  
sectors: 20,  
coreWorlds: ['Central Hub', 'Nexus Prime', 'Unity Core']  
},  
military: {  
fleetSize: '10,000 capital ships',  
flagshipClasses: ['Assimilation Cube', 'Sphere', 'Diamond'],  
groundForces: '200 million drones'  
},  
economy: {  
gdp: '1 sextillion credits',  
primaryResources: ['Assimilated tech', 'Biomass', 'Energy', 'Raw materials'],  
tradeRoutes: 0  
},  
technology: {  
level: 10,  
specialties: ['Assimilation', 'Adaptation', 'Regeneration', 'Neural networks']  
},  
politics: {  
government: 'Hive Mind',  
leader: 'Central Consciousness',  
stability: 100,  
allies: [],  
enemies: ['All independent civilizations']  
},  
culture: {  
dominantSpecies: ['Assimilated species'],  
values: ['Perfection', 'Unity', 'Efficiency', 'Order'],  
arts: ['None (considered inefficient)']  
}  
},  
{  
id: 'trade_alliance',  
name: 'Interstellar Trade Alliance',  
type: 'alliance',  
tier: 3,  
description: 'Commercial alliance focused on trade and economic cooperation',  
territory: {  
systems: 200,  
sectors: 5,  
coreWorlds: ['Trade Hub Alpha', 'Commerce Prime', 'Market Central']  
},  
military: {  
fleetSize: '500 capital ships',  
flagshipClasses: ['Merchant Cruiser', 'Escort Carrier', 'Patrol Vessel'],  
groundForces: '10 million security forces'  
},  
economy: {  
gdp: '400 quadrillion credits',  
primaryResources: ['Trade goods', 'Currency', 'Services', 'Luxury items'],  
tradeRoutes: 1000  
},  
technology: {  
level: 6,  
specialties: ['Trade', 'Logistics', 'Finance', 'Communication']  
},  
politics: {  
government: 'Corporate Council',  
leader: 'CEO Council',  
stability: 70,  
allies: ['Terran Federation', 'Vulcan Alliance'],  
enemies: ['Pirate factions']  
},  
culture: {  
dominantSpecies: ['Various merchant species'],  
values: ['Profit', 'Commerce', 'Negotiation', 'Innovation'],  
arts: ['Luxury goods', 'Fashion', 'Entertainment', 'Architecture']  
}  
},  
{  
id: 'ancient_guardians',  
name: 'Ancient Guardians',  
type: 'hegemony',  
tier: 5,  
description: 'Ancient civilization with god-like technology, maintaining galactic balance',  
territory: {  
systems: 50,  
sectors: 2,  
coreWorlds: ['Sanctuary', 'Oculus', 'Eternity']  
},  
military: {  
fleetSize: '100 capital ships (god-tier)',  
flagshipClasses: ['Worldship', 'Dreadnought', 'Reality Anchor'],  
groundForces: '1 million elite guardians'  
},  
economy: {  
gdp: 'Unknown (post-scarcity)',  
primaryResources: ['Dyson sphere energy', 'Matter replication', 'Time manipulation'],  
tradeRoutes: 0  
},  
technology: {  
level: 10,  
specialties: ['Reality manipulation', 'Time travel', 'Dimensional travel', 'Energy mastery']  
},  
politics: {  
government: 'Council of Ancients',  
leader: 'The First',  
stability: 100,  
allies: [],  
enemies: ['None (above conflict)']  
},  
culture: {  
dominantSpecies: ['Ancient race'],  
values: ['Balance', 'Wisdom', 'Non-interference', 'Preservation'],  
arts: ['Cosmic art', 'Temporal music', 'Reality sculptures', 'Memory preservation']  
}  
}  
];

export const galaxyClusters: GalaxyCluster[] = [  
{  
id: 'local_group',  
name: 'Local Group',  
type: 'irregular',  
size: '10 million light-years',  
galaxyCount: 54,  
description: 'Our local galactic neighborhood containing the Milky Way and Andromeda',  
majorPowers: ['Terran Federation', 'Klingon Empire', 'Romulan Star Empire'],  
notableFeatures: ['Milky Way', 'Andromeda Galaxy', 'Triangulum', 'Magellanic Clouds'],  
dangers: ['Supernova remnants', 'Black holes', 'Gamma ray bursts']  
},  
{  
id: 'virgo_supercluster',  
name: 'Virgo Supercluster',  
type: 'irregular',  
size: '110 million light-years',  
galaxyCount: 47000,  
description: 'Massive supercluster containing our Local Group and thousands of other galaxies',  
majorPowers: ['Ancient Guardians', 'Covenant Collective'],  
notableFeatures: ['Virgo Cluster', 'Coma Cluster', 'Centaurus Cluster', 'Fornax Cluster'],  
dangers: ['Galactic collisions', 'Dark matter concentrations', 'Gravitational anomalies']  
},  
{  
id: 'laniakea_supercluster',  
name: 'Laniakea Supercluster',  
type: 'irregular',  
size: '500 million light-years',  
galaxyCount: 100000,  
description: 'Supercluster containing Virgo and surrounding galaxy clusters',  
majorPowers: ['Ancient Guardians'],  
notableFeatures: ['Great Attractor', 'Norma Cluster', 'Hydra-Centaurus Supercluster'],  
dangers: ['Great Attractor gravitational pull', 'Cosmic voids', 'Dark energy effects']  
},  
{  
id: 'shapley_supercluster',  
name: 'Shapley Supercluster',  
type: 'irregular',  
size: '650 million light-years',  
galaxyCount: 8000,  
description: 'Massive concentration of galaxies, largest known structure',  
majorPowers: ['Unknown (unexplored)'],  
notableFeatures: ['Shapley Concentration', 'Great Wall', 'Supercluster core'],  
dangers: ['Extreme gravitational forces', 'Uncharted territories', 'Ancient anomalies']  
},  
{  
id: 'bootes_void',  
name: 'Boötes Void',  
type: 'dwarf',  
size: '330 million light-years',  
galaxyCount: 60,  
description: 'Enormous cosmic void with very few galaxies',  
majorPowers: ['None'],  
notableFeatures: ['Cosmic emptiness', 'Isolated galaxies', 'Dark matter void'],  
dangers: ['Isolation', 'Resource scarcity', 'Unknown phenomena']  
}  
];

export function getGalacticPower(id: string): GalacticPower | undefined {  
return galacticPowers.find((power) => power.id === id);  
}

export function getGalaxyCluster(id: string): GalaxyCluster | undefined {  
return galaxyClusters.find((cluster) => cluster.id === id);  
}

export function getPowersByTier(tier: number): GalacticPower[] {  
return galacticPowers.filter((power) => power.tier === tier);  
}

export function getPowersByType(type: GalacticPower['type']): GalacticPower[] {  
return galacticPowers.filter((power) => power.type === type);  
}