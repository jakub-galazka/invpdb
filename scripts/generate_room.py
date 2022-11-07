import random
import string
from const import CSV_PATH, SEP
from typing import List
import pandas as pd


class Room:
    def __init__(self, quantity=1):
        self._prepare_csv(quantity)

    def create_room_number(self, quantity) -> List[str]:
        return [
            "".join(
                random.choices(string.digits, k=random.randrange(1, 4))
                + random.choices(
                    string.ascii_lowercase, k=random.randrange(0, 2)
                )
            )
            for _ in range(quantity)
        ]

    def create_room_name(self, quantity) -> List[str]:
        df = pd.read_csv("assets/animals_data.csv")

        animals = []
        for _ in range(quantity):
            animal = str(df.sample().values[0][0])
            if animal not in animals:
                animals.append(animal)
            else:
                new_animal = animal + "".join(
                    random.choices(
                        string.ascii_lowercase,
                        k=random.randrange(2, 10),
                    )
                )
                animals.append(new_animal)
        return animals

    def create_floors(self, quantity) -> List[str]:
        return [random.randint(0, 3) for _ in range(quantity)]

    def create_building_id(self, quantity) -> List[str]:
        id = pd.read_csv(
            CSV_PATH % "building", sep=SEP, index_col="id", usecols=["id"]
        )
        return [id.sample().index.values[0] for _ in range(quantity)]

    def _prepare_csv(self, quantity):
        df = pd.DataFrame(
            {
                "room_number": self.create_room_number(quantity),
                "room_name": self.create_room_name(quantity),
                "floor": self.create_floors(quantity),
                "building_id": self.create_building_id(quantity),
            }
        )
        df.index.name = "id"
        df.to_csv(CSV_PATH % "room", sep=SEP)
