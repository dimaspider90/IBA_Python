#Создайте класс и поля соответствующему вашему варианту (поля статические и динамические).
# Создайте три метода (класса, объекта и статический). Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей. ДОБАВИТЬ МЕТОДЫ КЛАССА И СТАТИЧЕСКИЕ МЕТОДЫ.
# Вар.5 Kласс Car: id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер
# Функции-члены реализуют запись и считывание полей (проверка корректности), вывода возраста машины.
# Создать список объектов. Вывести:
# a)	список автомобилей заданной марки;
# б) список автомобилей заданной модели, которые эксплуатируются больше n лет;
#Добавить: магические методы __setattr__, __str__, арифметические методы __add__ и __sub__,
# операторы сравнения __eq__ и __lt__, а также методы __new__ и __del__.

class Car:
    # Статическое поле
    car_count = 0

    def __new__(cls, *args, **kwargs):
        # Создание нового экземпляра
        instance = super(Car, cls).__new__(cls)
        return instance

    def __init__(self, car_id, brand, model, manufact_year, color, price, reg_number):
        # Динамические поля
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.manufact_year = manufact_year
        self.color = color
        self.__price = price # Инкапсуляция поля цена
        self.reg_number = reg_number
        Car.car_count += 1

    def __setattr__(self, key, value):
        # Проверка корректности при установке атрибутов
        if key == "price" and value <= 0:
            raise ValueError("Price must be a positive number")
        super().__setattr__(key, value)

    def __str__(self):
        # Строковое представление объекта
        return (f"Car({self.car_id}, {self.brand}, {self.model}, {self.manufact_year}, {self.color}, "
                f" {self.get_price()}, {self.reg_number})")

    def __add__(self, other):
        # Сложение цен двух машин
        if isinstance(other, Car):
            return self.price + other.price
        return NotImplemented

    def __sub__(self, other):
        # Вычитание цен двух машин
        if isinstance(other, Car):
            return self.price - other.price
        return NotImplemented

    def __eq__(self, other):
        # Сравнение машин по идентификатору
        if isinstance(other, Car):
            return self.car_id == other.car_id
        return NotImplemented

    def __lt__(self, other):
        # Сравнение машин по году производства
        if isinstance(other, Car):
            return self.manufact_year < other.year
        return NotImplemented

    def __del__(self):
        # Уменьшение счетчика машин при удалении объекта
        Car.car_count -= 1

    # Метод объекта
    def display_info(self):
        return (f"Car ID: {self.car_id}, Brand: {self.brand}, Model: {self.model},"
                f" Year of Manufacture: {self.manufact_year}, Color: {self.color}, Price: {self.get_price()}, "
                f"Registration number: {self.reg_number}")

    def age(self, current_year):
        return current_year - self.manufact_year

    # Статический метод
    @staticmethod
    def get_car_count():
        return f"Total number of cars: {Car.car_count}"

    # Метод класса
    @classmethod
    def create_car(cls, car_id, brand, model, manufact_year, color, price, reg_number):
        return cls(car_id, brand, model, manufact_year, color, price, reg_number)

    # Метод для фильтрации автомобилей по модели и возрасту
    @classmethod
    def filter_cars_by_model_and_age(cls, cars, model, n, current_year):
        return [car for car in cars if car.model == model and car.age(current_year) > n]

    # Инкапсулированное поле (сеттер и геттер)
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            raise ValueError("Price must be a positive number")

    def get_price(self):
        return self.__price


# Создание списка объектов
cars = [
    Car(1, "Mercedes-Benz", "CLS AMG", 2019, "Black", 57000, "1234 AA-1"),
    Car(2, "Toyota", "Corolla", 2020, "White", 19900, "5678 BB-2"),
    Car(3, "Renault", "Grand Scenic", 2019, "Silvery", 15999, "9876 CC-3"),
    Car(4, "Mercedes-Benz", "Vito", 2022, "Blue", 39500, "5432 AA-4"),
    Car(5, "Mercedes-Benz", "E-Class", 2015, "Red", 45000, "1111 AA-5"),
    Car(6, "Toyota", "Corolla", 2017, "Green", 39900, "2222 AA-6"),
]

# Пример использования для поиска модели по количеству лет эксплуатации
current_year = 2025
model_filter = "Corolla"
years_exploitation = 4

# Вывод списка машин заданного бренда
cars_brand = [car.display_info() for car in cars if car.brand == "Mercedes-Benz"]
print("Cars by Mercedes-Benz:")
for info in cars_brand:
    print(info)

# Вывод списка машин заданной модели, которые эксплуатируются больше n лет
cars_model_age = Car.filter_cars_by_model_and_age(cars, model_filter, years_exploitation, current_year)
print(f"\nCars of model '{model_filter}' that have been in operation for more than {years_exploitation} years:")
for car in cars_model_age:
    print(car.display_info())

# Вывод списка машин, выпущенных после заданного года
cars_manufact_year = [car.display_info() for car in cars if car.manufact_year > 2019]
print("\nCars manufactered after 2019:")
for info in cars_manufact_year:
    print(info)