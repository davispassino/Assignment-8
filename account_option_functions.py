#Here is the choose an option function:

def choose_an_option():
    print("Please choose an option:\n")
    print("A. Make a deposit")
    print("B. Make a withdrawal")
    print("C. View account information")
    print("D. Quit\n")
    option = input().upper()
    
    return option 

#Here is the function to valid the chosen option:

def validate_option(option):
    while option not in ["A","B","C","D"]:
        print("Invalid input. Please enter again!")
        option = input().upper()
    return option 