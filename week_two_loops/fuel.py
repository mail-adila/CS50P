# 03/02/2026

# Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
# For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full,
# and 3/4 indicates that a tank is 75% full.
# In a file called fuel.py, implement a program that prompts the user for a fraction,
# formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer,
# and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
# (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def get_percentage():
    while True:
        try:
            fraction = input("Enter the fraction in X/Y format: ")
            a, b = fraction.strip().split("/")
            if a > b or b == 0:
                continue
            percentage_value = (int(a) / int(b)) * 100
            return percentage_value
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def main():
    tank = get_percentage()
    if tank <= 1 :
        print("E")
    elif tank >= 99:
        print("F")
    else:
        print(f"{round(tank)}%")


if __name__ == "__main__":
    main()