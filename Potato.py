#I'm going to print something out
TheGoods = "Blah Blah Blah I'm just typing"
Num1 = 17
Num2 = 38
total = Num1 + Num2

print(TheGoods)
print(Num1 + Num2)
print(total)
print(Num1, Num2) # this prints both of them, but it does have a space
print(Num1, Num2, sep="Yoooooo") #Puts just a "Yoooooo"
print(Num1, Num2, Num1, sep="")

user_name = input("Enter your name: ")
print("Hello, " + user_name)

user_age = int(input("How old are you?")) #Collects user's age and converts it to an integer
print(type(user_age)) #This prints what type of variable user age is.
print("You are " + str(user_age * 7) + " in dog years.")
    #Calculates the user's age, converts it to a string, and then prints it within the string

print(f"You are {user_age * 7} in human years.")
    #The f makes it an f-string, which lets you insert variables or expressions directly inside the string using {}

# the following is something cool I can do with print() learned with chat
import time 
#this tells python that I want to use the time functionality (toolbox)

for number in range(10, 0, -1): 
#This is a loop that says create a variable called number, starts at 10, go to 0, go down by 1 each time 
    #(could be 2, 4, anything)
    print(f"\rLaunching in {number}...", end="")
        #the \r means "carriage return", and it sends the cursor back to the beginning of the line so it can overwrite itself
        #\n = next line
        #the end="" stops python from moving to the next line, because by default it will naturally do that and the end will be \n. You could also end with end = "!" or whatever you want.
    time.sleep(1)
        #This tells it to wait one second

print("\rLiftoff!             ")
        #The extra spaces help delete the other leftover text