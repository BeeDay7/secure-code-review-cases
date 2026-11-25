# OS command injection in a ping helper

| | |
|---|---|
| **Weakness** | CWE-78: OS Command Injection |
| **OWASP Top 10 (2021)** | A03 Injection |
| **Language** | Python |

## What goes wrong
The host name is placed into a shell command run with `shell=True`, so characters such as `;` start a second command.

## Why it matters
An attacker can run arbitrary commands on the server with the application's privileges.

## The fix
Validate the input against a strict pattern and pass arguments as a list without a shell.

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
