# Observer used to allow some objects to notify other objects about changes in their state.

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import random


class Subject:
    _data: int = 0
    _observers: List[Observer] = []

    def subscribe(self, observer: Observer):
        self._observers.append(observer)
        print("Subscribe successfully")

    def unsubscribe(self, observer: Observer):
        self._observers.remove(observer)
        print("Unsubscribe successfully")

    def notify(self):
        for observer in self._observers:
            observer.receive(self._data)
        print("Notify successfully")

    def random(self):
        self._data = random.randrange(1, 100)
        self.notify()


class Observer(ABC):
    @abstractmethod
    def receive(self, data: int):
        pass


class User1(Observer):
    def receive(self, data):
        print(f"User 1 receives {data}")


class User2(Observer):
    def receive(self, data):
        print(f"User 2 receives {data}")


if __name__ == "__main__":
    subject = Subject()
    user1 = User1()
    user2 = User2()

    subject.subscribe(user1)
    subject.subscribe(user2)
    subject.random()

    subject.unsubscribe(user2)
    subject.random()
