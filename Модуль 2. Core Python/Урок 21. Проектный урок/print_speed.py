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

import time
import random
import logging

# Настроим логирование
logging.basicConfig(filename='typing_speed_game.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def load_texts(file_path):
    """Загружает тексты из файла"""
    with open(file_path, 'r', encoding='utf-8') as file:
        texts = file.read().splitlines()
    print(f"Загружено {len(texts)} строк из файла.")
    return texts

def check_input(user_input, correct_text):
    """Проверяет, есть ли ошибки в вводе"""
    return user_input == correct_text

def main():
    # Получаем имя и фамилию
    first_name = input("Введите ваше имя: ")
    last_name = input("Введите вашу фамилию: ")

    # Загружаем фрагменты текста
    texts = load_texts("texts.txt")

    # Фильтруем фрагменты длиной 180 символов
    valid_texts = [text for text in texts if len(text) == 180]
    print(f"Найдено {len(valid_texts)} текстов длиной 180 символов.")

    if not valid_texts:
        print("В файле нет текстов длиной 180 символов.")
        logging.error("В файле нет текстов длиной 180 символов.")
        return

    # Выбираем случайный фрагмент текста
    correct_text = random.choice(valid_texts)

    # Обратный отсчет
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Поехали!")

    # Начало отсчета времени
    start_time = time.time()

    # Просим пользователя ввести текст
    user_input = input(f"Напечатайте следующее: \n{correct_text}\n")

    # Окончание отсчета времени
    end_time = time.time()

    # Вычисляем время
    elapsed_time = round(end_time - start_time, 2)

    # Проверяем на ошибки
    is_correct = check_input(user_input, correct_text)

    # Выводим результат
    print(f"\nИмя: {first_name} {last_name}")
    print(f"Фрагмент текста: {correct_text}")
    print(f"Ваш ввод: {user_input}")
    print(f"Ошибки: {'Нет' if is_correct else 'Да'}")
    print(f"Время: {elapsed_time} секунд")

    # Логируем информацию
    logging.info(f"Имя: {first_name} {last_name}, Фрагмент: {correct_text}, Ввод: {user_input}, Ошибки: {'Нет' if is_correct else 'Да'}, Время: {elapsed_time} секунд")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        logging.error(f"Ошибка: {e}")

