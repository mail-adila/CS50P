from week_five_unit_tests.fuel import convert
from week_five_unit_tests.fuel import gauge

def test_convert_positive():
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_convert_negative():
    assert convert("-4/4") == -100

def test_gauge_negative():
    assert gauge(-100) == 'E'
    assert gauge(0) == 'E'

def test_gauge_positive():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'