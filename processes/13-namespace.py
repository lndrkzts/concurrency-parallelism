import time
import logging

from multiprocessing import Manager, Process

logging.basicConfig(
    level=logging.INFO,
    format='%(process)s - %(processName)s: %(message)s'
)

#  Communication between processes


def get_value(namespace):
    while namespace.my_new_var_one is None and namespace.my_new_var_two is None:
        time.sleep(0.5)
        logging.info('vars have not value')
    else:
        logging.info(namespace.my_new_var_one)
        logging.info(namespace.my_new_var_two)


def set_value(namespace):
    time.sleep(5)
    namespace.my_new_var_one = 'I am the value one'
    namespace.my_new_var_two = 'I am the value two'


if __name__ == '__main__':
    namespace = Manager().Namespace()

    # We can give any name to the N variables
    namespace.my_new_var_one = None
    namespace.my_new_var_two = None

    process_one = Process(target=get_value, args=(namespace,))
    process_two = Process(target=set_value, args=(namespace,))

    process_one.start()
    process_two.start()

    # We need to call join()
    process_one.join()
    process_two.join()

    logging.info('End')
