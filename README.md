# RP Conversion - Novel Writing System

A comprehensive AI-assisted novel writing system for the **RP Conversion** multi-universal LitRPG epic.

## Project Structure

```
Projects/
├── guides/                          # Story reference documents
│   ├── master_novel_bible.md        # Complete world bible (expanded)
│   ├── story_guide_overview.md      # In-depth story guide
│   └── chapter_guide.md             # Detailed chapter-by-chapter guide
│
├── books/
│   └── rp_conversion/               # Book 1: RP Conversion
│       ├── chapters/                 # Final chapter files (chapter_001.md, etc.)
│       ├── outlines/                 # Per-chapter outlines before writing
│       └── drafts/                   # Work-in-progress drafts
│
├── memory_bank/                     # Persistent lore & consistency storage
│   ├── lore/                        # World rules, physics, Game mechanics
│   ├── characters/                  # Character profiles & state tracking
│   ├── factions/                    # Faction data & relationships
│   ├── species/                     # Alien species profiles
│   ├── vehicles/                    # Vehicle tier tracking & upgrade logs
│   ├── systems/                     # System Interface, RP economy, cultivation
│   ├── conflicts/                   # Active wars, skirmishes, political events
│   └── locations/                   # Zones, planets, universes, rift corridors
│
├── agents/                          # AI Agent modules
│   ├── __init__.py
│   ├── base_agent.py                # Base agent class
│   ├── lore_judge.py                # Agent 1: Lore consistency checker
│   ├── prose_writer.py              # Agent 2: Prose generation
│   ├── refusal_checker.py           # Agent 3: Refusal detection
│   ├── style_extractor.py           # Agent 4: Style analysis
│   ├── dialogue_specialist.py       # Agent 5: Dialogue improvement
│   ├── plot_checker.py              # Agent 6: Plot hole detection
│   ├── continuity_checker.py        # Agent 7: Timeline/continuity validation
│   ├── style_editor.py              # Agent 8: Prose polishing
│   ├── scene_beat_generator.py      # Agent 9: Scene planning
│   ├── summarizer.py                # Agent 10: Narrative summarization
│   ├── outline_generator.py         # Agent 11: Story outlining
│   ├── word_count_enforcer.py       # Word count enforcement
│   └── parameter_enforcer.py        # Parameter enforcement
│
├── pipelines/                       # Agent workflow pipelines
│   ├── __init__.py
│   ├── pipeline_engine.py           # Pipeline execution engine
│   └── pipeline_definitions.py      # All pipeline configurations
│
├── orchestrator.py                  # Main driver - controls all agents
├── memory_manager.py                # Memory bank read/write interface
├── config.py                        # Global configuration
├── requirements.txt                 # Python dependencies
├── .windsurfrules                   # Windsurf AI integration rules
└── README.md                        # This file
```

## Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Usage via Windsurf Chat
Simply open this project in Windsurf and use natural language commands:

- **"Write Chapter 1"** - Activates the orchestrator to generate Chapter 1
- **"Continue the story"** - Writes the next chapter in sequence
- **"Check lore consistency for Chapter 5"** - Runs the Lore Judge on a specific chapter
- **"Polish Chapter 3"** - Runs the Style Editor pipeline
- **"Outline the next 10 chapters"** - Generates detailed outlines
- **"Show Mohamed's current stats"** - Queries the memory bank
- **"What happened in the last 5 chapters?"** - Generates a narrative summary

### Agents
11 specialized AI agents work together through configurable pipelines:

| Agent | Role | Purpose |
|-------|------|---------|
| Lore Judge | Consistency | Validates prose against established lore |
| Prose Writer | Generation | Writes story chapters |
| Refusal Checker | Quality | Detects AI content refusals |
| Style Extractor | Analysis | Extracts and codifies writing style |
| Dialogue Specialist | Enhancement | Improves dialogue authenticity |
| Plot Checker | Validation | Detects plot holes |
| Continuity Checker | Validation | Checks timeline/character consistency |
| Style Editor | Enhancement | Polishes prose quality |
| Scene Beat Generator | Planning | Creates scene-by-scene plans |
| Summarizer | Utility | Condenses narrative content |
| Outline Generator | Planning | Structures story arcs |

### Pipelines
Pre-configured agent workflows for different writing needs:

- **Full Quality Pipeline** - Maximum quality (5 agents)
- **Quality Prose with Revision** - Lore-checked writing (4 agents)
- **Polished Output** - Final-draft quality (2 agents)
- **Quick Draft** - Fast generation (1 agent)
- **Dialogue Polish** - Dialogue-focused (2 agents)
- **Push Prompt Self-Correction** - Anti-refusal pipeline (4 agents)

## Novel: RP Conversion
- **Genre:** Apocalyptic LitRPG / Sci-Fi / Multi-Universal Epic
- **Target:** 500+ chapters, 2,500+ words each
- **Protagonist:** Mohamed Vance
- **Core Mechanic:** RP Conversion - the ability to convert matter into Resource Points
