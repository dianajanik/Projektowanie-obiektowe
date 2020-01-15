from abc import abstractmethod


class IDeserializer:

    @abstractmethod
    def deserialize(self, string) -> object:
        pass