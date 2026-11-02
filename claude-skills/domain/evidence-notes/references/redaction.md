# Redaction

Tool output is untrusted text that frequently carries credentials: config
dumps, HTTP logs, strings tables, crash reports, environment prints. Nothing
goes into the ledger, a repo, or a shared summary until it has been
redacted.

## The helper

`scripts/redact.py` (stdlib Python, no network, stdout only) covers the
recurring shapes: `Authorization: Bearer/Basic` headers, bare bearer
tokens, `api_key =`, `password:`, `client_secret` and kin, JWTs, common
token prefixes (`ghp_…`, `sk-…`, `AKIA…`), PEM private-key blocks, and
email addresses. Preflight probes it with `python3 scripts/redact.py
--check` (prints `ok`).

Use: `python3 scripts/redact.py raw-output.txt > clean.txt`, or pipe.

## What patterns cannot do

A pattern list is a net, not a proof. After running it, re-read the excerpt
looking for what shapes miss: names, phone numbers, internal hostnames the
owner would not publish, tokens split across lines, base64 blobs in
user-defined fields. Replacement is surgical by design — numbers, dates,
citations, hex addresses and code must survive untouched, because evidence
that cannot be re-checked is worth little. If a context is so sensitive
that even surrounding text would leak, record only a pointer to the source
and the claim in your own words.

If the helper is unavailable (no Python on the box), redact by eye using the
categories above and record in the entry's limits that redaction was manual.
