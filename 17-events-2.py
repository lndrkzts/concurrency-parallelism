import logging
import requests
import threading

logging.basicConfig(
    level=logging.INFO,
    format='%(thread)s - %(threadName)s: %(message)s'
)

user = dict()


def generate_request(event, url):
    global user
    res = requests.get(url)

    if res.status_code == 200:
        res_json = res.json()
        user = res_json.get('results')[0]
        event.set()


def show_user_name(event):
    event.wait()
    name = user.get('name').get('first')
    logging.info(f'User name is: {name}')


if __name__ == '__main__':
    event = threading.Event()

    thread_one = threading.Thread(target=generate_request, args=(event, 'https://randomuser.me/api',))
    thread_two = threading.Thread(target=show_user_name, args=(event,))

    thread_one.start()
    thread_two.start()
