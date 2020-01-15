from abc import abstractmethod


class ISerializer:

    @abstractmethod
    def serialize(self, obj) -> str:
        pass