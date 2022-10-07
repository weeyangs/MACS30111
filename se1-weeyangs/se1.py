"""
Short Exericses #1
"""


def add_one_and_multiply(a, x):
    """ Add 1 to a, and multiply by x"""

    ### EXERCISE 1 -- YOUR CODE GOES HERE
    # Replace "None" with the correct expression
    r = (a+1)*x

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return r


def out_of_range(x, lb, ub):
    """ Is x outside the range lb to ub (inclusive)?"""

    ### EXERCISE 2 -- YOUR CODE GOES HERE
    # Replace "None" with the correct expression
    r = True
    lowerlimit = lb
    upperlimit = ub
    if lb > ub:
        lowerlimit = ub
        upperlimit = lb
    if x >= lowerlimit and x <= upperlimit:
        r = False

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return r


def number_string(x):
    """
    Given a number x, produce a string: "POSITIVE", "NEGATIVE", "ZERO"
    (depending on whether the number is positive, negative, or zero)
    """

    ### EXERCISE 3 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable s should contain the value
    # we ask you to compute in this exercise.
    s = None
    if x > 0:
        s = "POSITIVE"
    if x == 0:
        s = "ZERO"
    if x < 0:
        s = "NEGATIVE"

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return s


def num_divisible(lb, ub, p, q):
    """
    How many numbers between lb and ub (inclusive) are divisible by p
    or divisible by q, but not divisible by both p and q.
    """

    ### EXERCISE 4 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable n should contain the value
    # we ask you to compute in this exercise.
    n = 0
    lowerlimit = lb
    upperlimit = ub
    if lb > ub:
        lowerlimit = ub
        upperlimit = lb
    for i in range(lowerlimit,upperlimit + 1):
        if (i % q == 0 or i % p == 0) and not (i % q == 0 and i % p == 0):
            n = n + 1
        
    ### DO NOT MODIFY THE FOLLOWING LINE!
    return n


def count_greater_than_val(lst, val):
    """
    Count the number of numbers in the list that are strictly greater than the value of val.
    """

    ### EXERCISE 5 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable n should contain the value
    # we ask you to compute in this exercise.
    n = 0
    for item in lst:
        if item > val:
            n = n + 1

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return n


def negate_list(lst):
    """
    Produce a *new* list with its values negated
    """

    ### EXERCISE 6 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable n should contain the value
    # we ask you to compute in this exercise
    new_lst = []
    for item in lst:
        new_lst.append(-item)

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return new_lst
