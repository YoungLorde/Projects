import { faiths } from './faiths';  
import { type DatabaseEntry } from './storyDatabases';

export interface Civilization {  
id: string;  
name: string;  
knowledgeLevel: number; // 1-10 scale  
population: number;  
technology: number; // 1-10 scale  
magicLevel: number; // 0-10 scale  
currentFaiths: string[];  
}

export function getAvailableFaiths(knowledgeLevel: number): DatabaseEntry[] {  
return faiths.filter((faith) => {  
const minLevel = faith.minKnowledgeLevel || 1;  
return minLevel });  
}

export function getRecommendedFaiths(civilization: Civilization): DatabaseEntry[] {  
const available = getAvailableFaiths(civilization.knowledgeLevel);

// Score faiths based on civilization characteristics  
const scored = available.map((faith) => {  
let score = 0;

// Knowledge level match  
const faithLevel = faith.minKnowledgeLevel || 1;  
if (faithLevel === civilization.knowledgeLevel) score += 10;  
else if (faithLevel < civilization.knowledgeLevel) score += 5;

// Technology level considerations  
if (civilization.technology >= 7) {  
// High tech civilizations prefer complex faiths  
if (faith.category === 'Monotheism' || faith.category === 'Hinduism') score += 5;  
if (faith.category === 'Animism') score -= 5;  
} else if (civilization.technology // Low tech civilizations prefer simple faiths  
if (faith.category === 'Animism' || faith.category === 'Polytheism') score += 5;  
if (faith.category === 'Buddhism' || faith.category === 'Hinduism') score -= 3;  
}

// Magic level considerations  
if (civilization.magicLevel >= 5) {  
// Magical civilizations prefer mystical faiths  
if (faith.category === 'Dao/Tao' || faith.category === 'Buddhism') score += 5;  
if (faith.category === 'Monotheism') score -= 3;  
}

// Population size considerations  
if (civilization.population > 10000000) {  
// Large populations favor organized religions  
if (faith.category === 'Monotheism' || faith.category === 'Hinduism') score += 5;  
if (faith.category === 'Animism') score -= 5;  
} else if (civilization.population < 100000) {  
// Small populations favor animism and local spirits  
if (faith.category === 'Animism' || faith.category === 'Polytheism') score += 5;  
if (faith.category === 'Monotheism') score -= 3;  
}

return { faith, score };  
});

// Sort by score and return top recommendations  
return scored  
.sort((a, b) => b.score - a.score)  
.slice(0, 5)  
.map((item) => item.faith);  
}

export function assignFaith(civilization: Civilization, faithId: string): boolean {  
const faith = faiths.find((f) => f.id === faithId);  
if (!faith) return false;

const minLevel = faith.minKnowledgeLevel || 1;  
if (minLevel > civilization.knowledgeLevel) return false;

// Check if faith is already assigned  
if (civilization.currentFaiths.includes(faithId)) return false;

// Add faith to civilization  
civilization.currentFaiths.push(faithId);  
return true;  
}

export function removeFaith(civilization: Civilization, faithId: string): boolean {  
const index = civilization.currentFaiths.indexOf(faithId);  
if (index === -1) return false;

civilization.currentFaiths.splice(index, 1);  
return true;  
}

export function getFaithCompatibility(faith1Id: string, faith2Id: string): number {  
const faith1 = faiths.find((f) => f.id === faith1Id);  
const faith2 = faiths.find((f) => f.id === faith2Id);  
if (!faith1 || !faith2) return 0;

// Same category: high compatibility  
if (faith1.category === faith2.category) return 80;

// Compatible categories  
const compatiblePairs: Record = {  
'Monotheism': ['Hinduism', 'Buddhism'],  
'Polytheism': ['Hinduism', 'Animism'],  
'Hinduism': ['Buddhism', 'Polytheism', 'Monotheism'],  
'Buddhism': ['Hinduism', 'Dao/Tao', 'Monotheism'],  
'Dao/Tao': ['Buddhism', 'Polytheism'],  
'Animism': ['Polytheism', 'Creed'],  
'Creed': ['Monotheism', 'Animism'],  
};

if (faith1.category && compatiblePairs[faith1.category]?.includes(faith2.category || '')) return 50;

// Incompatible categories  
const incompatiblePairs: Record = {  
'Monotheism': ['Animism', 'Polytheism'],  
'Animism': ['Monotheism', 'Buddhism'],  
};

if (faith1.category && incompatiblePairs[faith1.category]?.includes(faith2.category || '')) return 20;

// Neutral compatibility  
return 40;  
}

export function calculateFaithHarmony(civilization: Civilization): number {  
if (civilization.currentFaiths.length

let totalCompatibility = 0;  
let pairCount = 0;

for (let i = 0; i < civilization.currentFaiths.length; i++) {  
for (let j = i + 1; j < civilization.currentFaiths.length; j++) {  
totalCompatibility += getFaithCompatibility(  
civilization.currentFaiths[i],  
civilization.currentFaiths[j]  
);  
pairCount++;  
}  
}

return pairCount > 0 ? Math.round(totalCompatibility / pairCount) : 100;  
}

export function getFaithProgression(civilization: Civilization): {  
current: DatabaseEntry[];  
available: DatabaseEntry[];  
locked: DatabaseEntry[];  
} {  
const current = civilization.currentFaiths  
.map((id) => faiths.find((f) => f.id === id))  
.filter((f): f is DatabaseEntry => f !== undefined);

const available = getAvailableFaiths(civilization.knowledgeLevel).filter(  
(f) => !civilization.currentFaiths.includes(f.id)  
);

const locked = faiths.filter(  
(f) => (f.minKnowledgeLevel || 1) > civilization.knowledgeLevel  
);

return { current, available, locked };  
}