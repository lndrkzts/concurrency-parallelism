import time
import logging
import requests
import multiprocessing


logging.basicConfig(
    level=logging.INFO,
    format='%(process)s - %(processName)s: %(message)s'
)


def deamon_process(currency):
    while True:
        res = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={currency}USDT')
        
        if res.status_code == 200:
            price = res.json().get('price')
            logging.info(f'{currency} Price: {price} USDT')
            time.sleep(1.5)


if __name__ == '__main__':
    daemon_process_one = multiprocessing.Process(target=deamon_process, args=('BTC',), daemon=True)
    daemon_process_two = multiprocessing.Process(target=deamon_process, args=('ETH',), daemon=True)
    
    daemon_process_one.start()
    daemon_process_two.start()

    input('----- Press enter key to end -----\n')