import time
import logging
import threading


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s - %(threadName)s: %(message)s'
)


def database_conection():
    logging.info('Connecting to database')
    time.sleep(2)


def web_server_request():
    logging.info('Request to web server')
    time.sleep(3)


if __name__ == '__main__':
    thread_one = threading.Thread(target=database_conection)
    thread_two = threading.Thread(target=web_server_request)

    thread_one.start()
    thread_two.start()

    thread_one.join()  # Sleep main thread until thread_one ends
    thread_two.join()  # Sleep main thread until thread_two ends

    logging.info('End')
