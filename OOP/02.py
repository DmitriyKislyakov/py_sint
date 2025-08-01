class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        self.tr[eng].append(rus)
        # здесь продолжайте метод add

    def remove(self, eng):
        self.tr.pop(eng, False)
        # здесь продолжайте метод remove

    def translate(self, eng):
        print(* self.tr[eng])
        # здесь продолжайте метод translate


tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')
tr.translate('go')
