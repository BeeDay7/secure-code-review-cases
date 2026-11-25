import sqlite3, pytest
from . import vulnerable, fixed

@pytest.fixture
def conn():
    c = sqlite3.connect(":memory:")
    c.execute("CREATE TABLE users (name TEXT, password TEXT)")
    c.execute("INSERT INTO users VALUES ('alice', 's3cret')")
    return c

PAYLOAD = "' OR '1'='1"

def test_vulnerable_allows_bypass(conn):
    assert vulnerable.login(conn, "alice", PAYLOAD) is True

def test_fixed_blocks_bypass(conn):
    assert fixed.login(conn, "alice", PAYLOAD) is False

def test_fixed_still_works(conn):
    assert fixed.login(conn, "alice", "s3cret") is True
