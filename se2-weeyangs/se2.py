"""
MACS 30111/30121
Short Exercises #2
"""

def peep(p, e):
    """
    Determine whether or not peep = pp^e

    Inputs:
      p (int): first digit
      e (int): second digit

    Returns: True if peep = pp^e, False otherwise
    """
    
    ### EXERCISE 1 -- Replace pass with your code
    str_peep = str(p) + str(e) + str(e) + str(p)
    int_peep = int(str_peep)
    str_pp = str(p) + str(p)
    int_pp = int(str_pp)
    
    if int_peep == (int_pp ** e):
        return True
    else:
        return False

# helper function for EXERCISE 2
def count_val(lst, val):
    counter = 0
    
    for item in lst:
        if item == val:
            counter += 1
            
    return counter

def has_more(lst1, lst2, target):
    """
    Determine which list contains more of the target value

    Inputs:
      lst1 (list): first list
      lst2 (list): second list
      target: the target value

    Returns: True if lst1 contains more of target, False otherwise
    """

    ### EXERCISE 2 -- Replace pass with your code
    count_lst1 = count_val(lst1, target)
    count_lst2 = count_val(lst2, target)
    
    if count_lst1 > count_lst2:
        return True
    else:
        return False

# helper function for EXERCISE 3
def make_stars(int):
    """
    Turns integers into str of stars
    """
    
    str = ""
    for _ in range(0,int):
        str += "*"
    
    return str    
     

def make_star_strings(lst):
    """
    Create a list of star strings

    Input:
      lst (list of nonnegative integers): the list

    Returns: A list of strings of stars (*)
    """
    
    ### EXERCISE 3 -- Replace pass with your code
    newlst = []
    
    for val in lst:
        newlst.append(make_stars(val))
        
    return newlst

def replace(lst, replacee, replacer):
    """
    Replace one element in a list with another

    Input:
      lst (list): the list
      replacee: the element to replace
      replacer: the element to replace replacee with

    Returns: None, modifies lst in-place
    """

    ### EXERCISE 4 -- Replace pass with your code
    for index, value in enumerate(lst):
        if value == replacee:
            lst[index] = replacer
    
    return None

# helper functions for EXERCISE 5
def flip_row_columns(lst):
    """
    Takes a list and swaps around its row and columns
    """
    # create placeholder new list with number
    # of lists
    newlst = []
    for _ in range(0,len(lst[0])):
        newlst.append([])
    
    # populate newlst with oldlst
    # so that [0][1] = [1][0]
    
    for row_number, sublst in enumerate(lst):
        for i in range(0, len(sublst)):
            newlst[i].append(sublst[i])
    
    return newlst

def check_row(lst, val):
    """
    Checks whether there is a value in a single row that is a list of values
    Returns True if there is at least one instance of the target value
    """
    
    for item in lst:
        if item == val:
            return True

    return False

def check_grid(grid, val):
    """
    Checks a list of lists if it contains the target value in each row
    Returns True if there is at least one instance of the target value
    in each row
    """
    for list in grid:
        if not check_row(list, val):
            return False
    
    return True

def rows_and_columns_contain(lst, target):
    """
    Determines whether every row and every column of a list
      of lists contains a target value

    lst (list of lists): the list of lists
    target: the target value

    Returns: True if every row and every column of lst contains
      target, False otherwise
    """

    ### EXERCISE 5 -- Replace pass with your code
    
    # check if the grid fails the check rows test
    if not check_grid(lst, target):
        return False
    
    # then flips the columns and rows of the grid if it passes the first test
    flipped_lst = flip_row_columns(lst)
    if check_grid(flipped_lst, target):
        return True
    else: 
        return False
