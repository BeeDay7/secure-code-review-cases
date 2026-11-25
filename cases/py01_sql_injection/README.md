# SQL injection in a login query

| | |
|---|---|
| **Weakness** | CWE-89: SQL Injection |
| **OWASP Top 10 (2021)** | A03 Injection |
| **Language** | Python |

## What goes wrong
The query is built by pasting user input into the SQL string, so input such as `' OR '1'='1` changes the meaning of the query.

## Why it matters
An attacker can log in without a password, read other users' data or modify the database.

## The fix
Use parameterised queries (`?` placeholders). The database driver treats the input strictly as data.

## Files
- `vulnerable.*`: the flawed version, kept only for review and teaching.
- `fixed.*`: the corrected version.
- `test_*`: tests showing that the flaw is reachable in the vulnerable version and closed in the fixed one.
