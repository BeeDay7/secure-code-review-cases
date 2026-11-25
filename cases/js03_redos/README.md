# Regular-expression denial of service in an email check

| | |
|---|---|
| **Weakness** | CWE-1333: Inefficient Regular Expression Complexity |
| **OWASP Top 10 (2021)** | No direct Top 10 category (availability: denial of service) |
| **Language** | JavaScript (Node.js) |

## What goes wrong
The pattern `^([a-zA-Z0-9]+)*@` has nested quantifiers. A long string that almost matches makes the engine backtrack exponentially.

## Why it matters
One request can block the Node.js event loop for seconds or minutes, taking the service down.

## The fix
Use a linear pattern without nested quantifiers, and cap the input length before matching.

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
