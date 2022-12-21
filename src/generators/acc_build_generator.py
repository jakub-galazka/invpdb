import pandas as pd
from .generator import Generator


class AccBuildGenerator(Generator):
    def __init__(self, seed: int = None) -> None:
        super().__init__(seed)

    def generate(self, quantity: int = 1) -> None:
        acc_build = pd.DataFrame(
            {
                "account_id": super().get_ids("account", quantity),
                "building_id": super().get_ids("building", quantity),
            }
        )
        self.csvw.write(acc_build, "acc_build", False)
