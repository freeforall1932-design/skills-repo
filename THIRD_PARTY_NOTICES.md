# Third-party notices

This repository's own work is under the Unlicense (root `LICENSE`).
Vendored upstream text keeps its upstream licence; the Unlicense does not
relicence anything listed here. This file records **what each upstream
states** and how it was checked on 2026-11-02. It is an inventory for
readers, not legal advice, and draws no legal conclusions — items needing
an owner's judgement are flagged as such at the end.

The machine-readable source of truth stays `one-skill/sources.json` (with
`one-skill/upstream/PROVENANCE.json` generated from it); this file explains
the licence review behind those labels.

## A. Vendored into `one-skill` (carried verbatim under the manifest rules)

| Source slug | Project (origin) | Licence as stated at the pin | How checked |
| --- | --- | --- | --- |
| `mattpocock-skills` | mattpocock/skills `4ae2317d` | MIT | `LICENSE` (MIT, Copyright Matt Pocock) at the inspected commit |
| `anti-slop` | miqdadbadjuber/anti-slop `941b1532` (v3.2.25) | MIT | `LICENSE` at the inspected commit. Four newer reference docs inside two skills are stated upstream as adapted from addyosmani/web-quality-skills (MIT, under `LICENSE-web-quality-skills`); those docs are **not** vendored here (see `not_vendored` in the manifest) |
| `caveman` | JuliusBrussee/caveman `2e08b917` | Apache-2.0 | `LICENSING.md` at the pin: "Everything in this repository is licensed under the Apache License, Version 2.0, starting with Caveman 3.0.0"; pre-3.0 MIT parts keep an MIT notice (`LICENSE-MIT`). Manifest previously said MIT — corrected this round |
| `grug` | bigskysoftware/grugbrain.dev `b1b1ca85` | Grug 1-Clause License ("do what want") | repo `LICENSE` at the pin; `package.json` says BSD. No CC BY-SA statement found in the repo or on the live site (checked the rendered page end to end). Manifest previously said "CC BY-SA 4.0 (site)" — corrected this round |
| `strix` | usestrix/strix `6b7ae2eb` | Apache-2.0 | `LICENSE` at the inspected commit; only four method skills are carried |
| `mem0` | mem0ai/mem0 `753496cf` | Apache-2.0 | `LICENSE` at the inspected commit |
| `archify` | tt-a1i/archify `a4065941` | Apache-2.0 | `LICENSE` at the new pin; the previous pin was MIT (`LICENSE-MIT` retained upstream for historical releases). Manifest label updated with the pin |
| `local` | this repository (`legacy/`, `one-skill/written/`) | Unlicense (root), except `legacy/caveman-universal/` which is MIT | root `LICENSE`; `legacy/caveman-universal/LICENSE` (MIT). The manifest carries both labels; `legacy/` is frozen |

## B. Source archives kept at the repository root

| Archive | sha256 (first 16) | Licence stated inside | Notes |
| --- | --- | --- | --- |
| `Skill creator copy-v1.zip` | `64e07a41da76bba6` | Apache-2.0 — `skills/skill-creator-copy/LICENSE.txt` | Manifest previously said "see the pack" — corrected to Apache-2.0 this round |
| `Engineering-1.2.0-v1.zip` | `07e0c8272f9ed2b0` | **No licence stated inside the archive** (`plugin.json` names Anthropic as author; no LICENSE file) | The upstream repo this pack corresponds to (`anthropics/knowledge-work-plugins`) states Apache-2.0 at its root (checked via the GitHub API, 2026-11-02). Whether that statement covers this archive is an **owner decision** (see Flags); until decided, the manifest records "not stated in the pack" and no stronger claim is made anywhere in this repo |

## C. Referenced, not vendored (facts only; authored text in this repo)

The domain skills and two one-skill deltas were written for this repository
using checked facts from these projects. No upstream prose is copied; each
skill's manifest entry records exactly which facts were used.

| Project | Inspected | Licence as stated | What this repo does with it |
| --- | --- | --- | --- |
| morluto/rea (`rea-agents` 6.8.0) | `8250bf23` | MIT (its distribution also bundles third-party components under their own licences in `licenses/`) | Defers to it at runtime; REA's skill, orchestration and agents are not carried |
|  | `61a1fbc8` | Apache-2.0 | Check/install facts for re-native |
| HexRaysSA/ida-mcp | `391c2f06` | MIT (IDA Pro itself is commercial) | Check/install facts for re-native |
| icsharpcode/ILSpy | `68766c04` | MIT | `ilspycmd` flag facts for re-managed |
| SamboyCoding/Cpp2IL | `b5ad444b` | MIT | Output-format and recovered-body facts for re-managed |
| petergyang/no-ai-slop | `000650b1` | MIT | Pattern *delta* re-authored as `written/prose-detect.md`; the skill text is not carried |
| rehan-remade/universal-modder | `9811709d` | MIT | Domain-neutral practices re-authored as `written/field-practices.md`; `modder-bridge` defers to the tool |
| vercel-labs/skills | `92a9a34a` | MIT | Only its published discovery rules (containers/depth) informed the `skills/` publish layout; no code or text taken |

## D. SkillOpt

`skillopt-integration/` contains no SkillOpt source. It plugs into an
installed SkillOpt (MIT, microsoft/SkillOpt `bc0a392e` inspected) through
its extension points. The user's fork `freeforall1932-design/SkillOpt-fork`
(`e2edfa97`, 0 ahead / 2 behind upstream as of 2026-11-02) is read-only from
this repository: nothing here vendors or modifies it; see
`skillopt-integration/TRAINING.md`.

## Flags for the owner (no conclusion drawn here)

1. **Engineering pack licence (B above):** decide whether the upstream
   repo's root Apache-2.0 is the licence this archive is carried under, or
   keep it as "not stated" (current state). Content from it is already
   vendored under the manifest either way; this is about the label and any
   redistribution conditions, which deserve an explicit owner call.
2. **Grug wording (A above):** the repo LICENSE, `package.json` (BSD) and
   the website do not use the same label. The manifest now quotes the repo
   LICENSE at the pin ("Grug 1-Clause"). If the site text is later treated
   as a different source, re-check its terms then.
3. **`legacy/` provenance:** `legacy/caveman-universal/` is MIT inside an
   otherwise Unlicense tree, and `legacy/` is frozen (read, do not add).
   The manifest's `local` label records both; nothing needs doing unless
   legacy content starts moving again.

## How to re-run this audit

Re-clone each origin at the manifest pin (`one-skill/build.py sync` already
verifies pins), compare `LICENSE*`/`LICENSING*` against this file and the
`license` fields in `one-skill/sources.json`, and check both root archives
with `unzip -l` + `sha256sum`. Any label change goes through the manifest
first, then `python3 one-skill/build.py all` regenerates the copies.
