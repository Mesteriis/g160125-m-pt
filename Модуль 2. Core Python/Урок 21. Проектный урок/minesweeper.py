# Игра: Сапёр
#
# За основу возьмите свой код, разработанный в предыдущем проектном уроке, посвященном Game Hub (урок 13).
# Если в тот раз вы не реализовали весь функционал, то сначала реализуйте полностью игру, а затем переходите
# к рефакторингу на основе заданий из этого урока.
#
# Рефакторинг
# - Добавить логирование начала и окончания игры и всех ходов игрока с временными метками (дата и время).
# - Добавить обработку ошибок с использованием `try/except`, где это необходимо.
# - Добавить сохранение и загрузку состояния игры с использованием файлов в формате JSON.
# Если программа была прервана по ходу игры, то пользователь при старте программы начинает с того же места.


import json
import logging
import os
import random
import time

# Настройка логирования
logging.basicConfig(
    filename="minesweeper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def save_game(state, filename="minesweeper_save.json"):
    """Сохраняет текущее состояние игры в JSON-файл."""
    with open(filename, "w") as f:
        json.dump(state, f)


def load_game(filename="minesweeper_save.json"):
    """Загружает сохраненное состояние игры из JSON-файла."""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return None


def generate_board(size, mines):
    """Создает игровое поле."""
    board = [[0 for _ in range(size)] for _ in range(size)]
    mine_positions = random.sample(range(size * size), mines)

    for pos in mine_positions:
        row, col = divmod(pos, size)
        board[row][col] = "X"

    return board


def display_board(board, revealed):
    """Отображает игровое поле."""
    size = len(board)
    print("  " + " ".join(str(i) for i in range(size)))
    for i in range(size):
        row = [str(board[i][j]) if revealed[i][j] else "-" for j in range(size)]
        print(f"{i} {' '.join(row)}")


def play_game(size=5, mines=5):
    """Основная функция игры."""
    state = load_game()

    if state:
        logging.info("Загружено предыдущее состояние игры.")
        board = state["board"]
        revealed = state["revealed"]
        moves = state["moves"]
    else:
        board = generate_board(size, mines)
        revealed = [[False] * size for _ in range(size)]
        moves = []
        logging.info("Начало новой игры.")

    while True:
        display_board(board, revealed)
        try:
            row, col = map(int, input("Введите координаты (строка, столбец): ").split())
            if not (0 <= row < size and 0 <= col < size):
                raise ValueError("Координаты вне диапазона!")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            continue

        logging.info(f"Игрок выбрал клетку ({row}, {col}).")
        moves.append((row, col, time.strftime("%Y-%m-%d %H:%M:%S")))

        if board[row][col] == "X":
            print("Вы подорвались на мине! Игра окончена.")
            logging.info("Игрок проиграл.")
            os.remove("minesweeper_save.json")  # Удаляем сохранение, так как игра окончена
            break
        else:
            revealed[row][col] = True
            save_game({"board": board, "revealed": revealed, "moves": moves})

        if all(revealed[row][col] or board[row][col] == "X" for row in range(size) for col in range(size)):
            print("Поздравляем! Вы выиграли!")
            logging.info("Игрок победил.")
            os.remove("minesweeper_save.json")
            break


if __name__ == "__main__":
    play_game()
