# kigo/render/dx/renderer.py
from kigo.render.base.renderer import BaseRenderer

class DXRenderer(BaseRenderer):
    def initialize(self):
        print("DirectX renderer initialized")

    def draw(self):
        pass

    def enable_ssao(self):
        from kigo.render.dx.ssao import SSAO
        self.ssao = SSAO()