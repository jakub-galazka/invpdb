import os
import pandas as pd
from util.dbutils import *
from dotenv import load_dotenv
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
    transaction_names = ["1_select", "3_select", "4_update"]
    for name in transaction_names:
        print(f"\n_________________________ {name} _________________________\n")
        do_experiment(cur, name)

def do_experiment(cur, transaction_name: str) -> None:
    transaction = read_sql(os.path.join(TRANSACTIONS_DIR, f"{transaction_name}.sql"))
    experiment = {}

    # Before partition
    print("START before")
    experiment["before"] = test_transaction(cur, transaction, ITERATIONS)
    print("END")

    # After partition
    partition_dir = os.path.join("workload", "partitions", transaction_name, "dml")
    for partition_file in os.listdir(partition_dir):
        partition = read_sql(os.path.join(partition_dir, partition_file))
        partition_name = partition_file.split(".")[0]

        print(f"START {partition_name}")
        experiment[partition_name] = test_transaction(cur, partition, ITERATIONS)
        print("END")

        save_experiment(os.path.join(EXPERIMENTS_DIR, "partitions", transaction_name), experiment)

if __name__ == "__main__":
    main()
