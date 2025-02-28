# Напишите класс Vector, который реализует методы математических операций и сравнения
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other,Vector):
            return Vector(self.x + other.x, self.y+other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other,Vector):
            return Vector(self.x-other.x,self.y-other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar,(int,float)):
            return Vector(self.x*scalar,self.y*scalar)
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar,(int,float)):
            return Vector(self.x/scalar,self.y/scalar)
        return NotImplemented



