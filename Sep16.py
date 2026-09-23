#definite loop example = we know how many times we want it to run, even if it requires the user's input

for numby in range(5):
    #You can name it whatever you want to, but i is like industry standard
    print(f"Gimme Gimme {numby}" + str(numby))

for i in range (100, -1, -10):
    print(str(i))

for i in range (5):
    #don't need to use a different variable name
    print(i)

#indefinite loop = we don't know how many times it will run

while True:
    try:
        age = int(input("How old are ya shawty? "))
    except ValueError:
        print("Enter an integer only")
        continue

    if age == -16:
        break

    if age < 0:
        print("Goo goo, gah gah, you have not been born yet")
        continue

    break

print(age)

for i in range(1, 4):
    for i_two in range(1, 5):
        print(f"Day {i} Appointment {i_two}")

#Last chapter he didn't explain Git and Github...very sad...I will have to do that.
#Students write programs from the outside in. They start with a while loop. Experts start from the inside out. Start with Psuedocode.
#I can write the pseudocode, always start there. Loops are inside out. If I write the pseudocode, then I can ask AI to do it.
#Once a game is built for one guess, then I built it out from there. Inside out coding.
