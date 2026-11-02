# Training the domain skills with SkillOpt — later, on purpose

**Status: nothing here has been trained.** What ships now is the offline
half: per-skill datasets, deterministic rewards, configs, and a mock scorer
that runs in CI without a model or an API key. This file is the exact
recipe for running real training later, plus the reasons the live half is
kept out of CI.

## What exists today

| Piece | Where |
| --- | --- |
| Datasets (36 items, 6 per skill, 3/1/2 splits) | `data/domain/<skill>/`, built by `scripts/build_domain_dataset.py` |
| Reward (stdlib, deterministic) | `caveman_skillopt/domain_rewards.py` |
| Offline scorer / CI dry run | `python -m caveman_skillopt.score_domain` |
| Reference + tempting-wrong outputs | `examples/domain-predictions-{good,bad}.json` |
| Per-skill configs (inert until the adapter exists) | `configs/domain/<skill>.yaml` |
| Tests | `tests/test_domain_rewards.py` |

CI runs the mock mode: reference outputs must pass every hard gate
(currently 36/36) and the bad outputs must fail (0/36). That proves the
reward *discriminates the authored cases*; it says nothing about any
model's behaviour, and no number from it should be quoted as a capability
result.

## Why per-skill, never averaged

Each skill trains and validates alone, against its own dataset and its own
gate. Averaging across skills would let a dangerous failure — appsec
running without scope, triage inventing a disassembly — hide behind easy
points from evidence-notes. `score_domain` therefore prints only per-skill
lines, and a training run takes one `--config configs/domain/<skill>.yaml`
at a time.

## The one missing piece: a `domain_skill` EnvAdapter

SkillOpt envs plug in through `EnvAdapter` + `SplitDataLoader`, exactly as
`caveman_brief` already does in `caveman_skillopt/envs/caveman_brief/`. A
deliberate decision (see `docs/decisions.md`): this adapter is **not**
shipped now, because it cannot be honestly validated without SkillOpt
installed and a rollout endpoint available, and this repository does not
ship plausible-but-untested training code. To add it later:

1. `pip install skillopt` and `pip install -e skillopt-integration`.
2. Create `caveman_skillopt/envs/domain_skill/` mirroring `caveman_brief`:
   - `dataloader.py` — reuse `CavemanBriefDataLoader` unchanged if possible
     (split-dir layout is identical: `train|val|test/items.json`).
   - `rollout.py` — system prompt = candidate skill text; user prompt =
     item `instruction` (+ `context` if present). Persist each episode at
     `<out_root>/predictions/<id>/conversation.json` (the shared
     `EnvAdapter.reflect()` reads exactly there), and score with
     `caveman_skillopt.domain_rewards.evaluate_domain`, mapping `hard`
     to the gate pass and `soft` to the shaped reward.
   - `adapter.py` — subclass `EnvAdapter` like `CavemanBriefAdapter`;
     read a `skill_filter` config key and keep only items whose `skill`
     equals it (the config already passes it); serve reflection prompts
     from the env's own `prompts/` via the `get_*_prompt()` overrides.
3. Register it: in `caveman_skillopt/register.py`, add `"domain_skill"` →
   the new adapter class beside `ENV_KEY`, and add the package to
   `pyproject.toml` `[tool.setuptools] packages`.
4. Smoke-test offline: `python -m caveman_skillopt.score_domain --split all`
   must still pass, and one `eval_only` pass over the test split with the
   shipped skill must reproduce the reference hard-pass pattern before any
   training epoch is trusted.

## Running training (one skill at a time)

```bash
# from the repository root, with an API key for the configured backend
python -m caveman_skillopt.train --config skillopt-integration/configs/domain/re-triage.yaml
```

Costs are real: rollouts + reflection against the configured models. The
configs start small (3 epochs, batch 3, learning rate 2 edits) because the
datasets are tiny; growing the dataset beats raising epochs.

## Promoting a trained skill back

SkillOpt writes `runs/domain/<skill>/.../best_skill.md`. Do **not** copy it
over any published mirror. The path back is the same as every other edit:

1. Review the diff against `domain-skills/<skill>/SKILL.md` by hand —
   authorization gate, scope stops and no-fabrication lines are floor, not
   style; a trained edit that weakens them is rejected whatever the reward
   says (the reward is substring-level and cannot see semantics).
2. Apply accepted edits to `domain-skills/<skill>/SKILL.md` only.
3. `python3 one-skill/build.py pack && python3 one-skill/build.py check` —
   the 500-word budget, frontmatter lint and safety denylist all re-run.
4. `python -m caveman_skillopt.score_domain --skill <skill> --split test`
   with fresh predictions; record before/after per-skill numbers in the PR.

## Fork note

This repo points at `freeforall1932-design/SkillOpt-fork` for source
checkouts (`SKILLOPT_SRC`). As of 2026-11-02 the fork is 0 commits ahead
and 2 behind `microsoft/SkillOpt` (it lacks `9f1969b1f4` and `bc0a392ef0`),
so a plain fast-forward upstream sync is the only fork change needed;
nothing in this integration depends on fork-only code. The fork itself is
another repository and is not edited from here.
