class Nikola:
    __slots__ = ('name', 'age')
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        if self.name == 'Николай':
            return f'Я {self.name}, мне {self.age}'
        else:
            return f'Я не {self.name}, а Николай, мне {self.age}'


n1 = Nikola('hkj', 21)
print(n1)
n2 = Nikola('Николай', 35)
print(n2, n1)
