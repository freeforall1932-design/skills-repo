---
name: evidence-notes
description: >
  Use when an investigation needs a checkable record: turning output from
  REA, Ghidra, IDA, ILSpy, Cpp2IL or Strix into evidence entries with
  SHA-256 pins, locations and confidence, plus optional mem0 recall for
  confirmed facts. Do not use for general note-taking or storing secrets.
---

# Evidence Notes

## When to use / when not to use

Use to record what an investigation established, so a later reader can
re-check every claim: one claim, one artifact, its limits stated. Not a bin
for transcripts, preferences or plans. This skill installs nothing. Write
notes in the user's language (English or Indonesian); hashes, addresses,
tool names and code stay byte-exact. If one-skill is installed, its
registers govern your prose.

## Preflight

1. Name the notes file (`notes/<target>.md`), outside any public path the
   user did not choose.
2. Pin the target first: `sha256sum <file>` (`shasum -a 256` on macOS),
   plus version string where the target states one.
3. Check the redaction helper: `python3 scripts/redact.py --check` prints
   `ok`; if absent, follow [references/redaction.md](references/redaction.md)
   by hand and say so.
4. If REA analysed this target (`npx -y rea-agents@latest doctor` shows
   it), reuse its REA Evidence fields, don't invent parallels; setup is
   `npx rea-agents setup`, through re-triage.

## Method

1. Open the ledger with identity: target, sha256, version, authorization,
   question.
2. Write one entry per claim, from the template, before moving on.
3. Keep excerpts to a few lines; point to the rest by path, address or
   offset. Never paste whole decompiled dumps or commit binaries.
4. Redact every excerpt, then re-read it for secrets patterns miss.
5. Set `confirmed` only when a second source or a runtime check agrees.
6. Record limits inside the entry: unchecked is a fact about the entry.
7. Close with lessons learned: wrong turns, their shape, first probe next.

## Evidence

```text
E7 | claim: expiry compared against a fixed date
target: app.dll sha256:9f2c… | tool: ilspycmd 11.2
location: Acme.Licensing.Check | excerpt: if (today > expiry) …
confidence: likely | limits: decompiler only; IL unread
next: -il on same member, compare branch
```

Ledger rules in full: [references/ledger.md](references/ledger.md).

## What this cannot prove

A tidy ledger proves notes were kept, not that claims are true. Confidence
is judgement, a hash pins identity only, and a missing entry means "not
recorded" — never "checked and clean".

## Fallback

Plain text is enough. Say how identity was pinned (a listing is weaker than
a hash), redact by eye, mark unverified claims `hypothesis`. Optional mem0
recall ([references/mem0-recall.md](references/mem0-recall.md)) stores only
confirmed, distilled facts under explicit user/agent/session scope; the
notes file stays the source of truth, and secrets are never stored. Probe
it with a `mem0 search`; setup pointers are at docs.mem0.ai.

## Pairs with

re-triage, re-native, re-managed, appsec-strix — sources of claims to
record. All optional; the ledger stands alone.
