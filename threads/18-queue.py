import time
import queue
import logging
import threading

logging.basicConfig(
    level=logging.INFO,
    format='%(thread)s - %(threadName)s: %(message)s'
)

# Queue: https://docs.python.org/3/library/queue.html#module-queue


def add_items():
    for e in range(1, 20):
        my_queue.put(e)

    logging.info('Queue is load')


def show_items():
    while not my_queue.empty():
        logging.info(f'Item: {my_queue.get()}')
        my_queue.task_done()  # We have stopped using the queue
        time.sleep(0.5)


if __name__ == '__main__':
    my_queue = queue.Queue()  # FIFO queue
    add_items()

    for _ in range(4):
        thread = threading.Thread(target=show_items)
        thread.start()
