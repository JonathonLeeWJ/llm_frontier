"""
Command-line interface.

    python -m llmfrontier.cli run task.json --volume 100000 --min-quality 0.9

The task file is JSON:

    {
      "name": "sentiment",
      "task_type": "classification",
      "prompt_template": "Classify sentiment as positive/negative/neutral.\\nText: {input}\\nLabel:",
      "subset_match": false,
      "examples": [
        {"input": "I love this", "expected": "positive"},
        {"input": "This is terrible", "expected": "negative"}
      ]
    }

By default it runs in --mode mock (no API keys). Use --mode api with the
relevant provider keys in the environment to hit real models.
"""

from __future__ import annotations

import argparse
import json
import sys

from .pricing import MODELS
from .report import format_report, to_records
from .runner import evaluate_all
from .tasks import Example, Task


def load_task(path: str) -> Task:
    with open(path) as f:
        data = json.load(f)
    examples = [Example(input=e["input"], expected=e["expected"]) for e in data["examples"]]
    return Task(
        name=data["name"],
        task_type=data["task_type"],
        prompt_template=data["prompt_template"],
        examples=examples,
        subset_match=data.get("subset_match", False),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="llmfrontier")
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Evaluate a task across models.")
    run.add_argument("task", help="Path to task JSON file.")
    run.add_argument("--volume", type=int, default=100_000,
                     help="Projected request volume for cost projection.")
    run.add_argument("--min-quality", type=float, default=None,
                     help="Minimum acceptable quality in [0,1] for a recommendation.")
    run.add_argument("--models", nargs="*", default=None,
                     help="Subset of models to test (default: all known).")
    run.add_argument("--mode", choices=["mock", "api"], default="mock",
                     help="'mock' (offline, no keys) or 'api' (real calls).")
    run.add_argument("--export", default=None,
                     help="Optional path to write results as JSON records.")

    args = parser.parse_args(argv)

    if args.command == "run":
        task = load_task(args.task)
        models = args.models or list(MODELS)
        results = evaluate_all(task, models, mode=args.mode)
        print(format_report(results, volume=args.volume, min_quality=args.min_quality))
        if args.export:
            with open(args.export, "w") as f:
                json.dump(to_records(results, args.volume), f, indent=2)
            print(f"\nExported records to {args.export}")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
