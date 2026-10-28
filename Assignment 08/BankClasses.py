import random
from decimal import Decimal, InvalidOperation

#Create a bank account class with a name, balance, and account number
class BankAccount:
    #Create a constructor that assigns name, account number, and balance
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(1000000, 9999999)
        self.balance = Decimal("0.00")

    #Create a deposit function that gathers the amount to deposit, 
    #validates input, adds it to balance, and displays success
    def deposit(self):
        while True:
            try:
                amount = Decimal(input("\nEnter the value you would like to deposit. $").replace(",", ""))

                #Reject non-finite values, non-positive amounts, and partial pennies.
                if not amount.is_finite() or amount <= 0 or amount != amount.quantize(Decimal("0.01")):
                    print("Enter a positive amount with only whole pennies.")
                    continue

                #If the input is valid, add the amount to the balance
                amount = amount.quantize(Decimal("0.01"))
                self.balance += amount
                print(f"\nSuccessfully deposited ${amount:,.2f}")
                break
            except InvalidOperation:
                print("\nEnter a valid amount.")

    #Create a withdrawal function that gathers the amount to withdraw, 
    #validates input, subtracts it from balance, and displays success
    def withdrawal(self):
        while True:
            try:
                amount = Decimal(input("\nEnter the value you would like to withdraw. $").replace(",", ""))

                #Reject non-finite values, non-positive amounts, and partial pennies.
                if not amount.is_finite() or amount <= 0 or amount != amount.quantize(Decimal("0.01")):
                    print("Enter a positive amount with only whole pennies.")
                    continue
                amount = amount.quantize(Decimal("0.01"))
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"\nSuccessfully withdrew ${amount:,.2f}")
                    break
                else:
                    print("\nInsufficient funds. Try again.")
                    continue
            except InvalidOperation:
                print("\nEnter a valid amount.")

#Displays account information
    def view_account(self):
        print(f"""\nAccount Name: {self.name}
Account Number: {self.account_number}
Account Balance: ${self.balance:,.2f}""")
