import threading


def executor_one(id=0):
    for i in range(0, 10):
        print(f'Thread {id} - Iteración {i}')


def executor_two(id=0):
    for i in range(0, 10):
        print(f'Thread {id} - Iteración {i}')


def executor_three(id=0):
    for i in range(0, 10):
        print(f'Thread {id} - Iteración {i}')


thread_one = threading.Thread(target=executor_one, args=[1])
thread_two = threading.Thread(target=executor_one, args=(2,))
thread_three = threading.Thread(target=executor_one, kwargs={'id': 3})

thread_one.start()
thread_two.start()
thread_three.start()
