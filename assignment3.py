from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit Card")


class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


# Context Class
class PaymentProcessor:
    def __init__(self, holder_name, account_number, password):
        self.holder_name = holder_name
        self.account_number = account_number
        self.password = password
        self.strategy = None

    def set_payment_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount, entered_password):
        if entered_password != self.password:
            print("Invalid password! Payment failed.")
            return

        print("\nAccount Holder:", self.holder_name)
        print("Account Number:", self.account_number)

        if self.strategy:
            self.strategy.pay(amount)
        else:
            print("No payment method selected!")


# Main Program
holder_name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
password = input("Set account password: ")

processor = PaymentProcessor(holder_name, account_number, password)

print("\nSelect Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")

choice = int(input("Enter choice: "))

if choice == 1:
    processor.set_payment_strategy(CreditCardPayment())
elif choice == 2:
    processor.set_payment_strategy(DebitCardPayment())
elif choice == 3:
    processor.set_payment_strategy(UPIPayment())
else:
    print("Invalid choice!")

amount = float(input("Enter amount to pay: ₹"))
entered_password = input("Enter password to confirm payment: ")

processor.process_payment(amount, entered_password)