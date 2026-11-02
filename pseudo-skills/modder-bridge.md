> **Paste-only setup — method only.** This is the `modder-bridge` domain skill
> without its reference files: the gate, method and fallback below stand alone,
> but per-tool preflight detail lives in `references/` beside the real skill in
> `skills/modder-bridge/`. Paste a reference next to this file when a task needs one.
> Nothing here installs any tool; preflight names what to check.

---
name: modder-bridge
description: >
  Use when the user wants to mod a game they own — items, stats, recipes,
  maps, post-game content — and universal-modder (the `um` tool) may or may
  not be installed: defer to it when present, run a minimal owned-game
  workflow when absent. Do not use for anti-cheat bypass, DRM or ownership
  circumvention, online exploits, or distributing game files.
---

# Modder Bridge

## When to use / when not to use

For content in one's own game copy when the path is unclear. With
universal-modder installed this mostly steps aside — its `mod-any-game`
workflow and KB run deeper. Not for multiplayer advantage or evasion.

## Authorization gate

Games the user owns, offline/single-player, local installs. State the
game, platform and version before touching files. No ownership or a
request aimed at anti-cheat, DRM, licence checks, or other players: stop
and refuse that part — offer the legitimate-content version of the ask
where one exists. Never redistribute game assets or extracted files.

## Preflight

1. `um --version`. Present: defer — `um kb search` first, follow its
   workflow; this skill keeps scope and records. Absent: say so; pointer in
   [references/universal-modder.md](references/universal-modder.md). This
   skill installs nothing.
2. Identify game, version, platform, engine fingerprint (Unity / Godot /
   Ren'Py / RPG Maker cues); re-triage if a binary is involved.
3. Snapshot before edits: modded files or whole profile aside, restore
   step noted. Backups are step one, not a rescue plan.
4. If one-skill is installed, its registers govern your prose; notes follow
   the user's language, file paths and ids stay exact.

## Method

1. Write the goal as a player-visible outcome ("beat boss → secret area"),
   not a file edit.
2. Search prior notes/KB for this game and engine before recon; someone
   may have mapped the format already.
3. Recon the data layout read-only; custom formats route to
   re-managed/re-native for understanding only.
4. Build the smallest vertical slice (one item, flag, or room), launch the
   real game, watch it work or fail, then scale.
5. Same approach fails three times alike: change approach; note what the
   failures rule out.
6. Verify no version drift: game updates silently invalidate offsets and
   ids; re-pin version + hashes after any patch.
7. Package notes, not game files: what changed, where the backup is, how
   to uninstall and restore.

## Evidence

```text
Goal: post-final-boss secret area | game v1.4.2 (hash recorded)
Slice: flag 0x2F1 set on boss clear → door opens | verified in-game: yes
Backup: mods-backup/2026-11-02/ | restore: copy back, tested
Limits: untested on new-game+ path
```

## What this cannot prove

One working slice proves that path, that version, that save state. Other
routes, NG+, DLC combos, post-patch behaviour: unknown. "Loads" ≠ "works".

## Fallback

No `um`, unknown engine: stop at backup + read-only inventory, hand over
findings and the missing piece, write nothing into the install.

## Pairs with

universal-modder when present; re-triage/re-managed/re-native for format
understanding; evidence-notes for the ledger; one-skill for any code
written along the way.
