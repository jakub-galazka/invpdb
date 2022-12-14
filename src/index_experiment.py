import os
import pandas as pd
from util.dbutils import *
from dotenv import load_dotenv
from util.file_explorer import makedir
from util.experiment import save_experiment
from util.file_explorer import TRANSACTIONS_DIR, EXPERIMENTS_DIR

# Database connection params
load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

ITERATIONS = 10

def main():
    conn = open_connection(DB_USER, DB_PASS, DB_NAME)
    cur = conn.cursor()

    # Experiments
    transaction_names = ["1_select", "2_select", "5_delete"]
    for name in transaction_names:
        print(f"\n_________________________ {name} _________________________\n")
        do_experiment(cur, name)

def do_experiment(cur, transaction_name: str) -> None:
    transaction = read_sql(os.path.join(TRANSACTIONS_DIR, f"{transaction_name}.sql"))
    experiment = {}

    # Before index
    print("START before")
    experiment["before"] = test_transaction(cur, transaction, ITERATIONS)
    print("END")

    # After index
    indexes_dir = os.path.join("workload", "indexes", transaction_name)
    for index_file in os.listdir(indexes_dir):
        index = read_sql(os.path.join(indexes_dir, index_file))
        index_name = index_file.split(".")[0]

        print(f"START {index_name}")
        cur.execute(index[0])
        experiment[index_name] = test_transaction(cur, transaction, ITERATIONS)
        cur.execute(index[1])
        print("END")

    save_experiment(os.path.join(EXPERIMENTS_DIR, "indexes", transaction_name), experiment)

if __name__ == "__main__":
    main()
