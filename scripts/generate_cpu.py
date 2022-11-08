import numpy as np
import pandas as pd
from const import SEP, CSV_PATH

def generate_cpu(quantity=1):
    computer_data = pd.read_csv(CSV_PATH % "computer", sep=SEP)

    cpu_data = pd.read_csv("assets/cpu_data.csv", sep=SEP)
    els_no = cpu_data.shape[0]

    cpu_index = np.random.randint(0, els_no, quantity)

    df = pd.DataFrame({
        "cpu_name": cpu_data.iloc[cpu_index]["cpu_name"],
        "manufacturer": cpu_data.iloc[cpu_index]["manufacturer"],
        "cores_number": cpu_data.iloc[cpu_index]["cores_number"],
        "threads_number": cpu_data.iloc[cpu_index]["threads_number"],
        "min_clock_speed": cpu_data.iloc[cpu_index]["min_clock_speed"],
        "max_clock_speed": cpu_data.iloc[cpu_index]["max_clock_speed"],
        "memory": cpu_data.iloc[cpu_index]["memory"],
        "computer_id": computer_data.sample(quantity, replace=True).index.values
    })
    df = df.reset_index(drop=True)
    df.index.name = "cpu_id"
    df.to_csv(CSV_PATH % "cpu", sep=SEP)
