from abc import ABC
from copy import deepcopy


class RobotBase(ABC):

    def __init__(self, module):
        self.module = module

    def clone(self):
        return deepcopy(self)

    def produce(self):
        return self.module

