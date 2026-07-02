export interface DepthSystem {  
id: string;  
name: string;  
category: 'infrastructure' | 'authority' | 'laws' | 'realism' | 'science' | 'research';  
description: string;  
levels: {  
level: number;  
name: string;  
description: string;  
effects: string[];  
}[];  
}

export const depthSystems: DepthSystem[] = [  
{  
id: 'infrastructure_urban',  
name: 'Urban Infrastructure',  
category: 'infrastructure',  
description: 'Built environment and utility systems',  
levels: [  
{  
level: 1,  
name: 'Basic',  
description: 'Primitive structures and basic utilities',  
effects: ['Dirt roads', 'Basic shelters', 'Manual labor', 'No sanitation']  
},  
{  
level: 2,  
name: 'Developed',  
description: 'Organized infrastructure with utilities',  
effects: ['Paved roads', 'Plumbing', 'Basic electricity', 'Public services']  
},  
{  
level: 3,  
name: 'Advanced',  
description: 'Modern infrastructure with automation',  
effects: ['Highways', 'Smart grids', 'Mass transit', 'Waste treatment']  
},  
{  
level: 4,  
name: 'Futuristic',  
description: 'High-tech integrated systems',  
effects: ['Magnetic levitation', 'Automated services', 'Energy networks', 'Environmental control']  
},  
{  
level: 5,  
name: 'Transcendent',  
description: 'Reality-warping infrastructure',  
effects: ['Teleportation networks', 'Matter replication', 'Dimensional bridges', 'Time manipulation']  
}  
]  
},  
{  
id: 'infrastructure_communication',  
name: 'Communication Networks',  
category: 'infrastructure',  
description: 'Information and messaging systems',  
levels: [  
{  
level: 1,  
name: 'Verbal',  
description: 'Face-to-face and messenger communication',  
effects: ['Messengers', 'Signal fires', 'Drums', 'Written messages']  
},  
{  
level: 2,  
name: 'Analog',  
description: 'Telegraph and radio communication',  
effects: ['Telegraph', 'Radio', 'Telephone', 'Print media']  
},  
{  
level: 3,  
name: 'Digital',  
description: 'Internet and mobile communication',  
effects: ['Internet', 'Mobile phones', 'Satellite comms', 'Video conferencing']  
},  
{  
level: 4,  
name: 'Neural',  
description: 'Direct brain-to-brain communication',  
effects: ['Neural links', 'Thought sharing', 'Memory transfer', 'Collective consciousness']  
},  
{  
level: 5,  
name: 'Omnipresent',  
description: 'Instant universal communication',  
effects: ['Instant transmission', 'Universal translation', 'Reality awareness', 'Prescience']  
}  
]  
},  
{  
id: 'authority_structure',  
name: 'Authority Structure',  
category: 'authority',  
description: 'Organization of power and governance',  
levels: [  
{  
level: 1,  
name: 'Tribal',  
description: 'Clan-based leadership',  
effects: ['Elders council', 'Family ties', 'Oral tradition', 'Consensus decision']  
},  
{  
level: 2,  
name: 'Feudal',  
description: 'Hierarchical land-based power',  
effects: ['Nobility', 'Vassalage', 'Hereditary rule', 'Oath-based loyalty']  
},  
{  
level: 3,  
name: 'Bureaucratic',  
description: 'Organized administrative systems',  
effects: ['Civil service', 'Legal codes', 'Taxation', 'Standardized procedures']  
},  
{  
level: 4,  
name: 'Democratic',  
description: 'Citizen participation in governance',  
effects: ['Voting rights', 'Separation of powers', 'Civil liberties', 'Public accountability']  
},  
{  
level: 5,  
name: 'Technocratic',  
description: 'AI-optimized governance',  
effects: ['AI administration', 'Predictive governance', 'Resource optimization', 'Automated justice']  
}  
]  
},  
{  
id: 'authority_enforcement',  
name: 'Law Enforcement',  
category: 'authority',  
description: 'Systems for maintaining order',  
levels: [  
{  
level: 1,  
name: 'Vigilante',  
description: 'Community self-policing',  
effects: ['Mob justice', 'Reputation system', 'Community pressure', 'Personal honor']  
},  
{  
level: 2,  
name: 'Constabulary',  
description: 'Organized local enforcement',  
effects: ['Watchmen', 'Local guards', 'Investigations', 'Detention']  
},  
{  
level: 3,  
name: 'Professional',  
description: 'Specialized police forces',  
effects: ['Police departments', 'Detectives', 'Forensics', 'Legal procedures']  
},  
{  
level: 4,  
name: 'Surveillance',  
description: 'Comprehensive monitoring systems',  
effects: ['CCTV networks', 'Data mining', 'Predictive policing', 'Biometric tracking']  
},  
{  
level: 5,  
name: 'Omniscient',  
description: 'Total awareness and control',  
effects: ['Mind reading', 'Precrime prediction', 'Behavior modification', 'Thought policing']  
}  
]  
},  
{  
id: 'laws_complexity',  
name: 'Legal Complexity',  
category: 'laws',  
description: 'Sophistication of legal systems',  
levels: [  
{  
level: 1,  
name: 'Customary',  
description: 'Tradition-based unwritten rules',  
effects: ['Oral traditions', 'Precedent', 'Social norms', 'Community standards']  
},  
{  
level: 2,  
name: 'Codified',  
description: 'Written legal codes',  
effects: ['Written laws', 'Legal documents', 'Courts', 'Judges']  
},  
{  
level: 3,  
name: 'Comprehensive',  
description: 'Detailed legal frameworks',  
effects: ['Constitutions', 'Statutes', 'Regulations', 'Case law']  
},  
{  
level: 4,  
name: 'Specialized',  
description: 'Domain-specific legal systems',  
effects: ['International law', 'Corporate law', 'Space law', 'AI rights']  
},  
{  
level: 5,  
name: 'Universal',  
description: 'Cosmic-scale legal principles',  
effects: ['Universal rights', 'Dimensional law', 'Temporal jurisprudence', 'Existential mandates']  
}  
]  
},  
{  
id: 'realism_physics',  
name: 'Physics Realism',  
category: 'realism',  
description: 'Adherence to physical laws',  
levels: [  
{  
level: 1,  
name: 'Mythic',  
description: 'Magic and supernatural forces dominate',  
effects: ['Magic systems', 'Divine intervention', 'Mythical creatures', 'Supernatural phenomena']  
},  
{  
level: 2,  
name: 'Soft',  
description: 'Physics with some flexibility',  
effects: ['Enhanced abilities', 'Plot armor', 'Coincidence', 'Narrative causality']  
},  
{  
level: 3,  
name: 'Realistic',  
description: 'Earth-like physics',  
effects: ['Newtonian physics', 'Realistic biology', 'Natural consequences', 'Mortal limitations']  
},  
{  
level: 4,  
name: 'Hard',  
description: 'Strict scientific accuracy',  
effects: ['Relativistic effects', 'Quantum mechanics', 'Thermodynamics', 'Cosmic limitations']  
},  
{  
level: 5,  
name: 'Theoretical',  
description: 'Cutting-edge theoretical physics',  
effects: ['String theory', 'Multiverse', 'Time dilation', 'Exotic matter']  
}  
]  
},  
{  
id: 'realism_consequences',  
name: 'Consequence Realism',  
category: 'realism',  
description: 'Permanence and impact of actions',  
levels: [  
{  
level: 1,  
name: 'Cinematic',  
description: 'Dramatic but reversible consequences',  
effects: ['Plot armor', 'Redemption arcs', 'Miraculous recovery', 'Second chances']  
},  
{  
level: 2,  
name: 'Dramatic',  
description: 'Significant but manageable consequences',  
effects: ['Lasting injuries', 'Relationship damage', 'Reputation loss', 'Financial impact']  
},  
{  
level: 3,  
name: 'Gritty',  
description: 'Harsh and often permanent consequences',  
effects: ['Permanent death', 'Trauma', 'Irreversible damage', 'Social fallout']  
},  
{  
level: 4,  
name: 'Brutal',  
description: 'Unforgiving and realistic consequences',  
effects: ['No resurrection', 'Cumulative trauma', 'Systemic oppression', 'Economic ruin']  
},  
{  
level: 5,  
name: 'Nihilistic',  
description: 'Existential and meaningless consequences',  
effects: ['Cosmic indifference', 'Inevitable decay', 'Futility of struggle', 'Existential dread']  
}  
]  
},  
{  
id: 'science_level',  
name: 'Scientific Understanding',  
category: 'science',  
description: 'Knowledge of natural laws',  
levels: [  
{  
level: 1,  
name: 'Observational',  
description: 'Basic observation of patterns',  
effects: ['Seasons', 'Basic astronomy', 'Animal behavior', 'Plant cycles']  
},  
{  
level: 2,  
name: 'Empirical',  
description: 'Systematic experimentation',  
effects: ['Scientific method', 'Classification', 'Basic chemistry', 'Anatomy']  
},  
{  
level: 3,  
name: 'Theoretical',  
description: 'Understanding fundamental principles',  
effects: ['Atomic theory', 'Evolution', 'Relativity', 'Quantum mechanics']  
},  
{  
level: 4,  
name: 'Advanced',  
description: 'Manipulation of fundamental forces',  
effects: ['Nuclear power', 'Genetic engineering', 'Particle physics', 'Advanced materials']  
},  
{  
level: 5,  
name: 'Transcendent',  
description: 'Mastery of universal laws',  
effects: ['Reality manipulation', 'Dimensional travel', 'Time control', 'Matter creation']  
}  
]  
},  
{  
id: 'science_application',  
name: 'Technological Application',  
category: 'science',  
description: 'Practical use of scientific knowledge',  
levels: [  
{  
level: 1,  
name: 'Primitive',  
description: 'Basic tools and techniques',  
effects: ['Stone tools', 'Fire', 'Agriculture', 'Domestication']  
},  
{  
level: 2,  
name: 'Pre-industrial',  
description: 'Mechanical and chemical technology',  
effects: ['Metallurgy', 'Machinery', 'Gunpowder', 'Printing']  
},  
{  
level: 3,  
name: 'Industrial',  
description: 'Mass production and automation',  
effects: ['Assembly lines', 'Electricity', 'Internal combustion', 'Telecommunications']  
},  
{  
level: 4,  
name: 'Information',  
description: 'Digital and networked technology',  
effects: ['Computers', 'Internet', 'AI', 'Biotechnology']  
},  
{  
level: 5,  
name: 'Post-scarcity',  
description: 'Abundance through advanced technology',  
effects: ['Matter replication', 'Energy abundance', 'Life extension', 'Space colonization']  
}  
]  
},  
{  
id: 'research_organization',  
name: 'Research Organization',  
category: 'research',  
description: 'Structure of scientific inquiry',  
levels: [  
{  
level: 1,  
name: 'Individual',  
description: 'Lone scholars and inventors',  
effects: ['Individual discovery', 'Apprenticeship', 'Guilds', 'Patronage']  
},  
{  
level: 2,  
name: 'Institutional',  
description: 'Organized research institutions',  
effects: ['Universities', 'Laboratories', 'Funding agencies', 'Peer review']  
},  
{  
level: 3,  
name: 'Industrial',  
description: 'Corporate and government research',  
effects: ['R&D departments', 'Government labs', 'Military research', 'Corporate labs']  
},  
{  
level: 4,  
name: 'Collaborative',  
description: 'Global research networks',  
effects: ['International cooperation', 'Open science', 'Data sharing', 'Collaborative platforms']  
},  
{  
level: 5,  
name: 'Distributed',  
description: 'AI-augmented universal research',  
effects: ['AI researchers', 'Citizen science', 'Automated discovery', 'Knowledge synthesis']  
}  
]  
},  
{  
id: 'research_funding',  
name: 'Research Funding',  
category: 'research',  
description: 'Resources allocated to research',  
levels: [  
{  
level: 1,  
name: 'Minimal',  
description: 'Basic support for inquiry',  
effects: ['Personal funding', 'Patron support', 'Church sponsorship', 'Royal grants']  
},  
{  
level: 2,  
name: 'Moderate',  
description: 'Significant public and private investment',  
effects: ['Government grants', 'Private investment', 'University endowments', 'Philanthropy']  
},  
{  
level: 3,  
name: 'Substantial',  
description: 'Major research programs',  
effects: ['National programs', 'Corporate R&D', 'Military projects', 'Space programs']  
},  
{  
level: 4,  
name: 'Massive',  
description: 'Society-wide research commitment',  
effects: ['Global initiatives', 'Manhattan projects', 'Crash programs', 'Universal education']  
},  
{  
level: 5,  
name: 'Unlimited',  
description: 'Post-scarcity research capacity',  
effects: ['Automated research', 'Infinite computation', 'Universal knowledge', 'Omniscience']  
}  
]  
}  
];

export function getDepthSystem(id: string): DepthSystem | undefined {  
return depthSystems.find((system) => system.id === id);  
}

export function getDepthSystemsByCategory(category: DepthSystem['category']): DepthSystem[] {  
return depthSystems.filter((system) => system.category === category);  
}