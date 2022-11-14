import random
import pandas as pd
from faker import Faker
from .generator import Generator

class BuildingGenerator(Generator):

    def __init__(self, seed: int = None) -> None:
        super().__init__(seed)
        self.faker = Faker()
        if not seed == None:
            self.faker.seed_instance(seed)

    def generate(self, quantity: int = 1) -> None:
        building = pd.DataFrame({
            "building_name": super().generate_list(quantity, lambda: self.faker.unique.company()),
            "floors_number": super().generate_list(quantity, lambda: random.randint(1, 5)),
            "street": super().generate_list(quantity, lambda: self.faker.street_name(), True),
            "street_number": super().generate_list(quantity, lambda: self.faker.building_number(), True),
            "postal_code": super().generate_list(quantity, lambda: self.faker.postcode(), True),
            "city": super().generate_list(quantity, lambda: self.faker.city(), True),
            "country": super().generate_list(quantity, lambda: self.faker.country(), True),
        })
        self.csvw.write(building, "building")
