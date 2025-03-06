# Создайте абстрактный класс Shape, который определяет абстрактный метод area().
# Затем создайте несколько подклассов, таких как Circle, Rectangle и Triangle,
# которые реализуют метод area() для вычисления площади соответствующих фигур.
#
# Используйте полиморфизм, чтобы создать функцию, которая принимает список фигур и выводит их площади.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        ...

class Circle(Shape):

    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return 3,14 * self.rad **2

class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b

class Triangle(Shape):

    def __init__(self, base, hide):
        self.base = base
        self.hide = hide

    def area(self):
        return 0.5*self.base*self.hide

def main():

    def print_areas(shapes):
        for shape in shapes:
            print(f"{shape.area()}")

    shapes = [Circle(3), Rectangle(3, 4), Triangle(5, 6)]
    print_areas(shapes)

if __name__ == "__main__":
    main()