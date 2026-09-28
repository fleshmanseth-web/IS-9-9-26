blah = [1, 7, 19, 22, 4, 11, 8, 32, 40, 5, 7]
odd_nums = 0
even_nums = 0

for number in blah:
    if number % 2 == 0:
        print(f"{number} is even")
        even_nums += 1
    else:
        print(f"{number} is odd")
        odd_nums += 1

print(f"Total even numbers: {even_nums}")
print(f"Total odd numbers: {odd_nums}")