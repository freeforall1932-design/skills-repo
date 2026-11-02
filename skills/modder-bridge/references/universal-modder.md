# universal-modder: the tool this skill defers to

Tool: `rehan-remade/universal-modder` (MIT) — a TypeScript CLI (`um`) with
a searchable modding knowledge base and its own skills. Shape re-verified
2026-11-02 against its README, AGENTS.md and SECURITY.md.

## Presence and setup

- Check: `um --version`.
- Missing message: "universal-modder not installed. This skill does not
  install it: its skills install with
  `npx skills add https://github.com/rehan-remade/universal-modder`; the
  `um` binary comes from its releases or source (see its README). Without
  it, this skill still runs the scoped minimal workflow."
- Its own hard rules mirror this skill's gate: owned games, offline,
  backups before writes, and game files never committed or redistributed.

## Deference, in practice

When `um` exists:

1. `um kb search` for the game/engine/topic before any recon of your own —
   the KB records formats and failure history per title.
2. Follow its `mod-any-game` workflow (recon → backed-up lab → source map →
   vertical slice → verify in the real game → package/uninstall docs);
   keep evidence-notes entries alongside.
3. Use its engine plugin for the target before improvising format support;
   where it ships a reverse-engineering skill, prefer it over re-* skills
   for that game's known surfaces, and say which authority you followed in
   the ledger.

Where one-skill is also installed, engineering discipline for any helper
code (tests, version control, review) comes from there; game-domain facts
come from `um`'s KB. Conflicts: KB facts about the game win over your
memory of the engine, and the running game wins over both.
