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

#Notes on class
#I can create a portfolio on GitHub
#Git is local, Github is distributed
