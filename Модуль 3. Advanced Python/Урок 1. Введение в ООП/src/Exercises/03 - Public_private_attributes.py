# Ex 1
# Создайте класс `BankAccount` с публичным атрибутом `owner` и приватным атрибутом `__balance`.
# Реализуйте методы для внесения депозита и снятия денег, обеспечивая корректность операций
# (например, нельзя снять больше, чем есть на балансе).
# class BankAccount:
#     total_balance = 0
#
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#         BankAccount.total_balance += balance
#
#     def get_bal(self):
#         return self.__balance
#
#     def add_bal(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             BankAccount.total_balance += amount
#
#     def withdraw(self, amount):
#         if amount > 0:
#             if self.__balance >= amount:
#                 self.__balance -= amount
#                 BankAccount.total_balance -= amount
#             else:
#                 print("Not enough money")

# user1 = BankAccount("Max", 100)
# print(f"Balance Max: {user1.get_bal()}")
#
# user1.add_bal(200)
# print(f"Balance Max: {user1.get_bal()}")
#
# user1.withdraw(50)
# print(f"Current Balance Max: {user1.get_bal()}")
#
# user1.withdraw(1000)
# print(f"Balance change to: {user1.get_bal()}")

# Ex 2
# Создайте класс `Product` с публичным атрибутом `name` и приватным атрибутом `__price`.
# Реализуйте методы для получения и изменения цены,
# добавив проверки на корректность (цена не может быть отрицательной).

# class Product:
#     t_price = 0
#
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#         Product.t_price += price
#
#     def get_prods_list(self):
#         return self.__price
#
#     def change_price(self, amount):
#             if amount > 0:
#                 self.__price += amount
#                 Product.t_price += amount
#             else:
#                 print("Sum must be positive")
#
# product1 = Product("Iphone", 100)
# print(f"Current product price: {product1.get_prods_list()}")
#
# product1.change_price(200)
# print(f"Product changed to: {product1.get_prods_list()}")