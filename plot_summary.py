"""
Plot the cost/quality frontier from an exported records JSON.

    python examples/plot_frontier.py out.json frontier.png

Kept out of the core package so matplotlib stays an optional, example-only
dependency. The frontier line connects only Pareto-efficient points; dominated
models are shown greyed out.
"""

import json
import sys

import matplotlib.pyplot as plt


def main(records_path: str, out_path: str = "frontier.png") -> None:
    with open(records_path) as f:
        records = json.load(f)

    fig, ax = plt.subplots(figsize=(8, 5.5))

    frontier = sorted(
        [r for r in records if r["on_frontier"]],
        key=lambda r: r["cost_per_request"],
    )
    dominated = [r for r in records if not r["on_frontier"]]

    if frontier:
        ax.plot(
            [r["cost_per_request"] for r in frontier],
            [r["quality"] for r in frontier],
            "-o", color="#1f77b4", label="Pareto frontier", zorder=3,
        )
    for r in frontier:
        ax.annotate(r["model"], (r["cost_per_request"], r["quality"]),
                    textcoords="offset points", xytext=(6, 6), fontsize=8)

    if dominated:
        ax.scatter(
            [r["cost_per_request"] for r in dominated],
            [r["quality"] for r in dominated],
            color="#bbbbbb", label="dominated", zorder=2,
        )
        for r in dominated:
            ax.annotate(r["model"], (r["cost_per_request"], r["quality"]),
                        textcoords="offset points", xytext=(6, -10),
                        fontsize=8, color="#888888")

    ax.set_xlabel("Cost per request (USD)")
    ax.set_ylabel("Quality (score on your labeled examples)")
    ax.set_title("LLM cost / quality frontier")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "frontier.png")
