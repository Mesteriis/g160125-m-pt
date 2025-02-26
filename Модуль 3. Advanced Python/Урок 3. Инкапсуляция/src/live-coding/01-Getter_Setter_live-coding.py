class Car:
    def __init__(self, model, year):
        self.__model = model  # Приватный атрибут
        self.__year = year    # Приватный атрибут

    def get_model(self):
        return self.__model

    def set_model(self, model):
        if isinstance(model, str):
            self.__model = model
        else:
            raise ValueError("Model must be a string")

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if self.__year:
            raise ValueError("Year has already been set")
        if isinstance(year, int) and year > 1885:  # Первый автомобиль был создан в 1886 году
            self.__year = year
        else:
            raise ValueError("Year must be greater than 1885")


def main():
    car = Car("Toyota", None)
    print(car.get_model())  # Output: Toyota
    car.set_year(2021)
    print(car.get_year())  # Output: 2021
    car.set_year(2022)
    print(car.get_year())  # Output: 2021


if __name__ == "__main__":
    main()
