"""
The optimization core.

This is the part that makes the tool worth building: it treats model selection
as constrained optimization — minimize cost subject to quality >= threshold —
and exposes the full cost/quality trade-off as a Pareto frontier rather than a
single number.

Given a list of ModelResult (quality in [0,1], cost per request, latency), we:

  1. Identify the Pareto-efficient set (no other model is both cheaper AND
     better). Dominated models are never worth choosing and are flagged.
  2. Recommend an operating point given a minimum-quality constraint: the
     cheapest model that clears the bar.
  3. Find the "knee" — the frontier point with the best marginal quality per
     dollar, useful when the user has no hard threshold in mind.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ModelResult:
    model: str
    quality: float          # mean score in [0, 1] on the user's examples
    cost_per_request: float  # mean USD per request
    latency_s: float         # mean seconds per request
    n: int                   # number of examples evaluated

    def projected_cost(self, volume: int) -> float:
        return self.cost_per_request * volume


def pareto_frontier(results: list[ModelResult]) -> list[ModelResult]:
    """Return the Pareto-efficient models: maximize quality, minimize cost.

    A model is dominated if another is at least as cheap AND at least as good,
    and strictly better on at least one axis.
    """
    frontier: list[ModelResult] = []
    for r in results:
        dominated = any(
            (o.cost_per_request <= r.cost_per_request and o.quality >= r.quality)
            and (o.cost_per_request < r.cost_per_request or o.quality > r.quality)
            for o in results
            if o is not r
        )
        if not dominated:
            frontier.append(r)
    # Sort ascending by cost for a readable, plottable curve.
    return sorted(frontier, key=lambda r: r.cost_per_request)


def dominated_models(results: list[ModelResult]) -> list[ModelResult]:
    frontier_ids = {id(r) for r in pareto_frontier(results)}
    return [r for r in results if id(r) not in frontier_ids]


def recommend(
    results: list[ModelResult],
    min_quality: float,
) -> ModelResult | None:
    """Cheapest model meeting the quality bar. None if nothing qualifies."""
    qualifying = [r for r in results if r.quality >= min_quality]
    if not qualifying:
        return None
    return min(qualifying, key=lambda r: r.cost_per_request)


def knee_point(results: list[ModelResult]) -> ModelResult | None:
    """Frontier point of best 'bang per buck'.

    Uses the point that maximizes quality-per-cost among frontier models,
    with a small floor on cost to avoid divide-by-near-zero dominating.
    """
    frontier = pareto_frontier(results)
    if not frontier:
        return None
    return max(frontier, key=lambda r: r.quality / max(r.cost_per_request, 1e-9))


def savings_vs_best(results: list[ModelResult], volume: int) -> dict:
    """Compare the recommended-at-best-quality model to the top-quality model.

    Returns a summary dict quantifying the cost saving from picking the
    cheapest model that matches (within tolerance) the best model's quality.
    This is the headline 'X% of the quality at Y% of the cost' number.
    """
    if not results:
        return {}
    best = max(results, key=lambda r: r.quality)
    # Cheapest model within 2 percentage points of the best model's quality.
    close = [r for r in results if r.quality >= best.quality - 0.02]
    cheapest_close = min(close, key=lambda r: r.cost_per_request)
    best_cost = best.projected_cost(volume)
    picked_cost = cheapest_close.projected_cost(volume)
    return {
        "best_model": best.model,
        "best_quality": best.quality,
        "best_projected_cost": best_cost,
        "recommended_model": cheapest_close.model,
        "recommended_quality": cheapest_close.quality,
        "recommended_projected_cost": picked_cost,
        "quality_retained_pct": (cheapest_close.quality / best.quality * 100) if best.quality else 0.0,
        "cost_pct_of_best": (picked_cost / best_cost * 100) if best_cost else 0.0,
        "absolute_savings": best_cost - picked_cost,
    }
