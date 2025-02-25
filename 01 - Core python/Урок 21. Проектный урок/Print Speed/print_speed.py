import random
import time
import logging
from datetime import datetime

logging.basicConfig(filename="print_speed_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

TEXT_FILE = "text_fragments.txt"


def load_text_fragments():
    try:
        with open(TEXT_FILE, "r", encoding="utf-8") as file:
            fragments = file.readlines()
        return [fragment.strip() for fragment in fragments if len(fragment.strip()) <= 180]
    except (FileNotFoundError, UnicodeDecodeError) as e:
        logging.error("Ошибка загрузки фрагментов текста: %s", e)
        return []


def count_errors(user_input, target_text):
    user_input = user_input.strip()
    target_text = target_text.strip()

    errors = 0
    min_length = min(len(user_input), len(target_text))

    for i in range(min_length):
        if user_input[i] != target_text[i]:
            errors += 1

    errors += abs(len(user_input) - len(target_text))
    return errors


def play_print_speed_game():
    fragments = load_text_fragments()
    if not fragments:
        print("Ошибка: нет доступных фрагментов текста.")
        return

    first_name = input("Введите ваше имя: ").strip()
    last_name = input("Введите вашу фамилию: ").strip()

    target_text = random.choice(fragments)
    print(f"Задание: Напечатайте следующий текст (180 символов):\n\n{target_text}\n")

    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Поехали!\n")

    start_time = time.time()
    user_input = input("Введите текст: ").strip()
    end_time = time.time()

    errors = count_errors(user_input, target_text)
    time_taken = end_time - start_time

    print("\nРезультаты:")
    print(f"Имя: {first_name}")
    print(f"Фамилия: {last_name}")
    print(f"Заданный фрагмент текста:\n{target_text}")
    print(f"Ваш ввод:\n{user_input}")
    print(f"Количество ошибок: {errors}")
    print(f"Время на ввод: {time_taken:.2f} секунд")

    game_result = {
        "имя": first_name,
        "фамилия": last_name,
        "заданный фрагмент текста": target_text,
        "ваш ввод": user_input,
        "количество ошибок": errors,
        "время": f"{time_taken:.2f} секунд",
        "начало": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "конец": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    logging.info(f"Результат игры: {game_result}")


if __name__ == "__main__":
    play_print_speed_game()
