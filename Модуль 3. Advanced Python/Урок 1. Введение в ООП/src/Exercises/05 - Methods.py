# Ex 1
# Создайте класс `Temperature` с методами для преобразования температуры из градусов Цельсия в Фаренгейты и Кельвины.
# Реализуйте методы как статические.

# class Temperature:
#     _temp:int
#
#     def __init__(self, raw_temp):
#         self._temp = raw_temp
#
#
#     def _is_fer(self):
#         if self._temp > 50:
#             return True
#         return False
#
#     @property
#     def temp_fr(self):
#         if self._is_fer():
#             return self._temp
#         return self._temp * 2 + 30
#
#     @property
#     def temp_c(self):
#         if self._is_fer():
#             return (self._temp - 30) / 2
#         return self._temp


# #### Задание 2:
# Создайте класс `Counter` с атрибутом класса `count`,
# который будет отслеживать количество созданных экземпляров класса.
# Реализуйте метод класса `get_count`, который возвращает текущее значение `count`.

# class Counter:
#     count = 0
#
#     def __init__(self):
#         Counter.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
# test1 = Counter()
# print(test1.get_count())
#
# test2 = Counter()
# print(test2.get_count())
#
# test3 = Counter()
# print(test3.get_count())

