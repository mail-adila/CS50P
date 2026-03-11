# In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2,
# restructuring your code per the below, wherein shorten expects a str as input and returns
# that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
# def main():
#     ...
# def shorten(word):
#     ...
# if __name__ == "__main__":
#     main()
# Then, in a file called test_twttr.py, implement one or more functions that collectively test your
# implementation of shorten thoroughly, each of whose names should begin with test_ so that you
# can execute your tests with:
#
# pytest test_twttr.py
import sys


def main():
    text = get_text()
    print(f"{shorten(text)}")

def get_text():
    try:
        text = input("Enter your text: ").strip()
    except ValueError:
        sys.exit("Your text is invalid")
    return text

def shorten(word):
    vowels = "aeiouAEIOU"
    without_vowels = ""
    for character in word:
        if not character in vowels:
            without_vowels += character
    return without_vowels

if __name__ == "__main__":
    main()