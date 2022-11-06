import names
import string
import random
import pandas as pd
from typing import List
from datetime import datetime
from datetime import timedelta
from const import CSV_PATH, SEP


class Accounts:
    def __init__(self, quantity=1):
        self._prepare_csv(quantity)

    def create_username(self, quantity=1) -> List[str]:
        return [str(names.get_full_name()) for _ in range(quantity)]

    def create_emails(self, usernames: List[str]) -> List[str]:
        return [
            (f"{''.join(name.split())}@gmail.com").lower()
            for name in usernames
        ]

    def create_password(self, quantity=1) -> List[str]:
        return [
            "".join(
                random.choices(
                    string.ascii_letters + string.digits,
                    k=random.randrange(5, 10),
                )
            )
            for _ in range(quantity)
        ]

    def create_last_login(self, quantity=1) -> List[str]:
        date1 = datetime.strptime("1/1/2000", "%m/%d/%Y")
        date2 = datetime.strptime("1/1/2022", "%m/%d/%Y")
        return [
            "".join(self._random_date(date1, date2)) for _ in range(quantity)
        ]

    """
        This function will return a random datetime between two datetime
        objects.
    """
    def _random_date(self, start, end):
        delta = end - start
        random_second = random.randrange(delta.total_seconds())
        return str(start + timedelta(seconds=random_second))

    def _prepare_csv(self, quantity):
        usernames = self.create_username(quantity)
        df = pd.DataFrame(
            {
                "username": usernames,
                "email": self.create_emails(usernames),
                "password": self.create_password(quantity),
                "last_login": self.create_last_login(quantity),
            }
        )
        df.index.name = "id"
        df.to_csv(CSV_PATH % "account", index=True, sep=SEP)
