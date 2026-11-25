def build_ping(host: str) -> str:
    # Flaw: the string is later run with shell=True; ';' or '&&' chain extra commands.
    return f"ping -c 1 {host}"
