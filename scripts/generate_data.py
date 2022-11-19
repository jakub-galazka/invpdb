from generators import (
    Generator,
    AccountGenerator,
    BuildingGenerator,
    AccBuildGenerator,
    RoomGenerator,
    ComputerGenerator,
    CPUGenerator,
    GPUGenerator,
    RamStickGenerator,
    SoftwareGenerator,
    SoftCompGenerator,
)

SEED = 0


def main() -> None:
    generators: list[tuple[Generator, int]]  = [
        (AccountGenerator(SEED), 300),
        (BuildingGenerator(SEED), 500),
        (AccBuildGenerator(SEED), 1_000),
        (RoomGenerator(SEED), 50_000),
        (ComputerGenerator(SEED), 500_000),
        (CPUGenerator(SEED), 500_000),
        (GPUGenerator(SEED), 500_000),
        (RamStickGenerator(SEED), 1_000_000),
        (SoftwareGenerator(SEED), 2_000_000),
        (SoftCompGenerator(SEED), 2_000_000)
    ]

    for g in generators:
        g[0].generate(g[1])


if __name__ == "__main__":
    main()
