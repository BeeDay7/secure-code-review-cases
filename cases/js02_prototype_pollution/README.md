# Prototype pollution in a deep-merge helper

| | |
|---|---|
| **Weakness** | CWE-1321: Prototype Pollution |
| **OWASP Top 10 (2021)** | A08 Software and Data Integrity Failures |
| **Language** | JavaScript (Node.js) |

## What goes wrong
A recursive merge copies the key `__proto__` from JSON input, which modifies `Object.prototype` for the whole application.

## Why it matters
Every object suddenly gains attacker-chosen properties such as `isAdmin: true`, leading to privilege escalation or crashes.

## The fix
Skip `__proto__`, `constructor` and `prototype` keys and copy only own properties (or use `Object.create(null)` / `structuredClone`).

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
