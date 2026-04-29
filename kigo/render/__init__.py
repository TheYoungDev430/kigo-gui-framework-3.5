# kigo/render/__init__.py
from kigo.render.select import select_backend

_backend = select_backend()

if _backend == "dx":
    from kigo.render.dx.renderer import DXRenderer as Renderer
else:
    from kigo.render.gl.renderer import GLRenderer as Renderer

__all__ = ["Renderer"]