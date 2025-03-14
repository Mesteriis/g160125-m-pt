# Игра: Угадай число
#
# За основу возьмите свой код, разработанный в предыдущем проектном уроке, посвященном Game Hub (урок 13).
# Если в тот раз вы не реализовали весь функционал, то сначала реализуйте полностью игру, а затем переходите
# к рефакторингу на основе заданий из этого урока.
#
# Рефакторинг
# - Добавить логирование действий (попыток пользователя) с использованием модуля `datetime`.
# В файл записывается время начало игры, время и значение каждой попытки, время окончания игры и результат.
# - Добавить обработку ошибок с использованием `try/except`, где это необходимо.

import random
import datetime


def log_attempt(log_file, message):
    with open(log_file, "a") as file:
        file.write(f"{datetime.datetime.now()} - {message}\n")


def guess_number():
    log_file = "guess_number.log"
    secret_number = random.randint(1, 100)
    attempts = 0
    log_attempt(log_file, "Game started")

    print("Угадайте число от 1 до 100")

    while True:
        try:
            guess = input("Введите ваш вариант: ")
            if guess.lower() == 'exit':
                log_attempt(log_file, "Game aborted by user")
                print("Вы вышли из игры.")
                break
            guess = int(guess)
            attempts += 1
            log_attempt(log_file, f"Attempt {attempts}: {guess}")

            if guess < secret_number:
                print("Загаданное число больше.")
            elif guess > secret_number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
                log_attempt(log_file, f"Game won in {attempts} attempts")
                break
        except ValueError:
            print("Ошибка: Введите целое число!")
            log_attempt(log_file, "Invalid input (not an integer)")

    log_attempt(log_file, "Game ended")


if __name__ == "__main__":
    guess_number()
