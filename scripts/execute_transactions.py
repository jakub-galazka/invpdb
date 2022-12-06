import os
import cx_Oracle
import pandas as pd
from time import time
from dotenv import load_dotenv
from sqlscript import SQLScript

load_dotenv()

# Database connection
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Paths
ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "workload")
TRANSACTIONS_DIR = os.path.join(ROOT, "transactions")
EXECUTIONS_DIR = os.path.join(ROOT, "executions")
INDEXES_DIR = os.path.join(ROOT, "indexes")

ITERATIONS = 10
INDEX_KEYS = ["before_index", "b_tree", "bit_map"]

def main():
    # Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
    conn = cx_Oracle.connect("%s/%s@//localhost:1521/%s" % (DB_USER, DB_PASS, DB_NAME))
    cur = conn.cursor()

    for index_key in INDEX_KEYS:
        print("START", index_key)

        # Create dirs
        execution_dir = os.path.join(EXECUTIONS_DIR, index_key)
        query_plans_path = os.path.join(execution_dir, "query_plans")
        os.makedirs(query_plans_path)

        # Create indexes
        if not index_key == INDEX_KEYS[0]:
            execute_index_script(cur, index_key)

        # Do experiment
        scripts = {}
        for script_name in os.listdir(TRANSACTIONS_DIR):
            script = SQLScript(os.path.join(TRANSACTIONS_DIR, script_name))

            print("   START", script_name)
            for i in range(ITERATIONS):
                print(f'   {i + 1}/{ITERATIONS}')

                # Remove ROLLBACK statement
                statements = script.get_script_statements()
                if len(statements) > 1:
                    statements = statements[:-1]

                script.add_execution_time(execute_statements(cur, statements))
                cur.execute("ALTER SYSTEM FLUSH BUFFER_CACHE")
            print("   DONE", script_name)

            # Save query plan
            execute_statements(cur, script.get_explain_plan())
            script.set_query_plan(cur.fetchall())
            query_plan_path = os.path.join(query_plans_path, f'{script_name.split(".")[0]}.txt')
            with open(query_plan_path, "w") as f:
                f.write(script.get_query_plan())

            scripts[script_name] = script.get_execution_times()

        # Drop indexes
        if not index_key == INDEX_KEYS[0]:
            execute_index_script(cur, INDEX_KEYS[0])

        print("DONE", index_key)

        # Create report
        df = pd.DataFrame(scripts)
        df.loc["min"] = df.min()
        df.loc["max"] = df.max()
        df.loc["avg"] = df.mean()
        df.loc["std"] = df.std()
        df.to_csv(os.path.join(execution_dir, "report.csv"))

def execute_index_script(cur, index_key: str):
    script = SQLScript(os.path.join(INDEXES_DIR, f'{index_key}.sql'))
    execute_statements(cur, script.get_script_statements())

def execute_statements(cur, statements: list[str]) -> float:
    start = time()
    for s in statements:
        cur.execute(s)
    return time() - start

if __name__ == "__main__":
    main()
