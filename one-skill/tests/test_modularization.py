"""The modularization experiment, as a regression test.

Question: should one-skill's three published fragments replace the unified
skill as separately routed skills? Policy (docs/decisions.md): adopt only
if coverage is equal or better within budgets. It is not — the numbers
below are pinned so the decision re-opens automatically if the artifacts
change shape. Method and limits: docs/modularization-experiment.md.
"""

import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ONE_SKILL = HERE.parent
REPO = ONE_SKILL.parent
sys.path.insert(0, str(ONE_SKILL))

import build as b  # noqa: E402


def _experiment():
    man = b.Manifest(b.MANIFEST_PATH)
    families = {f["id"]: set(f["buckets"]) for f in man.data["families"]}
    frag_words = {
        fid: len(b.read(REPO / "claude-skills" / "fragments" / f"one-skill-{fid}" / "SKILL.md").split())
        for fid in families
    }
    unified_words = len(b.read(REPO / "claude-skills" / "app" / "one-skill" / "SKILL.md").split())
    cases = json.loads(b.read(HERE / "fragment_fixtures.json"))["cases"]

    rows = []
    for case in cases:
        need = set(case["buckets"])
        # smallest set of fragments covering the need (exact set cover)
        cover = None
        for r in range(1, len(families) + 1):
            for combo in itertools.combinations(sorted(families), r):
                if need <= set().union(*(families[c] for c in combo)):
                    cover = combo
                    break
            if cover:
                break
        rows.append({
            "task": case["task"],
            "cover": cover,
            "single": cover is not None and len(cover) == 1,
            "frag_words": sum(frag_words[c] for c in cover) if cover else None,
        })
    return rows, unified_words, frag_words


def test_unified_beats_fragments_on_coverage_and_cost():
    rows, unified_words, _ = _experiment()
    assert unified_words == 2394 and unified_words <= 2400
    # Unified: one load covers every case by construction (all 11 buckets).
    # Single-fragment routing (host loads top-1 only) covers 7/12.
    assert sum(r["single"] for r in rows) == 7
    cross = [r for r in rows if not r["single"]]
    assert len(cross) == 5
    # Even with perfect multi-loading, cross-family tasks cost more
    # always-on words than the unified skill.
    for r in cross:
        assert r["frag_words"] > unified_words, r
    # And single-family savings are negligible: fragments carry the same
    # core, so the cheapest fragment still costs >= 90% of unified.
    singles = [r for r in rows if r["single"]]
    assert min(r["frag_words"] for r in singles) >= 0.9 * unified_words
