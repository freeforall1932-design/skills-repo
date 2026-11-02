# IDA MCP backend

Driver: `HexRaysSA/ida-mcp` (MIT) — Hex-Rays' official MCP server for IDA
Pro. Facts re-verified 2026-11-02 against its README and package metadata.

## Presence and setup

- Check: the MCP server responds, or `uvx ida-mcp` starts (it needs IDALIB
  and a licensed IDA Pro 9.4+; Python 3.11+).
- Missing message: "IDA MCP not reachable. This skill does not install it:
  with IDA Pro licensed, run `uvx ida-hcli mcp install` (from the ida-hcli
  tool), or configure `uvx ida-mcp` in your MCP client per the HexRaysSA
  repo."
- Cost/licence: IDA Pro is commercial. If there is no licence, say so and
  route to Ghidra MCP — never suggest cracked copies.
- Headless (no GUI) works through IDALIB, which is the normal CI/agent
  shape; a database must exist or be created from the binary first.

## Driving it well

- Open the existing `.i64` when one exists: prior renames/types are
  evidence too, and re-analysis wastes them. Record the database path in
  the ledger.
- Inventory first (imports, strings, functions, segments), then decompile
  the scoped slice. Hex-Rays pseudocode is strong and still a hypothesis:
  check branch-carrying conclusions against the disassembly listing and
  xrefs.
- Comment findings into the database as you go (address-level comments),
  and keep renamed guesses prefixed until a second source confirms them.
- Debugger/trace routes, when licensed and appropriate to the scope, are
  the way to promote `likely` to `confirmed`; note in the ledger when a
  runtime check was not possible instead of strengthening the claim by
  tone.

Tool names and transport details evolve: read the live tool list from the
connected server rather than trusting a copied list.
