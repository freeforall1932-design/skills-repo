# Capability matrix — external sources inspected for the domain-skills round

Inspected 2026-11-02 (cloned, not just README-read). "Verdict" uses the
brief's four words: **integrate** (into one-skill), **separate** (beside
one-skill as its own skill/tool relationship), **defer** (later, with a
trigger), **reject** (deliberately not carried). Exact vendoring stays in
`one-skill/sources.json`; licences stay in `THIRD_PARTY_NOTICES.md`.

## The twelve brief sources

### 1. mattpocock/skills — `4ae2317d` — MIT — **integrate (refreshed)**

Already vendored. Needed: nothing new; HEAD changed ~10 carried files
(code-review, codebase-design, implement-spec, wayfinder, grilling,
setup trackers) with the same 31-skill set in scope (engineering +
productivity + misc; `in-progress` stays out per standing constraint).
Improved: pin bumped `49dd158d → 4ae2317d`, no manifest surgery needed.

### 2. miqdadbadjuber/anti-slop — `941b1532` (v3.2.25) — MIT — **integrate (refreshed)**

Needed: the design filter is one-skill's interface core; upstream had
moved 5 patch versions. Lacked: rules R-39/R-40, the Interaction
Affordances section, unrounded contrast ratios in the checker. Changes
resolved in the manifest: upstream deleted the First-Run Install Wizard
(its strip retired), four adapted web-quality reference docs excused in
`not_vendored` with their links de-linked by declared replaces,
`contrast-mcp.py` and `VERSION` not carried. Brief's "v3.2.7" note is
correct as a floor; current is v3.2.25.

### 3. petergyang/no-ai-slop — `000650b1` — MIT — **integrate (delta only), rest reject**

~26 prose patterns; most already stated by vendored antislop-copywriting.
The non-overlapping delta (detect mode with quoted evidence and no
authorship claim, portability test, colon reveals, delete-don't-improve
fake-profound endings, minimum-effective-edit) was **re-authored** as
`one-skill/written/prose-detect.md` (write-prose). The skill itself is not
vendored; its `eval.md` pass/fail shape informed the closing check.

### 4. microsoft/SkillOpt `bc0a392e` + SkillOpt-fork `e2edfa97` — MIT — **separate (offline extension), training defer**

Read-only fork respected: the fork is 0 ahead / 2 behind upstream
(missing `9f1969b1f4`, `bc0a392ef0`); only fix it needs is a fast-forward,
documented in `skillopt-integration/TRAINING.md`. Lacked: any way to train
or score the *domain* skills. Added: per-skill datasets (36 items),
deterministic per-skill rewards, inert configs, mock scorer in CI. The
live `domain_skill` adapter and any training are deferred with exact
steps (cannot be honestly validated without SkillOpt + an endpoint; no
paid calls allowed).

### 5. morluto/rea (`rea-agents` 6.8.0) — `8250bf23` — MIT — **separate (front door), vendoring reject**

Needed: a real front door for 15 platform domains (incl. JS bundles, APK,
firmware) that this repo should never try to reimplement as markdown.
re-triage defers to REA whenever `npx -y rea-agents@latest doctor` shows
it configured, and evidence-notes files its Evidence output unchanged.
Deliberately **not carried**: REA's own skill text, orchestration, router
taxonomies, domain agents, optional cloud enrichments (listed in
`domain-skills/re-triage/references/tool-matrix.md`). Verified limits
encoded: setup installs neither Node nor Ghidra/IDA; `doctor` only proves
setup-owned registrations; its own disclaimer bars DRM/anti-cheat
circumvention, matching this repo's gates.

### 6. bethington/ghidra-mcp — `61a1fbc8` — Apache-2.0 — **separate (driven by re-native)**

219-tool MCP bridge (`bridge-mcp-ghidra`), Ghidra 12.x + Java 21, setup
`python -m tools.setup preflight`. Carried as check/install facts and
driving guidance in `re-native/references/ghidra-mcp.md` — the no-IDA-
licence route.

### 7. HexRaysSA/ida-mcp — `391c2f06` — MIT — **separate (driven by re-native)**

Official Hex-Rays MCP; IDA Pro 9.4+ via IDALIB, Python 3.11+, install
`uvx ida-hcli mcp install`. Carried likewise in `re-native/references/ida-mcp.md`.
Rule encoded: no licence → route to Ghidra, never suggest cracked copies.

### 8. icsharpcode/ILSpy — `68766c04` — MIT — **separate (driven by re-managed)**

`ilspycmd` flags verified in `ICSharpCode.ILSpyCmd` source (`-l`,
`--list-resources`, `-t`/`-m`, `-il`). Carried as the .NET route with the
"verify claims in IL" rule.

### 9. SamboyCoding/Cpp2IL — `b5ad444b` — MIT — **separate (driven by re-managed)**

Brief's open question — *are recovered bodies still stubs?* — answered
from core output formats (`dll_il_recovery`, `dll_throw_null`,
`diffable-cs`): ISIL-based IL recovery is attempted, but bodies may be
stubs/exception bodies and recovered IL is rough. Encoded rule: metadata
= likely after spot-check, every recovered body = hypothesis until
verified in `GameAssembly` via re-native.

### 10. usestrix/strix — `6b7ae2eb` (vendored source) — Apache-2.0 — **separate (governed by appsec-strix)**

Vendored method skills were byte-identical at the new pin. Lacked: a
gate + verification layer between "scan my app" and an autonomous scanner.
Added `appsec-strix`: written scope precondition (no scope = nothing
runs), offline survey first, budget-bounded quick pass, hand-triaged
findings, honest coverage statement. Tool *driving* defers to Strix's own
`penetration-testing-with-strix` skill (installs via `npx skills add
usestrix/strix`); copied flag tables would go stale — rejected on purpose.
Editions verified: OSS needs Docker + own LLM key; cloud needs neither.

### 11. mem0ai/mem0 — `753496cf` (vendored source) — Apache-2.0 — **separate (optional recall only), P3 skill reject**

mem0 already ships its own `mem0-integrate` skill upstream; a
`mem0-integration` skill here would duplicate it. Instead evidence-notes
carries the narrow contract worth having: store **confirmed**, distilled
facts only, always with explicit `user_id`/`agent_id`/`session_id`,
search before storing, recall = hint until re-checked against the ledger.
That is the P3 assessed and answered: no separate skill.

### 12. rehan-remade/universal-modder — `9811709d` — MIT — **separate (modder-bridge) + integrate (practices delta)**

Needed: an owned-game modding route that respects the hard floor
(no anti-cheat/DRM/ownership bypass — its own rules agree). Added
`modder-bridge`, which defers to `um` (`um --version`, `um kb search`,
its `mod-any-game` workflow) when present and otherwise runs a minimal
backup-first lab workflow. Its domain-neutral practices that one-skill
lacked (search notes first, reversible lab, three-strikes rule) were
re-authored into `one-skill/written/field-practices.md`; beats already
carried (vertical slice ≈ tdd/to-tickets, lessons ≈ retro) were **not**
duplicated. Its own skills are not vendored.

## Vendored sources refreshed alongside (existing pins)

| Source | Pin move | Carried-text effect |
| --- | --- | --- |
| mattpocock/skills | `49dd158d → 4ae2317d` | 10 carried files updated |
| anti-slop | `388cbe3b → 941b1532` | R-39/R-40, Interaction Affordances, contrast fix |
| usestrix/strix | `… → 6b7ae2eb` | carried skills byte-identical (pin/provenance only) |
| mem0ai/mem0 | `… → 753496cf` | carried skills byte-identical (pin/provenance only) |
| tt-a1i/archify | `58ab0b98 → a4065941` | 10-type router; rewritten Output section no longer kept; 3 new internal skills excused by name; licence MIT → Apache-2.0 at the pin |
| caveman, grug, both root archives, local | unchanged | synced at existing pins; licence *labels* corrected (caveman Apache-2.0, grug "Grug 1-Clause", skill-creator Apache-2.0). Caveman v4 exists upstream — **deferred**: the repo has a standing v3.2.0-line constraint and v4 is a behaviour-changing major that deserves its own review round |

Built effect of the round: routed skills 78 → 80, references ≈90.5k →
≈93.6k words, always-on `SKILL.md` unchanged at 2 394/2 400 words,
cast-aside records 41 → 45 (3 new archify internals, 1 antislop
vendoring record). Baseline in `docs/baseline.md`.

## Corrections to the brief's pre-verified facts (Oct 28–30 snapshot)

- anti-slop is at **v3.2.25**, not v3.2.7 — and the install wizard the
  manifest used to strip no longer exists upstream.
- Archify is **Apache-2.0** at current HEAD, not MIT (MIT retained for
  historical releases); its diagram router now lists **ten** native types.
- Caveman's licence at the carried pin is **Apache-2.0**, not MIT.
- Cpp2IL no longer fits a flat "stubs only" description — recovery is
  attempted but bodies still require native verification (item 9).
- SkillOpt-fork needs nothing authored; it needs a **fast-forward**
  (0 ahead / 2 behind).

## Discovery fact used for the publish layout

`vercel-labs/skills` documents `npx skills add` discovering `SKILL.md`
under repo root, `skills/`, `.claude/skills/`, `.agents/skills/` and other
agent containers, walked up to three levels (`docs/creating-skills.md`,
`92a9a34a`). Hence domain skills publish to `skills/<name>/` *and*
`claude-skills/domain/<name>/`; `--full-depth` is explicitly warned
against in the README because it would surface vendored upstream
`SKILL.md` files from `one-skill/upstream/`.
