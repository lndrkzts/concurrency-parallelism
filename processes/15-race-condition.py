import time
import logging

from multiprocessing import Manager, Process

logging.basicConfig(
    level=logging.INFO,
    format='%(process)s - %(processName)s: %(message)s'
)

# Race Condition solution with processes


def desposit(namespace, lock):
    for _ in range(0, 100000):
        logging.info(_)
        with lock:
            namespace.balance += 10


def withdraw(namespace, lock):
    for _ in range(0, 100000):
        logging.info(_)
        with lock:
            namespace.balance -= 10


if __name__ == '__main__':
    manager = Manager()

    lock = manager.Lock()
    namespace = manager.Namespace()

    namespace.balance = 0

    process_one = Process(target=desposit, args=(namespace, lock,))
    process_two = Process(target=withdraw, args=(namespace, lock,))

    process_one.start()
    process_two.start()

    process_one.join()
    process_two.join()

    logging.info(f'Balance final value: {namespace.balance}')
