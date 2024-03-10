from Src.Logics.reporting import reporting
from Src.Logics.markdown_reporting import markdown_reporting
from Src.Logics.csv_reporting import csv_reporting
from Src.exceptions import exception_proxy, argument_exception, operation_exception

# Фабрика для отчетов
class report_factory:
    _maps = {}

    def __init__(self):
        self.__build_structure()

    def __build_structure(self):
        # Сформировать структуру
        self._maps["csv"] = csv_reporting
        self._maps["markdown"] = markdown_reporting

    def create(self, format: str, data) -> reporting:
        exception_proxy.validate(format, str)
        if data is None:
            raise argument_exception("Данные не переданы")

        if len(data) == 0:
            raise argument_exception("Данные пустые")

        if format not in self._maps.keys():
            raise operation_exception(f"Для {format} нет обработчика")

        report_type = self._maps[format]



