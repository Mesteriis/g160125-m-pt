# # Задание 1: Реализация геттера и сеттера для класса Person
# # Описание:
# #
# # Создайте класс Person, который будет иметь приватные атрибуты name и age.
# # Реализуйте геттеры и сеттеры для этих атрибутов без использования декораторов.
# #
# # Требования:
# #
# # Приватные атрибуты __name и __age.
# # Методы get_name и set_name для доступа и изменения атрибута __name.
# # Методы get_age и set_age для доступа и изменения атрибута __age.
# # Проверка, что возраст не может быть отрицательным.
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age if age >= 0 else 0
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if age >= 0:
#             self.__age = age
#         else:
#             print("Возраст не может быть отрицательным")
# # Задание 2: Реализация геттера и сеттера для класса Rectangle
# # Описание:
# #
# # Создайте класс Rectangle, который будет иметь приватные атрибуты width и height.
# # Реализуйте геттеры и сеттеры для этих атрибутов без использования декораторов.
# #
# # Требования:
# #
# # Приватные атрибуты __width и __height.
# # Методы get_width и set_width для доступа и изменения атрибута __width.
# # Проверка, что ширина должна быть положительной.
# # Методы get_height и set_height для доступа и изменения атрибута __height.
# # Проверка, что высота должна быть положительной.
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height
#
#     def get_width(self):
#         return self.__width
#
#     def set_width(self, width):
#         if width > 0:
#             self.__width = width
#         else:
#             print("Ширина должна быть положительной")
#
#     def get_height(self):
#         return self.__height
#
#     def set_height(self, height):
#         if height > 0:
#             self.__height = height
#         else:
#             print("Высота должна быть положительной")
