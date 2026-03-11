# FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for
# making large letters out of ordinary text, a form of ASCII art:
#  _ _ _          _   _     _
# | (_) | _____  | |_| |__ (_)___
# | | | |/ / _ \ | __| '_ \| / __|
# | | |   <  __/ | |_| | | | \__ \
# |_|_|_|\_\___|  \__|_| |_|_|___/
# Among the fonts supported by FIGlet are those at figlet.org/examples.html.
# FIGlet has since been ported to Python as a module called pyfiglet.
# In a file called figlet.py, implement a program that:
# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should
# be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
#
# Hints
# from pyfiglet import Figlet
# figlet = Figlet()
# You can then get a list of available fonts with code like this:
# figlet.getFonts()
# You can set the font with code like this, wherein f is the font’s name as a str:
# figlet.setFont(font=f)
# And you can output text in that font with code like this, wherein s is that text as a str:
# print(figlet.renderText(s))
# Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

def text_in_font(text):
    selected_font = get_font()
    figlet.setFont(font=selected_font)
    print(figlet.renderText(text))

def get_font():
    if len(sys.argv) == 1:
        return random.choice(figlet.getFonts())
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] in figlet.getFonts():
            return sys.argv[2]
        else:
            sys.exit("The provided font is not recognized")
    else:
        sys.exit("Arguments provided not valid")

def main():
    text = input("Enter a string: ")
    text_in_font(text)

main()
