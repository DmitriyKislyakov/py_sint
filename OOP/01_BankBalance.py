class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance

    def deposite(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            e = Exception('На вашем счету недостаточно средств!')
            raise e
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

b1 = BankAccount(500)
b1.deposite(200)
print(b1.get_balance())
b1.withdraw(500)
print(b1.get_balance())


