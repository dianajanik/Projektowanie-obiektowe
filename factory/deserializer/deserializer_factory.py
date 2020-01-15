from factory.deserializer.json_deserializer import JsonDeserializer
from factory.deserializer.xml_deserializer import XMLDeserializer


class Deserializers:
    JSON = 0,
    XML = 1


class DeserializerFactory:

    @staticmethod
    def get_deserializer(s_type):
        if s_type == Deserializers.JSON:
            return JsonDeserializer()
        elif s_type == Deserializers.XML:
            return XMLDeserializer()
        else:
            raise Exception('Not supported deserializer type: {}'.format(s_type))