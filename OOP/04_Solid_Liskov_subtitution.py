from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def speak(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print('I can fly!!!')

    def speak(self):
        print('Чирик-чирик')

class Penguin(Bird):
    def fly(self):
        print('I can\'t fly!')

    def speak(self):
        print('...')


s = Sparrow()
s.fly()
s.speak()
print()
p = Penguin()
p.fly()
p.speak()