# Ask her if it's bedtime
# If not, then just have her tell me when it's bedtime
# If it's bedtime, tell her the thing.
# Ask her how beautiful she is on a scale of 1-10
# I think you're the most beautiful woman in the whole wide universe :)

import time

def check_time():
    time_now = input("\nWhat time is it? Enter \"bedtime\" or \"not bedtime\": ")

    if time_now == "bedtime":
        print("\nYay!! It's bedtime!")
        bedtime = True
    elif time_now == "not bedtime":
        print("\nWake me up when it's bedtime *snooze, snore, snooze, sleeptalk*")
        bedtime = False
    else:
        print("\nEnter a valid guess bubba!")
        bedtime = False

    return(bedtime)

while True:
    if check_time() == True:
        break
    else:
        continue

print("\nI just want you to know before you go to bed...")
time.sleep(3)
print("\nThat I love you so much...")
time.sleep(3)
print("\nI love you more than any movie or TV show...")
time.sleep(3)
print("\nI love you more than our retiring savings account...")
time.sleep(3)
print("\nI love you more than the bad days, and the disagreements, and...")
time.sleep(3)
print("\nI...")
time.sleep(1)
print("\nalways...")
time.sleep(1)
print("\nwill :)")
time.sleep(3)

guess = input("\nHow beautiful would you say you are 1-10? be honest, I'm watching. ")
time.sleep(2)
print(f"\nThat's crazy!...I was going to say you're at least {guess}.5 :)")
print()
