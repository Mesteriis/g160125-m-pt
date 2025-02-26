# Продемонстрируйте и объясните в режиме live-coding:
# - Упаковку аргументов с args для списков и кортежей
from icecream import ic as print
# def my_func(*args):
#     for el in args:
#         print(el)
#
# def my_func2(a,b,c,d,e):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)
#
# # my_func(1,2,3,4,5)
#
# tuple_ = (1, 2, 3, 4, 5)
#
# my_func(tuple_)
# my_func(*tuple_)  # (1, 2, 3, 4, 5) -> 1, 2, 3, 4, 5
#
# # - Упаковку аргументов с kwargs для словарей
# def my_func3(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
# dict_ = {'name': 'Tom', 'age': 30, 'city': 'Moscow'}
# # * {'name': 'Tom', 'age': 30, 'city': 'Moscow'} -> ('name','Tom'), ('age',30), ('city','Moscow')
# # ** {'name': 'Tom', 'age': 30, 'city': 'Moscow'} -> name='Tom', age=30, city='Moscow'
#
# my_func3(**dict_)
# my_func3(name='Tom', age=30, city='Moscow')
#
#
#
#





# Продемонстрируйте в режиме live-coding и объясните работу:
# # - Глобальных и локальных переменных
# x = 10
#
# def my_func():
#     global x
#     x = 20
#     print(x)
#
# my_func()
# print(x)
# y = 10
# def my_func2():
#     y = 20
#     def my_func3():
#         global y
#         y = 30
#         print(y)
#     my_func3()
#     print(y)
#
# my_func2()
# print(y)


# - Ключевых слов global и nonlocal
# В- ложенных функций
# - Замыкания

# def outer_func(x):
#     def inner_func(y):
#         print(x + y) # print(10 + y)
#     return inner_func
# count = 1
# count += 1
# count += 1
# count += 1
# count += 1
# print(count)
# add_ten = outer_func(count)
# count += 1
# count += 1
# count += 1
# count += 1
# count += 1
# add_ten(10)

