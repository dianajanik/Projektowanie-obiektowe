from factory.serializer.i_serializer import ISerializer
import json


class JsonSerializer(ISerializer):
    def serialize(self, obj) -> str:
        obj = obj.__dict__ if not isinstance(obj, dict) else obj
        return json.dumps(obj)

