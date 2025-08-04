class Person:
    __slots__ = ('_fio', '_old', '_job')

    def __init__(self, fio, old, job):
        self._fio = fio
        self._old = old
        self._job = job


p1 = Person('Суворов', 52, 'полководец')
p2 = Person('Рахманинов', 50, 'пианист, композитор')
p3 = Person('Балакирев', 34, 'программист и преподаватель')
p4 = Person('Пушкин', 32, 'поэт и писатель')
persons = [p1, p2, p3, p4]
print(persons)