#In a file called game.py, implement a program that:
# Prompts the user for a level, 𝑛. If the user does not input a positive integer,
# the program should prompt again.
# Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer,
# the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.

import random

def generate_random():
    while True:
        try:
            n = int(input("Level:"))
            if n > 0 :
                return random.randint(1, n)
        except ValueError:
            pass


def guess_random_number(n):
    while True:
        try:
            guess = int(input("Guess:"))
            if guess > 0:
                if guess < n:
                    print("Too small!!")
                elif guess > n:
                    print("Too large!!")
                else:
                    print("Just right!")
                    return
        except ValueError:
            pass


def main():
    guess_random_number(generate_random())

if __name__ == "__main__":
    main()