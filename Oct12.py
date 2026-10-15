# Validation and exception handling
# Similar to just saying while True and then break
# Red dot is a stop or a breakpoint
# Step over will skip a function
# Step into a function will let you step into just one function
# Step out of will let you step out of a function
# You can just keep stepping through the program and see where it is and isn't working
import BankFunctions

has_error = True

balance = 100

while True:
    try:
        amount = int(input("Please enter the amount you want to withdraw: "))
        balance = BankFunctions.withdraw(amount, balance)
        break
    except ValueError:
        print("Please enter a number")

while has_error:
    try:
        number = int(input("Enter a number: "))
        print(number)
        has_error = False
    except ValueError:
        print("Invalid input. Please enter a whole number.")
    # What will happen if they Control + C
    except KeyboardInterrupt:
        print("You stopped the program")
    # Catch-all
    except:
        print("You got some rando error")
    else:
        # You will get something else even if you got accurate input, it will add
        # Could use a continue, which here applies still to the while loop and not the try except sequence
        print(number)
        if number == 10:
            print("You entered a valid number! Amazing!")
    finally:
        # This will go regardless of what else happens
        print("Later skater")

# Other error validation situations in BankFunctions
