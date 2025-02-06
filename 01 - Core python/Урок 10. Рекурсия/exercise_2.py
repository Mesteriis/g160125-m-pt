# Тема: Дополнительная практика на рекурсию

# # 1. Напишите функцию `sum_of_digits(n)`, которая возвращает сумму цифр числа `n` с помощью рекурсии.
# # Пример использования:
# # print(sum_of_digits(12345))  # Вывод: 15
# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum_of_digits(n // 10)
# print(sum_of_digits(12345))
# # 2. Напишите функцию `reverse_string(s)`, которая возвращает строку `s` в обратном порядке с помощью рекурсии.
# # Пример использования:
# # print(reverse_string("hello"))  # Вывод: "olleh"
# def reverse_string(s):
#     if len(s) <= 1:
#         return s
#     return s[-1] + reverse_string(s[:-1])
# print(reverse_string("hello"))
#

# 3. Напишите функцию `list_length(lst)`, которая возвращает длину списка `lst` с помощью рекурсии.
# Пример использования:
# print(list_length([1, 2, 3, 4, 5]))  # Вывод: 5
# def list_length(lst):
#     if not lst:
#         return 0
#     return 1 + list_length(lst[1:])
# print(list_length([1, 2, 3, 4, 5]))  # Вывод: 5
