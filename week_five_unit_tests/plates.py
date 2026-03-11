#In a file called plates.py, reimplement Vanity Plates from Problem Set 2,
# restructuring your code per the below, wherein is_valid still expects a str as
# input and returns True if that str meets all requirements and False if it does not,
# but main is only called if the value of __name__ is "__main__":
# def main():
#     ...
# def is_valid(s):
#     ...
# Then, in a file called test_plates.py, implement four or more functions that collectively
# test your implementation of is_valid thoroughly, each of whose names should begin with test_
# so that you can execute your tests with:
# pytest test_plates.py
def main():
    if is_valid(get_plate()):
        print("Plate is valid")
    else:
        print("Plate is not valid")

def get_plate():
    plate = input("Enter your plate: ").strip()
    return plate

def is_valid(plate_number):
    if (len(plate_number) < 2 or len(plate_number) > 6) or (not plate_number.isalnum()):
        return False
    if (not plate_number[0].isalpha()) or (not plate_number[1].isalpha()):
        return False
    found_number = False
    for char in plate_number:
        if char.isdigit():
            if not found_number:
                # this is the first number
                if char == "0":
                    return False
                found_number = True
        else:
            if found_number:
                # letter AFTER number → invalid
                return False
    return True

if __name__ == "__main__":
    main()