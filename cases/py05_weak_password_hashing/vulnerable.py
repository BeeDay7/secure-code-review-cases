import hashlib

def hash_password(password: str) -> str:
    # Flaw: fast, unsalted hash.
    return hashlib.md5(password.encode()).hexdigest()

def verify(password: str, stored: str) -> bool:
    return hash_password(password) == stored
