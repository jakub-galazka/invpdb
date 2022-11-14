import random
import pandas as pd
from .generator import Generator

class RamStickGenerator(Generator):

    # Naive RAM stick data generation
    MEMORY = [2**i for i in range(1, 6)]
    RAM_STICK_TYPE = ["DDR%d" % i for i in range(1, 5)]
    CLOCK_SPEED = [200, 266, 300, 333, 400, 533, 667, 800, 1000, 800, 1066, 1333, 1600, 2400, 2666, 2933, 3000, 3200, 3600, 4000, 4400]

    def __init__(self, seed: int = None) -> None:
        super().__init__(seed)

    def generate(self, quantity: int = 1) -> None:
        ram_stick = pd.DataFrame({
            "memory": random.choices(RamStickGenerator.MEMORY, k=quantity),
            "ram_stick_type": random.choices(RamStickGenerator.RAM_STICK_TYPE, k=quantity),
            "clock_speed": random.choices(RamStickGenerator.CLOCK_SPEED, k=quantity),
            "computer_id": super().get_ids("computer", quantity)
        })
        self.csvw.write(ram_stick, "ram_stick")
