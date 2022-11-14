import random
import string
import pandas as pd
from typing import List
from .generator import Generator


class RoomGenerator(Generator):

    ASSET_PATH = "scripts/generators/assets/animal_data.csv"
    
    def __init__(self, seed: int = None) -> None:
        if not seed == None:
            random.seed(seed)
        
        Generator.__init__(self)

    def generate(self, quantity: int = 1) -> None:
        room = pd.DataFrame({
            "room_number": self._generate_room_numbers(quantity),
            "room_name": self.create_room_name(quantity),
            "floor": self._generate_floors(quantity),
            "building_id": self._get_building_ids(quantity),
        })
        self.csvw.write(room, "room", "room_id")

    def _generate_room_numbers(self, quantity: int) -> List[str]:
        return [
            "".join(random.choices(string.digits, k=random.randrange(1, 4)))
            + random.choice(string.ascii_uppercase)
            for _ in range(quantity)
        ]

    def create_room_name(self, quantity: int) -> List[str]:
        animals = pd.read_csv(RoomGenerator.ASSET_PATH).squeeze().tolist()
        return random.choices(animals, k=quantity)

    def _generate_floors(self, quantity: int) -> List[str]:
        return [random.randint(1, 5) for _ in range(quantity)]

    def _get_building_ids(self, quantity: int) -> List[str]:
        building_id = pd.read_csv(self.csvw.csv_path % "building", sep=self.csvw.sep, usecols=["building_id"]).squeeze().tolist()
        return random.choices(building_id, k=quantity)
