# Strategy used to turns a set of behaviors into objects and makes them interchangeable inside original context object.

from __future__ import annotations
from abc import ABC, abstractmethod


class Context:

    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_something(self, list):
        return ", ".join(self._strategy.do_something(list))


class Strategy(ABC):

    @abstractmethod
    def do_something(self, list):
        pass


class AscSort(Strategy):
    def do_something(self, list):
        return sorted(list)


class DescSort(Strategy):
    def do_something(self, list):
        return reversed(sorted(list))


if __name__ == "__main__":
    context = Context(AscSort())
    arr = ["a", "d", "b", "c"]
    print(context.do_something(arr))
    context.strategy = DescSort()
    print(context.do_something(arr))
