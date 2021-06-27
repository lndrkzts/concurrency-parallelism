import time
import logging

from multiprocessing import Pool

# The Pool class is antoher way to create process pools
# But with the ProcessPoolExecutor class we can work in parallel


logging.basicConfig(
    level=logging.INFO,
    format='%(process)s - %(processName)s: %(message)s'
)


def is_even(num):
    time.sleep(2)
    return num % 2 == 0


if __name__ == '__main__':
    with Pool(processes=2) as executor:
        # .apply works synchronously
        # .apply returns the function 'is_even' result
        result = executor.apply(is_even, args=(11,))
        logging.info(f'Is number 11 even? {result}')

        result = executor.apply(is_even, args=(12,))
        logging.info(f'Is number 12 even? {result}')
