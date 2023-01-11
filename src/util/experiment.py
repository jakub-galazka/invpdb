import os
import pandas as pd
from .file_explorer import makedir

def save_experiment(filepath: str, experiment: dict) -> None:
    experiment_dir = makedir(filepath)

    data = {}
    for k, v in experiment.items():
        data[k] = v[0]
        with open(makedir(os.path.join(experiment_dir, "query_plans", f"{k}.txt")), "w") as f:
            f.write(v[1])

    df = pd.DataFrame(data)
    df.loc["min"] = df.min()
    df.loc["max"] = df.max()
    df.loc["avg"] = df.mean()
    df.to_csv(os.path.join(experiment_dir, "report.csv"))
