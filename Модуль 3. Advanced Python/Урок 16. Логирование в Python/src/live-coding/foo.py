import logging
import random


# Создать и добавить в код логгер со своим именем.
# Подключить два канала логирования (stdout и файл).
# Настроить разные форматы логов для разных каналов.
# Подключить каналы к логгеру.
# Создать записи о событиях разных уровней от DEBUG до CRITICAL.


def main():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    file_handler = logging.FileHandler(f"{__name__}.log", mode="w")

    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    #
    handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(hdlr=handler)
    logger.addHandler(hdlr=file_handler)

    logger.setLevel(level=logging.INFO)

    logger.warning("Hello")

if __name__ == '__main__':
    main()

random.shuffle