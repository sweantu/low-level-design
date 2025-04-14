# factory used to create object without specifying class

from __future__ import annotations
from abc import ABC, abstractmethod


class Factory:
    @abstractmethod
    def create(self) -> Transport:
        pass

    def do_delivery(self):
        transport = self.create()
        return transport.delivery()


class TruckFactory(Factory):
    def create(self):
        return Truck()


class ShipFactory(Factory):
    def create(self):
        return Ship()


class PlaneFactory(Factory):
    def create(self):
        return Plane()


class Transport:
    @abstractmethod
    def delivery(self) -> str:
        pass


class Truck(Transport):
    def delivery(self):
        return "driving"


class Ship(Transport):
    def delivery(self):
        return "sailing"


class Plane(Transport):
    def delivery(self):
        return "flying"


def delivery(factory: Factory):
    print(f"Goods are {factory.do_delivery()}")


if __name__ == "__main__":
    delivery(TruckFactory())
    delivery(ShipFactory())
    delivery(PlaneFactory())
