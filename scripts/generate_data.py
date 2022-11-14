from typing import List
from generators.generator import Generator
from generators.room_generator import RoomGenerator
from generators.account_generator import AccountGenerator
from generators.building_generator import BuildingGenerator


SEED = 0

def main():
    generators: List[(Generator, int)]  = [
        (AccountGenerator(SEED), 100),
        (BuildingGenerator(SEED), 10),
        (RoomGenerator(SEED), 100),
        
    ]

    for g in generators:
        g[0].generate(g[1])

if __name__ == "__main__":
    main()
