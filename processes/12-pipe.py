import time
import logging

from multiprocessing import Process, Pipe

logging.basicConfig(
    level=logging.INFO,
    format='%(process)s - %(processName)s: %(message)s'
)

#  Communication between processes


class Publisher(Process):
    def __init__(self, connection):
        Process.__init__(self)
        self.connection = connection

    def run(self):
        logging.info('This is the Publisher process')

        for e in range(20):
            self.connection.send(f'Hi from Publisher process. Value: {e}')
            time.sleep(0.25)

        logging.info('Closing connection from Publisher')
        
        # In this case, None is like a flag to warn the Subscriber that the connection was closed
        self.connection.send(None)
        self.connection.close()


class Subscriber(Process):
    def __init__(self, connection):
        Process.__init__(self)
        self.connection = connection
        self.is_alive = True

    def run(self):
        logging.info('This is the Subscriber process')

        while self.is_alive:
            message = self.connection.recv()
            self.is_alive = message is not None
            logging.info(message)
        else:
            logging.info('Closing connection from Subscriber')
            self.connection.close()


if __name__ == '__main__':
    # Pipe returns a pair of connection objects connected by a pipe
    con1, con2 = Pipe()

    publisher = Publisher(con1)
    subscriber = Subscriber(con2)

    publisher.start()
    subscriber.start()
