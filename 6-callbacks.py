import logging
import requests
import threading

from requests.models import Response

logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s - %(threadName)s: %(message)s'
)


def get_pokemon_name(res_json):
    name = res_json.get('name')
    logging.info(f'Pokemon name: {name}')


def get_randomuser_name(res_json):
    name = res_json.get('results')[0].get('name').get('first')
    logging.info(f'Random name: {name}')


def error():
    logging.error('Invalid request')


def generate_request(url, success_callback, error_callback):
    res = requests.get(url)

    if res.status_code == 200:
        success_callback(res.json())
    else:
        error_callback()


if __name__ == '__main__':
    kwargs_one = {
        'url': 'https://pokeapi.co/api/v2/pokemon/1',
        'success_callback': get_pokemon_name,
        'error_callback': error
    }

    kwargs_two = {
        'url': 'https://randomuser.me/api/',
        'success_callback': get_randomuser_name,
        'error_callback': error
    }

    thread_one = threading.Thread(target=generate_request, kwargs=kwargs_one)
    thread_two = threading.Thread(target=generate_request, kwargs=kwargs_two)

    thread_one.start()
    thread_two.start()
