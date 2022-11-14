from .csv_writer import CSVWriter
from abc import ABC, abstractmethod

class Generator(ABC):

    def __init__(self) -> None:
        self.csvw = CSVWriter()

    @abstractmethod
    def generate(self, quantity: int = 1):
        pass
