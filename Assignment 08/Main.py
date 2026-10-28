#Seth Fleshman
#Assignment 8 - a simple bank account simulator
import BankClasses

#Welcome the player
print("\nWelcome to Elgin Bank's Delux Online System! \n")
print("We are so pleased to have you with us. \n")

#Get the user's name and validate the input
acquiring_name = True
while acquiring_name:
    name = input("What is your name? ")

    # Because all input is read in as a string, we do not need to use try except,
    # so we will just make sure that the only use A-Z characters
    if name.replace(" ", "").isalpha():
        acquiring_name = False
    else:
        print("\nPlease enter a valid name using only A-Z and spaces.")

#Create an instance of the BankAccount class with the user's name as the account name
account = BankClasses.BankAccount(name)

#Welcome the user by name
print(f"\nWelcome {name}!")

#Give the user options for what to do.
#Options include deposits, withdrawals, viewing account info, and quitting
#Validate input. End when the user asks to quit.
while True:
    print(f"""\nPlease select an option below by typing the associated number.
1. Make a deposit
2. Make a withdrawal
3. View account information
4. Quit""")
    choice = input("")

    if choice == "1":
        account.deposit()
    elif choice == "2":
        account.withdrawal()
    elif choice == "3":
        account.view_account()
    elif choice == "4":
        print("\nThank you for your business!")
        break
    else:
        print("Invalid choice, please try again.")