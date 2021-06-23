import time
import logging
import threading

logging.basicConfig(
    level=logging.INFO,
    format='%(thread)s - %(threadName)s: %(message)s'
)


def thread_one(event):
    logging.info('I am waiting for the signal')
    event.wait()  # Thread execution stops until it receives the signal
    logging.info('Signal recived')


def thread_two(event):
    logging.info('I am thread two')

    while not event.is_set():
        logging.info('Waiting for the signal...')
        time.sleep(0.5)


if __name__ == '__main__':
    # Events works like a flag, by default is False
    event = threading.Event()

    thread_1 = threading.Thread(target=thread_one, args=(event,))
    thread_2 = threading.Thread(target=thread_two, args=(event,))

    thread_1.start()
    thread_2.start()

    time.sleep(2)

    event.set()  # Sending the signal, flag is True

    event.clear()  #  Sets flag False again
