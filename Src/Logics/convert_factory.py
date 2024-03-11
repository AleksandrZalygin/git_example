from Src.Logics.converter import converter
from Src.exceptions import operation_exception
from Src.reference import reference, exception_proxy

import datetime


class convert_factory(converter):
    __maps = {}

    def __init__(self):
        self.__maps[int] = converter.basic_convertor
        self.__maps[float] = converter.basic_convertor
        self.__maps[bool] = converter.basic_convertor
        self.__maps[datetime] = converter.datetime_convertor

        for inheritor in reference.__subclasses__():
            self.__maps[inheritor] = converter.reference_convertor


    def convert(self, obj):
        result = self._convert_list("data", obj)


        result = {}
        fields = reference.create_fields(obj)

        for field in fields:
            attribute = getattr(obj.__class__, field)
            if isinstance(attribute, property):
                value = getattr(obj, field)

                dictionary = self._convert_list(field, value)
                if dictionary is None:
                    dictionary = self._convert_item(field, value)

                result[field] = dictionary[field] if len(dictionary) == 1 else dictionary

        return result

    def _convert_item(self, field: str, source):
        exception_proxy.validate(field, str)
        if source is None:
            return {field: None}

        source_type = type(source)
        if source_type not in self.__maps:
            raise operation_exception(f"Unable to find converter for type {source_type}")

        converter1 = self.__maps[source_type]
        converter2 = converter
        dictionary = converter.convert(converter1, field, source)



        return dictionary

    def _convert_list(self, field: str, source):
        exception_proxy.validate(field, str)
        if not isinstance(source, list):
            return None

        return [self._convert_item(field, item) for item in source]



