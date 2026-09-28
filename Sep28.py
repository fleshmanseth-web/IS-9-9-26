#Today we learned about making custom functions
#In the world of program you know it's a method or a function if there are parentheses
#Keep an eye on the scope; the whole code can't see the whole code.

import random

def one_play(message):
    response = input(message)
    print(response)

#Welcome the user
print("Welcome to the higher/lower game my friend! Welcome, welcome.")
one_play("Sup shawty ")
isPlaying = True

while isPlaying == True:
    #Pick a random number
    secret_number = random.randint(1, 100)
    guess = 0
    print(secret_number)

    while True:
        #Get the user's guess
        guess = int(input("Guess a number between 1 and 100: "))

        #Verify that it's a valid guess
        while guess < 1 or guess > 100:
            print("That's an invalid guess! try again, number between 1 and 100")

        #Determine need of guess adjustment
        if guess == secret_number:
            print("Congratulations!")
            break
        elif guess < secret_number:
            print("Too low my friend, too low")
        elif guess > secret_number:
            print("Too high my friend, too high")

    play_again_response = input("Enter \"y\" to play again, or anything else to quit: ")

    if play_again_response.lower() != "y":
        isPlaying = False


