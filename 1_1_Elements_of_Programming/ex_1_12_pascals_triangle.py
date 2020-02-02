"""Exercise 1.12

The following pattern of numbers is called Pascal's triangle:

      1  
     1 1 
    1 2 1 
   1 3 3 1 
  1 4 6 4 1 
1 5 10 10 5 1 

The numbers at the edge of the triangle are all 1, and each number inside the 
triangle is the sum of the two numbers above it. Write a procedure that computes 
elements of Pascal's triangle by means of a recursive process.
"""

# My original answer:
def pascal(counter, triangle=None):
    if triangle == None:
        triangle = [[1]]
    if counter == 1:
        return triangle
    else:
        triangle.append(make_new_layer(triangle))
        return pascal(counter - 1, triangle)


# My original answer's helper function:
def make_new_layer(triangle):
    last_layer = triangle[-1]
    if last_layer == [1]:
        return [1, 1]
    else:
        new_layer = [1]
        for i in range(len(last_layer) - 1):
            new_element = last_layer[i] + last_layer[i + 1]
            new_layer.append(new_element)
        new_layer.append(1)
        return new_layer


assert pascal(1) == [[1]]
assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

# Real answer in Lisp:

"""
 (define (pascal r c) 
   (if (or (= c 1) (= c r)) 
       1 
       (+ (pascal (- r 1) (- c 1)) (pascal (- r 1) c))))
"""

# Python translation:
# I guess the question was just asking for "elements" and not the whole triangle.


def pascal_tri(r, c):
    """Calculates the value of Pascal's Triangle at row r column c.
    R and C are 1-indexed not zero-indexed.

    1  
    1 1 
    1 2 1 
    1 3 3 1 
    1 4 6 4 1
    1 5 10 10 5 1

    """
    if c == 1 or c == r:
        return 1
    else:
        return pascal_tri(r - 1, c - 1) + pascal_tri(r - 1, c)


assert pascal_tri(4, 3) == 3

