class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
print(hasattr(p1, 'job'))
setattr(p1, 'hobby', 1)
print(p1.__dict__)
print(Person.__doc__)
