import random
import string
import pandas as pd
from .generator import Generator

class RoomGenerator(Generator):

    ASSET_PATH = "scripts/generators/assets/animal_data.csv"
    
    def __init__(self, seed: int = None) -> None:
        super().__init__(seed)

    def generate(self, quantity: int = 1) -> None:
        room = pd.DataFrame({
            "room_number": self._generate_room_numbers(quantity),
            "room_name": self.create_room_name(quantity),
            "floor": self._generate_floors(quantity),
            "building_id": super().get_ids("building", quantity),
        })
        self.csvw.write(room, "room")

    def _generate_room_numbers(self, quantity: int) -> list[str]:
        return [
            "".join(random.choices(string.digits, k=random.randrange(1, 4)))
            + random.choice(string.ascii_uppercase)
            for _ in range(quantity)
        ]

    def create_room_name(self, quantity: int) -> list[str]:
        animals = pd.read_csv(RoomGenerator.ASSET_PATH).squeeze().tolist()
        return random.choices(animals, k=quantity)

    def _generate_floors(self, quantity: int) -> list[str]:
        return [random.randint(1, 5) for _ in range(quantity)]
