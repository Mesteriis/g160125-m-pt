### Тема: Рекурсия

# 1. Напишите функцию `is_palindrome(s)`, которая проверяет, является ли строка `s` палиндромом
# (порядок букв одинаковый при чтении слева направо и справа налево) с помощью рекурсии.
# Пример использования:
# print(is_palindrome("radar"))  # Вывод: True
# print(is_palindrome("hello"))  # Вывод: False
# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome(s[1:-1])
#
# print(is_palindrome("radar"))
# print(is_palindrome("hello"))


# 2. Напишите функцию `find_max(lst)`,
# которая возвращает максимальный элемент в списке `lst`
# с помощью рекурсии.
# Пример использования:
# print(find_max([1, 5, 3, 9, 2]))  # Вывод: 9
# def find_max(lst):
#     if len(lst) == 1:
#         return lst[0]
#     return max(lst[0], find_max(lst[1:]))
#
# print(find_max([1, 5, 3, 9, 2]))


# 3. Напишите функцию `find_min`, которая возвращает минимальный элемент в списке `lst` с помощью рекурсии.
# Пример использования:
# print(find_min([4, 2, 8, 1, 5]))  # Вывод: 1
def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    return min(lst[0],find_min[1:])

print(find_min([4, 2, 8, 1, 5]))  # Вывод: 1
