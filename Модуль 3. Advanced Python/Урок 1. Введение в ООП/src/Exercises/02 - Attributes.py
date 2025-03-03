# Ex 1
# Создайте класс `Library`, у которого будет атрибут класса `total_books` и
# атрибут объекта `books` (список книг в данной библиотеке).
# Реализуйте методы для добавления книги в библиотеку и вывода общего количества книг во всех библиотеках.
#
# Ex 2
# Создайте класс `Company` с атрибутом класса `company_name` и
# атрибутом объекта `employees` (список сотрудников).
# Реализуйте методы для добавления сотрудника и вывода списка всех сотрудников данной компании.
# class Library:
#     total_books = 0
#
#     def __init__(self,books):
#         self.books = books
#
#     def get_books(self):
#         return self.total_books
#
#     def add (self,book):
#         self.books.append(book)
# def main:
#


class Company:
    company_name:str

    def __init__(self,employees):
        self.employees = employees

    def add (self,employee):
        self.employees.append(employee)
