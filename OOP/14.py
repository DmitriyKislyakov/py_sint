class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if any(type(e) not in (int, float) for e in [self.a, self.b, self.c]):
            return 'Нужно вводить только числа!'
        if any(e<=0 for e in [self.a, self.b, self.c]):
            return 'С отрицательными числами ничего не выйдет!'
        if  self.a + self.b > self.c and  self.a + self.c > self.b and self.b + self.c > self.a:
            return 'Ура, можно построить треугольник!'
        else:
            return 'Жаль, но из этого треугольник не сделать.'

c1 = TriangleChecker('a', 2, 3)
print(c1.is_triangle())
c2 = TriangleChecker(4, 5.4, -3)
print(c2.is_triangle())
c3 = TriangleChecker(3, 2, 4)
print(c3.is_triangle())
c4 = TriangleChecker(1, 5, 100)
print(c4.is_triangle())