from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Flyable:
    def fly(self):
        print('I\'m flying!')

class Swimmable:
    def swim(self):
        print('I\'m swimming!')

class Runable:
    def run(self):
        print("I'm running!")

class Dog(Animal, Runable):
    def speak(self):
        print('Woof!')

    def move(self):
        self.run()

class Bird(Animal, Flyable):
    def speak(self):
        print('Tweet!')

    def move(self):
        self.fly()

class Fish(Animal, Swimmable):
    def speak(self):
        pass

    def move(self):
        self.swim()



d = Dog()
b = Bird()
f = Fish()

zoo = [d, b, f]
for a in zoo:
    a.speak()
    a.move()
    print()