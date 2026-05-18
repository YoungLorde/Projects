"""
AI Agents for the RP Conversion Novel Writing System.

Each agent is a specialized module with a defined role, system prompt,
and configuration. Agents are coordinated by the Orchestrator through
configurable Pipelines.
"""

from agents.base_agent import BaseAgent
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

__all__ = [
    "BaseAgent",
    "LoreJudge",
    "ProseWriter",
    "RefusalChecker",
    "StyleExtractor",
    "DialogueSpecialist",
    "PlotChecker",
    "ContinuityChecker",
    "StyleEditor",
    "SceneBeatGenerator",
    "Summarizer",
    "OutlineGenerator",
    "WordCountEnforcer",
    "ParameterEnforcer",
    "StatCurrencyTracker",
    "DatabaseManager",
    "VehicleCoreFeeding",
    "TimeDilationSystem",
    "SliceOfLifeSceneGenerator",
    "TechnologyInfrastructureManager",
]
