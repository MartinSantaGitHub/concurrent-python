import datetime
from model.hash_generator import HashGenerator

QUANTITY = 160


def main():
    hash_gen = HashGenerator(difficulty=4)
    t0 = datetime.datetime.now()

    hash_gen.get_hashes(quantity=QUANTITY)

    dt = datetime.datetime.now() - t0

    print(f'\nDone in {dt.total_seconds():.2f} seconds\n')


if __name__ == '__main__':
    main()
