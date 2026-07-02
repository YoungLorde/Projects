export interface KarmaEvent {  
id: string;  
name: string;  
description: string;  
karmaChange: number; // Positive or negative  
butterflyEffect: string; // Description of future impact  
triggerConditions: string | string[];  
severity: "minor" | "moderate" | "major" | "catastrophic" | "miraculous";  
category: "moral" | "social" | "combat" | "exploration" | "commerce" | "mystical" | "political";  
probability: number; // 0-100, chance of triggering when conditions are met  
delayedEffect?: {  
trigger: string;  
effect: string;  
delayTime: string; // e.g., "3 chapters", "1 arc", "5 years"  
};  
}

export const karmaEvents: KarmaEvent[] = [  
// Minor Events  
{  
id: "ke-001",  
name: "Helped a Lost Child",  
description: "You helped a lost child find their way home.",  
karmaChange: 5,  
butterflyEffect: "The child's parent is a minor noble who will remember your kindness years later.",  
triggerConditions: ["encounter lost child", "choose to help"],  
severity: "minor",  
category: "moral",  
probability: 75,  
delayedEffect: {  
trigger: "Meeting the noble in 3 years",  
effect: "Noble provides shelter and resources during a crisis",  
delayTime: "3 years"  
}  
},  
{  
id: "ke-002",  
name: "Ignored a Beggar",  
description: "You walked past a beggar without offering assistance.",  
karmaChange: -2,  
butterflyEffect: "The beggar was actually a disguised cultivator testing character.",  
triggerConditions: ["encounter beggar", "choose to ignore"],  
severity: "minor",  
category: "moral",  
probability: 60,  
delayedEffect: {  
trigger: "Seeking cultivation guidance",  
effect: "Cultivator refuses to teach due to failed test",  
delayTime: "1 year"  
}  
},  
{  
id: "ke-003",  
name: "Saved a Stray Animal",  
description: "You rescued an injured stray animal from the streets.",  
karmaChange: 3,  
butterflyEffect: "The animal is a spirit beast in disguise that will aid you in a future battle.",  
triggerConditions: ["find injured animal", "choose to heal"],  
severity: "minor",  
category: "mystical",  
probability: 55,  
delayedEffect: {  
trigger: "Facing a powerful enemy",  
effect: "Spirit beast intervenes to save your life",  
delayTime: "2 arcs"  
}  
},  
{  
id: "ke-004",  
name: "Stole from a Merchant",  
description: "You stole goods from a merchant's stall.",  
karmaChange: -5,  
butterflyEffect: "The merchant is part of a powerful merchant guild that will blacklist you.",  
triggerConditions: "opportunity to steal",  
severity: "minor",  
category: "commerce",  
probability: 80,  
delayedEffect: {  
trigger: "Attempting to trade in major cities",  
effect: "All merchants refuse to deal with you, forcing black market trade",  
delayTime: "6 months"  
}  
},  
{  
id: "ke-005",  
name: "Defended the Weak",  
description: "You stood up to bullies harassing someone weaker.",  
karmaChange: 8,  
butterflyEffect: "The person you saved is related to a sect elder who will become your patron.",  
triggerConditions: ["witness bullying", "choose to intervene"],  
severity: "minor",  
category: "social",  
probability: 52,  
delayedEffect: {  
trigger: "Applying to a cultivation sect",  
effect: "Sect elder ensures your acceptance despite low talent",  
delayTime: "1 year"  
}  
},  
{  
id: "ke-006",  
name: "Spread a Rumor",  
description: "You spread a damaging rumor about someone.",  
karmaChange: -3,  
butterflyEffect: "The rumor causes a chain reaction that destroys a family's reputation.",  
triggerConditions: ["know damaging information", "choose to spread"],  
severity: "minor",  
category: "social",  
probability: 76,  
delayedEffect: {  
trigger: "Seeking allies in a conflict",  
effect: "Family members refuse to help due to past actions",  
delayTime: "2 years"  
}  
},  
{  
id: "ke-007",  
name: "Returned Lost Item",  
description: "You found and returned a valuable item to its owner.",  
karmaChange: 6,  
butterflyEffect: "The owner is a traveling master who teaches you a technique.",  
triggerConditions: ["find valuable item", "choose to return"],  
severity: "minor",  
category: "moral",  
probability: 55,  
delayedEffect: {  
trigger: "Meeting the master again",  
effect: "Master teaches a rare cultivation technique",  
delayTime: "5 years"  
}  
},  
{  
id: "ke-008",  
name: "Cheated in a Competition",  
description: "You used underhanded methods to win a competition.",  
karmaChange: -7,  
butterflyEffect: "Your victory is discovered, tarnishing your reputation permanently.",  
triggerConditions: ["participate in competition", "choose to cheat"],  
severity: "minor",  
category: "social",  
probability: 85,  
delayedEffect: {  
trigger: "Seeking recognition or honors",  
effect: "Past cheating is revealed, destroying credibility",  
delayTime: "3 years"  
}  
},  
{  
id: "ke-009",  
name: "Showed Mercy to Enemy",  
description: "You spared a defeated enemy instead of killing them.",  
karmaChange: 10,  
butterflyEffect: "The enemy reforms and becomes a loyal ally in your darkest hour.",  
triggerConditions: ["defeat enemy", "choose to spare"],  
severity: "minor",  
category: "moral",  
probability: 35,  
delayedEffect: {  
trigger: "Facing overwhelming odds",  
effect: "Former enemy returns as a powerful ally",  
delayTime: "5 years"  
}  
},  
{  
id: "ke-010",  
name: "Killed a Defenseless Foe",  
description: "You killed an enemy who had surrendered or was helpless.",  
karmaChange: -10,  
butterflyEffect: "The act haunts your cultivation, creating a mental demon.",  
triggerConditions: ["enemy surrenders", "choose to kill"],  
severity: "minor",  
category: "moral",  
probability: 90,  
delayedEffect: {  
trigger: "Attempting a breakthrough",  
effect: "Mental demon manifests, causing breakthrough failure",  
delayTime: "2 years"  
}  
},  
// Moderate Events  
{  
id: "ke-011",  
name: "Betrayed a Friend",  
description: "You betrayed a close friend for personal gain.",  
karmaChange: -25,  
butterflyEffect: "The betrayal destroys your trust network, leaving you alone when you need help most.",  
triggerConditions: ["opportunity for gain", "friend involved"],  
severity: "moderate",  
category: "moral",  
probability: 95,  
delayedEffect: {  
trigger: "Facing a major crisis",  
effect: "No allies come to your aid due to reputation as betrayer",  
delayTime: "1 year"  
}  
},  
{  
id: "ke-012",  
name: "Sacrificed for Others",  
description: "You sacrificed something valuable to help others.",  
karmaChange: 20,  
butterflyEffect: "Your sacrifice inspires others to help you in return.",  
triggerConditions: ["others in need", "have valuable resource"],  
severity: "moderate",  
category: "moral",  
probability: 50,  
delayedEffect: {  
trigger: "Facing overwhelming odds",  
effect: "Inspired allies rally to your side against all expectations",  
delayTime: "6 months"  
}  
},  
{  
id: "ke-013",  
name: "Saved a Village",  
description: "You saved an entire village from destruction.",  
karmaChange: 30,  
butterflyEffect: "The village becomes a sanctuary that shelters you in the future.",  
triggerConditions: ["village in danger", "ability to help"],  
severity: "moderate",  
category: "combat",  
probability: 18,  
delayedEffect: {  
trigger: "Pursued by powerful enemies",  
effect: "Village hides and protects you at great risk to themselves",  
delayTime: "2 years"  
}  
},  
{  
id: "ke-014",  
name: "Destroyed a Village",  
description: "You destroyed an entire village for personal reasons.",  
karmaChange: -50,  
butterflyEffect: "Survivors form a vendetta that spans generations.",  
triggerConditions: ["village exists", "motivation to destroy"],  
severity: "moderate",  
category: "combat",  
probability: 98,  
delayedEffect: {  
trigger: "Any future interaction with descendants",  
effect: "Descendants recognize you and seek revenge",  
delayTime: "10 years"  
}  
},  
{  
id: "ke-015",  
name: "Discovered Ancient Secret",  
description: "You discovered an ancient secret but chose to keep it hidden.",  
karmaChange: 5,  
butterflyEffect: "The secret later saves you from a trap meant for others.",  
triggerConditions: ["find ancient knowledge", "choose to hide"],  
severity: "moderate",  
category: "exploration",  
probability: 30,  
delayedEffect: {  
trigger: "Triggering ancient trap",  
effect: "Secret knowledge allows you to bypass the trap",  
delayTime: "3 years"  
}  
},  
{  
id: "ke-016",  
name: "Shared Ancient Secret",  
description: "You shared an ancient secret with the world.",  
karmaChange: 15,  
butterflyEffect: "The secret causes chaos but also brings unexpected allies.",  
triggerConditions: ["find ancient knowledge", "choose to share"],  
severity: "moderate",  
category: "exploration",  
probability: 45,  
delayedEffect: {  
trigger: "Seeking rare knowledge",  
effect: "Those who benefited from sharing help you in return",  
delayTime: "5 years"  
}  
},  
{  
id: "ke-017",  
name: "Refused Corrupt Bribe",  
description: "You refused a bribe from a corrupt official.",  
karmaChange: 12,  
butterflyEffect: "The official respects your integrity and becomes an informant.",  
triggerConditions: ["offered bribe", "choose to refuse"],  
severity: "moderate",  
category: "political",  
probability: 60,  
delayedEffect: {  
trigger: "Investigating corruption",  
effect: "Official provides crucial evidence anonymously",  
delayTime: "1 year"  
}  
},  
{  
id: "ke-018",  
name: "Accepted Corrupt Bribe",  
description: "You accepted a bribe and looked the other way.",  
karmaChange: -20,  
butterflyEffect: "The bribe ties you to corruption that eventually destroys you.",  
triggerConditions: ["offered bribe", "choose to accept"],  
severity: "moderate",  
category: "political",  
probability: 88,  
delayedEffect: {  
trigger: "Corruption investigation",  
effect: "Your involvement is exposed, ruining your career",  
delayTime: "2 years"  
}  
},  
{  
id: "ke-019",  
name: "Healed a Stranger",  
description: "You used your resources to heal a stranger without expectation of reward.",  
karmaChange: 15,  
butterflyEffect: "The stranger is a powerful healer who teaches you their art.",  
triggerConditions: ["encounter injured stranger", "ability to heal"],  
severity: "moderate",  
category: "mystical",  
probability: 42,  
delayedEffect: {  
trigger: "Need advanced healing",  
effect: "Stranger reveals themselves and teaches secret techniques",  
delayTime: "3 years"  
}  
},  
{  
id: "ke-020",  
name: "Withheld Healing",  
description: "You refused to heal someone when you could have helped.",  
karmaChange: -15,  
butterflyEffect: "The person dies, and their death haunts your cultivation.",  
triggerConditions: ["encounter injured person", "ability to heal", "choose not to"],  
severity: "moderate",  
category: "moral",  
probability: 75,  
delayedEffect: {  
trigger: "Attempting to heal others",  
effect: "Guilt causes your healing arts to become less effective",  
delayTime: "1 year"  
}  
},  
// Major Events  
{  
id: "ke-021",  
name: "Saved a Nation",  
description: "You played a key role in saving an entire nation from destruction.",  
karmaChange: 100,  
butterflyEffect: "The nation grants you citizenship and honors that open doors everywhere.",  
triggerConditions: ["nation in crisis", "ability to help"],  
severity: "major",  
category: "political",  
probability: 15,  
delayedEffect: {  
trigger: "Seeking political influence",  
effect: "Nation's gratitude grants you significant political power",  
delayTime: "5 years"  
}  
},  
{  
id: "ke-022",  
name: "Destroyed a Nation",  
description: "You caused the destruction of an entire nation.",  
karmaChange: -200,  
butterflyEffect: "The destruction creates a power vacuum that leads to chaos affecting the entire region.",  
triggerConditions: ["nation exists", "power to destroy"],  
severity: "major",  
category: "political",  
probability: 99,  
delayedEffect: {  
trigger: "Traveling through the region",  
effect: "Chaos makes travel dangerous and resources scarce",  
delayTime: "10 years"  
}  
},  
{  
id: "ke-023",  
name: "Ascended to Divinity",  
description: "You achieved true divinity through righteous cultivation.",  
karmaChange: 500,  
butterflyEffect: "Your divine status allows you to intervene in mortal affairs at will.",  
triggerConditions: ["reach cultivation peak", "karma threshold met"],  
severity: "major",  
category: "mystical",  
probability: 5,  
delayedEffect: {  
trigger: "Any future crisis",  
effect: "Divine powers allow intervention in mortal affairs",  
delayTime: "immediate"  
}  
},  
{  
id: "ke-024",  
name: "Fallen to Demonhood",  
description: "You fell to demonic cultivation and became a demon lord.",  
karmaChange: -500,  
butterflyEffect: "Your demonic nature attracts enemies and corrupts everything you touch.",  
triggerConditions: ["tempted by demonic path", "choose to embrace"],  
severity: "major",  
category: "mystical",  
probability: 92,  
delayedEffect: {  
trigger: "Any interaction with others",  
effect: "Demonic aura corrupts those around you, creating enemies",  
delayTime: "immediate"  
}  
},  
{  
id: "ke-025",  
name: "Created a Legacy",  
description: "You established a lasting legacy that benefits generations.",  
karmaChange: 75,  
butterflyEffect: "Your legacy creates a network of allies across generations.",  
triggerConditions: ["achieve significant success", "choose to establish legacy"],  
severity: "major",  
category: "social",  
probability: 40,  
delayedEffect: {  
trigger: "Descendants or followers need help",  
effect: "Legacy ensures generations of allies and support",  
delayTime: "20 years"  
}  
},  
{  
id: "ke-026",  
name: "Erased a Legacy",  
description: "You destroyed someone's legacy, erasing their achievements from history.",  
karmaChange: -75,  
butterflyEffect: "The act of erasure creates a void that attracts dark forces.",  
triggerConditions: ["encounter legacy", "choose to destroy"],  
severity: "major",  
category: "social",  
probability: 85,  
delayedEffect: {  
trigger: "Using power in that area",  
effect: "Dark forces drawn to the void interfere with your actions",  
delayTime: "5 years"  
}  
},  
{  
id: "ke-027",  
name: "United Warring Factions",  
description: "You united warring factions into a peaceful alliance.",  
karmaChange: 80,  
butterflyEffect: "The alliance creates a golden age of prosperity.",  
triggerConditions: ["warring factions", "ability to mediate"],  
severity: "major",  
category: "political",  
probability: 25,  
delayedEffect: {  
trigger: "Need resources or allies",  
effect: "Alliance provides unmatched support and resources",  
delayTime: "10 years"  
}  
},  
{  
id: "ke-028",  
name: "Instigated War",  
description: "You instigated a war between peaceful nations for personal gain.",  
karmaChange: -100,  
butterflyEffect: "The war causes suffering that echoes through generations.",  
triggerConditions: ["peaceful nations", "motivation for war"],  
severity: "major",  
category: "political",  
probability: 94,  
delayedEffect: {  
trigger: "Seeking peace or stability",  
effect: "War's aftermath makes peace impossible in the region",  
delayTime: "15 years"  
}  
},  
{  
id: "ke-029",  
name: "Mastered a Forbidden Art",  
description: "You mastered a forbidden art through dedication and control.",  
karmaChange: 25,  
butterflyEffect: "The forbidden art becomes your greatest weapon and defense.",  
triggerConditions: ["find forbidden art", "dedicate to mastery"],  
severity: "major",  
category: "mystical",  
probability: 20,  
delayedEffect: {  
trigger: "Facing impossible odds",  
effect: "Forbidden art provides power to overcome any obstacle",  
delayTime: "3 years"  
}  
},  
{  
id: "ke-030",  
name: "Misused Forbidden Art",  
description: "You used a forbidden art recklessly, causing disaster.",  
karmaChange: -50,  
butterflyEffect: "The misuse creates a curse that affects your bloodline.",  
triggerConditions: ["know forbidden art", "use recklessly"],  
severity: "major",  
category: "mystical",  
probability: 90,  
delayedEffect: {  
trigger: "Your descendants cultivate",  
effect: "Curse manifests in descendants, hindering their progress",  
delayTime: "1 generation"  
}  
},  
// Catastrophic Events  
{  
id: "ke-031",  
name: "Betrayed Humanity",  
description: "You betrayed all of humanity to an alien or demonic force.",  
karmaChange: -1000,  
butterflyEffect: "Humanity is enslaved, and your name becomes synonymous with ultimate treachery.",  
triggerConditions: ["humanity exists", "opportunity to betray"],  
severity: "catastrophic",  
category: "moral",  
probability: 100,  
delayedEffect: {  
trigger: "Any future human interaction",  
effect: "All humans recognize and hate you, making cooperation impossible",  
delayTime: "eternal"  
}  
},  
{  
id: "ke-032",  
name: "Saved Humanity",  
description: "You saved humanity from extinction at great personal cost.",  
karmaChange: 1000,  
butterflyEffect: "Your sacrifice becomes legend, inspiring countless future generations.",  
triggerConditions: ["humanity in danger", "ability to save"],  
severity: "catastrophic",  
category: "moral",  
probability: 3,  
delayedEffect: {  
trigger: "Humanity faces crisis again",  
effect: "Legend of your sacrifice inspires others to save humanity again",  
delayTime: "eternal"  
}  
},  
{  
id: "ke-033",  
name: "Destroyed a World",  
description: "You destroyed an entire world and all its inhabitants.",  
karmaChange: -500,  
butterflyEffect: "The destruction echoes through the cosmos, attracting cosmic judgment.",  
triggerConditions: ["world exists", "power to destroy"],  
severity: "catastrophic",  
category: "combat",  
probability: 100,  
delayedEffect: {  
trigger: "Using cosmic power",  
effect: "Cosmic entities seek to punish you for world destruction",  
delayTime: "immediate"  
}  
},  
{  
id: "ke-034",  
name: "Created a World",  
description: "You created a new world and seeded it with life.",  
karmaChange: 500,  
butterflyEffect: "Your creation becomes a sanctuary for future generations.",  
triggerConditions: ["attain creation power", "choose to create"],  
severity: "catastrophic",  
category: "mystical",  
probability: 2,  
delayedEffect: {  
trigger: "Need sanctuary or new beginning",  
effect: "Created world provides refuge and new opportunities",  
delayTime: "immediate"  
}  
},  
{  
id: "ke-035",  
name: "Broke the Cycle of Samsara",  
description: "You broke the cycle of reincarnation, achieving true liberation.",  
karmaChange: 750,  
butterflyEffect: "Your liberation frees countless souls trapped in the cycle.",  
triggerConditions: ["reach enlightenment", "break cycle"],  
severity: "catastrophic",  
category: "mystical",  
probability: 0.1,  
delayedEffect: {  
trigger: "Any interaction with reincarnation",  
effect: "Your liberation affects the entire cycle of rebirth",  
delayTime: "eternal"  
}  
},  
{  
id: "ke-036",  
name: "Bound Souls to Suffering",  
description: "You bound countless souls to eternal suffering for power.",  
karmaChange: -750,  
butterflyEffect: "The bound souls' suffering creates a karmic debt that can never be repaid.",  
triggerConditions: ["souls available", "desire for power"],  
severity: "catastrophic",  
category: "mystical",  
probability: 100,  
delayedEffect: {  
trigger: "Any cultivation attempt",  
effect: "Karmic debt from bound souls hinders all progress",  
delayTime: "eternal"  
}  
},  
// Miraculous Events  
{  
id: "ke-037",  
name: "Achieved True Enlightenment",  
description: "You achieved true enlightenment, understanding all things.",  
karmaChange: 1000,  
butterflyEffect: "Your enlightenment illuminates the entire cosmos.",  
triggerConditions: ["reach peak cultivation", "let go of all attachments"],  
severity: "miraculous",  
category: "mystical",  
probability: 1,  
delayedEffect: {  
trigger: "Any question or mystery",  
effect: "Enlightenment provides perfect understanding of all things",  
delayTime: "immediate"  
}  
},  
{  
id: "ke-038",  
name: "Became One with the Dao",  
description: "You merged completely with the Dao, becoming existence itself.",  
karmaChange: 2000,  
butterflyEffect: "Your union with the Dao allows you to shape reality at will.",  
triggerConditions: ["transcend existence", "merge with Dao"],  
severity: "miraculous",  
category: "mystical",  
probability: 0.5,  
delayedEffect: {  
trigger: "Any desire or will",  
effect: "Union with Dao allows reality to conform to your will",  
delayTime: "immediate"  
}  
},  
{  
id: "ke-039",  
name: "Redeemed the Unredeemable",  
description: "You redeemed a being that was considered beyond redemption.",  
karmaChange: 300,  
butterflyEffect: "The redemption creates a chain reaction of redemption across the cosmos.",  
triggerConditions: ["encounter evil being", "choose to redeem"],  
severity: "miraculous",  
category: "moral",  
probability: 8,  
delayedEffect: {  
trigger: "Encountering other evil beings",  
effect: "Chain of redemption makes evil beings more likely to reform",  
delayTime: "5 years"  
}  
},  
{  
id: "ke-040",  
name: "Created Eternal Peace",  
description: "You established a state of eternal peace across all realms.",  
karmaChange: 500,  
butterflyEffect: "The eternal peace allows all beings to pursue their true potential.",  
triggerConditions: ["unite all realms", "establish peace"],  
severity: "miraculous",  
category: "political",  
probability: 0.05,  
delayedEffect: {  
trigger: "Any future conflict",  
effect: "Eternal peace prevents all conflicts from arising",  
delayTime: "eternal"  
}  
},  
// Additional Minor Events  
{  
id: "ke-041",  
name: "Shared Food with Hungry",  
description: "You shared your food with someone who was hungry.",  
karmaChange: 3,  
butterflyEffect: "The person remembers your kindness and helps you when you're starving.",  
triggerConditions: ["have food", "encounter hungry person"],  
severity: "minor",  
category: "moral",  
probability: 65,  
delayedEffect: {  
trigger: "Starving or in need",  
effect: "Person returns the kindness with food and shelter",  
delayTime: "1 year"  
}  
},  
{  
id: "ke-042",  
name: "Hoarded Resources",  
description: "You hoarded resources while others suffered.",  
karmaChange: -8,  
butterflyEffect: "Your hoarding causes resentment that leads to betrayal.",  
triggerConditions: ["have excess resources", "others in need"],  
severity: "minor",  
category: "moral",  
probability: 78,  
delayedEffect: {  
trigger: "Trusting others with resources",  
effect: "Those who resented your hoarding betray you",  
delayTime: "2 years"  
}  
},  
{  
id: "ke-043",  
name: "Taught a Skill",  
description: "You taught a valuable skill to someone without payment.",  
karmaChange: 7,  
butterflyEffect: "The student becomes a master who teaches your descendants.",  
triggerConditions: ["have skill", "someone wants to learn"],  
severity: "minor",  
category: "social",  
probability: 55,  
delayedEffect: {  
trigger: "Your descendants need training",  
effect: "Student or their descendants teach your family for free",  
delayTime: "10 years"  
}  
},  
{  
id: "ke-044",  
name: "Withheld Knowledge",  
description: "You refused to teach someone who desperately needed knowledge.",  
karmaChange: -6,  
butterflyEffect: "The person suffers, and their suffering is traced back to your refusal.",  
triggerConditions: ["have knowledge", "someone asks to learn"],  
severity: "minor",  
category: "moral",  
probability: 72,  
delayedEffect: {  
trigger: "Seeking knowledge yourself",  
effect: "Teachers refuse you due to your past refusal to teach",  
delayTime: "3 years"  
}  
},  
{  
id: "ke-045",  
name: "Protected the Environment",  
description: "You took action to protect the natural environment.",  
karmaChange: 5,  
butterflyEffect: "The protected area becomes a source of rare resources in the future.",  
triggerConditions: ["environment threatened", "ability to protect"],  
severity: "minor",  
category: "exploration",  
probability: 45,  
delayedEffect: {  
trigger: "Need rare resources",  
effect: "Protected area provides rare herbs and materials",  
delayTime: "5 years"  
}  
},  
{  
id: "ke-046",  
name: "Destroyed Habitat",  
description: "You destroyed a natural habitat for personal gain.",  
karmaChange: -10,  
butterflyEffect: "The destruction causes ecological collapse that affects you.",  
triggerConditions: ["natural habitat", "motivation to destroy"],  
severity: "minor",  
category: "exploration",  
probability: 82,  
delayedEffect: {  
trigger: "Relying on natural resources",  
effect: "Ecological collapse makes resources scarce",  
delayTime: "2 years"  
}  
},  
{  
id: "ke-047",  
name: "Honored Ancestors",  
description: "You performed proper rites to honor your ancestors.",  
karmaChange: 4,  
butterflyEffect: "Ancestors' spirits bless your endeavors.",  
triggerConditions: ["ancestors exist", "perform rites"],  
severity: "minor",  
category: "mystical",  
probability: 60,  
delayedEffect: {  
trigger: "Facing difficulty",  
effect: "Ancestral spirits provide subtle guidance and luck",  
delayTime: "immediate"  
}  
},  
{  
id: "ke-048",  
name: "Disrespected Ancestors",  
description: "You showed disrespect to your ancestors or their traditions.",  
karmaChange: -6,  
butterflyEffect: "Ancestral spirits withdraw their protection.",  
triggerConditions: ["ancestors exist", "disrespect traditions"],  
severity: "minor",  
category: "mystical",  
probability: 70,  
delayedEffect: {  
trigger: "Relying on luck or protection",  
effect: "Without ancestral blessing, misfortune follows",  
delayTime: "immediate"  
}  
},  
{  
id: "ke-049",  
name: "Kept a Promise",  
description: "You kept a difficult promise despite hardship.",  
karmaChange: 8,  
butterflyEffect: "Your reputation for honesty attracts trustworthy allies.",  
triggerConditions: ["made promise", "opportunity to break"],  
severity: "minor",  
category: "moral",  
probability: 48,  
delayedEffect: {  
trigger: "Need trustworthy allies",  
effect: "Reputation attracts honest and loyal companions",  
delayTime: "2 years"  
}  
},  
{  
id: "ke-050",  
name: "Broke a Promise",  
description: "You broke a promise for personal convenience.",  
karmaChange: -9,  
butterflyEffect: "Your broken promise destroys trust in your word.",  
triggerConditions: ["made promise", "opportunity to break"],  
severity: "minor",  
category: "moral",  
probability: 83,  
delayedEffect: {  
trigger: "Ask others to trust you",  
effect: "Broken promise makes others doubt your word",  
delayTime: "1 year"  
}  
}  
];