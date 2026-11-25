# Secure Code Review Cases

![tests](https://github.com/BeeDay7/secure-code-review-cases/actions/workflows/tests.yml/badge.svg)

A set of short, realistic code-review cases. Each case pairs a **vulnerable** snippet with a **fixed** version, explains the weakness (CWE and OWASP Top 10 category), and includes **automated tests** that show the flaw is reachable in the vulnerable code and closed in the fix.

I built it to practise and demonstrate secure code review across languages, the kind of analysis used in application-security work and in training and evaluating AI coding assistants.

## Cases

| # | Case | Weakness | OWASP Top 10 (2021) | Language |
|---|---|---|---|---|
| 1 | [SQL injection in a login query](cases/py01_sql_injection/) | CWE-89: SQL Injection | A03 Injection | Python |
| 2 | [OS command injection in a ping helper](cases/py02_command_injection/) | CWE-78: OS Command Injection | A03 Injection | Python |
| 3 | [Path traversal in a file download endpoint](cases/py03_path_traversal/) | CWE-22: Path Traversal | A01 Broken Access Control | Python |
| 4 | [Insecure deserialisation of a session cookie](cases/py04_insecure_deserialization/) | CWE-502: Deserialization of Untrusted Data | A08 Software and Data Integrity Failures | Python |
| 5 | [Fast, unsalted password hashing](cases/py05_weak_password_hashing/) | CWE-916: Use of Password Hash With Insufficient Computational Effort | A02 Cryptographic Failures | Python |
| 6 | [Timing-unsafe comparison of an API key](cases/py06_timing_unsafe_comparison/) | CWE-208: Observable Timing Discrepancy | A02 Cryptographic Failures | Python |
| 7 | [Predictable password-reset tokens](cases/py07_insecure_randomness/) | CWE-338: Use of Cryptographically Weak PRNG | A02 Cryptographic Failures | Python |
| 8 | [Insecure direct object reference in an invoice API](cases/py08_idor/) | CWE-639: Authorization Bypass Through User-Controlled Key | A01 Broken Access Control | Python |
| 9 | [Server-side request forgery in a URL preview feature](cases/py09_ssrf/) | CWE-918: Server-Side Request Forgery | A10 Server-Side Request Forgery | Python |
| 10 | [Session token accepted without signature check](cases/py10_unsigned_token/) | CWE-347: Improper Verification of Cryptographic Signature | A07 Identification and Authentication Failures | Python |
| 11 | [Cross-site scripting in a comment renderer](cases/js01_xss/) | CWE-79: Cross-site Scripting | A03 Injection | JavaScript (Node.js) |
| 12 | [Prototype pollution in a deep-merge helper](cases/js02_prototype_pollution/) | CWE-1321: Prototype Pollution | A08 Software and Data Integrity Failures | JavaScript (Node.js) |
| 13 | [Regular-expression denial of service in an email check](cases/js03_redos/) | CWE-1333: Inefficient Regular Expression Complexity | No direct Top 10 category (availability: denial of service) | JavaScript (Node.js) |
| 14 | [Open redirect after login](cases/js04_open_redirect/) | CWE-601: Open Redirect | A01 Broken Access Control | JavaScript (Node.js) |

## How each case is organised

```
cases/<id>/
  README.md        what goes wrong, why it matters, the fix
  vulnerable.*     flawed version (for review only)
  fixed.*          corrected version
  test_*           tests for both versions
```

## Run the tests

```bash
# Python cases
pip install pytest
pytest -q

# JavaScript cases (Node.js 18+)
node --test "cases/**/*.test.js"
```

Both suites also run on every push through GitHub Actions.

## Scope and responsible use

This repository is defensive and educational. The vulnerable snippets are minimal and use harmless demonstration inputs; they are not tools for attacking real systems. Never deploy the `vulnerable` versions.

## References

- [MITRE CWE](https://cwe.mitre.org/)
- [OWASP Top 10 (2021)](https://owasp.org/Top10/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)

## Author

**Abidemi Kuburat Adedeji**, AI security and application security; PhD candidate in Cybersecurity & AI.
[LinkedIn](https://www.linkedin.com/in/beeday7) · [ORCID](https://orcid.org/0009-0005-8760-8565)

## License

MIT
