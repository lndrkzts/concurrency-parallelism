import time
import random
import logging
import requests

from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s - %(threadName)s: %(message)s'
)

URLS = [
    'https://github.com',
    'https://twitter.com',
    'https://youtube.com',
    'https://hackerrank.com',
    'https://google.com',
    'https://dev.to',
    'https://code.visualstudio.com',
    'https://codewars.com'
]


def generate_request(url):
    time.sleep(random.randint(1, 3))
    return requests.get(url)


def check_status(response, url):
    logging.info(f'Server {url} response is {response.status_code}')


def sum(num_one, num_two):
    return num_one + num_two


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as executor:
        # executor.submit() returns a Future
        # futures = [executor.submit(generate_request, url) for url in URLS]

        # as_completed is a generator, and returns (by yield) the completed futures
        # for future in as_completed(futures):
        #     result, url = future.result()
        #     check_status(result, url)

        # map is a generator, in this case returns the method result
        results = executor.map(generate_request, URLS)

        for url, response in zip(URLS, results):
            check_status(response, url)

        # Add a new task to the first available thread
        future = executor.submit(sum, 10, 20)
        future.add_done_callback(
            lambda future: logging.info(f'Sum result is {future.result()}')
        )
