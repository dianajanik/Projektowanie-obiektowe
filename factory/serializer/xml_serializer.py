from factory.serializer.i_serializer import ISerializer
from dicttoxml import dicttoxml


class XmlSerializer(ISerializer):
    def serialize(self, obj) -> str:
        obj = obj.__dict__ if not isinstance(obj, dict) else obj
        return dicttoxml(obj)
