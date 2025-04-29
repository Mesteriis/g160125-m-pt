# Игра "Анаграммы" (anagrams.py)
#
# Игроку дается слово, и он должен составить из его букв как можно больше других слов за одну минуту.
# Слова должны содержаться в JSON файле. В каждом слове не менее 5 букв.
# Для каждой игры рандомно выбирается слово и выводится пользователю.
#
# Далее происходит отсчет одной минуты (не отображается в консоле).
# В это время пользователь должен через запятую вводить слова, состоящие из тех же букв, что и заданное слово.
# По истечению одной минуты программа проверяет ввод пользователя по следующим параметрам:
#
# - Придуманные пользователем слова не дублируют заданное слово;
# - Придуманные слова уникальны;
# - Придуманные слова состоят из тех же букв, что и заданное слово.
#
# Программа засчитывает только те слова, которые соответствуют критериям выше.
# Как результат игры программа выводит: заданное слово, количество засчитанных слов, придуманных пользователем,
# сами засчитанные слова, не засчитанные слова.
# Эта же информация, плюс дата и время начала и окончания игры должна записываться в лог-файл.
# Добавьте обработку ошибок с использованием `try/except`, где это необходимо.


import json
import random
import time
from datetime import datetime


# Загрузка слов из JSON файла
def load_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            words = json.load(f)
            return [word for word in words if len(word) >= 5]
    except FileNotFoundError:
        print("Файл не найден. Пожалуйста, проверьте путь к файлу.")
        return []
    except json.JSONDecodeError:
        print("Ошибка в формате JSON.")
        return []


# Проверка, состоит ли слово из тех же букв, что и заданное
def is_valid_word(word, target_word):
    return sorted(word) == sorted(target_word)


# Функция для игры
def play_game(words):
    if not words:
        print("Нет доступных слов для игры.")
        return

    # Случайное слово для игры
    target_word = random.choice(words)
    print(f"Задано слово: {target_word}")

    # Отсчет времени
    start_time = time.time()
    end_time = start_time + 60  # 60 секунд

    user_input = input("Введите слова (через запятую): ")
    user_words = [word.strip() for word in user_input.split(',')]

    valid_words = set()
    invalid_words = set()

    # Проверка каждого введенного слова
    for word in user_words:
        if word != target_word and len(word) >= 5 and word not in valid_words:
            if is_valid_word(word, target_word):
                valid_words.add(word)
            else:
                invalid_words.add(word)

    # Результаты игры
    print(f"\nЗадано слово: {target_word}")
    print(f"Количество засчитанных слов: {len(valid_words)}")
    print(f"Засчитанные слова: {', '.join(valid_words) if valid_words else 'Нет'}")
    print(f"Не засчитанные слова: {', '.join(invalid_words) if invalid_words else 'Нет'}")

    # Логирование результата игры
    log_game(target_word, valid_words, invalid_words, start_time, end_time)


# Логирование игры
def log_game(target_word, valid_words, invalid_words, start_time, end_time):
    log_data = {
        "target_word": target_word,
        "valid_words": list(valid_words),
        "invalid_words": list(invalid_words),
        "start_time": datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S'),
        "end_time": datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S'),
    }
    try:
        with open('game_log.json', 'a', encoding='utf-8') as f:
            json.dump(log_data, f, ensure_ascii=False, indent=4)
            f.write("\n")
    except Exception as e:
        print(f"Ошибка при записи в лог: {e}")


if __name__ == "__main__":
    # Загрузка слов
    words = load_words("words.json")

    # Запуск игры
    play_game(words)
