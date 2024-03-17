from Src.reference import reference
from Src.Models.storage_model import storage_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_model import unit_model

class storage_model(reference):
    def __init__(self, turnover: int):
        self.__storage_model = storage_model("")
        self.__nomenclature = nomenclature_model
        self.__turnover = turnover
        self.__unit = unit_model

