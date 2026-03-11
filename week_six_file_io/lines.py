#Even so, in a file called lines.py, implement a program that expects exactly one
# command-line argument, the name (or path) of a Python file, and outputs the number of lines
# of code in that file, excluding comments and blank lines. If the user does not specify exactly
# one command-line argument, or if the specified file’s name does not end in .py, or if the
# specified file does not exist, the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
# (A docstring should not be considered a comment.) Assume that any line that only
# contains whitespace is blank.
import sys

def get_filename():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not filename.endswith(".py"):
            sys.exit("Not a python file")
        return filename
    if len(sys.argv) > 2:
        sys.exit("Too many arguments")
    else:
        sys.exit("Too few arguments")

def get_lines_of(file):
    try:
        with open(file) as f:
            lines = f.readlines()
        line_counter = 0
        for line in lines:
            if not line.strip().startswith("#") and len(line.strip()) != 0:
                line_counter += 1
        return line_counter
    except FileNotFoundError:
        sys.exit("File doesn't exist")

def main():
    file = get_filename()
    print(get_lines_of(file))

if __name__ == "__main__":
    main()

