from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def swim(self):
        pass

class Runable(ABC):
    @abstractmethod
    def run(self):
        pass

class Swimable(ABC):
    @abstractmethod
    def swim(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Lion(Runable):
    def run(self):
        print('I can run!')

l = Lion()
l.run()
