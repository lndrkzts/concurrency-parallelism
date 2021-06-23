import logging
import threading

logging.basicConfig(
    level=logging.INFO,
    format='%(thread)s - %(threadName)s: %(message)s'
)

BALANCE = 100

lock = threading.RLock()  # Now is .RLock()


if __name__ == '__main__':
    lock.acquire()
    # With .Lock(), in next line python wait for the share resource to be released...
    lock.acquire()

    BALANCE -= 10

    lock.release()
    lock.release()  # If we acquire it twice, then we must release it twice

    logging.info(f'Balance final value: {BALANCE}')
