import random
import pandas as pd
from .generator import Generator

class RamStickGenerator(Generator):

    MEMORY = [2**i for i in range(1, 6)]
    RAM_STICKS = {
        "DDR1": [200, 266, 300, 333, 400],
        "DDR2": [400, 533, 667, 800, 1000],
        "DDR3": [800, 1066, 1333, 1600],
        "DDR4": [2400, 2666, 2933, 3000, 3200, 3600, 4000, 4400]
    }

    def __init__(self, seed: int = None) -> None:
        super().__init__(seed)

    def generate(self, quantity: int = 1) -> None:
        ram_stick_types = random.choices(list(RamStickGenerator.RAM_STICKS.keys()), k=quantity)
        ram_stick = pd.DataFrame({
            "memory": random.choices(RamStickGenerator.MEMORY, k=quantity),
            "ram_stick_type": ram_stick_types,
            "clock_speed": self._generate_clock_speeds(ram_stick_types),
            "computer_id": super().get_ids("computer", quantity)
        })
        self.csvw.write(ram_stick, "ram_stick")

    def _generate_clock_speeds(self, ram_stick_types: list[str]) -> list[int]:
        clock_speeds = []
        for rst in ram_stick_types:
            sw_len = len(RamStickGenerator.RAM_STICKS[rst])
            i = random.randint(0, sw_len - 1)
            clock_speeds.append(RamStickGenerator.RAM_STICKS[rst][i])
        return clock_speeds
