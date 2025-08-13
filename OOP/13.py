class Soda:

    def __init__(self, filler=None):
        self.filler = filler

    def show_my_drink(self):
        if self.filler:
            print(f'Газировка и {self.filler}.')
        else:
            print(f'Обычная газировка.')


s1 = Soda()
s2 = Soda('banana')
s1.show_my_drink()
s2.show_my_drink()