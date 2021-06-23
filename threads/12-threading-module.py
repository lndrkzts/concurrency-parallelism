import logging
import threading


logging.basicConfig(
    level=logging.INFO,
    format='%(thread)s - %(threadName)s: %(message)s'
)


def thread():
    current_thread = threading.current_thread()
    logging.info(f'Thread Id: {threading.get_ident()}')
    logging.info(f'Thread: {current_thread}')
    logging.info(f'Thread Name: {current_thread.getName()}')


if __name__ == '__main__':
    thread_one = threading.Thread(target=thread, name='my-first-thread')
    thread_two = threading.Thread(target=thread, name='my-second-thread')

    thread_one.start()
    thread_two.start()

    logging.info(f'Alive threads: {threading.enumerate()}')

    for thread in threading.enumerate():
        if thread == threading.main_thread():
            logging.info('This is the Main Thread')
