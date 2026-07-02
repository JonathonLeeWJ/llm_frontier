"""
Model clients.

A client turns a prompt into (text, input_tokens, output_tokens, latency_s).
Token counts drive cost, so they must be real, not estimated, whenever the
provider returns usage.

Two kinds of client:

  MockClient   - deterministic, offline, no API key. Lets anyone clone the repo
                 and see the full frontier immediately. Its "quality" is
                 simulated per-model so the demo is meaningful.
  APIClient    - thin wrappers for OpenAI / Anthropic. Used when API keys are
                 present. Kept minimal on purpose; extend as needed.

The runner is agnostic — it just needs .complete(prompt) -> Completion.
"""

from __future__ import annotations

import hashlib
import os
import time
from dataclasses import dataclass


@dataclass
class Completion:
    text: str
    input_tokens: int
    output_tokens: int
    latency_s: float


def _rough_token_count(text: str) -> int:
    """~4 chars/token heuristic. Only used when a provider omits usage."""
    return max(1, len(text) // 4)


class BaseClient:
    def __init__(self, model: str):
        self.model = model

    def complete(self, prompt: str) -> Completion:  # pragma: no cover
        raise NotImplementedError


class MockClient(BaseClient):
    """Offline client. Simulates both cost and a per-model quality profile.

    Quality is simulated by giving each model a 'competence' in [0,1] and
    returning the correct answer with that probability (deterministically
    seeded by model+prompt so runs are reproducible). This makes the frontier
    demo show real trade-offs without any network calls.
    """

    # Higher = more often correct in the simulation. Roughly tracks capability
    # tiers so the demo frontier is intuitive (frontier tools should never
    # ship with a flat/fake demo).
    COMPETENCE = {
        "claude-opus-4-8": 0.96,
        "claude-sonnet-4-6": 0.92,
        "claude-haiku-4-5-20251001": 0.83,
        "gpt-4o": 0.95,
        "gpt-4o-mini": 0.82,
    }

    def __init__(self, model: str, oracle: dict[str, str] | None = None):
        super().__init__(model)
        # oracle maps prompt -> the ground-truth string the runner expects,
        # so the mock can "sometimes" return it based on competence.
        self.oracle = oracle or {}

    def _hash_unit(self, prompt: str) -> float:
        h = hashlib.sha256(f"{self.model}:{prompt}".encode()).hexdigest()
        return int(h[:8], 16) / 0xFFFFFFFF  # deterministic [0,1)

    def complete(self, prompt: str) -> Completion:
        competence = self.COMPETENCE.get(self.model, 0.7)
        roll = self._hash_unit(prompt)
        truth = self.oracle.get(prompt)
        if truth is not None and roll < competence:
            text = truth
        elif truth is not None:
            text = "WRONG_ANSWER"  # deterministically "misses"
        else:
            text = f"[mock:{self.model}] response to prompt"
        return Completion(
            text=text,
            input_tokens=_rough_token_count(prompt),
            output_tokens=_rough_token_count(text),
            latency_s=0.2 + self._hash_unit(prompt) * 0.3,
        )


class OpenAIClient(BaseClient):
    def __init__(self, model: str):
        super().__init__(model)
        from openai import OpenAI  # imported lazily so the dep is optional
        self._client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def complete(self, prompt: str) -> Completion:
        t0 = time.time()
        resp = self._client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        latency = time.time() - t0
        usage = resp.usage
        return Completion(
            text=resp.choices[0].message.content or "",
            input_tokens=usage.prompt_tokens,
            output_tokens=usage.completion_tokens,
            latency_s=latency,
        )


class AnthropicClient(BaseClient):
    def __init__(self, model: str):
        super().__init__(model)
        import anthropic  # lazy import
        self._client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    def complete(self, prompt: str) -> Completion:
        t0 = time.time()
        resp = self._client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        latency = time.time() - t0
        text = "".join(b.text for b in resp.content if b.type == "text")
        return Completion(
            text=text,
            input_tokens=resp.usage.input_tokens,
            output_tokens=resp.usage.output_tokens,
            latency_s=latency,
        )


def make_client(model: str, mode: str = "mock", oracle: dict[str, str] | None = None) -> BaseClient:
    """Factory. mode='mock' needs no keys; 'api' picks the right provider."""
    if mode == "mock":
        return MockClient(model, oracle=oracle)
    if mode == "api":
        from .pricing import get_model
        provider = get_model(model).provider
        if provider == "openai":
            return OpenAIClient(model)
        if provider == "anthropic":
            return AnthropicClient(model)
        raise ValueError(f"No API client wired for provider {provider!r}. Add one in clients.py.")
    raise ValueError(f"Unknown mode {mode!r} (expected 'mock' or 'api').")
