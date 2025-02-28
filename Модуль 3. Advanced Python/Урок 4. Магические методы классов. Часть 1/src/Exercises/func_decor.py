# Задача: Создание класса-декоратора для времени выполнения функции
# Описание:
#
# Создайте класс-декоратор TimeLogger, который будет логировать время выполнения оборачиваемой функции.
# Класс должен использовать метод __call__ для измерения времени выполнения функции и вывода этой информации на экран.
#
# Требования:
#
# Класс TimeLogger должен принимать функцию в своем конструкторе.
# Метод __call__ должен измерять время выполнения функции и выводить эту информацию на экран.
# Напишите тестовый код, который демонстрирует использование этого декоратора.

import time

class TimeLogger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция '{self.func.__name__}' выполнена за {execution_time:.6f} секунд")
        return result

@TimeLogger
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

def main():
    result = example_function(1000000)
    print("Результат выполнения функции:", result)

if __name__ == '__main__':
    main()

