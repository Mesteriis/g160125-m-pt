# Тема: функции
#
# Покажите в формате live-coding и объясните:
# - Процесс создания и вызова функции.
# - Использование оператора return для возврата значения из функции.
# - Использования именованных аргументов, что делает вызов функции более гибким.
from typing import Any
from icecream import ic as print

def is_even(num: int) -> bool:
    return num % 2 == 0

def my_print(var: Any):
    print(var)

def my_sum(a: int, b: int) -> int:
    return a + b




def person_desc(name: str, age: int, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

person_desc("tom", 30, "Moscow", "Developer", married=True, children=3)
# person_desc("tom", 30, "Moscow", "Developer", married=True, children=3)


# Тема: args, kwargs
#
# Покажите в формате live-coding и объясните:
# - Как работать с произвольным числом параметров с помощью args и *kwargs.
