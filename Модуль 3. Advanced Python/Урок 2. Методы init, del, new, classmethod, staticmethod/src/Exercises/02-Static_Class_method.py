# Задание 1: Работа с методами класса.
# Создайте класс Library, который будет отслеживать количество созданных библиотек и
# хранить общее количество книг во всех библиотеках.
#
# Реализуйте атрибут класса total_books, который будет отслеживать общее количество книг во всех библиотеках.
# Реализуйте метод класса get_total_books, который будет возвращать значение total_books.
# Реализуйте метод класса add_books, который будет принимать количество книг в качестве аргумента и
# добавлять их к total_books.
# Метод __init__ должен увеличивать счетчик количества библиотек.
class Library:
    total_books = 0
    total_libraries = 0

    def __init__(self):
        Library.total_libraries += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    @classmethod
    def add_books(cls, count):
        if count > 0:
            cls.total_books += count
        else:
            print(f" Количество книг должно быть положительным числом")

library1 = Library()
library2 = Library()

Library.add_books(100)
Library.add_books(50)
print(f"Всего библиотек: {Library.total_libraries}")
print(f"Общее количество книг: {Library.get_total_books()}")
# Задание 2: Работа со статическими методами.
# Создайте класс MathOperations, который будет содержать статические методы для
# выполнения различных математических операций.
#
# Реализуйте статический метод add, который будет принимать два числа и возвращать их сумму.
# Реализуйте статический метод subtract, который будет принимать два числа и возвращать результат их вычитания.
# Реализуйте статический метод multiply, который будет принимать два числа и возвращать их произведение.
# Реализуйте статический метод divide, который будет принимать два числа и возвращать результат их деления.
# Если второе число равно нулю, метод должен возвращать сообщение об ошибке.
class MathOperations:

    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def subtract(a,b):
        return a - b

    @staticmethod
    def multiply(a,b):
        return a*b

    @staticmethod
    def divide(a,b):
        if b == 0:
            print(f"you cannot divide with 0 ")
        else:
            return a/b

print(MathOperations.add(5, 3))
print(MathOperations.subtract(10, 4))
print(MathOperations.multiply(2, 3))
print(MathOperations.divide(9, 3))
print(MathOperations.divide(5, 0))