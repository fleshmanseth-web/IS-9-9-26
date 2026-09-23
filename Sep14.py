import time

def type_text(message, delay=0.02):
    for letter in message:
        print(letter, end="", flush=True)
        time.sleep(delay)

calculation = 2 ** 8
    #** is to the power of, not a ^
calculation_2 = 5 % 2
    #% is the modulus, and it gives you the remainder after dividing them
calculation_3 = 5 / 3
calculation_4 = 5 // 3
    #Gives you just the amount of times it fits in evenly without a remainder
calculation_3 = round(calculation_3, 2)
    #This rounds it to 2 decimal places
num_1 = round(2.5)
    #Unless I specify the number of places then it will use banker's rounding, so if it's an even number (the number int he ones spot) then it will go down at .5, and if it's an odd number it will go up.


account_balance = 1000
account_balance = account_balance + 100
account_balance += 100
account_balance *= 2
account_balance -= 200
account_balance /= 2
print("Account balance is: $" + str(account_balance))

comparison = (5 > 3) & (4 == 4) & (2 > 3)
print(comparison)

type_text("Enter your age my friend! Don't be shy: ")
age = int(input())

#If it finds an exit that matches, it will leave. 
# If checks in order, if it's over 40, 
# it won't even check the next one.

if (age > 16 & age < 18) or (age == 171717):
    #you could also use an or
    #ands take precedent over ors
    #indentation matters
    print("ur 17 dawg")
elif (age < 0):
    type_text("Impossible! A fetus?!?")
elif (age < 40):
    type_text("Keep plugging along")
elif (age >= 40):
    type_text("You are old"), print("\nhaha")
    #Can keep it on the same line with the good old trusty comma
else:
    print("Incorrect input, better luck next time")