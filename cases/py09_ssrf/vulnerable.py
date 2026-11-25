from urllib.parse import urlparse

def is_allowed(url: str) -> bool:
    # Flaw: only checks that a host is present.
    return bool(urlparse(url).hostname)
