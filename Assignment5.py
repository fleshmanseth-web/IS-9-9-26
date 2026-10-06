# Seth Fleshman
# Rock Paper Scissors Game

import random

# prompt the player, convert the response to
# lowercase, validate the choice, and return the result
def get_player_choice():
        while True:
            user_choice = input("What do you choose? (Enter \"rock\", \"paper\", or \"scizzors\") ")
            if user_choice.lower() in options:
                break
            else:
                print("Enter a valid choice :)")
                continue

        return(user_choice.lower())

# compare the two choices and return "win",
# "loss", or "tie"
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        win_state = "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scizzors") 
        or (user_choice == "paper" and computer_choice == "rock") 
        or (user_choice == "scizzors" and computer_choice == "paper")
    ):
        win_state = "win"
    else:
        win_state = "loss"
    return(win_state)

options = ["rock", "paper", "scizzors"]
user_wins = 0
user_losses = 0
current_round = 1

# Welcome the user to the game
print("Welcome to the game! So glad you could make it!")

# Ask them how many rounds they would like to play.
while True:
    # Ensure that the number they enter is an odd number so there cannot be any ties.
    num_rounds = int(input("How many rounds would you like to play? Only enter an odd number. "))

    if num_rounds % 2 == 1:
        break
    else:
        print("Enter an odd number")
        continue

# Play each of the rounds
while current_round <= num_rounds:
    # Get the user's choice, the computer's choice, and the comparison
    user_choice = get_player_choice()
    computer_choice = random.choice(options)
    print(f"I choose: {computer_choice}")
    win_state = determine_winner(user_choice, computer_choice)

    # Act on whoever won, iterate the round unless it's a tie
    if win_state == "win":
        print("You win!")
        user_wins += 1
        current_round += 1
    elif win_state == "loss":
        print("I win!")
        user_losses += 1
        current_round += 1
    else:
        print("A tie!!")

#Identify overall winner and print results
print()
print("- - - - - - - - - - - - - - -")
print()
print(f"Score: You: {user_wins}, Me: {user_losses}")
if user_wins > user_losses:
    print("You win!")
else:
    print("I win!")
print("Thanks for playing :)")

