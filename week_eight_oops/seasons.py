# In a file called seasons.py, implement a program that prompts the user for their date of birth
# in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest
# integer, using English words instead of numerals, just like the song from Rent, without any
# and between words. Since a user might not know the time at which they were born, assume,
# for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date.
# And assume that the current time is also midnight. In other words, even if the user
# runs the program at noon, assume that it’s actually midnight, on the same date.
# Use datetime.date.today to get today’s date, per
# docs.python.org/3/library/datetime.html#datetime.date.today.
import sys
from datetime import date, datetime
import inflect

p = inflect.engine()


def main():
    birth_date = get_input()
    calculate_minutes(birth_date)

def get_input():
    bdate = input("Date of birth: ")
    try:
        return date.fromisoformat(bdate)
    except ValueError:
        sys.exit("Invalid date")

def calculate_minutes(bdate):
    delta = date.today() - bdate
    minutes = delta.days * 1440
    print(p.number_to_words(minutes, andword="").capitalize())


if __name__ == "__main__":
    main()