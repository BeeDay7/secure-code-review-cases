# Session token accepted without signature check

| | |
|---|---|
| **Weakness** | CWE-347: Improper Verification of Cryptographic Signature |
| **OWASP Top 10 (2021)** | A07 Identification and Authentication Failures |
| **Language** | Python |

## What goes wrong
The server reads the user name from a token but never checks the signature, so anyone can write their own token claiming to be an administrator.

## Why it matters
Full account takeover, including admin accounts.

## The fix
Verify an HMAC signature with a server-side secret, in constant time, before trusting any claim.

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
