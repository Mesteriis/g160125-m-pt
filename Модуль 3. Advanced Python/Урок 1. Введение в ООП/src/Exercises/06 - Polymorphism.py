# Ex 1
# Создайте базовый класс `Appliance` с методом `turn_on`, который должен быть переопределен в
# производных классах `WashingMachine` и `Refrigerator`.
# В каждом из производных классов метод `turn_on` должен выводить сообщение о том, что прибор включен.
# Создайте список различных приборов и продемонстрируйте полиморфизм, вызвав метод `turn_on` для каждого прибора.

# class Device:
#     state = True
#
#     def turn_on(self):
#         if self.state:
#             return "Device is on"
#         else:
#             return "Device is off"
#
# class WashingMachine(Device):
#     pass
# class Refrigerator(Device):
#     pass

# #### Задание 2:
# Создайте базовый класс `Employee` с методом `calculate_pay`,
# который должен быть переопределен в производных классах `SalariedEmployee` и `HourlyEmployee`.
# В классе `SalariedEmployee` метод должен рассчитывать ежемесячную зарплату на основе фиксированного оклада,
# а в классе `HourlyEmployee` — на основе количества отработанных часов и почасовой ставки.
# Продемонстрируйте полиморфизм, вызвав метод `calculate_pay` для объектов различных классов.

# class Employee:
#
#     def __init__(self, salary):
#         self.salary = salary
#
#     def calculate_pay(self, days_count):
#         return (self.salary / 30) * days_count
#
# class SalariedEmployee(Employee):
#     pass

# class HourlyEmployee(Employee):
#     pass