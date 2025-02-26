# Игра: Сапёр
#
# Цель игры: открыть все клетки, не содержащие мин.
#
# Правила игры:
#
# 1. Игровое поле состоит из клеток размером 5x5.
# 2. На поле случайным образом размещены 5 мин.
# 3. Игрок вводит координаты клетки (например, "2 3" для второй строки и третьего столбца), чтобы проверить ее.
# 4. Если игрок открывает клетку с миной, он проигрывает.
# 5. Если игрок открывает клетку без мины, на этой клетке отображается число, указывающее, сколько мин находится в соседних клетках (по горизонтали, вертикали и диагоналям).
# 6. Игрок побеждает, если открывает все клетки, не содержащие мин.
#
# Пример игрового процесса:
#
# 1. Игроку показывается пустое поле:
# - - - - -
# - - - - -
# - - - - -
# - - - - -
# - - - - -
#
# 2. Игрок вводит координаты клетки:
# Введите координаты клетки (строка столбец): 2 3
#
# 3. Если в этой клетке нет мины, открывается число:
# - - - - -
# - - 1 - -
# - - - - -
# - - - - -
# - - - - -
#
# 4. Игрок продолжает вводить координаты, пока не откроет все безопасные клетки или не попадет на мину.
# 5. Если игрок открывает клетку с миной, игра заканчивается:
# - - - - -
# - - * - -
# - - - - -
# - - - - -
# - - - - -
# Вы проиграли! Вы попали на мину.
#
# 6. Если игрок открывает все клетки без мин, игра заканчивается победой:
# - 1 1 1 -
# - 1 * 1 -
# - 2 2 2 -
# - 1 * 1 -
# - 1 1 1 -
# Поздравляем! Вы открыли все безопасные клетки.
import random


def create_board(size: int, mines: int) -> tuple[list[list[str]], set[tuple[int, int]]]:
    """
    Создание игрового поля и случайное размещение мин.

    :param size: Размер поля (size x size).
    :param mines: Количество мин для размещения на поле.

    :returns tuple: Кортеж, содержащий игровое поле (список списков) и набор позиций мин (набор кортежей).
    """

    board: list[list[str]] = [['-' for _ in range(size)] for _ in range(size)]
    mine_positions: set[tuple[int, int]] = set()
    while len(mine_positions) < mines:
        row: int = random.randint(0, size - 1)
        col: int = random.randint(0, size - 1)
        mine_positions.add((row, col))
    return board, mine_positions


def count_adjacent_mines(row: int, col: int, mine_positions: set[tuple[int, int]], size: int) -> int:
    """
    Подсчет количества мин, соседствующих с данной клеткой.

    :param row: Индекс строки клетки.
    :param col: Индекс столбца клетки.
    :param mine_positions: Набор позиций мин.
    :param size: Размер поля.

    :returns int: Количество соседних мин.
    """

    count: int = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if (r, c) in mine_positions and 0 <= r < size and 0 <= c < size:
                count += 1
    return count


def display_board(board: list[list[str]]) -> None:
    """
    Отображение текущего состояния игрового поля.

    :param board: Игровое поле.
    """

    for row in board:
        print(' '.join(row))


def play_game(size: int = 5, mines: int = 5) -> None:
    """
    Игра в Сапёра.

    :param size: Размер поля (по умолчанию 5).
    :param mines: Количество мин (по умолчанию 5).
    """

    board, mine_positions = create_board(size, mines)
    revealed: set[tuple[int, int]] = set()

    while len(revealed) < size * size - mines:
        display_board(board)
        row, col = map(int, input("Введите координаты клетки (строка столбец): ").split())
        row -= 1
        col -= 1
        if not (0 <= row < size and 0 <= col < size):
            print("Некорректные координаты. Попробуйте снова.")
            continue
        if (row, col) in mine_positions:
            print("Вы проиграли! Вы попали на мину.")
            return
        if (row, col) not in revealed:
            revealed.add((row, col))
            board[row][col] = str(count_adjacent_mines(row, col, mine_positions, size))


    print("Поздравляем! Вы открыли все безопасные клетки.")
    display_board(board)


if __name__ == "__main__":
    play_game()