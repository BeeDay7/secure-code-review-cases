import base64, hashlib, hmac, json

def sign(claims: dict, key: bytes) -> str:
    payload = base64.urlsafe_b64encode(json.dumps(claims).encode()).decode()
    sig = hmac.new(key, payload.encode(), hashlib.sha256).hexdigest()
    return f"{payload}.{sig}"

def read_token(token: str, key: bytes) -> dict:
    payload, sig = token.split(".")
    expected = hmac.new(key, payload.encode(), hashlib.sha256).hexdigest()
    # Fix: reject the token unless the signature matches.
    if not hmac.compare_digest(sig, expected):
        raise PermissionError("bad signature")
    return json.loads(base64.urlsafe_b64decode(payload))
