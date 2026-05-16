"""
Pipeline system for orchestrating agent workflows.

Pipelines define sequences of agents that process content through
multiple stages, enabling quality-controlled prose generation.
"""

from pipelines.pipeline_definitions import PIPELINES, get_pipeline
from pipelines.pipeline_engine import PipelineEngine

__all__ = [
    "PipelineEngine",
    "PIPELINES",
    "get_pipeline",
]
