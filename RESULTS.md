# Measured results

Five tasks were run live against three current Claude models (Opus 4.8,
Sonnet 4.6, Haiku 4.5) via the Anthropic API, spanning easy to deliberately
hard and two scoring methods (string-match and code-execution). Quality is the
mean score on each task's labeled examples; cost is real, from per-call token
usage. Projected monthly cost assumes 100,000 requests. Pricing as of
2026-07-02 (Sonnet 4.6 on introductory pricing through 2026-08-31, verify at
claude.com/pricing).

## Summary

| task | difficulty | Haiku | Sonnet | Opus | frontier | premium justified? |
|------|-----------|------:|-------:|-----:|----------|:---:|
| News classification (AG News, 100) | easy | 88% | 91% | 91% | Haiku, Sonnet | no (Opus dominated) |
| Invoice extraction, clean (60) | easy | 100% | 100% | 100% | Haiku | no (Opus dominated) |
| Support-intent classification (50) | harder | 96% | 96% | 96% | Haiku | no (all tied) |
| Invoice extraction, messy (60) | harder | 97% | 97% | 96% | Haiku | no (all tied) |
| **Code correctness (10 problems, 43 tests)** | **hard** | **70%** | **100%** | **100%** | **Haiku, Sonnet** | **partly (Haiku short; Opus dominated)** |

## The finding

**Across every task tested, the most expensive model (Opus 4.8) was never on
the cost/quality frontier.** On four of five tasks it was dominated outright -
matching cheaper models' quality at up to 5x the cost. Only the coding task
opened a real quality gap, and even there Opus was dominated by Sonnet (both
100%, Opus at ~3x the price).

What changed across the difficulty range was not whether the *premium* model was
worth it, it never was, but whether the *cheapest* model was good enough:

- **Easy and moderately hard tasks (4 of 5):** models converged. Even
  deliberately harder NLP, ambiguous support-ticket intent, messy invoices with
  decoy line items and noise, failed to separate them. Current small models
  handle practical business NLP as well as flagships. Cheapest model wins.
- **Code correctness (the one hard task):** models separated. Haiku dropped to
  70% (failing trickier problems like interval merging and spiral traversal),
  while Sonnet caught Opus at 100%. Here the cheap model is no longer sufficient
 , but the efficient choice is the *mid-tier* Sonnet, not the flagship.

## The takeaway

The right model depends on task difficulty, and you cannot know where that line
falls without measuring on your own task. But the direction of the surprise is
consistent: **the flagship was never the rational choice.** On easy tasks buy
the cheapest; on genuinely hard tasks (like code) step up to the mid-tier, but
paying for the top model bought no measurable quality on any task in this suite.
That is the entire argument against defaulting to the biggest model, and it is
why this tool measures rather than guesses.

## Honesty notes

- Sample sizes are small (10 to 100 examples). Ties ("no measurable difference")
  mean the models were indistinguishable *on this sample*, not that they are
  equal in general. Haiku's 70% on code is a clear, real drop; the Sonnet-vs-Opus
  100% ties break on cost, not a proven quality equality.
- The coding task was added deliberately to probe where a premium might be
  justified, after the NLP tasks showed no gap, a boundary-test, reported as-is.
- Prices drift; all figures are dated above.

## Reproducing

Offline (no key) shows the pipeline; `--mode api` with an `ANTHROPIC_API_KEY`
produces live numbers. Results here were produced via a hosted notebook to avoid
local TLS-inspection interfering with the HTTPS handshake, the tool itself is
unchanged.

```bash
python -m llmfrontier.cli run examples/ag_news_task.json --mode api \
    --models claude-opus-4-8 claude-sonnet-4-6 claude-haiku-4-5-20251001 \
    --volume 100000 --min-quality 0.85
```
