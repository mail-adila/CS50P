#In a file called pizza.py, implement a program that expects exactly one command-line argument,
# the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII
# art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the
# library’s grid format. If the user does not specify exactly one command-line argument, or if the
# specified file’s name does not end in .csv, or if the specified file does not exist, the program
# should instead exit via sys.exit.
import csv
import sys
from tabulate import tabulate

def get_file():
    if len(sys.argv) == 2:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a csv file")
        return sys.argv[1]
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    else:
        sys.exit("Too few arguments")

def print_pretty(file):
    try:
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file)
            print(tabulate(csv_reader, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found")

def main():
    csv_file = get_file()
    print_pretty(csv_file)

if __name__ == "__main__":
    main()