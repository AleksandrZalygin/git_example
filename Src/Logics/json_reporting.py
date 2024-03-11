import json

from Src.Logics.reporting import reporting
from Src.Logics import convert_factory
from Src.reference import reference
from Src.exceptions import operation_exception



class json_reporting(reporting):
    def create(self, typeKey: str):
        super().create(typeKey)
        result = []

        # Исходные данные
        items = self.data[typeKey]
        if items == None:
            raise operation_exception("Невозможно сформировать данные. Данные не заполнены.")

        if len(items) == 0:
            raise operation_exception("Невозможно сформировать данные. Нет данных.")

        data = {}
        for item in items:
            for field in self.fields:
                value = getattr(item, field)
                data[field] = value
            res = convert_factory(data).convert()
        data = json.dumps(result)
        return data

