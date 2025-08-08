class Employee:
    _emp_list = []

    @classmethod
    def add_emp(cls, emp):
        cls._emp_list.append(emp)

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        self.add_emp(self)

    def get_info(self):
        print(f'меня зовут {self.name}, я работаю {self.position}, зарабатываю {self.salary}')

class Developer(Employee):
    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        print(f'я- {self.name}, работаю {self.position}, пишу на {self.programming_language}, зарабатываю {self.salary}.')

class Manager(Employee):
    def get_info(self):
        e_list = []
        for i in self._emp_list:
            if not (i.position == 'developer' or i.position == 'manager'):
                e_list.append(i.name)
        print(f'я {self.name}, зарабатываю {self.salary} и {self.position}: {", ".join(e_list)}')


e1 = Employee('mike', 'worker', 1000)
e2 = Employee('stiv', 'seller', 300)
e1.get_info()
e2.get_info()
d1 = Developer(name='cler', position='developer', salary=60000000000, programming_language='JS')
d1.get_info()
m1 = Manager('Bob', 'manager', 5000)
m1.get_info()