import os

TRANSACTIONS_DIR = os.path.join("workload", "transactions")
INDEXES_DIR = os.path.join("workload", "indexes")
EXPERIMENTS_DIR = os.path.join("workload", "experiments")

def makedir(dirpath: str) -> str:
    if len(os.path.split(dirpath)) > 1:
        directory = os.path.dirname(dirpath)
    else:
        directory = dirpath
    os.makedirs(directory, exist_ok=True)
    return dirpath
