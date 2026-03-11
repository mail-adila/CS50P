#In a file called working.py, implement a function called convert that expects a str in any
# of the 12-hour formats below and returns the corresponding str in 24-hour format
# (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein)
# and that there will be a space before each. Assume that these times are representative of
# actual times, not necessarily 9:00 AM and 5:00 PM specifically.

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM
# Raise a ValueError instead if the input to convert is not in either of those formats or if either
# time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start
# ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
#
# Structure working.py as follows, wherein you’re welcome to modify main and/or implement other
# functions as you see fit, but you may not import any other libraries. You’re welcome, but not
# required, to use re and/or sys.

import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    matches = re.fullmatch(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)",s.strip())
    print(matches.groups())
    if not matches:
        raise ValueError("Invalid format")

    h1, m1, p1, h2, m2, p2 = matches.groups()
    h1, h2 = int(h1), int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    if not 1 <= h1 <= 12 and not 1 <= h2 <= 12:
        raise ValueError("Invalid hour")
    if not 0 <= m1 <= 59 and not 1 <= m2 <= 59:
        raise ValueError("Invalid minutes")

    if p1 == "AM":
        h1 = 0 if h1 == 12 else h1
    else:
        h1 = 12 if h1 == 12 else h1 + 12

        # Convert end time
    if p2 == "AM":
        h2 = 0 if h2 == 12 else h2
    else:
        h2 = 12 if h2 == 12 else h2 + 12

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"



if __name__ == "__main__":
    main()