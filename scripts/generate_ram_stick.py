import numpy as np
import pandas as pd
from const import CSV_PATH, SEP

# Naive RAM stick data generation
MEMORY = np.array([2**i for i in range(1, 6)])
RAM_STICK_TYPE = np.array(["DDR%d" % i for i in range(1, 5)])
CLOCK_SPEED = np.array([200, 266, 300, 333, 400, 533, 667, 800, 1000, 800, 1066, 1333, 1600, 2400, 2666, 2933, 3000, 3200, 3600, 4000, 4400])

def generate_ram_stick(quantity=1):
    computer_data = pd.read_csv(CSV_PATH % "computer", sep=SEP)

    memory_index = np.random.randint(0, len(MEMORY), quantity)
    ram_stick_type_index = np.random.randint(0, len(RAM_STICK_TYPE), quantity)
    clock_speed_index = np.random.randint(0, len(CLOCK_SPEED), quantity)

    df = pd.DataFrame({
        "memory": MEMORY[memory_index],
        "ram_stick_type": RAM_STICK_TYPE[ram_stick_type_index],
        "clock_speed": CLOCK_SPEED[clock_speed_index],
        "computer_id": computer_data.sample(quantity, replace=True).index.values
    })
    df.index.name = "id"
    df.to_csv(CSV_PATH % "ram_stick", sep=SEP)
