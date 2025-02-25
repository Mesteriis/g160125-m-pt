import json
import logging
from datetime import datetime
import os

logging.basicConfig(filename="game_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

game_state_file = "game_state.json"
story_file = "story.json"

def load_story():
    try:
        with open(story_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logging.error("Ошибка загрузки сюжета игры.")
        return {}

def save_game(state):
    try:
        with open(game_state_file, "w", encoding="utf-8") as file:
            json.dump(state, file, ensure_ascii=False, indent=4)
        logging.info("Игра сохранена: %s", state)
    except Exception as e:
        logging.error("Ошибка сохранения игры: %s", e)

def load_game():
    if os.path.exists(game_state_file):
        try:
            with open(game_state_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            logging.error("Ошибка загрузки сохраненной игры.")
    return None

def start_game():
    story = load_story()
    state = load_game() or {"location": "start"}
    logging.info("Игра начата.")
    play(state, story)

def play(state, story):
    while True:
        location = state["location"]
        scene = story.get(location)
        if not scene:
            print("Ошибка: неизвестная локация!")
            break

        print(scene["text"])
        logging.info("Локация: %s", location)

        if "choices" not in scene or not scene["choices"]:
            print("Конец игры!")
            logging.info("Игра завершена.")
            os.remove(game_state_file)
            break

        for i, choice in enumerate(scene["choices"], 1):
            print(f"{i}. {choice['text']}")

        while True:
            try:
                user_choice = int(input("Ваш выбор: ")) - 1
                if 0 <= user_choice < len(scene["choices"]):
                    state["location"] = scene["choices"][user_choice]["next"]
                    save_game(state)
                    break
                else:
                    print("Некорректный ввод. Попробуйте снова.")
            except ValueError:
                print("Введите число!")

if __name__ == "__main__":
    start_game()
