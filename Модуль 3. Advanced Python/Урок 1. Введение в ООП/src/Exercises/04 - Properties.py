# Ex 1
# Создайте класс `Employee` с приватными атрибутами `__name` и `__salary`.
# Реализуйте геттеры и сеттеры для этих атрибутов, добавив проверку,
# что зарплата не может быть ниже минимальной зарплаты (например, 10000).
# class Employee:
#
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def set_name(self, name):
#         self.__name = name
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def set_salary(self, salary):
#         if salary > 10000:
#             self.__salary = salary
#
# employee = Employee("John", 12000)
# print(employee.name, employee.salary)

# Ex 2
# Создайте класс `Circle` с приватным атрибутом `__radius`.
# Реализуйте свойства (property) для получения и установки значения радиуса,
# а также метод для вычисления площади круга.

# class Circle:
#
#     def __init__(self, radius):
#         self.__radius = radius
#
#     @property
#     def radius(self):
#         return self.__radius
#
#     @property
#     def circle_square(self):
#         return 3.14 * (self.__radius * self.__radius)
#
# circle = Circle(5)
# print(circle.circle_square)