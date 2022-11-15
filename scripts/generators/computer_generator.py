import random
import numpy as np
import pandas as pd
from faker import Faker
from .generator import Generator

class ComputerGenerator(Generator):

    ASSET_PATH = "scripts/generators/assets/computer_data.csv"
    SSD_MEMORY = [2**i for i in range(7, 14)]
    HDD_MEMORY = [1000 * i for i in range(1, 21)]

    def __init__(self, seed: int = None) -> None:
        super().__init__(seed)
        self.faker = Faker()
        if not seed == None:
            self.faker.seed_instance(seed)
            np.random.seed(seed)

    def generate(self, quantity: int = 1) -> None:
        computer_data = pd.read_csv(ComputerGenerator.ASSET_PATH, usecols=["model", "manufacturer"])

        els_no = computer_data.shape[0]
        index = np.random.randint(0, els_no, quantity)

        computer = pd.DataFrame({
            "computer_name": super().sample_df(computer_data, "model", index),
            "manufacturer": super().sample_df(computer_data, "manufacturer", index),
            "ssd_memory": random.choices(ComputerGenerator.SSD_MEMORY, k=quantity),
            "hdd_memory": super().generate_list(quantity, lambda: random.choice(ComputerGenerator.HDD_MEMORY), Generator.NULL_RATE),
            "add_info": super().generate_list(quantity, lambda: " ".join(self.faker.text(2000).splitlines()), Generator.NULL_RATE),
            "room_id": super().get_ids("room", quantity),
        })
        self.csvw.write(computer, "computer")
