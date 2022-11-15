import random
import numpy as np
import pandas as pd
from .csv_writer import CSVWriter
from abc import ABC, abstractmethod

class Generator(ABC):

    NULL_RATE = .25

    def __init__(self, seed: int = None) -> None:
        self.csvw = CSVWriter()
        if not seed == None:
            random.seed(seed)

    @abstractmethod
    def generate(self, quantity: int = 1) -> None:
        pass

    def generate_list(self, quantity: int, fun, null_rate: int = None) -> list:
        if not null_rate == None:
            return ["" if random.random() < null_rate else fun() for _ in range(quantity)]
        return [fun() for _ in range(quantity)]

    def sample_df(self, df: pd.DataFrame, column_name: str, index: np.ndarray) -> list:
        return df.iloc[index][column_name].tolist()

    def get_ids(self, csv_name: str, quantity: int) -> list[int]:
        ids = pd.read_csv(self.csvw.csv_path % csv_name, usecols=[csv_name + "_id"]).squeeze().tolist()
        return random.choices(ids, k=quantity)
