import pytest
from . import vulnerable, fixed

PAYLOAD = "example.com; echo injected"

def test_vulnerable_command_contains_second_command():
    assert "; echo injected" in vulnerable.build_ping(PAYLOAD)

def test_fixed_rejects_payload():
    with pytest.raises(ValueError):
        fixed.build_ping(PAYLOAD)

def test_fixed_accepts_valid_host():
    assert fixed.build_ping("example.com") == ["ping", "-c", "1", "example.com"]
