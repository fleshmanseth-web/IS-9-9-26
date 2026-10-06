import time

def type_text(message, delay=0.07):
    for letter in message:
        print(letter, end = "", flush=True)
        time.sleep(delay)

numbers = [17, 11, 38, 2019, -8]

for i in range(len(numbers)):
    type_text(str(numbers[i]))
    print()

word = input("What word would you like to analyze? ")

num_vowels = 0
num_letters = 0

for letter in word:
    if letter in ["a", "e", "i", "o", "u"]:
        num_vowels += 1
        num_letters += 1
    else:
        num_letters += 1

print(str(num_letters) + " " + str(num_vowels))