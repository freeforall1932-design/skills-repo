---
name: re-triage
description: >
  Use when an unknown binary, app or firmware sample needs a first look and a
  route: identify the target, then hand off to REA (rea-agents) when present,
  to Ghidra MCP or IDA MCP for native code, or to ILSpy (ilspycmd) and
  Cpp2IL for .NET and IL2CPP. Do not use for deep analysis of an identified
  target, patching, or anything outside written authorization.
---

# RE Triage

## When to use / when not to use

The front door: "what is this file, how do I analyse it?" Deliver an
identification, a route, and the first evidence entries. Target already
identified: go straight to the specialist skill.

## Authorization gate

Before any probe, obtain the authorization line in writing: who owns the
target or authorizes the analysis, and the scope. Only work on systems
owned by the user, covered by an engagement, or realistically test targets
(labs, CTFs, your own game and software installs). No line: stop, ask, run
nothing. Bypassing anti-cheat, DRM or licence checks is out of scope for
every skill here, authorized or not.

## Preflight

1. `npx -y rea-agents@latest doctor` — configured REA is the front door.
   Missing: say "REA not detected; routing by format"; install is the
   user's call (`npx rea-agents setup`).
2. Note file size and `sha256sum` before opening anything.
3. Format probe from magic bytes only; never execute the target.
4. If one-skill is installed, its registers govern your prose; notes follow
   the user's language, identifiers stay exact.

## Method

1. Record the authorization line at the top of the notes (evidence-notes).
2. Identify: format (PE/ELF/Mach-O/APK/ZIP-in-disguise/firmware), bitness,
   runtime fingerprints (.NET metadata, `GameAssembly`, `global-metadata`,
   Electron `resources/app`, JVM classes).
3. If REA is present, start there: it covers 15 platforms, JS/web bundles,
   APK and firmware, and writes its own evidence reports. Everything below
   is the route when REA is absent or hands off.
4. Route native PE/ELF/Mach-O to re-native; .NET or Mono assemblies to
   re-managed; IL2CPP (`GameAssembly` + `global-metadata.dat`) to
   re-managed first, re-native after.
5. Electron/webview → JS/HTML under REA/web tooling; APK/JVM, firmware →
   REA. No specialist skill here covers these: say so.
6. Note what resisted identification; emit first evidence entries (target,
   hash, route).

## Evidence

```text
Triage: sample.exe sha256:41ab… | PE32+ x64, no CLR header, imports list
Route: re-native (Ghidra MCP) | REA: not detected
Authorization: user-owned install, analysis only
Limits: packed (high entropy .text) — identification provisional
```

## What this cannot prove

Triage identifies containers, not intent. Fingerprints can be spoofed or
packed; every finding is hypothesis until the specialist pass confirms it.

## Fallback

No REA, MCP or decompiler: report file facts only (hash, size, magic,
strings actually seen), the recommended route and the exact missing tool,
and stop. Never invent behaviour from a filename.

## Pairs with

evidence-notes for the record; re-native / re-managed as downstream
specialists; modder-bridge when the target is a game you own and the goal
is content. Full tool matrix: [references/tool-matrix.md](references/tool-matrix.md).
