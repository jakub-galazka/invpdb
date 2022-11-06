import string
import random
import pandas as pd
from faker import Faker
from typing import List
from const import CSV_PATH, SEP


class Building:
    def __init__(self, quantity=1):
        self.fake_place = Faker()

        self._prepare_csv(quantity)

    def create_name(self, quantity) -> List[str]:
        # Unique name
        names_list = []
        for _ in range(quantity):
            name = self.fake_place.street_suffix()
            names_list = self._add_name(names_list, name)
        return names_list

    def _add_name(self, names_list, name):
        if name not in names_list:
            names_list.append(name)
        else:
            new_name = (
                name
                + " "
                + "".join(
                    random.choices(
                        string.ascii_lowercase,
                        k=random.randrange(2, 10),
                    )
                ).capitalize()
            )
            self._add_name(names_list, new_name)
        return names_list

    def create_floors_number(self, quantity=1) -> List[str]:
        return [random.randint(0, 3) for _ in range(quantity)]

    def create_street(self, quantity) -> List[str]:
        return [
            ""
            if random.randint(1, 100) <= 10
            else self.fake_place.street_name()
            for _ in range(quantity)
        ]

    def create_street_number(self, quantity=1) -> List[str]:
        return [
            ""
            if random.randint(1, 100) <= 10
            else "".join(
                random.choices(string.digits, k=random.randrange(1, 5))
                + random.choices(
                    string.ascii_lowercase, k=random.randrange(0, 2)
                )
            )
            for _ in range(quantity)
        ]

    def create_postal_code(self, quantity) -> List[str]:
        return [
            "" if random.randint(1, 100) <= 10 else self.fake_place.postcode()
            for _ in range(quantity)
        ]

    def create_city(self, quantity) -> List[str]:
        return [
            "" if random.randint(1, 100) <= 10 else self.fake_place.city()
            for _ in range(quantity)
        ]

    def create_country(self, quantity) -> List[str]:
        return [
            "" if random.randint(1, 100) <= 10 else self.fake_place.country()
            for _ in range(quantity)
        ]

    def _prepare_csv(self, quantity):
        df = pd.DataFrame(
            {
                "building_name": self.create_name(quantity),
                "floors_number": self.create_floors_number(quantity),
                "street": self.create_street(quantity),
                "street_number": self.create_street_number(quantity),
                "postal_code": self.create_postal_code(quantity),
                "city": self.create_city(quantity),
                "county": self.create_country(quantity),
            }
        )
        df.index.name = "id"
        df.to_csv(CSV_PATH % "building", index=True, sep=SEP)
