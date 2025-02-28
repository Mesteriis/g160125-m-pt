# Напишите класс, который переопределяет все методы сравнения (__eq__, __ne__, __lt__, __le__, __gt__, __ge__)
# для сравнения объектов по нескольким критериям: сначала по имени, затем по возрасту
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y =y

    def __eq__(self, other):
        if isinstance(other,Vector):
            return self.x == other.x, self.y == other.y
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other,Vector):
            return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other,Vector):
            return (self.x**2 + self.y**2) <= (other.x**2 + other.y**2)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other,Vector):
            return (self.x**2 + self.y**2) > (other.x**2 + other.y**2)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other,Vector):
            return (self.x**2 + self.y**2) >= (other.x**2 + other.y**2)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

def main():
        # Примеры использования
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = Vector(1, 2)

    print(v1 == v2)
    print(v1 == v3)
    print(v1 != v2)
    print(v1 < v2)
    print(v1 <= v2)
    print(v1 > v2)
    print(v1 >= v2)


if __name__ == "__main__":
    main()

