"""Human-readable reporting over the optimization results."""

from __future__ import annotations

from .frontier import (
    ModelResult,
    dominated_models,
    knee_point,
    pareto_frontier,
    recommend,
    savings_vs_best,
)
from .pricing import AS_OF


def format_report(
    results: list[ModelResult],
    volume: int,
    min_quality: float | None = None,
) -> str:
    lines: list[str] = []
    add = lines.append

    add("=" * 68)
    add("LLM COST / QUALITY FRONTIER")
    add(f"Pricing as of {AS_OF} (verify against provider pages — prices drift)")
    add(f"Projected monthly volume: {volume:,} requests")
    add("=" * 68)

    add("")
    add("All models (sorted by cost):")
    add(f"  {'model':<22}{'quality':>9}{'$/req':>12}{'proj. $':>14}{'lat(s)':>9}")
    for r in sorted(results, key=lambda x: x.cost_per_request):
        add(
            f"  {r.model:<22}{r.quality:>8.1%}{r.cost_per_request:>12.6f}"
            f"{r.projected_cost(volume):>14,.2f}{r.latency_s:>9.2f}"
        )

    frontier = pareto_frontier(results)
    add("")
    add("Pareto-efficient models (no other is both cheaper and better):")
    for r in frontier:
        add(f"  * {r.model:<22} quality {r.quality:.1%}  @  ${r.cost_per_request:.6f}/req")

    dominated = dominated_models(results)
    if dominated:
        add("")
        add("Dominated — never the rational choice (something beats them on both axes):")
        for r in dominated:
            add(f"  x {r.model}")

    knee = knee_point(results)
    if knee:
        add("")
        add(f"Best bang-per-buck (knee): {knee.model} "
            f"— {knee.quality:.1%} quality at ${knee.cost_per_request:.6f}/req")

    if min_quality is not None:
        add("")
        add(f"Constraint: quality >= {min_quality:.0%}")
        rec = recommend(results, min_quality)
        if rec is None:
            add("  No model meets this quality bar. Loosen the constraint or "
                "improve the prompt.")
        else:
            add(f"  Recommended: {rec.model} "
                f"— cheapest that clears the bar "
                f"(${rec.projected_cost(volume):,.2f}/month at {rec.quality:.1%}).")

    s = savings_vs_best(results, volume)
    if s:
        add("")
        add("Headline:")
        if s["recommended_model"] == s["best_model"]:
            # Cheapest model is also the highest-quality one: nothing to trade.
            add(f"  {s['recommended_model']} is both the highest-quality and "
                f"cheapest option here — the premium models are dominated.")
        else:
            add(f"  {s['recommended_model']} delivers {s['quality_retained_pct']:.0f}% of "
                f"{s['best_model']}'s quality at {s['cost_pct_of_best']:.0f}% of the cost.")
            add(f"  Projected saving: ${s['absolute_savings']:,.2f}/month "
                f"({volume:,} requests).")

    add("=" * 68)
    return "\n".join(lines)


def to_records(results: list[ModelResult], volume: int) -> list[dict]:
    """Flat export for CSV/JSON or plotting."""
    frontier_ids = {id(r) for r in pareto_frontier(results)}
    return [
        {
            "model": r.model,
            "quality": round(r.quality, 4),
            "cost_per_request": round(r.cost_per_request, 8),
            "projected_cost": round(r.projected_cost(volume), 4),
            "latency_s": round(r.latency_s, 3),
            "n_examples": r.n,
            "on_frontier": id(r) in frontier_ids,
        }
        for r in sorted(results, key=lambda x: x.cost_per_request)
    ]
