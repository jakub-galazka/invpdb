import os

class SQLScript:

    EXPLAIN_PLAN_STATEMENT = "EXPLAIN PLAN FOR"
    SELECT_QUERY_PLAN = "SELECT * FROM table(DBMS_XPLAN.DISPLAY)"

    def __init__(self, sql_script_path: str) -> None:
        self.name = os.path.basename(sql_script_path)
        self.script_statements = self._read_sql(sql_script_path)

    def generate_report(self) -> str:
        return "SCRIPT NAME: %s\nEXECUTION TIME: %f\nQUERY PLAN:\n%s\n" % (self.name, self.execution_time, self.query_plan) 

    def _read_sql(self, sql_script_path: str) -> list[str]:
        with open(sql_script_path, "r") as f:
           return f.read().split(";")[:-1]

    def get_script_statements(self) -> list[str]:
        return self.script_statements

    def get_explain_plan(self) -> list[str]:
        return [SQLScript.EXPLAIN_PLAN_STATEMENT + self.script_statements[0], SQLScript.SELECT_QUERY_PLAN]

    def set_execution_time(self, execution_time: float) -> None:
        self.execution_time = execution_time

    def set_query_plan(self, query_plan_res: list[tuple]) -> None:
        self.query_plan = ""
        for e in query_plan_res:
            self.query_plan += e[0] + "\n"
