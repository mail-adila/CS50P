# 02/27/2026 Friday

# implement a program that prompts the user for the name of a variable in camel case
# and outputs the corresponding name in snake case. Assume that the user’s input will
# indeed be in camel case.

def change_to_snake_case(camel_case_name):
    snake_case = ""
    for character in camel_case_name:
        if character.isupper():
            snake_case += '_' + character.lower()
        else:
            snake_case += character
    return snake_case

# implement a program that prompts the user to insert a coin, one at a time,
# each time informing the user of the amount due. Once the user has inputted at least 50 cents,
# output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

def coin_change():
    sum_of_coins = 0
    while sum_of_coins < 50:
        print(f"Amount Due = {50 - sum_of_coins}")
        coin_amount = int(input("Insert Coin - 5c 10c or 25c: ")) #5

        if coin_amount in [5, 10, 25]:
            sum_of_coins += coin_amount #10

    print(f"Change owed = {sum_of_coins-50}")


# implement a program that prompts the user for a str of text and then outputs that same text
# but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def remove_vowels():
    vowels = "aeiouAEIOU"
    text = input("Enter your text: ").strip()
    without_vowels = ""
    for character in text:
        if not character in vowels:
            without_vowels += character
    print("Your text without vowels: ", without_vowels)


# implement a program that prompts the user for a vanity plate and then output Valid if
# meets all of the requirements or Invalid if it does not. Assume that any letters in the
# user’s input will be uppercase. Structure your program per the below, wherein is_valid
# returns True if s meets all requirements and False if it does not.
# Assume that s will be a str. You’re welcome to implement additional functions for
# is_valid to call (e.g., one function per requirement).
# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def validate_plate():
    plate = input("Enter your plate: ").strip()

    if len(plate) > 6 or len(plate) < 2:
        return False
    if not plate.isalnum():
        return False
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False
    found_number = False
    for char in plate:
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







def main():
    # change_to_snake_case
    # name = input("Enter the name in camel_case format : ")
    # print(f"Name in snake case is : {change_to_snake_case(name)}")

    #insert_coin
    #coin_change()
    #remove_vowels()
    # if validate_plate():
    #     plate = input("Valid Plate")
    # else:
    #     plate = input("Invalid Plate")
    pass




if __name__ == "__main__":
    main()