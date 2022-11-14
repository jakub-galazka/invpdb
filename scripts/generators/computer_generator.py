import random
import pandas as pd
from faker import Faker
from typing import List
from .generator import Generator


class ComputerGenerator(Generator):

    ASSET_PATH = "scripts/generators/assets/computer_data.csv"
    SSD_MEMORY = [2**i for i in range(7, 13)]
    HDD_MEMORY = [1000 * i for i in range(1, 20)]

    def __init__(self, seed: int = None) -> None:
        self.faker = Faker()
        if not seed == None:
            self.faker.seed_instance(seed)
            random.seed(seed)
        
        Generator.__init__(self)

    def generate(self, quantity: int = 1):
        computer = pd.read_csv(ComputerGenerator.ASSET_PATH, sep=self.csvw.sep, usecols=["model", "manufacturer"])

        building = pd.DataFrame({
            "computer_name": self._sample_list(computer["model"].tolist(), quantity),
            "manufacturer": self._sample_list(computer["manufacturer"].tolist(), quantity),
            "ssd_memory": random.choices(ComputerGenerator.SSD_MEMORY, k=quantity),
            "hdd_memory": super()._generate_with_null(quantity, lambda: random.choice(ComputerGenerator.HDD_MEMORY)),
            "add_info": super()._generate_with_null(quantity, lambda: " ".join(self.faker.text(2000).splitlines())),
            "room_id": self._get_room_ids(quantity),
        })
        self.csvw.write(building, "computer", "computer_id")

    def _get_room_ids(self, quantity: int) -> List[str]:
        room_id = pd.read_csv(self.csvw.csv_path % "room", sep=self.csvw.sep, usecols=["room_id"]).squeeze().tolist()
        return random.choices(room_id, k=quantity)

    def _sample_list(self, list: List, quantity: int) -> List[str]:
         return random.choices(list, k=quantity)
