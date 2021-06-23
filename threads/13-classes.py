import time
import logging
import threading

logging.basicConfig(
    level=logging.INFO,
    format='%(thread)s - %(threadName)s: %(message)s'
)


class MyThread(threading.Thread):
    def __init__(self, name, daemon):
        threading.Thread.__init__(self, name=name, daemon=daemon)

    def run(self):
        while True:
            logging.info('Here will be the tasks that we want to execute')
            time.sleep(1)


if __name__ == '__main__':
    thread = MyThread('thread_name', True)
    thread.start()
    time.sleep(3)
    logging.info('End')
