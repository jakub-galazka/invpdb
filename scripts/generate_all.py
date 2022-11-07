import random
import numpy as np
from generate_account import Accounts
from generate_building import Building
from generate_gpu import generate_gpu
from generate_ram_stick import generate_ram_stick


SEED = 0
random.seed(SEED)
np.random.seed(SEED)

QUANTITY = 100_000

def main():
    Accounts(int(QUANTITY / 1000))
    Building(int(QUANTITY / 10000))
    generate_gpu(QUANTITY)
    generate_ram_stick(2 * QUANTITY)

if __name__ == "__main__":
    main()
