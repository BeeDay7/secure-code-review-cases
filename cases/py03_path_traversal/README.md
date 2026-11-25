# Path traversal in a file download endpoint

| | |
|---|---|
| **Weakness** | CWE-22: Path Traversal |
| **OWASP Top 10 (2021)** | A01 Broken Access Control |
| **Language** | Python |

## What goes wrong
The requested file name is joined to the upload folder without checking the result, so `../` escapes the folder.

## Why it matters
An attacker can read configuration files, keys or other users' files.

## The fix
Resolve the final path and check that it stays inside the allowed base directory.

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
