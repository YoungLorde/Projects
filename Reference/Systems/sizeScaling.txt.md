export interface ScaleLevel {  
id: string;  
name: string;  
description: string;  
baseUnit: string;  
multiplier: number; // Multiplier relative to previous level  
examples: string[];  
typicalPopulation: string;  
typicalArea: string;  
features: string[];  
}

export const scaleLevels: ScaleLevel[] = [  
{  
id: "building",  
name: "Building",  
description: "Single structure or small complex",  
baseUnit: "meters",  
multiplier: 1,  
examples: ["House", "Shop", "Office", "Warehouse", "Temple"],  
typicalPopulation: "1-100",  
typicalArea: "100-10,000 m²",  
features: ["Rooms", "Floors", "Utilities", "Storage"]  
},  
{  
id: "district",  
name: "District",  
description: "Neighborhood or small area within a settlement",  
baseUnit: "hectares",  
multiplier: 100,  
examples: ["Market District", "Residential Block", "Industrial Zone", "Academic Quarter"],  
typicalPopulation: "1,000-10,000",  
typicalArea: "10-100 hectares",  
features: ["Multiple buildings", "Local services", "Community spaces", "Transport links"]  
},  
{  
id: "city",  
name: "City",  
description: "Urban settlement with full infrastructure",  
baseUnit: "km²",  
multiplier: 100,  
examples: ["Metropolis", "Port City", "Fortress City", "Trade Hub"],  
typicalPopulation: "10,000-10,000,000",  
typicalArea: "10-1,000 km²",  
features: ["Districts", "Government", "Defense", "Trade", "Culture", "Education"]  
},  
{  
id: "region",  
name: "Region",  
description: "Geographic area containing multiple cities",  
baseUnit: "km²",  
multiplier: 100,  
examples: ["Province", "Duchy", "State", "Territory"],  
typicalPopulation: "100,000-100,000,000",  
typicalArea: "1,000-100,000 km²",  
features: ["Multiple cities", "Natural resources", "Transport networks", "Regional government"]  
},  
{  
id: "continent",  
name: "Continent",  
description: "Large landmass with diverse ecosystems",  
baseUnit: "km²",  
multiplier: 100,  
examples: ["Continent", "Subcontinent", "Large Island Chain"],  
typicalPopulation: "1,000,000-1,000,000,000",  
typicalArea: "1,000,000-50,000,000 km²",  
features: ["Multiple regions", "Diverse climates", "Major rivers", "Mountain ranges", "Coastlines"]  
},  
{  
id: "planet",  
name: "Planet",  
description: "Celestial body with its own ecosystem",  
baseUnit: "km²",  
multiplier: 10,  
examples: ["Earth-like", "Desert world", "Ocean world", "Gas giant moon"],  
typicalPopulation: "1,000,000-100,000,000,000",  
typicalArea: "500,000,000 km² (surface)",  
features: ["Atmosphere", "Climate zones", "Continents", "Oceans", "Natural satellites"]  
},  
{  
id: "system",  
name: "Solar System",  
description: "Star with orbiting bodies",  
baseUnit: "AU",  
multiplier: 1000,  
examples: ["Single star system", "Binary system", "Trinary system"],  
typicalPopulation: "N/A",  
typicalArea: "50-100 AU diameter",  
features: ["Star(s)", "Planets", "Asteroid belts", "Comets", "Space stations"]  
},  
{  
id: "sector",  
name: "Sector",  
description: "Region of space containing multiple systems",  
baseUnit: "light-years",  
multiplier: 100,  
examples: ["Core sector", "Frontier sector", "Trade corridor"],  
typicalPopulation: "N/A",  
typicalArea: "100-1,000 light-years",  
features: ["Multiple systems", "Trade routes", "Space highways", "Naval bases"]  
},  
{  
id: "galaxy",  
name: "Galaxy",  
description: "Gravitationally bound system of stars",  
baseUnit: "light-years",  
multiplier: 100,  
examples: ["Spiral galaxy", "Elliptical galaxy", "Irregular galaxy"],  
typicalPopulation: "N/A",  
typicalArea: "100,000-300,000 light-years",  
features: ["Billions of stars", "Galactic core", "Spiral arms", "Dark matter halo"]  
},  
{  
id: "cluster",  
name: "Galaxy Cluster",  
description: "Group of galaxies bound by gravity",  
baseUnit: "megaparsecs",  
multiplier: 10,  
examples: ["Local Group", "Virgo Cluster", "Supercluster"],  
typicalPopulation: "N/A",  
typicalArea: "1-10 megaparsecs",  
features: ["Multiple galaxies", "Intergalactic space", "Dark matter", "Cosmic web connections"]  
}  
];

export function getScaleMultiplier(from: string, to: string): number {  
const fromIndex = scaleLevels.findIndex((s) => s.id === from);  
const toIndex = scaleLevels.findIndex((s) => s.id === to);

if (fromIndex === -1 || toIndex === -1) return 1;

let multiplier = 1;  
for (let i = fromIndex; i < toIndex; i++) {  
multiplier *= scaleLevels[i].multiplier;  
}

return multiplier;  
}

export function convertScale(value: number, from: string, to: string): number {  
return value * getScaleMultiplier(from, to);  
}

export function getScaleDescription(scaleId: string): ScaleLevel | undefined {  
return scaleLevels.find((s) => s.id === scaleId);  
}