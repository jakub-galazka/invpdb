import os
import random
import numpy as np
from generate_account import Accounts
from generate_building import Building
from generate_room import Room
from generate_cpu import generate_cpu
from generate_gpu import generate_gpu
from generate_ram_stick import generate_ram_stick
from generate_software import Software
from const import CSV_PATH
from generate_room import Room
from generate_computer import Computer


SEED = 0
random.seed(SEED)
np.random.seed(SEED)

QUANTITY_ACCOUNTS = 100
QUANTITY_BUILDINGS = 10
QUANTITY_ROOMS = 1000
QUANTITY_CPU_GPU = 100_000
QUANTITY_RAM_STICK = 200_000
QUANTITY_SOFTWARE = 200_000
QUANTITY_COMPUTERS = 100_000

def main():
    if not os.path.exists(CSV_PATH % "account"): Accounts(QUANTITY_ACCOUNTS)
    if not os.path.exists(CSV_PATH % "building"): Building(QUANTITY_BUILDINGS)
    if not os.path.exists(CSV_PATH % "room"): Room(QUANTITY_ROOMS)
    if not os.path.exists(CSV_PATH % "computer"): Computer(QUANTITY_COMPUTERS)
    if not os.path.exists(CSV_PATH % "cpu"): generate_cpu(QUANTITY_CPU_GPU)
    if not os.path.exists(CSV_PATH % "gpu"): generate_gpu(QUANTITY_CPU_GPU)
    if not os.path.exists(CSV_PATH % "ram_stick"): generate_ram_stick(QUANTITY_RAM_STICK)
    if not os.path.exists(CSV_PATH % "software"): Software(QUANTITY_SOFTWARE)

if __name__ == "__main__":
    main()
