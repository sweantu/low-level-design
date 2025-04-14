class Singleton(type):
    _instances = {}

    def __call__(self, *args, **kwds):
        if self not in self._instances:
            self._instances[self] = super().__call__(*args, **kwds)
        return self._instances[self]


class Test(metaclass=Singleton):
    def do_something(self):
        pass


if __name__ == "__main__":
    test1 = Test()
    test2 = Test()
    if id(test1) == id(test2):
        print("Singleton")
    else:
        print("Wrong")
