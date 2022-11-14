import random
from typing import List
from .csv_writer import CSVWriter
from abc import ABC, abstractmethod

class Generator(ABC):

    def __init__(self) -> None:
        self.csvw = CSVWriter()

    @abstractmethod
    def generate(self, quantity: int = 1):
        pass

    def _generate_with_null(self, quantity: int, fun) -> List[str]:
        return [
            ""
            if random.random() < .25
            else fun()
            for _ in range(quantity)
        ]
