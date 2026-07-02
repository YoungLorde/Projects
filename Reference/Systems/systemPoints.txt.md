export interface SystemHolder {  
id: string;  
name: string;  
systemPoints: number;  
level: number; // 1-10  
totalEarned: number;  
totalSpent: number;  
achievements: string[];  
unlockedFeatures: string[];  
}

export interface SystemPurchase {  
id: string;  
name: string;  
description: string;  
cost: number;  
category: 'abilities' | 'knowledge' | 'resources' | 'privileges' | 'cosmetic';  
requirements: {  
level?: number;  
achievements?: string[];  
systemPoints?: number;  
};  
effects: string[];  
oneTime: boolean;  
}

export const systemPurchases: SystemPurchase[] = [  
{  
id: 'basic_ai_assistance',  
name: 'Basic AI Assistance',  
description: 'Access to basic AI writing suggestions',  
cost: 100,  
category: 'abilities',  
requirements: { level: 1 },  
effects: ['AI writing suggestions', 'Grammar checking', 'Style recommendations'],  
oneTime: true  
},  
{  
id: 'advanced_ai_assistance',  
name: 'Advanced AI Assistance',  
description: 'Advanced AI with plot and character analysis',  
cost: 500,  
category: 'abilities',  
requirements: { level: 3, achievements: ['basic_ai_assistance'] },  
effects: ['Plot analysis', 'Character development', 'Story structure', 'Pacing suggestions'],  
oneTime: true  
},  
{  
id: 'world_building_pack',  
name: 'World Building Pack',  
description: 'Comprehensive world building tools and databases',  
cost: 300,  
category: 'knowledge',  
requirements: { level: 2 },  
effects: ['Culture generator', 'Geography tools', 'History templates', 'Language creator'],  
oneTime: true  
},  
{  
id: 'character_generator',  
name: 'Character Generator',  
description: 'Advanced character creation with personality systems',  
cost: 250,  
category: 'abilities',  
requirements: { level: 2 },  
effects: ['Personality assignment', 'Background generation', 'Skill system', 'Relationship mapping'],  
oneTime: true  
},  
{  
id: 'plot_structure_library',  
name: 'Plot Structure Library',  
description: 'Access to hundreds of plot structures and templates',  
cost: 200,  
category: 'knowledge',  
requirements: { level: 1 },  
effects: ['Hero journey', 'Three act structure', 'Save the cat', 'Custom templates'],  
oneTime: true  
},  
{  
id: 'daily_word_boost',  
name: 'Daily Word Boost',  
description: 'Double word count progress for one day',  
cost: 50,  
category: 'privileges',  
requirements: { level: 1 },  
effects: ['2x word count', 'Motivation boost', 'Streak protection'],  
oneTime: false  
},  
{  
id: 'inspiration_generator',  
name: 'Inspiration Generator',  
description: 'AI-powered idea generation for stories',  
cost: 150,  
category: 'abilities',  
requirements: { level: 2 },  
effects: ['Plot ideas', 'Character concepts', 'Scene prompts', 'Dialogue suggestions'],  
oneTime: true  
},  
{  
id: 'export_premium',  
name: 'Premium Export',  
description: 'Export to multiple formats with formatting',  
cost: 200,  
category: 'privileges',  
requirements: { level: 1 },  
effects: ['PDF export', 'EPUB export', 'Custom formatting', 'Cover generation'],  
oneTime: true  
},  
{  
id: 'collaboration_tools',  
name: 'Collaboration Tools',  
description: 'Share and collaborate on stories with others',  
cost: 400,  
category: 'privileges',  
requirements: { level: 3 },  
effects: ['Real-time editing', 'Comments', 'Version history', 'User permissions'],  
oneTime: true  
},  
{  
id: 'analytics_dashboard',  
name: 'Analytics Dashboard',  
description: 'Detailed writing statistics and insights',  
cost: 300,  
category: 'knowledge',  
requirements: { level: 2 },  
effects: ['Writing patterns', 'Productivity metrics', 'Goal tracking', 'Comparisons'],  
oneTime: true  
},  
{  
id: 'custom_themes',  
name: 'Custom Themes',  
description: 'Personalize the application appearance',  
cost: 100,  
category: 'cosmetic',  
requirements: { level: 1 },  
effects: ['Color schemes', 'Font selection', 'Layout options', 'Background images'],  
oneTime: true  
},  
{  
id: 'cloud_storage',  
name: 'Cloud Storage',  
description: 'Backup and sync stories to cloud',  
cost: 250,  
category: 'resources',  
requirements: { level: 2 },  
effects: ['Auto-sync', 'Version history', 'Cross-device access', 'Offline mode'],  
oneTime: true  
},  
{  
id: 'ai_coauthor',  
name: 'AI Co-author',  
description: 'AI that writes alongside you',  
cost: 1000,  
category: 'abilities',  
requirements: { level: 5, achievements: ['advanced_ai_assistance'] },  
effects: ['Co-writing', 'Style matching', 'Continuation', 'Dialogue generation'],  
oneTime: true  
},  
{  
id: 'master_class_access',  
name: 'Master Class Access',  
description: 'Access to writing master classes and tutorials',  
cost: 500,  
category: 'knowledge',  
requirements: { level: 3 },  
effects: ['Video lessons', 'Writing exercises', 'Expert feedback', 'Community access'],  
oneTime: true  
},  
{  
id: 'unlimited_projects',  
name: 'Unlimited Projects',  
description: 'Create unlimited number of projects',  
cost: 400,  
category: 'privileges',  
requirements: { level: 2 },  
effects: ['No project limits', 'Advanced organization', 'Project templates', 'Bulk operations'],  
oneTime: true  
}  
];

export function earnSystemPoints(holder: SystemHolder, amount: number): SystemHolder {  
holder.systemPoints += amount;  
holder.totalEarned += amount;

// Check for level up  
const newLevel = calculateLevel(holder.totalEarned);  
if (newLevel > holder.level) {  
holder.level = newLevel;  
holder.achievements.push(`level_${newLevel}`);  
}

return holder;  
}

export function spendSystemPoints(holder: SystemHolder, amount: number): boolean {  
if (holder.systemPoints < amount) return false;

holder.systemPoints -= amount;  
holder.totalSpent += amount;  
return true;  
}

export function calculateLevel(totalPoints: number): number {  
// Level formula: level = floor(sqrt(totalPoints / 100)) + 1  
return Math.floor(Math.sqrt(totalPoints / 100)) + 1;  
}

export function getPointsForNextLevel(currentLevel: number): number {  
// Points needed for next level  
return Math.pow(currentLevel, 2) * 100;  
}

export function canPurchase(holder: SystemHolder, purchase: SystemPurchase): boolean {  
if (holder.systemPoints < purchase.cost) return false;

if (purchase.requirements.level && holder.level < purchase.requirements.level) {  
return false;  
}

if (purchase.requirements.achievements) {  
for (const achievement of purchase.requirements.achievements) {  
if (!holder.achievements.includes(achievement)) {  
return false;  
}  
}  
}

if (purchase.requirements.systemPoints && holder.totalEarned < purchase.requirements.systemPoints) {  
return false;  
}

return true;  
}

export function makePurchase(holder: SystemHolder, purchaseId: string): boolean {  
const purchase = systemPurchases.find((p) => p.id === purchaseId);  
if (!purchase) return false;

if (!canPurchase(holder, purchase)) return false;

if (!spendSystemPoints(holder, purchase.cost)) return false;

if (!holder.unlockedFeatures.includes(purchaseId)) {  
holder.unlockedFeatures.push(purchaseId);  
}

if (!holder.achievements.includes(`purchased_${purchaseId}`)) {  
holder.achievements.push(`purchased_${purchaseId}`);  
}

return true;  
}

export function getAvailablePurchases(holder: SystemHolder): SystemPurchase[] {  
return systemPurchases.filter((purchase) => {  
// Already purchased and one-time  
if (purchase.oneTime && holder.unlockedFeatures.includes(purchase.id)) {  
return false;  
}

return canPurchase(holder, purchase);  
});  
}

export function getPurchasedPurchases(holder: SystemHolder): SystemPurchase[] {  
return systemPurchases.filter((purchase) =>   
holder.unlockedFeatures.includes(purchase.id)  
);  
}

export function getLockedPurchases(holder: SystemHolder): SystemPurchase[] {  
return systemPurchases.filter((purchase) => {  
// Already purchased  
if (holder.unlockedFeatures.includes(purchase.id)) {  
return false;  
}

return !canPurchase(holder, purchase);  
});  
}

export function calculatePointsFromWords(wordsWritten: number): number {  
// 1 point per 100 words written  
return Math.floor(wordsWritten / 100);  
}

export function calculatePointsFromSession(sessionDuration: number): number {  
// Bonus points for long writing sessions (1 point per 10 minutes)  
return Math.floor(sessionDuration / 10);  
}

export function calculatePointsFromStreak(streakDays: number): number {  
// Streak bonus: 10 points per day of streak  
return streakDays * 10;  
}

export function calculateDailyPoints(wordsWritten: number, sessionDuration: number, streakDays: number): number {  
let points = 0;  
points += calculatePointsFromWords(wordsWritten);  
points += calculatePointsFromSession(sessionDuration);  
points += calculatePointsFromStreak(streakDays);  
return points;  
}