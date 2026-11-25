from pathlib import Path

def resolve(base: Path, name: str) -> Path:
    # Fix: resolve symlinks and '..', then require the result to stay inside base.
    base = base.resolve()
    target = (base / name).resolve()
    if not target.is_relative_to(base):
        raise PermissionError("path escapes the upload folder")
    return target
