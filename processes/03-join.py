import time
import logging
import multiprocessing


logging.basicConfig(
    level=logging.INFO,
    format='%(process)s - %(processName)s: %(message)s'
)


def database_conection():
    logging.info('Connecting to database')
    time.sleep(2)


def web_server_request():
    logging.info('Request to web server')
    time.sleep(3)


if __name__ == '__main__':
    process_one = multiprocessing.Process(target=database_conection)
    process_two = multiprocessing.Process(target=web_server_request)

    process_one.start()
    process_two.start()

    process_one.join()  # Sleep main process until process_one ends
    process_two.join()  # Sleep main process until process_two ends

    logging.info('End')
