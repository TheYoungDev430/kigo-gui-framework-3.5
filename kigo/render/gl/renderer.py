# kigo/render/gl/renderer.py
from kigo.render.base.renderer import BaseRenderer

class GLRenderer(BaseRenderer):
    def initialize(self):
        print("OpenGL renderer initialized")

    def draw(self):
        pass

    def enable_ssao(self):
        from kigo.render.gl.ssao import SSAO
        self.ssao = SSAO()