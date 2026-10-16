# Program by Seth Fleshman
# This is the main program for a Wordle, guess the word type game
import wordle_functions

#Welcome the player and provide instructions
print("Welcome to The Mystery Wordle Game!!!")
print("\nTry to guess the five letter word")
print("\nG = correct letter and position")
print("Y = correct letter, incorrect position")
print("- = letter is not in word\n")

# Give the player up to six guesses.
playing = True

while playing:
    current_guess = 1
    # Select a secret five-letter word.
    secret_word = wordle_functions.choose_word()
    # Clear the list of previous guesses for this round
    previous_guesses = []

    while current_guess < 7:
        print(f"Guess {current_guess} of 6: ")
        # validate guesses, require each guess to contain exactly five letters.
        # Reject guesses that have already been used.
        guess = wordle_functions.get_guess(previous_guesses)
        # Add valid guesses to the list of previous guesses from this round
        previous_guesses.append(guess.upper())
        current_guess += 1
        # Evaluate the guess
        feedback = wordle_functions.evaluate_guess(guess, secret_word)
        # Display guess and feedback after every guess.
        # Tell the player when a letter is correct, misplaced, or absent.
        wordle_functions.display_guess(guess, feedback)

        # End the game when the player guesses the word or uses all six attempts.
        has_won = wordle_functions.has_won(guess, secret_word)
        if has_won == False and current_guess < 7:
            # Keep going if they get it wrong but have remaining guesses
            continue
        elif has_won == False:
            # Display the secret word if the player loses.
            print(f"Too bad! You ran out of guesses. The word was {secret_word.upper()}.")
            break
        else:
            print(f"Good job! You won!! The word was {secret_word.upper()}.")
            break

    # Ask whether or not the player would like to keep playing
    if input("Enter y to play again, or anything else to quit: ").lower() == "y":
        continue
    else:
        print("Thanks for playing!! :)")
        playing = False