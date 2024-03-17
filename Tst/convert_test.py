from Src.Logics.start_factory import start_factory
from Src.Logics.convert_factory import convert_factory
from Src.Models.storage_transaction_model import storage_transaction_model
from Src.Logics.process_factory import ProcessFactory, ProcessStorageTurn

import unittest
import json

class convert_test(unittest.TestCase):
    
    #
    # Проверить формирование словаря и преобразование в json номенклатуры
    #
    def test_check_convert_nomenclature(self):
        # Подготовка
        items = start_factory.create_nomenclatures()
        factory = convert_factory()
        if len(items) == 0:
            raise Exception("Список номенклатуры пуст!")
        
        item = items[0]
        
        # Действие
        result = factory.serialize(item)
        
        # Проверки
        assert result is not None
        json_text = json.dumps(result, sort_keys = True, indent = 4)  
       
        file = open("nomenclature.json", "w")
        file.write(json_text)
        file.close()
        
    #
    # Проверить формирование словаря по списку номенклатуры и конвертацию в json
    #
    def test_check_convert_nomenctalures(self):
        # Подготовка
        items = start_factory.create_nomenclatures()
        factory = convert_factory()
        
        # Действие
        result = factory.serialize(items)
        
        # Проверки
        assert result is not None
        json_text = json.dumps(result, sort_keys = True, indent = 4)  
       
        file = open("nomenclatures.json", "w")
        file.write(json_text)
        file.close()
            
    #
    # Проверить формирование словаря по списку рецептов и конвертация в json
    #        
    def test_check_convert_receipts(self):
        # Подготовка
        items = start_factory.create_receipts()
        factory = convert_factory()
        
        # Действие
        result = factory.serialize(items)
        
        # Проверки
        assert result is not None
        json_text = json.dumps(result, sort_keys = True, indent = 4)  
       
        file = open("receipts.json", "w")
        file.write(json_text)
        file.close()





    def test_check_generate_transaction(self):
        st = storage_transaction_model(5, 'Поступление')
        result = st.generate_transactions()
        assert len(result) == 20


    def test_calculate_turns(self):
        factory = ProcessFactory()
        factory.register_process('process_storage_turn', ProcessStorageTurn)
        storage_row_model = [
            {
                'period_start': '2022-01-01',
                'period_end': '2022-01-31',
                'product_code': '123',
                'measurement_unit': 'шт',
                'warehouse': 'Склад 1',
                'transactions': [
                    {
                        'operation_type': 'Поступление',
                        'amount': 100
                    },
                    {
                        'operation_type': 'Списание',
                        'amount': 50
                    }
                ]
            }
        ]
        process = factory.create_process('process_storage_turn')
        turns = ProcessStorageTurn(storage_row_model).calculate_turns()
        self.assertEqual(turns[0]['turn'], 50)
