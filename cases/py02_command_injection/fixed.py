import re

_HOST = re.compile(r"^(?=.{1,253}$)[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?$")

def build_ping(host: str) -> list[str]:
    # Fix: strict validation, and an argument list for subprocess.run(..., shell=False).
    if not _HOST.match(host):
        raise ValueError("invalid host name")
    return ["ping", "-c", "1", host]
