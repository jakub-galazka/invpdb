import pandas as pd

class CSVWriter:

    def __init__(self, csv_path: str = "csv/%s.csv") -> None:
        self.csv_path = csv_path

    def write(self, df: pd.DataFrame, file_name: str, index: bool = True) -> None:
        df.index.name = file_name + "_id"
        df.to_csv(self.csv_path % file_name, index=index)
