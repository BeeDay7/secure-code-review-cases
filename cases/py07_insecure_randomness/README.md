# Predictable password-reset tokens

| | |
|---|---|
| **Weakness** | CWE-338: Use of Cryptographically Weak PRNG |
| **OWASP Top 10 (2021)** | A02 Cryptographic Failures |
| **Language** | Python |

## What goes wrong
Reset tokens come from `random`, a predictable generator. Observing some outputs (or knowing the seed) lets an attacker predict others.

## Why it matters
Account takeover through guessed reset links.

## The fix
Generate security tokens with the `secrets` module.

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
