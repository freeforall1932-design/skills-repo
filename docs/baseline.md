# Baseline — recorded before the domain-skills round

Recorded 2026-11-02 on branch `arena/ee0f820f-skills-repo` (the session's
feature branch, cut from `main` at `fd694133`), before any file in this round
was changed. Nothing here is a claim about what the round later produced; the
after-numbers live in `docs/capability-matrix.md` and the pull request.

Environment: Python 3.11.2, git 2.39.5, gh 2.23.0. `pytest` is not installed
system-wide (PEP 668, `externally-managed-environment`), so tests were run in
a throwaway venv at `/tmp/venv` (`python3 -m venv /tmp/venv`,
`/tmp/venv/bin/pip install pytest`, `/tmp/venv/bin/pip install -e skillopt-integration`),
matching the two non-SkillOpt CI jobs in `.github/workflows/tests.yml`. The
third CI job installs `skillopt==0.2.0` from PyPI; it was not reproduced
locally beyond the no-SkillOpt path (follow-up command in the PR).

## Commands actually run, and what they said

| Command | Result |
|---|---|
| `python3 one-skill/build.py check` | pass — `published copies are current (78 skills, 11 references, 0 dead links; fragments prose (25 skills, 33k words), code (56, 43k), design (5, 18k))` |
| `python3 one-skill/build.py build` | `built 78 skills into 11 references (90k words of reference material)`; `SKILL.md: 2394 words always loaded` |
| `pytest one-skill/tests -q` (venv) | **56 passed** in 1.07s (48 test functions; parametrisation collects 56) |
| `pytest skillopt-integration/tests -q` (venv, no SkillOpt) | **23 passed, 2 skipped** (39 test functions in source; the two SkillOpt-dependent modules skip as units without the package, per the integration's lazy-import design) |
| `python -m caveman_skillopt.score --split-dir skillopt-integration/data/caveman_brief_split --split test --predictions skillopt-integration/examples/predictions-good.json --show-violations` | mean soft reward **0.9784**, hard pass **100%** (matches the handoff) |

`git status` was clean before the first edit.

## Counts at the baseline (builder's `split()` word counts)

- Routed skills in `one-skill/sources.json`: **78**, across **10 sources**
  (local 10, anti-slop 6, mattpocock-skills 31, caveman 13, grug 1, strix 4,
  mem0 1, archify 1, engineering-plugin 10, skill-creator 1).
- Cast-aside records: `not_merged` **22** + `not_routed` **11** +
  `not_vendored` **8** = **41 records**, each with a reason. The root README
  said "34 recorded as dropped" next to the same 22/11/8 breakdown — the
  first number is simply wrong.
- `SKILL.md`: **2394 / 2400** words (`ALWAYS_ON_BUDGET`, enforced in `assemble`).
- Reference files (buckets): **11**, plus generated `references/SOURCES.md`:

  | reference | words | | reference | words |
  |---|---:|---|---|---:|
  | code-craft.md | 15,974 | | teach-and-author.md | 7,055 |
  | ship-workflow.md | 15,483 | | write-prose.md | 6,045 |
  | ui-craft.md | 13,204 | | think-first.md | 5,053 |
  | origins.md | 11,118 | | responsive-access.md | 4,808 |
  | setup-repo.md | 4,486 | | terse-chat.md | 4,309 |
  | secure-and-harden.md | 2,954 | | SOURCES.md | 4,515 |

  Bucket references total ≈ **90.5k** words (builder prints `90k`); including
  `SOURCES.md`, 95,004. `code-craft` and `ship-workflow` are already at the
  edge of "read one at a time in one pass" — any growth there gets flagged.
- Fragments: `one-skill-code` SKILL.md 2389, `one-skill-design` 2155,
  `one-skill-prose` 2329 words.
- Root README inconsistencies confirmed present: intro "Sixty-nine skills
  from eight sources", tree comment "24 tests", "Adding a fourth repository",
  "MIT-encumbered" license sentence, "see the pack" for both archives.

## Pins vs upstream HEAD on the inspection date (2026-11-02)

Each repository was cloned shallow and read at the commit in the right
column. "Carried delta" compares only the files this repo vendors.

| Source | Pinned in `sources.json` | HEAD inspected | Carried delta at HEAD |
|---|---|---|---|
| mattpocock/skills | `49dd158d` | `4ae2317d` 2026-10-31 | same 31 skill names; 10 carried files differ (fresh-context subagents, setup/tracker fixes) |
| miqdadbadjuber/anti-slop | `388cbe3b` (VERSION 3.2.20) | `941b1532` 2026-11-01 = tag v3.2.25 | core loses the First-Run Install Wizard; new rules R-39/R-40; `antislop-human` grows Interaction Affordances; `contrast-check.py` unrounded-ratio fix; new sibling `references/` docs (adapted from Addy Osmani — not carried, see matrix) |
| usestrix/strix | `f7a32ae6` | `6b7ae2eb` 2026-10-29 | the 4 carried skills are byte-identical; 2 cast-aside driver skills differ |
| mem0ai/mem0 | `b7ad69af` | `753496cf` 2026-10-30 | the 6 vendored `SKILL.md` files are byte-identical; repo gained many `integrations/*` plugin skills outside `skills/` |
| JuliusBrussee/caveman | `2e08b917` ("finalize Caveman 3.2.0 release metadata", 2026-10-08) | `9b68f7ed` 2026-10-25; releases now at v4.0.1 / bin-v4.0.2 | one carried file differs (`caveman-compress` provider warning); LICENSE at the pin is already Apache-2.0, not MIT as the manifest said |
| bigskysoftware/grugbrain.dev | `b1b1ca85` | `b1b1ca85` (unchanged) | none; repo `LICENSE` is "Grug 1-Clause License: do what want", `package.json` says BSD — neither matches the manifest's "CC BY-SA 4.0 (site)", and the live site carries no license statement either |
| tt-a1i/archify | `58ab0b98` (MIT at pin) | `a4065941` 2026-10-31 | kept sections grew (5 new diagram types); one `replace` needle stale; current source relicensed Apache-2.0 (historical MIT kept for old releases); `.agents/skills/` gained `archify-tuning`, `simplify-codebase`, `test-value` |
| Anthropic archives | `sha256:07e0c827…`, `sha256:64e07a41…` (full digests verified with `sha256sum`) | n/a | skill-creator pack contains `LICENSE.txt` = Apache-2.0; engineering pack contains no LICENSE — its README points at `anthropics/knowledge-work-plugins`, whose repo root is Apache-2.0 |

New sources inspected at: petergyang/no-ai-slop `000650b1` (2026-09-01),
microsoft/SkillOpt `bc0a392e` (2026-10-29), freeforall1932-design/SkillOpt-fork
`e2edfa97` (2026-10-25; behind upstream by exactly 2 commits, 0 ahead),
morluto/rea `8250bf23` (2026-11-02, package version 6.8.0),
bethington/ghidra-mcp `61a1fbc8` (2026-10-31), HexRaysSA/ida-mcp `391c2f06`
(2026-10-28, version 20261028.0.3), icsharpcode/ILSpy `68766c04` (2026-11-01;
releases v11.0 2026-08-12 → v11.2 2026-10-27), SamboyCoding/Cpp2IL `b5ad444b`
(2026-09-12, default branch `development`; last milestone 2022.1.0-pre-release.21,
2026-02-22), rehan-remade/universal-modder `9811709d` (2026-10-29).
What each contains and what was decided per source: `docs/capability-matrix.md`.
Corrections to the brief that ordered this round are recorded there too.
