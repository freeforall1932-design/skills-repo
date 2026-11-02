# Modularization experiment: unified one-skill vs separately routed fragments

**Decision: keep the unified skill. Do not split `one-skill` into
independently routed fragment skills.** The fragments stay published as
install-time alternatives (a human chooses one), not as router rivals.

## Question and adoption rule

If the three existing fragments (`one-skill-prose`, `one-skill-code`,
`one-skill-design`) were offered to hosts *instead of* the unified
`one-skill`, would routing coverage be equal or better within the same
budgets? Adopt the split only on equal-or-better evidence; otherwise keep
and record (brief §6, P2).

## Method

12 representative tasks were hand-labelled with the reference buckets a
correct answer needs (`one-skill/tests/fragment_fixtures.json`, labels
from the published router table). For each task, the smallest covering set
of fragments was computed exactly from the manifest's family definitions,
and always-on cost was measured as the word count of the published
`SKILL.md` files. The arithmetic is pinned in
`one-skill/tests/test_modularization.py`, so the decision re-opens if the
artifacts change shape.

Measured 2026-11-02, after the source refresh:

| Artifact | Always-on words |
| --- | --- |
| unified `one-skill` | 2 394 (budget 2 400) |
| `one-skill-prose` | 2 329 |
| `one-skill-code` | 2 389 |
| `one-skill-design` | 2 155 |

## Results

- **Coverage, top-1 routing:** if a host loads a single skill, fragments
  fully cover **7 of 12** tasks. The 5 misses are ordinary cross-family
  work, not edge cases: landing page with copy (design+prose), PR
  description (code+prose), accessible form component (design+code),
  teaching the Git workflow (prose+code), design-system PR review
  (code+design). Unified covers 12/12 in one load by construction — all
  11 buckets sit behind one router.
- **Cost, perfect multi-load:** even if a host loaded exactly the covering
  fragments, cross-family tasks cost 4 484–4 718 always-on words
  (mean 4 602) vs 2 394 unified — about **1.9×**. Over all 12 tasks the
  fragment policy averages 3 276 words vs 2 394 (+37%).
- **Savings when fragments win:** single-family tasks save only 5–239
  words (2–10%), because every fragment carries the same core rules; the
  unified skill's marginal cost over a fragment is just the wider router
  table. Reference loading is already one-file-at-a-time in the unified
  design, so modularity buys almost no token economy either.

## Limits of this evidence

Task labels are editorial ground truth, and host routers are probabilistic,
not set-cover solvers: a real router might load the wrong single fragment
(making fragments look worse) or several fragments for one-family tasks
(making cost worse). Nothing here measures answer *quality* under either
policy. What the arithmetic does establish is structural: under any routing
accuracy, the fragment policy cannot beat unified on both coverage and
cost, because its best-case savings are ≤10% while its cross-family cost
is ~1.9× and its top-1 coverage is 58%.

## What would change the answer

- Core rules shrink enough that fragments stop duplicating ~2 200 words
  each (e.g. a host-level shared-core mechanism).
- A standard multi-skill composition contract in hosts (explicit
  pairs-with loading), making cross-family coverage reliable.
- Unified SKILL.md breaching its 2 400-word budget under real content
  pressure.

Until one of those holds, the unified deliverable stands, and domain depth
goes into separate *domain* skills (`domain-skills/`) rather than fragment
surgery.
