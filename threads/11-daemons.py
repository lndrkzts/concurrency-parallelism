import time
import logging
import threading
import requests


logging.basicConfig(
    level=logging.INFO,
    format='%(thread)s - %(threadName)s: %(message)s'
)


def deamon_thread(currency):
    while True:
        res = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={currency}USDT')
        
        if res.status_code == 200:
            price = res.json().get('price')
            logging.info(f'{currency} Price: {price} USDT')
            time.sleep(1.5)


if __name__ == '__main__':
    daemon_thread_one = threading.Thread(target=deamon_thread, args=('BTC',), daemon=True)
    daemon_thread_two = threading.Thread(target=deamon_thread, args=('ETH',), daemon=True)
    
    daemon_thread_one.start()
    daemon_thread_two.start()

    input('----- Press enter key to end -----\n')
