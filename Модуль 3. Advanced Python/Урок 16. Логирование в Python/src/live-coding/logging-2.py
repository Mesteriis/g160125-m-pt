import logging


def main():
    logger = logging.getLogger(__name__)
    stdout_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    stdout_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename=f'{__name__}.log', mode='w')

    stdout_handler.setFormatter(fmt=stdout_formatter)
    file_handler.setFormatter(fmt=file_formatter)

    logger.addHandler(hdlr=stdout_handler)
    logger.addHandler(hdlr=file_handler)

    logger.setLevel(level=logging.DEBUG)

    logger.info('Info')


if __name__ == '__main__':
    main()
