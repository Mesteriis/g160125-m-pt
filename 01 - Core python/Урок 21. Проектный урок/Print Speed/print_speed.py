# Игра "Скорость печати" (print_speed.py)
#
# Программа запрашивает имя и фамилию пользователя. Затем производит обратный отсчет в консоле: 3, 2, 1, “поехали”.
# Далее выводит задание: Напечатай фрагмент текста из 180 символов: “какое-то предложение”.
# Пользователь печатает в консоль фрагмент текста и нажимает enter.
# Программа проверяет, есть ли во вводе ошибки и замеряет скорость печати.
# Выводит результат:
# - имя, фамилию;
# - фрагмент текста, который нужно было записать;
# - ввод пользователя;
# - есть ошибки или нет (то есть полностью ли совпадает ввод пользователя и фрагмент текста);
# - время, потраченное пользователем на ввод.
#
# Эта же информация, плюс дата и время начала и окончания игры должна записываться в лог-файл.
# Фрагменты текста для печати берутся в рандомном порядке из файла. То есть для каждой попытки из файла
# выбирается какой-то участок текста на 180 символов (включая пробелы) и выдается пользователю.
#
# Добавьте обработку ошибок с использованием `try/except`, где это необходимо.
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

def check_for_errors(user_input, target_text):
    return user_input == target_text

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

    is_correct = check_for_errors(user_input, target_text)
    time_taken = end_time - start_time

    print("\nРезультаты:")
    print(f"Имя: {first_name}")
    print(f"Фамилия: {last_name}")
    print(f"Заданный фрагмент текста:\n{target_text}")
    print(f"Ваш ввод:\n{user_input}")
    print(f"Ошибки: {'Нет' if is_correct else 'Есть'}")
    print(f"Время на ввод: {time_taken:.2f} секунд")

    game_result = {
        "имя": first_name,
        "фамилия": last_name,
        "заданный фрагмент текста": target_text,
        "ваш ввод": user_input,
        "ошибки": "Нет" if is_correct else "Есть",
        "время": f"{time_taken:.2f} секунд",
        "начало": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "конец": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    logging.info(f"Результат игры: {game_result}")

if __name__ == "__main__":
    play_print_speed_game()

