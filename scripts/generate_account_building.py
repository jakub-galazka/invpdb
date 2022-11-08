from typing import List
from const import CSV_PATH, SEP
import pandas as pd


class Account_Building:
    def __init__(self, quantity):
        self._prepare_csv(quantity)

    def create_account_id(self, quantity) -> List[str]:
        id = pd.read_csv(CSV_PATH % "account", sep=SEP, usecols=["id"])
        return id.sample(quantity, replace=True).index.values

    def create_building_id(self, quantity) -> List[str]:
        id = pd.read_csv(CSV_PATH % "building", sep=SEP, usecols=["id"])
        return id.sample(quantity, replace=True).index.values

    def _prepare_csv(self, quantity):
        df = pd.DataFrame(
            {
                "account_id": self.create_account_id(quantity),
                "building_id": self.create_building_id(quantity),
            }
        )
        df.to_csv(CSV_PATH % "account_building", index=False, sep=SEP)
