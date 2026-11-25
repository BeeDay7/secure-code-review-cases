# Fast, unsalted password hashing

| | |
|---|---|
| **Weakness** | CWE-916: Use of Password Hash With Insufficient Computational Effort |
| **OWASP Top 10 (2021)** | A02 Cryptographic Failures |
| **Language** | Python |

## What goes wrong
Passwords are stored as unsalted MD5. Identical passwords give identical hashes, and billions of guesses per second are possible.

## Why it matters
A database leak exposes most user passwords within hours.

## The fix
Use a slow, salted key-derivation function (scrypt here; Argon2 or bcrypt are also good) and compare in constant time.

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
