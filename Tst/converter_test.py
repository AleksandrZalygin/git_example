from Src.Logics.converter import converter
from Src.Logics.convert_factory import convert_factory

import unittest
import datetime


class converter_test(unittest.TestCase):
    def test_convert_list(self):
        convert1 = convert_factory()
        result = convert1.convert([1, 2, 3])
        self.assertNotEqual(result, [{"data": 1}, {"data": 2}, {"data": 3}])