import random
import os
import logging
from datetime import datetime

LOG_FILE = "game_log.txt"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")


def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 6
    user_attempts = []

    print("Начинаем игру 'Угадай число' с шести попыток!")
    print("Я придумаю число от 1 до 100, а твоя задача — его угадать.")
    input("Готов? Нажми Enter ")

    start_time = datetime.now()
    logging.info(f"Игра началась в {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    logging.info(f"Загаданное число: {secret_number}")

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt}")
        try:
            guess = int(input("Введите целое число от 1 до 100: "))
        except ValueError:
            print("Ошибка! Нужно ввести целое число.")
            logging.warning(f"Попытка {attempt}: некорректный ввод")
            continue

        user_attempts.append(guess)
        logging.info(f"Попытка {attempt}: {guess}")

        if guess == secret_number:
            print(f"\n Верно, это действительно {secret_number}!")
            print(f"Вы угадали с {attempt}-й попытки! Ваша интуиция потрясающая!")
            end_time = datetime.now()
            logging.info(f"Игрок угадал число с {attempt}-й попытки")
            logging.info(f"Игра завершена в {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
            return
        elif guess < secret_number:
            print(f" Загаданное число больше, чем {guess}.")
        else:
            print(f" Загаданное число меньше, чем {guess}.")

    print(f"\n К сожалению, вы не угадали! Загаданное число было {secret_number}.")
    print(f"Ваши попытки: {user_attempts}")

    end_time = datetime.now()
    logging.info(f"Игра окончена. Число не угадано. Загаданное число: {secret_number}")
    logging.info(f"Время окончания игры: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    guess_number()
