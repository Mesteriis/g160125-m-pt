# import logging
#
# # Создать и добавить в код логгер по умолчанию.
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
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),  # Вывод в консоль
            logging.FileHandler("app.log", mode='w')  # Запись в файл
        ]
    )


def main():
    setup_logger()

    logging.debug("Это сообщение отладки (DEBUG)")
    logging.info("Это информационное сообщение (INFO)")
    logging.warning("Это предупреждение (WARNING)")
    logging.error("Это сообщение об ошибке (ERROR)")
    logging.critical("Это критическая ошибка (CRITICAL)")


if __name__ == '__main__':
    main()
