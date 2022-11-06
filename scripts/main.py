from generate_account import Accounts
from generate_building import Building


QUANTITY = 1000


def main():
    Accounts(QUANTITY)
    Building(QUANTITY)


if __name__ == "__main__":
    main()
