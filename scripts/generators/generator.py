import random
import numpy as np
import pandas as pd
from .csv_writer import CSVWriter
from abc import ABC, abstractmethod

class Generator(ABC):

    def __init__(self, seed: int = None) -> None:
        self.csvw = CSVWriter()
        if not seed == None:
            random.seed(seed)

    @abstractmethod
    def generate(self, quantity: int = 1) -> None:
        pass

    def generate_with_null(self, quantity: int, fun) -> list[str]:
        return [
            ""
            if random.random() < .25
            else fun()
            for _ in range(quantity)
        ]

    def sample_df(self, df: pd.DataFrame, column_name: str, index: np.ndarray) -> list:
        return df.iloc[index][column_name].tolist()

    def get_ids(self, csv_name: str, quantity: int) -> list[int]:
        ids = pd.read_csv(self.csvw.csv_path % csv_name, sep=self.csvw.sep, usecols=[csv_name + "_id"]).squeeze().tolist()
        return random.choices(ids, k=quantity)
