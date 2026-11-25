# Cross-site scripting in a comment renderer

| | |
|---|---|
| **Weakness** | CWE-79: Cross-site Scripting |
| **OWASP Top 10 (2021)** | A03 Injection |
| **Language** | JavaScript (Node.js) |

## What goes wrong
User comments are inserted into HTML without encoding, so a comment containing `<script>` or an `onerror` attribute runs in other users' browsers.

## Why it matters
Session theft, actions performed as the victim, defacement.

## The fix
HTML-encode untrusted text before inserting it (or use a templating engine that escapes by default), plus a Content Security Policy.

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
