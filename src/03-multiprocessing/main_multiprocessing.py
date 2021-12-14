import datetime
import multiprocessing
from model.hash_generator import HashGenerator

QUANTITY = 160


def main():
    hash_gen = HashGenerator(difficulty=4)
    processor_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool()

    print(f'\nProcessors count: {processor_count}\n')

    t0 = datetime.datetime.now()

    for _ in range(processor_count):
        pool.apply_async(func=hash_gen.get_hashes, args=(QUANTITY / processor_count,))

    pool.close()
    pool.join()

    dt = datetime.datetime.now() - t0

    print(f'\nDone in {dt.total_seconds():.2f} seconds\n')


if __name__ == '__main__':
    main()
