class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
            pass
        # здесь продолжайте метод add

    def remove(self, eng):
        pass
        # здесь продолжайте метод remove

    def translate(self, eng):
        pass
        # здесь продолжайте метод translate
