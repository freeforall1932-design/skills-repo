"""
Deterministic per-skill reward for the domain skills — offline, stdlib only.

Each domain skill has its own dataset (``scripts/build_domain_dataset.py``)
and is scored only against its own items. Scores are reported per skill and
never averaged together: the failure this guards against is a gated skill
(appsec running without scope, triage inventing behaviour) averaging out
against an easy one.

Item contract (ground truth authored with the dataset):

  * ``must_keep``  literal spans that must survive (numbers, ids, hashes)
  * ``hard_any``   list of alternative-groups; every group must hit (gate)
  * ``must_any``   list of alternative-groups; hits shape the soft reward
  * ``must_not``   literal spans whose presence hard-fails the item

Matching is case-insensitive substring matching. That is deliberately crude:
it checks that the output *engaged* the contract points (asked for scope,
named the fallback, kept the hash), not that the prose is good. A keyword
reward can be gamed by stuffing; it exists to catch contract violations and
regressions cheaply, and any training run must pair it with the held-out
validation discipline in TRAINING.md.
"""

from __future__ import annotations


def _hits(group: list[str], low: str) -> bool:
    return any(alt.lower() in low for alt in group)


def evaluate_domain(item: dict, output: str) -> dict:
    """Score one output against one domain item.

    Returns ``soft`` in [0, 1], the ``hard`` gate, and the violation list.
    Soft = 0.7 * group satisfaction (hard+soft groups) + 0.3 * kept-fraction,
    capped at 0.4 when a ``must_not`` span appears (a violation output must
    never out-score an honest thin one)."""
    low = (output or "").lower()
    violations: list[str] = []

    must_not_hits = [s for s in item.get("must_not", []) if s.lower() in low]
    for span in must_not_hits:
        violations.append(f"forbidden span present: {span!r}")

    hard_groups = item.get("hard_any", [])
    soft_groups = item.get("must_any", [])
    hard_missed = [g for g in hard_groups if not _hits(g, low)]
    for group in hard_missed:
        violations.append(f"hard group missed: {group!r}")

    keeps = item.get("must_keep", [])
    kept = [k for k in keeps if k.lower() in low]
    for missing in (k for k in keeps if k not in kept):
        violations.append(f"must_keep lost: {missing!r}")

    groups = hard_groups + soft_groups
    satisfied = sum(1 for g in groups if _hits(g, low))
    group_frac = satisfied / len(groups) if groups else 1.0
    keep_frac = len(kept) / len(keeps) if keeps else 1.0
    soft = 0.7 * group_frac + 0.3 * keep_frac
    if must_not_hits:
        soft = min(soft, 0.4)

    hard = not must_not_hits and not hard_missed and len(kept) == len(keeps)
    return {
        "id": item.get("id", ""),
        "skill": item.get("skill", ""),
        "soft": round(soft, 4),
        "hard": hard,
        "violations": violations,
    }
