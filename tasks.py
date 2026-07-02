"""
Model pricing registry.

Prices are USD per 1,000,000 tokens (input / output). LLM prices change
often, so this is deliberately a plain, dated data structure you update by
hand rather than logic buried in code. Always report the `AS_OF` date to the
user so a stale price is never mistaken for a live one.

To add a model: add an entry to MODELS. The `provider` field is free text
used only for grouping/display. `context_window` is informational.
"""

from __future__ import annotations

from dataclasses import dataclass

# Update this whenever you refresh the numbers below.
AS_OF = "2026-07-02"


@dataclass(frozen=True)
class ModelPricing:
    name: str
    provider: str
    input_per_mtok: float   # USD per 1M input tokens
    output_per_mtok: float  # USD per 1M output tokens
    context_window: int

    def cost(self, input_tokens: int, output_tokens: int) -> float:
        """Cost in USD for a single request of the given token counts."""
        return (
            input_tokens / 1_000_000 * self.input_per_mtok
            + output_tokens / 1_000_000 * self.output_per_mtok
        )


# NOTE: These are illustrative list prices as of AS_OF. Verify against each
# provider's pricing page before relying on them — they are not guaranteed
# current, and this tool never pretends otherwise.
MODELS: dict[str, ModelPricing] = {
    # --- Current Claude models (verify against claude.com/pricing) ---
    # Note: Sonnet 4.6 is on introductory pricing of $2/$10 through
    # 2026-08-31, reverting to $3/$15 after. The $2/$10 rate is used here;
    # update when the intro period ends.
    "claude-opus-4-8": ModelPricing("claude-opus-4-8", "anthropic", 5.00, 25.00, 1_000_000),
    "claude-sonnet-4-6": ModelPricing("claude-sonnet-4-6", "anthropic", 2.00, 10.00, 1_000_000),
    "claude-haiku-4-5-20251001": ModelPricing("claude-haiku-4-5-20251001", "anthropic", 1.00, 5.00, 200_000),

    # --- OpenAI (kept for when billing is set up) ---
    "gpt-4o": ModelPricing("gpt-4o", "openai", 2.50, 10.00, 128_000),
    "gpt-4o-mini": ModelPricing("gpt-4o-mini", "openai", 0.15, 0.60, 128_000),
}


def get_model(name: str) -> ModelPricing:
    if name not in MODELS:
        raise KeyError(
            f"Unknown model {name!r}. Known: {', '.join(sorted(MODELS))}"
        )
    return MODELS[name]
