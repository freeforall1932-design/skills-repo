#!/usr/bin/env python3
"""
Score outputs against the per-skill domain rewards — no API calls, no model.

    python -m caveman_skillopt.score_domain                 # mock CI mode:
        scores the reference outputs in examples/domain-predictions-good.json
    python -m caveman_skillopt.score_domain --skill re-triage
    python -m caveman_skillopt.score_domain --predictions preds.json

``preds.json`` maps item id → model output. Results print per skill and are
never averaged across skills. Exit code is 0 only when every scored item
passes its hard gate, mirroring ``caveman_skillopt.score``, so this drops
into CI as a regression check on the shipped domain skills and their reward
functions. The default run is a dry run over hand-written reference outputs:
it proves the datasets and rewards are wired and discriminating (the bad
predictions file must fail), not that any model performs well.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .domain_rewards import evaluate_domain

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "domain"
DEFAULT_PREDS = ROOT / "examples" / "domain-predictions-good.json"


def _skills(requested: str) -> list[str]:
    names = sorted(p.name for p in DATA.iterdir() if (p / "split_manifest.json").exists())
    if requested:
        if requested not in names:
            raise SystemExit(f"unknown skill {requested!r}; known: {', '.join(names)}")
        return [requested]
    return names


def _items(skill: str, split: str) -> list[dict]:
    path = DATA / skill / split / "items.json"
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", default="", help="score one skill only (default: each skill, reported separately)")
    parser.add_argument("--split", default="test", choices=("train", "val", "test", "all"))
    parser.add_argument("--predictions", default=str(DEFAULT_PREDS),
                        help="id → output map (default: the reference outputs, i.e. mock mode)")
    parser.add_argument("--show-violations", action="store_true")
    args = parser.parse_args(argv)

    predictions: dict[str, str] = json.loads(Path(args.predictions).read_text(encoding="utf-8"))
    splits = ("train", "val", "test") if args.split == "all" else (args.split,)
    all_pass = True
    for skill in _skills(args.skill):
        for split in splits:
            results = [evaluate_domain(item, predictions.get(item["id"], ""))
                       for item in _items(skill, split)]
            passed = sum(1 for r in results if r["hard"])
            mean = sum(r["soft"] for r in results) / len(results) if results else 0.0
            print(f"{skill} [{split}]: hard {passed}/{len(results)}, mean soft {mean:.3f} "
                  f"(per-skill only; never averaged across skills)")
            if passed != len(results):
                all_pass = False
            if args.show_violations:
                for r in results:
                    for v in r["violations"]:
                        print(f"  {r['id']}: {v}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
