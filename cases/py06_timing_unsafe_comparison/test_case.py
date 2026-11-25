import inspect
from . import vulnerable, fixed

def test_both_accept_correct_key():
    assert vulnerable.check_key("k-123", "k-123") and fixed.check_key("k-123", "k-123")

def test_both_reject_wrong_key():
    assert not vulnerable.check_key("k-124", "k-123") and not fixed.check_key("k-124", "k-123")

def test_fixed_uses_constant_time_compare():
    assert "compare_digest" in inspect.getsource(fixed.check_key)
