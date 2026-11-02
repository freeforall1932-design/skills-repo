#!/usr/bin/env python3
"""Redact secrets from investigation excerpts before they enter a ledger.

Usage:
    python3 redact.py --check          # prints "ok"; used by preflight
    some-command | python3 redact.py   # redacted text to stdout
    python3 redact.py raw-log.txt      # redacted file contents to stdout

Stdlib only, no network, never writes in place. Redaction is pattern-based:
it catches the shapes below and preserves everything else byte-for-byte
(numbers, dates, citations, code). Patterns cannot know every secret, so
the output still gets a human re-read before it is stored or shared.
"""

from __future__ import annotations

import re
import sys

REDACTED = "<REDACTED>"

PATTERNS: list[tuple[re.Pattern, str]] = [
    # PEM private key blocks, whole block
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", re.S),
     f"-----BEGIN PRIVATE KEY-----\n{REDACTED}\n-----END PRIVATE KEY-----"),
    # Authorization headers and bearer tokens
    (re.compile(r"(?i)(Authorization:\s*Bearer\s+)(\S+)"), r"\g<1>" + REDACTED),
    (re.compile(r"(?i)(Authorization:\s*Basic\s+)(\S+)"), r"\g<1>" + REDACTED),
    (re.compile(r"(?i)\b(Bearer\s+)([A-Za-z0-9._~+/=-]{16,})"), r"\g<1>" + REDACTED),
    # key = value / key: value shapes, quoted or not
    (re.compile(r"""(?ix)\b(api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|
                    password|passwd|secret|session[_-]?key)(\s*[:=]\s*)(["']?)([^\s"']{4,})(\3)"""),
     r"\g<1>\g<2>\g<3>" + REDACTED + r"\g<5>"),
    # JWTs
    (re.compile(r"\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b"), REDACTED),
    # well-known token prefixes
    (re.compile(r"\b(ghp|gho|github_pat|sk|AKIA)[A-Za-z0-9_-]{16,}\b"), REDACTED),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), REDACTED),
    # email addresses (personal data in logs)
    (re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), "<REDACTED:EMAIL>"),
]


def redact(text: str) -> str:
    for pattern, replacement in PATTERNS:
        text = pattern.sub(replacement, text)
    return text


def main(argv: list[str]) -> int:
    if "--check" in argv:
        print("ok")
        return 0
    paths = [a for a in argv if not a.startswith("-")]
    if len(paths) > 1:
        print("redact.py: pass at most one file, or pipe stdin", file=sys.stderr)
        return 2
    data = open(paths[0], encoding="utf-8", errors="replace").read() if paths else sys.stdin.read()
    sys.stdout.write(redact(data))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
