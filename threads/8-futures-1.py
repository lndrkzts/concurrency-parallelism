# Python Futures = Javascript Promises

import time
import logging
from concurrent.futures import Future


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s - %(threadName)s: %(message)s'
)


def callback_future(future):
    logging.info('Callback executed after the future has a value')
    logging.info(f'Future value: {future.result()}')


if __name__ == '__main__':
    future = Future()
    future.add_done_callback(callback_future)

    logging.info('Task init...')
    time.sleep(2)
    logging.info('Task end...')

    future.set_result('lndr')
    logging.info('Value added to future')
