import base64, json

def read_token(token: str) -> dict:
    payload, _signature = token.split(".")
    # Flaw: the signature is ignored.
    return json.loads(base64.urlsafe_b64decode(payload))
