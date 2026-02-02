from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardpayment(Payment):
    def process_payment(self, amount):
        print("processing CreditCardpayment of amount", amount)

class UPIPayment(Payment):
    def process_payment(self, amount):
        print("processing UPIPayment of amount",amount)

#p1 = Payment()
p2 = CreditCardpayment()
p3 = UPIPayment()

#p1.process_payment()
p2.process_payment(5000)
p3.process_payment(4000)