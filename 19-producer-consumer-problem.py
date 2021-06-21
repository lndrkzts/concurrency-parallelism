import time
import queue
import random
import logging
import threading

logging.basicConfig(
    level=logging.INFO,
    format='%(thread)s - %(threadName)s: %(message)s'
)

products = queue.Queue(maxsize=10)


def producer():
    while True:
        if not products.full():
            product = random.randint(1, 11)
            products.put(product)
            logging.info(f'Product {product} added')
            time.sleep(random.randint(1, 4))


def consumer():
    while True:
        if not products.empty():
            product = products.get()
            products.task_done()
            logging.info(f'Product {product} taken')
            time.sleep(random.randint(1, 4))


if __name__ == '__main__':
    thread_one = threading.Thread(target=producer)
    thread_two = threading.Thread(target=consumer)

    thread_one.start()
    thread_two.start()
