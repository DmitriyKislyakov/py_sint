class RealString:
    def __init__(self, stroka):
        self.stroka = str(stroka)

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self.stroka) == len(other.stroka)
        elif isinstance(other, str):
            return len(self.stroka) == len(other)
        else:
            raise TypeError('Оператор должен быть строкой или объектом класса RealString')

s1 = RealString('asda')
s2 = RealString('asda')
s3 = 'dasd'
print(s2 == s1)
print(s3 == s1)
