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
        # .map works synchronously
        # .map returns a List of the function 'is_even' results

        nums = [x for x in range(1, 11)]
        results = executor.map(is_even, nums)

        logging.info('This message will be displayed after .map execution ends')

        for num, result in zip(nums, results):
            logging.info(f'Is number {num} even? {result}')
