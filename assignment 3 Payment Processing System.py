from abc import ABC, abstractmethod
from functools import wraps


def log_transaction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("\nTransaction Started...")
        result = func(*args, **kwargs)
        print("Transaction Completed.")
        return result
    return wrapper


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):

    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Payment of ₹{amount} successful using Credit Card ({self.card_number[-4:]})")


class UPIPayment(PaymentStrategy):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Payment of ₹{amount} successful using UPI ({self.upi_id})")


class PayPalPayment(PaymentStrategy):

    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Payment of ₹{amount} successful using PayPal ({self.email})")


class NetBankingPayment(PaymentStrategy):

    def __init__(self, bank_name):
        self.bank_name = bank_name

    def pay(self, amount):
        print(f"Payment of ₹{amount} successful using {self.bank_name} Net Banking")


class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    @log_transaction
    def process_payment(self, amount):
        self.strategy.pay(amount)


print("===== Payment Processing System =====")

amount = float(input("Enter Amount: "))

print("\nSelect Payment Method")
print("1. Credit Card")
print("2. UPI")
print("3. PayPal")
print("4. Net Banking")

choice = int(input("Enter Choice: "))

if choice == 1:
    card = input("Enter Card Number: ")
    payment = CreditCardPayment(card)

elif choice == 2:
    upi = input("Enter UPI ID: ")
    payment = UPIPayment(upi)

elif choice == 3:
    email = input("Enter PayPal Email: ")
    payment = PayPalPayment(email)

elif choice == 4:
    bank = input("Enter Bank Name: ")
    payment = NetBankingPayment(bank)

else:
    print("Invalid Choice")
    exit()

processor = PaymentProcessor(payment)
processor.process_payment(amount)

print("\nThank You!")