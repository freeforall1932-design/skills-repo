# Strix: editions, presence, deference

Tool: `usestrix/strix` (Apache-2.0). Shape re-verified 2026-11-02 against
its README and bundled skills.

## Editions (same `strix` binary)

- **OSS CLI** — local, needs Docker and your own LLM key
  (`STRIX_LLM` naming a LiteLLM model), agents run sandboxed. Cost is the
  LLM spend; govern it with a budget cap per run.
- **Cloud** (`strix cloud …`) — managed runs, no Docker or LLM key, domain
  registration and verification happen in their asset flow; billing is
  credit-based. If Docker is unavailable, use Strix Cloud or do not run;
  do not improvise infrastructure.

## Presence and setup

- Check: `strix --version`.
- Missing message: "Strix not installed. This skill does not install it:
  `pipx install strix-agent` (also published for uv/pip); upstream also
  offers an install script — if you use it, review it first like any
  `curl | bash`. Then set the LLM key per the quickstart at docs.strix.ai."
- Its own skills install from the upstream repo (`npx skills add
  usestrix/strix` per its docs). When `penetration-testing-with-strix` is
  among the agent's skills, it is the authority for flags, modes, target
  syntax and report formats; this runbook only governs authorization,
  verification and reporting. Flag details copied here would go stale —
  that is why they are absent.

## Running responsibly

- Non-interactive runs for auditability; targets spelled out, one per
  flag/line, never a wildcard that can wander outside scope.
- Cloud "verified domain" flows exist so scans hit assets their users
  control; treat any unverifiable target as out of scope regardless of
  edition.
- Findings output (local run directories, cloud dashboards) contains
  request/response captures: redact before anything enters the ledger or a
  ticket (evidence-notes), and never paste captured credentials into chat
  summaries.
- Record edition, version, target list, budget cap and the scan mode in
  the run header; a finding without its run context cannot be re-tested
  against the same ground.
