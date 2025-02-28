# Создайте класс BankAccount, который будет представлять банковский счет. Класс должен включать следующие функции:
#
# Инкапсуляция: Приватные атрибуты для номера счета и баланса.
# Конструктор: Метод для инициализации объекта с номером счета и начальным балансом.
# Геттеры и сеттеры: Методы для доступа и изменения баланса.
# Магические методы: Методы для добавления и снятия денег (__add__ и __sub__),
# сравнения балансов (__eq__, __lt__, __le__, и т.д.), строкового представления (__str__ и __repr__),
# и вызова объекта (__call__).

class BankAccount:
    def __init__(self, account_name, balance):
        self.__account_name = account_name
        self.__balance = balance

    def get_account_name(self):
        return self.__account_name

    def set_account_name(self, account_name):
        if isinstance(account_name, str):
            self.__account_num = account_name
        else:
            raise ValueError("Account name must be string values!")

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            raise ValueError("Use number values!")

    def __add__(self, deposit):
        if isinstance(deposit, int):
            self.__balance += deposit
        else:
            raise ValueError("Use numbers!")

    def __sub__(self, withdraw):
        if isinstance(withdraw, int):
            if self.__balance > withdraw:
                self.__balance -= withdraw
            else:
                raise ValueError("Not enough money on balance!")

    def __eq__(self, other):
        return (self.__account_name, self.__balance) == (other.__account_name, other.__balance)

    def __lt__(self, other):
        return (self.__account_name, self.__balance) < (other.__account_name, other.__balance)

    def __le__(self, other):
        return (self.__account_name, self.__balance) <= (other.__account_name, other.__balance)

    def __gt__(self, other):
        return (self.__account_name, self.__balance) > (other.__account_name, other.__balance)

    def __ge__(self, other):
        return (self.__account_name, self.__balance) >= (other.__account_name, other.__balance)

    def __repr__(self):
        return f"Client '{self.__account_name}' has balance={self.__balance}"

    def __str__(self):
        return f"{self.__balance + self.__balance}"

    def __call__(self, *args, **kwargs):
        print(f"Client1 balance called: {self.__balance}")

client1 = BankAccount("Richman", 1000)
client2 = BankAccount("Looser", 100)

client1.get_account_name()
client1.set_account_name("Richest man")
client1.get_balance()
client1.set_balance(2000)
client2.__add__(200)
client1.__sub__(100)

print("Client:",client1.get_account_name())
print("Current balance:",client1.get_balance())
print("Client:",client2.get_account_name())
print("Current balance:",client2.get_balance())

print(client1 == client2)
print(client1 < client2)
print(client1 <= client2)
print(client1 > client2)
print(client1 >= client2)

print(client1.__repr__(), client2.__repr__())
print(client1.__str__())
print(client2.__call__())