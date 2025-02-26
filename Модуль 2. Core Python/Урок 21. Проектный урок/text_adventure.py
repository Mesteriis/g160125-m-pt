# Игра "Текстовый квест"
#
# За основу возьмите свой код, разработанный в предыдущем проектном уроке, посвященном Game Hub (урок 13).
# Если в тот раз вы не реализовали весь функционал, то сначала реализуйте полностью игру, а затем переходите
# к рефакторингу на основе заданий из этого урока.
#
# Рефакторинг
# - Добавить логирование начала и окончания игры и всех ходов игрока с временными метками (дата и время).
# - Добавить обработку ошибок с использованием `try/except`, где это необходимо.
# - Сюжет игры должен подгружаться из файла JSON.
# - Добавить сохранение и загрузку состояния игры с использованием файлов в формате JSON.
# Если программа была прервана по ходу игры, то пользователь при старте программы начинает с того же места.


import json
import logging
import os
from datetime import datetime

# Настройка логирования
logging.basicConfig(
    filename="game.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_story(filename="story.json"):
    """Загружает сюжет игры из JSON-файла."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("Файл сюжета не найден.")
        print("Ошибка: Файл с сюжетом не найден.")
        exit(1)
    except json.JSONDecodeError:
        logging.error("Ошибка в формате JSON-файла.")
        print("Ошибка: Некорректный формат файла сюжета.")
        exit(1)


def load_game_state(filename="savegame.json"):
    """Загружает сохраненное состояние игры."""
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            logging.error("Ошибка чтения сохраненного состояния.")
            return None
    return None


def save_game_state(state, filename="savegame.json"):
    """Сохраняет текущее состояние игры."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(state, file, indent=4)


def play_game():
    """Основной игровой цикл."""
    logging.info("Начало игры.")
    story = load_story()
    state = load_game_state() or {"current_scene": "start"}

    while True:
        scene = state["current_scene"]
        if scene not in story:
            logging.error(f"Сцена {scene} не найдена в сюжете.")
            print("Ошибка: Сюжет поврежден или неполный.")
            break

        print(story[scene]["text"])
        if "choices" not in story[scene]:
            print("Конец игры!")
            logging.info("Игра завершена.")
            break

        for i, choice in enumerate(story[scene]["choices"], 1):
            print(f"{i}. {choice['text']}")

        try:
            choice = int(input("Введите номер выбора: ")) - 1
            if choice < 0 or choice >= len(story[scene]["choices"]):
                raise ValueError("Некорректный ввод.")
            state["current_scene"] = story[scene]["choices"][choice]["next_scene"]
            save_game_state(state)
            logging.info(f"Игрок выбрал: {story[scene]['choices'][choice]['text']}")
        except ValueError:
            print("Ошибка: Введите корректный номер выбора.")
            logging.warning("Игрок ввел некорректное значение.")


if __name__ == "__main__":
    play_game()
