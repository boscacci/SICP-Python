# Exercise 1.3.
# Define a procedure that takes three numbers as arguments and returns
# the sum of the squares of the two larger numbers.


def sum_squares_of_bigger_2(x, y, z):
    sorted_list = sorted([x, y, z])  # Get them in an ordered list
    squares = [n ** 2 for n in sorted_list[1:]]  # Skip item 0, square each
    return sum(squares)  # Add em up


def sum_squares_of_bigger_2_alt(x, y, z):
    """Performs same function but with only conditionals
    """
    if x < y and x < z:
        return y ** 2 + z ** 2
    elif y < x and y < z:
        return x ** 2 + z ** 2
    else:
        return x ** 2 + y ** 2

