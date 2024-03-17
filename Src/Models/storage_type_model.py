from Src.reference import reference

class storage_type_model(reference):
    def __init__(self, type):
        if type not in ['Поступление', 'Списание']:
            raise "Несуществующий тип"

        self.__type = type

    @property
    def type(self):
        return self.__type
