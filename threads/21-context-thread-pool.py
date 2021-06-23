import time
import logging

from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(
    level=logging.INFO,
    format='%(thread)s - %(threadName)s: %(message)s'
)


def sum(num_one, num_two):
    time.sleep(1)
    result = num_one + num_two
    logging.info(f'{num_one} + {num_two} = {result}')


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3, thread_name_prefix='MyThreadPool') as executor:
        executor.submit(sum, 10, 20)
        executor.submit(sum, 20, 30)
        executor.submit(sum, 30, 40)
        executor.submit(sum, 40, 50)

        executor.shutdown()

        executor.submit(sum, 40, 50)  # Error in this line because .shutdown() executed
