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

import datetime

now = datetime.datetime.now()
print(now)

import random

def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "ничья"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        return "пользователь"
    else:
        return "компьютер"

def play_game():
    user_score = 0
    computer_score = 0
    winning_difference = 3

    while abs(user_score - computer_score) < winning_difference:
        user_choice = input("Введите свой выбор (камень, ножницы, бумага): ").strip().lower()
        if user_choice not in ["камень", "ножницы", "бумага"]:
            print("Неверный выбор, попробуйте снова.")
            continue

        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)
        if winner == "пользователь":
            user_score += 1
            print("Вы выиграли этот раунд!")
        elif winner == "компьютер":
            computer_score += 1
            print("Компьютер выиграл этот раунд!")
        else:
            print("Этот раунд закончился ничьей!")

        print(f"Счет: Пользователь {user_score} - Компьютер {computer_score}")

    if user_score > computer_score:
        print("Поздравляем! Вы победили в игре!")
    else:
        print("Компьютер победил в игре. Попробуйте снова!")

play_game()





