# Observer pattern using pull model - observers request data from subject when notified

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import random


class Subject:

    def __init__(self):
        self._data: int = 0
        self._observers: List[Observer] = []

    def subscribe(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print("Subscribe successfully")
        else:
            print("Observer already subscribed")

    def unsubscribe(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print("Unsubscribe successfully")
        else:
            print("Observer not found")

    def notify(self):
        # Only notify observers without sending data
        for observer in self._observers:
            observer.update(self)
        print("Notify successfully")

    def random(self):
        self._data = random.randrange(1, 100)
        self.notify()

    # Getter method for observers to pull data when needed
    def get_data(self) -> int:
        return self._data


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        """Update method receives the subject reference, not the data"""
        pass


class User1(Observer):

    def update(self, subject: Subject):
        # Pull data from subject when notified
        data = subject.get_data()
        print(f"User 1 pulls and receives {data}")


class User2(Observer):

    def update(self, subject: Subject):
        # Pull data from subject when notified
        data = subject.get_data()
        print(f"User 2 pulls and receives {data}")


if __name__ == "__main__":
    subject = Subject()
    user1 = User1()
    user2 = User2()

    subject.subscribe(user1)
    subject.subscribe(user2)
    subject.random()

    subject.unsubscribe(user2)
    subject.random()
