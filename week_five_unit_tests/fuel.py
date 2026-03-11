#In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3,
# restructuring your code per the below, wherein:

# convert expects a str in X/Y format as input, wherein X is a non-negative integer and Y is a
# positive integer, and returns that fraction as a percentage rounded to the nearest int between 0
# and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert
# should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
# gauge expects an int and returns a str that is:
# "E" if that int is less than or equal to 1,
# "F" if that int is greater than or equal to 99,
# and "Z%" otherwise, wherein Z is that same int.
# def convert(fraction):
#     ...
# def gauge(percentage):
#     ...
# Then, in a file called test_fuel.py, implement two or more functions that collectively
# test your implementations of convert and gauge thoroughly, each of whose names should begin
# with test_ so that you can execute your tests with:

def get_fuel():
    fraction = input("Enter the fraction in X/Y format: ")
    return fraction

def convert(fraction):
    try:
        a, b = fraction.strip().split("/")
        a, b = int(a), int(b)
        if b == 0:
            raise ZeroDivisionError
        if a > b:
            raise ValueError
        return round((a / b) * 100)
    except (ValueError, ZeroDivisionError):
        raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    percentage = convert(get_fuel())
    print(gauge(percentage))

if __name__ == "__main__":
    main()