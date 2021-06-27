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
        # .apply_async works asynchronously
        # .apply returns an ApplyResult object, like a future object
        logging.info('Executing async')
        apply_result = executor.apply_async(is_even, args=(11,))

        logging.info('The process continues to run 1...')
        logging.info('The process continues to run 2...')
        logging.info('The process continues to run 3...')

        apply_result.wait(timeout=2)
        logging.info(f'Is number 11 even? {apply_result.get()}')