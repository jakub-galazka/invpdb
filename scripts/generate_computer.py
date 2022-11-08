import random
from const import CSV_PATH, SEP
import pandas as pd
from lorem_text import lorem
from typing import List


class Computer:
    def __init__(self, quantity=1):
        self.computers = pd.read_csv("assets/computer.csv")
        self.memory_ssd = [
            16,
            32,
            64,
            128,
            240,
            250,
            256,
            480,
            500,
            512,
            960,
            1000,
            1024,
            1920,
            2000,
            2048,
            3840,
            4000,
            4096,
            7680,
            8000,
        ]
        self.memory_hdd = [
            1000,
            2000,
            3000,
            4000,
            6000,
            8000,
            10_000,
            12_000,
            14_000,
            16_000,
            18_000,
            20_000,
        ]
        self._prepare_csv(quantity)

    def create_computer_name(self, quantity) -> List[str]:
        return [
            self.computers["Model Name"].sample().values[0]
            for _ in range(quantity)
        ]

    def create_manufacturer(self, quantity) -> List[str]:
        return [
            self.computers["Manufacturer"].sample().values[0]
            for _ in range(quantity)
        ]

    def create_ssd_memory(self, quantity) -> List[str]:
        return [
            ""
            if random.randint(1, 100) <= 10
            else random.choice(self.memory_ssd)
            for _ in range(quantity)
        ]

    def create_hdd_memory(self, quantity) -> List[str]:
        return [
            ""
            if random.randint(1, 100) <= 10
            else random.choice(self.memory_hdd)
            for _ in range(quantity)
        ]

    def create_add_info(self, quantity) -> List[str]:
        return [
            "" if random.randint(1, 100) <= 40 else lorem.words(150).rstrip()
            for _ in range(quantity)
        ]

    def create_room_id(self, quantity) -> List[str]:
        id = pd.read_csv(
            CSV_PATH % "room", sep=SEP, index_col="id", usecols=["id"]
        )
        return [id.sample().index.values[0] for _ in range(quantity)]

    def _prepare_csv(self, quantity):
        df = pd.DataFrame(
            {
                "computer_name": self.create_computer_name(quantity),
                "manufacturer": self.create_manufacturer(quantity),
                "ssd_memory": self.create_ssd_memory(quantity),
                "hdd_memory": self.create_hdd_memory(quantity),
                "add_info": self.create_add_info(quantity),
                "room_id": self.create_room_id(quantity),
            }
        )

        df.index.name = "id"
        df.to_csv(CSV_PATH % "computer", sep=SEP)
