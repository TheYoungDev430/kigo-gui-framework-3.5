class SSAOSettings:
    def __init__(self, radius=0.5, bias=0.025, samples=32):
        self.radius = radius
        self.bias = bias
        self.samples = samples


def enable_ssao(*, radius=0.5, strength=1.0, blur=True):
    """
    Enable screen-space ambient occlusion in the current GL pipeline.
    """
    # Internals handled by renderer
    pass