import time
import logging
import multiprocessing

logging.basicConfig(
    level=logging.INFO,
    format='%(process)s - %(processName)s: %(message)s'
)


if __name__ == '__main__':
    process = multiprocessing.current_process()
    pid = process.pid
    name = process.name

    logging.info(f'Process: {process}')
    logging.info(f'Id: {pid}')
    logging.info(f'Name: {name}')
