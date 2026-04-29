# kigo/render/dx/ssao.py
class SSAO:
    def __init__(self, radius=0.5, samples=32):
        self.radius = radius
        self.samples = samples