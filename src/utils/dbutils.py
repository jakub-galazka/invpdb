import time
import cx_Oracle

EXPLAIN_PLAN = "EXPLAIN PLAN FOR\n"
SELECT_QUERY_PLAN = "SELECT * FROM table(DBMS_XPLAN.DISPLAY)"
FLUSH_BUFFER_CACHE = "ALTER SYSTEM FLUSH BUFFER_CACHE"

def open_connection(db_user: str, db_pass: str, db_name: str):
    # Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
    return cx_Oracle.connect(f"{db_user}/{db_pass}@//localhost:1521/{db_name}")

def test_transaction(cur, statements: list[str], iterations: int) -> tuple[list[float], str]:
    return measure_execution_times(cur, statements, iterations), explain_plan(cur, statements[0])

def explain_plan(cur, statement: str) -> str:
    statements = [EXPLAIN_PLAN + statement, SELECT_QUERY_PLAN]
    execute_statements(cur, statements)
    query_plan = ""
    for e in cur.fetchall():
        query_plan += f"{e[0]}\n"
    return query_plan

def measure_execution_times(cur, statements: list[str], iterations: int) -> list[float]:
    execution_times = []
    for i in range(1, iterations + 1):
        print(f"Iteration {i}/{iterations}")
        execution_times.append(execute_statements(cur, statements))
        flush_buffer_cache(cur)
    return execution_times

def execute_statements(cur, statements: list[str]) -> float:
    start = time.time()
    for s in statements:
        cur.execute(s)
    return time.time() - start
    
def flush_buffer_cache(cur) -> None:
    cur.execute(FLUSH_BUFFER_CACHE)

def read_sql(sqlpath: str) -> list[str]:
    with open(sqlpath, "r") as f:
        return f.read().split(";")[:-1]
