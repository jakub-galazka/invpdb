import numpy as np
from random import seed
from generate_account import Accounts
from generate_building import Building
from generate_gpu import generate_gpu


seed(0)
np.random.seed(0)

QUANTITY = 100_000

def main():
    Accounts(int(QUANTITY / 1000))
    Building(int(QUANTITY / 10000))
    generate_gpu(QUANTITY)

if __name__ == "__main__":
    main()
