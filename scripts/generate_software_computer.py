from typing import List
from const import CSV_PATH, SEP
import pandas as pd


class Software_Computer:
    def __init__(self, quantity):
        self._prepare_csv(quantity)

    def create_software_id(self, quantity) -> List[str]:
        id = pd.read_csv(CSV_PATH % "software", sep=SEP, usecols=["id"])
        return id.sample(quantity, replace=True).index.values

    def create_computer_id(self, quantity) -> List[str]:
        id = pd.read_csv(CSV_PATH % "computer", sep=SEP, usecols=["id"])
        return id.sample(quantity, replace=True).index.values

    def _prepare_csv(self, quantity):
        df = pd.DataFrame(
            {
                "software_id": self.create_software_id(quantity),
                "computer_id": self.create_computer_id(quantity),
            }
        )
        df.to_csv(CSV_PATH % "software_computer", index=False, sep=SEP)
