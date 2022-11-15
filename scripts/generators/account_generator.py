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
        usernames = super().generate_list(quantity, lambda: self.faker.name())
        account = pd.DataFrame({
            "username": usernames,
            "email": self._generate_emails(usernames),
            "pass": super().generate_list(quantity, lambda: self.faker.password()),
            "last_login": super().generate_list(quantity, lambda: self.faker.date_time_between()),
        })
        self.csvw.write(account, "account")

    def _generate_emails(self, usernames: list[str]) -> list[str]:
        return [
            f"{''.join(username.split()).lower()}@gmail.com"
            for username in usernames
        ]
