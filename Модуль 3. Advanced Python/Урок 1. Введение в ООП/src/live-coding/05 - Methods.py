# Методы классов в Python — это функции, которые определены внутри класса и
# предназначены для выполнения действий с объектами этого класса.
# Методы могут взаимодействовать с атрибутами класса и его экземпляров.
#
# Типы методов классов:
# Обычные методы (Instance Methods)
# Методы класса (Class Methods)
# Статические методы (Static Methods)

# Обычные методы (Instance Methods)
# Обычные методы работают с экземплярами класса и имеют доступ к их атрибутам.
# Первый параметр таких методов — это всегда self,
# который ссылается на текущий экземпляр класса.

# Методы класса (Class Methods)
# Методы класса работают с самим классом, а не с его экземплярами.
# Первый параметр таких методов — это cls, который ссылается на сам класс.
# Методы класса обозначаются декоратором @classmethod.

# Статические методы (Static Methods)
# Статические методы не имеют доступа ни к атрибутам экземпляра (self), ни к атрибутам класса (cls).
# Они функционируют как обычные функции, но принадлежат классу. Обозначаются декоратором @staticmethod.

from icecream import ic as print


def is_motorized():
    return True
class Car:
    wheels = 4

    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Model: {self.model}, Year: {self.year}, {self.wheels}")

    @classmethod
    def change_wheels(cls, new_wheels):
        cls.wheels = new_wheels

    @staticmethod
    def is_motorized():
        return True




def main():
    car1 = Car("Toyota", 2020)
    car2 = Car("BMW", 2019)

    print('Instance methods')
    car1.display_info()
    car2.display_info()

    print('\nClass methods')
    Car.change_wheels(6)
    print(Car.wheels)  # Output: 6
    print('Instance methods')
    car1.display_info()
    car2.display_info()

    print('\nStatic methods')
    print(Car.is_motorized())  # Output: True
    print(is_motorized())  # Output: True


if __name__ == "__main__":
    main()
