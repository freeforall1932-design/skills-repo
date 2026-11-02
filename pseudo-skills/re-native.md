> **Paste-only setup — method only.** This is the `re-native` domain skill
> without its reference files: the gate, method and fallback below stand alone,
> but per-tool preflight detail lives in `references/` beside the real skill in
> `skills/re-native/`. Paste a reference next to this file when a task needs one.
> Nothing here installs any tool; preflight names what to check.

---
name: re-native
description: >
  Use when analysing native binaries (PE, ELF, Mach-O) already identified
  by triage, driving Ghidra MCP or IDA MCP, or REA when configured, to
  explain functions and behaviour. Do not use for .NET or Unity-managed
  code (see re-managed), patching, or defeating licensing, DRM or
  anti-cheat checks.
---

# RE Native

## When to use / when not to use

Use for native code questions: what this function does, where X is decided,
which imports matter. Not for first identification (re-triage), managed
assemblies (re-managed), or producing patches.

## Authorization gate

Authorization line first: owner, engagement, or lab/CTF provenance, plus
scope. Missing: stop and ask; open nothing. Default scope is analysis-only:
rename and comment inside the database, never modify the binary unless
asked in writing. Licence bypass, anti-cheat evasion, DRM circumvention:
never in scope.

## Preflight

1. Target pinned: `sha256sum`, format, bitness (rerun triage if unrecorded).
2. Pick a backend in this order and say which: REA configured
   (`npx -y rea-agents@latest doctor`; setup is `npx rea-agents setup`);
   IDA MCP (`uvx ida-mcp`); Ghidra MCP (`bridge-mcp-ghidra`). IDA vs Ghidra
   follows licence and connectivity.
3. None reachable: emit the fallback report; do not guess.
4. If one-skill is installed, its registers govern your prose; symbols,
   addresses and code stay exact regardless of language.

## Method

1. Open or reuse the analysis database; log its path and tool version.
2. Inventory imports, exports, strings, sections, entry points. Note
   packers — high entropy changes every later claim.
3. Work from the scoped questions. Rename as evidence lands; prefix guesses
   (`guess_licenseCheck`) until confirmed.
4. Pseudocode is hypothesis. For any branch carrying a conclusion, confirm
   the disassembly agrees (recovery hides casts and inlining); runtime
   outranks both.
5. Cross-check each key claim a second way — xref, string ref, dynamic
   trace — before calling it `confirmed`.
6. Stop at the scope edge. One evidence entry per claim, excerpts short
   and located (function + address).

## Evidence

```text
E3 | claim: trial gate is time-based, not feature-flagged
target: app.exe sha256:77d1… | tool: IDA 9.4 via IDA MCP
location: sub_14001B220 | excerpt: cmp rax, [expiry]; ja loc_expired
confidence: likely | limits: disasm agrees; runtime untested
next: trace call under debugger, watch expiry value
```

Load exactly one backend file: [references/ghidra-mcp.md](references/ghidra-mcp.md)
or [references/ida-mcp.md](references/ida-mcp.md).

## What this cannot prove

Static views cannot prove runtime behaviour: unpacked payloads, plugins,
JIT and server-side decisions stay invisible. Symbols and strings are the
author's claims, not facts. Name the layer each claim rests on.

## Fallback

No backend: report hash and format, plus imports/strings only if
`strings`/`readelf`/`dumpbin` actually exist. Name the missing backend and
its install pointer from the references; mark all `hypothesis`.

## Pairs with

re-triage upstream; evidence-notes for the record; re-managed when a native
shell wraps managed payloads (IL2CPP second pass).
