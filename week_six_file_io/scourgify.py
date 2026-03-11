#In a file called scourgify.py, implement a program that:
# Expects the user to provide two command-line arguments:
# the name of an existing CSV file to read as input, whose columns are assumed to be, in order,
# name and house, and the name of a new CSV to write as output, whose columns should be, in order,
# first, last, and house.Converts that input to that output, splitting each name into a first name
# and last name. Assume that each student will have both a first name and last name.
# If the user does not provide exactly two command-line arguments, or if the first cannot be read,
# the program should exit via sys.exit with an error message.
# Hints
# Note that csv module comes with quite a few methods, per docs.python.org/3/library/csv.html,
# among which are DictReader, per docs.python.org/3/library/csv.html#csv.DictReader and DictWriter,
# per docs.python.org/3/library/csv.html#csv.DictWriter.
# Note that you can tell a DictWriter to write its fieldnames to a file using writeheader with no arguments,
# per docs.python.org/3/library/csv.html#csv.DictWriter.writeheader.
import sys
import csv

def get_file_names():
    if len(sys.argv) == 3:
        if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
            sys.exit("Not a csv file")
        return sys.argv[1], sys.argv[2]
    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")
    else:
        sys.exit("Too many arguments")

def write_file(file_to_read, file_to_write):
    try:
        with open(file_to_read, "r") as csvfile, open(file_to_write, "w", newline="") as csv_write_file:
            reader = csv.DictReader(csvfile)
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(csv_write_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                lname, fname = row["name"].split(", ")   # ← space, not comma
                writer.writerow({"first": fname, "last": lname, "house": row["house"]})
    except FileNotFoundError:
        sys.exit("File not found")
    except OSError:
        sys.exit(f"File could not be read: {file_to_read}")

def main():
    file_to_read, file_to_write = get_file_names()
    write_file(file_to_read, file_to_write)

if __name__ == "__main__":
    main()