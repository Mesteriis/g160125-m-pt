# Игра: Камень, ножницы, бумага
#
# Создайте игру "Камень, ножницы, бумага", где пользователь играет против компьютера.
# Компьютер случайным образом выбирает одно из трех значений: камень, ножницы или бумагу.
# Пользователь вводит свой выбор, и программа определяет победителя. Если выборы одинаковы, игра объявляет ничью.
# Игра продолжается до тех пор, пока один из игроков (пользователь или компьютер)
# не одержит на три победы больше, чем соперник. В конце показывается итоговый счет и объясляется победитель.

import random


def get_computer_choice() -> str:
    return random.choice(["камень", "ножницы", "бумага"])


def determine_winner(user_choice: str, computer_choice: str) -> int:
    """Определяет победителя раунда.
    Возвращает 1, если пользователь выиграл, -1 если компьютер, 0 если ничья."""
    winning_cases = {
        "камень": "ножницы",
        "ножницы": "бумага",
        "бумага": "камень"
    }
    if user_choice == computer_choice:
        return 0
    elif winning_cases[user_choice] == computer_choice:
        return 1
    else:
        return -1


def play_game():
    user_score = 0
    computer_score = 0
    win_margin = 3
    item = ["камень", "ножницы", "бумага"]
    while abs(user_score - computer_score) < win_margin:
        user_choice = int(input("Введите ваш выбор (1 -камень, 2-ножницы, 3-бумага): ").strip().lower())
        if user_choice not in [1,2,3]:
            print("Некорректный ввод. Попробуйте снова.")
            continue

        user_choice = item[user_choice - 1]
        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice)
        if result == 1:
            user_score += 1
            print("Вы выиграли раунд!")
        elif result == -1:
            computer_score += 1
            print("Компьютер выиграл раунд!")
        else:
            print("Ничья!")

        print(f"Счет: Вы {user_score} - {computer_score} Компьютер\n")

    if user_score > computer_score:
        print("Поздравляем! Вы выиграли игру!")
    else:
        print("Компьютер победил в этой игре. Удачи в следующий раз!")


if __name__ == "__main__":
    play_game()

