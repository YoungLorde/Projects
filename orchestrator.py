"""
Orchestrator — Main driver that controls all agents and pipelines.

The Orchestrator is the central controller for the RP Conversion Novel
Writing System. It coordinates agents, manages pipelines, enforces
parameters, and interfaces with the Memory Bank to maintain consistency
across 1000+ chapters.

Designed to be invoked from Windsurf chat via .windsurfrules integration.
"""

from typing import Optional

from agents.continuity_checker import ContinuityChecker
from agents.database_manager import DatabaseManager
from agents.dialogue_specialist import DialogueSpecialist
from agents.lore_judge import LoreJudge
from agents.outline_generator import OutlineGenerator
from agents.parameter_enforcer import ParameterEnforcer
from agents.plot_checker import PlotChecker
from agents.prose_writer import ProseWriter
from agents.refusal_checker import RefusalChecker
from agents.scene_beat_generator import SceneBeatGenerator
from agents.style_editor import StyleEditor
from agents.style_extractor import StyleExtractor
from agents.summarizer import Summarizer
from agents.slice_of_life_scenes import SliceOfLifeSceneGenerator
from agents.stat_currency_tracker import StatCurrencyTracker
from agents.technology_infrastructure import TechnologyInfrastructureManager
from agents.time_dilation import TimeDilationSystem
from agents.vehicle_core_feeding import VehicleCoreFeeding
from agents.word_count_enforcer import WordCountEnforcer
from config import CHAPTER_GUIDE, MIN_WORD_COUNT
from conflict_tracker import ConflictTracker
from memory_manager import MemoryManager
from pipelines.pipeline_definitions import PIPELINES, get_pipeline, list_pipelines
from pipelines.pipeline_engine import PipelineEngine
from relationship_tracker import RelationshipTracker


class Orchestrator:
    """
    Main driver for the RP Conversion Novel Writing System.

    Usage from Windsurf chat:
        orchestrator = Orchestrator()
        result = orchestrator.write_chapter(chapter_num=1)
        result = orchestrator.write_chapter(chapter_num=5, pipeline="full_quality")
        result = orchestrator.generate_outline(chapter_start=1, chapter_end=20)
        result = orchestrator.summarize_chapter(chapter_num=3)
        result = orchestrator.check_lore(prose="...")
        result = orchestrator.check_continuity(prose="...")
        result = orchestrator.auto_write(start=1, end=10)
        result = orchestrator.query_database(query="Dravik", category="races")

    Commands (mapped to Windsurf chat triggers):
        "Write Chapter N"       → orchestrator.write_chapter(N)
        "Auto Write N-M"        → orchestrator.auto_write(N, M)
        "Outline Chapters N-M"  → orchestrator.generate_outline(N, M)
        "Summarize Chapter N"   → orchestrator.summarize_chapter(N)
        "Check Lore"            → orchestrator.check_lore(prose)
        "Check Continuity"      → orchestrator.check_continuity(prose)
        "Check Conflicts"       → orchestrator.check_conflicts()
        "Add Conflict"          → orchestrator.add_conflict(name, ...)
        "Show Relationships"    → orchestrator.show_relationships(character)
        "Query Database"        → orchestrator.query_database(query, category)
        "Extract Style"         → orchestrator.extract_style(sample)
        "List Pipelines"        → orchestrator.list_available_pipelines()
        "Show State"            → orchestrator.get_current_state()
        "Update State"          → orchestrator.update_story_state(updates)
    """

    def __init__(self) -> None:
        # Memory Manager
        self.memory = MemoryManager()
        self.memory.load_state()

        # Initialize all agents
        self.agents = {
            "lore_judge": LoreJudge(),
            "prose_writer": ProseWriter(),
            "refusal_checker": RefusalChecker(),
            "style_extractor": StyleExtractor(),
            "dialogue_specialist": DialogueSpecialist(),
            "plot_checker": PlotChecker(),
            "continuity_checker": ContinuityChecker(),
            "style_editor": StyleEditor(),
            "scene_beat_generator": SceneBeatGenerator(),
            "summarizer": Summarizer(),
            "outline_generator": OutlineGenerator(),
            "word_count_enforcer": WordCountEnforcer(),
            "parameter_enforcer": ParameterEnforcer(),
            "stat_currency_tracker": StatCurrencyTracker(),
            "database_manager": DatabaseManager(),
            "slice_of_life": SliceOfLifeSceneGenerator(),
            "tech_infrastructure": TechnologyInfrastructureManager(),
        }

        # Pipeline engine
        self.pipeline_engine = PipelineEngine()

        # Relationship & Conflict trackers
        self.relationships = RelationshipTracker()
        self.conflicts = ConflictTracker()

        # Specialized subsystems
        self.vehicle_core_feeding = VehicleCoreFeeding()
        self.time_dilation = TimeDilationSystem()

        # Load databases
        db_agent = self.agents["database_manager"]
        if isinstance(db_agent, DatabaseManager):
            db_agent.load_databases()

    # ── Core Writing Commands ────────────────────────────────

    def write_chapter(
        self,
        chapter_num: Optional[int] = None,
        pipeline: str = "full_quality",
        scene_beats: str = "",
        arc_name: str = "",
        tone: str = "",
        characters_present: str = "",
        additional_notes: str = "",
        custom_parameters: Optional[dict] = None,
    ) -> dict:
        """
        Write a complete chapter using the specified pipeline.

        This is the primary entry point for chapter generation.
        Called when the user says "Write Chapter N" in Windsurf chat.

        Args:
            chapter_num: Chapter number to write (auto-detects next if None).
            pipeline: Pipeline name to use (default: full_quality).
            scene_beats: Pre-defined scene beats (optional).
            arc_name: Current story arc name (optional, auto-detected).
            tone: Desired tone for the chapter (optional).
            characters_present: Characters in this chapter (optional).
            additional_notes: Extra instructions (optional).
            custom_parameters: Custom parameter overrides (optional).

        Returns:
            Dict with chapter content, metadata, and validation results.
        """
        # Determine chapter number
        if chapter_num is None:
            chapter_num = self.memory.get_next_chapter_number()

        # Auto-detect arc if not provided
        if not arc_name:
            arc_name = self._get_arc_for_chapter(chapter_num)

        # Build writing context from memory bank
        context = self.memory.build_writing_context(chapter_num)

        # Inject rolling context (last 3 chapter summaries)
        rolling = self._build_rolling_context(chapter_num)
        if rolling:
            context = rolling + "\n\n" + context

        # Inject relationship context for characters in this chapter
        rel_context = self.relationships.build_relationship_context()
        if rel_context:
            context += "\n\n" + rel_context

        # Inject conflict context
        conflict_context = self.conflicts.build_conflict_context(chapter_num)
        if conflict_context:
            context += "\n\n" + conflict_context

        # Inject database context
        db_agent = self.agents["database_manager"]
        if isinstance(db_agent, DatabaseManager):
            db_context = db_agent.build_context_for_chapter(
                chapter_num=chapter_num,
                location=self.memory.get_state().get("location", ""),
                factions_needed=True,
            )
            if db_context:
                context += "\n\n" + db_context

        # Get chapter guide data if available
        chapter_guide = self._get_chapter_guide_data(chapter_num)

        # Get previous chapter summary for continuity
        previous_summary = ""
        if chapter_num > 1:
            previous_summary = self.memory.get_chapter_summary(
                chapter_num - 1
            )

        # Build chapter kwargs for agents
        chapter_kwargs = {
            "chapter_num": chapter_num,
            "arc_name": arc_name,
            "tone": tone or chapter_guide.get("tone", ""),
            "characters_present": (
                characters_present
                or chapter_guide.get("characters", "")
            ),
            "scene_beats": scene_beats or chapter_guide.get("beats", ""),
            "additional_notes": additional_notes,
            "previous_summary": previous_summary,
            "objectives": chapter_guide.get("objectives", ""),
        }

        # Load and configure the pipeline
        pipeline_config = get_pipeline(pipeline)
        if pipeline_config is None:
            pipeline_config = PIPELINES["full_quality"]

        self.pipeline_engine.load_pipeline(pipeline_config, self.agents)

        # Build the execution plan
        result = {
            "chapter_num": chapter_num,
            "pipeline": pipeline_config["name"],
            "arc": arc_name,
            "context_loaded": True,
            "steps": [],
            "final_prose": "",
            "word_count": 0,
            "validations": {},
            "status": "ready",
        }

        # Return the prepared execution plan
        # In Windsurf, each pipeline step is executed by the AI
        # using the agent's system prompt and built prompt

        for i, step in enumerate(self.pipeline_engine.steps):
            agent = step.agent
            prompt = self.pipeline_engine.build_step_prompt(
                step=step,
                context=context,
                previous_output="",
                previous_result=None,
                chapter_kwargs=chapter_kwargs,
            )

            result["steps"].append({
                "step_number": i + 1,
                "agent_name": agent.name,
                "agent_role": agent.role,
                "system_prompt": agent.system_prompt,
                "user_prompt": prompt,
                "temperature": agent.temperature,
                "max_tokens": agent.max_tokens,
                "status": "pending",
            })

        result["status"] = "execution_plan_ready"
        result["instructions"] = (
            f"Execute each step in order. Step 1 uses the context directly. "
            f"Each subsequent step receives the output of the previous step. "
            f"After the final step, run word count and parameter enforcement. "
            f"Minimum word count: {MIN_WORD_COUNT} words."
        )

        return result

    def finalize_chapter(
        self,
        chapter_num: int,
        prose: str,
        custom_parameters: Optional[dict] = None,
    ) -> dict:
        """
        Finalize a chapter after pipeline execution.

        Runs word count enforcement, parameter enforcement, saves the
        chapter, generates a summary, and updates story state.

        Args:
            chapter_num: Chapter number being finalized.
            prose: The final prose text.
            custom_parameters: Custom parameters to enforce.

        Returns:
            Dict with save results and validation status.
        """
        result: dict = {
            "chapter_num": chapter_num,
            "validations": {},
            "saved": False,
            "status": "validating",
        }

        # Word count check
        wc_agent = self.agents["word_count_enforcer"]
        if not isinstance(wc_agent, WordCountEnforcer):
            raise TypeError("word_count_enforcer agent has wrong type")
        wc_result = wc_agent.check(prose)
        result["validations"]["word_count"] = wc_result

        # Parameter enforcement
        pe_agent = self.agents["parameter_enforcer"]
        if not isinstance(pe_agent, ParameterEnforcer):
            raise TypeError("parameter_enforcer agent has wrong type")
        pe_result = pe_agent.local_check(prose, custom_parameters)
        result["validations"]["parameters"] = pe_result

        # Refusal check
        rc_agent = self.agents["refusal_checker"]
        if not isinstance(rc_agent, RefusalChecker):
            raise TypeError("refusal_checker agent has wrong type")
        refusal_detected = rc_agent.quick_check(prose)
        result["validations"]["refusal_check"] = {
            "refusal_detected": refusal_detected,
            "status": "fail" if refusal_detected else "pass",
        }

        # Determine if all validations pass
        all_pass = (
            wc_result["meets_minimum"]
            and pe_result["all_passed"]
            and not refusal_detected
        )

        # Stat & currency tracking
        sct_agent = self.agents["stat_currency_tracker"]
        if not isinstance(sct_agent, StatCurrencyTracker):
            raise TypeError("stat_currency_tracker agent has wrong type")
        extracted = sct_agent.extract_changes(prose)
        state = self.memory.get_state()
        validation = sct_agent.validate_math(extracted, state)
        result["validations"]["stat_tracking"] = {
            "extracted_changes": extracted,
            "math_valid": validation["valid"],
            "issues": validation["issues"],
            "warnings": validation["warnings"],
        }

        if all_pass:
            # Save the chapter
            filepath = self.memory.save_chapter(chapter_num, prose)
            result["saved"] = True
            result["filepath"] = str(filepath)
            result["status"] = "complete"

            # Auto-apply extracted stat/currency changes to state
            if validation["valid"] and extracted["raw_extractions"]:
                state_update = sct_agent.build_state_update(
                    extracted, state
                )
                if state_update:
                    self.memory.update_state(state_update)
                result["state_updates_applied"] = state_update

            # Update story state
            state = self.memory.get_state()
            state["current_chapter"] = chapter_num
            self.memory.save_state()
        else:
            result["status"] = "validation_failed"
            result["issues"] = []
            if not wc_result["meets_minimum"]:
                result["issues"].append(
                    f"Word count: {wc_result['word_count']} / "
                    f"{wc_result['minimum']} minimum "
                    f"({wc_result['deficit']} words short)"
                )
            if not pe_result["all_passed"]:
                result["issues"].extend(pe_result["fails"])
            if refusal_detected:
                result["issues"].append("AI refusal patterns detected")

        result["word_count"] = len(prose.split())
        return result

    def save_chapter_summary(
        self, chapter_num: int, summary: str
    ) -> None:
        """Save a chapter summary for future context."""
        self.memory.save_chapter_summary(chapter_num, summary)

    # ── Outline Commands ─────────────────────────────────────

    def generate_outline(
        self,
        chapter_start: int = 1,
        chapter_end: int = 10,
        arc_name: str = "",
        scope: str = "multi_chapter",
        objectives: str = "",
    ) -> dict:
        """
        Generate a structured outline for one or more chapters.

        Args:
            chapter_start: First chapter number.
            chapter_end: Last chapter number.
            arc_name: Arc name (optional, auto-detected).
            scope: "chapter", "arc", or "multi_chapter".
            objectives: High-level objectives for the outline.

        Returns:
            Dict with outline generation plan.
        """
        if not arc_name:
            arc_name = self._get_arc_for_chapter(chapter_start)

        context = self.memory.build_writing_context(chapter_start)
        agent = self.agents["outline_generator"]

        prompt = agent.build_prompt(
            context,
            scope=scope,
            chapter_start=chapter_start,
            chapter_end=chapter_end,
            arc_name=arc_name,
            objectives=objectives,
        )

        return {
            "command": "generate_outline",
            "chapter_range": f"{chapter_start}-{chapter_end}",
            "arc": arc_name,
            "agent_name": agent.name,
            "system_prompt": agent.system_prompt,
            "user_prompt": prompt,
            "temperature": agent.temperature,
            "max_tokens": agent.max_tokens,
            "status": "ready",
        }

    def generate_scene_beats(
        self,
        chapter_num: int,
        arc_name: str = "",
        objectives: str = "",
        tone: str = "",
        characters: str = "",
    ) -> dict:
        """
        Generate scene beats for a specific chapter.

        Args:
            chapter_num: Chapter number.
            arc_name: Arc name (optional).
            objectives: Chapter objectives (optional).
            tone: Desired tone (optional).
            characters: Characters in the chapter (optional).

        Returns:
            Dict with scene beat generation plan.
        """
        if not arc_name:
            arc_name = self._get_arc_for_chapter(chapter_num)

        context = self.memory.build_writing_context(chapter_num)
        agent = self.agents["scene_beat_generator"]

        prompt = agent.build_prompt(
            context,
            chapter_num=chapter_num,
            arc_name=arc_name,
            objectives=objectives,
            tone=tone,
            characters=characters,
        )

        return {
            "command": "generate_scene_beats",
            "chapter_num": chapter_num,
            "agent_name": agent.name,
            "system_prompt": agent.system_prompt,
            "user_prompt": prompt,
            "temperature": agent.temperature,
            "max_tokens": agent.max_tokens,
            "status": "ready",
        }

    # ── Validation Commands ──────────────────────────────────

    def check_lore(self, prose: str, chapter_num: int = 0) -> dict:
        """
        Check prose against established lore.

        Args:
            prose: The prose text to validate.
            chapter_num: Chapter number for context.

        Returns:
            Dict with lore check plan.
        """
        context = self.memory.build_lore_context()
        agent = self.agents["lore_judge"]

        prompt = agent.build_prompt(
            context, prose=prose, chapter_num=chapter_num
        )

        return {
            "command": "check_lore",
            "agent_name": agent.name,
            "system_prompt": agent.system_prompt,
            "user_prompt": prompt,
            "temperature": agent.temperature,
            "max_tokens": agent.max_tokens,
            "status": "ready",
        }

    def check_continuity(self, prose: str, chapter_num: int = 0) -> dict:
        """
        Check prose for continuity issues.

        Args:
            prose: The prose text to validate.
            chapter_num: Chapter number for context.

        Returns:
            Dict with continuity check plan.
        """
        context = self.memory.build_writing_context(chapter_num)
        agent = self.agents["continuity_checker"]

        prompt = agent.build_prompt(
            context, prose=prose, chapter_num=chapter_num
        )

        return {
            "command": "check_continuity",
            "agent_name": agent.name,
            "system_prompt": agent.system_prompt,
            "user_prompt": prompt,
            "temperature": agent.temperature,
            "max_tokens": agent.max_tokens,
            "status": "ready",
        }

    def check_plot(self, prose: str, chapter_num: int = 0) -> dict:
        """
        Check prose for plot holes.

        Args:
            prose: The prose text to validate.
            chapter_num: Chapter number for context.

        Returns:
            Dict with plot check plan.
        """
        context = self.memory.build_writing_context(chapter_num)
        agent = self.agents["plot_checker"]

        prompt = agent.build_prompt(
            context, prose=prose, chapter_num=chapter_num
        )

        return {
            "command": "check_plot",
            "agent_name": agent.name,
            "system_prompt": agent.system_prompt,
            "user_prompt": prompt,
            "temperature": agent.temperature,
            "max_tokens": agent.max_tokens,
            "status": "ready",
        }

    # ── Enhancement Commands ─────────────────────────────────

    def polish_style(self, prose: str) -> dict:
        """Polish prose for style and flow."""
        agent = self.agents["style_editor"]
        prompt = agent.build_prompt("", prose=prose)

        return {
            "command": "polish_style",
            "agent_name": agent.name,
            "system_prompt": agent.system_prompt,
            "user_prompt": prompt,
            "temperature": agent.temperature,
            "max_tokens": agent.max_tokens,
            "status": "ready",
        }

    def improve_dialogue(
        self, prose: str, characters: str = ""
    ) -> dict:
        """Improve dialogue in prose."""
        context = self.memory.build_character_context()
        agent = self.agents["dialogue_specialist"]
        prompt = agent.build_prompt(
            context, prose=prose, characters=characters
        )

        return {
            "command": "improve_dialogue",
            "agent_name": agent.name,
            "system_prompt": agent.system_prompt,
            "user_prompt": prompt,
            "temperature": agent.temperature,
            "max_tokens": agent.max_tokens,
            "status": "ready",
        }

    def extract_style(self, sample_text: str) -> dict:
        """Extract writing style from sample text."""
        agent = self.agents["style_extractor"]
        prompt = agent.build_prompt("", sample_text=sample_text)

        return {
            "command": "extract_style",
            "agent_name": agent.name,
            "system_prompt": agent.system_prompt,
            "user_prompt": prompt,
            "temperature": agent.temperature,
            "max_tokens": agent.max_tokens,
            "status": "ready",
        }

    # ── Summary Commands ─────────────────────────────────────

    def summarize_chapter(self, chapter_num: int) -> dict:
        """
        Summarize a specific chapter.

        Args:
            chapter_num: Chapter number to summarize.

        Returns:
            Dict with summarization plan.
        """
        content = self.memory.read_chapter(chapter_num)
        if not content:
            return {
                "command": "summarize_chapter",
                "error": f"Chapter {chapter_num} not found.",
                "status": "error",
            }

        context = self.memory.build_writing_context(chapter_num)
        agent = self.agents["summarizer"]

        prompt = agent.build_prompt(
            context, content=content, chapter_num=chapter_num
        )

        return {
            "command": "summarize_chapter",
            "chapter_num": chapter_num,
            "agent_name": agent.name,
            "system_prompt": agent.system_prompt,
            "user_prompt": prompt,
            "temperature": agent.temperature,
            "max_tokens": agent.max_tokens,
            "status": "ready",
        }

    # ── Stat & Currency Tracking ────────────────────────────

    def track_stats(
        self, prose: str, chapter_num: int = 0
    ) -> dict:
        """
        Analyze prose for stat, currency, and progression changes.

        Two modes:
          - Local extraction (fast): regex-based parsing
          - AI analysis: deeper implicit change detection

        Args:
            prose: The chapter prose to analyze.
            chapter_num: Chapter number for context.

        Returns:
            Dict with extracted changes, validation, and AI prompt.
        """
        sct_agent = self.agents["stat_currency_tracker"]
        if not isinstance(sct_agent, StatCurrencyTracker):
            raise TypeError("stat_currency_tracker agent has wrong type")

        # Local extraction
        extracted = sct_agent.extract_changes(prose)
        state = self.memory.get_state()
        validation = sct_agent.validate_math(extracted, state)
        state_update = sct_agent.build_state_update(extracted, state)

        # Build AI prompt for deeper analysis
        prompt = sct_agent.build_prompt(
            "",
            prose=prose,
            chapter_num=chapter_num,
            current_state=state,
        )

        return {
            "command": "track_stats",
            "chapter_num": chapter_num,
            "local_extraction": extracted,
            "math_validation": validation,
            "proposed_state_update": state_update,
            "agent_name": sct_agent.name,
            "system_prompt": sct_agent.system_prompt,
            "user_prompt": prompt,
            "temperature": sct_agent.temperature,
            "max_tokens": sct_agent.max_tokens,
            "status": "ready",
            "instructions": (
                "Local extraction found "
                f"{len(extracted['raw_extractions'])} changes. "
                "Run the AI prompt for deeper analysis if needed. "
                "Use 'Apply Stat Changes' to apply the proposed update."
            ),
        }

    def apply_stat_changes(
        self, changes: dict, chapter_num: int = 0
    ) -> dict:
        """
        Apply extracted stat/currency changes to the story state.

        Args:
            changes: Dict from track_stats()["local_extraction"] or
                     parsed AI output.
            chapter_num: Chapter number (for logging).

        Returns:
            Dict with the applied updates and new state.
        """
        sct_agent = self.agents["stat_currency_tracker"]
        if not isinstance(sct_agent, StatCurrencyTracker):
            raise TypeError("stat_currency_tracker agent has wrong type")

        state = self.memory.get_state()
        validation = sct_agent.validate_math(changes, state)

        if not validation["valid"]:
            return {
                "command": "apply_stat_changes",
                "applied": False,
                "issues": validation["issues"],
                "warnings": validation["warnings"],
                "status": "validation_failed",
            }

        state_update = sct_agent.build_state_update(changes, state)
        if state_update:
            self.memory.update_state(state_update)

        return {
            "command": "apply_stat_changes",
            "chapter_num": chapter_num,
            "applied": True,
            "updates": state_update,
            "warnings": validation["warnings"],
            "new_state": self.memory.get_state(),
            "status": "complete",
        }

    # ── State Commands ───────────────────────────────────────

    def get_current_state(self) -> dict:
        """Return the current story state."""
        return self.memory.get_state()

    def update_story_state(self, updates: dict) -> dict:
        """
        Update the story state with new values.

        Args:
            updates: Dict of state updates to apply.

        Returns:
            The updated state.
        """
        self.memory.update_state(updates)
        return self.memory.get_state()

    def list_available_pipelines(self) -> list:
        """List all available pipelines."""
        return list_pipelines()

    def get_chapter_status(self) -> dict:
        """Get overview of chapter completion status."""
        return {
            "total_chapters_written": self.memory.get_chapter_count(),
            "next_chapter": self.memory.get_next_chapter_number(),
            "current_state": self.memory.get_state(),
        }

    # ── Auto-Pilot Mode ────────────────────────────────────

    def auto_write(
        self,
        start: int = 1,
        end: int = 10,
        pipeline: str = "full_quality",
    ) -> dict:
        """
        Generate execution plans for multiple chapters in sequence.

        Auto-pilot mode queues chapters for sequential writing. Each
        chapter's output becomes context for the next. The rolling
        context window ensures continuity.

        Args:
            start: First chapter number.
            end: Last chapter number.
            pipeline: Pipeline to use for all chapters.

        Returns:
            Dict with queued chapter plans and instructions.
        """
        chapter_plans = []
        for ch in range(start, end + 1):
            plan = self.write_chapter(chapter_num=ch, pipeline=pipeline)
            chapter_plans.append({
                "chapter_num": ch,
                "arc": plan.get("arc", ""),
                "pipeline": plan.get("pipeline", ""),
                "step_count": len(plan.get("steps", [])),
                "status": "queued",
            })

        return {
            "command": "auto_write",
            "range": f"{start}-{end}",
            "total_chapters": end - start + 1,
            "pipeline": pipeline,
            "chapters": chapter_plans,
            "status": "execution_plan_ready",
            "instructions": (
                f"Execute chapters {start} through {end} sequentially. "
                f"For each chapter:\n"
                f"1. Run 'Write Chapter N' to get the execution plan\n"
                f"2. Execute each pipeline step in order\n"
                f"3. Run 'Finalize Chapter N' with the prose\n"
                f"4. The system auto-injects the last 3 chapter summaries "
                f"into the next chapter's context (rolling window)\n"
                f"5. Conflicts and relationships are tracked automatically\n"
                f"6. Stats and currency are extracted and validated\n"
                f"After each chapter, generate a summary and save it "
                f"before proceeding to the next chapter."
            ),
        }

    # ── Database Query Commands ──────────────────────────────

    def query_database(
        self,
        query: str = "",
        category: str = "",
        tier: Optional[int] = None,
        race: str = "",
        entry_type: str = "",
    ) -> dict:
        """
        Query the structured YAML databases.

        Args:
            query: Search term (name-based search).
            category: Database category filter (races, monsters, etc.).
            tier: Tier filter.
            race: Race/species filter.
            entry_type: Entry type filter.

        Returns:
            Dict with search results.
        """
        db_agent = self.agents["database_manager"]
        if not isinstance(db_agent, DatabaseManager):
            return {"error": "DatabaseManager not available"}

        results: list = []
        if query:
            results = db_agent.query_by_name(query, category)
        elif tier is not None:
            results = db_agent.query_by_tier(tier, category)
        elif race:
            results = db_agent.query_by_race(race)
        elif entry_type:
            results = db_agent.query_by_type(entry_type, category)
        elif category:
            cat_data = db_agent.get_full_category(category)
            return {
                "command": "query_database",
                "category": category,
                "files": list(cat_data.keys()),
                "file_count": len(cat_data),
                "status": "complete",
            }
        else:
            return {
                "command": "query_database",
                "summary": db_agent.get_stats_summary(),
                "status": "complete",
            }

        return {
            "command": "query_database",
            "query": query or f"tier={tier}" or f"race={race}" or f"type={entry_type}",
            "results_count": len(results),
            "results": results[:20],
            "status": "complete",
        }

    def get_database_stats(self) -> dict:
        """Get summary of all loaded databases."""
        db_agent = self.agents["database_manager"]
        if not isinstance(db_agent, DatabaseManager):
            return {"error": "DatabaseManager not available"}
        return db_agent.get_stats_summary()

    # ── Relationship Commands ────────────────────────────────

    def add_relationship(
        self,
        char_a: str,
        char_b: str,
        rel_type: str = "neutral",
        trust: int = 0,
        notes: str = "",
    ) -> dict:
        """Add or update a relationship between two characters."""
        entry = self.relationships.set_relationship(
            char_a, char_b, rel_type, trust, notes=notes,
        )
        return {
            "command": "add_relationship",
            "relationship": entry,
            "status": "complete",
        }

    def record_interaction(
        self,
        char_a: str,
        char_b: str,
        chapter: int,
        description: str,
        trust_change: int = 0,
    ) -> dict:
        """Record an interaction that affects a relationship."""
        entry = self.relationships.add_interaction(
            char_a, char_b, chapter, description, trust_change,
        )
        return {
            "command": "record_interaction",
            "relationship": entry,
            "status": "complete",
        }

    def show_relationships(self, character: str = "") -> dict:
        """Show relationships for a character or all relationships."""
        if character:
            rels = self.relationships.get_all_relationships_for(character)
        else:
            rels = list(self.relationships.get_all_relationships().values())
        return {
            "command": "show_relationships",
            "character": character or "all",
            "relationships": rels,
            "stats": self.relationships.get_stats(),
            "status": "complete",
        }

    # ── Conflict Commands ────────────────────────────────────

    def add_conflict(
        self,
        name: str,
        conflict_type: str = "personal",
        chapter: int = 0,
        participants: Optional[list] = None,
        stakes: str = "",
        description: str = "",
    ) -> dict:
        """Register a new plot conflict."""
        entry = self.conflicts.add_conflict(
            name, conflict_type, chapter,
            participants, stakes, description,
        )
        return {
            "command": "add_conflict",
            "conflict": entry,
            "status": "complete",
        }

    def update_conflict(
        self,
        conflict_id: str,
        new_state: str,
        chapter: int,
        event: str = "",
    ) -> dict:
        """Transition a conflict to a new state."""
        entry = self.conflicts.transition(
            conflict_id, new_state, chapter, event,
        )
        return {
            "command": "update_conflict",
            "conflict": entry,
            "status": "complete",
        }

    def resolve_conflict(
        self,
        conflict_id: str,
        chapter: int,
        resolution: str,
    ) -> dict:
        """Resolve a conflict."""
        entry = self.conflicts.resolve(conflict_id, chapter, resolution)
        return {
            "command": "resolve_conflict",
            "conflict": entry,
            "status": "complete",
        }

    def check_conflicts(self, current_chapter: int = 0) -> dict:
        """Get active conflicts and flag stale ones."""
        if current_chapter == 0:
            state = self.memory.get_state()
            current_chapter = state.get("current_chapter", 0)

        return {
            "command": "check_conflicts",
            "active": self.conflicts.get_active_conflicts(),
            "stale": self.conflicts.get_stale_conflicts(current_chapter),
            "dormant": self.conflicts.get_dormant_conflicts(),
            "resolved_count": len(self.conflicts.get_resolved_conflicts()),
            "stats": self.conflicts.get_stats(),
            "status": "complete",
        }

    # ── Internal Helpers ─────────────────────────────────────

    def _build_rolling_context(self, chapter_num: int, window: int = 3) -> str:
        """
        Build rolling context from the last N chapter summaries.

        This ensures chapter-to-chapter continuity by injecting recent
        summaries into the writing context automatically.

        Args:
            chapter_num: Current chapter being written.
            window: Number of previous chapters to include (default 3).

        Returns:
            Formatted string with recent chapter summaries.
        """
        if chapter_num <= 1:
            return ""

        sections = ["## ROLLING CONTEXT (Last 3 Chapters)"]
        found_any = False

        start = max(1, chapter_num - window)
        for i in range(start, chapter_num):
            summary = self.memory.get_chapter_summary(i)
            if summary:
                sections.append(f"### Chapter {i} Summary\n{summary}")
                found_any = True
            else:
                content = self.memory.read_chapter(i)
                if content:
                    sections.append(
                        f"### Chapter {i} (no summary — first 500 chars)\n"
                        f"{content[:500]}..."
                    )
                    found_any = True

        return "\n\n".join(sections) if found_any else ""

    def _get_arc_for_chapter(self, chapter_num: int) -> str:
        """Determine which arc a chapter belongs to."""
        arc_ranges = {
            "Day Zero": (1, 20),
            "The Scavenger": (21, 55),
            "Wolves and Worms": (56, 100),
            "First Blood Debt": (101, 150),
            "The Alien Question": (151, 200),
            "Underground King": (201, 250),
            "Warpath": (251, 310),
            "Into the Black": (311, 370),
            "The First Gate": (371, 430),
            "The Variable Grows": (431, 500),
        }
        for arc_name, (start, end) in arc_ranges.items():
            if start <= chapter_num <= end:
                return arc_name
        return "Beyond Book 1"

    def _get_chapter_guide_data(self, chapter_num: int) -> dict:
        """
        Extract chapter-specific data from the chapter guide.

        Returns a dict with keys: objectives, tone, characters, beats.
        Falls back to empty values if chapter guide data is unavailable.
        """
        guide_content = self.memory.read_file(CHAPTER_GUIDE)
        if not guide_content:
            return {
                "objectives": "",
                "tone": "",
                "characters": "",
                "beats": "",
            }

        # Search for chapter-specific section in the guide
        chapter_marker = f"Chapter {chapter_num}:"
        alt_marker = f"### Chapter {chapter_num}:"

        result = {
            "objectives": "",
            "tone": "",
            "characters": "",
            "beats": "",
        }

        lines = guide_content.split("\n")
        in_chapter = False
        section_content: list = []

        for line in lines:
            if chapter_marker in line or alt_marker in line:
                in_chapter = True
                continue
            elif in_chapter and line.startswith("### Chapter "):
                break
            elif in_chapter and line.startswith("## "):
                break
            elif in_chapter:
                section_content.append(line)

        if section_content:
            content = "\n".join(section_content)

            # Extract specific fields
            for line in section_content:
                stripped = line.strip()
                if stripped.startswith("**Tone:**"):
                    result["tone"] = stripped.replace("**Tone:**", "").strip()
                elif stripped.startswith("**Characters:**"):
                    result["characters"] = stripped.replace(
                        "**Characters:**", ""
                    ).strip()

            # Use the full section as objectives/beats
            result["objectives"] = content[:2000]

        return result

    # ── Vehicle Core Feeding Commands ─────────────────────────

    def feed_vehicle_core(
        self,
        resource_name: str,
        resource_tier: int = 0,
        quantity: int = 1,
        chapter_num: int = 0,
    ) -> dict:
        """
        Feed a resource to the Vehicle Core.

        Args:
            resource_name: Name of the resource to feed.
            resource_tier: Tier of the resource.
            quantity: Number of resources to feed.
            chapter_num: Chapter number for logging.

        Returns:
            Dict with feeding results.
        """
        state = self.memory.get_state()
        rp_balance = state.get("rp_balance", 0)

        result = self.vehicle_core_feeding.feed_core(
            resource_name=resource_name,
            resource_tier=resource_tier,
            quantity=quantity,
            rp_available=rp_balance,
            chapter_num=chapter_num,
        )

        if result.get("success"):
            self.memory.update_state({
                "vehicle_core_feeding_tier": self.vehicle_core_feeding.current_feeding_tier,
                "total_core_feedings": self.vehicle_core_feeding.total_feedings,
            })

        return {
            "command": "feed_vehicle_core",
            **result,
            "status": "complete" if result.get("success") else "failed",
        }

    def get_feeding_status(self) -> dict:
        """Get current Vehicle Core feeding status."""
        return {
            "command": "get_feeding_status",
            "current_tier": self.vehicle_core_feeding.get_feeding_tier_info(),
            "next_tier": self.vehicle_core_feeding.get_next_tier_requirements(),
            "summary": self.vehicle_core_feeding.get_feeding_summary(),
            "status": "complete",
        }

    def get_feeding_context(self) -> str:
        """Get feeding context for chapter writing."""
        return self.vehicle_core_feeding.build_feeding_context()

    # ── Time Dilation Commands ───────────────────────────────

    def activate_time_dilation(
        self,
        tier: int,
        duration_hours: int = 1,
        activity: str = "training",
        chapter_num: int = 0,
    ) -> dict:
        """
        Activate time dilation in the pocket dimension.

        Args:
            tier: Dilation tier to activate.
            duration_hours: Real-world hours to run dilation.
            activity: What to do during dilated time.
            chapter_num: Chapter number for logging.

        Returns:
            Dict with activation results.
        """
        state = self.memory.get_state()
        vehicle_tier = state.get("vehicle_tier", 0)
        rp_balance = state.get("rp_balance", 0)

        result = self.time_dilation.activate_dilation(
            tier=tier,
            vehicle_tier=vehicle_tier,
            rp_available=rp_balance,
            duration_hours=duration_hours,
            activity=activity,
            chapter_num=chapter_num,
        )

        return {
            "command": "activate_time_dilation",
            **result,
        }

    def get_dilation_status(self) -> dict:
        """Get current time dilation status."""
        state = self.memory.get_state()
        vehicle_tier = state.get("vehicle_tier", 0)
        return {
            "command": "get_dilation_status",
            "current_tier": self.time_dilation.get_tier_info(),
            "max_available": self.time_dilation.get_max_available_tier(vehicle_tier),
            "summary": self.time_dilation.get_dilation_summary(),
            "is_active": self.time_dilation.is_active,
            "status": "complete",
        }

    def get_dilation_context(self) -> str:
        """Get time dilation context for chapter writing."""
        state = self.memory.get_state()
        vehicle_tier = state.get("vehicle_tier", 0)
        return self.time_dilation.build_dilation_context(vehicle_tier)

    # ── Slice-of-Life Commands ───────────────────────────────

    def generate_slice_of_life(
        self,
        scene_type: str = "",
        chapter_num: int = 0,
        recent_events: str = "",
        mood: str = "",
        pacing_need: str = "",
    ) -> dict:
        """
        Generate a slice-of-life scene plan.

        Args:
            scene_type: Template ID or name (optional).
            chapter_num: Chapter number.
            recent_events: Recent story events for context.
            mood: Desired mood.
            pacing_need: Pacing category (after_action, between_arcs, etc.).

        Returns:
            Dict with scene generation plan.
        """
        context = self.memory.build_writing_context(chapter_num)
        agent = self.agents["slice_of_life"]

        prompt = agent.build_prompt(
            context,
            scene_type=scene_type,
            chapter_num=chapter_num,
            recent_events=recent_events,
            mood=mood,
            pacing_need=pacing_need,
        )

        return {
            "command": "generate_slice_of_life",
            "scene_type": scene_type or "auto",
            "chapter_num": chapter_num,
            "agent_name": agent.name,
            "system_prompt": agent.system_prompt,
            "user_prompt": prompt,
            "temperature": agent.temperature,
            "max_tokens": agent.max_tokens,
            "status": "ready",
        }

    def list_scene_templates(self) -> dict:
        """List available slice-of-life scene templates."""
        agent = self.agents["slice_of_life"]
        if not isinstance(agent, SliceOfLifeSceneGenerator):
            return {"error": "SliceOfLifeSceneGenerator not available"}
        templates = agent.get_all_templates()
        return {
            "command": "list_scene_templates",
            "templates": [
                {"id": t["id"], "name": t["name"], "tone": t["tone"]}
                for t in templates
            ],
            "pacing_categories": agent.get_pacing_categories(),
            "status": "complete",
        }

    def suggest_scene(self, pacing_need: str = "filler_breather") -> dict:
        """Suggest a scene template based on pacing needs."""
        agent = self.agents["slice_of_life"]
        if not isinstance(agent, SliceOfLifeSceneGenerator):
            return {"error": "SliceOfLifeSceneGenerator not available"}
        suggestions = agent.suggest_scene(pacing_need)
        return {
            "command": "suggest_scene",
            "pacing_need": pacing_need,
            "suggestions": suggestions,
            "status": "complete",
        }

    # ── Technology & Infrastructure Commands ─────────────────

    def get_tech_context(
        self,
        tech_category: str = "",
        chapter_num: int = 0,
    ) -> dict:
        """
        Get technology/infrastructure context for writing.

        Args:
            tech_category: Specific category (vr, networking, energy, etc.).
            chapter_num: Chapter for context.

        Returns:
            Dict with technology context.
        """
        agent = self.agents["tech_infrastructure"]
        if not isinstance(agent, TechnologyInfrastructureManager):
            return {"error": "TechnologyInfrastructureManager not available"}

        state = self.memory.get_state()
        vehicle_tier = state.get("vehicle_tier", 0)

        context = agent.build_tech_context(vehicle_tier)

        if tech_category:
            category_map = {
                "vr": agent.get_vr_info,
                "networking": agent.get_networking_info,
                "energy": agent.get_energy_info,
                "battery": agent.get_battery_info,
                "production": agent.get_production_info,
                "marketing": agent.get_marketing_info,
                "software": agent.get_software_info,
            }
            getter = category_map.get(tech_category)
            if getter:
                return {
                    "command": "get_tech_context",
                    "category": tech_category,
                    "data": getter(),
                    "status": "complete",
                }

        return {
            "command": "get_tech_context",
            "context": context,
            "vehicle_tier": vehicle_tier,
            "status": "complete",
        }

    def __repr__(self) -> str:
        state = self.memory.get_state()
        return (
            f"<Orchestrator("
            f"chapter={state.get('current_chapter', 0)}, "
            f"agents={len(self.agents)}, "
            f"pipelines={len(PIPELINES)})>"
        )
