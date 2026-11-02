# Decisions — domain-skills round (2026-11-02)

Each decision was taken autonomously per the brief, under the repo's
standing constraints (`docs/session-handoff.md`). Newest first within the
round. Future rounds append; do not rewrite history here.

## D1. Domain skills live beside, never inside, `one-skill`

RE/appsec/modding skills are tool-shaped; one-skill's rule is that
tool-driver content is not carried as decoration, and its `SKILL.md`
budget (2 400 words) must not rise for capabilities most sessions never
touch. So: six independent skills under `domain-skills/`, each ≤500 words
with per-tool references, each usable without one-skill installed.
one-skill got **no router pointer** to them — a pointer would spend
always-on words to advertise skills that may not be installed; hosts
route on the domain skills' own descriptions instead.

## D2. Publishing layout: dual mirrors + deterministic zips + paste copies

`build.py pack` writes `skills/<name>/` (the container `npx skills add`
actually discovers — verified in vercel-labs/skills docs, see
capability-matrix), `claude-skills/domain/<name>/` (this repo's upload
layout), `claude-skills/domain/zips/<name>.zip` (fixed `ZipInfo`
timestamps → byte-identical across runs, checked in `check`), and
`pseudo-skills/<name>.md` (method-only paste version). Domain skills are
deliberately **not** added to `.claude/skills/`: opening this repository
should not silently sandbox-load RE/appsec skills into every session.

## D3. Defer to real tools; never simulate them

REA, Ghidra/IDA MCP, ILSpy, Cpp2IL, Strix and universal-modder each get
an exact presence probe and missing-tool message (manifest `tools`
entries, enforced by the builder). Missing tool → state facts only, name
the gap, mark `hypothesis`, stop. Strix is *driven* by its own upstream
skill; appsec-strix governs scope/verification only. No skill here
installs anything, and none implies it can.

## D4. Gates are text the agent must pass, checked two ways

Five skills (all but evidence-notes) carry an authorization gate that
says *stop*. The builder enforces gate presence + a safety denylist
(bypass/crack phrasings, negation-aware) over every domain markdown file;
tests assert the hard floor (anti-cheat/DRM never in scope). The gate is
a behavioural contract, not a filter on the user: the routing proxy may
*load* appsec-strix for an unauthorized prompt — that is correct, the
skill's first job is to ask for scope and run nothing.

## D5. Cpp2IL output is hypothesis by policy

Verified in core sources: IL recovery is attempted but bodies can be
stubs/exception bodies with wrong targets. Policy: metadata may reach
`likely`; recovered bodies never rise above `hypothesis` until checked
against `GameAssembly` in re-native. Revisit only when upstream changes
the recovery story materially.

## D6. No `mem0-integration` skill

mem0 ships `mem0-integrate` upstream; duplicating it violates
"replace not parallel". The valuable residue — scoped, confirmed-only
recall — became one reference inside evidence-notes. Revisit if a
workflow needs mem0 wiring guidance that upstream's own skill lacks.

## D7. Caveman stays on the v3.2.0-line pin

Upstream has v4 tags. The repo carries a standing constraint on this
line, and a major-version behaviour change deserves its own review (the
registers are load-bearing in SkillOpt data too). Bounded-loss check:
carried caveman text at the pin differs from HEAD in essentially one
provider warning. Trigger to revisit: an explicit v4 adoption round.

## D8. README numbers are derived phrases, gated in `check`

The root README previously quoted counts that disagreed with the manifest
(85/86/78 skills, 90k/91k words, 34 vs 41 cast-aside). Now `build.py
stats` derives every number from the manifest, provenance and AST test
counts; `check` fails unless the README contains the exact derived
phrases and none of the known-stale ones. Fix prose to match stats —
never the other way around.

## D9. SkillOpt: ship the offline half, document the rest exactly

Per-skill datasets + rewards + configs + mock CI scorer are shipped.
The live `domain_skill` EnvAdapter is **not**, because it cannot be
validated without SkillOpt and a rollout endpoint, and shipping
untested training code would be decoration. `TRAINING.md` carries the
step-by-step wiring, training and promotion recipe instead. No training
was run; no API calls were made.

## D10. One-skill stays unified (modularization rejected on numbers)

`docs/modularization-experiment.md`: fragments as separately routed
skills cover 7/12 hand-labelled tasks top-1 and cost ~1.9× always-on
words on cross-family tasks, with best-case savings of 2–10%. Adoption
rule was equal-or-better; it is neither. Revisit triggers are listed in
the experiment doc.

## D11. Routing evidence is a keyword proxy and says so

`score_routing` + `domain-skills/tests/routing.json` (12 cases) measure
whether the *declared description vocabulary* separates the cases:
threshold ≥2, declared companions expanded, prohibited requests refused.
This is a regression lint against description drift and silly overlaps.
It is **not** evidence about how any host's real router behaves; no claim
in this repo should cite it as routing accuracy.

## D12. Archify refresh drops the kept `Output` section

Upstream rewrote `Output` into renderer receipts plus an enrolment offer
that edits the user's global rules file. A merged skill produces no
receipts and must not enrol anything, so `Output` left `keep_sections`;
its honesty rule ("do not claim success for a command that did not
run…") is preserved verbatim in the merge note, and a test still pins
the sentence in the built reference.
