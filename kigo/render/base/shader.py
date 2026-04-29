# kigo/render/base/shader.py
from pathlib import Path

def load_shader(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")