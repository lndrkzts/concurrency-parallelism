import logging
import threading


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s - %(threadName)s: %(message)s'
)


def callback():
    logging.info('Callback executed with delay by Timer class in another thread')

if __name__ == '__main__':
    thread = threading.Timer(3, callback)
    thread.start()

    logging.info('Principal thread')