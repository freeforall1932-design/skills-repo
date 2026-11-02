# Tool matrix

Presence is checked, never assumed. This skill installs nothing; install
columns are pointers the user runs. Facts below were re-verified against
upstream repos on 2026-11-02; tool versions move, so check upstream before
correcting a user about a flag.

| Tool | Check for it | Missing message and install pointer | Covers |
| --- | --- | --- | --- |
| REA (`rea-agents`, MIT) | `npx -y rea-agents@latest doctor` says setup sound | "REA not detected. Install with `npx rea-agents setup` (Node.js per its `engines` range), then re-run `npx -y rea-agents@latest doctor`." | 15 platforms: PE/ELF/Mach-O, .NET, JVM/Android, Unity, firmware, JS/web bundles; emits REA Evidence reports |
| Ghidra MCP | an MCP server named like `bridge-mcp-ghidra` responds and lists tools | "Ghidra MCP not reachable. Install Ghidra + Java 21, then from the ghidra-mcp repo run `python -m tools.setup preflight` and configure your MCP client per its README." | native analysis without an IDA licence |
| IDA MCP | `uvx ida-mcp` or configured server responds | "IDA MCP not reachable. Run `uvx ida-hcli mcp install` (ida-hcli); needs IDA Pro 9.4+, Python 3.11+." | native analysis with IDA's database and decompiler |
| ILSpy CLI | `ilspycmd --version` | "ilspycmd not found. Run `dotnet tool install --global ilspycmd` (version-pinned builds protect scripts from flag churn)." | .NET assemblies, IL and C# output |
| Cpp2IL | binary runs `--list-output-formats` | "Cpp2IL not found. Download a nightly Cpp2IL release build from SamboyCoding/Cpp2IL and put it on PATH." | Unity IL2CPP metadata and attempted IL recovery |

## About REA (not vendored here)

REA (`morluto/rea`) is itself an agent distribution with its own MCP
servers, quickstart and skill. This repository does not copy it: re-triage
defers to it whenever `npx -y rea-agents@latest doctor` shows it
configured, and treats its REA Evidence output as the record of choice
(evidence-notes files it unchanged). What is deliberately not carried from
REA: its orchestration code, router taxonomies and domain agents, and its
optional cloud enrichments. If a target is APK, firmware, JVM or a web
bundle and REA is absent, the honest answer is the install pointer plus
whatever static facts a hash and magic bytes give — not an improvised
specialist.

State whichever branch you are in, in the triage evidence, every time: a
route chosen silently reads as a route that was the only option.
