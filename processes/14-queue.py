import time
import logging

from multiprocessing import Manager, Process

logging.basicConfig(
    level=logging.INFO,
    format='%(process)s - %(processName)s: %(message)s'
)

#  Communication between processes


def get_value(queue):
    while not queue.empty():
        time.sleep(0.5)
        logging.info(f'Value is: {queue.get(block=True)}')


if __name__ == '__main__':
    queue = Manager().Queue()

    for num in range(0, 20):
        queue.put(num)

    process_one = Process(target=get_value, args=(queue,))
    process_two = Process(target=get_value, args=(queue,))

    process_one.start()
    process_two.start()

    process_one.join()
    process_two.join()

    logging.info('End')
