# Insecure deserialisation of a session cookie

| | |
|---|---|
| **Weakness** | CWE-502: Deserialization of Untrusted Data |
| **OWASP Top 10 (2021)** | A08 Software and Data Integrity Failures |
| **Language** | Python |

## What goes wrong
The session cookie is decoded with `pickle.loads`. Unpickling attacker-controlled bytes can execute arbitrary code.

## Why it matters
Remote code execution on the server from a single crafted cookie.

## The fix
Use a data-only format (JSON) and validate the expected fields; sign the cookie if it must be trusted.

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
