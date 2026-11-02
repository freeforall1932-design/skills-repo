# Ghidra MCP backend

Driver: `bethington/ghidra-mcp` (Apache-2.0) — a Ghidra extension plus a
Python MCP bridge (`bridge-mcp-ghidra`). Facts re-verified 2026-11-02
against its README/docs; the catalogue held 219 tools, including headless
batch decompilation and P-code emulation.

## Presence and setup

- Check: your MCP client lists its tools (functions like list/import
  programs, decompile, xrefs). A listed-but-silent server means the Ghidra
  side is not connected: ask the user to open the project; do not narrate
  results you cannot see.
- Missing message: "Ghidra MCP not reachable. This skill does not install
  it: install Ghidra (12.x) with Java 21, clone
  `bethington/ghidra-mcp`, run `python -m tools.setup preflight`, and
  register `bridge-mcp-ghidra` in your MCP client per its README
  (`Ghidra path` discovery is documented there)."
- Cost/licence: Ghidra is free and open source; this is the no-IDA-licence
  route. Analysis runs locally; no account.

## Driving it well

- Import, let auto-analysis finish, then inventory before theorizing:
  functions, imports, strings, memory map/sections.
- Batch-decompile only the slice in scope; whole-program pseudocode dumps
  drown the context and the evidence value per token collapses.
- Renames and comments live in the Ghidra project (`.gpr`): record the
  project path in the ledger header so the session can resume.
- Pseudocode stays hypothesis until the listing agrees on the branches you
  cite; use the emulator/trace tooling, when available, as the second
  source rather than re-reading the same decompile.

Tool names and arguments change between releases: read the live tool list
from the connected server instead of trusting any list here.
