# Adapter used to allow incompatible objects to collaborate.

from abc import ABC, abstractmethod
from enum import Enum


class Port(Enum):
    PORT_TYPE_C = 1
    PORT_TYPE_A = 2


class Charger(ABC):
    @abstractmethod
    def charge(self, port: Port):
        pass


class ChargerTypeC(Charger):
    def charge(self, port: Port):
        if port == Port.PORT_TYPE_C:
            print("Charging")
        else:
            print("Not supported")


class ChargerTypeA(Charger):
    def charge(self, port: Port):
        if port == Port.PORT_TYPE_A:
            print("Charging")
        else:
            print("Not supported")


class Adapter(Charger):
    def __init__(self, chargerTypeA: ChargerTypeA):
        self.chargerTypeA = chargerTypeA

    def charge(self, port: Port):
        if port == Port.PORT_TYPE_C:
            print("Adapter converting port Type-C to port Type-A")
            port = Port.PORT_TYPE_A
            self.chargerTypeA.charge(port)
        else:
            print("Not supported")


if __name__ == "__main__":
    portTypeC = Port.PORT_TYPE_C
    chargerTypeC = ChargerTypeC()
    chargerTypeC.charge(portTypeC)

    chargerTypeA = ChargerTypeA()
    chargerTypeA.charge(portTypeC)

    adapter = Adapter(chargerTypeA)
    adapter.charge(portTypeC)
