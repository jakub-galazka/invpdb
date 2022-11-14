import pandas as pd

class CSVWriter:

    def __init__(self, csv_path: str = "csv/%s.csv", sep: str = ";") -> None:
        self.csv_path = csv_path
        self.sep = sep

    def write(self, df: pd.DataFrame, file_name: str) -> None:
        df.index.name = file_name + "_id"
        df.to_csv(self.csv_path % file_name, sep=self.sep)
