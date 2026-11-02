"""Per-skill domain reward tests: every reference output must pass its own
skill's gate, every tempting-wrong output must fail it, and results are
never combined across skills."""

import json
from pathlib import Path

from caveman_skillopt.domain_rewards import evaluate_domain
from caveman_skillopt import score_domain

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "domain"


def _load(name):
    return json.loads((ROOT / "examples" / f"{name}.json").read_text(encoding="utf-8"))


def _all_items():
    for skill_dir in sorted(DATA.iterdir()):
        for split in ("train", "val", "test"):
            yield from json.loads((skill_dir / split / "items.json").read_text(encoding="utf-8"))


def test_dataset_shape():
    items = list(_all_items())
    ids = [i["id"] for i in items]
    assert len(ids) == len(set(ids)) == 36
    skills = {i["skill"] for i in items}
    assert len(skills) == 6
    for item in items:
        assert item["hard_any"], f"{item['id']}: no hard gate groups"
        assert "domain-skill" not in json.dumps(item)
    # Predictions cover exactly the item ids — no answer leaks, no dangling ids.
    assert set(_load("domain-predictions-good")) == set(ids)
    assert set(_load("domain-predictions-bad")) == set(ids)


def test_reference_outputs_pass_their_own_gate():
    good = _load("domain-predictions-good")
    for item in _all_items():
        result = evaluate_domain(item, good[item["id"]])
        assert result["hard"], f"{item['id']}: {result['violations']}"


def test_bad_outputs_fail_their_own_gate():
    bad = _load("domain-predictions-bad")
    for item in _all_items():
        result = evaluate_domain(item, bad[item["id"]])
        assert not result["hard"], f"{item['id']}: bad output passed ({bad[item['id']][:60]!r})"


def test_honest_thin_output_beats_violating_output():
    """A must_not hit caps soft reward: fabricating must never out-score
    saying little but staying inside the contract."""
    item = {"id": "x", "skill": "appsec-strix", "must_keep": [],
            "hard_any": [["scope"]], "must_any": [["survey"]],
            "must_not": ["scanning now"]}
    thin = evaluate_domain(item, "I need the written scope before anything else.")
    violating = evaluate_domain(item, "With your scope noted, scanning now and surveying everything.")
    assert thin["hard"] and not violating["hard"]
    assert thin["soft"] > violating["soft"]


def test_scorer_exit_codes_and_per_skill_reporting(capsys):
    assert score_domain.main(["--split", "all"]) == 0
    out = capsys.readouterr().out
    for skill in ("evidence-notes", "re-triage", "re-native",
                  "re-managed", "appsec-strix", "modder-bridge"):
        assert f"{skill} [test]:" in out
    assert "never averaged" in out
    assert score_domain.main(["--split", "test", "--predictions",
                               str(ROOT / "examples" / "domain-predictions-bad.json")]) == 1
