from week_five_unit_tests import plates
from week_five_unit_tests.plates import is_valid

def test_valid():
    assert is_valid('CS50') == True

def test_invalid_length():
    assert is_valid('OUTATIME') == False

def test_invalid_text():
    assert is_valid('CS05') == False
    assert is_valid('CS50P') == False
    assert is_valid('H') == False

def test_invalid_characters():
    assert is_valid('P13.14') == False