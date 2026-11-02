# Cpp2IL (Unity IL2CPP)

Tool: `SamboyCoding/Cpp2IL` (MIT). Behaviour re-verified 2026-11-02
against its README and core output formats.

## Presence and setup

- Check: the Cpp2IL binary runs `--list-output-formats` without error.
- Missing message: "Cpp2IL not found. This skill does not install it:
  download a nightly Cpp2IL release build from SamboyCoding/Cpp2IL
  (releases are moving builds; record the exact build), put it on PATH,
  and keep `global-metadata.dat` next to `GameAssembly`."
- Inputs are always a pair: the native `GameAssembly` (`.dll`/`.so`, or the
  executable on some platforms) and `global-metadata.dat`. A mismatch of
  the pair (wrong game version) produces garbage that looks structured —
  hash both, and record the Unity version Cpp2IL reports.

## What its output actually is (verified, not folklore)

Cpp2IL first recovers metadata: types, members, generic instantiations,
string literals. For method bodies it attempts machine-code-to-ISIL-to-IL
recovery; where that fails it emits stub or exception-throwing bodies, and
where it succeeds the IL is known-messy (call targets and control flow can
be wrong). Consequences for evidence:

- Type/member inventories, inheritance and string tables: useful,
  `likely` after a sanity spot-check.
- Any recovered body: `hypothesis`, always. Verify logic claims in
  `GameAssembly` via re-native (Ghidra/IDA) before promoting them.
- Absence of a type/member in Cpp2IL output is not evidence of absence in
  the binary (stripping, metadata version drift).

## Driving it well

- Pick the output format for the question (`--output-as`, list with
  `--list-output-formats`): `dll_il_recovery` attempts bodies (hypothesis,
  see above), `dll_throw_null`/`dll_empty` give browsable structure ILSpy
  can open, `diffable-cs` answers "what exists" in diffable text.
- Keep the generated tree in scratch; cite game version, both hashes,
  Cpp2IL build, and output format in the ledger.
- When metadata says a guard exists but the native side never calls it,
  the native pass wins — record the contradiction instead of resolving it
  by preference.
