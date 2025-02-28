# Учебная задача: Создание класса EnhancedList с расширенной функциональностью
# Описание:
#
# Создайте класс EnhancedList, который будет вести себя как список, но с дополнительной функциональностью.
# Класс должен поддерживать следующие возможности:
#
# Логирование всех операций по установке, получению и удалению атрибутов.
# Ведение счетчика вызовов объекта.
# Функциональность функторов для добавления и умножения элементов списка.
# Реализация методов __str__, __repr__, __len__ и __abs__.
# Требования:
#
# Реализуйте методы __setattr__, __getattribute__, __getattr__ и __delattr__ для логирования операций.
# Реализуйте метод __call__ для ведения счетчика вызовов.
# Создайте классы-функторы для добавления и умножения элементов списка.
# Реализуйте класс-декоратор для логирования времени выполнения методов.
# Реализуйте методы __str__, __repr__, __len__ и __abs__.

import time


class EnhancedList:
    def __init__(self, items):
        super().__setattr__('items', items)
    #     super().__setattr__('log', [])
    #     super().__setattr__('call_count', 0)
    #
    # def __setattr__(self, name, value):
    #     self.log.append(f"Setting attribute {name} to {value}")
    #     super().__setattr__(name, value)
    #
    # def __getattribute__(self, name):
    #     log = super().__getattribute__('log')
    #     log.append(f"Getting attribute {name}")
    #     return super().__getattribute__(name)
    #
    # def __getattr__(self, name):
    #     self.log.append(f"Attribute {name} not found, error")
    #     raise ValueError(f"Attribute {name} not found")
    #
    # def __delattr__(self, name):
    #     self.log.append(f"Deleting attribute {name}")
    #     super().__delattr__(name)
    #
    # def __call__(self):
    #     self.call_count += 1
    #     print(f"Called {self.call_count} times")

    # def __str__(self):
    #     return f"EnhancedList with items: {self.items}"
    #
    def __repr__(self):
        return f"EnhancedList({self.items})"

    def __len__(self):
        return len(self.items)

    def __abs__(self):
        return EnhancedList([abs(item) for item in self.items])


def main():
    # Пример использования


    # Создание объекта EnhancedList
    elist = EnhancedList([1, -2, 3, -4])

    # Использование методов
    print(elist)  # Использование __str__ EnhancedList with items: [1, -2, 3, -4]
    # print(repr(elist))  # Использование __repr__ EnhancedList([1, -2, 3, -4])
    # print(len(elist))  # Использование __len__
    # print(abs(elist))  # Использование __abs__

    # Функторы

if __name__ == "__main__":
    main()
