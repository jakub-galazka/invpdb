import pandas as pd
from .generator import Generator

class SoftCompGenerator(Generator):

    def __init__(self, seed: int = None) -> None:
        super().__init__(seed)

    def generate(self, quantity: int = 1) -> None:
        soft_comp = pd.DataFrame({
            "software_id": super().get_ids("software", quantity),
            "computer_id": super().get_ids("computer", quantity),
        })
        self.csvw.write(soft_comp, "soft_comp")
