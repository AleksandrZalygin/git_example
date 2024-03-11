from abc import ABC, abstractmethod

import datetime

class converter(ABC):

    @abstractmethod
    def convert(self, key: str, value: object):
        __data = {key: value}

        return __data
    


    def basic_convertor(self, key, value):
        if isinstance(value, int) or isinstance(value, float) or isinstance(value, str) or isinstance(value, bool):
            return self.convert(self, key, value)
        else:
            raise "Некорректный тип"
    
    def datetime_convertor(self):
        return self.convert(self, "datetime", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    def reference_convertor(self, key, value):
        return self.convert(self, key, value)
    
