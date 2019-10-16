from abc import ABC, abstractmethod


class IStoregeObject(ABC):

    def __init__(self, id):
        self.id = id

    @abstractmethod
    def print_me(self):
        pass

    @staticmethod
    def update(self):
        pass


