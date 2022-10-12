"""
CS121 Team Tutorial 2: Functions
"""

def count_twos(lst):
    """
    Count the number of twos in a list

    Input:
       lst (list): the list

    Returns (int): The number of twos in lst
    """
    count = 0
    for item in lst:
        if item == 2:
            count = count + 1
    return count

# Add your are_any_true function here
def are_any_true(lst):
    """
    Checks if at least one entry in a list is True

    Input:
       lst (list): the list

    Returns (bool): True if there is a True
    """
    for item in lst:
        if item:
            return True
    
    return False

# Add your add_lists function here
def add_lists(a, b):
    """
    Adds items in two lists of the same length 

    Input:
       lst1 (list): first list
       lst2 (list): second list

    Returns (lst): A new list
    """
    assert len(a) == len(b), "Lists must be the same length"
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])

    return c


# Add your add_one function here
def add_one(lst):
    """
    Adds 1 to each item in the list

    Input:
       lst (list): the list

    Returns (None): Modifies the list passed into parameter
    """
    for i in range(len(lst)):
        lst[i] = lst[i] + 1

    return None    

def go():
    '''
    Write code to verify that your functions work as expected here.
    Try to think of a few good examples to test your work.
    '''

    lst1 = [1, 2, 1, 0, 2, 0, 2]
    lst2 = [1, 1, 1, 0, 2, 0, 0]
    print(count_twos(lst1))
    print(count_twos(lst2))

    # Add your tests here

if __name__ == "__main__":
    go()
