---
name: re-managed
description: >
  Use when analysing .NET or Mono assemblies with ILSpy (ilspycmd), Unity
  IL2CPP builds with Cpp2IL, or REA when configured: recover types, members
  and logic and explain them. Do not use for native-only binaries (see
  re-native), for patching, or for defeating licensing, DRM or anti-cheat
  checks.
---

# RE Managed (.NET, Mono, IL2CPP)

## When to use / when not to use

Use when triage found a CLR header, Mono markers, or an IL2CPP pair
(`GameAssembly` + `global-metadata.dat`). Not for JVM/APK (REA) or
marker-free native code.

## Authorization gate

Authorization line first: owner, engagement, or lab/CTF provenance, plus
scope. Missing: stop and ask; decompile nothing. Decompilation is for
understanding, interop and security review of what you may analyse.
Licence bypass, anti-cheat evasion, DRM circumvention: never in scope.

## Preflight

1. Target pinned (`sha256sum`), runtime identified by triage.
2. .NET/Mono → check `ilspycmd --version`. Missing: say so, pointer
   `dotnet tool install --global ilspycmd`; this skill installs nothing.
3. IL2CPP → check the Cpp2IL binary runs `--list-output-formats`; confirm
   `global-metadata.dat` sits alongside `GameAssembly` first. A configured
   REA (`npx -y rea-agents@latest doctor`, setup `npx rea-agents setup`)
   may cover both: if so, defer, saying so.
4. If one-skill is installed, its registers govern your prose; type and
   member names stay byte-exact.

## Method

1. Inventory first: types and members (`ilspycmd -l c,i,s`), resources
   (`--list-resources`), entry points. Obfuscation (renamed `a.b.c`)
   downgrades every later claim — record it.
2. Decompile the scoped slice to C#. For any claim that matters, open the
   IL view (`-il`) on the same member: decompiler output is reconstructed,
   and async/iterator/async-state machines are where reconstruction lies
   most politely.
3. IL2CPP: run Cpp2IL for metadata (types, members, string literals) and
   DLL output. Recovered bodies are attempted machine-code-to-IL
   translations: expect stub or exception bodies, rough IL and wrong call
   targets. Treat every recovered body as hypothesis.
4. Verify IL2CPP logic claims against `GameAssembly` in re-native before
   calling them `likely`; names/metadata are claims about structure, not
   behaviour.
5. Decompile to scratch, never into the repo; cite `Type.Member` + assembly
   sha256, excerpt a few lines.
6. Record tool + version per entry; unversioned citations rot.

## Evidence

```text
E5 | claim: save file gated by a checksum, not encryption
target: Assembly-CSharp.dll sha256:b208… | tool: ilspycmd 11.2 -il
location: Save.Checksum.Update  | excerpt: IL_0042 call uint32 Crc::Step
confidence: confirmed (IL + C# agree) | limits: seed constant not traced
next: find Crc.Init callers, read seed
```

Per-tool detail — load one: [references/ilspy.md](references/ilspy.md),
[references/cpp2il.md](references/cpp2il.md).

## What this cannot prove

Decompiled C# proves plausible source shape, not original source, comments
or intent; Cpp2IL bodies prove even less. A clean-looking guard may be
dead code, patched server-side, or replaced by an AOT'd/native twin.

## Fallback

No tools: report what triage established (CLR present, assembly names if
metadata tools exist), the exact missing tool and install pointer, and
mark behaviour claims unmade — not guessed.

## Pairs with

re-triage upstream; re-native as IL2CPP's second pass; evidence-notes for
the record.
