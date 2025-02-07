# Тема: Дополнительная практика на рекурсию

# 1. Напишите функцию `sum_of_digits(n)`, которая возвращает сумму цифр числа `n` с помощью рекурсии.
# Пример использования:
# print(sum_of_digits(12345))  # Вывод: 15

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
def sum_of_digits(n):
    n = str(n)
    if not n:
        return 0
    return int(n[0]) + sum_of_digits(int(n[1:])) if len(n) > 1 else int(n[0])

def sum_of_digits(n):
    return sum(map(int, str(n)))
# 2. Напишите функцию `reverse_string(s)`, которая возвращает строку `s` в обратном порядке с помощью рекурсии.
# Пример использования:
# print(reverse_string("hello"))  # Вывод: "olleh"

def reverse_string(s):
    if not s:
        return s
    return reverse_string(s[1:]) + s[0]

# 3. Напишите функцию `list_length(lst)`, которая возвращает длину списка `lst` с помощью рекурсии.
# Пример использования:
# print(list_length([1, 2, 3, 4, 5]))  # Вывод: 5

def list_length(lst):
    if not lst:
        return 0
    return 1 + list_length(lst[1:])