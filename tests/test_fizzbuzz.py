import pytest

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


# - Can I call FizzBuzz
# - Get "1" when pass in 1
# - Get "2" when pass in 2
# - Get "Fizz" when pass in 3
# - Get "Buzz" when pass in 5
# - Get "Fizz" when pass in 6 (multiple of 3)
# - Get "Buzz" when pass in 10 (multiple of 5)
# - Get "FizzBuzz" when pass in 15 (multiple of 3 and 5)