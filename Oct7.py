import time
import turtle
from Oct7_2ndFile import is_odd_sidebar
from Oct7_2ndFile import type_text

numbers = [1, 3, 2, 4, 5]
#This sets a variable as global for this class
blah = 25
type_text("Hello")

def is_even(numero):
    # Allows me to access this variable outside of the function
    global even
    if numero % 2 == 0:
        even = True
    else:
        even = False

    #Allows blah to be accessible inside the function
    global blah
    blah += 1
    print(blah)

    return even

for i in numbers:
    if is_even(i) == True:
        print(f"{i} is even.")
    else:
        print(f"{i} is odd.")

for i in numbers:
    print(str(is_odd_sidebar(i)))

picture = [
    [0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0],
    [0, 0, 2, 2, 1, 1, 2, 1, 1, 2, 2, 0, 0],
    [0, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 0],
    [0, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 0],
    [2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2],
    [2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2],
    [2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2],
    [0, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 0],
    [0, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 0],
    [0, 0, 2, 2, 1, 1, 2, 1, 1, 2, 2, 0, 0],
    [0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0],
]

for row in picture:
    for pixel in row:
        if pixel == 1:
            print("🟧", end="")
        elif pixel == 2:
            print("⬛", end="")
        else:
            print("⬜", end="")
    print()

#lambda function
is_odd = lambda numero: numero % 2 != 0

for i in numbers:
    print(str(is_odd(i)))

pen = turtle.Turtle()
pen.speed(0)
turtle.bgcolor("black")

colors = ["cyan", "magenta", "yellow", "lime"]

for step in range(200):
    pen.color(colors[step % 4])
    pen.forward(step * 2)
    pen.right(91)

turtle.done()