# Тема: Список, срезы списков.

# Упражнение 1: Управление списком покупок
# Создайте список покупок, содержащий элементы "bread", "milk", "eggs".
# Измените элемент "milk" на "almond milk".
# Создайте срез, содержащий первые два элемента списка.
# Создайте вложенный список, где каждый элемент списка покупок будет содержать его цену.
# Выведите список покупок, срез и вложенный список.

# shopping_list = ["bread", "milk", "eggs"]
# shopping_list[1] = "almond milk"
# slice_shop_list = shopping_list[0:2]
# detailed_shopping_list = [["bread", 1.5], ["almond milk", 3.0], ["eggs", 2.0]]
#
# print(shopping_list)  # Ожидаемый результат: ["bread", "almond milk", "eggs"]
# print(slice_shop_list)  # Ожидаемый результат: ["bread", "almond milk"]
# print(detailed_shopping_list)  # Ожидаемый результат: [["bread", 1.5], ["almond milk", 3.0], ["eggs", 2.0]]


# Упражнение 2: Управление списком студентов и их оценок
# Создайте список студентов, содержащий элементы "Alice", "Bob", "Charlie", "David".
# Измените имя второго студента на "Eve".
# Создайте срез, содержащий студентов: "Bob", "Charlie".
# Создайте вложенный список, где каждый студент имеет список своих оценок.
# Выведите список студентов, срез и вложенный список.

# stud_list = ["Alice", "Bob", "Charlie", "David"]
# stud_list[1] = "Eve"
# top_students = stud_list[1:3]                          # if I changed Bob to Eve, how I can show ["Bob", "Charlie"]?
# student_grades = [["Alice", [90, 85, 88]], ["Eve", [75, 80, 82]], ["Charlie", [95, 92, 93]], ["David", [78, 85, 84]]]
#
# print(stud_list)  # Ожидаемый результат: ["Alice", "Eve", "Charlie", "David"]
# print(top_students)  # Ожидаемый результат: ["Bob", "Charlie"]
# print(student_grades)  # Ожидаемый результат:
# # [["Alice", [90, 85, 88]], ["Eve", [75, 80, 82]], ["Charlie", [95, 92, 93]], ["David", [78, 85, 84]]]


# Упражнение 3: Управление списком задач
# Создайте список задач, содержащий элементы "task1", "task2", "task3", "task4.
# Измените третью задачу на "task3 updated".
# Создайте срез, содержащий последние две задачи.
# Создайте вложенный список, где каждая задача имеет свой статус (True - выполнено, False - не выполнено).
# Выведите список задач, срез и вложенный список.

# tasks_list = ["task1", "task2", "task3", "task4"]
# tasks_list[2] = "task3 updated"
# last_tasks = tasks_list[2:4]
# tasks_status = [["task1", True], ["task2 updated", False], ["task3", True], ["task4", False]]
# print(tasks_list)  # Ожидаемый результат: ["task1", "task2", "task3 updated", "task4"]
# print(last_tasks)  # Ожидаемый результат: ["task3", "task4"]
# print(tasks_status)  # Ожидаемый результат:
# # [["task1", True], ["task2 updated", False], ["task3", True], ["task4", False]]


# Тема: Методы списков

# Упражнение 1: Управление списком фильмов и их рейтингов
# 1.1 Создайте список фильмов, содержащий элементы "Movie1", "Movie2", "Movie3".
# 1.2 Пропишите условие: добавить в список фильм "Movie4", если его еще нет в списке.
# 1.3 Пропишите условия: если количество фильмов больше 2, то название второго фильма меняется на "Updated Movie2".
# Если количество фильмов меньше 5, то объедините имеющийся список с новым списком ["Movie5", "Movie6", "Movie7"]
# 1.4 Создайте вложенный список, где каждый фильм имеет свой год выпуска и рейтинг:
# ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5], ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9],
# ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]

# 1.5 Добавьте фильм ["Movie", 2002, 7.7] в начало вложенного списка.
# 1.6 Выведите список фильмов и вложенный список.

# movies_list1 = ["Movie1", "Movie2", "Movie3"]
# if "Movie4" not in movies_list1:
#     movies_list1.append("Movie4")
# if len(movies_list1) > 2:
#     movies_list1[1] = "Updated Movie2"
# if len(movies_list1) < 5:
#     movies_list1.extend(["Movie5", "Movie6", "Movie7"])
# detailed_movies_list = [["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5], ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9],
# ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]]
# detailed_movies_list.insert(0, ["Movie", 2002, 7.7])
# print(movies_list1)  #  "Movie1", "Movie2", "Movie3", "Movie4", "Movie5", "Movie6", "Movie7"
# print(detailed_movies_list)  # Ожидаемый результат: [["Movie", 2002, 7.7], ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5],
# # ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9], ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]]


# Упражнение 2: Анализ списка курсов и их продолжительности
# 2.1 Создайте список курсов, содержащий элементы "Python", "Java", "JavaScript".
# 2.2 Добавьте в список курс "C++".
# 2.3 Измените название второго курса на "Kotlin".

# 2.4 Если первые три курса "Python", "Kotlin", "JavaScript", то создайте срез, содержащий первые три курса.
# 2.5 Отсортируйте курсы по названиям.
# 2.6 Cоздайте вложенный список, где каждый курс имеет свою продолжительность в часах.
# ["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]

# 2.7 Выполните сложение часов всех курсов во вложенном списке и выведите общую продолжительность всех курсов.
# 2.8 Выведите в консоль:
# - отсортированный список курсо, # Ожидаемый результат:['C++', 'JavaScript', 'Kotlin', 'Python']
# - срез, # Ожидаемый результат: ['Python', 'Kotlin', 'JavaScript']
# - вложенный список, # Ожидаемый результат: [['Python', 40], ['Kotlin', 30], ['JavaScript', 35], ['C++', 50]]
# - общую продолжительность всех курсов. # Ожидаемый результат: 155

# course_list = ["Python", "Java", "JavaScript"]
#
# course_list.append("C++")
# course_list[1] = "Kotlin"
# slice_course_list = course_list[:3]
#
# if slice_course_list != ["Python", "Java", "JavaScript"]:
#     slice_course_list = course_list
#
# course_list.sort()
# detailed_courses_list =  ["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]
# courses_timing = (detailed_courses_list[0][1] + detailed_courses_list[1][1]
#                   + detailed_courses_list[2][1] + detailed_courses_list[3][1])
#
# print(course_list)
# print(slice_course_list)
# print(detailed_courses_list)
# print(courses_timing)

# Мини-проект: Система управления задачами (To-Do List)

# Описание проекта:
# Создайте простую систему управления задачами, которая позволяет пользователям
# добавлять, удалять, и отмечать задачи как выполненные.
#
# Требования:
# 1. Программа должна запрашивать у пользователя ввод задачи. Программа должна преобразовывать введенную пользователем
# задачу в список, где первым элементом идет номер задачи, вторым задача, а третьим статус ее выполнения.
# При создании задачи статус всегда False. Список с задачей добавляется во вложенный список со всеми задачами tasks.

# 2. Программа должна выводить список задач.

# 3. Пользователь должен иметь возможность отметить задачу как выполненную. Для этого программа должна запросить у него
# номер задачи. Если такого номера нет, то вывести сообщение "Некорректный номер задачи.".
# Если номер корректный, то поменять статус задачи на True.

# 4. Пользователь должен иметь возможность удалить задачу. Чтобы удалить задачу, запросите ее номер.
# Если номер корректный, то удалите ее.
#     # В решении используется цикл, чтобы программа работала пока вы ее принудительно не завершите через Ctr-C.
#     # Циклы вы еще не проходили и для решения задачи эти знания не нужны. Просто пишите код с отступом, продолжая программу.
#     # Продолжите программу ниже. Код пишите с отсутпом, как принты выше.

tasks = []

while True:

    print("\nTask control")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark as completed")
    print("4. Remove task")

    choice = input("Choose action, by entering its number: ")

    if choice == "1":
        task_name = input("Enter your task: ")                      # 0 name
        task_number = len(tasks) + 1                                # 1 nummer
        task_status = False                                         # 2 status
        tasks.append([task_name, task_number, task_status])
        print(f"Task {task_name} was added")

    elif choice == "2":
        print(tasks)

    elif choice == "3":
        if not tasks:
            print("No tasks available")
        else:
            task_number = int(input("Enter task number: "))
            for task in tasks:
                if task[1] == task_number:                                          #1
                    status_change = input("Task done? Enter Y/N: ")
                    if status_change.upper() == "Y":
                        task[2] = True                                              #2
                        print(f"Task {task_name} marked as completed")
                    else:
                        task[2] = False                                             #3
                        print(f"Task {task_name} is not completed")

    elif choice == "4":
        task_number = int(input("Enter task number for removing: "))
        for task in tasks:
            if task[1] == task_number:                                               #1
                tasks.remove(task)
                print(f"Chosen task: {task[0]} was removed!")                       #0




