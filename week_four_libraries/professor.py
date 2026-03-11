# In a file called professor.py, implement a program that:
# Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a
# non-negative integer with 𝑛 digits. No need to support operations other than addition (+).
# Note: The order in which you generate x and y matters. Your program should generate random
# numbers in x, y pairs to simulate generating one math question at a time (e.g., x0 with y0,
# x1 with y1, and so on).
#
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
# the program should output EEE and prompt the user again, allowing the user up to three tries in
# total for that problem. If the user has still not answered correctly after three tries, the program
# should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.
# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the
# user for a level and returns 1, 2, or 3, and generate_integer returns a single randomly generated
# non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
import random

def get_level():
    while True:
        try:
            level = int(input("Level:"))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(number_of_digits):
    if number_of_digits == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif number_of_digits == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x,y

def ask_questions():
    q_no = 0
    score = 0
    level = get_level() #1
    for _ in range(10):
        a, b = generate_integer(level) # 7,0
        for tries in range(3):
            try:
                answer = int(input(f"{a} + {b} = "))
                if answer == a+b:
                    score += 1
                    break # breaks after correct answer
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else: # will reach here only when tries = 3
            print(f"{a} + {b} = {a+b}")
    print(f"Score : {score}")


def main():
    ask_questions()

if __name__ == "__main__":
    main()
