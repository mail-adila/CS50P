from week_five_unit_tests import bank
from week_five_unit_tests.bank import value

def test_positive_greeting():
    assert value("hello") == 0

def test_positive_starting():
    assert value("hey") == 20
    assert value("Harry potter") == 20
    assert value("hhhhhh") == 20

def test_negative_greeting():
    assert value("good morning") == 100
    assert value("adila") == 100
    assert value("random greeting") == 100