from Src.reference import reference
from Src.Models.storage_model import storage_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_model import unit_model

import random

class storage_transaction_model(reference):
    def __init__(self, amount: int, transaction_type: str, period=0):
        self.__storage_model = storage_model("")
        self.__nomenclature = nomenclature_model
        self.__amount = amount
        self.__transaction_type = transaction_type
        self.__unit = unit_model
        self.__period = period


    def generate_transactions(self):
        transactions = []
        for _ in range(20):
            transaction = {
                'amount': self.__amount,
                'transaction_type': self.__transaction_type,
                'period': str(random.randint(1640000000, 1640000000 + 86400))
            }
            transactions.append(transaction)
        return transactions

