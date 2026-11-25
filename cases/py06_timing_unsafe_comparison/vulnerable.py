def check_key(supplied: str, expected: str) -> bool:
    # Flaw: early-exit comparison.
    return supplied == expected
