from . import vulnerable, fixed

def test_vulnerable_same_password_same_hash():
    assert vulnerable.hash_password("winter2026") == vulnerable.hash_password("winter2026")

def test_fixed_salted():
    assert fixed.hash_password("winter2026") != fixed.hash_password("winter2026")

def test_fixed_verifies():
    stored = fixed.hash_password("winter2026")
    assert fixed.verify("winter2026", stored)
    assert not fixed.verify("summer2026", stored)
