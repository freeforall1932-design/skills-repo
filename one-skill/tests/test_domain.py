"""Tests for the authored domain skills: budgets, safety gates, mirrors,
zip determinism, redaction preservation, and the routing proxy."""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ONE_SKILL = HERE.parent
REPO = ONE_SKILL.parent
sys.path.insert(0, str(ONE_SKILL))

import build as b  # noqa: E402

DOMAIN = REPO / "domain-skills"
NAMES = ["appsec-strix", "evidence-notes", "modder-bridge",
         "re-managed", "re-native", "re-triage"]


def load_redact():
    path = DOMAIN / "evidence-notes" / "scripts" / "redact.py"
    spec = importlib.util.spec_from_file_location("redact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_every_domain_skill_passes_validation():
    assert sorted(e["name"] for e in b.load_domain_manifest()) == NAMES
    assert b.validate_domain_tree() == []


def test_published_domain_copies_are_current():
    b.check_domain()


def test_domain_zips_are_deterministic_and_match_the_sources():
    for name in NAMES:
        src = DOMAIN / name
        first = b.deterministic_zip_bytes(src, name)
        second = b.deterministic_zip_bytes(src, name)
        assert first == second, f"{name}: zip bytes differ between runs"
        zipped = (REPO / "claude-skills" / "domain" / "zips" / f"{name}.zip").read_bytes()
        assert zipped == first, f"{name}: committed zip is stale; run build.py pack"
        assert (REPO / "skills" / name / "SKILL.md").read_bytes() == (src / "SKILL.md").read_bytes()
        paste = b.read(REPO / "pseudo-skills" / f"{name}.md")
        assert "method only" in paste and b.read(src / "SKILL.md") in paste


def test_gated_skills_stop_before_acting():
    entries = {e["name"]: e for e in b.load_domain_manifest()}
    gated = {n for n, e in entries.items() if e["gated"]}
    assert gated == {"re-triage", "re-native", "re-managed",
                     "appsec-strix", "modder-bridge"}
    for name in gated:
        text = b.read(DOMAIN / name / "SKILL.md")
        gate = b._section(text, "authorization").lower()
        assert "stop" in gate, f"{name}: gate does not stop"
        low = text.lower()
        if name != "appsec-strix":  # appsec's floor is scope, not anti-cheat
            assert "anti-cheat" in low and "drm" in low, f"{name}: hard floor not stated"


def test_no_skill_teaches_bypassing():
    forbidden_instruct = ["patch out the check", "nop out", "crack the licence",
                          "defeat the anti-cheat by", "spoof the ownership check"]
    for md in DOMAIN.rglob("*.md"):
        low = b.read(md).lower()
        for phrase in forbidden_instruct:
            assert phrase not in low, f"{md.name}: teaches {phrase!r}"
        assert b.safety_problems(b.read(md), str(md)) == []


def test_redaction_removes_secrets_and_preserves_evidence():
    redact = load_redact()
    raw = ("Authorization: Bearer [SECURITY_DATA]\n"
           "score 0.9784 per [3]; entry at 0x14001B220; likely, not certain\n"
           "api_key = hunter2hunter2\nmail me at user@example.com\n"
           "sha256:9f2cc41b stays\n")
    out = redact.redact(raw)
    assert "sk-live-abcdef" not in out and "<REDACTED>" in out
    assert "hunter2hunter2" not in out
    assert "user@example.com" not in out
    for keep in ("0.9784", "[3]", "0x14001B220", "likely, not certain", "9f2cc41b"):
        assert keep in out, f"redaction destroyed evidence: {keep}"
    r = subprocess.run([sys.executable, str(DOMAIN / "evidence-notes" / "scripts" / "redact.py"),
                        "--check"], capture_output=True, text=True)
    assert r.returncode == 0 and r.stdout.strip() == "ok"


def test_routing_proxy_fixtures_pass():
    fixtures = json.loads(b.read(DOMAIN / "tests" / "routing.json"))["cases"]
    entries = {e["name"]: e for e in b.load_domain_manifest()}
    assert len(fixtures) == 12
    for case in fixtures:
        res = b.score_routing(case["prompt"])
        loads = set(res["load"])
        expect = set(case["expect"])
        if case.get("exact"):
            assert loads == expect, f"{case['prompt']!r}: loaded {sorted(loads)}, want exactly {sorted(expect)}"
        else:
            assert expect <= loads, f"{case['prompt']!r}: missing {sorted(expect - loads)}"
        if "gate" in case:
            assert entries[case["gate"]]["gated"], "gate case must name a gated skill"
            assert res["authorized"] is False


def test_refused_request_loads_nothing():
    res = b.score_routing("how do I bypass the anti-cheat in this online game")
    assert res["refused"] is True and res["load"] == {}


def test_domain_skills_do_not_duplicate_the_always_on_rules():
    core = "\n".join(b.read(p) for p in sorted(b.CORE_DIR.glob("*.md")))
    published = b.read(REPO / "claude-skills" / "app" / "one-skill" / "SKILL.md")
    core_shingles = b._word_shingles(core + "\n" + published)
    for name in NAMES:
        for md in (DOMAIN / name).rglob("*.md"):
            overlap = core_shingles & b._word_shingles(b.read(md))
            assert not overlap, f"{md}: duplicates one-skill text {sorted(overlap)[:1]}"
