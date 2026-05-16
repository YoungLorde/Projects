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
from agents.stat_currency_tracker import StatCurrencyTracker
from agents.word_count_enforcer import WordCountEnforcer
from config import CHAPTER_GUIDE, MIN_WORD_COUNT
from memory_manager import MemoryManager
from pipelines.pipeline_definitions import PIPELINES, get_pipeline, list_pipelines
from pipelines.pipeline_engine import PipelineEngine


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

    Commands (mapped to Windsurf chat triggers):
        "Write Chapter N"       → orchestrator.write_chapter(N)
        "Outline Chapters N-M"  → orchestrator.generate_outline(N, M)
        "Summarize Chapter N"   → orchestrator.summarize_chapter(N)
        "Check Lore"            → orchestrator.check_lore(prose)
        "Check Continuity"      → orchestrator.check_continuity(prose)
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
        }

        # Pipeline engine
        self.pipeline_engine = PipelineEngine()

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

    # ── Internal Helpers ─────────────────────────────────────

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

    def __repr__(self) -> str:
        state = self.memory.get_state()
        return (
            f"<Orchestrator("
            f"chapter={state.get('current_chapter', 0)}, "
            f"agents={len(self.agents)}, "
            f"pipelines={len(PIPELINES)})>"
        )
