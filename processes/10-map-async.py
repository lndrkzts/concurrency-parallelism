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
    time.sleep(1)
    return num % 2 == 0


if __name__ == '__main__':
    with Pool(processes=2) as executor:
        # .map works asynchronously
        # .map returns a MapResult object, like a future object

        nums = [x for x in range(1, 11)]
        results = executor.map_async(is_even, nums)

        logging.info('The process continues to run 1...')
        logging.info('The process continues to run 2...')
        logging.info('The process continues to run 3...')

        results.wait()

        for num, result in zip(nums, results.get()):
            logging.info(f'Is number {num} even? {result}')
