from abc import abstractmethod
from library.singleton import Singleton

class IDao(metaclass=Singleton):

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def read_element(self, id):
        pass

    @abstractmethod
    def save(self, storage_object):
        pass

    @abstractmethod
    def update(self, id, params):
        pass

    @abstractmethod
    def delete(self, storage_object):
        pass

