numbers = [10, 12, -1, 978]

for i in range(0, len(numbers)):
    print(numbers[i])

for i in numbers:
    print(i)

fam = [
    {"Name" : "Seth", "Age" : 22, "Gender" : True},
    {"Name" : "Jess", "Age" : 24, "Gender" : False}]

for person in fam:
    print(person["Name"] + " " + str(person["Age"]))

amount = 1000000

#Comma tells it to add commas like a number, the .2f says to two places
print("I don't need " + "${:,.2f}".format(amount))
print(f"I don't need ${amount:,.2f}")

from datetime import datetime
print(datetime.now())

# Notes on class
# I can create a portfolio on GitHub
# Git is local, Github is distributed
# Function(Arguement)

#Coding Challenge
