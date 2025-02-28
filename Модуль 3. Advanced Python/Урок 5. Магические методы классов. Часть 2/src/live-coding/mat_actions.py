class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        # raise ValueError("You can only add Vector instance")

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

class Vector3d:
    def __init__(self, x, y, z):
        self.x = x
        self.yy = y
        self.z = z

def main():
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    v3 = Vector3d(1, 2, 3)
    print(v1 + v3)  # Output: Vector(4, 5)
    print(v1 - v2)  # Output: Vector(0, 3)
    print(v1 * 3)  # Output: Vector(6, 12)
    print(v1 / 2)  # Output: Vector(1.0, 2.0)

main()