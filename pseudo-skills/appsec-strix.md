> **Paste-only setup — method only.** This is the `appsec-strix` domain skill
> without its reference files: the gate, method and fallback below stand alone,
> but per-tool preflight detail lives in `references/` beside the real skill in
> `skills/appsec-strix/`. Paste a reference next to this file when a task needs one.
> Nothing here installs any tool; preflight names what to check.

---
name: appsec-strix
description: >
  Use when planning or running an authorized application-security test with
  Strix, or reviewing its findings: written scope, offline survey first,
  then Strix's own skill drives execution and you verify its reports. Local
  Strix runs need Docker; cloud runs do not. Do not use without written
  authorization or against third-party systems.
---

# AppSec with Strix

## When to use / when not to use

Use to govern a Strix run: authorization, scope, preflight, verification,
honest coverage. Tool-driving mechanics belong to Strix's own skill
(`penetration-testing-with-strix`); this runbook does not duplicate its
flag tables. Not a scanner and not a "is this secure?" oracle.

## Authorization gate

Written authorization, worded as scope — targets, exclusions, window,
grantor — is a precondition. No scope: stop, ask, run nothing, not even a
"quick check". Owned systems, engagements, labs/CTFs only. Refusals for
other targets are recorded, not negotiated down.

## Preflight

1. Scope statement lands in the notes header (evidence-notes).
2. `strix --version`. Missing: stop; install pointer in
   [references/strix.md](references/strix.md). This skill installs nothing.
3. Edition: OSS CLI needs `docker info` healthy plus an LLM key; cloud
   needs login, no Docker. Say which will run.
4. Strix's own skill present? It drives. Absent: say so; upstream docs plus
   this governance only.
5. If one-skill is installed, its registers govern your prose; URLs and
   CVE ids stay byte-exact.

## Method

1. Record authorization + scope; targets outside stay untouched even if
   discovered (log as out-of-scope observations).
2. Survey offline first: local code/config/routes; note expected surface,
   so the run can be checked against something.
3. Configure scope, target list, budget cap and scan mode from Strix's own
   docs/skill — never from memory. Start bounded: quick pass, least
   sensitive target.
4. Run Strix; then triage every finding by hand. Reproduce it or read the
   cited code before believing it; scanner severity is a claim.
5. Record surviving findings as evidence: location, excerpt, confidence,
   impact in the owner's terms.
6. Propose fixes as ordinary engineering tickets; re-test after the fix
   and record the re-test beside the finding.
7. Close with the coverage statement (below).

## Evidence

```text
Run: strix (OSS) <ver>, staging only, window 2026-11-02T02:00Z
F2 | IDOR /orders/{id} | reproduced by hand | confidence: confirmed
fix: ownership check | retest: pending
Coverage: OpenAPI routes only; auth flows + websockets untested
```

Run detail and install pointers: [references/strix.md](references/strix.md).

## What this cannot prove

A clean run proves the tool found nothing along the paths, modes and
timebox it exercised — not that the system is secure. Logic flaws, drift
after the run, and anything off the target list stay unexamined; name them.

## Fallback

No Strix/Docker/budget: stop at the offline survey. Deliver the surface
inventory and a manual test plan, everything `hypothesis`, missing piece
stated exactly. Never fabricate a scan outcome.

## Pairs with

evidence-notes for scope and findings; one-skill's workflow to ticket and
fix confirmed findings with tests.
