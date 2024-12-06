## class and instance
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.make} {self.model}'s engine is starting")


toyota_car = Car("Toyota", "Camry", 2022)
audi_car = Car("Audi", "Q7", 2023)
toyota_car.start_engine()
audi_car.start_engine()


## encapsulation
class BackAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("amount must be positive")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("balance is insufficient")

    def get_balance(self):
        print(f"{self.__account_number}'s balance is {self.__balance}")


tu = BackAccount("123", 50)
tu.get_balance()
tu.deposit(10)
tu.get_balance()
tu.withdraw(100)
tu.get_balance()
tien = BackAccount("456", 0)
tien.get_balance()
tien.deposit(-100)
tien.deposit(200)
tien.withdraw(400)
tien.get_balance()
tien.withdraw(200)
tien.get_balance()


# inheritance
class Vehicle:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        print(f"Color is {self.__color}")
        return self.__color


class Car(Vehicle):
    def __init__(self, color, speed):
        super().__init__(color)
        self.speed = speed

    def get_speed(self):
        color = self.get_color()
        print(f"{color}'s speed is {self.speed}")


red = Car("red", 50)
red.get_color()
red.get_speed()


class Document:
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method.")


class Pdf(Document):
    def show(self):
        return "Show pdf content."


class Word(Document):
    def show(self):
        return "Show word content."


documents = [Pdf(), Word()]

for doc in documents:
    print(doc.show())


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
