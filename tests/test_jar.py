import pytest

from week_eight_oops.jar import *

def test_init():
    jar = Jar()  # default capacity
    assert jar.capacity == 12
    jar = Jar(5)
    assert jar.capacity == 5
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("hello")
    with pytest.raises(ValueError):
        Jar(3.5)

def test_str():
    jar = Jar()
    assert str(jar) == ""  # empty jar
    jar.deposit(1)
    assert str(jar) == "🍪"  # one cookie
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"  # full jar

def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(11)
    assert jar.size == 11
    jar.deposit(1)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(11)
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(11)


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(10)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(4)