# Server-side request forgery in a URL preview feature

| | |
|---|---|
| **Weakness** | CWE-918: Server-Side Request Forgery |
| **OWASP Top 10 (2021)** | A10 Server-Side Request Forgery |
| **Language** | Python |

## What goes wrong
The server fetches any URL a user supplies, including internal addresses such as `http://169.254.169.254/` (cloud metadata) or `http://localhost:8080/admin`.

## Why it matters
Attackers reach internal services and cloud credentials through the server.

## The fix
Allow only http(s), resolve the host, and reject private, loopback, link-local and reserved addresses (ideally also an allowlist of domains).

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
