"""
Base Agent — Abstract foundation for all AI agents in the system.

Every agent inherits from BaseAgent and implements its own system prompt
and processing logic. The base class provides shared infrastructure for
prompt construction, context injection, and result formatting.
"""

class BaseAgent:
    """
    Abstract base class for all novel writing AI agents.

    Subclasses must set:
        - name: Human-readable agent name
        - role: Brief role description
        - system_prompt: Full system prompt for the AI
        - temperature: Generation temperature
        - max_tokens: Maximum output tokens

    Subclasses must implement:
        - build_prompt(context, **kwargs) -> str
        - parse_result(raw_output) -> dict
    """

    name: str = "Base Agent"
    role: str = "Base"
    system_prompt: str = ""
    temperature: float = 0.50
    max_tokens: int = 2048

    def __init__(self) -> None:
        self._last_input: str = ""
        self._last_output: str = ""

    def build_prompt(self, context: str, **kwargs: object) -> str:
        """
        Build the user-facing prompt for this agent.

        Args:
            context: The story context (lore, state, previous chapters, etc.)
            **kwargs: Agent-specific parameters.

        Returns:
            The assembled prompt string to send to the AI.
        """
        raise NotImplementedError("Subclasses must implement build_prompt()")

    def parse_result(self, raw_output: str) -> dict:
        """
        Parse the raw AI output into a structured result.

        Args:
            raw_output: The raw text output from the AI.

        Returns:
            A dict with at minimum {"status": str, "output": str}.
        """
        raise NotImplementedError("Subclasses must implement parse_result()")

    def get_system_message(self) -> dict:
        """Return the system message dict for API calls."""
        return {
            "role": "system",
            "content": self.system_prompt,
        }

    def get_config(self) -> dict:
        """Return the agent's configuration."""
        return {
            "name": self.name,
            "role": self.role,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }

    def format_instruction(self, context: str, instruction: str) -> str:
        """Combine context and instruction into a single prompt."""
        parts = []
        if context:
            parts.append(f"## CONTEXT\n{context}")
        if instruction:
            parts.append(f"## INSTRUCTION\n{instruction}")
        return "\n\n".join(parts)

    def record_io(self, input_text: str, output_text: str) -> None:
        """Record the last input/output for debugging."""
        self._last_input = input_text
        self._last_output = output_text

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(name={self.name!r}, role={self.role!r})>"
