import random

#Here is the bank account class:

class BankAccount:
    def __init__(self, users_name):
        self.users_name = users_name
        self.account_balance = 0.00
        self.account_number = random.randint(10000, 99999)

#Function that makes a deposit in the account:

    def make_deposit(self):
        try:
            deposit_amount = float(input("Deposit amount:\n"))
            if deposit_amount > 0:
                self.account_balance += deposit_amount
            else:
                print("\nInvalid amount!\n")
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")

#Withdrawal function:

    def make_withdrawal(self):
        try:
            withdrawal_amount = float(input("Withdrawal amount:\n"))
            if 0 < withdrawal_amount <= self.account_balance:
                self.account_balance -= withdrawal_amount
            else:
                print("\nInvalid amount or insufficient funds!\n")
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")

#View account information function:

    def view_account_info(self):
        print(f"\nName: {self.users_name}")
        print(f"Account number: {self.account_number}")
        print(f"Account balance: ${self.account_balance:.2f}\n")