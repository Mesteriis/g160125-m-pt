# Ex 1
# Создайте базовый класс `Person` с атрибутами `name` и `age`.
# Затем создайте два производных класса `Student` и `Teacher`.
# Класс `Student` должен иметь дополнительный атрибут `student_id`, а класс `Teacher` — атрибут `subject`.
# Реализуйте методы для вывода информации о каждом объекте.

# Ex 2
# Создайте класс `Vehicle` с атрибутами `make` и `model`.
# Создайте производный класс `Car` с дополнительным атрибутом `num_doors` (количество дверей) и
# производный класс `Motorcycle` с атрибутом `has_sidecar` (имеет ли мотоцикл коляску).
# Реализуйте метод, который выводит полное описание транспортного средства.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id
        print(f"Класс персона __init__(student_id = {self.student_id})")

class Teacher(Person):
    def __init__(self,name,age,subject):
        super.__init__(name,age)
        self.subject = subject
        print(f"Class Person __init__(subject = {self.subject})")


class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model


class Car(Vehicle):
    def __init__(self,make,model,num_doors):
        super().__init__(make,model)
        self.num_doors = num_doors
        print(f"Class Venicle __init__(num_doors={self.num_doors})")

class Motorcycle(Vehicle):
    def __init__(self,make,model,has_sidecar):
        super().__init__(make,model)
        self.has_sidecar = has_sidecar
        print(f"Class Venicle __init__(has_sidecar = {self.has_sidecar})")


def main():
    pass  # you code here


if __name__ == '__main__':
    main()
