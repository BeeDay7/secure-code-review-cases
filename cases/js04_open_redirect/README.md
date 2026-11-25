# Open redirect after login

| | |
|---|---|
| **Weakness** | CWE-601: Open Redirect |
| **OWASP Top 10 (2021)** | A01 Broken Access Control |
| **Language** | JavaScript (Node.js) |

## What goes wrong
After login the app redirects to the `next` parameter without checking it, so a link on the real domain can send users to a phishing site.

## Why it matters
Convincing phishing links and token leakage through redirects.

## The fix
Accept only relative paths on the same site (reject `//host`, schemes and backslashes), or map `next` to an allowlist.

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
