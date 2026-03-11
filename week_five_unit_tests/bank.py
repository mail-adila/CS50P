#In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1,
# restructuring your code per the below, wherein value expects a str as input and returns an
# int, namely 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”),
# or 100 otherwise, treating the str case-insensitively. You can assume that the string passed
# to the value function will not contain any leading spaces. Only main should call print
# def main():
#     ...
# def value(greeting):
#     ...
# Then, in a file called .py, implement three or more functions that collectively
# test your implementation of value thoroughly, each of whose names should begin with test_ so
# that you can execute your tests with:

def get_input():
    greeting = input("Greeting:")
    return greeting


def value(greeting):
    g = greeting.strip().lower()
    if g.startswith("hello"):
        return 0
    elif g.startswith("h"):
        return 20
    else:
        return 100

def main():
    greeting = get_input()
    print(f"${str(value(greeting))}")

if __name__ == "__main__":
    main()