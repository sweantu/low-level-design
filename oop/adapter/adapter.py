# Adapter used to allow incompatible objects to collaborate.

from enum import Enum
from abc import ABC, abstractmethod


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


class PortTypeCToPortTypeAAdapter(Charger):
    def __init__(self, typeA: ChargerTypeA):
        self.typeA = typeA

    def charge(self, port: Port):
        if port == Port.PORT_TYPE_C:
            print("Adapter converting Type-C port to Type-A port")
            port = Port.PORT_TYPE_A
            self.typeA.charge(port)
        else:
            print("Not supported")


if __name__ == "__main__":
    port = Port.PORT_TYPE_C
    typeC = ChargerTypeC()
    typeC.charge(port)

    typeA = ChargerTypeA()
    typeA.charge(port)

    adapter = PortTypeCToPortTypeAAdapter(typeA)
    adapter.charge(port)
