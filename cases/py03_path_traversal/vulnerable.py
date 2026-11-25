from pathlib import Path

def resolve(base: Path, name: str) -> Path:
    # Flaw: no check that the result stays inside base.
    return base / name
