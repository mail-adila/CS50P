#Mini Challenge (Exceptions)
# Write a program that:
# Asks the user to enter a number
# Converts it to an integer
# Prints the number squared
# If the user enters something that cannot be converted to an integer, print: "That’s not a number!"
# The program should not crash if input is invalid

def get_number():
    while True:
        try:
            n = int(input("Enter a number: "))
            return n
        except ValueError:
            print("That's not a number")

def square_number(number):
        return number ** 2

def main():
    number = get_number()
    if number != 0:
        print(f"Square of {number} is {square_number(number)}")

if __name__ == "__main__":
    main()