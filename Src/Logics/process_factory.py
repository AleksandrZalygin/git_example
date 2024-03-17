import abc
from abc import ABC, abstractmethod


class ProcessFactory(abc.ABC):
    def __init__(self):
        self.processes = {}

    def register_process(self, process_name, process_class):
        self.processes[process_name] = process_class

    def create_process(self, process_name):
        if process_name not in self.processes:
            raise ValueError(f"Process {process_name} is not registered")
        return self.processes[process_name]

class ProcessStorageTurn:
    def __init__(self, storage_row_model):
        self.storage_row_model = storage_row_model

    def calculate_turns(self):
        turns = []
        for storage_row in self.storage_row_model:
            turn = {
                'period_start': storage_row.period_start,
                'period_end': storage_row.period_end,
                'product_code': storage_row.product_code,
                'measurement_unit': storage_row.measurement_unit,
                'warehouse': storage_row.warehouse,
                'turn': 0
            }
            for transaction in storage_row.transactions:
                if transaction.operation_type == 'Поступление':
                    turn['turn'] += transaction.amount
                elif transaction.operation_type == 'Списание':
                    turn['turn'] -= transaction.amount
            turns.append(turn)
        return turns


