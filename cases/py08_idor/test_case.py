import pytest
from . import vulnerable, fixed

def test_vulnerable_leaks_other_users_invoice():
    assert vulnerable.get_invoice("alice", 2)["owner"] == "bob"

def test_fixed_blocks_other_users_invoice():
    with pytest.raises(fixed.NotFound):
        fixed.get_invoice("alice", 2)

def test_fixed_returns_own_invoice():
    assert fixed.get_invoice("alice", 1)["total"] == 120
