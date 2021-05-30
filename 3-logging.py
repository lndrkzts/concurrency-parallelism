import logging

# Debug (10), Info (20), Warning (30), Error (40), Critical (50)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s: %(message)s'
    # format='%(levelname)s - %(filename)s - %(asctime)s - %(funcName)s - %(lineno)s - %(processName)s: %(message)s',
    # filename='log.txt'
)


def messages():
    logging.debug('DEBUG type message')
    logging.info('INFO type message')
    logging.warning('WARNING type message')
    logging.error('ERROR type message')
    logging.critical('CRITICAL type message')


if __name__ == '__main__':
    messages()
