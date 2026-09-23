#Remember, you start counting at 0

#Create an array of numbers, and a variable to count
#how many of each type there are
nums = [5, 0, 11, -12, 15]
negs = 0
pos = 0
zeros = 0

#For each number in the array, identify the type and
#increment that category
for i in nums:
    if i == 0:
        print("That's a zero.")
        zeros += 1
    elif i > 0:
        print("That's a positive number!")
        pos += 1
    elif i < 0:
        print("That's a negative number!")
        negs += 1

#Print out the results
print(f"Zeros: {zeros}")
print(f"Negative numbers: {negs}")
print(f"Positive numbers: {pos}")