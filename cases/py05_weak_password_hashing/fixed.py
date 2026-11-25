import hashlib, hmac, os

N, R, P = 2**14, 8, 1

def hash_password(password: str) -> str:
    # Fix: random salt + memory-hard KDF.
    salt = os.urandom(16)
    dk = hashlib.scrypt(password.encode(), salt=salt, n=N, r=R, p=P)
    return f"scrypt${salt.hex()}${dk.hex()}"

def verify(password: str, stored: str) -> bool:
    _, salt_hex, dk_hex = stored.split("$")
    dk = hashlib.scrypt(password.encode(), salt=bytes.fromhex(salt_hex), n=N, r=R, p=P)
    return hmac.compare_digest(dk.hex(), dk_hex)
