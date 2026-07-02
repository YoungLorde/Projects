export interface Chapter {  
id: string;  
title: string;  
content: string;  
wordCount: number;  
order: number;  
status: 'draft' | 'in_progress' | 'completed' | 'published';  
createdAt: string;  
updatedAt: string;  
notes?: string;  
}

export interface Story {  
id: string;  
title: string;  
description: string;  
genre: string[];  
chapters: Chapter[];  
status: 'planning' | 'writing' | 'editing' | 'completed' | 'published';  
createdAt: string;  
updatedAt: string;  
targetWordCount?: number;  
currentWordCount: number;  
tags: string[];  
settings?: {  
world?: string;  
characters?: string[];  
timeline?: string;  
};  
}

export interface Project {  
id: string;  
name: string;  
description: string;  
stories: Story[];  
createdAt: string;  
updatedAt: string;  
color: string;  
icon: string;  
}

export function createProject(name: string, description: string, color: string = '#00bcd4'): Project {  
return {  
id: `project_${Date.now()}`,  
name,  
description,  
stories: [],  
createdAt: new Date().toISOString(),  
updatedAt: new Date().toISOString(),  
color,  
icon: '📁'  
};  
}

export function createStory(title: string, description: string, genre: string[]): Story {  
return {  
id: `story_${Date.now()}`,  
title,  
description,  
genre,  
chapters: [],  
status: 'planning',  
createdAt: new Date().toISOString(),  
updatedAt: new Date().toISOString(),  
currentWordCount: 0,  
tags: []  
};  
}

export function createChapter(title: string, order: number): Chapter {  
return {  
id: `chapter_${Date.now()}`,  
title,  
content: '',  
wordCount: 0,  
order,  
status: 'draft',  
createdAt: new Date().toISOString(),  
updatedAt: new Date().toISOString()  
};  
}

export function addStoryToProject(project: Project, story: Story): Project {  
const updatedProject = {  
...project,  
stories: [...project.stories, story],  
updatedAt: new Date().toISOString()  
};  
return updatedProject;  
}

export function addChapterToStory(story: Story, chapter: Chapter): Story {  
const updatedStory = {  
...story,  
chapters: [...story.chapters, chapter],  
updatedAt: new Date().toISOString()  
};  
return updatedStory;  
}

export function updateChapter(story: Story, chapterId: string, updates: Partial): Story {  
const updatedChapters = story.chapters.map((ch) =>  
ch.id === chapterId ? { ...ch, ...updates, updatedAt: new Date().toISOString() } : ch  
);

const newWordCount = updatedChapters.reduce((sum, ch) => sum + ch.wordCount, 0);

return {  
...story,  
chapters: updatedChapters,  
currentWordCount: newWordCount,  
updatedAt: new Date().toISOString()  
};  
}

export function deleteChapter(story: Story, chapterId: string): Story {  
const updatedChapters = story.chapters.filter((ch) => ch.id !== chapterId);  
const newWordCount = updatedChapters.reduce((sum, ch) => sum + ch.wordCount, 0);

return {  
...story,  
chapters: updatedChapters,  
currentWordCount: newWordCount,  
updatedAt: new Date().toISOString()  
};  
}

export function reorderChapters(story: Story, chapterIds: string[]): Story {  
const chapterMap = new Map(story.chapters.map((ch) => [ch.id, ch]));  
const reorderedChapters = chapterIds  
.map((id) => chapterMap.get(id))  
.filter((ch): ch is Chapter => ch !== undefined)  
.map((ch, index) => ({ ...ch, order: index }));

return {  
...story,  
chapters: reorderedChapters,  
updatedAt: new Date().toISOString()  
};  
}

export function getProjectStats(project: Project): {  
totalStories: number;  
totalChapters: number;  
totalWords: number;  
completedChapters: number;  
inProgressChapters: number;  
} {  
const totalStories = project.stories.length;  
const totalChapters = project.stories.reduce((sum, story) => sum + story.chapters.length, 0);  
const totalWords = project.stories.reduce((sum, story) => sum + story.currentWordCount, 0);  
const completedChapters = project.stories.reduce(  
(sum, story) => sum + story.chapters.filter((ch) => ch.status === 'completed').length,  
0  
);  
const inProgressChapters = project.stories.reduce(  
(sum, story) => sum + story.chapters.filter((ch) => ch.status === 'in_progress').length,  
0  
);

return { totalStories, totalChapters, totalWords, completedChapters, inProgressChapters };  
}

export function getStoryProgress(story: Story): number {  
if (story.chapters.length === 0) return 0;  
const completed = story.chapters.filter((ch) => ch.status === 'completed').length;  
return Math.round((completed / story.chapters.length) * 100);  
}