import math
class Shape:
    def area(self):
        pass

    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.heigth = height

    def area(self):
        return self.width * self.heigth

    def perimeter(self):
        return (self.width + self.heigth) * 2

class Cirlce(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)



s1 = Shape()
r1 = Rectangle(2, 4)
r2 = Rectangle(10, 20)
c1 = Cirlce(10)
c2 = Cirlce(3)
shape_list = [s1, r1, r2, c1, c2]

for e in shape_list:
    print(e.area(), e.perimeter())