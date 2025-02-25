# Игра "Виселица"
#
# Напишите программу для игры "Виселица". Игроку дается слово, которое он должен угадать, называя буквы.
# Если игрок называет неправильную букву, ему начисляется штрафное очко.
# Игра заканчивается победой при угадывании слова или проигрышем при достижении лимита штрафных очков.
#
# Требования:
#
# 1. Программа должна случайным образом выбирать слово из списка.
# 2. Игрок должен иметь возможность вводить буквы по одной за попытку.
# 3. Если игрок угадал букву, она должна отображаться в правильных позициях в слове.
# Вместо остальных (скрытых) букв показываются звездочки *.
# 4. Если игрок назвал неправильную букву, количество штрафных очков должно увеличиваться.
# 5. Игра заканчивается победой, если все буквы слова угаданы, или проигрышем,
# если количество штрафных очков достигает лимита (например, 6).

import random
import json
import os
from datetime import datetime
import logging
save_play = "save_game.json"
logging.basicConfig(filename="game_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

def save_game(state):
    try:
        with open(save_play, "w", encoding="utf-8") as file:
            json.dump(state, file, ensure_ascii=False, indent=4)
        logging.info("Игра сохранена: %s", state)
    except Exception as e:
        logging.error("Ошибка сохранения игры: %s", e)

def load_game():
    if os.path.exists(save_play):
        try:
            with open(save_play, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            logging.error("Ошибка загрузки сохраненной игры.")
    return None
words =  ["ананас", "интернет", "телефон", "алкоголь", "чайник" ]
max_tries = 6
saved_state = load_game()
if saved_state:
    word = saved_state["word"]
    correct_letters = set(saved_state["correct_letters"])
    incorrect_ans = saved_state["incorrect_ans"]
    print("Загружена сохраненная игра.")
else:
    word = random.choice(words)
    correct_letters = set()
    incorrect_ans = 0
print("Добро пожаловать в игру 'Виселица'! ")

while incorrect_ans < max_tries:
    display = "".join(letter + " " if letter in correct_letters else "_ " for letter in word)
    print("\nСлово:", display.strip())

    guess = input("Введите букву (кириллица): ").lower()

    if guess in correct_letters:
        print("Вы уже вводили эту букву.")
        continue

    correct_letters.add(guess)

    if guess not in word:
        incorrect_ans += 1
        print(f"Неправильно! Ошибок: {incorrect_ans} из {max_tries}")
    else:
        print("Правильно!")
    game_state = {
        "word": word,
        "correct_letters": list(correct_letters),
        "incorrect_ans": incorrect_ans
    }
    save_game(game_state)

    if all(letter in correct_letters for letter in word):
        print("Поздравляем! Вы угадали слово:", word)
        os.remove(save_play)
        break
else:
    print("Вы проиграли! Было загадано слово:", word)
    os.remove(save_play)