# Тема: Список, срезы списков.
#from tabnanny import process_tokens
from random import choice

# Упражнение 1: Управление списком покупок
# Создайте список покупок, содержащий элементы "bread", "milk", "eggs".
orders = ["bread", "milk", "eggs"]
print(orders)
# Измените элемент "milk" на "almond milk".
orders[1]="almond milk"
print(orders)
# Создайте срез, содержащий первые два элемента списка.
slice_orders = orders[0:2]
print(slice_orders)
# Создайте вложенный список, где каждый элемент списка покупок будет содержать его цену.
detailed_shopping_list = [
                        ["bread", 1.5],
                        ["almond milk", 3.0],
                        ["eggs", 2.0]
]
print(detailed_shopping_list)

# Выведите список покупок, срез и вложенный список.
# print(shopping_list)  # Ожидаемый результат: ["bread", "almond milk", "eggs"]
# print(slice_shopping_list)  # Ожидаемый результат: ["bread", "almond milk"]
# print(detailed_shopping_list)  # Ожидаемый результат: [["bread", 1.5], ["almond milk", 3.0], ["eggs", 2.0]]


# Упражнение 2: Управление списком студентов и их оценок
# Создайте список студентов, содержащий элементы "Alice", "Bob", "Charlie", "David".
students = ["Alice", "Bob", "Charlie", "David"]
print(students)
# Измените имя второго студента на "Eve".
#students[2-1] = "Eve"
#print(students)
# Создайте срез, содержащий студентов: "Bob", "Charlie".
top_students = students[1:3]
print(top_students)
# Создайте вложенный список, где каждый студент имеет список своих оценок.
students[2-1] = "Eve"
student_grades = [
    [students[0], [90,85,88]],
    [students[1], [75,80,82]],
    [students[2], [95,92,93]],
    [students[3], [78,85,84]]
]
print(student_grades)
# Выведите список студентов, срез и вложенный список.
# print(students)  # Ожидаемый результат: ["Alice", "Eve", "Charlie", "David"]
# print(top_students)  # Ожидаемый результат: ["Bob", "Charlie"]
# print(student_grades)  # Ожидаемый результат:
# [["Alice", [90, 85, 88]], ["Eve", [75, 80, 82]], ["Charlie", [95, 92, 93]], ["David", [78, 85, 84]]]


# Упражнение 3: Управление списком задач
# Создайте список задач, содержащий элементы "task1", "task2", "task3", "task4.
tasks = ["task1", "task2", "task3", "task4"]
print (tasks)
# Измените третью задачу на "task3 updated".
tasks [2] = "task3 updated"
print(tasks)
# Создайте срез, содержащий последние две задачи.
last_tasks = tasks[-2][-1]
print(last_tasks)

# Создайте вложенный список, где каждая задача имеет свой статус
# (True - выполнено, False - не выполнено).
tasks [2] = "task3"
detailed_tasks = [
    [tasks[0], True],
    [tasks[1], False],
    [tasks[2], True],
    [tasks[3], False]
    ]
print(detailed_tasks)
# Выведите список задач, срез и вложенный список.
# print(tasks)  # Ожидаемый результат: ["task1", "task2", "task3 updated", "task4"]
# print(last_tasks)  # Ожидаемый результат: ["task3", "task4"]
# print(detailed_tasks)  # Ожидаемый результат:
# [["task1", True], ["task2 updated", False], ["task3", True], ["task4", False]]


# Тема: Методы списков

# Упражнение 1: Управление списком фильмов и их рейтингов
# 1.1 Создайте список фильмов, содержащий элементы "Movie1", "Movie2", "Movie3".
movie_list = ["Movie1", "Movie2", "Movie3"]
# 1.2 Пропишите условие: добавить в список фильм "Movie4", если его еще нет в списке. 1:41
if "Movie 4" not in movie_list:
    movie_list.append ("Movie 4")
print(movie_list)
# 1.3 Пропишите условия: если количество фильмов больше 2, то название второго фильма меняется на "Updated Movie2".
if len(movie_list) > 2:
    movie_list[1] = "Updated Movie2"
print(movie_list)
# Если количество фильмов меньше 5, то объедините имеющийся список с новым списком ["Movie5", "Movie6", "Movie7"]
movie_list2 = ["Movie5", "Movie6", "Movie7"]
print(movie_list2)
if len(movie_list) < 5:
    movie_list.extend(movie_list2)
print(movie_list)

# 1.4 Создайте вложенный список, где каждый фильм имеет свой год выпуска и рейтинг:
movie_details = [
    ["Movie1", 2010, 8.1],
    ["Updated Movie2", 2015, 7.5],
    ["Movie3", 2020, 8.6],
    ["Movie4", 2021, 7.9],
    ["Movie5", 2013, 8.5],
    ["Movie6", 2018, 8.6],
    ["Movie7", 2023, 7.0]]
print(movie_details)

# ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5], ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9], ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]
# 1.5 Добавьте фильм ["Movie", 2002, 7.7] в начало вложенного списка.
movie_details.insert (0, ["Movie", 2002, 7.7])
print(movie_details)
# 1.6 Выведите список фильмов и вложенный список.
# print(movie_list)  #  "Movie1", "Movie2", "Movie3", "Movie4", "Movie5", "Movie6", "Movie7"
# print(movie_details)  # Ожидаемый результат: [["Movie", 2002, 7.7], ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5],
# ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9], ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]]


# Упражнение 2: Анализ списка курсов и их продолжительности
# 2.1 Создайте список курсов, содержащий элементы "Python", "Java", "JavaScript".
cours_list = ["Python", "Java", "JavaScript"]

# 2.2 Добавьте в список курс "C++".
cours_list.append("C++")
print(cours_list)
# 2.3 Измените название второго курса на "Kotlin".
cours_list[1] = "Kotlin"
print(cours_list)
# 2.4 Если первые три курса "Python", "Kotlin", "JavaScript", то создайте срез, содержащий первые три курса.
if cours_list[0:3] == ["Python", "Kotlin", "JavaScript"]:
    print(cours_list,"done")
# 2.5 Отсортируйте курсы по названиям.
cours_list.sort()
print(cours_list)
# 2.6 Cоздайте вложенный список, где каждый курс имеет свою продолжительность в часах.
# ["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]

# 2.7 Выполните сложение часов всех курсов во вложенном списке и выведите общую продолжительность всех курсов.
courses_time = [["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]]
print(courses_time)
courses_hours_sum = courses_time[0][1]+courses_time[1][1]+courses_time[2][1]+courses_time[3][1]
print("всего", courses_hours_sum, "часов")
# 2.8 Выведите в консоль:
# - отсортированный список курсо, # Ожидаемый результат:['C++', 'JavaScript', 'Kotlin', 'Python']
# - срез, # Ожидаемый результат: ['Python', 'Kotlin', 'JavaScript']
# - вложенный список, # Ожидаемый результат: [['Python', 40], ['Kotlin', 30], ['JavaScript', 35], ['C++', 50]]
# - общую продолжительность всех курсов. # Ожидаемый результат: 155


# Мини-проект: Система управления задачами (To-Do List)

# Описание проекта:
# Создайте простую систему управления задачами, которая позволяет пользователям
# добавлять, удалять, и отмечать задачи как выполненные.
#
# Требования:
# 1. Программа должна запрашивать у пользователя ввод задачи.
# Программа должна преобразовывать введенную пользователем
# задачу в список,
# где первым элементом идет номер задачи,
# вторым задача, а третьим статус ее выполнения.
# При создании задачи статус всегда False.
# Список с задачей добавляется во вложенный список со всеми задачами tasks.

# 2. Программа должна выводить список задач.



# 3. Пользователь должен иметь возможность отметить задачу как выполненную.
# Для этого программа должна запросить у него
# номер задачи. Если такого номера нет, то вывести сообщение
# "Некорректный номер задачи.".
# Если номер корректный, то поменять статус задачи на True.

# 4. Пользователь должен иметь возможность удалить задачу.
# Чтобы удалить задачу, запросите ее номер.
# Если номер корректный, то удалите ее.
#
tasks = []
# #
while True:
     # В решении используется цикл, чтобы программа работала пока вы ее принудительно не завершите через Ctr-C.
      # Циклы вы еще не проходили и для решения задачи эти знания не нужны. Просто пишите код с отступом, продолжая программу.
    print("\nСистема управления задачами")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    choice = input("Выберите действие, введя его номер: ")
    if choice == "1":
        task = input("Введите задачу: ")
        tasks.append([len(tasks)+1, task, False])
    elif choice == "2":
        print(tasks)
    elif choice == "3":
        task = int(input("Введите номер задачи: "))
        tasks [task -1][2] = True
    elif choice == "4":
        task_number = int(input ("введите номер задачи"))
        tasks.pop (task_number -1)
    else:
        print("Nekoerektny Vvod")




