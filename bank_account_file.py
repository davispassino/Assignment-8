#Here is the bank account class:

class Bank_account:
    def __init__(self, users_name):
        self.users_name = users_name
        self.account_balance = 0.00

#Function that makes a deposit in the account:

    def make_deposit(self):
        deposit_amount = float(input("Deposit amount:\n"))
        if deposit_amount > 0:
            self.account_balance += deposit_amount
        else:
            print("Invalid amount!")

#Withdrawal function:

    def make_withdrawal(self):
        withdrawal_amount = float(input("Withdrawl_amount:\n"))
        if 0 < withdrawal_amount <= self.account_balance:
            self.account_balance -= withdrawal_amount
        else:
            print("Invalid amount or insufficient funds!")

    def view_account_info(self):
        print(f"\nName: {self.users_name}")
        print(f"Account number: _____")
        print(f"Account balance: ${self.account_balance:.2f}\n")
