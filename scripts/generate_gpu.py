import numpy as np
import pandas as pd
from const import SEP, CSV_PATH


TGP = [i for i in range(4, 22)]
TGP.append("") # null
TGP = np.array(TGP)

def generate_gpu(quantity=1):
    gpu_data = pd.read_csv("assets/gpu_data.csv", sep=SEP)
    els_no = gpu_data.shape[0]

    gpu_index = np.random.randint(0, els_no, quantity)
    tgp_index = np.random.randint(0, len(TGP), quantity)

    df = pd.DataFrame({
        "gpu_name": gpu_data.iloc[gpu_index]["gpu_name"],
        "manufacturer": gpu_data.iloc[gpu_index]["manufacturer"],
        "memory": gpu_data.iloc[gpu_index]["memory"],
        "tgp": TGP[tgp_index]
    })
    df = df.reset_index(drop=True)
    df.index.name = "gpu_id"
    df.to_csv(CSV_PATH % "gpu", sep=SEP)
