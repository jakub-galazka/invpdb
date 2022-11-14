import random
import numpy as np
import pandas as pd
from .generator import Generator

class GPUGenerator(Generator):

    ASSET_PATH = "scripts/generators/assets/gpu_data.csv"
    TGP = [35, 40, 60, 75, 80, 90, 100, 115, 125, 130]

    def __init__(self, seed: int = None) -> None:
        super().__init__(seed)
        if not seed == None:
            np.random.seed(seed)

    def generate(self, quantity: int = 1) -> None:
        gpu_data = pd.read_csv(GPUGenerator.ASSET_PATH, sep=self.csvw.sep)

        els_no = gpu_data.shape[0]
        index = np.random.randint(0, els_no, quantity)

        gpu = pd.DataFrame({
            "gpu_name": super().sample_df(gpu_data, "gpu_name", index),
            "manufacturer": super().sample_df(gpu_data, "manufacturer", index),
            "memory": super().sample_df(gpu_data, "memory", index),
            "tgp": super().generate_list(quantity, lambda: random.choice(GPUGenerator.TGP), True),
            "computer_id": super().get_ids("computer", quantity)
        })
        self.csvw.write(gpu, "gpu")
