import random
import numpy as np
from generate_account import Accounts
from generate_building import Building
from generate_gpu import generate_gpu
from generate_ram_stick import generate_ram_stick
from generate_room import Room


SEED = 0
random.seed(SEED)
np.random.seed(SEED)

QUANTITY_ACCOUNTS = 100
QUANTITY_BUILDINGS = 10
QUANTITY_ROOMS = 1000
QUANTITY_GPU = 100_000
QUANTITY_RAM_STICK = 200_000


def main():
    Accounts(QUANTITY_ACCOUNTS)
    Building(QUANTITY_BUILDINGS)
    Room(QUANTITY_ROOMS)
    generate_gpu(QUANTITY_GPU)
    generate_ram_stick(QUANTITY_RAM_STICK)


if __name__ == "__main__":
    main()
