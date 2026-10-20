# Improvement log

Chronicles substantive changes and the reasoning behind them. Entries are
dated; newest first.

## 2026-10-11 — a review pass: what the last round got wrong, plus two packs

**Change:** the merge was read back end to end instead of grown, two archives the owner
committed were integrated (`Engineering-1.2.0-v1.zip` → 10 skills, `Skill creator
copy-v1.zip` → the authoring half), and be-brief was retired into `legacy/` with one
carve-out rewritten for this bundle. Ten sources now route **78 skills into 11 reference
files (90k words)** behind a **2394-word** `SKILL.md`; **56 tests**.

**What the review found, because a review that finds nothing is a rubber stamp.**

* **Two pins in `sources.json` were not real revisions.** The last round recorded
  `2e08b91e0a7d…` and `388cbe3b6c32…` — seven characters I had extended into forty by
  hand. GitHub answers `422` for both. Nothing noticed, because a pin that is never
  fetched cannot fail: `sync` ran `git fetch <ref>` with `check=False` and, when it
  failed, left the clone on the default branch. `strix` and `archify` had already drifted
  that way (manifest said `62b4964`, tree held `f7a32ae6`). Now: a failed fetch dies, a
  checked-out SHA is compared with the pin, and a short SHA is rejected offline in
  `validate_pins`, so CI sees it without the network.
* **A manifest excused a file that does not exist** — a retired be-brief record cited
  `references/audit.md`, which the legacy tree never had. An excuse reads as a decision,
  so a nonexistent path is worse than no path: `validate_records` now refuses any cast-aside
  record whose `path` is not vendored.
* **A ruling in the hand-written layer shipped as a broken sentence**: "Both are right
  about their reader: a produce goes to one place". Nobody could parse it, including me,
  for a full round. Rewritten, and the four precedence rows plus the `write-prose` layer
  label that still named the retired skill now name *the document register*.
* **Retiring be-brief was only safe because of what else went with it.** The old `unified`
  variant — the previous single-file edition of this same bundle — carried a second,
  older copy of the layers and command tables and told the reader to pair with
  `be-brief-output`. Two stale copies of a routing table in one skill is how a merge starts
  lying, so `unified/SKILL.md`, its examples, and its two reference files (each verified
  byte-identical to a routed copy) went to `legacy/` too. What was still carrying weight —
  summarising a long document — was rewritten as `one-skill/written/document-summary.md`,
  grug's complexity budget and caveman's compress-only rule in a professional register,
  and marked `authored: true` so `SOURCES.md` labels it as this bundle's own text instead of
  inventing an upstream for it.
* **The two packs stayed honest by being small.** None of the ten engineering skills is
  `disable-model-invocation` upstream, so none of them is offered as a named command here —
  my first pass marked all ten as commands, which cost 194 words of always-loaded budget and
  invented an interface upstream never had. Their `~~source control` steps are already
  conditional, so the text needed no edits, and the one line that pointed at the plugin's
  `CONNECTORS.md` was replaced with the convention spelled out inline.
* **Provenance quoting must survive markdown.** `SOURCES.md` prints the exact upstream line
  a `replace` deleted; a line containing a pipe reflowed the table row, and a line containing
  backticks needed a `` … `` span, which the fragment-link test then mistook for a dangling
  link. Both sides now share one `mask_code_spans`.

**Two more things the review turned up.** `pytest` from the repository root aborted at
collection because `legacy/coding-agents/tests/test_compile.py` imported PyYAML at module
level while its own two frontmatter checks had already declared it a soft dependency — half a
fix, and the worse half: a frozen tree that cannot be collected hides every other result. It
skips now (102 passed, 10 skipped from the root). And the budget number needed explaining: the
builder's `split()` count is 38 words higher than `wc -w` on the same bytes, because
`str.split()` also breaks on no-break spaces. It is the stricter of the two, which is the right
direction for a limit to be wrong in, and `README.md` now says which measure it quotes.

**Two more, found by reading the round's own output rather than the code.** A `not_routed`
record excused `unified/references/cut-lists.md` twice — once with the be-brief retirement,
once with the `unified` retirement — so `SOURCES.md` printed one decision twice in two
different words and the README counted a dropped file that was dropped once; each record was
valid on its own, which is why no existing gate saw it. And
`test_a_fragment_holds_exactly_its_own_buckets` read `one-skill/dist/families/`, gitignored
scratch that CI never has, so it `pytest.skip`ped and the suite reported green while checking
nothing about the fragments — for two rounds. The fixture builds the bundle now, and the
missing-tree case is an assertion. A check that quietly stops checking is the one defect class
this repository is specifically built to catch, so both are gates now: duplicate cast-aside
records die, and no test in `one-skill/tests` skips.

**Also:** `BUILD.json` records the checksum of every entry, sibling doc and `core/` file, and
`check` reads it back *before* rebuilding — the work list's item 4, which the mirror diff only
half-covered: a hand-edit inside `upstream/` landed on both sides of that comparison, so it
reported "stale, run `install`" and invited baking the edit in. The message now names the
drifted input and offers `sync` as the other option.

## 2026-10-10 (later) — five more sources, an implementability filter, and fragments

**Change:** the merge gained `usestrix/strix` (4 of 9 skills), `mem0ai/mem0` (1 of 6),
`tt-a1i/archify` (1 of 2), `JuliusBrussee/caveman` **v3.2.0** (13 skills, replacing this
repo's v2.x-era copy) and `bigskysoftware/grugbrain.dev` (grug's site text in full).
69 skills now land in 11 reference files (87k words) behind the same 2.4k-word
`SKILL.md`. `anti-slop` was re-pointed at its origin
[`miqdadbadjuber/anti-slop`](https://github.com/miqdadbadjuber/anti-slop) after
verifying the fork was byte-identical. Three **fragments** —
`one-skill-prose`, `-code`, `-design` — are generated from the same manifest into
`claude-skills/fragments/`, each with its own ZIP, as the documented fallback for a
host that cannot carry the full bundle.

**The filter:** "take only what works, cast aside what is not implementable." Strix's
skills are a Docker-launched scanner, mem0's are an SDK plus an API key plus
fetch-the-docs-at-runtime, and Archify's renderer is 6 MB of Node pipeline. None of it
can be obeyed from a markdown file, so 21 upstream skills are **not** carried — and
each one is listed with its reason in the manifest *and* in the shipped
`references/SOURCES.md`, next to the coverage table and the honesty rules that did
survive. Three new builder knobs serve the same idea: `keep_sections` (carry the two
sections of a tool driver that work without the tool, drop the rest by name), `markup`
(remove a generated page's furniture — grug's site wraps headings in anchors — without
touching a word), and `not_merged`/`not_vendored` records.

**The gate:** `build.py` now fails if a vendored `SKILL.md` is neither routed nor
listed under its source's `not_merged`, if a cast-aside record has no reason, or if a
declared `replace` no longer matches anything upstream. Silence was the failure mode:
an unaccounted skill looks exactly like a merged one. `sync` also records, per source,
every skill the *upstream tree* contains (`discover` → `discovered_upstream` in
`PROVENANCE.json`), so a source that vendors one flat file per skill — anti-slop, and
this repo's own `legacy/` — cannot pass the gate by having been copied narrowly.

**What it cost:** `SKILL.md` sat at 2398 of its 2400 words before this round — the
builder's own counter, which is 38 higher than `wc -w` on the same bytes because
`str.split()` also breaks on no-break spaces, and being stricter is the right way for
a budget to be wrong. Two
new router rows and 19 new command/trigger lines were paid for by moving the
nine-row provenance table out of the always-on file into `SOURCES.md` (licenses now
sit in each reference file's head, where the text they cover is actually read),
shortening the open paragraph, and deleting the `diagrams` bucket that had been
created for Archify in the same session — 410 words of reference material do not pay
for a router row, and the anti-slop filter already asks a diagram the question it asks
a page. The budget check also moved out of the reporting step into `assemble`, so no
command can now write an over-budget `SKILL.md` at all.

**Fixed on the way, both real:** `sync` deleted a vendored tree when a source path
moved (it copied 0 files and did not care; now a missing include is a hard stop and
`local` reads the working tree instead of cloning the default branch, where `legacy/`
does not exist), and the link audit treated a markdown link inside a code span as a
live link — which made `SOURCES.md`'s own record of a replaced sentence look like a
dead link. Tests went 25 → 48, including six that mutate the manifest to prove the new gates
bite.

## 2026-10-10 — one skill: three repositories merged behind a manifest

**Change:** every skill in this repo, plus
[freeforall1932-design/anti-slop-fork](https://github.com/freeforall1932-design/anti-slop-fork)
(6 skills) and
[mattpocock/skills](https://github.com/mattpocock/skills) (31 skills: engineering,
productivity, misc), is merged into a single generated skill — published as
`.claude/skills/one-skill/`, `claude-skills/app/one-skill/` and the upload ZIP, built
by `one-skill/build.py` from a `one-skill/sources.json` manifest. 50 upstream skills
landed in 10 reference files (75k words) behind a 2.4k-word `SKILL.md`. The previous
skill sets moved to `legacy/`, and `.claude/skills/`, `claude-skills/app/`,
`claude-skills/app/zips/` and `pseudo-skills/` now carry only `one-skill`. CI's
pack-building job was replaced by a merge job (`pytest one-skill/tests` +
`build.py check` + an offline-reproducibility gate).

**Why generated rather than hand-merged:** the ask is to keep adding sources. A
hand-written merge means the fourth repository is another 300 files to reconcile by
eye; a manifest makes it one entry and a rebuild. Router table, command table,
per-bucket indexes, provenance and counts all regenerate.

**Why verbatim rather than rewritten:** four of these sources contradict each other
on the same sentence (caveman: *fragments OK*; be-brief: *never broken grammar*;
antislop: *liveliness is added*; Pocock: *ask before you build*). Paraphrasing them
into agreement is how a merge destroys the thing each author was protecting, and
this repo already had the right precedent — the four variants quoted upstream rather
than summarising it. So bodies are carried as written, and the reconciliation lives
in `core/10-precedence.md` as *rulings by destination*, with the argument one hop
away in `references/origins.md` (which carries the old `philosophy/conflicts.md`
verbatim).

**Two escape hatches, both fail-closed.** `strip_sections` drops an upstream
section that only makes sense for a standalone install — antislop's first-run wizard
literally tells the agent to fetch files and edit an entry file, which a merged skill
must never do. `replace` makes a literal wording edit where verbatim carriage would
otherwise make the skill lie about its own layout ("the script sits next to this
`SKILL.md`"). Both are recorded per section in `references/SOURCES.md`, and both
**fail the build** when their target string no longer exists upstream: a strip that
silently stopped matching is a rule shipping on a file that moved. The first run
caught a stale strip I had over-declared, and the second caught a needle I had
guessed instead of read — which is the argument for the guard existing.

**Why an always-loaded budget.** `SKILL.md` rides in every request, so bloat there is
taxed on every turn. `ALWAYS_ON_BUDGET = 2400` words, enforced by the build. It
forced real cuts (the eight named rulings lost their prose but not their verdicts,
and one duplicated rule in `always-on` was deleted rather than restated). Getting
from the first draft's 2912 words to 2373 was mostly removing duplication between
the merge layer and the buckets.

**Why buckets are destinations, not origins.** Two skills from different repos that
govern the same output sit adjacent in one reference file. That is where a
contradiction is visible to a reader; sorting by repo hides it in two places at once.

**What is deliberately not merged:** `mattpocock/skills/in-progress/` (betas, no docs
pages, "can change or disappear without warning") and `skills/deprecated/` (empty by
upstream policy). Recorded in the manifest, not silently dropped.

**Kept honest about size:** a 50-skill package is heavy, and a merged skill that
loads all 75k words would cost more context than the writing saves. Hence the split:
one always-loaded file, ten on-demand references, and a paste path for models with no
uploader that ships the router alone. Also hence the decision *not* to build a
monolith export, and to say so in `pseudo-skills/one-skill.md`.

**One mistake worth recording.** The new CI job failed while every local test passed.
The repository's `.gitignore` has a global `dist/`, so `one-skill/dist/` was never
committed, and the tests comparing install mirrors against it iterated a directory
that did not exist in CI — an empty loop, a green suite, a bundle nobody had verified.
`check` and the mirror test now rebuild from the manifest and compare against the
*published* copies, and a test pins the convention so the two cannot drift apart
again. `dist/` stays out of git: the skill would otherwise be four copies of 1.3 MB.

**Follow-ups, in order of value:**
1. Train the merged bundle with SkillOpt as one document (today the trainer still
   targets the four register documents in `legacy/`). The wiring is one manifest
   `entry` pointing at a `best_skill.md`; the reward function already scores per
   register, so decide whether that gate survives the merge.
2. `build.py sync` could record upstream file hashes in `BUILD.json` *and* verify
   them, so a re-vendored file that changed underneath a hand-edit is caught.
3. `scripts/` is shared across buckets: if a future source ships a script with a
   colliding basename, the build silently keeps the first. Namespace or fail.
4. The ZIP is 194 KiB. If the app surface has an upload ceiling, the fix is trimming
   `references/`, not the router.

## 2026-09-17 — CI: pin SkillOpt, make the integration job blocking

**Change:** `skillopt-integration` CI job went from
`continue-on-error: true` + `pip install skillopt` to
`continue-on-error: ${{ github.event_name == 'schedule' }}` +
`pip install skillopt==0.2.0`, with a weekly `schedule` trigger that installs
latest instead.

**Why:** the previous configuration was the worst of both worlds — un-pinned, so
not reproducible, *and* non-blocking, so not a gate. An un-pinned blocking job
would be worse (upstream publishes, this repo's CI turns red on unrelated PRs).
Pinning is what makes blocking safe: with the version fixed, the job is
deterministic, so a failure means *this* repo broke it.

**Why not just drop the job:** it covers the tests that
`pytest.importorskip("skillopt")` skips in the no-SkillOpt job — the dataloader
and adapter paths. That is the part of the integration layer most likely to
drift against upstream.

**Why the weekly un-pinned run:** pinning alone means silently testing against
an old version forever. The scheduled run installs latest and is allowed to
fail, so upstream breaking changes surface on their own schedule and get a
deliberate pin bump rather than an emergency.

**Verified:** clean-room venv on Python 3.11, `skillopt==0.2.0` from PyPI,
39 passed. 0.2.0 is simultaneously the latest on PyPI and the version the whole
integration was developed against, so pinning introduced zero drift.

## 2026-09-17 — variants became real skills, not instruction documents

**Change:** `variants/*.md` (four flat files) → `variants/<name>/SKILL.md` +
`references/` + `examples.md`.

**Why:** an outside review judged the flat files "more like just text
instruction than an actual skill," and that was correct. Against the Agent
Skills spec they were missing:

| Requirement | Before | After |
|---|---|---|
| Progressive disclosure | one flat file, everything always loaded | `SKILL.md` + `references/`, one level deep |
| Optional frontmatter fields | none | `metadata`; `disallowed-tools` on grug |
| Description discipline | approximate | third person, states *what* and *when*, triggers front-loaded, ≤1024 chars |
| Workflow with feedback loop | absent | numbered flow + self-check checklist |
| Worked examples | absent from the skills | `examples.md` per variant |
| Evals | existed, never linked | `metadata.evaluation` points at `skillopt-integration/` |

**The two that mattered most.** Feedback loops turn rules the model follows into
rules it audits itself against — each variant now ends in a self-check ("every
number survived? every hedge survived? code byte-identical?") with instructions
to fix silently rather than announce. Progressive disclosure means the agent
sees SKILL.md and pulls `references/cut-lists.md` only when it is actually
cutting.

**Consequence for packaging:** the paste route now *flattens* the same content
into one self-contained file, because a pasted file has no filesystem beside it
and relative links to `references/` would be dead on arrival. Cursor `.mdc` does
the same, being a single-file format. A test asserts no `](../../` links survive
into packs, where they would resolve to nothing.

**Deliberate omissions:** no `scripts/` or `assets/` — there is nothing
genuinely executable here, and adding one to tick a spec box would be
cargo-culting. `disallowed-tools` appears only on `grug-reasoning`, a reasoning
layer that should not be writing files; the output variants need unrestricted
access.

## 2026-09-17 — Qwen split into two profiles

**Change:** added `profiles/qwen-agent.json` (Qwen Chat agent) alongside
`profiles/qwen.json` (Qwen Code CLI). Added `web-workspace` as a wire protocol
and `upload` as an instruction method; `compile.py` now requires
`instruction.paste_dir` for such agents instead of config paths.

**Why:** these are different products. Qwen Code is a terminal CLI with a config
directory. The Qwen Chat agent is a hosted agent with an uploadable workspace,
no CLI, and no config directory. One profile could not describe both honestly.

**Correction made:** the Qwen Code profile pinned `0.22.3`, inherited from the
official caveman profile registry. Checked on 2026-09-17 and corrected to
`0.24.0`: npm `@qwen-code/qwen-code` `dist-tags.latest` = 0.24.0 published
2026-09-16, GitHub release v0.24.0 published 2026-09-16, repo last pushed
2026-09-17, ~27.9k stars, not archived. Note the npm package is
`@qwen-code/qwen-code` — a package named `qwen-coder` does not exist, which is
a plausible source of an "it was abandoned" impression.

**Honesty constraint preserved:** the Chat agent's `SKILL.md` handling is
genuinely unknown, so the profile sets `skills: null` rather than guessing, and
its pack ships plain `.md` with no frontmatter. That is why the pseudo-skill
fallback must stay.

## 2026-09-17 — CI added, zip made reproducible

**Change:** `.github/workflows/tests.yml` with three jobs. Made `compile.py`
write `ZipInfo` with a fixed timestamp.

**Why:** the stale-packs gate (`compile`, then `git diff --exit-code`) is only
meaningful if compilation is deterministic. The first attempt embedded file
mtimes, so every run produced a different zip and the gate failed on noise.
Verified reproducible by hashing two independent runs.

The SkillOpt job installs only `skillopt-integration` (not `skillopt`) and still
exercises the reward function, because the scorer was made dependency-free —
see below.

## 2026-09-17 — offline scorer made dependency-free

**Change:** extracted `normalise_item` into
`caveman_skillopt/envs/caveman_brief/schema.py`; made the package and env
`__init__.py` resolve SkillOpt-dependent modules lazily via `__getattr__`.

**Why:** the reward function is useful as a plain linter, without the training
framework. Took three attempts — the package `__init__`, then the env
`__init__`, then `score.py` itself each imported SkillOpt transitively. Result:
23 passed / 2 skipped with SkillOpt absent, 39 passed with it installed.

## Earlier in the session — evaluator correctness fixes

Each of these was a real bug found by testing, not a stylistic change.

- `contains_number` flagged `1240` as lost when the output wrote `1,240` — strip
  thousands separators on both sides.
- `contains_span` called "delays"→"delayed" a lost fact — added a conservative
  stem fallback (min 4-char stem), erring toward recall.
- Caveman fragments scored register fidelity 1.0 under `be_brief` — added
  `_BARE_VERB_RE` to catch bare-verb fragments like "check use".
- The identity copy passed the hard gate (a degenerate optimum) — added
  `no_compression_or_grew` as a blocking violation.
- Code-assist items could never reach 0.5 compression, since byte-exact code is
  uncompressible — target clamped via `_adjust_target_for_code` to
  `min(target, 0.30)`.
- `INVENTED_ABBREV_RE` false-positived on "auth", "res", "diff", "doc" —
  narrowed to the official set `cfg|impl|req|res|fn`.
- Cursor `.mdc` generation emitted an unquoted YAML scalar containing `": "`,
  which made the entire frontmatter unparseable so Cursor silently ignored the
  rule — fixed with `_yaml_scalar()` (double-quote + escape).
