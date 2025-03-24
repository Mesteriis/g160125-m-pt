import logging


def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, filename='l.log', filemode='w',)

    logger.debug('This is DEBUG level message')
    logger.info('This is INFO level message')
    logger.warning('This is WARNING level message')
    logger.error('This is ERROR level message')
    logger.critical('This is CRITICAL level message')


if __name__ == '__main__':
    main()
