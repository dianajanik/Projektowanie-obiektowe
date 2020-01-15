from factory.serializer.serializer_factory import SerializerFactory, Serializers
from factory.deserializer.deserializer_factory import Deserializers, DeserializerFactory

if __name__ == "__main__":

    a = {'a': 12, 'b': 13, 'c': 'Ala ma kota'}
    xml_serializer = SerializerFactory.get_serializer(Serializers.XML)
    json_serializer = SerializerFactory.get_serializer(Serializers.JSON)

    a_xml = xml_serializer.serialize(a)
    a_json = json_serializer.serialize(a)
    print("Serializing:")
    print("XML:")
    print(a_xml)

    print("JSON:")
    print(a_json)

    print("Deserializing:")

    xml_deserializer = DeserializerFactory.get_deserializer(Deserializers.XML)
    json_deserializer = DeserializerFactory.get_deserializer(Deserializers.JSON)
    dict_from_xml = xml_deserializer.deserialize(a_xml)
    dict_from_json = json_deserializer.deserialize(a_json)

    print("from XML:")
    print(dict_from_xml)

    print("from JSON:")
    print(dict_from_json)

