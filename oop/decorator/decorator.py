# Decorator used to add new behaviors to objects dynamically by placing them inside special wrapper objects, called decorators.


from __future__ import annotations

from abc import ABC, abstractmethod


# this abstract class forces that Decorator class must implement make method as same as OriginalPizza class
class Pizza(ABC):
    @abstractmethod
    def make(self) -> str:
        pass


class OriginalPizza(Pizza):
    def make(self):
        return "pizza"


class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    @abstractmethod
    def make(self) -> str:
        pass


class ChesseDecorator(PizzaDecorator):
    def make(self):
        return f"cheese {self.pizza.make()}"


class FruitDecorator(PizzaDecorator):
    def make(self):
        return f"fruit {self.pizza.make()}"


class PepperDecorator(PizzaDecorator):
    def make(self):
        return f"pepper {self.pizza.make()}"


class MushroomDecorator(PizzaDecorator):
    def make(self):
        return f"mushroom {self.pizza.make()}"


def serve(pizza: Pizza):
    print(f"Serving {pizza.make()}")


if __name__ == "__main__":
    originalPizza = OriginalPizza()
    serve(originalPizza)

    cheesePizza = ChesseDecorator(OriginalPizza())
    serve(cheesePizza)

    fruitPizza = FruitDecorator(ChesseDecorator(OriginalPizza()))
    serve(fruitPizza)

    specialPizza = PepperDecorator(
        ChesseDecorator(MushroomDecorator(PepperDecorator(OriginalPizza())))
    )
    serve(specialPizza)
