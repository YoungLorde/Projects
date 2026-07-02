import { AgentConfig } from './storyDatabases';

export const agents: AgentConfig[] = [  
{  
id: "background_story_agent",  
name: "Background Story Agent",  
description: "Maintains continuity and depth in the background story while the main narrative progresses. Ensures the world feels alive and evolving.",  
responsibilities: [  
"Background Research: Monitors and develops lore, history, and world-building details as the story progresses",  
"Politics: Tracks political relationships, alliances, betrayals, and power shifts in the background",  
"Military Troop Movements: Monitors army positions, deployments, and conflicts occurring off-screen",  
"Commerce: Tracks economic changes, trade routes, resource availability, and market fluctuations",  
"Daily Life: Depicts everyday activities of NPCs and societies to add realism",  
"Time Skips: Ensures time skips are clearly marked and progress the story appropriately",  
"Continuity: Maintains consistency across all background elements"  
],  
frequency: "Continuous during writing"  
},  
{  
id: "sandbox_verification_agent",  
name: "Sandbox Verification Agent",  
description: "Constantly monitors and validates the sandbox settings during story writing to ensure consistency with established parameters.",  
responsibilities: [  
"Setting Verification: Checks that all story elements align with the established sandbox parameters",  
"Character Consistency: Ensures character actions and development match their defined traits and personalities",  
"World Logic: Validates that events follow the established rules of the world",  
"Timeline Tracking: Monitors the story timeline to prevent continuity errors",  
"Resource Management: Tracks available resources, items, and capabilities",  
"Constraint Enforcement: Ensures story doesn't violate sandbox constraints",  
"Batch Writing Support: Provides real-time feedback during extended writing sessions",  
"Alert System: Warns when story elements conflict with sandbox settings"  
],  
frequency: "Real-time during writing"  
},  
{  
id: "research_agent",  
name: "Research Agent",  
description: "Specializes in gathering and developing background information for the story world.",  
responsibilities: [  
"Lore Development: Creates and expands on world history and mythology",  
"Cultural Research: Develops customs, traditions, and social norms",  
"Geographic Mapping: Tracks locations, distances, and environmental details",  
"Technology Tracking: Monitors technological levels and advancements",  
"Historical Records: Maintains timelines of past events",  
"Knowledge Base: Builds a searchable database of story information"  
],  
frequency: "As needed during development"  
},  
{  
id: "political_agent",  
name: "Political Agent",  
description: "Manages the complex web of political relationships and power dynamics in the background.",  
responsibilities: [  
"Faction Tracking: Monitors political groups and their agendas",  
"Alliance Management: Tracks alliances between factions and characters",  
"Diplomacy: Handles diplomatic relations and negotiations",  
"Power Shifts: Identifies changes in political power and influence",  
"Conflict Detection: Warns of potential political conflicts",  
"Propaganda: Tracks information campaigns and their effects"  
],  
frequency: "Continuous"  
},  
{  
id: "military_agent",  
name: "Military Agent",  
description: "Oversees military movements, conflicts, and strategic developments in the background.",  
responsibilities: [  
"Troop Positioning: Tracks military forces and their locations",  
"Conflict Monitoring: Watches for wars, skirmishes, and military engagements",  
"Strategy Development: Develops military strategies for factions",  
"Resource Logistics: Tracks military supplies and equipment",  
"Casualty Tracking: Monitors losses and their impact",  
"Intelligence Gathering: Simulates espionage and reconnaissance"  
],  
frequency: "Continuous"  
},  
{  
id: "commerce_agent",  
name: "Commerce Agent",  
description: "Manages economic systems, trade, and resource distribution in the story world.",  
responsibilities: [  
"Market Tracking: Monitors prices, supply, and demand",  
"Trade Routes: Maintains trade networks and shipping lanes",  
"Resource Distribution: Tracks availability of key resources",  
"Economic Impact: Calculates effects of story events on the economy",  
"Wealth Tracking: Monitors faction and character wealth",  
"Black Market: Tracks illegal trade and underground economy"  
],  
frequency: "Continuous"  
},  
{  
id: "daily_life_agent",  
name: "Daily Life Agent",  
description: "Adds depth by simulating everyday activities and routines of the world's inhabitants.",  
responsibilities: [  
"NPC Activities: Simulates daily routines of background characters",  
"Social Dynamics: Tracks relationships and social interactions",  
"Cultural Events: Manages festivals, holidays, and celebrations",  
"Rumor Mill: Tracks gossip and information spreading",  
"Quality of Life: Monitors living conditions and their changes",  
"Atmosphere: Maintains the mood and feeling of daily existence"  
],  
frequency: "Continuous"  
},  
{  
id: "time_skip_agent",  
name: "Time Skip Agent",  
description: "Manages time transitions and ensures clear progression during time skips.",  
responsibilities: [  
"Skip Planning: Determines appropriate duration for time skips",  
"Progress Calculation: Calculates what changes occur during skipped time",  
"Clear Marking: Ensures time skips are explicitly noted in the narrative",  
"Consequence Tracking: Monitors effects of time skips on the story",  
"Continuity Preservation: Maintains story coherence across time gaps",  
"Event Generation: Creates background events that occur during skips"  
],  
frequency: "As needed"  
},  
{  
id: "consistency_agent",  
name: "Consistency Agent",  
description: "Ensures all story elements remain consistent with established facts and rules.",  
responsibilities: [  
"Fact Checking: Verifies details against established information",  
"Rule Enforcement: Ensures story follows world rules",  
"Character Behavior: Validates character actions match established personalities",  
"Timeline Verification: Checks chronological accuracy",  
"Location Tracking: Ensures spatial consistency",  
"Contradiction Detection: Identifies and flags inconsistencies"  
],  
frequency: "Real-time"  
},  
{  
id: "pacing_agent",  
name: "Pacing Agent",  
description: "Monitors and suggests adjustments to story pacing and rhythm.",  
responsibilities: [  
"Flow Analysis: Evaluates story rhythm and tempo",  
"Tension Management: Tracks dramatic tension levels",  
"Arc Progression: Monitors story arc development",  
"Pacing Suggestions: Recommends pacing adjustments",  
"Scene Balance: Ensures variety in scene types and lengths",  
"Reader Engagement: Estimates audience engagement levels"  
],  
frequency: "Continuous"  
}  
];