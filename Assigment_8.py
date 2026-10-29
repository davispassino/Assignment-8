#Here is where my program imports the needed functions:

from bank_account_file import BankAccount
from account_option_functions import choose_an_option, validate_option

#Here the program welcomes you and asks your name:

print("\nWelcome to Passino's Bank!\n")
users_name = input("Enter your name: ").title()
print(f"\nWelcome {users_name}!")

#Here my variables are defined:

account = BankAccount(users_name)
option = "A"

#Here is the program loops the options until the users chooses "D":

while option in ["A","B","C"]:

    option = choose_an_option()
    option = validate_option(option)

    if option == "A":
        account.make_deposit()
    elif option == "B":
        account.make_withdrawal()
    elif option == "C":
        account.view_account_info()
    
print("\nThank you for your business!\n")