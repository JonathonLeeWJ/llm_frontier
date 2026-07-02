"""llm-frontier: pick the cheapest LLM that still passes your eval."""

from .frontier import ModelResult, pareto_frontier, recommend, knee_point, savings_vs_best
from .report import format_report, to_records
from .runner import evaluate_all, evaluate_model
from .tasks import Example, Task

__version__ = "0.1.0"

__all__ = [
    "Task", "Example",
    "evaluate_all", "evaluate_model",
    "ModelResult", "pareto_frontier", "recommend", "knee_point", "savings_vs_best",
    "format_report", "to_records",
]
