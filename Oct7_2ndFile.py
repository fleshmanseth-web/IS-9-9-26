import time

def is_odd_sidebar(numero):
    if numero % 2 == 0:
        odd = False
    else:
        odd = True

    return odd

def type_text(message, delay=0.05):
# define type_text (function) is a function of message (variable) and delay (integer, which is set)
    for letter in message:
        print(letter, end="", flush=True) 
        #commas allow you to add multiple things in a string and use keyword settings. + is mostly for saving a variable because commas only act as glue in functions like print, and if you want stuff to touch
        #flush = true forces the terminal to display the text immediately instead of delaying it until you are on a new line, making the typewriter effect work
        time.sleep(delay)
