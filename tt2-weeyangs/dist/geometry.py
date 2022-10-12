"""
CS121 Team Tutorial 2: Functions
"""

import math

def dist_to_origin(p):
    """
    Find the distance from a point to the origin

    Input:
      p (tuple): a point in two dimensions

    Returns (float): The distance between p and the origin
    """
    (x, y) = p
    return math.sqrt((x * x) + (y * y))

# Add your distance function here
def dist_two_points(p,q):
    """
    Find the distance from between 2 points

    Input:
      p (tuple): a point in two dimensions
      q (tuple): a point in two dimensions

    Returns (float): The distance between p and q
    """
    (x1, y1) = p
    (x2, y2) = q
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Add your perimeter function here
def perimeter(p,q,r):
    """
    Find the perimeter of the triangle with 3 points

    Input:
      p (tuple): a point in two dimensions
      q (tuple): a point in two dimensions
      r (tuple): a point in two dimensions

    Returns (float): The total perimeter of p, q and r
    """
    totalperimeter = dist_two_points(p,q) + dist_two_points(q,r) + dist_two_points(r,p)

    return totalperimeter

def go():
    '''
    Write a small amount of code to verify that your functions work

    Verify that the distance between the points (0, 1) and (1, 0) is
    close to math.sqrt(2)

    After that is done, verify that the triangle with vertices at
    (0, 0), (0, 1), (1, 0) has a perimeter 2 + math.sqrt(2)
    '''

    s = "The distance between {} and the origin is: {:f}"
    p = (1, 0)
    print(s.format(p, dist_to_origin(p)))

    p = (1, 1)
    print(s.format(p, dist_to_origin(p)))

    # Add your tests here

if __name__ == "__main__":
    go()
