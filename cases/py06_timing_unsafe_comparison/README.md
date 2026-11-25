# Timing-unsafe comparison of an API key

| | |
|---|---|
| **Weakness** | CWE-208: Observable Timing Discrepancy |
| **OWASP Top 10 (2021)** | A02 Cryptographic Failures |
| **Language** | Python |

## What goes wrong
`==` on strings stops at the first different character, so response time leaks how much of a guessed key is correct.

## Why it matters
An attacker can recover a secret key one character at a time.

## The fix
Compare secrets with `hmac.compare_digest`, which takes the same time regardless of where the strings differ.

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
