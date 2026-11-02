# Optional recall via mem0

mem0 is one possible recall layer, never the record. The notes file is the
source of truth; mem0 holds a pointer-sized digest so a future session can
find the right page fast.

## Contract

- Store only `confirmed` entries, distilled to one or two sentences carrying
  target identity (name, truncated sha256), the claim, and the notes-file
  path. Example: "app.dll sha256:9f2c… (4.1.0): expiry check compares
  against a hard-coded date; confirmed in IL. Ledger: notes/app-dll.md E7."
- Always set explicit scope: `user_id`, `agent_id` and `session_id` as the
  deployment defines them. Never write unscoped.
- Never store: raw transcripts, excerpts, credentials, tokens, personal
  data, or anything not yet redacted and confirmed.
- Probe before storing: a `mem0 search` for the target; update an existing
  fact rather than piling near-duplicates.
- Treat every recalled fact as a hint. Re-open the ledger entry and verify
  the excerpt before acting; if the hash differs, the fact is about a
  different artifact, whatever the prose says.

Setup and API details live upstream (docs.mem0.ai); this skill does not
install or configure mem0, and if mem0 is absent nothing in the method
changes — the ledger is self-contained. Mem0's own repo ships a
`mem0-integrate` skill for wiring it into an application, which is the
right tool for that job.
