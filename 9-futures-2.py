# Python Futures = Javascript Promises

import logging
import threading
import requests
from concurrent.futures import Future


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s - %(threadName)s: %(message)s'
)


def generate_request(url):
    future = Future()
    thread = threading.Thread(target=(
        lambda: future.set_result(requests.get(url))
    ))
    thread.start()
    return future


def show_pokemon_name(future):
    res_json = future.result().json()
    name = res_json.get('name')
    logging.info(f'Pokemon name: {name}')


if __name__ == '__main__':
    future = generate_request('https://pokeapi.co/api/v2/pokemon/1')
    future.add_done_callback(show_pokemon_name)

    while not future.done():
        logging.info('Waiting for result...')
    else:
        logging.info('Result saved!')