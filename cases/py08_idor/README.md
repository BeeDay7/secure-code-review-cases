# Insecure direct object reference in an invoice API

| | |
|---|---|
| **Weakness** | CWE-639: Authorization Bypass Through User-Controlled Key |
| **OWASP Top 10 (2021)** | A01 Broken Access Control |
| **Language** | Python |

## What goes wrong
The handler returns any invoice whose ID is in the URL. It checks that the user is logged in, but not that the invoice belongs to them.

## Why it matters
Any customer can read every other customer's invoices by changing a number.

## The fix
Check ownership on every object access (or query by owner), and return the same error for "not found" and "not yours".

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
