"""Code in python for a Binary Search Tree"""

import time


def binary_search(sorted_array, requested_value):
    """
    arguments:
        sorted_array: list of sorted values to search through
    returns:
        True if value is found
        False if value is not found
    """
    if requested_value in sorted_array:
        return True
    else:
        return False
