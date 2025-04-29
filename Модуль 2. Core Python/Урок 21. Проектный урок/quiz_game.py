# Игра: Викторина
#
# За основу возьмите свой код, разработанный в предыдущем проектном уроке, посвященном Game Hub (урок 13).
# Если в тот раз вы не реализовали весь функционал, то сначала реализуйте полностью игру, а затем переходите
# к рефакторингу на основе заданий из этого урока.
#
# Рефакторинг
# - Добавить загрузку вопросов и ответов из файла JSON.
# - Добавить обработку ошибок с использованием `try/except`, где это необходимо.
# - Добавить необходимость указания имени и фамилии перед прохождением теста.
# - По итогу теста должен создаваться текстовый файл, где должно быть указано:
#     - Имя и фамилия испытуемого.
#     - Время начала и окончания теста.
#     - Общее количество вопросов, количество правильных ответов, процент выполнения теста.
#     - Все тестовые вопросы, ответы пользователя на них, правильные ответы и указание,
#     ответил пользователь правильно или нет (True, False)

import json


def load_questions_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def quiz_game():
    questions = load_questions_from_file("questions.json")
    correct_answers = 0

    for index, q in enumerate(questions, start=1):
        print(f"\n{index}. {q['question']}")
        for i, option in enumerate(q["options"], start=1):
            print(f"  {i}. {option}")

        while True:
            try:
                answer = int(input("Ваш выбор: "))
                if 1 <= answer <= len(q["options"]):
                    break
                else:
                    print("Пожалуйста, выберите вариант из списка.")
            except ValueError:
                print("Введите число от 1 до 3.")

        if answer == q["answer"]:
            print("Верно!")
            correct_answers += 1
        else:
            print("Неверно!")

    print(f"\nВы правильно ответили на {correct_answers} из {len(questions)} вопросов.")


if __name__ == "__main__":
    quiz_game()
