# kigo/render/select.py
import sys

def select_backend():
    if sys.platform.startswith("win"):
        return "dx"
    return "gl"