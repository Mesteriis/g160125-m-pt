# Задача 1: Создание класса Student с использованием декоратора property
# Описание:
#
# Создайте класс Student, который будет иметь приватные атрибуты name и grade.
# Реализуйте геттеры и сеттеры для этих атрибутов с использованием декоратора property.
#
# Требования:
#
# Приватные атрибуты __name и __grade.
# Свойства name и grade с геттерами и сеттерами.
# В сеттере для grade реализуйте проверку, что оценка должна быть в диапазоне от 0 до 100.
class Student:
    MIN_GRADE = 0
    MAX_GRADE = 100
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self,grade):
        if self.MIN_GRADE<=grade<=self.MAX_GRADE:
            self.__grade = grade
        else:
            print("Value Error")
# Задача 2: Создание класса BankAccount с использованием декоратора property
# Описание:
#
# Создайте класс BankAccount, который будет иметь приватные атрибуты account_number и balance.
# Реализуйте геттеры и сеттеры для этих атрибутов с использованием декоратора property.
#
# Требования:
#
# Приватные атрибуты __account_number и __balance.
# Свойства account_number и balance с геттерами и сеттерами.
# В сеттере для balance реализуйте проверку, что баланс не может быть отрицательным.
#
# TODO: Добавить более сложный пример работы с @property, например отсюда
#  https://proproprogs.ru/python_oop/primer-ispolzovaniya-obektov-property
class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self,account_number):
        self.__account_number = account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,balance):
        if balance>=0:
            self.__balance = balance
        else:
            print("Value Error")
