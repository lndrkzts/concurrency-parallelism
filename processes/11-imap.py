import time
import logging

from multiprocessing import Pool

logging.basicConfig(
    level=logging.INFO,
    format='%(process)s - %(processName)s: %(message)s'
)


def is_even(num):
    time.sleep(1)
    return num, num % 2 == 0


if __name__ == '__main__':
    with Pool(processes=2) as executor:
        # .imap_unordered is a generator (yield)
        # for cases where order is not important
        nums = [x for x in range(1, 11)]

        for num, result in executor.imap_unordered(is_even, nums):
            logging.info(f'Is number {num} even? {result}')
