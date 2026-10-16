# Program by Seth Fleshman
# This program contains all the custom functions for the Wordle game in main.py
import random

possible_words = [
    "GRAPE", "PEACH", "MANGO", "MELON", "LEMON", "OLIVE",
    "PRUNE", "BREAD", "BAGEL", "SCONE", "CREAM", "SUGAR",
    "HONEY", "SYRUP", "CANDY", "BEANS", "GRAIN", "WHEAT",
    "FLOUR", "YEAST", "SPICE", "WATER", "JUICE", "CIDER",
    "MOCHA", "PLATE", "STOVE", "TABLE", "CHAIR", "SHELF",
    "LIGHT", "HOUSE", "CABIN", "PORCH", "BRICK", "STONE",
    "PLANK", "PAINT", "BRUSH", "CLOTH", "TOWEL", "SHIRT",
    "PANTS", "SKIRT", "SCARF", "GLOVE", "APRON", "TIGER",
    "ZEBRA", "HORSE", "MOUSE", "CAMEL", "BISON", "LEMUR",
    "SLOTH", "WHALE", "SHARK", "SQUID", "PERCH", "ROBIN",
    "FINCH", "CRANE", "RAVEN", "STORK", "QUAIL", "GECKO",
    "SNAKE", "SNAIL", "CORAL", "PRAWN", "MOTHS", "FERNS",
    "VINES", "MAPLE", "BIRCH", "CEDAR", "BEACH", "ASPEN",
    "DAISY", "TULIP", "PETAL", "ACORN", "FLORA", "EARTH",
    "OCEAN", "COAST", "SHORE", "ISLET", "DELTA", "MOUNT",
    "RIDGE", "PLAIN", "FIELD", "CLOUD", "STORM", "RAINY",
    "SNOWY", "WINDY", "FROST", "MISTY", "HUMID", "NORTH",
    "SOUTH", "SPACE", "ORBIT", "COMET", "LUNAR", "SOLAR",
    "NIGHT", "DAWNS", "SMILE", "LAUGH", "AMUSE", "GRACE",
    "CHARM", "BRAVE", "PROUD", "NOBLE", "SMART", "QUICK",
    "SWIFT", "AGILE", "READY", "QUIET", "FRESH", "CLEAN",
    "CLEAR", "CRISP", "JUICY", "TANGY", "WHITE", "BLACK",
    "BROWN", "AMBER", "IVORY", "AZURE", "MAUVE", "ROUND",
    "CURVY", "SHARP", "SWING", "LARGE", "GIANT", "SHORT",
    "GRAND", "DANCE", "MUSIC", "PIANO", "FLUTE", "VIOLA",
    "DRUMS", "BANJO", "CHOIR", "CHORD", "TEMPO", "STORY",
    "NOVEL", "POEMS", "RHYME", "WRITE", "LEARN", "STUDY",
    "TEACH", "THINK", "COUNT", "SOLVE", "BUILD", "CRAFT",
    "CLIMB", "PAGES", "NOTES", "PRINT", "TRAIN", "PLANE",
    "TRUCK", "DRIVE", "SKATE", "ABOUT", "ABOVE", "ABUSE",
    "ACTOR", "ACUTE", "ADOPT", "ADULT", "AFTER", "AGENT",
    "AISLE", "ALBUM", "ALERT", "ALIEN", "ALIGN", "ALIKE",
    "ALIVE", "ALOUD", "ALTER", "AMPLE", "ANGEL", "ANGER",
    "ANGLE", "ANKLE", "APHID", "ARGUE", "ARISE", "AROSE",
    "ASIDE", "AUDIO", "AUDIT", "AVOID", "BADGE", "BAKER",
    "BALMY", "BARGE", "BASIC", "BASIL", "BATCH", "BATHE",
    "BATON", "BEARD", "BEAST", "BEGUN", "BEING", "BELOW",
    "BENCH", "BERTH", "BIRTH", "BLADE", "BLAME", "BLAND",
    "BLANK", "BLAST", "BLAZE", "BLEND", "BLIMP", "BLIND",
    "BLINK", "BLOAT", "BLOCK", "BLOND", "BLOWN", "BLUNT",
    "BOARD", "BOAST", "BONUS", "BOUND", "BOWEL", "BOXER",
    "BRAIN", "BRAKE", "BRAND", "BRAVO",
]

# choose_word() – Selects and returns a secret word with 5 letters and no repeat letters
def choose_word():
    word = random.choice(possible_words)
    return word

# get_guess() – Gets and validates the player’s guess.
def get_guess(previous_guesses):
    valid = False
    # Because inputs are read in as strings, there is no need for try except.
    # Instead, I will validate the guess by making sure it's only alphabet characters and 5 letters long
    # I will also compare it with a list of previous guesses from main,py
    while valid == False:
        guess = input("Enter a five letter word: ")
        if guess.upper() in previous_guesses:
            print("You must enter a new guess")
        elif len(guess) == 5 and guess.isalpha():
            valid = True
            break
        else:
            print("Enter a valid, 5 letter word")
    return (guess)

# evaluate_guess() – Compares the guess with the secret word and returns feedback.
def evaluate_guess(guess, secret_word):
    feedback = ["-"] * 5
    guess = guess.upper()
    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback[i] = "G"
        elif guess[i] in secret_word:
            feedback[i] = "Y"
    return "".join(feedback)


# display_guess() – Displays the guess and its feedback.
def display_guess(guess, feedback):
    guess = guess.upper()
    print(f"Your guess:   {guess[0]} {guess[1]} {guess[2]} {guess[3]} {guess[4]}")
    print(f"Feedback:     {feedback[0]} {feedback[1]} {feedback[2]} {feedback[3]} {feedback[4]}")

# has_won() – Determines whether the player has guessed the word.
def has_won(guess, secret_word):
    if guess.upper() == secret_word:
        player_wins = True
    else:
        player_wins = False
    return(player_wins)
