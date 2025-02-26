# Игра "Виселица"
#
# За основу возьмите свой код, разработанный в предыдущем проектном уроке, посвященном Game Hub (урок 13).
# Если в тот раз вы не реализовали весь функционал, то сначала реализуйте полностью игру, а затем переходите
# к рефакторингу на основе заданий из этого урока.
#
# Рефакторинг
# - Добавить логирование начала и окончания игры и всех попыток игрока с временными метками (дата и время).
# - Добавить обработку ошибок с использованием `try/except`, где это необходимо.
# - Добавить возможность сохранять текущий прогресс игры в файл для продолжения игры позже,
# если игра не была завершена победой или поражением (то есть было прерывание программы во время игры).


import json
import logging
import os
import datetime
import random

# Настройка логирования
logging.basicConfig(
    filename="hangman.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_progress():
    if os.path.exists("hangman_save.json"):
        try:
            with open("hangman_save.json", "r") as file:
                return json.load(file)
        except Exception as e:
            logging.error(f"Ошибка загрузки прогресса: {e}")
    return None


def save_progress(word, guessed_letters, attempts):
    try:
        with open("hangman_save.json", "w") as file:
            json.dump({"word": word, "guessed_letters": guessed_letters, "attempts": attempts}, file)
    except Exception as e:
        logging.error(f"Ошибка сохранения прогресса: {e}")


def delete_progress():
    if os.path.exists("hangman_save.json"):
        os.remove("hangman_save.json")


def choose_word():
    words = ["python", "hangman", "developer", "programming", "challenge"]
    return random.choice(words)


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def hangman():
    logging.info("Начало игры")

    progress = load_progress()

    if progress:
        word = progress["word"]
        guessed_letters = set(progress["guessed_letters"])
        attempts = progress["attempts"]
        print("Продолжение сохраненной игры.")
    else:
        word = choose_word()
        guessed_letters = set()
        attempts = 6
        print("Начало новой игры.")

    while attempts > 0:
        print("\nСлово:", display_word(word, guessed_letters))
        print(f"Оставшиеся попытки: {attempts}")

        guess = input("Введите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже угадали эту букву.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"Буквы '{guess}' нет в слове.")
        else:
            print(f"Отлично! Буква '{guess}' есть в слове.")

        logging.info(f"Попытка: {guess}, Осталось попыток: {attempts}")

        if set(word) <= guessed_letters:
            print(f"Поздравляем! Вы угадали слово: {word}")
            delete_progress()
            logging.info("Игра завершена победой")
            return

        save_progress(word, list(guessed_letters), attempts)

    print(f"Вы проиграли! Загаданное слово было: {word}")
    delete_progress()
    logging.info("Игра завершена поражением")


if __name__ == "__main__":
    try:
        hangman()
    except Exception as e:
        logging.error(f"Критическая ошибка в игре: {e}")
