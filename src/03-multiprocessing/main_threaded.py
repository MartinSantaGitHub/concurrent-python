import datetime
import multiprocessing
from threading import Thread
from model.hash_generator import HashGenerator

QUANTITY = 160


def main():
    hash_gen = HashGenerator(difficulty=4)
    processor_count = multiprocessing.cpu_count()
    threads = []

    print(f'\nProcessors count: {processor_count}\n')

    t0 = datetime.datetime.now()

    for _ in range(processor_count):
        threads.append(Thread(target=hash_gen.get_hashes, args=(QUANTITY / processor_count,)))

    [t.start() for t in threads]
    [t.join() for t in threads]

    dt = datetime.datetime.now() - t0

    print(f'\nDone in {dt.total_seconds():.2f} seconds\n')


if __name__ == '__main__':
    main()
