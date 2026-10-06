numbies = [17, 38, 9000, 11, 7, 234]

def even_check(num):
    if num % 2 == 0:
        even = True
    else:
        even = False

    return even #returns the value even so whatever is calling the function can see it

#Allow the user to input as many numbers to the list as possible
while True:
    print(f"So we are going to check if {numbies} is/are even, right?")
    inp = input("Did I miss anything? (enter n if not) ")
    if inp == "n":
        break
    else:
        numbies.append(int(inp))

for num in numbies:
    if even_check(num): #Does the same thing as checking if it's true or not
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

