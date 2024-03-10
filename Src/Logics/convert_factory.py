from Src.Logics.converter import converter


class convert_factory(converter):
    def __init__(self, obj):
        self.obj = obj


    def convert(self):
        result = {}
        result.update(converter.basic_convertor(converter, self.obj))
        result.update(converter.datetime_convertor(converter))
        result.update(converter.reference_convertor(converter, self.obj))
        return result

