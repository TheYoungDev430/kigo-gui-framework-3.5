# kigo/render/base/renderer.py
from abc import ABC, abstractmethod

class BaseRenderer(ABC):
    def __init__(self, qt_window):
        self.window = qt_window

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def enable_ssao(self):
        pass