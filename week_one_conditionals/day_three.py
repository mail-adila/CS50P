# 02/26/2026 - Thursday

# Deep Thought
# program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

def check_answer():
    answer = input("What is the the answer to the Great Question of Life, the Universe and Everything?")

    answer = answer.strip().lower()
    match answer:
        case '42' | 'forty-two' | 'forty two':
            print("Yes")
        case _:
            print("No")


# program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”),
# output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and
# treat the user’s greeting case-insensitively.

def check_greeting():
    greeting = input("Greeting:")
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

# implement a program that prompts the user for the name of a file and
# then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
# .gif    .jpg    .jpeg   .png    .pdf    .txt    .zip
# If the file’s name ends with some other suffix or has no suffix at all,
# output application/octet-stream instead, which is a common default.

def check_file_media_type():
    file_name = input("Enter the file name with the extension:")
    file_name = file_name.strip().lower()
    if '.' in file_name:
        extension = file_name.split(".")[-1]
        match extension:
            case 'gif' | 'png':
                print(f"image/{extension}")
            case 'jpg' | 'jpeg':
                print(f"image/jpeg")
            case 'pdf':
                print(f"application/{extension}")
            case 'txt':
                print(f"text/plain")
            case 'zip':
                print(f"application/zip")
            case _:
                print("application/octet-stream")
    else:
        print("application/octet-stream")


# implement a program that prompts the user for an arithmetic expression and
# then calculates and outputs the result as a floating-point value formatted to one decimal place.
# Assume that the user’s input will be formatted as x y z, with one space between x and y and
# one space between y and z, wherein:
# x is an integer   y is +, -, *, or /  z is an integer

def calculate():
    a, operator, b = input("Enter the arithmetic expression, formatted as x y z:").split()
    a = int(a)
    b = int(b)
    result = 0

    if operator == '+':
        result = (a + b)
    elif operator == '-':
        result = (a - b)
    elif operator == '*':
        result = (a * b)
    elif operator == '/' and b != 0:
        result = (a / b)

    print(f"{result:.1f}")

# Mini Challenge (Conditional Logic)
# Write a program that:
#   Asks user for a number
#   If the number is divisible by 3 → print “Fizz”
#   If divisible by 5 → print “Buzz”
#   If divisible by both 3 and 5 → print “FizzBuzz”
#   Otherwise → print the number

def fizz_buzz():
    number = int(input("Enter the number: "))

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else: print(number)


# Implement a program that prompts the user for a time and outputs whether it’s breakfast time,
# lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all.
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
# And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00,
# or anytime in between, it’s time for breakfast.
# Structure your program per the below, wherein convert is a function (that can be called by main)
# that converts time, a str in 24-hour format, to the corresponding number of hours as a float.
# For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes),
# convert should return 7.5 (i.e., 7.5 hours).
# def main():
#     ...
# def convert(time):
#     ...
# if __name__ == "__main__":
#     main()


def convert(time):
    hour, minute = map(int, time.strip().split(":"))
    return hour + minute/60

def main():
    input_time = input("Enter the time in 24 hour format as #:## or ##:##:")
    time_to_check = convert(input_time)
    if 7.0 <= time_to_check <= 8.0:
        print("Breakfast time!!")
    elif 12.0 <= time_to_check <= 13.0:
        print("Lunch Time!!")
    elif 18.0 <= time_to_check <= 19.0:
        print("Dinner Time!!")

if __name__ == "__main__":
    main()