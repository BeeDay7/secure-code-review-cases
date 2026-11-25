import ipaddress, socket
from urllib.parse import urlparse

def is_allowed(url: str, resolver=socket.getaddrinfo) -> bool:
    # Fix: scheme allowlist + reject internal address ranges after DNS resolution.
    parts = urlparse(url)
    if parts.scheme not in ("http", "https") or not parts.hostname:
        return False
    try:
        infos = resolver(parts.hostname, None)
    except OSError:
        return False
    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
            return False
    return True
