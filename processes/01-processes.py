import time
import logging
import multiprocessing

logging.basicConfig(
    level=logging.INFO,
    format='%(process)s - %(processName)s: %(message)s'
)


def new_process(secs, message):
    logging.info('Son process, you can search me in your OS process list')
    time.sleep(secs)
    logging.info(message)
    logging.info('End')


if __name__ == '__main__':
    logging.info('Root process')
    # args [] () or kwargs {} to send arguments to functions
    process = multiprocessing.Process(target=new_process, args=(10, 'I am a message',))
    process.start()
