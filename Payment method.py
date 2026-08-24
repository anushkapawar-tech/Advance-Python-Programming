# Payment methods
class CreditCard:
    def pay(self, amount):
        print("Paid $", amount, "using Credit Card")

class PayPal:
    def pay(self, amount):
        print("Paid $", amount, "using PayPal")

class UPI:
    def pay(self, amount):
        print("Paid $", amount, "using UPI")

# Payment Processor
class PaymentProcessor:
    def __init__(self, payment):
        self.payment = payment

    def change_payment(self, payment):
        self.payment = payment

    def process_payment(self, amount):
        self.payment.pay(amount)

# Main program
processor = PaymentProcessor(CreditCard())
processor.process_payment(100)

processor.change_payment(PayPal())
processor.process_payment(200)

processor.change_payment(UPI())
processor.process_payment(300)