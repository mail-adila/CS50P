# In a file called numb3rs.py, implement a function called validate that expects an IPv4
# address as input as a str and then returns True or False, respectively, if that input is a
# valid IPv4 address or not.
# Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement
# other functions as you see fit, but you may not import any other libraries. You’re welcome,
# but not required, to use re and/or sys.
#
# def main():
#     print(validate(input("IPv4 Address: ")))

# def validate(ip):
#     ...
#
# if __name__ == "__main__":
#     main()
# Either before or after you implement validate in numb3rs.py, additionally implement,
# in a file called test_numb3rs.py, two or more functions that collectively test your
# implementation of validate thoroughly, each of whose names should begin with test_ so that
# you can execute your tests with:
#
# pytest test_numb3rs.py
import re

def get_input():
    ip = input("IPv4 address: ")
    return ip

def validate(ip):
    try:
        matches = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip)
        if not matches:
            return False
        for i in range(1,5):
            octet = matches.group(i)
            if len(octet) > 1 and  octet.startswith("0"):
                return False
            if not 0 <= int(octet) <= 255:
                return False
        return True
    except AttributeError:
        return False

def main():
    ip_address = get_input()
    print(validate(ip_address))

if __name__ == "__main__":
    main()
