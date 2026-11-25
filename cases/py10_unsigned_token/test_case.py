import base64, json, pytest
from . import vulnerable, fixed

KEY = b"server-side-secret"
forged = base64.urlsafe_b64encode(json.dumps({"user": "admin"}).encode()).decode() + ".deadbeef"

def test_vulnerable_accepts_forged_token():
    assert vulnerable.read_token(forged)["user"] == "admin"

def test_fixed_rejects_forged_token():
    with pytest.raises(PermissionError):
        fixed.read_token(forged, KEY)

def test_fixed_accepts_genuine_token():
    assert fixed.read_token(fixed.sign({"user": "alice"}, KEY), KEY)["user"] == "alice"
