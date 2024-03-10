from Src.Logics.converter import converter
from Src.Logics.convert_factory import convert_factory

import unittest


class converter_test(unittest.TestCase):

    def test_check_convert_data(self):
        assert converter.convert(converter, "key", "value") == {"key": "value"}

    def test_check_basic_convert(self):
        assert converter.basic_convertor(converter, "number", 123) == {"number": 123}

    def test_check_datetime_convert(self):
        assert converter.datetime_convertor(converter)

    def test_check_reference_convert(self):
        assert converter.reference_convertor(converter, "reference_key", "reference_value") == {"reference_key": "reference_value"}



    def test_check_conver_factory(self):
        assert convert_factory(123)