import random
import time

secret_number = random.randint(1, 10)

def type_text(message, delay=0.05):
    for letter in message:
        print(letter, end="", flush=True)
        time.sleep(delay)

while True: #While true will keep the loop running forever, because true is always true, unless there is a break.

    type_text("\nI'm thinking of a number between 1 and 10...can you guess what it is? :) ")
    guess = int(input())

    if guess < secret_number:
        type_text("Too low my friend, too low")
    elif guess > secret_number:
        type_text("Too high *chuckle* too high")
    else:
        type_text(f"That's crazy...no, yeah, because actually the number was {secret_number} and a half...but you still win :)")
        break





