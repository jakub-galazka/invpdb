from generators import Generator, AccountGenerator, BuildingGenerator, AccBuildGenerator, RoomGenerator, ComputerGenerator, CPUGenerator, GPUGenerator, RamStickGenerator, SoftwareGenerator, SoftCompGenerator

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
        (RamStickGenerator(SEED), 200_000),
        (SoftwareGenerator(SEED), 500_000),
        (SoftCompGenerator(SEED), 500_000)
    ]

    for g in generators:
        g[0].generate(g[1])

if __name__ == "__main__":
    main()
