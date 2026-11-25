import base64, json, pickle, pytest
from . import vulnerable, fixed

CALLED = []

def _mark():
    CALLED.append(True)
    return "ran"

class Gadget:
    def __reduce__(self):
        return (_mark, ())

def test_vulnerable_executes_code():
    CALLED.clear()
    cookie = base64.b64encode(pickle.dumps(Gadget())).decode()
    vulnerable.load_session(cookie)
    assert CALLED == [True]

def test_fixed_rejects_pickle():
    cookie = base64.b64encode(pickle.dumps(Gadget())).decode()
    with pytest.raises(Exception):
        fixed.load_session(cookie)

def test_fixed_reads_json():
    cookie = base64.b64encode(json.dumps({"user": "alice"}).encode()).decode()
    assert fixed.load_session(cookie) == {"user": "alice"}
