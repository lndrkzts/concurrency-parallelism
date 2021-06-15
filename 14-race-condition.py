import logging
import threading

logging.basicConfig(
    level=logging.INFO,
    format='%(thread)s - %(threadName)s: %(message)s'
)

# Race Condition ==> https://en.wikipedia.org/wiki/Race_condition


BALANCE = 0


def desposit():
    global BALANCE

    for _ in range(0, 1000000):
        BALANCE += 10  # Critical section


def withdraw():
    global BALANCE

    for _ in range(0, 1000000):
        BALANCE -= 10  # Critical section


if __name__ == '__main__':
    thread_one = threading.Thread(target=desposit)
    thread_two = threading.Thread(target=withdraw)

    thread_one.start()
    thread_two.start()

    thread_one.join()
    thread_two.join()

    logging.info(f'Balance final value: {BALANCE}')
