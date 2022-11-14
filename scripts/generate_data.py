from generators.generator import Generator
from generators.cpu_generator import CPUGenerator
from generators.gpu_generator import GPUGenerator
from generators.room_generator import RoomGenerator
from generators.account_generator import AccountGenerator
from generators.building_generator import BuildingGenerator
from generators.computer_generator import ComputerGenerator
from generators.ram_stick_generator import RamStickGenerator
from generators.acc_build_generator import AccBuildGenerator

SEED = 0

def main() -> None:
    generators: list[tuple[Generator, int]]  = [
        (AccountGenerator(SEED), 100),
        (BuildingGenerator(SEED), 10),
        (AccBuildGenerator(SEED), 200),
        (RoomGenerator(SEED), 100),
        (ComputerGenerator(SEED), 100_000),
        (CPUGenerator(SEED), 100_000),
        (GPUGenerator(SEED), 100_000),
        (RamStickGenerator(SEED), 200_000)

    ]

    for g in generators:
        g[0].generate(g[1])

if __name__ == "__main__":
    main()
