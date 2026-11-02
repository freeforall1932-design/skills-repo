# The ledger, in full

One file per investigation. Header first, then numbered entries, then a
lessons-learned block. Write in the user's language; never translate
identifiers, addresses or hashes.

## Header

```text
# <target> — investigation notes, <date>
Target pinned: <name>, sha256:<full hash or first 16 + …>, version/build
Authorization: <who owns or authorized it, one line>, scope: <…>
Question: <the one question this file answers>
Tools seen: <name + version for each actually run>
```

Identity is pinned with `sha256sum` (or `shasum -a 256` on macOS; both ship
with coreutils equivalents on every desktop OS — there is nothing to
install). A hash of the wrong file is worse than none: hash the artifact the
claim is about, after any extraction step you performed, and say so.

## Entry fields

- **id** — `E1`, `E2`, …, never reused, so chats and issues can cite them.
- **claim** — one sentence, falsifiable. "Licensing looked odd" is not a
  claim; "Check compares today against a hard-coded 2026-01-01" is.
- **target** — name + sha256 (+version). Repeat it even though the header
  has it; excerpts travel.
- **tool + version** — the exact binary and version that produced the
  excerpt (`ilspycmd 11.2.0`, not "ILSpy").
- **location** — address, file:line, type.member, offset, URL+route. Enough
  for a stranger to land on the same spot.
- **excerpt** — a few lines, redacted. Pointers for anything longer.
- **confidence** — `confirmed` (two independent sources, or runtime
  observed), `likely` (one good source, no contradiction), `hypothesis`
  (inferred, name/string-only, or generated output such as decompiled
  pseudocode awaiting disassembly agreement).
- **limits** — what was not checked, what could be misleading (packing,
  obfuscation, version skew, a stub body).
- **next probe** — the smallest action that would raise or kill confidence.

When REA did the analysis, REA Evidence entries already carry several of
these fields in REA's own shape. File them as-is under this header and add
confidence/limits where REA left them implicit; do not keep two competing
formats for the same target.

## Storage hygiene

Notes are text. Do not commit binaries, pcaps, full decompiled trees or
database dumps alongside them — record where the artifact lives and its
hash instead. Keep the file out of public locations unless the user chose
that on purpose; an evidence file names weaknesses precisely, which is the
point and also the risk. Secrets never enter, even as "context" (see
redaction.md).

## Lessons learned

Close with: the route that worked, the wrong turns and their common shape,
tool quirks hit (with versions), and what the first probe should be if this
target or its sibling comes back. This is the part future sessions read
first.
