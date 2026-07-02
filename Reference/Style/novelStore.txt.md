export interface Novel {  
id: string;  
title: string;  
author: string;  
description: string;  
genre: string[];  
wordCount: number;  
chapters: number;  
status: 'completed' | 'ongoing' | 'hiatus';  
rating: number; // 0-5  
price: number;  
coverImage?: string;  
tags: string[];  
publishDate: string;  
lastUpdated: string;  
}

export interface StoreCategory {  
id: string;  
name: string;  
description: string;  
icon: string;  
}

export const storeCategories: StoreCategory[] = [  
{ id: 'featured', name: 'Featured', description: 'Top picks and new releases', icon: '⭐' },  
{ id: 'fantasy', name: 'Fantasy', description: 'Magic, adventure, and wonder', icon: '🗡️' },  
{ id: 'scifi', name: 'Sci-Fi', description: 'Space, technology, and future', icon: '🚀' },  
{ id: 'romance', name: 'Romance', description: 'Love stories and relationships', icon: '💕' },  
{ id: 'mystery', name: 'Mystery', description: 'Thrillers and suspense', icon: '🔍' },  
{ id: 'horror', name: 'Horror', description: 'Scary and supernatural', icon: '👻' },  
{ id: 'litrpg', name: 'LitRPG', description: 'Game-like progression stories', icon: '🎮' },  
{ id: 'xianxia', name: 'Xianxia', description: 'Chinese cultivation novels', icon: '☯️' },  
{ id: 'urban', name: 'Urban Fantasy', description: 'Magic in modern settings', icon: '🏙️' },  
{ id: 'historical', name: 'Historical', description: 'Stories set in the past', icon: '📜' }  
];

export const featuredNovels: Novel[] = [  
{  
id: 'novel_1',  
title: 'The Ascendant',  
author: 'System Author',  
description: 'A young cultivator rises from nothing to challenge the heavens themselves.',  
genre: ['Xianxia', 'Fantasy', 'Action'],  
wordCount: 2500000,  
chapters: 1500,  
status: 'ongoing',  
rating: 4.8,  
price: 0,  
tags: ['Cultivation', 'Strong MC', 'Magic', 'Adventure'],  
publishDate: '2024-01-15',  
lastUpdated: '2024-04-20'  
},  
{  
id: 'novel_2',  
title: 'Starforged',  
author: 'Cosmic Writer',  
description: 'In a galaxy of warring factions, one engineer discovers an ancient power.',  
genre: ['Sci-Fi', 'Space Opera', 'Adventure'],  
wordCount: 1800000,  
chapters: 800,  
status: 'ongoing',  
rating: 4.6,  
price: 0,  
tags: ['Space', 'Technology', 'War', 'Discovery'],  
publishDate: '2024-02-01',  
lastUpdated: '2024-04-19'  
},  
{  
id: 'novel_3',  
title: 'Shadow\'s Edge',  
author: 'Night Author',  
description: 'A thief with the power to walk between shadows must save her city.',  
genre: ['Urban Fantasy', 'Mystery', 'Action'],  
wordCount: 950000,  
chapters: 400,  
status: 'completed',  
rating: 4.7,  
price: 2.99,  
tags: ['Magic', 'Thieves', 'Urban', 'Mystery'],  
publishDate: '2023-08-10',  
lastUpdated: '2024-01-20'  
},  
{  
id: 'novel_4',  
title: 'The Last Dungeon',  
author: 'Game Master',  
description: 'The final dungeon of the world has been conquered, but something remains.',  
genre: ['LitRPG', 'Fantasy', 'Adventure'],  
wordCount: 1200000,  
chapters: 600,  
status: 'ongoing',  
rating: 4.5,  
price: 0,  
tags: ['Gaming', 'Dungeon', 'Fantasy', 'Progression'],  
publishDate: '2024-01-20',  
lastUpdated: '2024-04-18'  
},  
{  
id: 'novel_5',  
title: 'Echoes of Eternity',  
author: 'Time Keeper',  
description: 'A time traveler must prevent the collapse of reality across multiple timelines.',  
genre: ['Sci-Fi', 'Time Travel', 'Thriller'],  
wordCount: 750000,  
chapters: 350,  
status: 'hiatus',  
rating: 4.4,  
price: 1.99,  
tags: ['Time', 'Sci-Fi', 'Thriller', 'Multiple Timelines'],  
publishDate: '2023-11-05',  
lastUpdated: '2024-02-15'  
},  
{  
id: 'novel_6',  
title: 'Crimson Blade',  
author: 'Sword Master',  
description: 'A legendary swordmaster seeks redemption in a world of darkness.',  
genre: ['Fantasy', 'Action', 'Dark'],  
wordCount: 1500000,  
chapters: 700,  
status: 'ongoing',  
rating: 4.6,  
price: 0,  
tags: ['Swords', 'Action', 'Dark Fantasy', 'Redemption'],  
publishDate: '2023-12-01',  
lastUpdated: '2024-04-17'  
}  
];

export function getNovelsByCategory(categoryId: string): Novel[] {  
if (categoryId === 'featured') return featuredNovels;

return featuredNovels.filter((novel) => {  
const categoryMap: Record = {  
'fantasy': ['Fantasy', 'Urban Fantasy', 'Dark Fantasy'],  
'scifi': ['Sci-Fi', 'Space Opera'],  
'romance': ['Romance'],  
'mystery': ['Mystery', 'Thriller'],  
'horror': ['Horror'],  
'litrpg': ['LitRPG'],  
'xianxia': ['Xianxia', 'Cultivation'],  
'urban': ['Urban Fantasy'],  
'historical': ['Historical']  
};

const categoryGenres = categoryMap[categoryId] || [];  
return novel.genre.some((g) => categoryGenres.includes(g));  
});  
}

export function searchNovels(query: string): Novel[] {  
const lowerQuery = query.toLowerCase();  
return featuredNovels.filter((novel) =>   
novel.title.toLowerCase().includes(lowerQuery) ||  
novel.author.toLowerCase().includes(lowerQuery) ||  
novel.description.toLowerCase().includes(lowerQuery) ||  
novel.tags.some((tag) => tag.toLowerCase().includes(lowerQuery))  
);  
}

export function getNovelById(id: string): Novel | undefined {  
return featuredNovels.find((novel) => novel.id === id);  
}

export function getNovelsByGenre(genre: string): Novel[] {  
return featuredNovels.filter((novel) =>   
novel.genre.includes(genre)  
);  
}

export function getFreeNovels(): Novel[] {  
return featuredNovels.filter((novel) => novel.price === 0);  
}

export function getCompletedNovels(): Novel[] {  
return featuredNovels.filter((novel) => novel.status === 'completed');  
}

export function getOngoingNovels(): Novel[] {  
return featuredNovels.filter((novel) => novel.status === 'ongoing');  
}