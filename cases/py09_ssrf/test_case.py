from . import vulnerable, fixed

def fake_resolver(host, port):
    table = {"internal.example": "10.0.0.5", "metadata": "169.254.169.254", "news.example": "93.184.216.34"}
    return [(None, None, None, None, (table.get(host, host), 0))]

def test_vulnerable_allows_metadata():
    assert vulnerable.is_allowed("http://169.254.169.254/latest/meta-data/")

def test_fixed_blocks_internal_targets():
    for url in ["http://169.254.169.254/", "http://127.0.0.1/admin", "http://internal.example/", "file:///etc/passwd"]:
        assert not fixed.is_allowed(url, resolver=fake_resolver)

def test_fixed_allows_public_site():
    assert fixed.is_allowed("https://news.example/article", resolver=fake_resolver)
