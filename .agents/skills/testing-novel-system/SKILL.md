---
name: testing-novel-system
description: Test the RP Conversion AI-assisted novel writing system end-to-end. Use when verifying orchestrator, agents, databases, trackers, or pipeline changes.
---

# Testing the RP Conversion Novel Writing System

This system is a Python library (no web UI). All testing is shell-based via Python commands.

## Prerequisites

- Python 3.x with PyYAML installed (`pip install pyyaml`)
- Run all commands from the repo root `/home/ubuntu/repos/Projects`
- Always `import sys; sys.path.insert(0, '.')` before importing project modules

## Quick Smoke Test

```python
from orchestrator import Orchestrator
orch = Orchestrator()
print(len(orch.agents))  # Should be 15
```

## Key Test Areas

### 1. Agent Loading
Verify all 15 agents load: lore_judge, prose_writer, refusal_checker, style_extractor, dialogue_specialist, plot_checker, continuity_checker, style_editor, scene_beat_generator, summarizer, outline_generator, word_count_enforcer, parameter_enforcer, stat_currency_tracker, database_manager.

### 2. Database Queries
```python
db = orch.agents['database_manager']
stats = db.get_stats_summary()  # Should show 23 files, 9 categories
results = db.query_by_name('Dravik')  # Known race entry
results = db.query_by_tier(2, 'monsters')  # Filter by tier
results = db.query_by_race('Human')  # Filter by race
```

Categories: races, monsters, factions, powers, vehicles, items, worlds, technology, ancient_races.

### 3. Relationship Tracker
```python
from relationship_tracker import RelationshipTracker
rt = RelationshipTracker()
rt.set_relationship('A', 'B', 'ally', 80)
rt.add_interaction('A', 'B', 1, 'Event description', trust_change=10)
rel = rt.get_relationship('A', 'B')  # Also works as get_relationship('B', 'A')
ctx = rt.build_relationship_context()  # For agent injection
```

**Known quirk:** History entries use field name `event` (not `description`). Trust is clamped to [-100, 100].

### 4. Conflict Tracker
```python
from conflict_tracker import ConflictTracker
ct = ConflictTracker()
entry = ct.add_conflict('Name', 'personal', chapter=1, participants=['A'])
cid = entry['id']
ct.transition(cid, 'developing', chapter=5)
ct.get_stale_conflicts(current_chapter=30, threshold=20)  # Flags inactive conflicts
ctx = ct.build_conflict_context(current_chapter=30)
```

Valid states: introduced, developing, escalating, climax, resolving, resolved, dormant, abandoned.
Invalid state transitions return `{'error': ...}` without changing state.

### 5. Orchestrator Commands
```python
# Write chapter (returns execution plan, not actual prose)
plan = orch.write_chapter(chapter_num=1, pipeline='full_quality')
# plan keys: arc, chapter_num, context_loaded, final_prose, instructions, pipeline, status, steps, validations, word_count

# Finalize (validates prose)
result = orch.finalize_chapter(1, prose_text)
# result keys: chapter_num, issues, saved, status, validations, word_count
# validations contains: word_count, parameters, refusal_check, stat_tracking

# Auto-pilot
result = orch.auto_write(start=1, end=5)  # Queues 5 chapters

# Database query through orchestrator
result = orch.query_database(query='Broodmother')

# Relationships & conflicts through orchestrator
orch.add_relationship('Mohamed Vance', 'Zero AI', 'ally', 85)
orch.show_relationships('Mohamed Vance')
orch.add_conflict('Raider Threat', 'personal', 5, ['Mohamed'], 'Stakes')
orch.check_conflicts(current_chapter=10)
```

### 6. Pipeline Engine
```python
from pipelines import PipelineEngine, PIPELINES
# PipelineEngine() takes no args
# load_pipeline(config_dict, agents_dict) — config from PIPELINES[name], agents from orch.agents
pe = PipelineEngine()
pe.load_pipeline(PIPELINES['full_quality'], orch.agents)
print(len(pe.steps))  # 6 for full_quality
```

Expected step counts: quality_prose_with_revision=4, quick_draft=1, polished_output=2, dialogue_polish=2, full_quality=6, quality_with_lore_check=3, push_prompt_self_correction=4, outline_and_write=3, full_editorial=9.

### 7. Stat Tracker
```python
from agents.stat_currency_tracker import StatCurrencyTracker
tracker = StatCurrencyTracker()
extracted = tracker.extract_changes(prose)  # Not extract_local
tracker.validate_math(extracted, current_state)
```

**Important:** RP extraction regex expects `earned N RP` or `gained N RP` format. Does NOT match `RP earned: N` (colon format). Stat gains use `+N STAT` format (e.g., `+5 STR`). Level ups match `Level N` pattern.

### 8. Rolling Context
```python
orch.memory.save_chapter_summary(1, 'Summary text')
ctx = orch._build_rolling_context(chapter_num=2, window=3)  # Last 3 summaries
# Returns empty string for chapter 1 (no previous chapters)
```

### 9. Memory Manager
```python
state = orch.get_current_state()
orch.update_story_state({'level': 5, 'rp_balance': 5000})
updated = orch.get_current_state()  # Verify roundtrip
```

## Test Artifacts

Clean up before tests:
```python
import os
for f in ['books/rp_conversion/relationships.yaml', 'books/rp_conversion/conflicts_state.yaml']:
    if os.path.exists(f): os.remove(f)
```

These files are generated at runtime by RelationshipTracker and ConflictTracker.

## No LLM Execution

Agents are prompt generators — `build_prompt()` returns prompt text. The orchestrator returns execution plans (dicts with system_prompt/user_prompt per step). Actual LLM execution happens in Windsurf. To test the full Windsurf integration, open the project in Windsurf and try commands like "Write Chapter 1".
