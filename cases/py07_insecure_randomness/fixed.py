import secrets

def reset_token() -> str:
    # Fix: CSPRNG, 256 bits of entropy.
    return secrets.token_urlsafe(32)
