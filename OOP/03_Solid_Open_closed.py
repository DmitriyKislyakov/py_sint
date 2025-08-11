from abc import ABC, abstractmethod

class PaymentProcessor:
    @abstractmethod
    def pay(self):
        pass

class PayPayPaL(PaymentProcessor):
    def pay(self):
        return "Оплата PayPal"

class PayCreditCart(PaymentProcessor):
    def pay(self):
        return 'Оплата картой'

class PayCrypto(PaymentProcessor):
    def pay(self):
        return' Оплата криптой'

class Order:
    def __init__(self, items: list[float], payment_processor=PaymentProcessor):
        self.items = items
        self.payment_processor = payment_processor

    def bucket(self):
        print(f'Ваш заказ на сумму {sum(self.items)}, {self.payment_processor.pay()}')

o1 = Order([213, 34234, 453453], PayPayPaL())
o1.bucket()

o2 = Order([125.51, 1564.456, 448.46], PayCrypto())
o2.bucket()

o3 = Order([123, 45, 789], PayCreditCart())
o3.bucket()
