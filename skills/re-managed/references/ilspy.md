# ILSpy (ilspycmd)

Decompiler: `icsharpcode/ILSpy` (MIT). CLI surface re-verified 2026-11-02
against `ICSharpCode.ILSpyCmd` source and its README.

## Presence and setup

- Check: `ilspycmd --version`.
- Missing message: "ilspycmd not found. This skill does not install it:
  `dotnet tool install --global ilspycmd` (needs a .NET sdk; pin a version
  with `--version` when output feeds scripts, because reconstructed C#
  changes between releases)."
- A Docker packaging exists upstream for automation; the dotnet tool is the
  normal route. The GUI (Windows Avalonia builds sit next to it) is the
  same engine — CLI output is what an agent can cite.

## Driving it well

- Inventory: `ilspycmd -l c,i,s <asm>` lists classes/interfaces/structs;
  `--list-resources` lists embedded resources (often where config, keys or
  strings tables hide).
- Slice, don't dump: `-t <full type name>` or `-m <member>` decompiles one
  type/member. Whole-assembly `-p -o` project output is for scratch
  exploration, never for the repo.
- Verify in IL: add `-il` for the same member. Where C# and IL disagree in
  shape (hoisted closures, async/iterator state machines, `in`/`ref`
  reconstructions), IL is the evidence and C# is the reading aid — say so
  in the entry.
- PDB present? `--use-varnames-from-pdb` recovers local names, which
  upgrades readability without changing semantics; note whether a PDB was
  used, since it changes how strong "original names" claims are.
- Obfuscators: renamed-only obfuscation keeps logic readable; control-flow
  obfuscation makes decompiled output actively misleading. Record which
  you saw; it sets the confidence ceiling for the whole file.
- Cite `Type.Member`, assembly file + sha256, and `ilspycmd --version` in
  every ledger entry. Reconstructed text is versioned text.
