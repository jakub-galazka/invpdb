import random
import pandas as pd
from typing import List
from faker import Faker
from .generator import Generator


class BuildingGenerator(Generator):

    def __init__(self, seed: int = None) -> None:
        self.faker = Faker()
        if not seed == None:
            self.faker.seed_instance(seed)
            random.seed(seed)
        
        Generator.__init__(self)

    def generate(self, quantity: int = 1) -> None:
        building = pd.DataFrame({
            "building_name": self._generate_building_names(quantity),
            "floors_number": self._generate_floors_numbers(quantity),
            "street": self._generate_streets(quantity),
            "street_number": self._generate_street_numbers(quantity),
            "postal_code": self._generate_postal_codes(quantity),
            "city": self._generate_cities(quantity),
            "country": self._generate_countries(quantity),
        })
        self.csvw.write(building, "building", "building_id")

    def _generate_building_names(self, quantity: int) -> List[str]:
        return [self.faker.unique.company() for _ in range(quantity)]

    def _generate_floors_numbers(self, quantity: int) -> List[str]:
        return [random.randint(1, 5) for _ in range(quantity)]

    def _generate_streets(self, quantity: int) -> List[str]:
        return super()._generate_with_null(quantity, lambda: self.faker.street_name())

    def _generate_street_numbers(self, quantity: int) -> List[str]:
        return super()._generate_with_null(quantity, lambda: self.faker.building_number())

    def _generate_postal_codes(self, quantity: int) -> List[str]:
        return super()._generate_with_null(quantity, lambda: self.faker.postcode())

    def _generate_cities(self, quantity: int) -> List[str]:
        return super()._generate_with_null(quantity, lambda: self.faker.city())

    def _generate_countries(self, quantity: int) -> List[str]:
        return super()._generate_with_null(quantity, lambda: self.faker.country())
