# Напишите класс Vector, который реализует методы математических операций и сравнения


class Vector:
    def __init__(self, *coords):
        self.coords = coords

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors must have the same dimension")
        return Vector(*(a + b for a, b in zip(self.coords, other.coords)))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors must have the same dimension")
        return Vector(*(a - b for a, b in zip(self.coords, other.coords)))

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(*(a * scalar for a in self.coords))
        return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Dot product works only with vectors")
        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors must have the same dimension")
        return sum(a * b for a, b in zip(self.coords, other.coords))

    def length(self):
        return (sum(x * x for x in self.coords)) ** 0.5

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.coords == other.coords

    def __lt__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.length() < other.length()

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __repr__(self):
        return f"Vector{self.coords}"
