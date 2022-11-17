import numpy as np
import pandas as pd
from .generator import Generator


class CPUGenerator(Generator):

    ASSET_PATH = "scripts/generators/assets/cpu_data.csv"

    def __init__(self, seed: int = None) -> None:
        super().__init__(seed)
        if seed is not None:
            np.random.seed(seed)

    def generate(self, quantity: int = 1) -> None:
        cpu_data = pd.read_csv(CPUGenerator.ASSET_PATH)

        els_no = cpu_data.shape[0]
        index = np.random.randint(0, els_no, quantity)

        cpu = pd.DataFrame(
            {
                "cpu_name": super().sample_df(cpu_data, "cpu_name", index),
                "manufacturer": super().sample_df(
                    cpu_data, "manufacturer", index
                ),
                "cores_number": super().sample_df(
                    cpu_data, "cores_number", index
                ),
                "threads_number": super().sample_df(
                    cpu_data, "threads_number", index
                ),
                "min_clock_speed": super().sample_df(
                    cpu_data, "min_clock_speed", index
                ),
                "max_clock_speed": super().sample_df(
                    cpu_data, "max_clock_speed", index
                ),
                "memory": super().sample_df(cpu_data, "memory", index),
                "computer_id": super().get_ids("computer", quantity),
            }
        )
        self.csvw.write(cpu, "cpu")
