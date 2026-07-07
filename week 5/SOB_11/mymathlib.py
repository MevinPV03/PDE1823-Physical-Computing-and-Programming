#File: mymathlib.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

#Main file:

import mymathlib  # Importing user-defined library

print(mymathlib.add(5, 3))
print(mymathlib.multiply(4, 2))


#Custom Class: BankAccount

class BankAccount:
    """
    This class represents a bank account.
    It allows depositing and withdrawing money.
    """

    def __init__(self, owner, balance):
        self.owner = owner           # Property
        self.balance = balance       # Property

    def deposit(self, amount):
        """Adds money to the account."""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Removes money from the account if sufficient balance exists."""
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"


# Create object
account1 = BankAccount("Mevin", 1000)

# Use methods
print("Initial balance:", account1.balance)

account1.deposit(500)
print("After deposit:", account1.balance)

account1.withdraw(300)
print("After withdrawal:", account1.balance)
