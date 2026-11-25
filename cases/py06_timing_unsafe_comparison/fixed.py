import hmac

def check_key(supplied: str, expected: str) -> bool:
    # Fix: constant-time comparison.
    return hmac.compare_digest(supplied.encode(), expected.encode())
