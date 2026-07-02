export interface DatabaseEntry {   
id: string;   
name: string;   
description: string;   
tooltip?: string;   
canBeGained?: boolean;   
canBeLost?: boolean;   
category?: string;   
origin?: string;   
galaxyRegion?: string;   
specialties?: string[];   
cost?: number;   
loyalty?: string;   
attributes?: TraitAttribute[];   
specialEffects?: string[];   
minKnowledgeLevel?: number; // For faiths - minimum civilization knowledge required   
frequency?: string; // For agents - how often they appear   
responsibilities?: string[]; // For agents - their responsibilities   
}

export interface TraitAttribute {   
name: string;   
value: number | string;   
type: "stat" | "skill" | "resistance" | "bonus" | "penalty";   
}

export interface SizeScale {   
id: string;   
name: string;   
baseSize: number; // in km or appropriate unit   
ratioToReality: number;   
canScaleInfinitely: boolean;   
maxScale?: number;   
}

export interface GenreEntry {   
id: string;   
name: string;   
description: string;   
examples: string[];   
}

export interface AgentConfig {   
id: string;   
name: string;   
description: string;   
responsibilities: string[];   
frequency: string;   
}

// Re-export all database arrays for easy importing   
export { personalities } from './personalities';   
export { traits } from './traits';   
export { races } from './races';   
export { mercenaries } from './mercenaries';   
export { genres } from './genres';   
export { faiths } from './faiths';   
export { artStyles } from './artStyles';   
export { agents } from './agents';   
export { titles } from './titles';   
export { karmaEvents } from './karmaEvents';