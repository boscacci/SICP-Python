# Exercise 1.3.
# Define a procedure that takes three numbers as arguments and returns
# the sum of the squares of the two larger numbers.


def sum_squares_of_bigger_2(x, y, z):
    sorted_list = sorted([x, y, z])  # Get them in an ordered list
    squares = [n ** 2 for n in sorted_list[1:]]  # Skip #0 and square
    return sum(squares)  # Add em up
