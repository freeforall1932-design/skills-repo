# Sources

This skill is generated. `one-skill/sources.json` decides what is in it;
`one-skill/build.py` writes this file. Editing `SKILL.md` or `references/`
by hand is a mistake — the next build overwrites it.

| source | upstream | revision | files vendored | license |
|---|---|---|---|---|
| this repository — grug, caveman, and the register rules | `freeforall1932-design/skills-repo` | `93d8fb6496` | 29 | Unlicense (root) / MIT (caveman-universal) |
| anti-slop — the design filter (miqdadbadjuber/anti-slop) | `miqdadbadjuber/anti-slop` | `941b1532f9` | 7 | MIT |
| mattpocock/skills — engineering, productivity, misc | `mattpocock/skills` | `4ae2317ddb` | 57 | MIT |
| Caveman — the token-efficiency voice (upstream v3.2.0) | `JuliusBrussee/caveman` | `2e08b9177c` | 22 | Apache-2.0 |
| The Grug Brained Developer (grugbrain.dev) | `bigskysoftware/grugbrain.dev` | `b1b1ca855c` | 1 | Grug 1-Clause (repo LICENSE at pin) |
| Strix — security testing method (usestrix/strix) | `usestrix/strix` | `6b7ae2ebe4` | 9 | Apache-2.0 |
| mem0 — integration discipline (mem0ai/mem0) | `mem0ai/mem0` | `753496cf14` | 6 | Apache-2.0 |
| Archify — diagram authoring discipline (tt-a1i/archify) | `tt-a1i/archify` | `a4065941f1` | 2 | Apache-2.0 |
| Anthropic engineering plugin 1.2.0 — ten workflow skills | ``Engineering-1.2.0-v1.zip` (committed archive)` | `sha256:07e` | 10 | not stated in the pack (see THIRD_PARTY_NOTICES.md) |
| Anthropic skill-creator — authoring discipline for skills | ``Skill creator copy-v1.zip` (committed archive)` | `sha256:64e` | 1 | Apache-2.0 (LICENSE.txt in the pack) |

## What the merge changed

Upstream text is carried verbatim except for:

1. YAML frontmatter stripped (the merged skill has one frontmatter block).
2. Headings demoted one level, leading H1 dropped (each section is titled by
   `sources.json`).
3. Links to a sibling file rewritten to an in-file anchor, because siblings
   ride in the same reference file.
4. The sections listed in `strip_sections` — only the ones that instruct the
   agent to fetch files or edit an entry file, which a merged skill must not do.
5. Where a skill is mostly a driver for a tool this skill does not ship,
   `keep_sections` carries only the sections that work without it, and
   `markup` removes website markup (never words) from sources that are
   generated pages. Both are listed per section below.

Everything else is the author's wording. Nothing was paraphrased to make the
packaging convenient.

## Per-section notes

| section | carried from | notes |
|---|---|---|
| Caveman output — terse developer chat | `local/caveman-output` | Not carried: Reference material, Language. |
| Micro mode — the 85-token floor | `local/micro-mode` | Not carried: Ralph Wiggum Loop (Optional). |
| Grug reasoning — internal, never shown | `local/grug-reasoning` | Not carried: Reference material, Language. Literal edits recorded in `replace`: `` Pair with `be-brief-output` for documents or `caveman-output` for chat. ``. |
| Ralph Wiggum loop — iterative polish | `local/ralph-wiggum` |  Literal edits recorded in `replace`: `Ralph complements the caveman-be-brief skill:`; `1. **caveman-be-brief** produces tight professional output (pass 1)`; `caveman-be-brief still runs`. |
| Where grug, caveman and be-brief disagree | `local/philosophies` | The argument behind the tables in `SKILL.md`, kept because a rule nobody can argue with gets renegotiated every session. Where a table here disagrees with the precedence file, `SKILL.md` is current: these rows were written while be-brief was still a routed skill, and its half of the split is now this repo's own document rule. Literal edits recorded in `replace`: `` Every rule in `coding-agents/` traces ``; `` MIT (`caveman-universal/`) ``; `` The coding-agent packaging** in `coding-agents/` ``; `` [`skillopt-integration/`](../skillopt-integration/) ``; `` `caveman-universal/references/upstream/official-caveman-skill.md` ``; `` `python coding-agents/compile.py` ``; `` at `caveman-universal/references/upstream/` ``; `` this repo's `caveman-universal/` ``; `` which is why `coding-agents/` looks the way it does ``. |
| Grug engine — the full internal reasoning rule set | `local/grug-engine` | Kept alongside the short `grug-reasoning` section because it holds what that one omits: hard length budgets, the sentence and paragraph rules for the internal trace, the word-swap table, the abbreviation trap and the continuation protocol for a truncated context. Not carried: CRITICAL DISTINCTION: TWO MODES, LANGUAGE, RALPH WIGGUM LOOP (Optional Iteration), STICKY REASONING MODE, EXIT PHRASES (Return to normal reasoning). |
| Summarising a long report or document | `written/document-summary.md` — written for this bundle | Written for this bundle, not carried from upstream: this is the one procedure worth keeping from the retired be-brief skill, re-grounded in grug's complexity budget and caveman's compress-only rule. The register rules it used to argue for are already always-on (rule 1, rule 5, the self-check), so carrying the skill again would say them twice in two voices. |
| Detect AI slop in a draft, and edit it in the writer's voice | `written/prose-detect.md` — written for this bundle | Written for this bundle, not carried from upstream: the prose-only delta of petergyang/no-ai-slop (MIT, inspected at 000650b1, 2026-11-02) that antislop-copywriting does not already state — detect-with-quoted-evidence, the portability test, colon reveals, and delete-don't-improve fake-profound endings. Its other twenty-odd patterns overlap the antislop sections and stay there; its eval.md pass/fail shape is reused as the closing check here and in skillopt-integration's reward notes. |
| Field practices — notes first, a reversible lab, three strikes | `written/field-practices.md` — written for this bundle | Written for this bundle, not carried from upstream: the domain-neutral half of rehan-remade/universal-modder's workflow (MIT, inspected at 9811709d, 2026-11-02) that this bundle did not already say. Its vertical-slice and runtime-verification beats are already carried by tdd, to-tickets and diagnosing-bugs, and its lessons-learned beat by retro, so only the missing three are written out here. |
| Grill me — the alias | `mattpocock-skills/grill-me` | Upstream this is a whole skill: one line that routes to `grilling`. Merged, there is no second skill to call, so the line is kept as the trigger and the work happens in the `grilling` section of this file. |
| Caveman — the voice contract (upstream v3.2.0) | `caveman/caveman-voice` | Upstream original, replaces this repo's v2.x copy. Its 'Anti-slop and the voice' section is the honest bridge to the anti-slop filter; both are carried, and where anti-slop's own rule is stricter, `antislop-human` wins for prose (see the precedence table). |
| Caveman compress — memory and instruction files | `caveman/caveman-compress-upstream` | Different job from this repo's `caveman-review`/`caveman-compress` pair, which compress *documents*. Upstream compresses the instruction files the agent itself loads. Both are carried; pick by artifact. |
| Grug — the full text of the site | `grug/grug-canonical` | The site's markdown source, so it carries page furniture: an empty anchor before each heading and a link to that anchor. The four `markup` transforms remove that scaffolding and nothing else; no word of grug's prose is changed. Read this instead of the compressed summary when the argument matters more than the rule. |
| Technical documentation — README, runbook, onboarding | `engineering-plugin/eng-documentation` | Carried as written: its tool steps are conditional (`If **~~source control** is connected`), and `~~category` means whatever tool the user has for that category. With no connector, produce the text the user would have posted and let them post it. The pack's MCP wiring is not vendored, on the record. |
| Authoring a skill — intent, progressive disclosure, writing style | `skill-creator/skill-authoring` | The craft half of skill-creator, kept while its measurement half is dropped. It says what this repository's build says from the other direction: always-on judgement in `SKILL.md`, depth in reference files that say when to read them, explain why instead of stacking MUSTs, and generalise rather than overfit to the examples in front of you. Not carried: Test Cases, Report structure, Executive summary, Key findings, Recommendations, Commit message format, Writing Style, Running and evaluating test cases, Step 1: Spawn all runs (with-skill AND baseline) in the same turn, Step 2: While runs are in progress, draft assertions, Step 3: As runs complete, capture timing data, Step 4: Grade, aggregate, and launch the viewer, What the user sees in the viewer, Step 5: Read the feedback, Improving the skill, The iteration loop, Advanced: Blind comparison, Description Optimization, Step 1: Generate trigger eval queries, Step 2: Review with user, Step 3: Run the optimization loop, How skill triggering works, Step 4: Apply the result, Package and Present (only if a file-delivery tool is available), Claude.ai-specific instructions, Cowork-Specific Instructions, Reference files. |
