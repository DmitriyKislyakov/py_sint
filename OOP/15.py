class  KgToPounds:
    def __init__(self, kg: int):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def get_kg(self):
        return self.__kg

    @get_kg.setter
    def set_kg(self, val):
        self.__kg = val

k1 = KgToPounds(15)
print(k1.get_kg)
k1.set_kg = 25
print(k1.get_kg)
print(k1.to_pounds())


