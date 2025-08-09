class Flyable:
    def fly(self):
        print('I\'m flying!')

class Swimmable:
    def swim(self):
        print('I\'m swimming!')

class Duck(Flyable, Swimmable):
    def make_sound(self):
        print('Quack!')

d1 = Duck()
d1.swim()
d1.fly()
d1.make_sound()
