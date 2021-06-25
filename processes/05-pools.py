import logging

from concurrent.futures import ProcessPoolExecutor


logging.basicConfig(
    level=logging.INFO,
    format='%(process)s - %(processName)s: %(message)s'
)

NUMS = [10, 20, 35, 231]


def is_even(num):
    return num % 2 == 0


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as executor:
        results = executor.map(is_even, NUMS)
        for num, result in zip(NUMS, results):
            logging.info(f'Is number {num} even? {result}')
