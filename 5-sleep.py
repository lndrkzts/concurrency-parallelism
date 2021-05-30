import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s - %(threadName)s: %(message)s'
)


def clock():
    count = 0

    while True:
        time.sleep(1)
        count += 1
        logging.debug(f'Time elapsed: {count} seconds')


if __name__ == '__main__':
    clock()
