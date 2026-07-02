export interface ExternalTool {  
id: string;  
name: string;  
description: string;  
category: 'writing' | 'productivity' | 'research' | 'ai' | 'storage' | 'communication';  
type: 'api' | 'webhook' | 'oauth' | 'custom';  
status: 'available' | 'configured' | 'error' | 'disabled';  
icon: string;  
configFields: {  
key: string;  
label: string;  
type: 'text' | 'password' | 'url' | 'number' | 'boolean';  
required: boolean;  
placeholder?: string;  
}[];  
capabilities: string[];  
documentation?: string;  
}

export interface ToolIntegration {  
toolId: string;  
config: Record;  
enabled: boolean;  
lastSync?: string;  
errors?: string[];  
}

export const externalTools: ExternalTool[] = [  
{  
id: 'openai',  
name: 'OpenAI',  
description: 'AI-powered writing assistance and content generation',  
category: 'ai',  
type: 'api',  
status: 'available',  
icon: '🤖',  
configFields: [  
{ key: 'apiKey', label: 'API Key', type: 'password', required: true, placeholder: 'sk-...' },  
{ key: 'model', label: 'Model', type: 'text', required: false, placeholder: 'gpt-4' },  
{ key: 'maxTokens', label: 'Max Tokens', type: 'number', required: false, placeholder: '2000' }  
],  
capabilities: ['Text generation', 'Editing suggestions', 'Summarization', 'Translation'],  
documentation: 'https://platform.openai.com/docs'  
},  
{  
id: 'anthropic',  
name: 'Anthropic Claude',  
description: 'Advanced AI assistant for writing and analysis',  
category: 'ai',  
type: 'api',  
status: 'available',  
icon: '🧠',  
configFields: [  
{ key: 'apiKey', label: 'API Key', type: 'password', required: true, placeholder: 'sk-ant-...' },  
{ key: 'model', label: 'Model', type: 'text', required: false, placeholder: 'claude-3-opus' }  
],  
capabilities: ['Text generation', 'Analysis', 'Code assistance', 'Long-form writing'],  
documentation: 'https://docs.anthropic.com'  
},  
{  
id: 'google_drive',  
name: 'Google Drive',  
description: 'Cloud storage and document management',  
category: 'storage',  
type: 'oauth',  
status: 'available',  
icon: '📁',  
configFields: [  
{ key: 'clientId', label: 'Client ID', type: 'text', required: true },  
{ key: 'clientSecret', label: 'Client Secret', type: 'password', required: true },  
{ key: 'folderId', label: 'Default Folder ID', type: 'text', required: false }  
],  
capabilities: ['Cloud backup', 'Document sync', 'File sharing', 'Version history'],  
documentation: 'https://developers.google.com/drive'  
},  
{  
id: 'dropbox',  
name: 'Dropbox',  
description: 'File storage and synchronization',  
category: 'storage',  
type: 'oauth',  
status: 'available',  
icon: '📦',  
configFields: [  
{ key: 'accessToken', label: 'Access Token', type: 'password', required: true },  
{ key: 'appKey', label: 'App Key', type: 'text', required: true },  
{ key: 'appSecret', label: 'App Secret', type: 'password', required: true }  
],  
capabilities: ['File sync', 'Backup', 'Sharing', 'Version control'],  
documentation: 'https://www.dropbox.com/developers'  
},  
{  
id: 'notion',  
name: 'Notion',  
description: 'Productivity and note-taking integration',  
category: 'productivity',  
type: 'oauth',  
status: 'available',  
icon: '📝',  
configFields: [  
{ key: 'integrationToken', label: 'Integration Token', type: 'password', required: true },  
{ key: 'databaseId', label: 'Database ID', type: 'text', required: false }  
],  
capabilities: ['Note sync', 'Task management', 'Database integration', 'Page creation'],  
documentation: 'https://developers.notion.com'  
},  
{  
id: 'github',  
name: 'GitHub',  
description: 'Version control and collaboration',  
category: 'writing',  
type: 'oauth',  
status: 'available',  
icon: '🐙',  
configFields: [  
{ key: 'token', label: 'Personal Access Token', type: 'password', required: true },  
{ key: 'repo', label: 'Repository', type: 'text', required: false },  
{ key: 'branch', label: 'Branch', type: 'text', required: false, placeholder: 'main' }  
],  
capabilities: ['Version control', 'Collaboration', 'Backup', 'Issue tracking'],  
documentation: 'https://docs.github.com'  
},  
{  
id: 'discord',  
name: 'Discord',  
description: 'Community and communication integration',  
category: 'communication',  
type: 'webhook',  
status: 'available',  
icon: '💬',  
configFields: [  
{ key: 'webhookUrl', label: 'Webhook URL', type: 'url', required: true },  
{ key: 'channelId', label: 'Channel ID', type: 'text', required: false }  
],  
capabilities: ['Notifications', 'Updates', 'Community engagement', 'Automated posts'],  
documentation: 'https://discord.com/developers/docs/webhooks'  
},  
{  
id: 'slack',  
name: 'Slack',  
description: 'Team communication and notifications',  
category: 'communication',  
type: 'webhook',  
status: 'available',  
icon: '💼',  
configFields: [  
{ key: 'webhookUrl', label: 'Webhook URL', type: 'url', required: true },  
{ key: 'channel', label: 'Channel', type: 'text', required: false }  
],  
capabilities: ['Notifications', 'Updates', 'Team collaboration', 'Automated messages'],  
documentation: 'https://api.slack.com/webhooks'  
},  
{  
id: 'scrivener',  
name: 'Scrivener',  
description: 'Long-form writing software integration',  
category: 'writing',  
type: 'custom',  
status: 'available',  
icon: '📖',  
configFields: [  
{ key: 'projectPath', label: 'Project Path', type: 'text', required: true },  
{ key: 'autoSync', label: 'Auto Sync', type: 'boolean', required: false }  
],  
capabilities: ['Project import/export', 'Chapter sync', 'Backup', 'Format conversion'],  
documentation: 'https://www.literatureandlatte.com/scrivener'  
},  
{  
id: 'obsidian',  
name: 'Obsidian',  
description: 'Note-taking and knowledge base integration',  
category: 'productivity',  
type: 'custom',  
status: 'available',  
icon: '🔮',  
configFields: [  
{ key: 'vaultPath', label: 'Vault Path', type: 'text', required: true },  
{ key: 'syncInterval', label: 'Sync Interval (minutes)', type: 'number', required: false, placeholder: '5' }  
],  
capabilities: ['Note sync', 'Markdown export', 'Link management', 'Plugin integration'],  
documentation: 'https://help.obsidian.md'  
},  
{  
id: 'grammarly',  
name: 'Grammarly',  
description: 'Grammar and writing style checking',  
category: 'writing',  
type: 'api',  
status: 'available',  
icon: '✅',  
configFields: [  
{ key: 'apiKey', label: 'API Key', type: 'password', required: true },  
{ key: 'language', label: 'Language', type: 'text', required: false, placeholder: 'en-US' }  
],  
capabilities: ['Grammar checking', 'Style suggestions', 'Plagiarism check', 'Tone detection'],  
documentation: 'https://developer.grammarly.com'  
},  
{  
id: 'wikipedia',  
name: 'Wikipedia',  
description: 'Research and fact-checking integration',  
category: 'research',  
type: 'api',  
status: 'available',  
icon: '🌐',  
configFields: [  
{ key: 'language', label: 'Language Code', type: 'text', required: false, placeholder: 'en' },  
{ key: 'maxResults', label: 'Max Results', type: 'number', required: false, placeholder: '10' }  
],  
capabilities: ['Article search', 'Fact checking', 'Reference lookup', 'Summary generation'],  
documentation: 'https://en.wikipedia.org/api/rest_v1'  
}  
];

export function getToolById(id: string): ExternalTool | undefined {  
return externalTools.find((tool) => tool.id === id);  
}

export function getToolsByCategory(category: ExternalTool['category']): ExternalTool[] {  
return externalTools.filter((tool) => tool.category === category);  
}

export function getAvailableTools(): ExternalTool[] {  
return externalTools.filter((tool) => tool.status === 'available' || tool.status === 'configured');  
}

export function getConfiguredTools(integrations: ToolIntegration[]): ExternalTool[] {  
return externalTools.filter((tool) =>   
integrations.some((integration) => integration.toolId === tool.id && integration.enabled)  
);  
}

export function validateToolConfig(tool: ExternalTool, config: Record): { valid: boolean; errors: string[] } {  
const errors: string[] = [];

for (const field of tool.configFields) {  
if (field.required && !config[field.key]) {  
errors.push(`${field.label} is required`);  
}

if (field.type === 'url' && config[field.key] && !isValidUrl(config[field.key])) {  
errors.push(`${field.label} must be a valid URL`);  
}

if (field.type === 'number' && config[field.key] && isNaN(Number(config[field.key]))) {  
errors.push(`${field.label} must be a number`);  
}  
}

return { valid: errors.length === 0, errors };  
}

function isValidUrl(url: string): boolean {  
try {  
new URL(url);  
return true;  
} catch {  
return false;  
}  
}

export function createToolIntegration(toolId: string, config: Record): ToolIntegration {  
return {  
toolId,  
config,  
enabled: true,  
lastSync: new Date().toISOString()  
};  
}