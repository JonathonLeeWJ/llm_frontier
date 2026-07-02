# llm-frontier

**Pick the cheapest LLM that still passes your eval.**

Everyone building with LLMs guesses at model selection: they default to the
biggest model out of caution, or the cheapest out of budget, without measuring
whether a cheaper model would actually pass their quality bar *on their own
task*. Pricing calculators tell you what a model costs. They don't tell you
whether you can get away with it.

`llm-frontier` treats model selection as what it is, **constrained
optimization**: minimize cost subject to `quality >= threshold`, where quality
is measured empirically on *your* labeled examples. It runs your task across
models, scores each against your labels, and returns the **cost/quality Pareto
frontier** with a recommended operating point.

```
Headline:
  gpt-4o-mini delivers 100% of gpt-4o's quality at 6% of the cost.
  Projected saving: $11.23/month (100,000 requests).
```

![five-task summary](examples/summary.png)

> **Measured on real models (5 tasks, easy to hard):** the most expensive model
> (Opus 4.8) was never on the cost/quality frontier. On four tasks it was
> dominated outright, matching cheaper models at up to 5x the cost. Only code
> correctness opened a real gap, and even there the *mid-tier* Sonnet caught
> Opus at 100% for a third of the price, while Haiku fell to 70%. The lesson:
> on easy tasks buy the cheapest; on hard tasks step up to mid-tier, but the
> flagship never earned its premium here. Full numbers and caveats in
> **[RESULTS.md](RESULTS.md)**.

<details>
<summary>Single-task Pareto frontier (news classification)</summary>

![frontier](examples/frontier.png)

Opus (greyed out) is dominated: same 91% quality as Sonnet at 3.4x the cost.
</details>

## Why this is different from a pricing calculator

A pricing calculator is a lookup table, it's a solved, commodity problem. The
neglected, actually-hard part is tying cost to *your* quality bar. That's the
whole tool:

- **Grounded in your task.** You supply a prompt and a handful of labeled
  examples. Quality is your measured score, not a generic benchmark.
- **Frontier, not a number.** Dominated models (something is both cheaper *and*
  better) are flagged and dropped, they're never the rational choice. You see
  the real trade-off curve.
- **A decision, not a metric.** Given a minimum-quality constraint, it names the
  cheapest model that clears the bar and projects the monthly saving.

## Quickstart (no API keys)

Runs fully offline against a mock backend with simulated per-model quality, so
you can see the whole pipeline immediately.

```bash
pip install -e .

# classification, 100 balanced examples from AG News (public, MIT)
python -m llmfrontier.cli run examples/ag_news_task.json \
    --volume 100000 --min-quality 0.85 --export out.json

# extraction, 60 invoice snippets, scored by field-level F1
python -m llmfrontier.cli run examples/invoice_extraction_task.json \
    --volume 100000 --min-quality 0.9

# optional plot
pip install matplotlib
python examples/plot_frontier.py out.json frontier.png
```

Three example tasks ship with the repo: `ag_news_task.json` (topic
classification), `invoice_extraction_task.json` (structured field extraction),
and `sentiment.json` (a tiny illustrative set). The first two are sized for
real quality estimates; run them with `--mode api` for measured results.

## Real model calls

```bash
pip install -e ".[api]"
export OPENAI_API_KEY=...     # and/or ANTHROPIC_API_KEY
python -m llmfrontier.cli run examples/sentiment.json --mode api \
    --models gpt-4o gpt-4o-mini claude-3-5-haiku --volume 100000 --min-quality 0.9
```

Token costs come from real provider `usage` on every call, not estimated.

## Defining a task

A task is a prompt template + labeled examples + a task type that picks the
scorer. JSON:

```json
{
  "name": "sentiment",
  "task_type": "classification",
  "prompt_template": "Classify sentiment as positive/negative/neutral.\nText: {input}\nLabel:",
  "examples": [
    {"input": "I love this", "expected": "positive"},
    {"input": "This is terrible", "expected": "negative"}
  ]
}
```

Supported task types (v1, all programmatically scorable):

| type | scorer | `expected` is |
|------|--------|---------------|
| `classification` | normalized exact match | a label string |
| `extraction` | field-level F1 | a flat `{field: value}` dict |
| `structured` | JSON equality (or subset) | the expected JSON object |

## Scope and honest limitations

- **v1 scores only tasks with checkable outputs** (classification, extraction,
  structured JSON). This is deliberate: it's the part that can be measured
  rigorously without introducing a noisy, costly judge.
- **Open-ended generation is out of scope for v1.** It needs LLM-as-judge, which
  is itself noisy and costs money. That's the v2 extension, and pretending it's
  solved would undermine the tool's whole premise.
- **Prices drift.** Pricing lives in one dated table (`pricing.py`,
  `AS_OF = 2026-01-01`) and every report prints the date. Update the table;
  don't trust a stale number.
- **Small example sets give noisy quality estimates.** Use enough labeled
  examples that a one-example flip doesn't move the recommendation. Reporting a
  confidence interval on quality is a natural next addition.

## Design

```
tasks.py      task definitions + deterministic scorers
clients.py    model backends (offline mock / OpenAI / Anthropic)
pricing.py    dated price table (single source of truth)
runner.py     runs each example, scores it, records real cost + latency
frontier.py   the optimization core: Pareto frontier, recommend, knee, savings
report.py     human-readable report + flat export
cli.py        command-line entry point
```

The core (`frontier.py`) is pure and separately tested, Pareto dominance,
constrained recommendation, knee-point, and the savings headline all have unit
tests in `tests/`.

## License

MIT.
