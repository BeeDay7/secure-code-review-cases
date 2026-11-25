import base64, json

def load_session(cookie: str) -> dict:
    # Fix: JSON carries data only; validate the shape.
    data = json.loads(base64.b64decode(cookie))
    if not isinstance(data, dict) or not isinstance(data.get("user"), str):
        raise ValueError("invalid session")
    return {"user": data["user"]}
