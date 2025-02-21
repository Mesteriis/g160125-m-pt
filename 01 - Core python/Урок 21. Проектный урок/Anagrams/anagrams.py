import random
import json
import logging
from datetime import datetime

logging.basicConfig(filename="anagrams_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")
WORDS_FILE = "words.json"

def load_words():
    try:
        with open(WORDS_FILE, "r", encoding="utf-8") as file:
            words = json.load(file)
        return [word for word in words if len(word) >= 5]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error("Ошибка загрузки словаря: %s", e)
        return []

def is_valid_anagram(word, anagram):
    if len(anagram) < 5:
        return False

    word_letters = list(word)
    for letter in anagram:
        if letter in word_letters:
            word_letters.remove(letter)
        else:
            return False
    return True

def play_anagrams():
    words = load_words()
    if not words:
        print("Ошибка: список слов не загружен.")
        return

    word = random.choice(words)
    print(f"Ваше слово: {word}")
    print("У вас есть 60 секунд, чтобы ввести слова через запятую, используя буквы этого слова!")

    start_time = datetime.now()
    user_input = ""

    while True:

        elapsed_time = (datetime.now() - start_time).total_seconds()

        if elapsed_time >= 60:
            print("Время вышло! Вы не успели ввести слова.")
            break


        user_input = input("Введите слова через запятую: ").lower().replace(" ", "")

        if user_input:
            break

    end_time = datetime.now()

    user_words = [w.strip() for w in user_input.split(",") if w.strip()]
    valid_words = []
    invalid_words = []
    seen_words = set()

    for w in user_words:
        if w == word:
            invalid_words.append(w)
        elif w in seen_words:
            invalid_words.append(w)
        elif is_valid_anagram(word, w):
            valid_words.append(w)
            seen_words.add(w)
        else:
            invalid_words.append(w)

    print("\nРезультаты:")
    print(f"Исходное слово: {word}")
    print(f"Засчитанных слов: {len(valid_words)}")
    print("Засчитанные слова:", ", ".join(valid_words) if valid_words else "нет")
    print("Не засчитанные слова:", ", ".join(invalid_words) if invalid_words else "нет")

    game_result = {
        "слово": word,
        "начало": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "конец": end_time.strftime("%Y-%m-%d %H:%M:%S"),
        "засчитанные слова": valid_words,
        "незасчитанные слова": invalid_words
    }

    logging.info(json.dumps(game_result, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    play_anagrams()
