import time

def type_text(message, delay=0.05):
# define type_text (function) is a function of message (variable) and delay (integer, which is set)
    for letter in message:
        print(letter, end="", flush=True) 
        #commas allow you to add multiple things in a string and use keyword settings. + is mostly for saving a variable because commas only act as glue in functions like print, and if you want stuff to touch
        #flush = true forces the terminal to display the text immediately instead of delaying it until you are on a new line, making the typewriter effect work
        time.sleep(delay)

type_text("What is your name?: ")
name = input()

while name.lower() != "jess":
# name.lower() lowercases it.
    type_text("Get lost loser!! I'm looking for Jess!!!")
    time.sleep(0.5)
    print()
    type_text("Try again, what is your name?: ")
    name = input()

type_text("Finna rizz you up in 5...")
time.sleep(1)

for number in range(4, -1, -1):
    print(f"\rFinna rizz you up in {number}...", end=(""))
    time.sleep(1)

print("\n")

for mwah_number in range(1, 76, 1): #the start number is included, but not the stop, so it has to be one higher than what I want
    print("Mmmmwwwwaaaah number " + str(mwah_number))
    time.sleep(0.2)

print("\r.", end="")
time.sleep(1)
print("\r..", end="")
time.sleep(1)
print("\r...", end="")
time.sleep(2)
type_text("\rOne for every day we've been married :) ")
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(". ", end="")
time.sleep(2)
type_text("I love you :)")


# if name == "Jess": 
#         #The : is very important for if and else
#         # in Python = means assign value, and == is what you would use here to check the value
#     print("Hi dreamboat :)")
# else:
#     print("Get lost!!!")
