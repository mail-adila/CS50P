# Suppose that you’d like to implement a cookie jar in which to store cookies.
# In a file called jar.py, implement a class called Jar with these methods:
# __init__ should initialize a cookie jar with the given capacity,
# which represents the maximum number of cookies that can fit in the cookie jar.
# If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
# __str__ should return a str with 𝑛 🍪, where 𝑛 is the number of cookies in the cookie jar.
# For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
# deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie
# jar’s capacity, though, deposit should instead raise a ValueError.
# withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that
# many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
# capacity should return the cookie jar’s capacity.
# size should return the number of cookies actually in the cookie jar, initially 0.
#Structure your class per the below. You may not alter these methods’ parameters,
# but you may add your own methods.

# Note that it’s not as easy to test instance methods as it is to test functions alone,
# since instance methods sometimes manipulate the same “state” (i.e., instance variables).
# To test one method (e.g., withdraw), then, you might need to call another method first (e.g., deposit).
# But the method you call first might itself not be correct!
# And so programmers sometimes mock (i.e., simulate) state when testing methods,
# as with Python’s own mock object library, so that you can call just the one method but
# modify the underlying state first, without calling the other method to do so.

class Jar:
    def __init__(self, capacity=12):
        self.n = 0
        if not isinstance(capacity, int) or  capacity < 0:
            raise ValueError('Capacity exceeded')
        self._capacity = capacity

    def __str__(self):
        return "🍪"* self.n

    def deposit(self, n):
        if self.n + n > self.capacity:
            raise ValueError('Capacity exceeded')
        self.n += n

    def withdraw(self, n):
        if n > self.n:
            raise ValueError('Capacity exceeded')
        self.n -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.n


def main():
    jar = Jar(5)
    print(jar)

if __name__ == '__main__':
    main()