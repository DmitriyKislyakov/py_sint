class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return 'Ошибка: нельзя создавать объекты абстрактного класса'

class SingletonFive:
    __count = 0
    __instanse = None
    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__instanse = super().__new__(cls)
            cls.__count += 1
        return cls.__instanse

    def __init__(self, name):
        self.name = name



objs = [print(SingletonFive(str(n))) for n in range(10)]