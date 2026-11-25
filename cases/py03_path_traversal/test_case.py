import pytest
from pathlib import Path
from . import vulnerable, fixed

def test_vulnerable_escapes(tmp_path):
    base = tmp_path / "uploads"; base.mkdir()
    (tmp_path / "secret.txt").write_text("key")
    assert vulnerable.resolve(base, "../secret.txt").read_text() == "key"

def test_fixed_blocks_escape(tmp_path):
    base = tmp_path / "uploads"; base.mkdir()
    with pytest.raises(PermissionError):
        fixed.resolve(base, "../secret.txt")

def test_fixed_allows_normal_file(tmp_path):
    base = tmp_path / "uploads"; base.mkdir()
    (base / "report.pdf").write_text("ok")
    assert fixed.resolve(base, "report.pdf").read_text() == "ok"
