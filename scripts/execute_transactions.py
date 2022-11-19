import os
import cx_Oracle
from time import time
from sqlscript import SQLScript

# Database connection
DB_NAME = "INVPDB"
DB_USER = "INVADM"
DB_PASS = "admin123"

# Paths
ROOT = "transactions"
REPORT_OUTPUT = "transactions_report.txt"

def main():
    # Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
    conn = cx_Oracle.connect("%s/%s@//localhost:1521/%s" % (DB_USER, DB_PASS, DB_NAME))
    cur = conn.cursor()

    scripts: list[SQLScript] = []
    for script_name in os.listdir(ROOT):
        print("START", script_name)
        script = SQLScript(os.path.join(ROOT, script_name))

        script.set_execution_time(execute_statements(cur, script.get_script_statements()))
        execute_statements(cur, script.get_explain_plan())
        script.set_query_plan(cur.fetchall())

        scripts.append(script)
        print("DONE")

    with open(REPORT_OUTPUT, "w") as f:
        for s in scripts:
            f.write(s.generate_report())
            f.write("%s\n\n" % "".join("#" for _ in range(150)))

def execute_statements(cur, statements: list[str]) -> float:
    start = time()
    for s in statements:
        cur.execute(s)
    return time() - start

if __name__ == "__main__":
    main()
