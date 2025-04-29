# import logging
#
# # Создать и добавить в код логгер со своим именем.
# # Подключить два канала логирования (stdout и файл).
# # Настроить разные форматы логов для разных каналов.
# # Подключить каналы к логгеру.
# # Создать записи о событиях разных уровней от DEBUG до CRITICAL.
#
#
# def main():
#     # your code here
#     pass
#
#
# if __name__ == '__main__':
#     main()

import logging


def setup_logger():
    # Создаем логгер
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик для вывода в stdout
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.INFO)
    stdout_formatter = logging.Formatter("[%(levelname)s] %(message)s")
    stdout_handler.setFormatter(stdout_formatter)

    # Создаем обработчик для записи в файл
    file_handler = logging.FileHandler("app.log", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    # Добавляем обработчики к логгеру
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)

    return logger


def main():
    logger = setup_logger()

    # Логирование событий разного уровня
    logger.debug("Это сообщение DEBUG")
    logger.info("Это сообщение INFO")
    logger.warning("Это сообщение WARNING")
    logger.error("Это сообщение ERROR")
    logger.critical("Это сообщение CRITICAL")


if __name__ == '__main__':
    main()
