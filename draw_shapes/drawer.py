
from abc import ABC, abstractmethod


class Drawer(ABC):
    pass


class PixelsDrawer(Drawer):

    def __init__(self):
        self.name = "Pixels draw_shapes"


class VectorDrawer(Drawer):

    def __init__(self):
        self.name = "Vector draw_shapes"


class DrawersProvider:

    def __init__(self):
        self.drawers = {"pixel": PixelsDrawer(), "vector": VectorDrawer()}
