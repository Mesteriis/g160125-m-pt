class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def update(self, row, col, symbol):
        if self.board[row][col] == ' ':
            self.board[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        for row in self.board:
            if all(cell == symbol for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == symbol for row in range(3)):
                return True

        if all(self.board[i][i] == symbol for i in range(3)) or \
                all(self.board[i][2 - i] == symbol for i in range(3)):
            return True

        return False

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Игрок 1", 'X'), Player("Игрок 2", 'O')]
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def play(self):
        while True:
            self.board.display()
            player = self.players[self.current_player_index]
            try:
                row, col = map(int, input(
                    f"{player.name} ({player.symbol}), введите строку и столбец (0-2 через пробел): ").split())
                if row not in range(3) or col not in range(3):
                    raise ValueError
            except ValueError:
                print("Неверный ввод. Попробуйте снова.")
                continue

            if self.board.update(row, col, player.symbol):
                if self.board.check_winner(player.symbol):
                    self.board.display()
                    print(f"{player.name} победил!")
                    break
                if self.board.is_full():
                    self.board.display()
                    print("Ничья!")
                    break
                self.switch_player()
            else:
                print("Эта ячейка уже занята. Попробуйте снова.")


if __name__ == "__main__":
    game = Game()
    game.play()
