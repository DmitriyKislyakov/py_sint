class Temperature:
    def __init__(self, temp_c: int):
        self.temp_c = temp_c

    @classmethod
    def f_to_c(cls, temp_f):
        return (temp_f - 32)/1.8

    @property
    def get_temp_k(self):
        return(self.temp_c + 273.5)

    @staticmethod
    def freeze_point(temp):
        return temp <= 0

t = Temperature(45)
print(t.__dict__)
print(t.get_temp_k )
print(t.f_to_c(50))
print(t.freeze_point(0))
