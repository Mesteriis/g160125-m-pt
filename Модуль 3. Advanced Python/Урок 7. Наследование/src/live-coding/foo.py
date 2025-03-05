from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def get_salary1(self):
        pass

    @abstractmethod
    def get_salary2(self):
        pass

    @abstractmethod
    def get_salary3(self):
        pass

    @abstractmethod
    def get_salary4(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    def get_salary2(self):
        pass

    def get_salary3(self):
        pass

    def get_salary4(self):
        pass

    def get_salary(self):
        pass


class Engineer(Employee):
    pass


class Intern(Employee):
    pass


class SoftwareEngineer(Engineer):
    pass

m = Manager()
e = Engineer()
i = Intern()
se = SoftwareEngineer()

for el in [m, e, i, se]:
    print(el.get_salary())