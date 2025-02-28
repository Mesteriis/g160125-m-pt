# Задание 1: Работа с методами __init__ и __del__.
# Создайте класс Book, который будет иметь атрибуты title, author и year.
# Реализуйте методы __init__ и __del__ для инициализации объектов и
# вывода сообщения при удалении объекта соответственно.
#
# Метод __init__ должен инициализировать атрибуты title, author и year.
# Метод __del__ должен выводить сообщение, содержащее название книги и автора, когда объект удаляется.
class Book:
    def __init__(self,title,author,year):
        self.autor = author
        self.title = title
        self.year = year
        print(f" Книга{self.title}({self.year}),автора {self.autor} инициализирована")
    def __del__(self):
        print(f"Книга{self.title} удалена")

book1 = Book("Harry Potter", "Joahn Rowling", 1989)
book2 = Book("The Lord of The Rings", "J.R.R Tolkien", 1942)
del book1
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
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Главный класс инициализирован")

class Dog(Animal):
    def __init__(self,name,age, breed):
        super().__init__(name,age)
        self.breed = breed
        print(self)

    def __str__(self):
        return f"{self.name}, {self.age}, {self.breed}"