from factory.deserializer.i_deserializer import IDeserializer
import json


class JsonDeserializer(IDeserializer):
    def deserialize(self, json_string) -> object:
        json_string = u'{}'.format(json_string)
        obj = json.loads(json_string)
        return obj

