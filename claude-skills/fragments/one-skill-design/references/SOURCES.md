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
| antislop core — craftsmanship standard, R-rules, liveliness | `anti-slop/antislop-core` | Upstream removed its first-run install wizard in v3.2.25, so the strip that used to name it is gone with it; what remains stripped is the update pointer for standalone installs. In this merged skill every sibling is already inside the same skill, so there is nothing for the agent to fetch and no entry file to edit. Not carried: Already installed, and the user asks how to update. |
| antislop-ui — colour, layout, components, decoration, motion | `anti-slop/antislop-ui` |  Literal edits recorded in `replace`: ``CORE-WEB-VITALS.md`, in the full skill`; ``WEB-BASELINE.md`, in the full skill`. |
| antislop-human — contrast, keyboard, focus, states | `anti-slop/antislop-human` | The contrast checker no longer sits next to a standalone SKILL.md: it is carried at `scripts/contrast-check.py` inside this skill, which is what the command below resolves to. Literal edits recorded in `replace`: `` (`contrast-check.py`, next to this `SKILL.md`) ``; `point the script path at this skill's folder directly`; ``A11Y-PATTERNS.md`, in the full skill`; ``WCAG.md`, in the full skill`. |
| Pick the diagram type, then be honest about the artifact | `archify/archify-method` | Two sections of a 2 500-word skill at the 2026-11-02 pin: the diagram-type router (ten native types now) and the Mermaid mapping. The Output section is no longer kept: upstream rewrote it into renderer receipts plus an offer to enrol a proactive mode in the user's global rules file, and a merged skill produces no receipts and edits no entry file. The remaining renderer sections are dropped by name as before, and the two declared edits below exist because upstream keeps pointing at artifacts this bundle does not ship. Read the type table as a *choice of what to draw*, not as a validation step. The honesty rule from the dropped Output section is kept here verbatim in substance: Do not claim success for a command that did not run, and do not claim visual inspection you did not perform. Not carried: Choose the artifact, Existing candidate handoff, Native diagram authoring, Update awareness, Delivery, Optional viewer capabilities, Setup and fallback, Output. Literal edits recorded in `replace`: `` run `node bin/archify.mjs guide "<scenario>" --json` ``; `` then name them for the reader: use everyday `icon` values and `meta.legend` labels as in **Node icons** (`authoring-contract.md`, in the full skill). ``. |
