#Random Number Game by Seth Fleshman
#The computer picks a random number between 1 and 100 and the user tries to guess it

#import random functionality
import random

while True:
    #Pick the secret number and set the turns to 0
    secretNumber = random.randint(1, 100)
    turns = 0

    #While the user has not guessed the number, have them keep guessing
    while True:
        guess = int(input("I'm thinking of a number between 1 and 100. Enter your guess: "))

        #Check that the guess is valid. If not, restart the loop and ask for their guess again.
        if guess < 1 or guess > 100:
            print("Invalid guess. Try again.")
            continue

        #Increment turns
        turns += 1

        #Tell them if their guess is too high, too low, or spot on
        if guess > secretNumber:
            print("Lower!")
        elif guess < secretNumber:
            print("Higher!")
        elif guess == secretNumber:
            #Print their congratulations message based on their # of turns
            print("Congratulations!")
            if turns == 1:
                print("You guessed it in 1 turn! Amazing!")
            elif turns >= 2 and turns <= 3:
                print(f"You guessed it in {turns} turns! Amazing!")
            elif turns >= 4 and turns <= 5:
                print(f"You guessed it in {turns} turns! Impressive!")
            elif turns >= 6 and turns <= 7:
                print(f"You guessed it in {turns} turns! Good Job!")
            elif turns >= 8 and turns <= 9:
                print(f"You guessed it in {turns} turns! Took a little longer, but you got there!")
            elif turns >= 10:
                print(f"You guessed it in {turns} turns! You need to lock in.")
            print(turns)
            break

    #See if they would like to play again.
    userResponse = input("Enter \"y\" to play again. Enter any other key to be done: ")
    if userResponse.lower() == "y":
        continue
    else:
        print("Thanks for playing then!")
        break



    
