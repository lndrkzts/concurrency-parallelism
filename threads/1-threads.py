import requests
import threading


def get_name():
    res = requests.get('https://randomuser.me/api/')

    if res.status_code == 200:
        results = res.json().get('results')
        name = results[0].get('name').get('first')
        print(name)


if __name__ == '__main__':
    # Sequential
    for _ in range(0, 20):
        get_name()

    # Concurrent
    for _ in range(0, 20):
        thread = threading.Thread(target=get_name)
        thread.start()
