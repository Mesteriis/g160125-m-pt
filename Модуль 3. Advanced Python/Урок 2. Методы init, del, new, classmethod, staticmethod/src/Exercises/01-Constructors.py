# Задание 1: Работа с методами __init__ и __del__.
# Создайте класс Book, который будет иметь атрибуты title, author и year.
# Реализуйте методы __init__ и __del__ для инициализации объектов и
# вывода сообщения при удалении объекта соответственно.
#
# Метод __init__ должен инициализировать атрибуты title, author и year.
# Метод __del__ должен выводить сообщение, содержащее название книги и автора, когда объект удаляется.
#
#
# Задание 2: Вызов конструктора базового класса.
#
# Создайте базовый класс Animal, который будет иметь атрибуты name и age.
# Затем создайте производный класс Dog, который будет наследовать от Animal и добавит атрибут breed.
# Реализуйте вызов конструктора базового класса внутри конструктора производного класса.
#
# Класс Animal должен иметь метод __init__, инициализирующий атрибуты name и age.
# Класс Dog должен наследовать от Animal и иметь свой метод __init__, который вызывает конструктор базового класса
# и инициализирует атрибут breed.

class Book(object):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def som_foon(self):
        print(f'Book: {self.title}, Author: {self.author}, Year: {self.year}')

    @classmethod
    def from_string(cls, book_string):
        title, author, year = book_string.split(',')
        return cls(title.strip(), author.strip(), int(year.strip()))

    @staticmethod
    def is_valid_year(year):
        return isinstance(year, int) and year > 0