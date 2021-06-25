import time
import logging
import multiprocessing


logging.basicConfig(
    level=logging.INFO,
    format='%(process)s - %(processName)s: %(message)s'
)


def task():
    logging.info('Starting task...')
    time.sleep(10)
    logging.info('Finishing task...')


if __name__ == '__main__':
    process = multiprocessing.Process(target=task)
    process.start()
    time.sleep(2)

    if process.is_alive():
        process.terminate()
        logging.info('Terminate child process')
    
    logging.info('End')