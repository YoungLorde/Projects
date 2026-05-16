"""
Pipeline Engine — Executes agent workflows in sequence.

Manages the flow of data between agents, handles conditional logic
(e.g., re-prompting after a refusal or lore violation), and tracks
pipeline execution state for debugging and logging.
"""

from typing import Optional

from agents.base_agent import BaseAgent


class PipelineStep:
    """Represents a single step in a pipeline."""

    def __init__(
        self,
        agent: BaseAgent,
        step_number: int,
        is_conditional: bool = False,
        condition_field: str = "",
        condition_value: str = "",
    ) -> None:
        self.agent = agent
        self.step_number = step_number
        self.is_conditional = is_conditional
        self.condition_field = condition_field
        self.condition_value = condition_value
        self.input_text: str = ""
        self.output_text: str = ""
        self.result: dict = {}
        self.skipped: bool = False

    def should_execute(self, previous_result: Optional[dict]) -> bool:
        """Determine if this step should execute based on conditions."""
        if not self.is_conditional:
            return True
        if previous_result is None:
            return True
        return previous_result.get(self.condition_field) == self.condition_value

    def __repr__(self) -> str:
        status = "skipped" if self.skipped else "ready"
        return (
            f"<PipelineStep(#{self.step_number}, "
            f"agent={self.agent.name!r}, status={status!r})>"
        )


class PipelineEngine:
    """
    Executes agent pipelines — sequences of agents that process
    content through multiple stages.

    The engine handles:
    - Sequential agent execution
    - Data passing between steps (output of step N → input of step N+1)
    - Conditional execution (skip steps based on previous results)
    - Revision loops (re-run prose writer if lore/continuity issues found)
    - Execution logging and state tracking
    """

    def __init__(self) -> None:
        self.steps: list = []
        self.execution_log: list = []
        self.current_step: int = 0
        self.pipeline_name: str = ""

    def load_pipeline(self, pipeline_config: dict, agents: dict) -> None:
        """
        Load a pipeline configuration and resolve agent references.

        Args:
            pipeline_config: Pipeline definition dict with 'steps' list.
            agents: Dict mapping agent names to BaseAgent instances.
        """
        self.pipeline_name = pipeline_config.get("name", "Unknown Pipeline")
        self.steps = []
        self.execution_log = []
        self.current_step = 0

        step_configs = pipeline_config.get("steps", [])
        for i, agent_key in enumerate(step_configs):
            agent = agents.get(agent_key)
            if agent is None:
                raise ValueError(
                    f"Unknown agent '{agent_key}' in pipeline "
                    f"'{self.pipeline_name}'"
                )
            step = PipelineStep(agent=agent, step_number=i + 1)
            self.steps.append(step)

    def build_step_prompt(
        self,
        step: PipelineStep,
        context: str,
        previous_output: str,
        previous_result: Optional[dict],
        chapter_kwargs: dict,
    ) -> str:
        """
        Build the prompt for a pipeline step.

        For the first step, uses the original context.
        For subsequent steps, incorporates previous output.
        For revision steps (prose_writer after a checker), includes
        the checker's feedback as revision notes.
        """
        agent = step.agent

        # Determine if this is a revision step
        is_revision = (
            agent.name == "Prose Writer"
            and previous_result is not None
            and previous_result.get("needs_revision", False)
        )

        if is_revision:
            # Build revision notes from previous checker output
            issues = previous_result.get("issues", [])
            revision_notes = "\n".join(
                f"- {issue.get('issue', '')} "
                f"(Fix: {issue.get('suggestion', 'address this')})"
                for issue in issues
            )
            chapter_kwargs["revision_notes"] = revision_notes
            chapter_kwargs["prose"] = previous_output

        # Different agents need different kwargs
        agent_name = agent.name.lower().replace(" ", "_")

        if agent_name in ("lore_judge", "continuity_checker", "plot_checker"):
            return agent.build_prompt(
                context,
                prose=previous_output,
                chapter_num=chapter_kwargs.get("chapter_num", 1),
            )
        elif agent_name == "refusal_checker":
            return agent.build_prompt(context, prose=previous_output)
        elif agent_name == "style_editor":
            return agent.build_prompt(context, prose=previous_output)
        elif agent_name == "dialogue_specialist":
            return agent.build_prompt(
                context,
                prose=previous_output,
                characters=chapter_kwargs.get("characters_present", ""),
            )
        elif agent_name == "summarizer":
            return agent.build_prompt(
                context,
                content=previous_output or context,
                chapter_num=chapter_kwargs.get("chapter_num", 1),
            )
        else:
            return agent.build_prompt(context, **chapter_kwargs)

    def get_execution_summary(self) -> dict:
        """Return a summary of the pipeline execution."""
        return {
            "pipeline": self.pipeline_name,
            "total_steps": len(self.steps),
            "completed_steps": self.current_step,
            "log": self.execution_log,
            "steps": [
                {
                    "number": step.step_number,
                    "agent": step.agent.name,
                    "skipped": step.skipped,
                    "has_output": bool(step.output_text),
                }
                for step in self.steps
            ],
        }

    def log_step(
        self, step_number: int, agent_name: str,
        status: str, details: str = "",
    ) -> None:
        """Add an entry to the execution log."""
        self.execution_log.append({
            "step": step_number,
            "agent": agent_name,
            "status": status,
            "details": details,
        })

    def __repr__(self) -> str:
        return (
            f"<PipelineEngine(pipeline={self.pipeline_name!r}, "
            f"steps={len(self.steps)}, current={self.current_step})>"
        )
