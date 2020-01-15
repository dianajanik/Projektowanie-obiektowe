from factory.serializer.json_serializer import JsonSerializer
from factory.serializer.xml_serializer import XmlSerializer


class Serializers:
    JSON = 0,
    XML = 1


class SerializerFactory:

    @staticmethod
    def get_serializer(s_type):
        if s_type == Serializers.JSON:
            return JsonSerializer()
        elif s_type == Serializers.XML:
            return XmlSerializer()
        else:
            raise Exception('Not suported serializer type: {}'.format(s_type))
