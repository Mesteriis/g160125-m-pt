# Игра: Камень, ножницы, бумага
#
# За основу возьмите свой код, разработанный в предыдущем проектном уроке, посвященном Game Hub (урок 13).
# Если в тот раз вы не реализовали весь функционал, то сначала реализуйте полностью игру, а затем переходите
# к рефакторингу на основе заданий из этого урока.
#
# Рефакторинг
# - Добавить логирование действий пользователя с использованием модуля `datetime`.
# В файл записывается время начало игры, время и значения ходов компьютера и пользователя,
# время окончания игры и результат.
# - Добавить обработку ошибок с использованием `try/except`, где это необходимо.
# - Использовать генераторы для создания последовательности ходов компьютера.



# АЛЕКСАНДР!!! Я - РАЗГИЛЬДЯЙ И ЛЕНТЯЙ!



import random
import datetime


def computer_moves():
    """Генератор ходов компьютера."""
    choices = ['камень', 'ножницы', 'бумага']
    while True:
        yield random.choice(choices)


def log_game(data):
    """Запись данных игры в лог-файл."""
    with open("game_log.txt", "a", encoding="utf-8") as file:
        file.write(data + "\n")


def determine_winner(user, computer):
    """Определение победителя."""
    if user == computer:
        return "Ничья"
    elif (user == 'камень' and computer == 'ножницы') or \
            (user == 'ножницы' and computer == 'бумага') or \
            (user == 'бумага' and computer == 'камень'):
        return "Пользователь победил"
    else:
        return "Компьютер победил"


def main():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    log_game(f"Начало игры: {datetime.datetime.now()}")

    computer_move_gen = computer_moves()

    while True:
        try:
            user_move = input("Введите камень, ножницы или бумага (или 'выход' для завершения): ").lower()
            if user_move == 'выход':
                break
            if user_move not in ['камень', 'ножницы', 'бумага']:
                raise ValueError("Некорректный ввод. Попробуйте снова.")

            computer_move = next(computer_move_gen)
            log_game(f"{datetime.datetime.now()} - Пользователь: {user_move}, Компьютер: {computer_move}")

            result = determine_winner(user_move, computer_move)
            print(f"Компьютер выбрал: {computer_move}")
            print(f"Результат: {result}")
            log_game(f"{datetime.datetime.now()} - {result}")

        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    log_game(f"Конец игры: {datetime.datetime.now()}\n")
    print("Спасибо за игру!")


if __name__ == "__main__":
    main()
