import pandas as pd
from faker import Faker
from .generator import Generator

class AccountGenerator(Generator):

    def __init__(self, seed: int = None) -> None:
        super().__init__(seed)
        self.faker = Faker()
        if not seed == None:
            self.faker.seed_instance(seed)

    def generate(self, quantity: int = 1) -> None:
        usernames = self._generate_usernames(quantity)
        account = pd.DataFrame({
            "username": usernames,
            "email": self._generate_emails(usernames),
            "pass": self._generate_passwords(quantity),
            "last_login": self._generate_last_logins(quantity),
        })
        self.csvw.write(account, "account")

    def _generate_usernames(self, quantity: int) -> list[str]:
        return [self.faker.name() for _ in range(quantity)]

    def _generate_emails(self, usernames: list[str]) -> list[str]:
        return [
            (f"{''.join(username.split()).lower()}@gmail.com")
            for username in usernames
        ]

    def _generate_passwords(self, quantity: int) -> list[str]:
        return [self.faker.password() for _ in range(quantity)]

    def _generate_last_logins(self, quantity: int) -> list[str]:
        return [self.faker.date_time_between() for _ in range(quantity)]
