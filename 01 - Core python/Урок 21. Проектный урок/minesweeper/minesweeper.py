import random
import json
import os
import logging

SAVE_FILE = "save_game.json"
LOG_FILE = "game_log.txt"

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

SIZE = 5
MINES = 5


def save_game(state):
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(state, file, ensure_ascii=False, indent=4)
        logging.info("Игра сохранена: %s", state)
    except Exception as e:
        logging.error("Ошибка сохранения игры: %s", e)


def load_game():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            logging.error("Ошибка загрузки сохраненной игры.")
    return None


def create_board(size, mines):
    board = [['-' for _ in range(size)] for _ in range(size)]
    mine_positions = set()

    while len(mine_positions) < mines:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        mine_positions.add((row, col))

    return board, mine_positions


def count_adjacent_mines(row, col, mine_positions, size):
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if (r, c) in mine_positions and 0 <= r < size and 0 <= c < size:
                count += 1
    return count


def display_board(board):
    print("\nТекущее поле:")
    for row in board:
        print(' '.join(row))
    print()


def reveal_empty_cells(row, col, board, mine_positions, revealed, size):
    if (row, col) in revealed or not (0 <= row < size and 0 <= col < size):
        return

    revealed.add((row, col))
    adjacent_mines = count_adjacent_mines(row, col, mine_positions, size)
    board[row][col] = str(adjacent_mines) if adjacent_mines > 0 else " "

    if adjacent_mines == 0:
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                reveal_empty_cells(r, c, board, mine_positions, revealed, size)


def play_game():
    game_data = load_game()

    if game_data:
        board = game_data["board"]
        mine_positions = set(tuple(pos) for pos in game_data["mine_positions"])
        revealed = set(tuple(pos) for pos in game_data["revealed"])
        print("Загружена сохраненная игра.")
    else:
        board, mine_positions = create_board(SIZE, MINES)
        revealed = set()

    while len(revealed) < SIZE * SIZE - MINES:
        display_board(board)

        try:
            row, col = map(int, input("Введите координаты клетки (строка столбец): ").split())
            row -= 1
            col -= 1
        except ValueError:
            print("Ошибка ввода. Введите два числа через пробел.")
            continue

        if not (0 <= row < SIZE and 0 <= col < SIZE):
            print("Некорректные координаты. Попробуйте снова.")
            continue

        if (row, col) in mine_positions:
            print("Вы проиграли! Вы попали на мину.")
            board[row][col] = "*"
            display_board(board)

            if os.path.exists(SAVE_FILE):
                os.remove(SAVE_FILE)

            return

        if (row, col) not in revealed:
            reveal_empty_cells(row, col, board, mine_positions, revealed, SIZE)

        save_game({"board": board, "mine_positions": list(mine_positions), "revealed": list(revealed)})

    print("Поздравляем! Вы открыли все безопасные клетки.")
    display_board(board)
    os.remove(SAVE_FILE)


if __name__ == "__main__":
    play_game()
